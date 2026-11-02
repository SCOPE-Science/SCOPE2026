"""Exact finite tests for the half-grid projection theorem.

Requires only Python 3 standard library. This checker is corroborative;
the all-size statement follows from the proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def clip(q):
    return min(F(1), max(F(0), q))


def eval_term(t, vals):
    op = t[0]
    if op == 'c': return t[1]
    if op == 'v': return vals[t[1]]
    if op == 'not': return F(1) - eval_term(t[1], vals)
    if op == 'min': return min(eval_term(t[1], vals), eval_term(t[2], vals))
    if op == 'max': return max(eval_term(t[1], vals), eval_term(t[2], vals))
    if op == 'shift': return clip(eval_term(t[2], vals) + t[1])
    raise ValueError(t)


# A piece is ('c', value) or ('a', variable_name, +/-1, intercept).
# Its meaning is the constant or clip(sign*x + intercept).
def eval_piece(piece, vals):
    return piece[1] if piece[0]=='c' else clip(piece[2]*vals[piece[1]] + piece[3])


def join(A, B):
    return A + B


def meet(A, B):
    return [a+b for a in A for b in B]


def negate_piece(z):
    if z[0]=='c':return [[('c', F(1)-z[1])]]
    return [[('a',z[1],-z[2],F(1)-z[3])]]


def shift_piece(z, s):
    if z[0]=='c':return [[('c',clip(z[1]+s))]]
    a=('a',z[1],z[2],z[3]+s)
    if s>=0:
        return [[('c',s)],[a]]
    return [[('c',F(1)+s),a]]


def transform(A, piece_fn):
    out=[]
    for conj in A:
        sub=[[]]
        for piece in conj:
            sub=meet(sub,piece_fn(piece))
        out.extend(sub)
    return out


def negate(A):
    # NOT(max_i min_j p_ij) = min_i max_j NOT(p_ij).
    out=[[]]
    for conj in A:
        neg_conj=[]
        for piece in conj:
            neg_conj.extend(negate_piece(piece))
        out=meet(out,neg_conj)
    return out


def dnf(t):
    op=t[0]
    if op=='c':return [[('c',t[1])]]
    if op=='v':return [[('a',t[1],1,F(0))]]
    if op=='not':return negate(dnf(t[1]))
    if op=='min':return meet(dnf(t[1]),dnf(t[2]))
    if op=='max':return join(dnf(t[1]),dnf(t[2]))
    if op=='shift':return transform(dnf(t[2]),lambda z:shift_piece(z,t[1]))
    raise ValueError(t)


def eval_dnf(A, vals):
    return max((min((eval_piece(z,vals) for z in conj),default=F(1)) for conj in A),default=F(0))


def max_piece_conjunction(positive, negative):
    # Exactly maximize min(clip(x+a),clip(-x+b)) on [0,1].
    if not positive and not negative:return F(1), F(0)
    if not positive:return clip(min(negative)),F(0)
    if not negative:return clip(F(1)+min(positive)),F(1)
    a=min(positive); b=min(negative)
    x=clip((b-a)/2)
    candidates=(F(0),F(1),x)
    pairs=[(min(clip(t+a),clip(-t+b)),t) for t in candidates]
    return max(pairs)


def project(A, hidden):
    out=[]
    for conj in A:
        kept=[z for z in conj if z[0]=='c' or z[1] not in hidden]
        for v in hidden:
            pos=[z[3] for z in conj if z[0]=='a' and z[1]==v and z[2]==1]
            neg=[z[3] for z in conj if z[0]=='a' and z[1]==v and z[2]==-1]
            if pos or neg:
                height,_=max_piece_conjunction(pos,neg)
                kept.append(('c',height))
        out.append(kept)
    return out


def random_term(rng,depth,d):
    if depth==0 or rng.random()<.27:
        if rng.random()<.70:return ('v',rng.choice(('p','q','r')))
        return ('c',F(rng.randrange(d+1),d))
    which=rng.choice(('not','shift','min','max'))
    if which=='not':return ('not',random_term(rng,depth-1,d))
    if which=='shift':return ('shift',F(rng.randrange(-d,d+1),d),random_term(rng,depth-1,d))
    return (which,random_term(rng,depth-1,d),random_term(rng,depth-1,d))


def test():
    rng=Random(26032335)
    cases=0
    comparisons=0
    for d in range(1,5):
      for depth in range(6):
        for _ in range(12):
          t=random_term(rng,depth,d)
          A=dnf(t)
          hidden={'p','r'}
          B=project(A,hidden)
          # Random off-grid visible assignments and random full assignments.
          for trial in range(3):
            vals={v:F(rng.randrange(31),30) for v in ('p','q','r')}
            if eval_term(t,vals)!=eval_dnf(A,vals):
                raise AssertionError(('normalization',t,A,vals))
            if eval_dnf(B,vals)!=eval_dnf(B,{'p':F(0),'q':vals['q'],'r':F(0)}):
                raise AssertionError('hidden variable in projected form')
          # Direct exhaustive optimized evaluation at the half grid and a finer grid.
          if depth<=3:
            for q in (F(0),F(2,7),F(1)):
              exact=eval_dnf(B,{'p':F(0),'q':q,'r':F(0)})
              half=max(eval_term(t,{'p':F(i,2*d),'q':q,'r':F(j,2*d)})
                         for i in range(2*d+1) for j in range(2*d+1))
              finer=max(eval_term(t,{'p':F(i,4*d),'q':q,'r':F(j,4*d)})
                          for i in range(4*d+1) for j in range(4*d+1))
              if exact!=half or exact!=finer:
                  raise AssertionError(('projection',d,t,q,exact,half,finer))
              # Dual check, via the exact complement identity.
              exact_inf=F(1)-eval_dnf(project(negate(A),hidden),{'p':F(0),'q':q,'r':F(0)})
              direct_inf=min(eval_term(t,{'p':F(i,2*d),'q':q,'r':F(j,2*d)})
                             for i in range(2*d+1) for j in range(2*d+1))
              if exact_inf!=direct_inf:
                  raise AssertionError(('dual projection',d,t,q,exact_inf,direct_inf))
              comparisons+=2
          for conj in B:
             for z in conj:
                 if z[0]=='c' and (2*d*z[1]).denominator!=1:
                     raise AssertionError(('non-half-grid constant',z,d))
          cases+=1
    # Witness for every d has a unique maximizer of reduced denominator exactly 2d.
    for d in range(1,25):
        k=0 if d==1 else (1 if d%2==0 else 2)
        x=F(d+k,2*d)
        assert x.denominator==2*d
        t=('min',('v','p'),('shift',F(k,d),('not',('v','p'))))
        A=dnf(t); B=project(A,{'p'})
        assert eval_dnf(B,{'p':F(0)})==x
        # Non-refined input grid misses the uniquely optimal point.
        assert max(eval_term(t,{'p':F(j,d)}) for j in range(d+1))<x
    print(f'ALL_CHECKS_OK; random_terms={cases}; sup_inf_comparisons={comparisons}; sharp_denominators=24')


if __name__=='__main__':test()
