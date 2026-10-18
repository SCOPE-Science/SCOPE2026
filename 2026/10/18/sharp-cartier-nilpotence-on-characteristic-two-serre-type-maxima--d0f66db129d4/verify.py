"""Exact finite checks for the Cartier transition and antipodal basis.
These tests support, but do not replace, the all-odd-n proof.
"""

def test(n):
    assert n >= 3 and n % 2 == 1
    m = (2**n+1)//3
    N=3*m
    g=3*(m-1)//2
    B={(i,j) for j in range(4) for i in range(2**n) if 4*i+m*j<=2*g-2}
    assert len(B)==g
    S={4*(i+1)+m*j:(i,j) for i,j in B}
    assert len(S)==g
    assert not set(S).intersection({N-t for t in S})
    missing=[t for t in range(1,(N-1)//2+1) if t not in S and N-t not in S]
    assert missing==[m],(n,missing)
    def cart(pair):
        i,j=pair
        if j==0:
            return ((i-1)//2,0) if i%2 else None
        if j==1:
            return (i//2+(m-1)//2,0) if i%2==0 else ((i-1)//2,2)
        if j==2:
            return ((i-1)//2,1) if i%2 else None
        raise ValueError('j out of range')
    for a in B:
        v=cart(a)
        t=4*(a[0]+1)+m*a[1]
        tt=(t+N*(t%2))//2
        assert (v is not None)==(tt in S),(n,a,tt)
        if v is not None:
            assert v in B
            assert 4*(v[0]+1)+m*v[1]==tt
    v=( (m-3)//2,1 )
    assert v in B
    for i in range(n-1):
        v=cart(v)
        assert v in B,(n,i,v)
    assert v==(0,0),(n,v)
    assert cart(v) is None
    if n>=5:
        v=((m-5)//2,1)
        for i in range(n-1):
            v=cart(v)
            assert v in B,(n,i,v)
        assert v==(2,0),(n,v)
        assert cart(v) is None
    cur=B.copy()
    ranks=[]
    for i in range(n):
        cur={cart(v) for v in cur if cart(v) is not None}
        ranks.append(len(cur))
    assert ranks[-1]==0
    assert ranks[-2]>=(2 if n>=5 else 1)
    print(f'n={n}: m={m}; genus={g}; rank(C)={ranks[0]}; '
          f'rank(C^(n-1))={ranks[-2]}; C^n=0; '
          f'unrepresented antipodal pair=({m},{2*m})')

if __name__=='__main__':
    for n in [3,5,7,9,11,13,15]:
        test(n)
    print('VERIFY_OK')
