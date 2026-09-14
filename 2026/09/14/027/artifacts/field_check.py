import cmath, math, random
def theta1(z, tau, N=80):
    s=0j
    for n in range(-N,N+1):
        s+=cmath.exp(1j*math.pi*n*n*tau+2j*math.pi*n*z)
    return s
def theta2(z1,z2,t11,t12,t22,N=22):
    s=0j
    for n1 in range(-N,N+1):
        for n2 in range(-N,N+1):
            s+=cmath.exp(1j*math.pi*(n1*n1*t11+2*n1*n2*t12+n2*n2*t22)+2j*math.pi*(n1*z1+n2*z2))
    return s
tau11=1.2j; tau12=0.15+0.1j
random.seed(1)
pts=[(random.uniform(-2,2),random.uniform(-2,2)) for _ in range(10)]
# reconstruction analogue: u=2*arg ratio -> use 4*atan(|t_shift|/|t|) style smooth functional
def u1(z1): return 4*math.atan(abs(theta1(z1+0.25,tau11)/theta1(z1,tau11)))
def u2(z1,z2,t22):
    F=theta2(z1,z2,tau11,tau12,t22); Fs=theta2(z1+0.25,z2+0.1,tau11,tau12,t22)
    return 4*math.atan(abs(Fs/F))
def u0lim(z1,z2,t22):
    L=theta1(z1,tau11)+theta1(z1+tau12,tau11)*cmath.exp(1j*math.pi*t22+2j*math.pi*z2)+theta1(z1-tau12,tau11)*cmath.exp(1j*math.pi*t22-2j*math.pi*z2)
    Ls=theta1(z1+0.25,tau11)+theta1(z1+0.25+tau12,tau11)*cmath.exp(1j*math.pi*t22+2j*math.pi*(z2+0.1))+theta1(z1+0.25-tau12,tau11)*cmath.exp(1j*math.pi*t22-2j*math.pi*(z2+0.1))
    return 4*math.atan(abs(Ls/L))
for delta in [0.2,0.1,0.05,0.025]:
    tau22=0.3+1j*(math.log(1/delta)/math.pi+0.5)
    errs=[]
    for (x,t) in pts:
        z1=0.3*x+0.11*t; z2=0.23*x-0.31*t+0.1
        errs.append(abs(u2(z1,z2,tau22)-u0lim(z1,z2,tau22)))
    print(f"delta={delta} sup|u2-u0lim|={max(errs):.3e} ratio={max(errs)/delta:.3f}")
