from itertools import product

def count(q,r):
    F=list(range(q))
    basis=list(product(F,repeat=4))
    good=[]
    for a,d,c,e in basis:
        if (a*e+d*c)%q==0:good.append((a,d,c,e))
    # Count r=2 only without f; direct matrices 16? q3 81^2, fine
    counts=[0,0,0,0]
    for seq in product(good,repeat=r):
        if any((u[0]*v[3]+u[3]*v[0]+u[1]*v[2]+u[2]*v[1])%q for u,v in zip(seq,seq[1:])):continue
        cols=[(v[0],-v[2]) for v in seq]+[(v[1],v[3]) for v in seq]
        rows=[(v[0],v[1]) for v in seq]+[(-v[2],v[3]) for v in seq]
        rank_one=lambda xs: all((x[0]*y[1]-x[1]*y[0])%q==0 for i,x in enumerate(xs) for y in xs[i+1:])
        im=rank_one(cols);ker=rank_one(rows)
        assert im or ker
        counts[0]+=1
        counts[1]+=im
        counts[2]+=ker
        counts[3]+=im and ker
    expected_total=1+(q+1)**2*(q**r-1)+2*(q+1)*(q**r-1)*(q**r-q)
    expected_one=1+(q+1)**2*(q**r-1)+(q+1)*(q**r-1)*(q**r-q)
    expected_both=1+(q+1)**2*(q**r-1)
    print(q,r,counts,[expected_total,expected_one,expected_one,expected_both]);assert counts==[expected_total,expected_one,expected_one,expected_both]
for q in (2,3,5):count(q,2)
print('RULINGS_INTERSECTION_OK')
