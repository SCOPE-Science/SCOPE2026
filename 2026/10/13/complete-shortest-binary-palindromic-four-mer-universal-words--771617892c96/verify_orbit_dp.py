"""Separate orbit-prefix dynamic-programming certificate for four-mer palindrome covers.
Run: python3 verify_orbit_dp.py
The dynamic program NEVER checks all sixteen factors of a palindrome.
"""
from collections import defaultdict

EXPECTED = {
    '000010110011110011010000',
    '000011001011110100110000',
    '000011010011110010110000',
    '111100101100001101001111',
    '111100110100001011001111',
    '111101001100001100101111',
}

rep = {f'{v:04b}': min(f'{v:04b}', f'{v:04b}'[::-1]) for v in range(16)}
orbits = sorted(set(rep.values()))
assert len(orbits) == 10
bit = {key: (1 << orbits.index(rep[key])) for key in rep}
full_mask = (1 << len(orbits)) - 1

def run():
    # DP states consist of last three symbols, coverage mask, and prefix strings.
    # All 2^14 prefixes of length 14 occur exactly once in this DP.
    states = {(f'{i:03b}', 0): [f'{i:03b}'] for i in range(8)}
    for size in range(4, 15):
        nxt = defaultdict(list)
        for (tail,mask), strings in states.items():
            for letter in '01':
                four = tail + letter
                newmask = mask | bit[four]
                newtail = four[1:]
                for s in strings:
                    nxt[(newtail,newmask)].append(s+letter)
        states = nxt
        assert sum(map(len, states.values())) == 1 << size
    solutions = []
    for (tail,mask), strings in states.items():
        if mask != full_mask:
            continue
        for p in strings:
            if p[-4:] != p[-4:][::-1]:
                continue
            u = p[:12]
            assert p == (u+u[::-1])[:14]
            solutions.append(u+u[::-1])
    assert set(solutions) == EXPECTED
    assert len(solutions) == 6
    print('ORBIT_DP_OK states',len(states),'length14_prefixes',16384,'solutions',len(solutions))
    for word in sorted(solutions):
        print(word)

if __name__=='__main__':
    run()
