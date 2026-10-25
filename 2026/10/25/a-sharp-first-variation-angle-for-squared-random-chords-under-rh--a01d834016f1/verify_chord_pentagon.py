from fractions import Fraction as Q
from math import isqrt

V=[(0,0),(5070,0),(1619,3480),(1331,3600),(-3570,3600)]

def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def polygon_moments(V):
 n=len(V);pairs=list(zip(V,V[1:]+V[:1])); edges=[(b[0]-a[0],b[1]-a[1]) for a,b in pairs]
 cross=[a[0]*b[1]-a[1]*b[0] for a,b in pairs]
 assert all(edges[i][0]*edges[(i+1)%n][1]-edges[i][1]*edges[(i+1)%n][0]>0 for i in range(n))
 A=Q(sum(cross),2)
 cm=[sum(Q((a[j]+b[j])*cr,1) for ((a,b),cr) in zip(pairs,cross))/(6*A) for j in range(2)]
 area_second=sum(Q(cr*(dot(a,a)+dot(a,b)+dot(b,b)),1) for ((a,b),cr) in zip(pairs,cross))/(12*A)
 Iv=area_second-(cm[0]**2+cm[1]**2)
 lengths=[]
 for ex,ey in edges:
  k=isqrt(ex*ex+ey*ey);assert k*k==ex*ex+ey*ey
  lengths.append(k)
 P=sum(lengths)
 bm=[sum(Q((a[j]+b[j])*length,2) for ((a,b),length) in zip(pairs,lengths))/P for j in range(2)]
 bound_second=sum(Q(length*(dot(a,a)+dot(a,b)+dot(b,b)),3) for ((a,b),length) in zip(pairs,lengths))/P
 Bv=bound_second-(bm[0]**2+bm[1]**2)
 return A,P,cm,bm,Iv,Bv,Bv/Iv

# Independent evaluation from the rhombus's removal/addition moment formulas.
def analytic_rhombus(t, c, h):
    one=Q(1); a=t*t/2; q2=2*(one+c); perimeter=4+(h-2)*t
    f=((h-2)*t+(1-h)*t*t)/2
    G=Q(4,3)+h*t*((1+c)*(Q(1,2)-t)+t*t*(2+c)/3) - (t*(1+c)-t*t*(1+c)+Q(2,3)*t**3)
    bound_var=G/perimeter-f*f*q2/(perimeter**2)
    cap_var=t*t*(2-c)/18
    mu=Q(1,2)-t/3
    int_var=(Q(1,6)-a*cap_var)/(1-a)-a*q2*mu*mu/((1-a)**2)
    return bound_var/int_var

def main():
    A,P,ic,bc,iv,bv,R=polygon_moments(V)
    c=Q(-119,169);h=Q(24,13);t=Q(1,30)
    assert A==18241860 and P==20254
    assert R==Q(3586477854403938963,1792478301783239474)
    assert R-2==Q(1521250837460015,1792478301783239474)>0
    assert R==analytic_rhombus(t,c,h)
    first_variation=(h-2)*(1+3*c)/4
    assert first_variation>0
    for n in (100,1000,10000):
        slope=(analytic_rhombus(Q(1,n),c,h)-2)*n
        assert abs(slope-first_variation)<Q(10,n)
    print('PASS: strictly convex integer pentagon, exact moments, independent formula, local slope')
    print('Area:',A,'Perimeter:',P)
    print('Interior chord second moment:',2*iv)
    print('Boundary chord second moment:',2*bv)
    print('Ratio:',R)
    print('Excess over 2:',R-2)
    print('Rhombus first variation at rational angle:',first_variation)

if __name__=='__main__':
    main()
