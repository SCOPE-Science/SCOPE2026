"""Finite crosschecks for Serre-type curves over characteristic two.
The proof for all odd n is given in RESULT.md, not inferred from tests.
"""
def check(n):
    k=(n-3)//2
    m=(2**n+1)//3
    W=3*m-5
    B={(i,j) for j in range(3) for i in range((W-j*m)//4+1) if W>=j*m}
    assert len(B)==(2**n-2)//2
    def C(pair):
        i,j=pair
        if j==0:return ((i-1)//2,0) if i%2 else None
        if j==2:return ((i-1)//2,1) if i%2 else None
        return ((i-1)//2,2) if i%2 else ((i+m-1)//2,0)
    assert all(C(b) is None or C(b) in B for b in B)
    S=B
    for _ in range(n-1):S={C(b) for b in S if C(b) is not None}
    want={((2*4**r-2)//3,0) for r in range(k+1)}
    assert S==want,(n,S,want)
    assert not any(C(b) is not None for b in S)
    print(n,len(B),len(S), sorted(S))
if __name__=='__main__':
 for n in [3,5,7,9,11,13,15]:check(n)
 print('CARTIER_LAST_ITERATE_CHECKS_PASSED')
