# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The strict interior follows from the quadratic energy \(V=\|x-Fe\|^2/2\). At a finite endpoint the derivative is only negative semidefinite, so the proof must classify the zero-dissipation set rather than silently extend a strict Lyapunov argument. The key polarization identity
\[
e^TG(w)=-w^TAw
\]
follows by expanding \((e+sw)^TG(e+sw)=0\). Cyclic equivariance makes \(A\) circulant, and \(Ae=e^TA=0\). On a critical eigenspace of \(S=(A+A^T)/2\), every vector is orthogonal to \(e\), while
\[
(d/dt)(e^Tw)=-p_*\|w\|^2
\]
at every nonzero point. Hence the largest invariant subset of the LaSalle zero set is only the origin. Boundedness follows directly from the nonincreasing coercive energy, so forward solutions are global. Outside the stated window, normality of the circulant linearization gives an eigenvalue with positive real part and therefore instability.

The Lorenz-96 Fourier symbol and the even/odd negative threshold were checked algebraically and numerically for dimensions 4 through 64. These computations are consistency checks; the all-dimensional proof is analytic.

## Originality

PASS, to the best of our knowledge. The closest known result is Proposition 1 in the published Kerin--Engler treatment, which establishes global asymptotic stability under the strict inequalities \(Fp_+<1\) and \(Fp_-<1\) for localized G-maps. Their negative-definite proof does not establish the equality case. Their spectral calculations, and the earlier van Kekem--Sterk bifurcation work, locate the same linear thresholds, so neither the strict interior nor those threshold values are claimed as new.

The endpoint issue is scientifically nontrivial rather than a formal replacement of < by <=. Schlegel--Noack's general theory of energy-preserving quadratic systems explicitly warns that negative-semidefinite symmetric parts require additional information; semidefinite energy alone need not imply convergence. The present cyclic polarization identity supplies that missing information and proves a complete equality-set rigidity statement.

Targeted exact and synonymous searches for Lorenz-96 global endpoint stability, semidefinite critical forcing, LaSalle closure, generalized G-maps, and lossless quadratic systems found no statement equivalent to the closed iff window or the endpoint transversality identity. The final publisher full text of Kerin--Engler was not fully accessible in the source inspected; its strict Proposition 1 was checked through an accessible manuscript copy, while the arXiv version and publisher metadata were also inspected. This is the principal residual priority risk. Later generalized Lorenz-96 work found in the search emphasizes bifurcation cascades, traveling waves, multistability, or chaotic regimes rather than this global endpoint closure.

## Value

PASS. The result removes the exact gap between a known strict global Lyapunov region and the first linear-instability boundary for an entire Lorenz-96-type class. It covers nonhyperbolic Hopf, double-Hopf, and pitchfork endpoints with one argument, and shows that the spectral stability window is not merely local: it is exactly the nonlinear global-stability window. The mechanism also explains why a semidefinite energy estimate happens to be decisive in this structured class although it is not decisive for general lossless quadratic systems.

## Checked evidence and limitations

Kerin--Engler was checked at the model class, linearization/eigenvalue-curve analysis, strict global-stability proposition available in the published-manuscript copy, and publisher metadata. Van Kekem--Sterk was checked at the explicit Lorenz-96 Jacobian spectrum and first-bifurcation theorem. Schlegel--Noack's accessible primary text was checked at the negative-definite trapping argument and its appendix discussion of semidefinite cases.

Scientifically, the theorem requires homogeneous quadratic Euclidean-energy preservation and cyclic equivariance with uniform damping and forcing. It does not extend automatically to site-dependent coefficients or arbitrary lossless quadratic systems. No endpoint decay rate is asserted, and no claim is made about dynamics after the first instability.
