#!/usr/bin/env python3
"""Independent 256-matrix inclusion-exclusion for the full 3-mer spectrum."""

def full_spectrum_by_inclusion_exclusion(n):
    assert n>=2
    total=0
    for forbidden in range(256):
        ways=[1]*4
        for _ in range(n-2):
            nxt=[0]*4
            for s,num in enumerate(ways):
                for bit in (0,1):
                    triple=(2*s)+bit
                    if not (forbidden>>triple)&1:
                        nxt[triple&3]+=num
            ways=nxt
        allowed=sum(ways)
        total+=(-1 if forbidden.bit_count()%2 else 1)*allowed
    return total


def main():
    known={13:934,14:2632,15:6890,16:17118,17:40908,18:94884,
           19:214956,20:477922,21:1046544,22:2263228,23:4843834,
           24:10277132,25:21645226}
    for n,value in known.items():
        actual=full_spectrum_by_inclusion_exclusion(n)
        assert value==actual,(n,value,actual)
    print('INCLUSION_EXCLUSION_OK', len(known), 'checks',
          'n=14',full_spectrum_by_inclusion_exclusion(14),
          'n=25',full_spectrum_by_inclusion_exclusion(25))

if __name__=='__main__':
    main()
