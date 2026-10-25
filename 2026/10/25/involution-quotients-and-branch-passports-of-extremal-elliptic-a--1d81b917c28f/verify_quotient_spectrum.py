"""Finite sanity checks for involution quotient ramification classes.

This does not replace the geometric proof for arbitrary powers of two.
"""

def check(q):
    assert q >= 8 and (q & (q-1)) == 0
    def mul(a,b):
        i,e,f=a; j,d,g=b
        return ((i+(-1 if e else 1)*j)%q, (e+d)%2,(f+g)%2)
    ident=(0,0,0)
    invols=[(i,1,f) for i in range(q) for f in range(2)] + [(0,0,1),(q//2,0,0),(q//2,0,1)]
    assert all(mul(s,s)==ident for s in invols)
    H=[ident,(1,1,0)]
    G=[(i,e,f) for i in range(q) for e in range(2) for f in range(2)]
    classes={}
    for x in G:
        coset=tuple(sorted([x,mul(x,H[1])]))
        classes[coset]=coset
    assert len(classes)==2*q
    C=set(classes)
    for s in invols:
        r2=sum((s[1]==0 and s[0]==0) or (s[1]==1 and (s[0]-2*i)%q==0) for i in range(q))
        r1=sum(tuple(sorted([mul(s,c[0]),mul(s,c[1])]))==c for c in C)
        r=r1+r2
        g=(q+2-r)//2
        kind='deck' if s==(0,0,1) else 'central_free' if s[1]==0 else ('even_reflection' if s[0]%2==0 else 'odd_reflection')
        classes.setdefault('counts',[]).append((kind,s,r,g,r2,r1))
    assert sorted((x[2] for x in classes['counts'] if x[0]=='odd_reflection' and x[1][2]==0)) == [4]*(q//2)
    by={}
    for kind,s,r,g,r2,r1 in classes['counts']:
        by.setdefault(kind,set()).add((r,g))
    assert by['deck']=={(q,1)}
    assert by['central_free']=={(0,q//2+1)}
    assert by['even_reflection']=={(2,q//2)}
    assert by['odd_reflection']=={(0,q//2+1),(4,q//2-1)}
    return by

if __name__=='__main__':
    for q in [8,16,32,64,128]:
        print(q,check(q))
    print('QUOTIENT_SPECTRUM_SANITY_OK')
