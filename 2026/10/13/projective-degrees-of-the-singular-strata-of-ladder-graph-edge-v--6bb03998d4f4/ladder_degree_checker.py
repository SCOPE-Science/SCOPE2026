"""Exact finite regression tests for projective edge varieties of ladder graphs.
Run: python3 ladder_degree_checker.py. No third-party dependencies.
This finite test does not prove the all-parameter theorem.
"""
from itertools import product

def gf_rank(rows, p=101):
    a = [r[:] for r in rows]
    piv = 0
    for col in range(len(a[0])):
        k = next((j for j in range(piv, len(a)) if a[j][col] % p), None)
        if k is None: continue
        a[piv], a[k] = a[k], a[piv]
        inv = pow(a[piv][col] % p, -1, p)
        a[piv] = [z*inv % p for z in a[piv]]
        for j in range(piv+1, len(a)):
            factor = a[j][col]
            if factor:
                a[j] = [(v-factor*w)%p for v,w in zip(a[j],a[piv])]
        piv += 1
        if piv == len(a): break
    return piv

def data(m):
    n=3*m+1
    v=lambda i: i
    u=lambda i: m+i
    w=lambda i: 2*m+i
    quads=[(v(i-1),v(i),u(i),w(i)) for i in range(1,m+1)]
    predicted=[]
    for i in range(1,m+1):
        basic={v(i-1),v(i),u(i),w(i)}
        neighbor_options=[]
        if i>1: neighbor_options.append((u(i-1),w(i-1)))
        if i<m: neighbor_options.append((u(i+1),w(i+1)))
        for selection in product(*neighbor_options):
            zeros=basic|set(selection)
            predicted.append(((1<<n)-1)^sum(1<<j for j in zeros))
    for i in range(1,m):
        zeros={v(i),u(i),w(i),u(i+1),w(i+1)}
        predicted.append(((1<<n)-1)^sum(1<<j for j in zeros))
    assert len(predicted)==len(set(predicted))==5*(m-1)
    degrees=[]
    for mask in predicted:
        complete=sum(all((mask>>j)&1 for j in q) for q in quads)
        degrees.append(2**complete)
    expected=(3*m-1)*2**(m-2)
    assert sum(degrees)==expected,(m,sum(degrees),expected)
    if m>2:
        assert degrees.count(2**(m-3))==4*(m-2)
        assert degrees.count(2**(m-2))==m+3
    admissible=[]
    singular=[]
    for mask in range(1,1<<n):
        if any(((mask>>a)&1)*((mask>>b)&1)!=((mask>>c)&1)*((mask>>d)&1) for a,b,c,d in quads):continue
        admissible.append(mask)
        jac=[]
        for a,b,c,d in quads:
            row=[0]*n
            row[a]=(mask>>b)&1;row[b]=(mask>>a)&1
            row[c]=-((mask>>d)&1);row[d]=-((mask>>c)&1)
            jac.append(row)
        if gf_rank(jac)<m:singular.append(mask)
    max_singular=[s for s in singular if not any(s!=t and (s&t)==s for t in singular)]
    assert set(max_singular)==set(predicted),('maximal support discrepancy',m,max_singular,predicted)
    print('m=%d admissible=%d singular=%d components=%d degree=%d degree_multiset=%s' %
          (m,len(admissible),len(singular),len(predicted),sum(degrees),sorted(degrees)))

if __name__=='__main__':
    for m in range(2,7):data(m)
    print('FINITE_CHECK_OK')
