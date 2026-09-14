import cmath, math, random
def theta1(z, tau, N=80):
    s = 0j
    for n in range(-N, N+1):
        s += cmath.exp(1j*math.pi*(n*n*tau) + 2j*math.pi*n*z)
    return s
def theta2(z1, z2, t11, t12, t22, N=25):
    s = 0j
    for n1 in range(-N, N+1):
        for n2 in range(-N, N+1):
            s += cmath.exp(1j*math.pi*(n1*n1*t11+2*n1*n2*t12+n2*n2*t22) + 2j*math.pi*(n1*z1+n2*z2))
    return s
tau11 = 1.2j; tau12 = 0.15+0.1j
random.seed(0)
pts=[(random.uniform(-2,2), random.uniform(-2,2)) for _ in range(8)]
print("delta, q~delta, max|full-lead-corr|/|lead|, max|full-lead|/|lead|")
prev=None
for delta in [0.2,0.1,0.05,0.025]:
    tau22 = 0.3 + 1j*(math.log(1/delta)/math.pi + 0.5)
    q = abs(cmath.exp(1j*math.pi*tau22))
    e1=[]; e2=[]
    for (x,t) in pts:
        z1 = 0.3*x+0.11*t; z2 = 0.23*x-0.31*t+0.1
        full = theta2(z1,z2,tau11,tau12,tau22)
        lead = theta1(z1,tau11)
        corr = theta1(z1+tau12,tau11)*cmath.exp(1j*math.pi*tau22+2j*math.pi*z2) + theta1(z1-tau12,tau11)*cmath.exp(1j*math.pi*tau22-2j*math.pi*z2)
        e1.append(abs(full-lead-corr)/abs(lead))
        e2.append(abs(full-lead)/abs(lead))
    print(f"{delta} q={q:.4f} 2nd-order={max(e1):.3e} 1st-order={max(e2):.3e} ratio1/delta={max(e2)/delta:.3f}")
print(" scaling check done")
