"""Numerical replication for a cyclic, translation-invariant LQR locality example.
This code supplements, but does not replace, the analytic argument.
"""
import math
import numpy as np

def kernel(theta):
    q=2.25+2*np.cos(theta)
    p=(q-0.75+np.sqrt((q+0.25)*(q+2.25)))/2
    return 0.5*p/(1+p),p

for N in [2048,4096,8192,16384]:
    theta=2*math.pi*np.arange(N)/N
    K,P=kernel(theta)
    q=2.25+2*np.cos(theta)
    coeff=np.fft.fft(K)/N
    assert max(abs(coeff.imag))<1.e-13
    vals=[]
    for n in [4,8,12,16]:
        approx=(-1)**(n-1)*math.sqrt(3)/(2*math.sqrt(math.pi))*(2**-n)*(n**-1.5)
        vals.append(round(coeff[n].real/approx,6))
    print('N, coefficient/asymptotic at n=4,8,12,16:',N,vals)
    for radius in [5,7,9,11]:
        truncated = coeff[0].real + 2*sum(coeff[j].real*np.cos(j*theta) for j in range(1,radius+1))
        z=0.5-truncated
        assert max(abs(z))<1
        Sigma=1/(1-z*z)
        Jt=0.5*np.mean((q+truncated*truncated)*Sigma)
        Jopt=0.5*np.mean(P)
        actual=Jt-Jopt
        identity=0.5*np.mean((1+P)*((truncated-K)**2)*Sigma)
        tail=np.mean((truncated-K)**2)
        lower_constant=radius**-3*4.**(-radius)/(2*math.pi)
        print(' ',radius,'gap',actual,'identity',identity,'tail',tail,'tail ratio',tail/lower_constant)
        assert abs(actual-identity)<max(2.e-12,0.0001*actual)
        assert actual>=.5*tail-1.e-12
print('verification completed')
