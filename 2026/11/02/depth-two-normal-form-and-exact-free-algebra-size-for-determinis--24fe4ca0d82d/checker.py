"""Reproducible finite checks for modal type classification."""
from itertools import product
from collections import Counter


def weak(f):
    for x, y in enumerate(f):
        if y >= 0 and f[y] >= 0 and f[y] not in (x, y):
            return False
    return True


def tcode(f, col, x):
    a = col[x]
    y = f[x]
    if y < 0:
        return ('T', a)
    if y == x:
        return ('F', a)
    b = col[y]
    z = f[y]
    if z < 0:
        return ('L', a, b)
    if z == y:
        return ('F', a) if a == b else ('R', a, b)
    assert z == x
    return ('F', a) if a == b else ('P', a, b)


def sigma(f, col, x, depth):
    if depth == 0:
        return col[x]
    return col[x], None if f[x] < 0 else sigma(f, col, f[x], depth-1)


def allcodes(q):
    return ({('T',a) for a in range(q)} |
            {('F',a) for a in range(q)} |
            {('L',a,b) for a in range(q) for b in range(q)} |
            {('R',a,b) for a in range(q) for b in range(q) if a!=b} |
            {('P',a,b) for a in range(q) for b in range(q) if a!=b})


def sample(t):
    c=t[0]
    if c=='T': return (-1,), (t[1],)
    if c=='F': return (0,), (t[1],)
    if c=='L': return (1,-1), (t[1],t[2])
    if c=='R': return (1,1), (t[1],t[2])
    if c=='P': return (1,0), (t[1],t[2])
    raise ValueError(t)


def charformula(t):
    c=t[0];a=t[1]
    color=lambda a: ('color',a)
    d=lambda x: ('diamond',x)
    c_and=lambda x,y: ('and',x,y)
    if c=='T':return c_and(color(a), ('not',d(('top',))))
    if c=='F':return c_and(color(a), d(c_and(color(a),d(color(a)))))
    b=t[2]
    if c=='L': return c_and(color(a), d(c_and(color(b),('not',d(('top',))))))
    if c=='R': return c_and(color(a), d(c_and(color(b),d(color(b)))))
    if c=='P': return c_and(color(a), d(c_and(color(b),d(color(a)))))
    raise ValueError(t)


def truth(form, f, col, root):
    op=form[0]
    if op=='color': return col[root]==form[1]
    if op=='top':return True
    if op=='not':return not truth(form[1],f,col,root)
    if op=='and':return truth(form[1],f,col,root) and truth(form[2],f,col,root)
    if op=='diamond':return f[root]>=0 and truth(form[1],f,col,f[root])
    raise ValueError(form)


def main():
    for q in [1,2,3]:
        ts=sorted(allcodes(q))
        assert len(ts)==3*q*q
        assert all(weak(sample(t)[0]) for t in ts)
        signatures={sigma(*sample(t), 0, 2):t for t in ts}
        assert len(signatures)==len(ts)
        # Each formula is a singleton test across all canonical types.
        for i,t in enumerate(ts):
            form=charformula(t)
            assert [j for j,u in enumerate(ts) if truth(form, *sample(u), 0)] == [i], (q,t)
        print('q=',q,'types=',len(ts),'pairwise distinct depth2; characteristic formulas=OK')
    count=0
    for n in range(1,7):
        good=0
        for f in product(range(-1,n),repeat=n):
            if not weak(f):continue
            good+=1
            # Independent modal depth2 signatures must agree exactly with types.
            for col in product(range(2),repeat=n):
                count+=n
                for x in range(n):
                    t=tcode(f,col,x)
                    signature=sigma(f,col,x,2)
                    can_f,can_col=sample(t)
                    assert sigma(can_f,can_col,0,2)==signature,(n,f,col,x,t)
                    # Check actual rooted characteristic formula on each finite model for n<=4
                    if n<=4:
                        assert truth(charformula(t),f,col,x)
        print('n=',n,'valid partial maps=',good)
    assert sigma((0,), (0,),0,1)==sigma((1,-1), (0,0),0,1)
    assert sigma((0,), (0,),0,2)!=sigma((1,-1), (0,0),0,2)
    print('ALL_CHECKS_OK; examined rooted coloured cases=',count)

if __name__=='__main__':main()
