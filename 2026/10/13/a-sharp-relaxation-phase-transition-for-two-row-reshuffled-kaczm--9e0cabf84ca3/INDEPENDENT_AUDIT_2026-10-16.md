# Independent mathematical audit

## correctness

PASS

Using bisector unit normals (sqrt((1+c)/2), ±sqrt((1-c)/2)), form U=I-omega aa^T, V=I-omega bb^T. Independent symbolic multiplication gives Q=[(VU)^T(VU)+(UV)^T(UV)]/2 diagonal, with trace S_c=c^2 omega^2(2-omega)^2+2(omega-1)^2 and diagonal difference D_c=c omega(omega-2)(c^2 omega^2-2omega+2); hence the largest eigenvalue is (S_c+|D_c|)/2. For omega outside (0,2) each relaxed projection has least singular value >=1. On [1,2], first Q diagonal entry is strictly increasing, while the other decreases then increases and has a unique stationary minimum F_c=0. The cross-over c^2 omega^2-2omega+2=0 occurs only for c<1/sqrt2. Substituting omega=1+t^2/2,c=t/(1+t^2/2) into F_c yields t(t^3+3t^2/2-1); its unique root defines c0=0.55111240553326. Direct symbolic Q and numerical local scans on both sides independently verify the claimed piecewise unique minimizer; analytic monotonicity proves all c,omega, not the finite scans.

## originality

PASS

PASS best of knowledge. Han–Xie arxiv:2410.01140 analyzes ordinary unrelaxed uniform reshuffling and a worst-permutation contraction bound; the new objective is the sharp expected-square supremum for a shared variable relaxation over two orderings. Oswald–Zhou studies reshuffled SOR/Kaczmarz under generic spectral bounds and Marshall–Mickelin optimized independently sampled noisy steps, not the exact two-direction envelope or crossover between minimax mechanisms.

## value

PASS

The familiar omega=1 projection is never the sharp one-epoch expected-square best choice for two nonparallel rows; over-relaxation strictly improves it. The explicit switch between eigen-direction equalization and interior stationarity is a nontrivial parameter-selection theorem for a canonical minimum-size randomized reshuffling system, beyond a routine textbook one-step optimization. It does not claim asymptotic many-epoch optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
