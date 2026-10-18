"""Independent exact arithmetic checks for Lights Out on Cartesian products of cliques."""
from itertools import product
from math import prod

def prediction(qs):
    d=len(qs)
    odds=[q for q in qs if q%2]
    evens=[q for q in qs if q%2==0]
    odd_total=prod(odds)
    odd_reduced=prod(q-2 for q in odds)
    scalar_zero_multiplicity=(odd_total + (1 if (d+1)%2==0 else -1)*odd_reduced)//2
    assert evens, "At least one even coordinate size is required"
    even_total=prod(evens)
    even_reduced=prod(q-2 for q in evens)
    return scalar_zero_multiplicity*((even_total+even_reduced)//2)

def matrix_rows(qs):
    d=len(qs)
    vertices=list(product(*(range(q) for q in qs)))
    at={v:i for i,v in enumerate(vertices)}
    rows=[]
    for v in vertices:
        row=1<<at[v]
        for j in range(d):
            for b in range(qs[j]):
                if b!=v[j]:
                    w=list(v);w[j]=b
                    row ^=1<<at[tuple(w)]
        rows.append(row)
    return vertices,rows

def nullity(rows):
    pivots={}
    for row in rows:
        while row:
            k=row.bit_length()-1
            if k not in pivots:
                pivots[k]=row;break
            row^=pivots[k]
    return len(rows)-len(pivots)

def test():
    verified=0;checks=0
    families=[]
    for d in range(2,5):
        for qs in product(range(2,5),repeat=d):
            if prod(qs)>180 or all(q%2 for q in qs):continue
            families.append(qs)
    for qs in families:
        vs,rows=matrix_rows(qs)
        expected=prediction(qs)
        actual=nullity(rows)
        assert actual==expected,(qs,expected,actual)
        even_coordinate_count=sum(q%2==0 for q in qs)
        if even_coordinate_count%2==0:
            x=(1<<len(vs))-1
        else:
            i=next(j for j,q in enumerate(qs) if q%2==0)
            x=sum(1<<t for t,v in enumerate(vs) if v[i]==0)
        assert all((row&x).bit_count()%2==1 for row in rows),qs
        assert (actual==0)==(len(qs)%2==0 and even_coordinate_count==len(qs)),qs
        verified+=1;checks+=len(vs)
    print('PASS',verified,'mixed-alphabet or all-even graph families,',checks,'exact toggle equations, ranks and nullities')
if __name__=='__main__':test()
