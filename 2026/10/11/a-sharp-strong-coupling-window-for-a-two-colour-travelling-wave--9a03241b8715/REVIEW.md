# Independent mathematical audit

## correctness

PASS

For f(x)=2x²−1, direct exact substitutions give f(u)=v, f(v)=u, with u=(sqrt(5)−1)/4, v=−(sqrt(5)+1)/4, and f'(u)f'(v)=−4. Because each site's neighbours equal its local image in X=(u,v,...) and Y=(v,u,...), F_a(X)=Y and F_a(Y)=X at every 0<=a<=1, including the double neighbour for N=2. In each 2-sublattice Fourier mode k=2πm/N, m=0,...,N/2−1, the two step matrix has diagonal K=a² cos²k−4(1−a)² and off-diagonal entries 2a(1−a)f'(v)cos k and 2a(1−a)f'(u)cos k. Its eigenvalues are K±4i a(1−a)cos k, whose moduli equal 4(1−a)²+a²cos²k. The k=0 mode always occurs, giving spectral radius 4(1−a)²+a² uniformly in even N. ρ−1=(a−1)(5a−3), so all multipliers contract precisely for 3/5<a<1, with instability for 0<=a<3/5; the endpoints have neutral multipliers and are not claimed nonlinearly classified. Unique quadratic minimum 4/5 at a=4/5. On the infinite 2-colour background affine ℓ² class, a 2-site Fourier direct integral yields the same spectral radius; the nonlinear remainder h↦h² is bounded ℓ²→ℓ² with norm <=||h||², hence the return map is C¹ and its power contracts locally if ρ<1. Independent from-scratch SymPy substitution and NumPy full-Jacobian eigenspectrum tests on N=2,4,6,8,12,20 and 10 couplings gave maximal absolute discrepancy <=8.89e−16. The unrestricted theorem rests on block algebra and operator theory, not finite tests.

## originality

PASS

Best-of-knowledge original concrete strong-coupling theorem for a spatially alternating travelling 2-cycle. Lippolis (2026) treats synchronized states explicitly, with real period-two cycle only up to a=1/3. Dettmann–Lippolis (2005) defines the same two-site 2B+ coupling, but its complete accessible manuscript emphasizes small-coupling orbit enumeration and cycle expansions, not this exact all-even-N multiplier cancellation, sharp interval, optimum and ℓ² extension. General Floquet and space-frequency reduction methods, as in Chatterjee–Gupte, are prior and not claimed as new. The highly plausible Dettmann (2002) same-model source was readable only at abstract level; cannot exclude appendix coverage, but this access issue alone is not decisive negative evidence.

## value

PASS

The question of coherent travelling-pattern stability is natural for the same spatially extended Chebyshev system whose synchronized temporal 2-cycle disappears by a=1/3. The result constructs a distinct orbit that persists for all a, gives a complete all-even-ring Floquet phase window 3/5<a<1, and fixes the optimal linear contraction coupling a=4/5. Its cancellation across all Fourier modes and extension to square-summable perturbations are motivated dynamical invariants, not a numerical slice or trivial renamed assertion. The result is local, not a global attractor theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
