#!/usr/bin/env python3
"""Exact arithmetic checks for the cyclic stripe sector of the separable-field CA.

All dependencies are in the Python standard library. This checks finite identities;
the unbounded-height statements require the accompanying mathematical proof.
"""
from fractions import Fraction as Q

S=(Q(1,18),Q(7,18))
B=(Q(1,3),Q(8,9))

def field_step(matrix, S=S, B=B):
    H=len(matrix); W=len(matrix[0]); assert H>=3 and W>=3
    assert all(len(row)==W for row in matrix)
    row=[sum(r) for r in matrix]
    col=[sum(matrix[j][i] for j in range(H)) for i in range(W)]
    R=[sum(row[(j+d)%H] for d in (-1,0,1)) for j in range(H)]
    C=[sum(col[(i+d)%W] for d in (-1,0,1)) for i in range(W)]
    mx=max(R)*max(C)
    if not mx:return [[0]*W for _ in range(H)]
    out=[]
    for j in range(H):
        rr=[]
        for i in range(W):
            q=Q(R[j]*C[i],mx)
            rr.append(int(S[0]<=q<=S[1]) if matrix[j][i] else int(B[0]<=q<=B[1]))
        out.append(rr)
    return out

def stripe_step(word, S=S, B=B):
    n=len(word);assert n>=3
    t=[sum(word[(j+d)%n] for d in (-1,0,1)) for j in range(n)]
    m=max(t)
    if not m:return [0]*n
    return [int(S[0]<=Q(t[j],m)<=S[1]) if word[j] else
            int(B[0]<=Q(t[j],m)<=B[1]) for j in range(n)]

def rule_step(word, r):
    n=len(word)
    return [(r>>((word[(i-1)%n]<<2)|(word[i]<<1)|word[(i+1)%n]))&1 for i in range(n)]

def has_triple(word):
    n=len(word)
    return any(all(word[(j+d)%n] for d in (-1,0,1)) for j in range(n))

def bits(mask,n):
    return [(mask>>i)&1 for i in range(n)]

def main():
    assertions=0
    regimes=[(Q(1,18),Q(7,18),Q(1,3),Q(8,9)),
             (Q(1,3),Q(1,3),Q(1,3),Q(2,3)),
             (Q(1,40),Q(49,100),Q(1,5),Q(4,5)),
             (Q(1,20),Q(2,5),Q(1,3),Q(7,10))]
    for sl,sh,bl,bh in regimes:
        ss=(sl,sh); bb=(bl,bh)
        for n in range(3,10):
            for mask in range(1<<n):
                w=bits(mask,n)
                m=max(sum(w[(j+d)%n] for d in (-1,0,1)) for j in range(n))
                out=stripe_step(w,ss,bb)
                predicted=rule_step(w,54) if m==3 else (rule_step(w,18) if m==2 else [0]*n)
                assert out==predicted,(ss,bb,n,mask,m,out,predicted)
                assertions+=1
                if m==2:
                    assert not has_triple(out)
                    assertions+=1
                if n<=6 and mask%3==0:
                    for W in (3,4,6):
                        mat=[w[j:j+1]*W for j in range(n)]
                        assert field_step(mat,ss,bb)==[[z]*W for z in out]
                        assertions+=1
    # The cited period-169 rule-54 orbit also exists in the full 2D model.
    seed='#.###........'
    assert len(seed)==13
    state=[int(c=='#') for c in seed]
    orbit=set()
    for step in range(169):
        tup=tuple(state)
        assert tup not in orbit
        orbit.add(tup)
        assert has_triple(state)
        assert stripe_step(state)==rule_step(state,54)
        for W in (3,5):
            mat=[[state[j]]*W for j in range(13)]
            expected=[[z]*W for z in stripe_step(state)]
            assert field_step(mat)==expected
            assertions+=1
        state=stripe_step(state)
        assertions+=3
    assert state==[int(c=='#') for c in seed]
    assert len(orbit)==169
    # All period cycles of height <= 9 are assigned exactly one regime.
    for n in range(3,10):
        graph={m:sum(stripe_step(bits(m,n))[i]<<i for i in range(n))
               for m in range(1<<n)}
        seen=set()
        for init in range(1<<n):
            if init in seen:continue
            path=[];first={};cur=init
            while cur not in first and cur not in seen:
                first[cur]=len(path);path.append(cur);cur=graph[cur]
            seen.update(path)
            if cur not in first:continue
            cyc=path[first[cur]:]
            classes=set(max(sum(bits(x,n)[(j+d)%n] for d in (-1,0,1))
                            for j in range(n)) for x in cyc)
            assert len(classes)==1,(n,cyc,classes)
            assertions+=1
    print(f'VERIFY_OK assertions={assertions} orbit_period=169 rule_regimes=(54,18,0)')
if __name__=='__main__':main()
