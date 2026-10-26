#!/usr/bin/env python3
"""Finite tests of unary-team compression for standard inquisitive team logic.
No symbolic experiments here are used as proofs of unbounded expressivity.
"""
from itertools import combinations

def subsets(t):
    t=tuple(t)
    for k in range(len(t)+1):
        for u in combinations(t,k):
            yield frozenset(u)

def atom(kind, *terms): return ('atom', kind, *terms)
def neg(f): return ('imp',f,('bot',))
def cls_or(a,b): return neg(('and',neg(a),neg(b)))

EQ=atom('eq','x','y')
PX=atom('pred','x')
PY=atom('pred','y')

FORMULAS = [
 ('bot',), PX, ('imp',PX,('bot',)),
 ('some','y',EQ),
 ('all','y',('inqor',EQ,neg(EQ))),
 ('imp',('some','y',EQ),PX),
 ('some','y',('and',neg(EQ),PX)),
 ('all','y',('imp',EQ,PY)),
 ('imp',('some','y',neg(EQ)),('some','y',EQ)),
 ('inqor',('some','y',EQ),('all','y',PX)),
 ('some','y',('some','z',('and',atom('neq','y','z'),cls_or(atom('eq','x','y'),atom('eq','x','z'))))),
 ('imp',('all','y',('inqor',atom('eq','x','y'),neg(atom('eq','x','y')))),('bot',)),
]

def direct(f, team, P, D):
    tag=f[0]
    if tag=='bot': return not team
    if tag=='atom':
        kind,*vars=f[1:]
        if kind=='pred': return all(dict(s)[vars[0]] in P for s in team)
        if kind=='eq': return all(dict(s)[vars[0]]==dict(s)[vars[1]] for s in team)
        if kind=='neq':return all(dict(s)[vars[0]]!=dict(s)[vars[1]] for s in team)
        raise AssertionError(kind)
    if tag=='and':return direct(f[1],team,P,D) and direct(f[2],team,P,D)
    if tag=='inqor':return direct(f[1],team,P,D) or direct(f[2],team,P,D)
    if tag=='imp':return all(not direct(f[1],u,P,D) or direct(f[2],u,P,D) for u in subsets(team))
    if tag in ('all','some'):
        y,sub=f[1:]
        results=[]
        for d in D:
            updated=frozenset(tuple(sorted({**dict(s),y:d}.items())) for s in team)
            results.append(direct(sub,updated,P,D))
        return all(results) if tag=='all' else any(results)
    raise AssertionError(tag)

def compressed(f, S, env, P, D):
    tag=f[0]
    if tag=='bot':return not S
    if tag=='atom':
        kind,*vars=f[1:]
        get=lambda var,x: x if var=='x' else env[var]
        if kind=='pred':return all(get(vars[0],x) in P for x in S)
        if kind=='eq':return all(get(vars[0],x)==get(vars[1],x) for x in S)
        if kind=='neq':return all(get(vars[0],x)!=get(vars[1],x) for x in S)
        raise AssertionError(kind)
    if tag=='and':return compressed(f[1],S,env,P,D) and compressed(f[2],S,env,P,D)
    if tag=='inqor':return compressed(f[1],S,env,P,D) or compressed(f[2],S,env,P,D)
    if tag=='imp':return all(not compressed(f[1],U,env,P,D) or compressed(f[2],U,env,P,D) for U in subsets(S))
    if tag in ('all','some'):
        y,sub=f[1:]
        results=[compressed(sub,S,{**env,y:d},P,D) for d in D]
        return all(results) if tag=='all' else any(results)
    raise AssertionError(tag)

def check():
    tested=0
    for n in range(1,5):
        D=tuple(range(n))
        signatures={}
        for P in subsets(D):
            for X in subsets(D):
                team=frozenset((('x',x),) for x in X)
                profile=(len(X&P),len(P-X),len(X-P),len(set(D)-(X|P)))
                result=[]
                for f in FORMULAS:
                    left=direct(f,team,P,D)
                    right=compressed(f,X,{},P,D)
                    assert left==right,(n,P,X,f,left,right)
                    result.append(left)
                    tested+=1
                result=tuple(result)
                key=(n,profile)
                if key in signatures:assert signatures[key]==result,(key,result,signatures[key])
                signatures[key]=result
        print('UNARY_COMPRESSION_AND_COLOR_INVARIANCE_OK',n, tested)
    # Direct checks that <=k and complement >=d are correct on nonempty teams.
    for n in range(1,6):
        D=tuple(range(n))
        for X in subsets(D):
            team=frozenset((('x',x),) for x in X)
            for k in range(4):
                if k==0: formula=('bot',)
                else:
                    ors=atom('eq','x','y0')
                    for i in range(1,k):ors=cls_or(ors,atom('eq','x','y'+str(i)))
                    formula=ors
                    for i in reversed(range(k)):formula=('some','y'+str(i),formula)
                actual=direct(formula,team,frozenset(),D)
                expected=(not X or len(X)<=k)
                assert actual==expected,(n,X,k,'upper')
            for d in range(4):
                if d==0:formula=('imp',('bot',),('bot',))
                else:
                    atoms=[atom('neq','x','y'+str(i)) for i in range(d)]
                    atoms += [atom('neq','y'+str(i),'y'+str(j)) for i in range(d) for j in range(i+1,d)]
                    formula=atoms[0]
                    for aa in atoms[1:]:formula=('and',formula,aa)
                    for i in reversed(range(d)):formula=('some','y'+str(i),formula)
                actual=direct(formula,team,frozenset(),D)
                expected=(not X or n-len(X)>=d)
                assert actual==expected,(n,X,d,'outside')
    print('UNARY_TEAM_FORMULA_SCHEMES_OK')
    print('INQUISITIVE_UNARY_CHECK_OK', tested)

if __name__=='__main__':check()
