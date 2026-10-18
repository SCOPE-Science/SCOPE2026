# Independent mathematical audit

## correctness

PASS

For complex Haar simplex weights and spectrum (0,1,2), write y=p1,s=1-y,d=p0-p2,w=1-2y,c=cos(theta). The squared overlap equals (y+sc)^2+d^2(1-c^2), a convex quadratic in c with vertex admissible precisely when y<=1/2 and d^2<=s*w. For |w|<=h the endpoint c=-1 gives a full simplex strip of Haar mass h; for w>h the feasible d-length is 2 sqrt(z_minus), z_minus=(w+h^2-sqrt((1-h^2)*(w^2-h^2)))/2. Thus P3(h^2)=h+integral_h^1 sqrt(z_minus)dw, endpoints 0,1 by continuity. Rationalization, dominated convergence bounded by sqrt(2)*(1+w)/(2 sqrt(w)) give (P3(h^2)/h)->1+4/3=7/3. For Haar qubit min fidelity=(2p-1)^2 with p uniform, P2(h^2)=h. Correct domains complex Fubini-Study, harmonic exact spectrum, unrestricted time.

## originality

PASS

Best-of-knowledge original exact distribution and 7/3 near-zero coefficient for the time-minimized complex-Haar qutrit; primary Morley-Short et al. treats same orbit with qubit analytic real-Gaussian sampling and higher-dimensional simulations, but not the complex-Haar qutrit CDF. Fixed-operator numerical-shadow formulas cannot alone cover minimization across a continuous orbit. Other numerical-shadow or quantum fidelity literature may conceal an equivalent specialization.

## value

PASS

Near-orthogonality probability is a natural free-orbit distinguishability and experimental initial-state calibration observable. Sharp geometric 1+4/3 decomposition replaces a numerical dimension-three treatment with a continuous-time exact law, a motivated nontrivial spectral boundary, and a quantitative contrast with two-level Haar sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
