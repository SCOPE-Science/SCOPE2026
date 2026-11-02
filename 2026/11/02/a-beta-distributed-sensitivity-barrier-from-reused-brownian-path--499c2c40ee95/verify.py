"""Independent numerical checks for the shared-path sensitivity example.

Analytic identities and general dimension claims are proved in RESULT.md; these
finite checks are supplementary, not proof by finite enumeration.
"""
import math
import numpy as np

rng = np.random.default_rng(20261028)
checks = 0

def check(condition, msg):
    global checks
    if not condition:
        raise AssertionError(msg)
    checks += 1

# A Gaussian derivative of a terminal threshold probability.
for x in np.linspace(-2.5, 2.5, 41):
    h = 1e-5
    cdf = lambda t: 0.5 * math.erfc(-t / math.sqrt(2.0))
    derivative = (cdf(x + h) - cdf(x - h)) / (2*h)
    density = math.exp(-x*x/2) / math.sqrt(2*math.pi)
    check(abs(derivative - density) < 2e-10, 'normal derivative identity')

# With one reused Brownian endpoint, the outer estimator equals ZZ^T/4
# for ANY Gaussian drift draws, even though the threshold outcomes vary.
for d in (2, 3, 7, 11):
    for m in (1, 2, 19, 223):
        z = rng.normal(size=d)
        u = rng.normal(size=(m, d))
        signs = (u[:, -1] + z[-1] > 0).astype(float) - 0.5
        g = signs[:, None] * z[None, :]
        K_hat = (g.T @ g) / m
        check(np.allclose(K_hat, np.outer(z,z)/4, rtol=1e-12,atol=2e-14), 'one-path collapse')

# All outer sample gradients are combinations of the SAME inner endpoint vectors.
for d, l, m in ((3,1,11),(5,2,100),(8,4,75),(12,5,21)):
    Z = rng.normal(size=(d,l))
    U = rng.normal(size=(m,d))
    indicators = (U[:,-1,None] + Z[-1,:][None,:] > 0).astype(float)-0.5
    grads = indicators @ Z.T / l
    Q,_ = np.linalg.qr(Z,mode='reduced')
    err = grads - (grads@Q)@Q.T
    check(np.linalg.norm(err) < 1e-10, 'shared span')
    K_hat = grads.T @ grads/m
    check(np.linalg.norm(K_hat-(Q@Q.T)@K_hat) < 1e-10, 'matrix range')
    check(np.linalg.matrix_rank(K_hat,tol=1e-9) <= l, 'inner path rank')
    check(np.linalg.eigvalsh(K_hat)[-1]>0, 'nonzero leading eigenspace')

# Haar Gaussian subspace: the exact mean projected energy is l/d,
# and its one-dimensional squared angle is Beta(1/2,(d-1)/2).
for d,l in ((3,1),(6,1),(8,2),(8,4),(12,3),(16,8)):
    data=[]
    for _ in range(1800):
        Z = rng.normal(size=(d,l))
        Q,_=np.linalg.qr(Z,mode='reduced')
        projected_sq=float(np.sum(Q[-1,:]**2))
        check(-1e-13<=projected_sq<=1+1e-13, 'projected unit energy range')
        data.append(projected_sq)
    check(abs(np.mean(data)-l/d)<0.028,'Beta projected energy mean')

# Bayes approximation MSE, from exact orthant formula.
# Var(E[Phi(U_d)|v.U])=arcsin(q/2)/(2*pi) when |v_d|^2=q.
for q in np.linspace(0,1,21):
    a=math.sqrt(q/(2-q))
    nodes,weights=np.polynomial.hermite.hermgauss(96)
    yy=nodes*math.sqrt(2)
    Phi=np.array([0.5*math.erfc(-a*y/math.sqrt(2)) for y in yy])
    v=float(np.sum(weights*(Phi-0.5)**2)/math.sqrt(math.pi))
    formula=math.asin(q/2)/(2*math.pi)
    check(abs(v-formula)<2e-13,'exact orthant Bayes risk identity')
    risk=1/12-v
    check(risk+1e-13>=(1-q)/12,'linear universal risk floor')
    check(risk>=-1e-13,'nonnegative risk')

# Optimal prior-averaged scalar martingale coefficient is beta=-1/2.
U=rng.normal(size=220000)
Z=rng.normal(size=220000)
I=(U+Z>0).astype(float)
weighted=float(np.mean(I*Z*Z)/np.mean(Z*Z))
check(abs(weighted-0.5)<0.009,'mean optimal CV coefficient')

# Scalar exact gradient covariance: E[phi(U)^2] = 1/(2*pi*sqrt(3)).
U=rng.normal(size=250000)
pdf_sq=np.exp(-U*U)/(2*math.pi)
check(abs(float(np.mean(pdf_sq))-1/(2*math.pi*math.sqrt(3)))<0.0007,'population sensitivity eigenvalue')

print('PASS: %d reproducible numerical and algebraic checks' % checks)
