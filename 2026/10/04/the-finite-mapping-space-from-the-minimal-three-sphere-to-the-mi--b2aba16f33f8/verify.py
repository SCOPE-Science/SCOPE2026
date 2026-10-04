#!/usr/bin/env python3
import itertools, json
from pathlib import Path

SRC_LEVEL = (0,0,1,1,2,2,3,3)
TGT_LEVEL = (0,0,1,1,2,2)


def leq_t(a,b):
    return a == b or TGT_LEVEL[a] < TGT_LEVEL[b]


def source_leq(i,j):
    return i == j or SRC_LEVEL[i] < SRC_LEVEL[j]


def monotone(f):
    return all((not source_leq(i,j)) or leq_t(f[i],f[j])
               for i in range(8) for j in range(8))


def enumerate_maps():
    # Lexicographic order on target-value 8-tuples, filtered exhaustively.
    return [f for f in itertools.product(range(6), repeat=8) if monotone(f)]


def map_leq(f,g):
    return all(leq_t(a,b) for a,b in zip(f,g))


def strict_masks(maps):
    n=len(maps)
    up=[0]*n; down=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            ij=map_leq(maps[i],maps[j]); ji=map_leq(maps[j],maps[i])
            if ij and ji:
                raise AssertionError('distinct maps equivalent in T0 mapping poset')
            if ij:
                up[i] |= 1<<j; down[j] |= 1<<i
            elif ji:
                up[j] |= 1<<i; down[i] |= 1<<j
    return up,down


def main():
    cert=json.loads(Path(__file__).with_name('DELETION_CERTIFICATE.json').read_text(encoding='utf-8'))
    maps=enumerate_maps()
    assert len(maps)==cert['map_count']==738
    # Exhaustiveness guard: every emitted tuple really is monotone and all 6^8 tuples were filtered.
    assert all(monotone(f) for f in maps)
    up,down=strict_masks(maps)
    alive=(1<<len(maps))-1
    up_count=down_count=0
    for step,e in enumerate(cert['deletions']):
        x=int(e['delete']); y=int(e['witness']); kind=e['kind']
        assert (alive>>x)&1, ('deleted point already absent',step,x)
        assert (alive>>y)&1, ('witness absent',step,y)
        if kind=='up':
            U=up[x]&alive
            assert (U>>y)&1, ('up witness is not strictly above',step,x,y)
            # y is the minimum of the current strict upper set of x.
            assert ((U & ~(1<<y)) & ~up[y]) == 0, ('not an up-beat point',step,x,y)
            up_count += 1
        elif kind=='down':
            D=down[x]&alive
            assert (D>>y)&1, ('down witness is not strictly below',step,x,y)
            # y is the maximum of the current strict lower set of x.
            assert ((D & ~(1<<y)) & ~down[y]) == 0, ('not a down-beat point',step,x,y)
            down_count += 1
        else:
            raise AssertionError(('bad deletion kind',kind))
        alive &= ~(1<<x)
    remaining=[i for i in range(len(maps)) if (alive>>i)&1]
    constants=[i for i,f in enumerate(maps) if len(set(f))==1]
    assert len(cert['deletions'])==732
    assert up_count==cert['up_deletions']==128
    assert down_count==cert['down_deletions']==604
    assert remaining==cert['remaining_map_indices']==constants
    assert len(remaining)==6
    assert [list(maps[i]) for i in remaining]==cert['remaining_maps']

    # Check that the six constant maps inherit exactly the target order X_2.
    by_value={maps[i][0]:i for i in remaining}
    assert set(by_value)==set(range(6))
    for a in range(6):
        for b in range(6):
            assert map_leq(maps[by_value[a]], maps[by_value[b]]) == leq_t(a,b)

    # Check that the terminal subposet has no beat points, so it is a core.
    remmask=alive
    for x in remaining:
        U=up[x]&remmask; D=down[x]&remmask
        has_up=False
        bits=U
        while bits:
            lsb=bits&-bits; y=lsb.bit_length()-1; bits-=lsb
            if ((U & ~(1<<y)) & ~up[y]) == 0:
                has_up=True; break
        has_down=False
        bits=D
        while bits:
            lsb=bits&-bits; y=lsb.bit_length()-1; bits-=lsb
            if ((D & ~(1<<y)) & ~down[y]) == 0:
                has_down=True; break
        assert not has_up and not has_down

    print(f'VERIFY_OK maps={len(maps)} deletions={len(cert["deletions"])} up={up_count} down={down_count} core={len(remaining)}')

if __name__=='__main__':
    main()
