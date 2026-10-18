"""Independent vectorized conic census; requires NumPy.

Uses alternate smoothness and projective point-evaluation paths.
Run: python crosscheck_numpy.py
"""
import itertools
import numpy as np

def run(q):
    P=np.array([(1,y,z) for y in range(q) for z in range(q)]
               +[(0,1,z) for z in range(q)]+[(0,0,1)], dtype=np.int64)
    incidence=((P@P.T)%q==0)
    mon=np.array([[x*x,x*y,x*z,y*y,y*z,z*z] for x,y,z in P], dtype=np.int64)
    base=(mon @ np.array([0,0,1,(-1)%q,0,0]))%q==0
    assert base.sum()==q+1
    smooth,covered,hist=0,0,{}
    for lead in range(6):
        for tail in itertools.product(range(q),repeat=5-lead):
            a,b,c,d,e,f=(0,)*lead+(1,)+tail
            determinant=(2*a*((2*d)*(2*f)-e*e)
                         -b*(b*(2*f)-e*c)
                         +c*(b*e-(2*d)*c))%q
            if not determinant: continue
            smooth+=1
            mask=(mon@np.array((a,b,c,d,e,f)))%q==0
            counts=incidence@(base|mask).astype(np.int8)
            if np.min(counts)>0:
                covered+=1
                hist[(int((base&mask).sum()),int((base|mask).sum()))] = hist.get((int((base&mask).sum()),int((base|mask).sum())),0)+1
    return smooth,covered,hist

if __name__=='__main__':
    result5=run(5)
    result7=run(7)
    assert result5==(3100,12,{(1,11):12}),result5
    assert result7==(16758,0,{}),result7
    print('q=5',result5,'q=7',result7)
    print('PASS')
