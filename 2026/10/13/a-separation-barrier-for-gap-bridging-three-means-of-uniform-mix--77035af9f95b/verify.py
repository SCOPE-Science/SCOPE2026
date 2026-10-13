"""Exact arithmetic checks for a two-interval quadratic quantization obstruction."""
from fractions import Fraction as F


def bridge_cost(p, u, v, gap):
    """Best three-cell error for left/core/right contiguous allocation (unit segments)."""
    q = 1 - p
    a, b = p * u, q * v
    within = (p*((1-u)**3+u**3) + q*((1-v)**3+v**3))/12
    mixing = a*b/(a+b) * (gap+(u+v)/2)**2
    return within+mixing


def anchored_cost(p):
    """Best of the two componentwise 2+1 quantizers (unit segments)."""
    q=1-p
    return min(p/F(48)+q/F(12),p/F(12)+q/F(48))


def assert_identity(p,u,v,g):
    q=1-p
    a,b=p*u,q*v
    saving_left = p*u*(1-u)/4
    saving_right = q*v*(1-v)/4
    cross=a*b/(a+b)*(g+(u+v)/2)**2
    assert bridge_cost(p,u,v,g) == F(1,12)-saving_left-saving_right+cross
    assert cross > min(saving_left,saving_right)
    assert bridge_cost(p,u,v,g)>anchored_cost(p)


def cell_integral(lo,hi,mean,weight):
    return weight*((hi-mean)**3-(lo-mean)**3)/3


def main():
    cases=0
    for pk in range(1,10):
        p=F(pk,10)
        for uk in range(1,10):
            for vk in range(1,10):
                u,v=F(uk,10),F(vk,10)
                for g in (F(3,4),F(1),F(2)):
                    assert_identity(p,u,v,g)
                    cases+=1
    # A symmetric centroidal candidate for gap 1/10, which is below the barrier.
    p=F(1,2); gap=F(1,10); u=v=F(3,10)
    centers=[F(7,20),F(21,20),F(7,4)]
    assert (centers[0]+centers[1])/2 == 1-u
    assert (centers[1]+centers[2])/2 == 1+gap+v
    exact=(cell_integral(F(0),1-u,centers[0],p)
          + cell_integral(1-u,F(1),centers[1],p)
          + cell_integral(1+gap,1+gap+v,centers[1],1-p)
          + cell_integral(1+gap+v,2+gap,centers[2],1-p))
    assert exact==bridge_cost(p,u,v,gap)==F(257,6000)
    assert exact<F(5,96)
    print('VERIFY_OK cases=%d small_gap_cost=%s split_cost=%s' % (cases,exact,F(5,96)))


if __name__=='__main__':
    main()
