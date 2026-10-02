"""Exact certificate replay with primitive scaling and complete gap checks."""
import json, math, runpy
from pathlib import Path
from fractions import Fraction as Q

def verify(root):
    ns=runpy.run_path(str(root/'verify_certificate.py'),run_name='certificate_library')
    def primitive(poly):
        denominator=math.lcm(*(c.denominator for c in poly))
        ints=[int(c*denominator) for c in poly];divisor=math.gcd(*ints)
        return [Q(c//divisor) for c in ints] if divisor else [Q(0)]
    cache={}
    def sturm(poly):
        key=tuple(poly)
        if key not in cache:
            seq=[primitive(poly),primitive([i*c for i,c in enumerate(poly)][1:])]
            while ns['poly_deg'](seq[-1])>0:
                seq.append(primitive([-c for c in ns['poly_rem'](seq[-2],seq[-1])]))
            cache[key]=seq
        return cache[key]
    ns['main'].__globals__['sturm_seq']=sturm
    ns['main'](str(root))
    R=ns['load_coeffs'](str(root/'R_coeffs.txt'))
    D=ns['poly_sub'](ns['poly_mul']([i*R[i] for i in range(1,len(R))],[Q(1),Q(0),Q(1)]),[Q(0)]+[48*c for c in R])
    pieces={'P1':(Q(0),Q('1.506')),'P2':(Q('2.014'),Q(319)),'P3':(Q(-319),Q('-2.014')),'P4':(Q('-1.506'),Q(0))}
    for name,boxes in json.loads((root/'critical_boxes.json').read_bytes()).items():
        low,high=pieces[name];previous=low
        for left,right,count in sorted(boxes,key=lambda b:Q(b[0])):
            left,right=Q(left),Q(right)
            assert previous<=left<right<=high
            assert ns['sturm_count'](D,left,right)==count
            previous=right
    # Machin's identity plus alternating-series error gives rational pi bounds.
    def atan_bounds(x,n=40):
        s=sum((-1)**j*x**(2*j+1)/(2*j+1) for j in range(n))
        nxt=(-1)**n*x**(2*n+1)/(2*n+1)
        return min(s,s+nxt),max(s,s+nxt)
    a,b=atan_bounds(Q(1,5));c,d=atan_bounds(Q(1,239))
    pi_lo,pi_hi=16*a-4*d,16*b-4*c
    def trig_bounds(x,cosine=False,n=50):
        start=0 if cosine else 1
        s=sum((-1)**j*x**(2*j+start)/math.factorial(2*j+start) for j in range(n))
        err=x**(2*n+start)/math.factorial(2*n+start)
        return s-err,s+err
    def tan_bounds(x):
        sl,sh=trig_bounds(x);cl,ch=trig_bounds(x,True)
        assert cl>0
        return sl/ch,sh/cl
    assert tan_bounds(pi_hi*(Q(1,3)-Q(1,50)))[1]<Q('1.506')
    assert tan_bounds(pi_lo*(Q(1,3)+Q(1,50)))[0]>Q('2.014')
    assert tan_bounds(pi_lo/1000)[0]>Q(1,319)
    # Exact Fourier triangle bound for F' on the remaining strip.
    uq=ns['load_coeffs'](str(root/'u_coeffs.txt'))
    cos={1:Q(1)};sin={2:Q(1,2)}
    for k in range(1,13):
        cos[k]=cos.get(k,Q(0))-uq[2*k-2];cos[2*k]=cos.get(2*k,Q(0))+uq[2*k-2]
        sin[k]=sin.get(k,Q(0))-uq[2*k-1];sin[2*k]=sin.get(2*k,Q(0))+uq[2*k-1]
    bound=sum(k*(abs(cos.get(k,0))+abs(sin.get(k,0))) for k in cos.keys()|sin.keys())
    assert bound==Q(1511419981,51300000)
    assert R[-1]-2*pi_hi*bound/1000>Q('0.2355')
    print('VERIFY_OK: every critical box; rational pi/tan cover; Fourier strip bound')

if __name__=='__main__':verify(Path(__file__).resolve().parent)
