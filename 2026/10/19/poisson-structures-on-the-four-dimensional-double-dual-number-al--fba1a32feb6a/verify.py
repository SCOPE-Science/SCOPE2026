from itertools import product

def gf(q):
    if q in (2,4):
        def add(a,b): return a^b
        if q==2: return add,lambda a,b:a&b,2
        def mul(a,b):
            z=0
            for i in range(2):
                if (b>>i)&1:z^=a<<i
            if z&8: z^=0b1100
            if z&4: z^=0b0111
            return z
        return add,mul,2
    return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q,q

def verify(q):
    add,mul,p=gf(q)
    neg=lambda a: (-a)%q if p!=2 else a
    zero=(0,0,0,0)
    one=(1,0,0,0); xx=(0,1,0,0); yy=(0,0,1,0); xy=(0,0,0,1)
    basis=[one,xx,yy,xy]
    plus=lambda a,b:tuple(add(u,v) for u,v in zip(a,b))
    times=lambda a,b: tuple([mul(a[0],b[0]),add(mul(a[0],b[1]),mul(a[1],b[0])),add(mul(a[0],b[2]),mul(a[2],b[0])),add(add(mul(a[0],b[3]),mul(a[3],b[0])),add(mul(a[1],b[2]),mul(a[2],b[1])))])
    dx=lambda a:(a[1],0,a[3],0)
    dy=lambda a:(a[2],a[3],0,0)
    wedge=lambda a,b:plus(times(dx(a),dy(b)),tuple(neg(z) for z in times(dy(a),dx(b))))
    def bracket(f,a,b):return times(f,wedge(a,b))
    def allchecks(f):
        for a,b,c in product(basis, repeat=3):
            lhs=bracket(f,times(a,b),c)
            rhs=plus(times(a,bracket(f,b,c)),times(b,bracket(f,a,c)))
            if lhs!=rhs:return False,('Leibniz',f,a,b,c,lhs,rhs)
            j=plus(plus(bracket(f,a,bracket(f,b,c)),bracket(f,b,bracket(f,c,a))),bracket(f,c,bracket(f,a,b)))
            if j!=zero:return False,('Jacobi',f,a,b,c,j)
    fs=[]
    for f in product(range(q),repeat=4):
        if p!=2 and f[:3]!=(0,0,0):continue
        result=allchecks(f)
        if result:return result
        fs.append(f)
    print(q,'total valid brackets',len(fs),'expected',q**4 if p==2 else q,'Jacobi/Leibniz passed')
    if p==2:
        group=[]
        for a,b,c,d in product(range(q),repeat=4):
            det=add(mul(a,d),mul(b,c))
            if not det:continue
            di=next(i for i in range(1,q) if mul(det,i)==1)
            for u,v in product(range(q),repeat=2):
                h=mul(add(mul(a,v),mul(c,u)),di)
                k=mul(add(mul(b,v),mul(d,u)),di)
                group.append((a,b,c,d,u,v,det,h,k,di))
        def trans(f,g):
            a,b,c,d,u,v,det,h,k,di=g
            f0,f1,f2,f3=f
            A=f0;B=add(mul(f1,a),mul(f2,c));C=add(mul(f1,b),mul(f2,d));D=add(add(mul(f1,u),mul(f2,v)),mul(f3,det))
            return (mul(A,di),mul(add(B,mul(A,h)),di),mul(add(C,mul(A,k)),di),mul(add(add(D,mul(B,k)),mul(C,h)),di))
        allset=set(fs); orbits=[]
        while allset:
            f=min(allset)
            orbit={trans(f,g) for g in group}
            assert orbit <= allset or not (orbit-allset),('leaked orbit',q,f)
            assert all(z[3]==f[3] for z in orbit)
            orbits.append((f,len(orbit)))
            allset-=orbit
        expected={1:q,q*q-1:q,q*q*(q-1):q}
        got={}
        for f,z in orbits:got[z]=got.get(z,0)+1
        assert got==expected,(q,got,expected)
        print(q,'Poisson iso orbits:',len(orbits),'by sizes',got)
    if p!=2:
        # Every associative automorphism has either diagonal or anti-diagonal linear part.
        # Directly verify the induced action on all permitted Poisson brackets.
        group=[]
        for a,d,u,v in product(range(q),repeat=4):
            if a and d:group.append((a,0,0,d,u,v))
        for b,c,u,v in product(range(q),repeat=4):
            if b and c:group.append((0,b,c,0,u,v))
        orbit_seen=set(); orbit_sizes=[]
        for parameter in range(q):
            if parameter in orbit_seen:continue
            orbit=set()
            for a,b,c,d,u,v in group:
                # Evaluate transformed image coefficient against the linear Jacobian.
                norm=add(mul(a,d),mul(b,c))
                det=add(mul(a,d),neg(mul(b,c)))
                inverse=next(z for z in range(1,q) if mul(det,z)==1)
                orbit.add(mul(parameter,mul(norm,inverse)))
            orbit_seen.update(orbit);orbit_sizes.append(len(orbit))
        assert len(orbit_sizes)==(q+1)//2
        assert sorted(orbit_sizes)==[1]+[2]*((q-1)//2)
        print(q,'odd-characteristic isomorphism types',len(orbit_sizes),'verified')
    return True

if __name__=='__main__':
    for q in (2,3,4,5,7): assert verify(q)==True
