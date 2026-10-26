"""Exhaustive 2x2 Jordan-plane representation counts over selected finite fields.

Run: python verify.py
The loops check XY-YX=Y^2 literally, without using the proof's geometric
classification. They also verify every fixed-Y fiber and the claimed
set-theoretic component equations.
"""
from itertools import product


def field_tables(q):
    if q in (2, 3, 5, 7):
        return ([[ (a+b)%q for b in range(q)] for a in range(q)],
                [[ (a*b)%q for b in range(q)] for a in range(q)])
    if q == 4:
        add = [[a^b for b in range(4)] for a in range(4)]
        def mul(a,b):
            v=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1:
                        v^=1<<(i+j)
            if v&4:
                v^=7  # x^2 = x+1 in F2[x]/(x^2+x+1)
            return v
        return add,[[mul(a,b) for b in range(4)] for a in range(4)]
    raise ValueError('unsupported test field')


def check(q):
    add,mul=field_tables(q)
    neg=lambda a: next(i for i in range(q) if add[a][i] == 0)
    z=[neg(a) for a in range(q)]
    mats=list(product(range(q),repeat=4))
    tr=lambda a:add[a[0]][a[3]]
    det=lambda a:add[mul[a[0]][a[3]]][z[mul[a[1]][a[2]]]]
    def mm(x,y):
        return (add[mul[x[0]][y[0]]][mul[x[1]][y[2]]],
                add[mul[x[0]][y[1]]][mul[x[1]][y[3]]],
                add[mul[x[2]][y[0]]][mul[x[3]][y[2]]],
                add[mul[x[2]][y[1]]][mul[x[3]][y[3]]])
    def is_solution(x,y):
        a=mm(x,y);b=mm(y,x);c=mm(y,y)
        return all(add[a[j]][z[b[j]]]==c[j] for j in range(4))
    # Literal matrix multiplication test, with no use of rank or trace
    count=0; fibcounts={}; maincount=0; flatcount=0; intersection=0
    for y in mats:
        fy=0
        for x in mats:
            if not is_solution(x,y):
                continue
            count+=1;fy+=1
            flat = y==(0,0,0,0)
            if q%2==0:
                a,b,c,_=y
                u,v,w,_=x
                f=add[mul[a][a]][add[mul[b][c]][add[mul[v][c]][mul[b][w]]]]
                main = (tr(x)==0 and tr(y)==0 and f==0)
            else:
                disc=add[mul[tr(x)][tr(x)]][z[mul[4%q][det(x)]]]
                main=(tr(y)==0 and det(y)==0 and disc==0)
            assert main or flat,(q,x,y)
            maincount+=main;flatcount+=flat;intersection+=main and flat
        fibcounts[y]=fy
        if q%2==0:
            expected = q**4 if y==(0,0,0,0) else (q**2 if tr(y)==0 and (y[1]!=0 or y[2]!=0) else 0)
        else:
            expected = q**4 if y==(0,0,0,0) else (q**2 if tr(y)==0 and det(y)==0 else 0)
        assert fy==expected,(q,y,fy,expected)
    expected_count = q**5+q**4-q**3 if q%2==0 else 2*q**4-q**2
    if q%2==0:
        expected_parts=(q**5,q**4,q**3)
    else:
        expected_parts=(q**4+q**3-q**2,q**4,q**3)
    assert count==expected_count,(q,count,expected_count)
    assert (maincount,flatcount,intersection)==expected_parts,(q,(maincount,flatcount,intersection),expected_parts)
    print('q=',q,'total=',count,'main/flat/intersection=',(maincount,flatcount,intersection),'PASS')

if __name__ == '__main__':
    for q in (2,3,4,5,7):
        check(q)
    print('JORDAN_PLANE_MODULAR_2X2_OK')
