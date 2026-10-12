"""Reproduce count-sector singular spectra and high-index moment bounds.

Requires NumPy. Finite checks support, but do not replace, the asymptotic proof.
"""
import itertools
import math
import numpy as np


def gate(left, right):
    s, a, sb, ab = left
    u, b, ub, bb = right
    return (u, a ^ ((s ^ u) & b), ub, ab ^ ((sb ^ ub) & bb)), (s, b, sb, bb)


def packets(word, t):
    word = list(word)
    for j in range(t):
        for i in range(t + j - 1, j - 1, -1):
            word[i], word[i+1] = gate(word[i], word[i+1])
    return tuple(word[:t]), tuple(word[t:])


def assemble(t, problem):
    cells = {}
    if problem == 'operator':
        for word in itertools.product(range(4), repeat=2*t - 1):
            ins = [(v//2,v%2,v//2,v%2) for v in word[:t]]
            ins += [(1,0,0,0)]
            ins += [(v//2,v%2,v//2,v%2) for v in word[t:]]
            k=sum(p[0]==0 for p in ins[t+1:])
            ell=sum(p[0]==0 for p in ins[:t])
            x,y=packets(ins,t)
            cells[(x,y)]=(k,ell,2.0**(-(2*t-1)))
    else:
        for lsec in itertools.product((0,1), repeat=t):
            for right in itertools.product(range(4), repeat=t):
                ins=[(s,0,s,0) for s in lsec]
                ins += [(v//2,v%2,v//2,v%2) for v in right]
                k=sum(p[0]==0 for p in ins[t:])
                ell=sum(p[0]==0 for p in ins[:t])
                x,y=packets(ins,t)
                cells[(x,y)]=(k,ell,2.0**(-1.5*t))
    rows=sorted({x for x,y in cells}); cols=sorted({y for x,y in cells})
    rid={r:i for i,r in enumerate(rows)};cid={c:i for i,c in enumerate(cols)}
    M=np.zeros((len(rows),len(cols)), dtype=float)
    blocks={}
    for (x,y),(k,ell,amp) in cells.items():
        M[rid[x],cid[y]]=amp
        blocks.setdefault((k,ell),[]).append((x,y,amp))
    assert abs(np.sum(M*M)-1.0)<1e-12
    return M,blocks


def branch_test(t,problem,blocks):
    for (k,ell),pts in blocks.items():
        rows=sorted({x for x,y,a in pts});cols=sorted({y for x,y,a in pts})
        ri={r:i for i,r in enumerate(rows)};ci={c:i for i,c in enumerate(cols)}
        B=np.zeros((len(rows),len(cols)))
        for x,y,a in pts:B[ri[x],ci[y]]=a
        g=abs(ell-k) if problem=='wall' else (ell-k-1 if ell>k else k-ell)
        rank=2**g
        prob=(math.comb(t,k)*math.comb(t,ell)/4**t) if problem=='wall' else (math.comb(t-1,k)*math.comb(t,ell)/2**(2*t-1))
        vals=np.linalg.svd(B,compute_uv=False)**2
        positive=vals[vals>1e-11]
        assert len(positive)==rank, (t,problem,k,ell,len(positive),rank)
        assert np.allclose(positive,prob/rank,rtol=1e-10,atol=2e-12)
    return len(blocks)


def moment_bounds(t, problem, M):
    vals=np.linalg.svd(M,compute_uv=False)**2
    if problem=='wall':
        qs=[math.comb(t,k)/2**t for k in range(t+1)]
        rs=qs[:]
        g=lambda d:abs(d)
    else:
        qs=[math.comb(t-1,k)/2**(t-1) for k in range(t)]
        rs=[math.comb(t,l)/2**t for l in range(t+1)]
        g=lambda d: d-1 if d>0 else -d
    for alpha in (1.2,1.5,2.0,3.0):
        z=sum(float(v**alpha) for v in vals if v>1e-15)
        zd=sum((qs[k]*rs[k])**alpha for k in range(min(len(qs),len(rs))))
        rhs=sum((sum((qs[k]*rs[l])**alpha for k in range(len(qs))
                    for l in range(len(rs)) if l-k==d)*2**((1-alpha)*g(d)))**(1/(2*alpha))
                for d in range(-(len(qs)-1),len(rs)))**(2*alpha)
        assert zd <= z*(1+1e-9),('lower',t,problem,alpha,zd,z)
        assert z <= rhs*(1+1e-9),('upper',t,problem,alpha,z,rhs)
    return True


def main():
    count=0
    for problem in ('operator','wall'):
        for t in (1,2,3,4):
            M,branches=assemble(t,problem)
            count+=branch_test(t,problem,branches)
            assert moment_bounds(t,problem,M)
            print(problem,t,'shape',M.shape,'branches',len(branches))
    print('VERIFY_OK',count,'flat count-sector spectra; diagonal pinching and Minkowski moments')

if __name__=='__main__':main()
