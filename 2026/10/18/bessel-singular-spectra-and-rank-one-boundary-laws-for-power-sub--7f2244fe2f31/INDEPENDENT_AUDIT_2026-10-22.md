# Independent mathematical audit

## correctness

PASS

The operator kernel 1_{t<=x^alpha} is Hilbert–Schmidt; K=T* T has kernel 1-max(s,t)^{1/alpha}. Its eigenvalue equation differentiates to u_doubleprime+(1-gamma)u_prime/t+(gamma/lambda)t^{gamma-1}u=0 with u(1)=0 and t^(1-gamma)u_prime(t)->0, gamma=1/alpha. The Bessel basis t^(gamma/2)J_{+-gamma/(gamma+1)}(z t^((gamma+1)/2)) shows weighted-derivative endpoint selects J_{-gamma/(gamma+1)}; at t=1 its positive simple zeros give s_n=2 sqrt(alpha)/((1+alpha)j_{-1/(1+alpha),n}). Converse integration of boundary ODE eliminates spurious solutions, compact injectivity completes spectrum. Trace integrations produce moments 1/(1+alpha), 1/((1+alpha)(1+2alpha)); fixed-order zeros give n*s_n. Near alpha=0 the first Bessel zero escapes to zero, others tend to j_{1,k}; Rayleigh sum and dominated tail lead s1=1-3alpha/4+o(alpha), tail HS 1/2; alpha->inf yields j_{0,k}. Independent alpha=1 Volterra singular values and moments and 21 alpha=2 Bessel roots checked; not a general proof.

## originality

PASS

Primary scientific comparisons concern same objects, parameters, reductions and stronger-coverage possibilities; no inspected statement decisively covers the complete final claim. Best-of-knowledge originality with explicit remaining access/priority risks.

## value

PASS

Whole singular spectrum fixes every finite-rank approximation error, Schatten boundary and singular alpha limits for a nonnormal operator whose ordinary eigenvalues are misleadingly geometric. The sharp rank-one residual profile is motivated and unavailable from the ordinary spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
