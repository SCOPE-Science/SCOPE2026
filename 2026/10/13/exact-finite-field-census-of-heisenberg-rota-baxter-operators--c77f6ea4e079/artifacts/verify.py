from itertools import product

def bracket(x,y,q):
    # basis c,e,f; [e,f]=c
    return ((x[1]*y[2]-x[2]*y[1])%q,0,0)

def mv(M,x,q):
    return tuple(sum(M[i][j]*x[j] for j in range(3))%q for i in range(3))

def add(x,y,q): return tuple((x[i]+y[i])%q for i in range(3))
def scale(a,x,q): return tuple(a*t%q for t in x)

def rb(M,lam,q):
    E=[(1,0,0),(0,1,0),(0,0,1)]
    for x in E:
        for y in E:
            Rx,Ry=mv(M,x,q),mv(M,y,q)
            lhs=add(bracket(Rx,Ry,q),scale(lam,mv(M,bracket(x,y,q),q),q),q)
            rhs=mv(M,add(bracket(Rx,y,q),bracket(x,Ry,q),q),q)
            if lhs!=rhs: return False
    return True

def det(M,q):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%q

def expected_total(q,lam):
    return q**6 if lam==0 else q**6+q**4

def expected_inv(q,lam):
    if lam==0: return q**3*(q-1)*(q*q-q-1)
    return q**3*(q**3-2*q*q+2)

# Full q^9 enumeration, independent of the reduced equations.
for q in (2,3):
    for lam in (0,1):
        n=inv=0
        for ent in product(range(q),repeat=9):
            M=(ent[0:3],ent[3:6],ent[6:9])
            if rb(M,lam,q):
                n+=1
                inv+=det(M,q)!=0
        assert n==expected_total(q,lam),(q,lam,n)
        assert inv==expected_inv(q,lam),(q,lam,inv)
        print({'full':True,'q':q,'weight':lam,'count':n,'invertible':inv})

# Reduced equation in column convention R(c),R(e),R(f).
for q in (2,3,5,7):
    for lam in (0,1):
        n=inv=0
        for x,alpha,beta,y,u,v,z in product(range(q),repeat=7):
            if ((y-x)*z-(x*y-lam*x+u*v))%q: continue
            M=((x,alpha,beta),(0,y,u),(0,v,z))
            assert rb(M,lam,q)
            n+=1; inv+=det(M,q)!=0
        assert n==expected_total(q,lam)
        assert inv==expected_inv(q,lam)
        print({'q':q,'weight':lam,'count':n,'invertible':inv})
print('VERIFY_OK')
