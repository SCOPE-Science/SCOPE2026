"""Exhaustive independent checks for determinants of normalized symmetric circulants.
Run with Python 3: python verify.py. Requires only the standard library.
"""
from collections import Counter
from itertools import product


class Field:
    def __init__(self, q):
        self.q = q
        if q == 9:
            self.p = 3
            def unpack(x): return x % 3, x // 3
            def add(x,y):
                a,b=unpack(x); c,d=unpack(y)
                return (a+c)%3+3*((b+d)%3)
            def mul(x,y):
                a,b=unpack(x); c,d=unpack(y)
                return (a*c-b*d)%3+3*((a*d+b*c)%3)
        else:
            self.p = q
            def add(x,y): return (x+y)%q
            def mul(x,y): return (x*y)%q
        self.add = [[add(x,y) for y in range(q)] for x in range(q)]
        self.mul = [[mul(x,y) for y in range(q)] for x in range(q)]
        self.neg = [next(y for y in range(q) if self.add[x][y] == 0) for x in range(q)]
        self.inv = [0] + [next(y for y in range(1,q) if self.mul[x][y] == 1) for x in range(1,q)]
    def difference(self,x,y): return self.add[x][self.neg[y]]


def determinant(rows,F):
    a=[row[:] for row in rows]
    n=len(a); answer=1
    for j in range(n):
        piv=next((i for i in range(j,n) if a[i][j]!=0), None)
        if piv is None:return 0
        if piv!=j:
            a[j],a[piv]=a[piv],a[j]
            answer=F.neg[answer]
        v=a[j][j]
        answer=F.mul[answer][v]
        inv=F.inv[v]
        for i in range(j+1,n):
            coeff=F.mul[a[i][j]][inv]
            if not coeff:continue
            for k in range(j+1,n):
                a[i][k]=F.difference(a[i][k],F.mul[coeff][a[j][k]])
            a[i][j]=0
    return answer


def orbit_profile(m,q):
    unseen=set(range(1,m))
    if m%2==0:unseen.discard(m//2)
    result=[]
    while unseen:
        root=min(unseen); orbit={root}; todo=[root]
        for x in todo:
            for y in ((q*x)%m,(-x)%m):
                if y not in orbit:
                    orbit.add(y); todo.append(y)
        assert len(orbit)%2 == 0
        unseen -= orbit
        result.append(len(orbit)//2)
    assert sum(result)==(m-1)//2 if m%2 else sum(result)==(m-2)//2
    return sorted(result)


def expected(n,F):
    p=F.p;q=F.q;m=n
    while m%p==0:m//=p
    orbit_degrees=orbit_profile(m,q)
    lifts=q**((n-m)//2)
    if m==1:return {1:q**((n-1)//2)},orbit_degrees
    U=1
    for e in orbit_degrees:U*=q**e-1
    if n%2==0:
        count=Counter({0:q**(n//2)-lifts*(q-1)*U})
        for z in range(1,q):count[z]=lifts*U
        return dict(count),orbit_degrees
    assert U%(q-1)==0
    count=Counter({0:q**((n-1)//2)-lifts*U})
    squares={F.mul[x][x] for x in range(1,q)}
    assert len(squares)==(q-1)//2
    for s in squares:count[s]=2*lifts*U//(q-1)
    return dict(count),orbit_degrees


def actual(n,F):
    q=F.q;d=n//2
    counts=Counter()
    for params in product(range(q),repeat=d):
        row=[0]*n
        s=0
        for j,val in enumerate(params,1):
            row[j]=row[n-j]=val
            if n%2==0 and j==d:s=F.add[s][F.mul[1][val]]
            else:s=F.add[s][F.add[val][val]]
        row[0]=F.difference(1,s)
        matrix=[[row[(j-i)%n] for j in range(n)] for i in range(n)]
        counts[determinant(matrix,F)]+=1
    return dict(counts)


def run():
    cases=0;matrices=0;zero_counts=0;special=0
    settings={3:[1,2,3,4,5,6,7,8,9,10,11],5:[1,2,3,4,5,6,7,8,9,10],7:[1,2,3,4,5,6,7,8],11:[1,2,3,4,5,6,7],9:[1,2,3,4,5,6,7,8]}
    for q,ns in settings.items():
        F=Field(q)
        for n in ns:
            want,exponents=expected(n,F)
            got=actual(n,F)
            assert all(got.get(x,0)==want.get(x,0) for x in range(q)),(q,n,want,got,exponents)
            assert sum(got.values())==q**(n//2)
            cases+=1; matrices+=q**(n//2);zero_counts+=got.get(0,0)
            if n%F.p==0:special+=1
    print('VERIFY_OK fields=5 cases=%d matrices=%d zero_determinants=%d characteristic_divides_order_cases=%d' %(cases,matrices,zero_counts,special))

if __name__=='__main__':run()
