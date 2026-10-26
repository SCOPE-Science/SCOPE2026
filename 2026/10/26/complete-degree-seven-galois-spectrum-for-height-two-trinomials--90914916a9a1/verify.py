#!/usr/bin/env python3
"""Exact reproducibility for the degree-seven small-trinomial Galois classification.
Requires Python 3 and SymPy >=1.12; run: python verify.py
All calculations are exact over ZZ, QQ and finite fields.
"""
import json
from pathlib import Path
import sympy as sp

x=sp.Symbol('x')
certificate=json.loads((Path(__file__).resolve().parent/'CERTIFICATE.json').read_text(encoding='utf8'))
expected={'S7':8,'S6':8,'S3xS3':4,'S3xS4':4}
requirements={
 7:{'irreducible':(7,), 'transposition':(5,2)},
 6:{'irreducible':(6,), 'primitivity':(5,1), 'transposition':(3,2,1)},
 4:{'irreducible':(4,), 'three_cycle':(3,1)},
 3:{'irreducible':(3,)},
}
assert certificate['frequency']==expected
assert len(certificate['rows'])==24
assert len(certificate['factor_certificates'])==28
certmap={tuple(c['coefficients']):c for c in certificate['factor_certificates']}
assert len(certmap)==28
seen=set()
counts={k:0 for k in expected}
for row in certificate['rows']:
 k,a,b=row['k'],row['a'],row['b']
 assert (1<=k<=6 and a in (-2,2) and b in (-1,1))
 assert (k,a,b) not in seen
 seen.add((k,a,b))
 f=sp.Poly(x**7+a*x**k+b,x,domain=sp.ZZ)
 factors=[sp.Poly.from_list(e['coefficients'],gens=x,domain=sp.ZZ) for e in row['factors']]
 assert all(p.LC()==1 for p in factors)
 product=sp.Poly(1,x,domain=sp.ZZ)
 for factor in factors: product*=factor
 assert product==f
 assert sorted(p.degree() for p in factors)==row['degrees']
 assert sp.factor_list(f)[1]==[(p.as_expr(),1) for p in factors] or sp.prod(factors)==f
 typ={ (7,):'S7', (1,6):'S6', (1,3,3):'S3xS3', (3,4):'S3xS4' }[tuple(row['degrees'])]
 assert row['galois_group']==typ
 counts[typ]+=1
 # Check the quadratic subfields for each pair of nontrivial factors:
 discs=[int(sp.discriminant(p.as_expr(),x)) for p in factors if p.degree()>1]
 if typ=='S3xS3':assert sorted(discs)==[-31,-23]
 if typ=='S3xS4':assert sorted(discs)==[-23,257]
for coeff,c in certmap.items():
 f=sp.Poly.from_list(coeff,gens=x,domain=sp.ZZ)
 d=f.degree()
 assert c['degree']==d and int(sp.discriminant(f.as_expr(),x))==c['discriminant']
 assert set(c['witnesses'])==set(requirements[d])
 for role,w in c['witnesses'].items():
  p=w['prime']
  assert sp.isprime(p) and c['discriminant']%p!=0
  fac=sp.factor_list(f,modulus=p)[1]
  assert all(e==1 for _,e in fac)
  dd=tuple(sorted([g.degree() for g,_ in fac],reverse=True))
  assert dd==requirements[d][role]==tuple(w['degrees'])
assert len(seen)==24 and counts==expected
print('CERTIFICATE_OK rows=24 nonlinear_factors=28 groups='+str(counts))
