#!/usr/bin/env python3
"""Symbolic extension-count certificate for thick partial geometries.
No third-party packages. Evaluates all ten ordered 2-types and their
possible one-point extension types from counting identities.
"""
from fractions import Fraction
from collections import defaultdict
import json

def profile(s,t,a):
    assert s>=2 and t>=2 and 1<=a<=min(s+1,t+1)
    v=Fraction((s+1)*(s*t+a),a)
    b=Fraction((t+1)*(s*t+a),a)
    k=s*(t+1);lam=s-1+t*(a-1);mu=a*(t+1)
    profiles={}
    def present(D):return tuple(sorted(key for key,count in D.items() if count>0))
    def check(D):
        assert all(x>=0 for x in D.values()),(s,t,a,D)
    def PP(s,t,a):
        v=Fraction((s+1)*(s*t+a),a);b=Fraction((t+1)*(s*t+a),a)
        k=s*(t+1); lam=s-1+t*(a-1); mu=a*(t+1)
        eq={('PE','PE'):1,('PC','PC'):k,('PN','PN'):v-1-k,('PI','PI'):t+1,('PO','PO'):b-t-1}
        col={('PE','PC'):1,('PC','PE'):1,
          ('PC','PC'):lam,('PC','PN'):k-1-lam,('PN','PC'):k-1-lam,('PN','PN'):v-2*k+lam,
          ('PI','PI'):1,('PI','PO'):t,('PO','PI'):t,('PO','PO'):b-2*t-1}
        non={('PE','PN'):1,('PN','PE'):1,
          ('PC','PC'):mu,('PC','PN'):k-mu,('PN','PC'):k-mu,('PN','PN'):v-2-2*k+mu,
          ('PI','PI'):0,('PI','PO'):t+1,('PO','PI'):t+1,('PO','PO'):b-2*t-2}
        check(eq);check(col)
        if a<=s:check(non)
        result={'PE':present(eq),'PC':present(col)}
        if a<=s:result['PN']=present(non)
        return result
    profiles.update(PP(s,t,a))
    maps={'PE':'LE','PC':'LM','PN':'LN','PI':'LI','PO':'LO'}
    for key,entries in PP(t,s,a).items():
        profiles[maps[key]]=tuple(sorted((maps[u],maps[v]) for u,v in entries))
    on={('PE','LI'):1,('PC','LI'):s,('PC','LO'):s*t,('PN','LO'):v-1-k,
        ('PI','LE'):1,('PI','LM'):t,('PO','LM'):s*t,('PO','LN'):b-1-(s+1)*t}
    off={('PE','LO'):1,('PC','LI'):a,('PN','LI'):s+1-a,('PC','LO'):k-a,
         ('PN','LO'):Fraction((s*t-a)*(s+1-a),a),
         ('PO','LE'):1,('PI','LM'):a,('PI','LN'):t+1-a,
         ('PO','LM'):(s+1)*t-a,('PO','LN'):Fraction((s*t-a)*(t+1-a),a)}
    check(on);check(off)
    profiles['PI']=present(on);profiles['PO']=present(off)
    profiles['LI']=tuple(sorted((v,u) for u,v in profiles['PI']))
    profiles['LO']=tuple(sorted((v,u) for u,v in profiles['PO']))
    return dict(sorted(profiles.items()))

def category(s,t,a):return ('2' if a==s+1 else ('1' if a==s else '0'))+('2' if a==t+1 else ('1' if a==t else '0'))

def main():
    from check_profiles import gq22,net3,td34,affine3,sts15,fano,dual,profile as direct
    gs=[gq22(),net3(),td34(),affine3(),sts15(),fano()]
    gs += [dual(g) for g in (td34(),affine3(),sts15())]
    for g in gs:
        observed,_=direct(g)
        predicted=profile(g['s'],g['t'],g['a'])
        observed={k:tuple(map(tuple,v)) for k,v in observed.items()}
        assert predicted==observed,(g['name'],{k:(predicted.get(k),observed.get(k)) for k in predicted if predicted.get(k)!=observed.get(k)})
    total=0;perclass=defaultdict(set)
    for s in range(2,81):
        for t in range(2,81):
            for a in range(1,min(s+1,t+1)+1):
                v=Fraction((s+1)*(s*t+a),a); b=Fraction((t+1)*(s*t+a),a)
                # Arithmetic feasibility is not an existence theorem.
                if v.denominator!=1 or b.denominator!=1:continue
                p=profile(s,t,a)
                perclass[category(s,t,a)].add(json.dumps(p,sort_keys=True))
                total+=1
    assert set(perclass)==set(x+y for x in '012' for y in '012')
    assert all(len(v)==1 for v in perclass.values()),{k:len(v) for k,v in perclass.items()}
    assert len({next(iter(v)) for v in perclass.values()})==9
    print('INDEPENDENT_DIRECT_EXAMPLES',len(gs))
    print('PARAMETER_TRIPLES_ARITHMETICALLY_ADMISSIBLE',total)
    print('CLASSES',','.join(sorted(perclass)))
    print('EACH_CLASS_HAS_UNIQUE_SUPPORT_PROFILE',True)
    print('ALL_NINE_SUPPORT_PROFILES_DISTINCT',True)
    print('PASS')
if __name__=='__main__':main()
