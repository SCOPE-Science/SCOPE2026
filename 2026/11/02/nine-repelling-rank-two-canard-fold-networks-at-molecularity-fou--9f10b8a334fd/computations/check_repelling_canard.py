"""Exact complete three-reaction canard-molecularity census.

Standard-library-only. Enumerates unordered triples of distinct directed
reactions among nonnegative integer two-species complexes of degree <= d.
Rates are unrestricted positive constants. The X component is fast.
"""
from itertools import combinations
from functools import reduce
from math import gcd
from pathlib import Path

def complexes(d):
    return tuple((a,b) for a in range(d+1) for b in range(d+1-a))

def reactions(d):
    cs=complexes(d)
    return tuple((source,target,target[0]-source[0],target[1]-source[1])
                 for source in cs for target in cs if source != target)

def cross(u,v):
    return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])

def dot(u,v):
    return sum(a*b for a,b in zip(u,v))

def primitive(u):
    g=reduce(gcd,u)
    return tuple(x//g for x in u)

def classify(rows):
    N=tuple(r[2] for r in rows)
    M=tuple(r[3] for r in rows)
    a=tuple(r[0][0] for r in rows)
    b=tuple(r[0][1] for r in rows)
    raw=cross(N,tuple(N[i]*a[i] for i in range(3)))
    if not (all(t>0 for t in raw) or all(t<0 for t in raw)):
        return None
    if dot(M,raw)!=0:
        return None
    flux=primitive(raw if raw[0]>0 else tuple(-t for t in raw))
    moments=(dot(tuple(N[i]*a[i]*(a[i]-1) for i in range(3)),flux),
             dot(tuple(N[i]*b[i] for i in range(3)),flux),
             dot(tuple(M[i]*a[i] for i in range(3)),flux),
             dot(tuple(M[i]*b[i] for i in range(3)),flux))
    return flux,moments

def census(d):
    counts={'rank_two_positive_null':0,'canard':0,'negative':0,'zero':0,'positive':0}
    positive=[]
    for rows in combinations(reactions(d),3):
        x=classify(rows)
        if x is None:continue
        counts['rank_two_positive_null']+=1
        flux,(n20,n01,m10,m01)=x
        if n20 == 0 or n01*m10 >= 0:continue
        counts['canard']+=1
        sign='positive' if m01>0 else 'negative' if m01<0 else 'zero'
        counts[sign]+=1
        if m01>0:positive.append((rows,flux,(n20,n01,m10,m01)))
    assert counts['canard']==counts['negative']+counts['zero']+counts['positive']
    return counts,positive

def reaction_text(row):
    source,target,_,_=row
    return '{}:{}>{}:{}'.format(source[0],source[1],target[0],target[1])

def table():
    results={}
    for d in (2,3,4):
        ct,sol=census(d)
        print('d=%s complexes=%s directed_reactions=%s %s' % (d,len(complexes(d)),len(reactions(d)),ct))
        results[d]=ct
        if d==4:
            assert len(sol)==9
            lines=['row\treaction_1\treaction_2\treaction_3\tflux_1\tflux_2\tflux_3\tn20\tn01\tm10\tm01']
            for j,(rows,flux,moments) in enumerate(sol,1):
                lines.append('\t'.join(map(str,[j]+[reaction_text(row) for row in rows]+list(flux)+list(moments))))
            data='\n'.join(lines)+'\n'
            print(data)
    assert results[2]=={'rank_two_positive_null':0,'canard':0,'negative':0,'zero':0,'positive':0}
    assert results[3]=={'rank_two_positive_null':82,'canard':16,'negative':11,'zero':5,'positive':0}
    assert results[4]=={'rank_two_positive_null':1590,'canard':350,'negative':278,'zero':63,'positive':9}
    assert any([reaction_text(row) for row in rows]==['0:2>1:3','1:0>0:0','2:1>3:0']
               and flux==(1,2,1) and moments==(2,3,-2,1)
               for rows,flux,moments in census(4)[1])
    return data

if __name__=='__main__':
    result=table()
    Path(__file__).with_name('repelling_canard_molecularity4.tsv').write_text(result,encoding='utf-8')
    print('PASS: exact exhaustive finite classification and concrete positive-trace witness')
