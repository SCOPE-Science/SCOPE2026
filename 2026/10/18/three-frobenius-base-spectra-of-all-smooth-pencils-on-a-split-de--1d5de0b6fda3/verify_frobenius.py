#!/usr/bin/env python3
"""Exact finite-extension certification of the geometric pencil base schemes.
Pure Python. Computes all 13 orbit representatives over F_{2^k}, k=1..7.
Together with Bezout degree 9, the counted points prove geometric reducedness.
"""
from verify_exact import classify, BASIS
from collections import Counter
import csv,json

IRRED={1:0b11,2:0b111,3:0b1011,4:0b10011,
       5:0b100101,6:0b1000011,7:0b10000011}


def mul(a,b,n):
    out=0; q=1<<n;poly=IRRED[n]
    while b:
        if b&1:out^=a
        b>>=1
        a<<=1
        if a&q:a^=poly
    return out


def field(n):
    q=1<<n
    table=[[mul(a,b,n) for b in range(q)] for a in range(q)]
    for a in range(1,q):
        assert set(table[a][1:])==set(range(1,q)), 'not a field polynomial'
    return table


def monvals(point,t):
    x,y,z=point
    x2=t[x][x];y2=t[y][y];z2=t[z][z]
    return (t[x2][y],t[x2][z],t[x][y2],t[y2][z],
            t[x][z2],t[y][z2],t[t[x][y]][z],t[z2][z])


def base_counts(reps,n):
    t=field(n);q=1<<n
    rows=[(1,y,z) for y in range(q) for z in range(q)]
    rows.extend((0,1,z) for z in range(q))
    rows.append((0,0,1))
    counts=[0]*len(reps)
    for point in rows:
        v=monvals(point,t)
        for j,rep in enumerate(reps):
            f,g=rep[:2]
            u=0;w=0
            for i in range(8):
                if f>>i&1:u^=v[i]
                if g>>i&1:w^=v[i]
            counts[j]+=u==0 and w==0
    return counts


def mobius_inverse(N):
    a=[]
    for k in range(1,8):
        rem=N[k-1]-sum(d*a[d-1] for d in range(1,k) if k%d==0)
        assert rem>=0 and rem%k==0
        a.append(rem//k)
    return a


def execute():
    S,P,orbits=classify()
    reps=[r['rep'] for r in orbits]
    by_rep=[[] for _ in reps]
    for n in range(1,8):
        c=base_counts(reps,n)
        for i,v in enumerate(c):by_rep[i].append(v)
    out=[]
    for i,r in enumerate(orbits):
        N=by_rep[i]
        a=mobius_inverse(N)
        degrees=tuple(d for d in range(1,8) for _ in range(a[d-1]))
        total=sum(degrees)
        assert total==9, (r,degrees,total)
        assert a[0]==r['b']
        assert degrees in ((1,1,1,6),(1,1,7),(1,1,2,5))
        out.append({'rep':list(r['rep']),'orbit_size':r['size'],
                    'base_extension_point_counts':N,'base_closed_degrees':degrees,
                    'residual_closed_degrees':tuple(sorted(degrees[2:])),
                    'rational_members_points':r['member_points']})
    frequencies=Counter(tuple(d['residual_closed_degrees']) for d in out for _ in range(d['orbit_size']))
    assert frequencies=={(1,6):48,(7,):32,(2,5):24}
    with open('orbit_frobenius.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['mask_1','mask_2','mask_3','orbit_size','smooth_member_point_counts',
                    'total_base_degrees','residual_base_degrees','N1','N2','N3','N4','N5','N6','N7'])
        for d in out:
            w.writerow([*d['rep'],d['orbit_size'],','.join(map(str,d['rational_members_points'])),
                ','.join(map(str,d['base_closed_degrees'])),','.join(map(str,d['residual_closed_degrees'])),
                *d['base_extension_point_counts']])
    return {'field_modulus_polynomials':{str(k):hex(v) for k,v in IRRED.items()},
            'pencil_total':len(P),'orbit_total':len(out),
            'frequency_by_residual_closed_degrees':{','.join(map(str,k)):v for k,v in frequencies.items()},
            'geometrically_reduced_all':True,'orbits':out}

if __name__=='__main__':
    print(json.dumps(execute(),indent=2,sort_keys=True))
