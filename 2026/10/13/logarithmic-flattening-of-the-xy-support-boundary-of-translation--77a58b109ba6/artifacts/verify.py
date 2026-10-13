#!/usr/bin/env python3
import math
def energy(g,n=20000):
    h=(math.pi/2)/n
    def f(x): return math.sqrt(1-(1-g*g)*math.sin(x)**2)
    s=f(0)+f(math.pi/2)
    s+=4*sum(f((2*j-1)*h) for j in range(1,n//2+1))
    s+=2*sum(f(2*j*h) for j in range(1,n//2))
    return -(h*s/3)/(4*math.pi)
def asym(g):
    L=math.log(4/g)
    return -1/(4*math.pi)-g*g/(8*math.pi)*(L-.5)-3*g**4/(64*math.pi)*(L-13/12)
def ep1(g):
    L=math.log(4/g); return -g/(4*math.pi)*(L-1)
def ep2(g):
    L=math.log(4/g); return -L/(4*math.pi)+1/(2*math.pi)
def main():
    qs=[]; cs=[]
    for g in (0.1,0.03,0.01):
        q=(energy(g)-asym(g))/(g**6*math.log(1/g)); qs.append(q)
        a=ep1(g); g2=-1/ep2(g)
        cs.append(g2*math.log(1/abs(a))/(4*math.pi))
    assert all(-0.012<q<-0.008 for q in qs)
    assert abs(qs[-1]-qs[-2])<abs(qs[-2]-qs[-3])
    assert 1.0<cs[2]<cs[1]<cs[0]<2.5
    print("VERIFY_OK remainder="+",".join(f"{x:.9f}" for x in qs)+" curvature_ratio="+",".join(f"{x:.9f}" for x in cs))
if __name__=="__main__": main()
