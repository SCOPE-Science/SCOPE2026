"""An isogeny-invisible paired total-ramification spectrum."""
from group_orbits import profile
from pathlib import Path
import json
irr={1:3,2:7,3:11,4:19}
def mul(a,b,d):
    q=1<<d;P=irr[d];v=0
    while b:
        if b&1:v^=a
        b>>=1;a<<=1
        if a&q:a^=P
    return v

def npoints(mask,d):
    q=1<<d
    powers={t:[1,t,mul(t,t,d),mul(mul(t,t,d),t,d)] for t in range(q)}
    powers[q]=[1,0,0,0]
    count=0
    for a in range(q+1):
        for b in range(q+1):
            X=powers[a];Y=powers[b]
            value=0
            for j in range(4):
                for i in range(4):
                    if mask>>(4*j+i)&1:
                        value^=mul(X[3-i if a==q else i],Y[3-j if b==q else j],d)
            count+=value==0
    return count

smooth=Path('data/smooth_bitset.bin').read_bytes()
for mask in (6335,10685):assert not smooth[mask]
N=tuple(npoints(6335,d) for d in range(1,5))
assert N==(2,8,17,20)
assert tuple(npoints(10685,d) for d in range(1,5))==N
assert profile(6335)==(0,2) and profile(10685)==(0,0)
print('equal zeta: masks 6335,10685 both N1..N4=(2,8,17,20); total-ramification pairs (0,2),(0,0)')
print('common genus-four Weil numerator: 1-T+2T^2+T^3+2T^5+8T^6-8T^7+16T^8')
