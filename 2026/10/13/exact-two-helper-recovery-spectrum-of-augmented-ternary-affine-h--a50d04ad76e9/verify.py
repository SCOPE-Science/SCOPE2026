"""Direct finite-field incidence check for affine-half augmented ternary codes."""
from itertools import product
from collections import defaultdict

def norm(v):
    for a in v:
        if a%3:
            return tuple((c*(1 if a==1 else 2))%3 for c in v)
    raise ValueError('zero vector')

def verify(n):
    m=n-1
    ev=[];tags=[]
    for z in (0,1):
        for y in product(range(3),repeat=m):
            ev.append((z,)+y+(1,));tags.append(('eval',z,y))
    cols=ev[:]
    for j in range(n+1):
        cols.append(tuple(1 if k==j else 0 for k in range(n+1)))
        tags.append(('systematic',j))
    L=len(cols)
    by_class=defaultdict(list)
    for i,v in enumerate(cols):by_class[norm(v)].append(i)
    counts=[0]*L
    for i in range(L):
        for j in range(i+1,L):
            a,b=cols[i],cols[j]
            if norm(a)==norm(b):continue
            for w in (tuple((u+v)%3 for u,v in zip(a,b)),tuple((u-v)%3 for u,v in zip(a,b))):
                for k in by_class.get(norm(w),[]):
                    assert k!=i and k!=j
                    counts[k]+=1
    B=(3**m-1)//2 +2*m+1
    expected=[]
    for tag in tags:
        if tag[0]=='systematic':
            k=tag[1]
            expected.append(3**m+1 if k==0 else (2*3**m+2 if 1<=k<=m else B))
        else:
            _,z,y=tag
            supplement=(z==0 and any(y)) + int((z==1 and not any(y)) or (z==0 and sum(t!=0 for t in y)==1))
            expected.append(B+supplement)
    assert len(counts)==len(expected)
    mismatches=[(i,tags[i],counts[i],expected[i]) for i in range(L) if counts[i]!=expected[i]]
    print('n',n,'length',L,'base',B,'types',sorted(set(expected)),'sum',sum(counts),'mismatches',mismatches[:15])
    assert not mismatches
    assert sum(counts)%3==0
    return counts

if __name__=='__main__':
    for n in (3,4,5):verify(n)
    print('VERIFY_OK')
