"""Independent exact enumeration of strict graph-continuous maps on small complete multipartite graphs.

All computations use integers. This checks the closed coefficient formulas against
explicit matchings, independent image sets, inverse-transversal and covering tests.
"""
from itertools import combinations, permutations, product
from math import comb, factorial


def falling(n,k):
    if k>n or k<0: return 0
    x=1
    for j in range(k): x*=n-j
    return x


def matchings(edges):
    ans=[()]
    for e in edges:
        ans += [m+(e,) for m in list(ans) if all(not(set(e)&set(f)) for f in m)]
    return ans


def prediction(sizes):
    n=sum(sizes); r=len(sizes); maxk=n//2
    # Evaluate matching count by independent edge-type arrays, not matching enumeration.
    pairs=list(combinations(range(r),2))
    m=[0]*(maxk+1)
    def rec(pos,deg,mult,k):
        if pos==len(pairs):
            z=1
            for i,d in enumerate(deg): z*=falling(sizes[i],d)
            m[k]+= z//mult
            return
        i,j=pairs[pos]
        for a in range(min(sizes[i]-deg[i],sizes[j]-deg[j],maxk-k)+1):
            deg[i]+=a;deg[j]+=a
            rec(pos+1,deg,mult*factorial(a),k+a)
            deg[i]-=a;deg[j]-=a
    rec(0,[0]*r,1,0)
    total=[]; regular=[]; idem=[]
    for k in range(maxk+1):
        if not k: total.append(1);regular.append(1);idem.append(1);continue
        s=sum(comb(t,k) for t in sizes if t>=k)
        b=sum(comb(sizes[i],k)*falling(n-sizes[i],k) for i in range(r) if sizes[i]>=k)
        b-=sum(comb(sizes[i],k)*falling(sizes[j],k) for i,j in pairs if sizes[i]>=k)
        total.append(factorial(k)*s*m[k])
        regular.append(factorial(k)*s*b)
        idem.append(sum(comb(sizes[i],k)*falling(n-sizes[i],k) for i in range(r) if sizes[i]>=k))
    return total,regular,idem


def direct(sizes):
    parts=[]
    for i,n in enumerate(sizes): parts += [i]*n
    n=len(parts); verts=range(n)
    edges=[(i,j) for i,j in combinations(verts,2) if parts[i]!=parts[j]]
    matches=matchings(edges)
    byrank={}
    for m in matches: byrank.setdefault(len(m),[]).append(m)
    total=[0]*(n//2+1);regular=total.copy();idem=total.copy()
    for k,group in byrank.items():
        images=[s for s in combinations(verts,k) if len({parts[x] for x in s})<=1]
        for m in group:
            # Directly search for a same-part choice of one endpoint per edge.
            transversal=any(len({parts[x] for x in picks})<=1 for picks in product(*m)) if m else True
            for im in images:
                # Directly search matching that covers every image vertex once.
                covering=any(all(sum(v in e for e in cov)==1 for v in im) for cov in byrank[k])
                for p in permutations(im):
                    total[k]+=1
                    if transversal and covering:regular[k]+=1
                    if all(p[j] in m[j] for j in range(k)):idem[k]+=1
    return total,regular,idem



def brute_inverse_check(profile):
    """Direct fgf=f test with a second independent generator of all maps."""
    parts=[i for i,n in enumerate(profile) for _ in range(n)]
    n=len(parts)
    edges=[(i,j) for i,j in combinations(range(n),2) if parts[i]!=parts[j]]
    ms=matchings(edges)
    transformations=[]
    for m in ms:
        k=len(m)
        for im in combinations(range(n),k):
            if len({parts[z] for z in im})>1:continue
            for assignment in permutations(im):
                f=[-1]*n
                for j,e in enumerate(m):
                    for v in e:f[v]=assignment[j]
                transformations.append(tuple(f))
    def composition(f,g):
        return tuple(g[z] if z>=0 else -1 for z in f)
    regular=sum(any(composition(composition(f,g),f)==f for g in transformations)
                for f in transformations)
    predicted=sum(prediction(profile)[1])
    assert regular==predicted,(profile,regular,predicted)
    print('INVERSE',profile,'size',len(transformations),'regular',regular)


def main():
    profiles=[(1,),(2,),(1,1),(1,2),(2,2),(1,1,1),(1,2,2),(2,2,2),
              (1,1,1,1),(2,1,1,1),(1,2,3),(2,2,3),(1,1,2,2),(1,1,1,2,2),
              (2,3,3)]
    for p in profiles:
        pred=prediction(p);actual=direct(p)
        assert pred==actual,(p,pred,actual)
        expected_reg=(len(p)<=2 or len(p)==3 and (min(p)==1 or max(p)<=2) or len(p)>=4 and max(p)==1)
        is_reg=sum(pred[0])==sum(pred[1])
        assert expected_reg==is_reg,(p,expected_reg,is_reg)
        print('PASS',p,'total',sum(pred[0]),'regular',sum(pred[1]),'idempotents',sum(pred[2]),'nonregular_by_rank',[a-b for a,b in zip(pred[0],pred[1])])
    for p in [(1,2,2),(2,1,1,1),(1,1,2,2),(2,2,2)]:brute_inverse_check(p)
    print('ALL',len(profiles),'PROFILES PASSED')

if __name__=='__main__':main()
