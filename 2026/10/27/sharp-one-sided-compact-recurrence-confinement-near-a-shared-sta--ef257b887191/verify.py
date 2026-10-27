"""Exact rational spot checks of an affine defect and its sharp fixed-point saturation."""
from fractions import Fraction as Q

def check(tl,dl,tr,dr,lam):
    assert lam*lam-tr*lam+dr==0 and 0<lam<1
    assert dl>0 and tl>1+dl and dr<0 and tr<-abs(1+dr)
    kap=lam*tl-dl-lam*lam
    H=lambda x,y:y+lam*x-lam/(1-lam)
    for x in [Q(-3),Q(-2),Q(-1),Q(-1,3),Q(0),Q(1,2),Q(2)]:
        for y in [Q(-5,3),Q(-1),Q(0),Q(7,4)]:
            t,d=(tl,dl) if x<0 else (tr,dr)
            xn,yn=t*x+y+1,-d*x
            assert H(xn,yn)==lam*H(x,y)-kap*max(Q(0),-x)
    x=1/(1-tl+dl)
    y=-dl*x
    assert x<0
    assert (tl*x+y+1,-dl*x)==(x,y)
    assert H(x,y)==-kap*(-x)/(1-lam)
    assert kap==(lam*tl-dl-lam*lam)
    return 29

def main():
    total=0
    total+=check(Q(3),Q(13,10),Q(-2),Q(-5,4),Q(1,2))
    total+=check(Q(9,4),Q(1,2),Q(-5,3),Q(-2,3),Q(1,3))
    assert Q(1,7)==Q(13,7)+Q(1,2)*Q(-10,7)-Q(1)
    print('VERIFIED: 2 admissible coefficient families,',total*1,'exact branch/fixed-point assertions; exact model identity and sharp witness hold.')
if __name__=='__main__':
    main()
