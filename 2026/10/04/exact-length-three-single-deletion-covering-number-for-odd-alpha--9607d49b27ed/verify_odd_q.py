#!/usr/bin/env python3
from itertools import combinations
from math import ceil

WITNESSES = {
    5: [(0,2,4),(1,3,4)],
    7: [(0,3,6),(0,2,4),(1,3,5),(1,4,6),(2,5,6)],
    9: [(0,3,5),(1,3,7),(1,5,8),(1,4,6),(0,2,6),(0,4,7),(2,4,8),(2,5,7),(3,6,8)],
    11: [(0,3,5),(0,2,7),(0,4,6),(0,8,10),(3,6,8),(1,6,9),(2,6,10),(1,3,7),(3,9,10),(1,4,8),(1,5,10),(2,4,9),(2,5,8),(4,7,10),(5,7,9)],
    13: [(0,3,5),(0,2,7),(0,4,9),(0,6,8),(0,10,12),(2,5,9),(2,4,10),(2,6,11),(2,8,12),(1,4,6),(4,8,11),(4,7,12),(3,6,10),(1,3,8),(5,8,10),(1,7,10),(5,7,11),(1,5,12),(1,9,11),(3,7,9),(3,11,12),(6,9,12)],
}

def dball(w):
    a,b,c=w
    return {(a,b),(a,c),(b,c)}

def leave(q):
    if q % 3 == 0:
        return {tuple(sorted((i,(i+1)%q))) for i in range(q)}, None
    n=q-1
    return {tuple(sorted((i,(i+1)%n))) for i in range(n)}, q-1

def code_from_blocks(q, blocks):
    L, isolated = leave(q)
    code=[]
    for x,y,z in blocks:
        code += [(x,y,z),(z,y,x)]
    if q % 3 == 0:
        for i in range(q):
            code.append((i,(i+1)%q,i))
    else:
        n=q-1
        for i in range(n):
            code.append((i,(i+1)%n,i))
        code.append((isolated,isolated,isolated))
    return code

def check_blocks(q, blocks):
    L,_=leave(q)
    expected={tuple(sorted(e)) for e in combinations(range(q),2)}-L
    seen=[]
    for t in blocks:
        assert len(set(t))==3
        for e in combinations(t,2):
            e=tuple(sorted(e))
            assert e in expected
            seen.append(e)
    assert len(seen)==len(set(seen))
    assert set(seen)==expected

def check_code(q, code):
    cov=set()
    for w in code:
        cov |= dball(w)
    assert cov == {(a,b) for a in range(q) for b in range(q)}
    assert len(code)==ceil(q*q/3)

def arithmetic():
    for q in range(3,1000,2):
        if q%3==0:
            if q==3:
                n=3
            else:
                b=q*(q-3)//6
                n=2*b+q
        else:
            b=(q-1)*(q-2)//6
            n=2*b+q
        assert n==ceil(q*q/3)

def main():
    code3=[(0,1,0),(1,2,1),(2,0,2)]
    check_code(3,code3)
    for q,blocks in WITNESSES.items():
        check_blocks(q,blocks)
        check_code(q,code_from_blocks(q,blocks))
    arithmetic()
    print('VERIFY_OK')

if __name__=='__main__':
    main()
