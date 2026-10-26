"""Finite checks for a candidate-specific collective-consent clone theorem.
Run: python3 check.py
Only standard-library Python required.
"""
from itertools import combinations
from random import Random


def in_awvc(rankings, approvals, c):
    n=len(rankings)
    m=len(rankings[0])
    assert all(len(x)==m and set(x)==set(rankings[0]) for x in rankings)
    s=sum(c in a for a in approvals)
    if s==0:return False
    disapprovers=[i for i in range(n) if c not in approvals[i]]
    positions=[{name:j for j,name in enumerate(r)} for r in rankings]
    for j in range(1,len(disapprovers)+1):
        for S in combinations(disapprovers,j):
            common=sum(all(positions[i][d]<positions[i][c] for i in S)
                       for d in rankings[0] if d!=c)
            if j*m>s*(m-common):
                return False
    return True


def clone_profile(rankings, approvals, d, t):
    cloned=tuple(f'copy_{q}' for q in range(t))
    ranks=[]
    aps=[]
    for r,a in zip(rankings,approvals):
        out=[]
        for x in r:
            out.append(x)
            if x==d: out.extend(cloned)
        ranks.append(out)
        aps.append(set(a)| (set(cloned) if d in a else set()))
    return ranks,aps


def exact_clone_status(rankings,approvals,c,d,t):
    n=len(rankings);m=len(rankings[0]);s=sum(c in a for a in approvals)
    if s==0:return False
    dis=[i for i in range(n) if c not in approvals[i]]
    pos=[{x:j for j,x in enumerate(row)} for row in rankings]
    for j in range(1,len(dis)+1):
        for S in combinations(dis,j):
            b=sum(all(pos[i][e]<pos[i][c] for i in S)
                  for e in rankings[0] if e!=c)
            delta=int(all(pos[i][d]<pos[i][c] for i in S))
            if j*(m+t)>s*(m-b+t*(1-delta)):
                return False
    return True


def special_profile(L):
    assert L>=2
    U=[f'U_{i}' for i in range(2*L-1)]
    V=[f'V_{i}' for i in range(L-1)]
    W=[f'W_{i}' for i in range(3)]
    c='c'; d=V[0]
    base=[c]+V+W+U
    p4=V+W+[c]+U
    p5=U+W+[c]+V
    rank=[base[:],base[:],base[:],p4,p5]
    aps=[{c},{c},{c},set(V+W),set(U+W)]
    return rank,aps,c,d


def main():
    assertions=0
    for L in range(2,37):
        rankings,approvals,c,d=special_profile(L)
        for t in range(0,3*L+4):
            rt,at=clone_profile(rankings,approvals,d,t)
            direct=in_awvc(rt,at,c)
            expected=1<=t<=3*L-2
            affine=exact_clone_status(rankings,approvals,c,d,t)
            assert direct==expected==affine,(L,t,direct,expected,affine)
            assertions+=2
    rng=Random(132951)
    for n in range(3,9):
        for m in range(3,10):
            for trial in range(100):
                alphabet=[f'a{i}' for i in range(m)]
                rankings=[]; approvals=[]
                for i in range(n):
                    r=alphabet[:];rng.shuffle(r)
                    rankings.append(r)
                    approvals.append(set(r[:rng.randrange(m+1)]))
                c=alphabet[0];d=alphabet[1]
                for t in (0,1,2,3,7):
                    newr,newa=clone_profile(rankings,approvals,d,t)
                    direct=in_awvc(newr,newa,c)
                    affine=exact_clone_status(rankings,approvals,c,d,t)
                    assert direct==affine,(n,m,trial,t)
                    assertions+=1
    print(f'PASS: {assertions} independently compared AWVC conditions; all exact integers.')

if __name__=='__main__':main()
