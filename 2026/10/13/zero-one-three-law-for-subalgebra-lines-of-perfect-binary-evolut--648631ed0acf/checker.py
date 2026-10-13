"""Independent finite-field spot checks for projective subalgebra-line counts.
Run: python research11_char2_check.py
Finite tests support, but do not prove, the unrestricted theorem.
"""
from collections import Counter

def mul(x,y,q,poly):
    z=0
    while y:
        if y&1:z^=x
        y>>=1
        x<<=1
        if x&q:x^=poly
    return z

def census(q,poly):
    points=[(1,t) for t in range(q)]+[(0,1)]
    sq=[(mul(x,x,q,poly),mul(y,y,q,poly)) for x,y in points]
    hist=Counter()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                for d in range(q):
                    if mul(a,d,q,poly)==mul(b,c,q,poly):continue
                    r=0
                    for (x,y),(xx,yy) in zip(points,sq):
                        vx=mul(a,xx,q,poly)^mul(b,yy,q,poly)
                        vy=mul(c,xx,q,poly)^mul(d,yy,q,poly)
                        if mul(x,vy,q,poly)==mul(y,vx,q,poly):r+=1
                    hist[r]+=1
    N=q*(q-1)*(q-1)*(q+1)
    assert sum(hist.values())==N
    assert hist==Counter({0:N//3,1:N//2,3:N//6}), (q,hist)
    return dict(sorted(hist.items()))

if __name__=='__main__':
    for q,poly in [(2,0b11),(4,0b111),(8,0b1011),(16,0b10011)]:
        print('field_size',q,'distribution',census(q,poly))
    print('VERIFY_OK')
