#!/usr/bin/env python3

def mat_from_bits(x,n):
    mask=(1<<n)-1
    return tuple((x>>(i*n))&mask for i in range(n))

def eye(n): return tuple(1<<i for i in range(n))
def zero(n): return (0,)*n

def add(A,B): return tuple(a^b for a,b in zip(A,B))

def mul(A,B):
    n=len(A); out=[]
    for row in A:
        v=0; k=0; t=row
        while t:
            if t&1: v ^= B[k]
            t >>= 1; k += 1
        out.append(v)
    return tuple(out)

def mpow(A,m):
    n=len(A); R=eye(n); X=A
    while m:
        if m&1: R=mul(R,X)
        X=mul(X,X); m//=2
    return R

def is_zero(A): return not any(A)

def rank2(A):
    rows=list(A); n=len(rows); r=0
    for c in range(n):
        p=next((i for i in range(r,n) if (rows[i]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(n):
            if i!=r and ((rows[i]>>c)&1): rows[i]^=rows[r]
        r+=1
    return r

def nil_index(A):
    n=len(A); P=eye(n)
    for r in range(1,n+1):
        P=mul(P,A)
        if is_zero(P): return r
    return None

def dual_mul(X,Y):
    A,B=X; C,D=Y
    return mul(A,C), add(mul(A,D),mul(B,C))

def dual_nil_index(A,B,limit):
    n=len(A); X=(A,B); P=(eye(n),zero(n))
    for k in range(1,limit+1):
        P=dual_mul(P,X)
        if is_zero(P[0]) and is_zero(P[1]): return k
    return None

def jordan_type(parts):
    n=sum(parts); rows=[0]*n; o=0
    for r in parts:
        for j in range(r-1): rows[o+j] |= 1<<(o+j+1)
        o+=r
    return tuple(rows)

def check_A(A,direct=True):
    n=len(A); r=nil_index(A); P=mpow(A,r-1); s=rank2(P)
    pred=(1<<(n*n))-(1<<(n*n-s*s)); got=0
    for bits in range(1<<(n*n)):
        B=mat_from_bits(bits,n)
        crit=not is_zero(mul(mul(P,B),P))
        got += crit
        if direct:
            idx=dual_nil_index(A,B,2*r)
            if (idx==2*r)!=crit:
                raise AssertionError(('criterion',n,r,s,bits,idx,crit))
    if got!=pred: raise AssertionError(('count',n,r,s,got,pred))
    return n,r,s,got,pred

def main():
    nil_As=[]
    for bits in range(1<<9):
        A=mat_from_bits(bits,3)
        if nil_index(A) is not None: nil_As.append(A)
    assert len(nil_As)==64
    by_rs={}
    for A in nil_As:
        n,r,s,got,pred=check_A(A,True)
        by_rs[(r,s)]=by_rs.get((r,s),0)+1
    print('M3_F2_nilpotent_A_count',len(nil_As))
    print('M3_F2_types_by_(r,s)',sorted(by_rs.items()))

    # Dimension four: exhaust every B for each Jordan type. Direct powers are
    # rechecked on a deterministic sample of 4096 B values per type; the exact
    # count itself is obtained by exhaustive evaluation of PBP over all 65536 B.
    for parts in ([4],[3,1],[2,2],[2,1,1],[1,1,1,1]):
        A=jordan_type(parts); n=len(A); r=nil_index(A); P=mpow(A,r-1); s=rank2(P)
        pred=(1<<(n*n))-(1<<(n*n-s*s)); got=0
        for bits in range(1<<(n*n)):
            B=mat_from_bits(bits,n)
            crit=not is_zero(mul(mul(P,B),P)); got+=crit
            if bits<4096:
                idx=dual_nil_index(A,B,2*r)
                if (idx==2*r)!=crit: raise AssertionError(('sample',parts,bits,idx,crit))
        assert got==pred
        print('M4_F2_type',parts,'r',r,'s',s,'maximal_count',got,'predicted',pred)
    print('VERIFY_OK')

if __name__=='__main__': main()
