#!/usr/bin/env python3
from itertools import product
from collections import defaultdict, deque


def all_faces(n):
    """All augmented faces of the Morse complex of K_{2,n}, including empty."""
    faces=set()
    for a in range(-1,n):      # A_a=u->w_a, or absent
      for b in range(-1,n):    # B_b=v->w_b, or absent
        for rs in product(range(3), repeat=n): # 0 none,1 X_i=w_i->u,2 Y_i=w_i->v
          if a>=0 and rs[a]==1: continue
          if b>=0 and rs[b]==2: continue
          if a>=0 and b>=0 and a!=b and rs[a]==2 and rs[b]==1: continue
          s=[]
          if a>=0: s.append(('A',a))
          if b>=0: s.append(('B',b))
          for i,t in enumerate(rs):
            if t==1: s.append(('X',i))
            elif t==2: s.append(('Y',i))
          faces.add(frozenset(s))
    return faces


def greedy_augmented_matching(n, faces):
    alive=set(faces)
    pairs=[]
    order=[]
    for i in range(n): order += [('X',i),('A',i),('Y',i),('B',i)]
    for q in order:
        low=[]
        for s in list(alive):
            if q not in s:
                t=s|{q}
                if t in alive:
                    low.append(s)
        for s in low:
            t=s|{q}
            if s in alive and t in alive:
                alive.remove(s); alive.remove(t); pairs.append((s,t,q))
    return pairs,alive


def predicted(n):
    out=set()
    # Family II.
    for j in range(1,n):
        s={('B',j),('X',j)}|{('Y',k) for k in range(n) if k!=j}
        out.add(frozenset(s))
    # Family I.
    for i in range(1,n):
        # j=0
        s={('A',i),('B',0)}|{('Y',k) for k in range(1,n)}
        out.add(frozenset(s))
        for j in range(1,n):
            if j<=i:
                s={('A',i),('B',j)}|{('Y',k) for k in range(n) if k!=j}
            else:
                s={('A',i),('B',j),('X',j)}|{('Y',k) for k in range(n) if k not in (i,j)}
            out.add(frozenset(s))
    return out


def acyclic_nonempty(faces,pairs):
    nonempty={s for s in faces if s}
    # Drop augmented pair incident with empty; retain all other matching pairs.
    match={}
    for lo,hi,_ in pairs:
        if not lo: continue
        match[(lo,hi)]=True
    indeg={s:0 for s in nonempty}
    adj=defaultdict(list)
    for hi in nonempty:
        for q in hi:
            lo=hi-{q}
            if not lo: continue
            if (lo,hi) in match:
                u,v=lo,hi
            else:
                u,v=hi,lo
            adj[u].append(v); indeg[v]+=1
    dq=deque([s for s,d in indeg.items() if d==0]); seen=0
    while dq:
        s=dq.popleft(); seen+=1
        for t in adj[s]:
            indeg[t]-=1
            if indeg[t]==0: dq.append(t)
    return seen==len(nonempty)


def euler_nonempty(faces):
    e=0
    for s in faces:
        if s: e += (-1)**(len(s)-1)
    return e


def main():
    for n in range(1,8):
        faces=all_faces(n)
        pairs,crit=greedy_augmented_matching(n,faces)
        pred=predicted(n)
        assert crit==pred, (n,len(crit),len(pred),crit^pred)
        assert len(crit)==n*n-1
        assert all(len(s)==n+1 for s in crit)
        # Removing the pair containing empty leaves one critical vertex and same top cells.
        empty_pairs=[p for p in pairs if not p[0]]
        assert len(empty_pairs)==1
        critical_nonempty={empty_pairs[0][1]}|crit
        assert len(empty_pairs[0][1])==1
        assert euler_nonempty(faces)==1+(-1)**n*(n*n-1)
        if n<=6:
            assert acyclic_nonempty(faces,pairs)
        fv=defaultdict(int)
        for s in faces:
            if s: fv[len(s)-1]+=1
        print(f"n={n} faces={len(faces)-1} fvector={[fv[d] for d in sorted(fv)]} critical0=1 critical_top={len(crit)} dag={'OK' if n<=6 else 'not-run'}")
    print('VERIFY_OK')

if __name__=='__main__': main()
