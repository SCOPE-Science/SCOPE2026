"""Reproducible independent checks for weak-harmonic-return first-passage asymptotic.
Scientific diagnostics only; no external input or external services.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import erfc, erfcx, erf

D=1.0
L=1.0

# Finite-return stiffness OU first-passage functions.
def ret_negative(a,k):
    c=math.sqrt(k/(2*D))
    return math.sqrt(math.pi/(2*D*k))*quad(lambda y: erfcx(c*y),0,a,epsabs=2e-11,epsrel=2e-11)[0]

def pos_profile(k, number=1501):
    from scipy.integrate import cumulative_trapezoid
    z=np.linspace(0,L,number)
    a=k/(2*D)
    S=cumulative_trapezoid(np.exp(a*z*z),z,initial=0)
    J=cumulative_trapezoid(np.where(a>0,np.sqrt(np.pi)*np.exp(a*z*z)*erf(np.sqrt(a)*z)/(2*np.sqrt(a)),z),z,initial=0)
    m=(J[-1]*S/S[-1]-J)/D
    h=S/S[-1]
    return z,m,h

def search_density(x,mode,parameter):
    if x>=L:return 0.0
    if mode=='exp':
        q=math.sqrt(parameter/D)
        return q/2*(math.exp(-q*abs(x))-math.exp(-q*(2*L-x)))
    if mode=='fixed':
        t=parameter
        d=math.sqrt(4*math.pi*D*t)
        return (math.exp(-x*x/(4*D*t))-math.exp(-(2*L-x)**2/(4*D*t)))/d
    raise ValueError

def search_prob(mode,p):
    if mode=='exp':return math.exp(-L*math.sqrt(p/D))
    if mode=='fixed':return erfc(L/math.sqrt(4*D*p))
    raise ValueError

def search_mean(mode,p):
    if mode=='exp':return (1-search_prob(mode,p))/p
    if mode=='fixed':
        return quad(lambda t: math.erf(L/math.sqrt(4*D*t)),0,p,epsrel=2e-10)[0]
    raise ValueError

def calculate(mode,parameter,k):
    z,m,h=pos_profile(k)
    g=np.array([search_density(x,mode,parameter) for x in z])
    right_prob=np.trapezoid(h*g,z)
    right_duration=np.trapezoid(m*g,z)
    from scipy.integrate import quad
    cap=20*math.sqrt(D/parameter) if mode=='exp' else 20*math.sqrt(D*parameter)
    neg_moment=quad(lambda a: a*search_density(-a,mode,parameter),0,cap,epsabs=1e-12)[0]
    neg_duration=quad(lambda a:ret_negative(a,k)*search_density(-a,mode,parameter),0,cap,epsabs=1e-11)[0]
    p_s=search_prob(mode,parameter)
    p0=p_s+quad(lambda x:x/L*search_density(x,mode,parameter),0,L)[0]
    p= p_s+right_prob
    mean=(search_mean(mode,parameter)+neg_duration+right_duration)/p
    return {'p0':p0,'AoverL':neg_moment/L,'mean':mean,'scaled':math.sqrt(k)*mean,'pk':p, 'negative_duration':neg_duration,'positive_duration':right_duration}

def main():
    required=L*math.sqrt(math.pi/(2*D))
    checks=0
    for mode,param in [('exp',0.35),('exp',1.0),('exp',4.0),('fixed',0.25),('fixed',1.2)]:
        print('RESET',mode,param)
        prev=None
        for k in [0.02,0.005,0.001,0.0002]:
            out=calculate(mode,param,k)
            assert abs(out['AoverL']-out['p0'])<2e-7,(mode,param,out)
            checks+=1
            err=abs(out['scaled']/required-1)
            print(f' k={k:.4g}: sqrt(k)*MFPT={out["scaled"]:.9f}, target={required:.9f}, relerr={err:.5g}, p0={out["p0"]:.8f}')
            if prev is not None: assert err <prev*1.02
            prev=err
            checks+=1
        if mode=='exp':
            b=L*math.sqrt(param/D)
            direct=(1-math.exp(-2*b))/(2*b)
            assert abs(out['p0']-direct)<2e-8
            checks+=1
    for k in (0.0003,0.01,0.2,2.0):
        z,m,h=pos_profile(k)
        assert abs(m[0])<1e-10 and abs(m[-1])<1e-10
        assert min(m)>-1e-8 and abs(h[0])<1e-10 and abs(h[-1]-1)<1e-10
        checks+=4
    print('PASS',checks,'independent deterministic tests')

if __name__=='__main__':main()
