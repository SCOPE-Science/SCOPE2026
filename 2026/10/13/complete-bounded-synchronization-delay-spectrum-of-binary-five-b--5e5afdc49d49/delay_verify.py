"""Exhaustive finite block-code delay census, using graph DFS (stdlib only).

Run: python3 delay_verify.py [catalogue.csv]
All integers and bit strings are ordinary exact values.
"""
import itertools
import sys
from collections import Counter, defaultdict

N = 5
WORDS = [format(x, "05b") for x in range(32)]


def rotations(word):
    return sorted({word[i:] + word[:i] for i in range(N)})


def necklace_orbits():
    seen = set()
    orbits = []
    for word in WORDS:
        if word in seen:
            continue
        orbit = rotations(word)
        seen.update(orbit)
        if len(orbit) == N:
            orbits.append(orbit)
    return orbits


def false_phase_delay(code):
    """Least d>=1 such that no shifted parse has d consecutive codewords.

    None means unbounded; a cycle supplies arbitrarily long false parses.
    """
    in_code = set(code)
    max_edges = 0
    for r in range(1, N):
        edges = {
            left: [right for right in code if left[r:] + right[:r] in in_code]
            for left in code
        }
        colors = {word: 0 for word in code}
        depth = {}

        def visit(word):
            if colors[word] == 1:
                raise ValueError("periodic false parse")
            if colors[word] == 2:
                return depth[word]
            colors[word] = 1
            result = max((1 + visit(other) for other in edges[word]), default=0)
            colors[word] = 2
            depth[word] = result
            return result

        try:
            max_edges = max(max_edges, *(visit(word) for word in code))
        except ValueError:
            return None
    return max_edges + 1


def symmetry_orbit(code):
    output = set()
    for reverse in (False, True):
        for flip in (False, True):
            words = []
            for word in code:
                if reverse:
                    word = word[::-1]
                if flip:
                    word = "".join("1" if bit == "0" else "0" for bit in word)
                words.append(word)
            output.add(tuple(sorted(words)))
    return output


def run():
    orbits = necklace_orbits()
    assert len(orbits) == 6 and all(len(x) == N for x in orbits)
    found = {}
    totals = Counter()
    for choice in itertools.product(*orbits):
        code = tuple(sorted(choice))
        delay = false_phase_delay(code)
        totals[delay] += 1
        if delay is not None:
            found[code] = delay
    assert len(found) == 9204
    assert totals == Counter({None: 6421, 1: 86, 2: 5546, 3: 3116, 4: 456})
    orbit_counts = defaultdict(Counter)
    remaining = set(found)
    while remaining:
        code = min(remaining)
        orbit = symmetry_orbit(code)
        assert orbit <= remaining.union(set(found) - remaining)
        assert all(found[other] == found[code] for other in orbit)
        orbit_counts[found[code]][len(orbit)] += 1
        remaining -= orbit
    expected_orbits = {
        1: {2: 7, 4: 18},
        2: {2: 17, 4: 1378},
        3: {2: 10, 4: 774},
        4: {4: 114},
    }
    assert {d: dict(x) for d, x in orbit_counts.items()} == expected_orbits
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", encoding="utf-8", newline="\n") as stream:
            stream.write("codewords,delay\n")
            for code, delay in sorted(found.items()):
                stream.write('"' + ",".join(code) + '",' + str(delay) + "\n")
    print("primitive_orbits=6 assignments=15625 invalid=6421 delay1=86 delay2=5546 delay3=3116 delay4=456 accepted=9204")
    for d in sorted(orbit_counts):
        print("delay", d, "orbit_counts", dict(sorted(orbit_counts[d].items())))


if __name__ == "__main__":
    run()
