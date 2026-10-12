import math

def S(t,a,b):
    e=math.exp(b*t)
    return a*a*(e+a)/((a+1.0)*(e+a-1.0)**2)

def f(t,a,b):
    e=math.exp(b*t)
    return a*a*b*e*(e+a+1.0)/((a+1.0)*(e+a-1.0)**3)

def model_likelihood(ts, causes, Rs, a, b1, b2):
    L=1.0
    for t,c,R in zip(ts,causes,Rs):
        if c==1:
            L*=f(t,a,b1)*S(t,a,b2)
        else:
            L*=f(t,a,b2)*S(t,a,b1)
        L*=(S(t,a,b1)*S(t,a,b2))**R
    return L

def printed_31(ts, causes, Rs, a, b1, b2):
    m=len(ts); m1=sum(c==1 for c in causes); m2=m-m1
    L=a**(4*m)*b1**m1*b2**m2/(1+a)**(2*m)
    for t,c,R in zip(ts,causes,Rs):
        e1=math.exp(b1*t); e2=math.exp(b2*t)
        if c==1:
            L*= e1*(a+e1+1)*(a+e2)/((a+1)**2*(a+e1-1)**3*(a+e2-1)**2)
        else:
            L*= e2*(a+e1)*(a+e2+1)/((a+1)**2*(a+e1-1)**2*(a+e2-1)**3)
        L*=((a+e1)*(a+e2)/((a+1)**2*(a+e1-1)**2*(a+e2-1)**2))**R
    return L

def log_32(ts, causes, Rs, a, b1, b2):
    out=0.0
    for t,c,R in zip(ts,causes,Rs):
        out += R*(math.log(S(t,a,b1))+math.log(S(t,a,b2)))
        if c==1: out += math.log(f(t,a,b1))+math.log(S(t,a,b2))
        else: out += math.log(f(t,a,b2))+math.log(S(t,a,b1))
    return out

ts=[0.2,0.8,1.6]
causes=[1,2,1]
Rs=[1,0,1]
a,b1,b2=1.3,0.6,0.9
m=len(ts); R=sum(Rs)
Lm=model_likelihood(ts,causes,Rs,a,b1,b2)
Lp=printed_31(ts,causes,Rs,a,b1,b2)
Llog=math.exp(log_32(ts,causes,Rs,a,b1,b2))
ratio=a**(-4*R)*(1+a)**(-2*m)
assert abs(Lp/Lm-ratio) < 2e-12*abs(ratio)
assert abs(Llog/Lm-1.0) < 2e-12

# Posterior correction magnitude for a source simulation design.
n=30; msrc=20; Rsrc=n-msrc; a0=1.1; a1=2.0
score=4*Rsrc/a0 + 2*msrc/(1+a0)
logcorr0=4*Rsrc*math.log(a0)+2*msrc*math.log(1+a0)
logcorr1=4*Rsrc*math.log(a1)+2*msrc*math.log(1+a1)
relative=math.exp(logcorr1-logcorr0)
assert abs(score-55.41125541125541)<1e-12
assert 3e16 < relative < 5e16

print('VERIFY_OK')
print('likelihood_ratio_printed_to_correct', format(Lp/Lm,'.16e'))
print('predicted_ratio', format(ratio,'.16e'))
print('eq32_to_direct', format(Llog/Lm,'.16e'))
print('missing_score_at_alpha_1.1', format(score,'.12f'))
print('correction_factor_ratio_alpha2_vs_alpha1.1', format(relative,'.12e'))
