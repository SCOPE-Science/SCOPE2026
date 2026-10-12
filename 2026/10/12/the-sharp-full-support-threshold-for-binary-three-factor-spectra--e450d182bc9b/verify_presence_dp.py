#!/usr/bin/env python3
"""Finite exact certificate for the modal binary 3-factor support theorem.

No library dependencies. State (s, m): last two bits s in 0..3 and
bitset of observed triples m in 0..255. Initial states represent the four
length-two binary words exactly once. The update appends either bit.
"""

def profiles_through(max_n=50):
    current=[[0]*256 for _ in range(4)]
    for s in range(4):
        current[s][0]=1
    for n in range(3,max_n+1):
        following=[[0]*256 for _ in range(4)]
        for s in range(4):
            for mask,count in enumerate(current[s]):
                if count:
                    for b in (0,1):
                        tri=(s<<1)|b
                        following[tri&3][mask|(1<<tri)]+=count
        current=following
        counts=[sum(current[s][mask] for s in range(4)) for mask in range(256)]
        assert sum(counts)==(1<<n)
        yield n,counts


def main():
    import csv
    from pathlib import Path
    table=Path(__file__).with_name("finite_profiles_3_to_50.csv")
    with table.open(newline="", encoding="utf-8") as handle:
        expected=list(csv.DictReader(handle))
    assert len(expected)==48
    n13=None
    cert=[]
    for row,(n,counts) in zip(expected, profiles_through()):
        assert int(row["length"])==n
        full=counts[255]
        other=max(counts[:255])
        top=max(counts)
        winners=";".join(f"0x{m:02x}" for m,v in enumerate(counts) if v==top)
        assert int(row["full_support_count"])==full
        assert int(row["largest_proper_support_count"])==other
        assert int(row["maximum_fiber_size"])==top
        assert row["maximizing_support_masks_hex"]==winners
        if n==13:
            assert (top,full,other)==(989,934,989)
            assert [mask for mask in range(256) if counts[mask]==top]==[127,254]
        if 14<=n<=50:
            assert full>other, (n,full,other)
            cert.append((n,full,other))
        if n==14:
            assert (full,other)==(2632,2218)
        if n==18:
            assert (full,other)==(94884,40556)
    assert len(cert)==37
    print('CERTIFIED 14..50: unique full eight-triple support maximizes each exact fiber')
    print('13: 989 maximizing words for each mask 0x7f and 0xfe; full mask 934')
    print('14: 2632 versus best proper-support fiber 2218')
    print('50:',cert[-1])
    print('50-length table rows=',len(cert),'sum full counts=',sum(a for _,a,_ in cert))

if __name__=='__main__':
    main()
