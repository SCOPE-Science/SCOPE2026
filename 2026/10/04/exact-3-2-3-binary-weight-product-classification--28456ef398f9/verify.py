#!/usr/bin/env python3
def weight(n):
    return n.bit_count()

def main():
    bound = 2 ** (-13 + 4*2*3)
    assert bound == 2048
    admissible = []
    hits = []
    for u in range(1, 11):
        a = 1 + (1 << u)
        assert a % 2 == 1 and weight(a) == 2
        for v in range(1, 11):
            for w in range(v + 1, 11):
                b = 1 + (1 << v) + (1 << w)
                assert b % 2 == 1 and weight(b) == 3
                if a*b < bound:
                    row = (u,v,w,a,b,a*b,weight(a*b))
                    admissible.append(row)
                    if row[-1] == 3:
                        hits.append(row)
    assert len(admissible) == 119
    assert hits == [(1,1,2,3,7,21,3),(2,1,2,5,7,35,3)]

    direct = []
    for a in range(1, bound, 2):
        if weight(a) != 2:
            continue
        for b in range(1, bound, 2):
            if a*b >= bound:
                break
            if weight(b) == 3 and weight(a*b) == 3:
                direct.append((a,b,a*b))
    assert direct == [(3,7,21),(5,7,35)]
    assert bin(21) == "0b10101"
    assert bin(35) == "0b100011"
    print("VERIFY_OK")
    print("bound=2048")
    print("admissible_exponent_triples=119")
    print("solutions=[(3,7,21),(5,7,35)]")

if __name__ == "__main__":
    main()
