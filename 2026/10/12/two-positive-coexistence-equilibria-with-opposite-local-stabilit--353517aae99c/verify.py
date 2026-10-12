from fractions import Fraction as Q

def exp_bounds(t, n=70):
    assert isinstance(t,Q) and 0<=t<Q(n+2)
    s=Q(1); term=Q(1)
    for k in range(1,n+1):
        term*=t/k; s+=term
    rest=term*t/Q(n+1) / (1-t/Q(n+2))
    return s, s+rest

def xdiff(x,h):
    # sign x/(exp(x)-1) - h/10
    l,u=exp_bounds(x)
    z=h/10
    low=x-z*(u-1); hi=x-z*(l-1)
    assert low>0 or hi<0,('x',x,low,hi)
    return 1 if low>0 else -1

def ydiff(y,h):
    # sign y/(1-exp(-y)) - 3*h/10
    l,u=exp_bounds(y);z=3*h/10
    if y>=z: return 1
    lo=z-(z-y)*u; hi=z-(z-y)*l
    assert lo>0 or hi<0,('y',y,lo,hi)
    return 1 if lo>0 else -1

def xy_brackets(h, steps=37):
    xl,xu=Q(1, 2**70),Q(6)
    yl,yu=Q(1, 2**70),Q(8)
    for i in range(steps):
        xm=(xl+xu)/2
        if xdiff(xm,h)>0: xl=xm
        else:xu=xm
        ym=(yl+yu)/2
        if ydiff(ym,h)>0:yu=ym
        else:yl=ym
    assert xdiff(xl,h)>0 and xdiff(xu,h)<0
    assert ydiff(yl,h)<0 and ydiff(yu,h)>0
    return (xl,xu),(yl,yu)

class I:
    def __init__(self,l,u=None):
        self.l=Q(l);self.u=Q(u) if u is not None else Q(l)
        assert self.l<=self.u
    def __add__(self,v):
        v=ii(v);return I(self.l+v.l,self.u+v.u)
    __radd__=__add__
    def __neg__(self):return I(-self.u,-self.l)
    def __sub__(self,v):return self+-ii(v)
    def __rsub__(self,v):return ii(v)+-self
    def __mul__(self,v):
        v=ii(v);terms=[a*b for a in (self.l,self.u) for b in (v.l,v.u)]
        return I(min(terms),max(terms))
    __rmul__=__mul__
    def __truediv__(self,v):
        v=ii(v);assert v.l*v.u>0
        return self*I(Q(1)/v.u,Q(1)/v.l)
    def __rtruediv__(self,v):return ii(v)/self
    def __repr__(self):return f'[{float(self.l):.12g},{float(self.u):.12g}]'
def ii(v):return v if isinstance(v,I) else I(v)

def invexp_interval(y):
    lo,hi=exp_bounds(y.l);lo2,hi2=exp_bounds(y.u)
    return I(Q(1)/hi2,Q(1)/lo)

def exp_interval(x):
    lo,hi=exp_bounds(x.l);lo2,hi2=exp_bounds(x.u)
    return I(lo,hi2)

def interval_xy(hlo,hhi):
    (xl1,xu1),(yl1,yu1)=xy_brackets(hlo)
    (xl2,xu2),(yl2,yu2)=xy_brackets(hhi)
    return I(xl2,xu1),I(yl1,yu2)

def interval_r(h):
    (xl,xu),(yl,yu)=xy_brackets(h)
    ex=exp_interval(I(xl,xu));ey=exp_interval(I(yl,yu))
    return ex*(ii(h)+ey)

def rsign(h):
    q=interval_r(h);R=Q(26)
    assert q.l>R or q.u<R,('rsign',h,q)
    return 1 if q.l>R else -1

def bisect_r(l,u,sl,su,steps=23):
    assert rsign(l)==sl and rsign(u)==su and sl!=su
    for i in range(steps):
        m=(l+u)/2;sm=rsign(m)
        if sm==sl:l=m
        else:u=m
    return l,u

def det3(M):
    a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def verify_box(l,u,label):
    h=I(l,u);x,y=interval_xy(l,u);E=invexp_interval(y);D=ii(1)+h*E
    aj=Q(1,10);aa=Q(3,10)
    J=[[1/D,-h,-h/D],[x/(h*D),aj*h,-x/D],[y/h,I(0),aa*h*E]]
    Jt=[[I(1 if i==j else 0)-J[i][j] for j in range(3)] for i in range(3)]
    c1=-(J[0][0]+J[1][1]+J[2][2]);c2=J[0][0]*J[1][1]-J[0][1]*J[1][0]+J[0][0]*J[2][2]-J[0][2]*J[2][0]+J[1][1]*J[2][2]-J[1][2]*J[2][1];c3=-det3(J)
    signs=[1+c1+c2+c3,1-c1+c2-c3,1-c2+c1*c3-c3*c3,1+c3,1-c3]
    print(label,'h',h,'x',x,'y',y,'p(1)',det3(Jt),'jury',signs)
    if label=='stable':
        for v in signs:assert v.l>0
    else:assert det3(Jt).u<0
    return J

if __name__=='__main__':
    lo1,hi1=bisect_r(Q(49,10),Q(5),1,-1)
    lo2,hi2=bisect_r(Q(9),Q(19,2),-1,1)
    verify_box(lo1,hi1,'stable');verify_box(lo2,hi2,'unstable')
    print('VERIFY_OK')
