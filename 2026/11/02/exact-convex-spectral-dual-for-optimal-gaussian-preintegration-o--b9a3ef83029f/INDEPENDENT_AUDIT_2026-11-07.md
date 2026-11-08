# Independent mathematical audit

## correctness

PASS

For symmetric real A, b and X standard Gaussian, decomposing X=Y+Zv, independent, gives R(v)=v^T B v−0.5(v^TAv)^2 with B=A²+bb^T and exact remaining variance. Completing the square for any scalar t gives R(v)<=0.5t²+lambda_max(B−tA); the latter is strongly convex and coercive, hence has unique minimizer t*. Its eigenvalue subdifferential condition says t* belongs to the range of A Rayleigh quotients on the top eigenspace E*; continuity and extremal compression eigenvectors produce an attaining unit v, proving no dual gap even with eigenvalue multiplicities. Equality in both squares yields the exact two-term nonnegative gap. For b=0, the inequality (lambda−a)(c−lambda)>=0 gives R*=(a²+c²)/2 when a<0<c and mixed extreme eigenvector weights −a/(c−a) and c/(c−a), and endpoint solution when semidefinite. In A=diag(−3,0,2), one such mixed direction leaves zero variance, whereas leading A² eigenvector leaves variance 2. Independently compared spectral minmax against direct direction samples in 60 dense symmetric trials; no finite check proves universal optimization.

## originality

PASS

PASS with qualification. Liu–Owen 2023 explicitly gives the affine-quadratic Sobol total-effect/variance-reduction expression in its Section 4, Proposition 4.2, so that objective is known. The new all-instance exact scalar convex spectral dual, complete optimizer and dual-gap certificate, and explicit indefinite-spectrum optimum were not identified in the inspected preintegration analysis. The spectral subgradient argument is a generic convex-analysis method and broader joint-numerical-range hidden convexity might imply its abstract form; distinguish the application from the method.

## value

PASS

Choosing the variance-optimal preintegration direction instead of the natural leading active-subspace heuristic is a motivated numerical-integration decision, and the exact all-dimensional convex spectral dual with a constructive optimality certificate resolves it. The indefinite two-extreme mixture can remove all variance in a rank-two example where standard eigenvector selection cannot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
