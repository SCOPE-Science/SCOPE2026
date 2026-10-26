"""Replay the equality-template classification and its natural symmetry orbits.

Run after the equality-pattern program: python3 verify_orbits.py rgs_output.txt
"""
import sys

OUTPUT = sys.argv[1] if len(sys.argv) > 1 else 'rgs_output.txt'
EXPECTED = {
    3: (203, 133, 3, {3: 1}, 1),
    4: (4140, 3690, 4, {2: 1, 3: 4, 4: 1}, 4),
    5: (115975, 113073, 6, {3: 1}, 1),
    6: (4213597, 4194600, 6, {2: 2, 3: 8, 4: 2}, 5),
}


def normalize(a, b):
    assignments = {}
    t = []
    for symbol in a + b:
        if symbol not in assignments:
            assignments[symbol] = str(len(assignments))
        t.append(assignments[symbol])
    n = len(a)
    return ''.join(t[:n]), ''.join(t[n:])


def orbit(a, b):
    return {normalize(*t) for t in ((a, b), (b, a),
            (a[::-1], b[::-1]), (b[::-1], a[::-1]))}


def main():
    patterns = {}
    sections = {}
    current = None
    for line in open(OUTPUT, encoding='utf-8'):
        a = line.split()
        if not a:
            continue
        if a[0] == 'N':
            current = int(a[1])
            sections[current] = (int(a[3]), int(a[5]), int(a[7]), int(a[9]))
            patterns[current] = []
        elif a[0] == 'PATTERN':
            patterns[current].append((a[1], a[2], int(a[4])))
    assert sorted(sections) == sorted(EXPECTED)
    for n, (bell, eligible, maximum, profile, number_orbits) in EXPECTED.items():
        assert sections[n][:3] == (bell, eligible, maximum)
        ps = patterns[n]
        assert len(ps) == sections[n][3]
        assert {s:sum(1 for _, _, t in ps if t == s) for s in profile} == profile
        assert all(len(set(a+b)) == s and normalize(a, b) == (a, b)
                   for a,b,s in ps)
        missing = {(a,b) for a,b,_ in ps}
        classes = []
        while missing:
            a,b = min(missing)
            orb = orbit(a,b)
            assert orb <= {(x,y) for x,y,_ in ps}
            missing -= orb
            classes.append((min(orb),len(orb)))
        assert len(classes) == number_orbits
        print('n=', n, 'max=', maximum,
              'support_profile=', dict(sorted(profile.items())),
              'orbits=', sorted(classes))
    print('ORBIT_VERIFY_OK')


if __name__ == '__main__':
    main()
