from fractions import Fraction as Q
from itertools import combinations
from math import sqrt

def gain(L,a,b):
    d=b-a
    return Q(d*d*(a+b-L), 2*(L*(d+1)-d*d))

def harmonic(L,a,b):
    edges={(j,j+1) for j in range(L)}
    edges.add((a,b))
    neigh=[set() for _ in range(L+1)]
    for u,v in edges:
        neigh[u].add(v);neigh[v].add(u)
    n=L-1
    M=[]
    for j in range(1,L):
        row=[Q(0) for _ in range(n+1)]
        row[j-1]=Q(len(neigh[j]))
        for k in neigh[j]:
            if 1<=k<L:row[k-1]-=1
            elif k==L:row[n]+=1
        M.append(row)
    for c in range(n):
        idx=next(i for i in range(c,n) if M[i][c])
        M[c],M[idx]=M[idx],M[c]
        p=M[c][c]
        M[c]=[v/p for v in M[c]]
        for i in range(n):
            if i!=c:
                p=M[i][c]
                if p:M[i]=[v-p*w for v,w in zip(M[i],M[c])]
    return [Q(0)]+[M[i][-1] for i in range(n)]+[Q(1)]

def explicit(L,a,b):
    d=b-a;F=L*(d+1)-d*d
    return [Q((d+1)*j,F) if j<=a else Q(d*a+j,F) if j<=b else Q((d+1)*j-d*d,F) for j in range(L+1)]

def run():
    assertions=0
    for L in range(3,12):
        chords=[(a,b) for a in range(L+1) for b in range(a+2,L+1)]
        best=max(gain(L,a,b) for a,b in chords)
        assert best>0;assertions+=1
        endpoint_best=max(gain(L,a,L) for a in range(1,L-1))
        assert best==endpoint_best;assertions+=1
        for a,b in chords:
            h=harmonic(L,a,b)
            ex=explicit(L,a,b)
            assert h==ex;assertions+=1
            assert sum(h[1:-1],Q(0))-Q(L-1,2)==gain(L,a,b);assertions+=1
            assert gain(L,a,b)<=gain(L,L-(b-a),L);assertions+=1
    for L in range(3,160):
        opts=[a for a in range(1,L-1) if gain(L,a,L)==max(gain(L,j,L) for j in range(1,L-1))]
        def P(a):return L*L - 3*L*a -L*a*a +a*a*a
        lo,hi=0.,float(L)
        for _ in range(60):
            mid=(lo+hi)/2
            if P(mid)>0:lo=mid
            else:hi=mid
        alpha=(lo+hi)/2
        assert all(abs(a-alpha)<=1 for a in opts);assertions+=1
        assert all(gain(L,a,L)>0 for a in opts);assertions+=1
    print(f'PASS {assertions} exact/comparison assertions')
    for L in (6,10,20,50,100,200):
        opts=[a for a in range(1,L-1) if gain(L,a,L)==max(gain(L,j,L) for j in range(1,L-1))]
        a=opts[0]
        d=gain(L,a,L)
        print(f'L={L}, optimal endpoints=({a},{L}), total_gain={d}, mean_new={Q(1,2)+d/Q(L-1)}')
if __name__=='__main__':run()
