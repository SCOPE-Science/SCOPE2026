# Independent mathematical audit

## correctness

PASS

The graph has separate exterior rays at each junction and M finite interior paths of L-1 sites; deleting the incident edges is finite rank and leaves half-line adjacency operators, so the essential band is [-2,2]. The band recurrence has no nonzero square-summable ray solution, including double characteristic roots at +/-2. Thus the junction amplitudes vanish, and each interior amplitude is a Dirichlet sine mode. Its nonzero first-site value and its proportional last-site value reduce the two junction constraints to one copy-amplitude sum, giving exactly M-1 modes at each listed energy and none at the edges. For E>2, square summability forces decay by q per exterior step and uniquely fixes each interior branch from the two hub amplitudes. The resulting self-energy B*(E-K)^{-1}B has negative-semidefinite derivative, since the disconnected K has norm 2; both real parity scalars have derivative at least one. At E down to 2, the even value tends to 2-2M<0, the odd to 2-2M(1-1/L)<=0 with equality only at (2,2); both diverge positively at large E. The positive off-diagonal response magnitude orders the two distinct roots and makes each eigenspace one-dimensional. At the exception the bounded E=2 solution has hubs 1 and -1, middle sites zero, and constant tails of the matching signs. The integer-label bipartition gives the E=-2 solution and the negative eigenvalues. In q coordinates the parity secular equation is 1-(2M-1)q^2-s(M-1)q^L(1+q^2)=0 for 0<q<1; it follows by simplifying the sinh quotient to (q+s q^{L-1})/(1+s q^L). This places the roots on opposite sides of the single-junction value and shows local-uniform convergence in E>2 as L grows, so strict sign bracketing proves convergence. Independent direct L=2 interior elimination and an exact threshold residual check are replayable with python3 /workspace/branches/independent_checks.py 4. The supplied finite-ray eigensolver was read, not executed; it is not evidence of exact threshold or infinite-volume completeness by itself.

## originality

PASS

The supported contribution is a complete discrete infinite two-junction point-spectrum classification and sharp isolated missing odd bound pair with its threshold resonance. Credit the known single-junction energy, local-symmetry compact localization, ordinary Dirichlet path eigenvalues, and the metric two-junction BIC mechanism. No inspected statement establishes this conjunction for the specified discrete adjacency operator. Full-text access to the crossbar comparator remains limited as documented.

## value

PASS

The exact point-spectrum census resolves what finite separation of two kinetic junctions changes: an entire compact embedded ladder, a split pair of exterior levels when both exist, and a single minimal geometry where a bound branch instead meets the continuum edge as a resonance. That is a reusable family-wide threshold result, more than an example of a BIC or a finite-matrix approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
