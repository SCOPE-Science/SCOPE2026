#!/usr/bin/env python3
"""Direct finite-field centralizer-rank enumeration for truncated tensor algebra units.
Only ordinary mathematical data; no special-purpose external libraries.
"""
from itertools import product
from collections import Counter


def add(a,b,q):
    if q==4: return a^b
    return (a+b)%q

def mul(a,b,q):
    if q==4:
        z=0
        while b:
            if b&1: z^=a
            b>>=1
            a<<=1
            if a&4: a^=7
        return z
    return (a*b)%q

def inv(a,q):
    assert a
    for b in range(1,q):
        if mul(a,b,q)==1: return b
    raise ValueError('no inverse')

def rank(rows,q):
    if not rows: return 0
    rows=[r[:] for r in rows]
    n=len(rows); m=len(rows[0]); i=0
    for j in range(m):
        k=next((k for k in range(i,n) if rows[k][j]),None)
        if k is None: continue
        rows[i],rows[k]=rows[k],rows[i]
        c=inv(rows[i][j],q)
        rows[i]=[mul(c,x,q) for x in rows[i]]
        for k in range(i+1,n):
            c=rows[k][j]
            if c:
                rows[k]=[add(x,(-mul(c,y,q))%q if q!=4 else mul(c,y,q),q) for x,y in zip(rows[k],rows[i])]
        i+=1
        if i==n: break
    return i

def matrices(d,q):
    words=[]
    for k in (1,2,3): words+=list(product(range(d),repeat=k))
    col_words=words[:d+d*d]
    out_words=words[d:]
    index={w:i for i,w in enumerate(out_words)}
    for coeffs in product(range(q),repeat=d+d*d):
        u={w:c for w,c in zip(col_words,coeffs) if c}
        a=coeffs[:d]; b=coeffs[d:]
        mat=[[0]*len(col_words) for _ in out_words]
        for j,w in enumerate(col_words):
            for v,c in u.items():
                if len(v)+len(w)<4:
                    vw=v+w; wv=w+v
                    mat[index[vw]][j]=add(mat[index[vw]][j],c,q)
                    mat[index[wv]][j]=add(mat[index[wv]][j],(-c)%q if q!=4 else c,q)
        yield (a,b,rank(mat,q))

def run(d,q):
    got=Counter(); wrong=[]
    for a,b,r in matrices(d,q):
        got[r]+=1
        if any(a): expected=d*d+d-2
        elif not any(b): expected=0
        else:
            expected=d
            # Direct tensor multiplication determines whether some nonzero linear x commutes with b.
            for x in product(range(q),repeat=d):
                if not any(x): continue
                out={w:0 for w in product(range(d),repeat=3)}
                for i in range(d):
                    for j in range(d):
                        t=b[i*d+j]
                        for k in range(d):
                            out[(i,j,k)]=add(out[(i,j,k)],mul(t,x[k],q),q)
                            out[(k,i,j)]=add(out[(k,i,j)],(-mul(x[k],t,q))%q if q!=4 else mul(x[k],t,q),q)
                if not any(out.values()):
                    expected=d-1;break
        if r!=expected and len(wrong)<5:wrong.append((a,b,r,expected))
    r1=d*d+d-2
    expected=Counter({0:1,d-1:q**d-1,d:q**(d*d)-q**d,r1:(q**d-1)*q**(d*d)})
    # Some rank levels may collide for d=2, so sum those counts.
    ex=Counter()
    for r,num in expected.items(): ex[r]+=num
    # Counter literal already collapses duplicates in d=2? d=2 ranks 0,1,2,4 distinct.
    assert got==ex,(d,q,got,ex)
    assert not wrong,(d,q,wrong)
    print('PASS d=%d q=%d size=%d rank_counts=%s'%(d,q,q**(d+d*d+d**3),sorted((r,num*q**(d**3)) for r,num in got.items())))

if __name__=='__main__':
    for d,q in [(2,2),(2,3),(2,4),(2,5),(3,2)]:run(d,q)
    print('FREE_TRUNCATED_TENSOR_GROUP_CLASS_SPECTRUM_OK 5_CONFIGURATIONS')
