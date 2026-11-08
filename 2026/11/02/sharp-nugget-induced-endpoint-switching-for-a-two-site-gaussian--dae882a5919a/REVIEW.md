# Independent mathematical audit

## correctness

PASS

For two sites Y=(b,-b), known noise h>0 and signal variance1, exact diagonalization yields L(t)=2z/(A-t)+ln(A²-t²), A=1+h, z=b². For A>=2 compare L(t)-L(0)=2t[z-J_A(t)]/[A(A-t)]; series derivative shows J_A strictly increasing to J_A(1)=kappa(h). Differentiation gives derivative sign from q(t)=t²+(z-A)t+Az, excluding hidden interior minima if z<kappa, including z=0 and tie z=kappa. Series S(u) proves kappa strictly increasing from ln(4/3) toward 1/2. For ALL h>0 the bound J_A(t)<t/[2(1+t/A)]<1/2 forces t=0 when z>=1/2. Endpoints are compactification limits, never positive finite lengthscales under assumed kernel continuity/strict interior t. Independent numerical endpoint, tie and derivative calculations corroborate not exhaust the continuum.

## originality

PASS

The GP negative log-likelihood formula is standard; Karvonen–Oates Section 4 investigates nugget smoothing with numerical endpoint evidence rather than an exact two-opposite-residual high-nugget threshold. Fosdick–Raftery cover unconstrained Gaussian correlation estimation, not constrained positive GP t in [0,1]. The current theorem gives a sharp nonattained finite-lengthscale interval, monotone noise-switch threshold and all-h large-contrast obstruction. Best-of-knowledge novelty concerns that complete constrained global classification only.

## value

PASS

Lengthscale nonexistence despite strictly positive noise and nonconstant data is an important boundary of Gaussian-process hyperparameter optimization. The exact all-high-noise endpoint switch and monotone threshold provide a complete natural two-site classification, including a high-signal counterboundary to global flatness. Its fixed mean, signal variance and contrast are essential; no general multi-site optimizer is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
