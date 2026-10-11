# Independent mathematical audit

## correctness

PASS

Fresh elimination gives \(\det(\lambda I-M)=\lambda(\lambda^2+(2t^3-6t^2+3t-1)\lambda+t^3)\). Its discriminant is \((1-t)^2(4t^4-16t^3+12t^2-4t+1)\), with one root \(t_*=0.5947955253657324\) in \((0,1)\). Before that root the dominant positive real eigenvalue decreases (with only a horizontal derivative at \(t=1/2\)); afterward the conjugate modulus is \(t^{3/2}\) and increases. This independently reproduces \(\rho_*/a=1.4678898250138708\) and factor \(0.4587240807118043\).

## originality

PASS

Best-of-knowledge originality passes. The accessible prior work establishes convergence regions or optimizes a distinct relaxation step; no inspected statement gives the exact penalty minimizing the spectral radius of the unmodified symmetric scalar three-block iteration. The closest 2018 quadratic paper remains an explicit full-text access risk.

## value

PASS

Exact penalty selection for direct multi-block ADMM is a natural calibration question because convergence-safe penalties need not be rate-optimal. The smallest symmetric strongly convex three-block model already exhibits a sharp real/complex phase transition, giving a reusable benchmark for broader tuning theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
