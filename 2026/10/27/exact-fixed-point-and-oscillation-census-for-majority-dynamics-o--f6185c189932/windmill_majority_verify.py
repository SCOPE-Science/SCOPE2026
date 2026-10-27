"""Exact finite checks for synchronous majority on the clique windmill K_1 vee r K_3.
Uses only Python standard library. Runs exhaustively for r=1,...,5.
"""
from math import comb


def update_majority(state, r):
    """Direct update using adjacency lists, independent of the sector formula."""
    n=3*r+1
    h=state&1
    next_state=0
    for v in range(n):
        if v==0:
            neighbors=range(1,n)
            degree=3*r
        else:
            j=(v-1)//3
            base=1+3*j
            neighbors=(0,)+(tuple(w for w in range(base,base+3) if w!=v))
            degree=3
        ones=sum((state>>w)&1 for w in neighbors)
        bit=1 if 2*ones>degree else 0 if 2*ones<degree else (state>>v)&1
        next_state |=bit<<v
    return next_state


def update_sectors(state,r):
    """Equivalent local sector table for cross-checking."""
    h=state&1
    s=0; y=0
    for i in range(r):
        q=(state>>(1+3*i))&7
        k=q.bit_count()
        s+=k
        if h==0:
            q2=7 if k==3 else ((~q)&7 if k==2 else 0)
        else:
            q2=7 if k>=2 else ((~q)&7 if k==1 else 0)
        y|=q2<<(1+3*i)
    if 2*s>3*r or 2*s==3*r and h:y|=1
    return y


def formula(r):
    fixed=2*sum(comb(r,b) for b in range(r+1) if 2*b<=r)
    two=0
    for a in range(r+1):
        for b in range(r-a+1):
            if 2*(2*a+3*b)>3*r>2*(a+3*b):
                two+=comb(r,a)*comb(r-a,b)*3**a
    return fixed,two


def enumerate_states(r):
    fix=0;twos=0;max_depth=0
    for x in range(1<<(3*r+1)):
        y=update_majority(x,r)
        assert y==update_sectors(x,r),(r,x)
        z=update_majority(y,r)
        if x==y:fix+=1
        elif x!=y and z==x and (x&1)==0:
            twos+=1
            assert (y&1)==1
        cur=x;cur2=z;depth=0
        while cur!=cur2:
            depth+=1
            cur=update_majority(cur,r)
            cur2=update_majority(update_majority(cur,r),r)
            assert depth<=4,(r,x,depth)
        max_depth=max(max_depth,depth)
    return fix,twos,max_depth


def sharp_witness(r):
    # Bit patterns 3=011 (two ones), 1=001 (one one), 0=000.
    if r%2:
        triples=[3,1,1]
    else:
        triples=[3,3,1,0]
    while len(triples)<r:
        triples.extend([0,7])
    x=1
    for i,q in enumerate(triples):x|=q<<(1+3*i)
    cur=x
    for t in range(4):
        assert update_majority(update_majority(cur,r),r)!=cur,(r,t)
        cur=update_majority(cur,r)
    assert update_majority(update_majority(cur,r),r)==cur,r
    return x


if __name__=='__main__':
    for r in range(1,6):
        observed=enumerate_states(r)
        predicted=formula(r)
        assert observed[:2]==predicted,(r,observed,predicted)
        assert observed[2]==(1 if r==1 else 3 if r==2 else 4)
        print(f'r={r}: fixed={observed[0]}, two_cycles={observed[1]}, max_depth={observed[2]} PASS')
    for r in range(3,17):
        print('sharp_depth_4_witness',r,sharp_witness(r))
    for r in (6,7,8,10,20,50,100):
        print('formula',r,*formula(r))
    print('ALL_CHECKS_PASSED')
