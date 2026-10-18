"""Finite-state independent checks for positive-multiple digit-sum spectra."""
from collections import deque

def reachability(b, r, cap):
    m=b**r+1
    todo=deque()
    seen=set()
    for d in range(1,b):
        if d<=cap:
            z=(d%m,d)
            if z not in seen:seen.add(z);todo.append(z)
    while todo:
        residue,weight=todo.popleft()
        for d in range(min(b-1,cap-weight)+1):
            z=((b*residue+d)%m,weight+d)
            if z not in seen:
                seen.add(z);todo.append(z)
    return {weight for residue,weight in seen if residue==0}

def expected(b,cap):
    return {s for s in range(1,cap+1) if s%2==0 or (b%2==0 and s>=b+1)}

def digit_sum(n,b):
    out=0
    while n:
        out+=n%b; n//=b
    return out

def odd_witness(b,r):
    J=1 if r==1 else 0
    return 1+sum(b**(r-1+2*r*j) for j in range(J,J+b))

def concat(x,y,b):
    shift=0
    z=x
    while z:
        shift+=1;z//=b
    return x+(b**(shift+1))*y

if __name__=='__main__':
    finite=0
    total_states=0
    for b in range(2,11):
      for r in range(1,6):
        if b**r+1>2200: continue
        cap=2*b+7
        have=reachability(b,r,cap)
        want=expected(b,cap)
        assert have==want,(b,r,sorted(want-have),sorted(have-want))
        finite+=1
    witnesses=0
    for b in range(2,15):
      for r in range(1,6):
        n=b**r+1
        E=odd_witness(b,r)
        assert E%n==0
        assert digit_sum(E,b)==b+1
        assert digit_sum(n,b)==2
        for i in range(1,6):
            x=n
            for _ in range(i-1): x=concat(x,n,b)
            assert x%n==0 and digit_sum(x,b)==2*i
            if b%2==0:
                y=concat(x,E,b)
                assert y%n==0 and digit_sum(y,b)==2*i+b+1
            witnesses+=1
    print('VERIFY_OK: exact finite automata for',finite,'(base, exponent) settings;')
    print('constructive witnesses for',witnesses,'settings/sums, all checked exactly')
