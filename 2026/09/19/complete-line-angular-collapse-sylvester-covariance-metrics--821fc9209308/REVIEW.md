# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The completeness classification follows from two complementary estimates.  Along the scalar ray, homogeneity gives an exact one-dimensional length integral, proving incompleteness for degrees below or above two by escape to zero or infinity.  At degree two, the diagonal part of every kernel metric bounds the Euclidean speed of the ordered log-spectrum.  This prevents finite-length escape from every compact spectral annulus; positivity and continuity of the kernel then give uniform equivalence with the Frobenius metric on a larger annulus, which closes the Cauchy-sequence argument.

The dilation and inversion identities were checked both algebraically and numerically.  The isospectral-rotation formula follows by differentiating X(theta)=R(theta) D R(theta)^T in its instantaneous eigenbasis; the only nonzero tangent entries are the symmetric off-diagonal pair, so the kernel factorization gives the displayed length exactly.  Its three regimes follow from cosh((a/2) log kappa) ~ kappa^{|a|/2}/2 for a != 0.  The mean-kernel threshold follows from the two logarithmic partial derivatives of M_a.  The public verification artifact independently checks these identities and asymptotics.

Adversarial checks included eigenvalue crossings in the completeness proof, whether a short path could leave the spectral annulus before the local norm-equivalence argument is used, the constant rescaling of a kernel metric, the factor of two from the two symmetric off-diagonal entries, and the distinction between an explicit path length and the true geodesic distance.  The record uses the rotation path only as an upper bound on distance.

## Originality

**PASS, to the best of our knowledge.** The motivating paper arXiv:2609.17089 was inspected for the metric definition, kernel factorization, named members, and exponent/shape conditioning analysis.  Its text does not state the completeness classification, inversion symmetry, dilation symmetry, or the isospectral angular-collapse law reported here.

Hiai--Petz (arXiv:0809.4974) and the Thanwerdas--Pennec syntheses arXiv:2109.05768 and arXiv:2111.02990 were checked because they are the closest general geometric literature.  They explicitly state completeness for mean-kernel metrics with homogeneity power two.  The complete-line subset |p-q|<=2 of the present family falls under that known result after constant normalization and is excluded from the novelty claim.  The checked literature did not locate the stronger positive-homogeneous-kernel lemma without a mean hypothesis, the resulting complete non-mean members |p-q|>2, or the exact angular-collapse threshold and rate for this family.

Searches used the formulations homogeneous kernel metric, degree-two completeness, inversion isometry, scale/dilation invariance, eigenvector rotation, and the cosh kernel.  No exact prior statement was found.  The residual risk is diffuse rather than tied to one inaccessible source: older matrix-geometry or operator-mean literature may contain an equivalent homogeneous-kernel completeness argument or isospectral-orbit asymptotic in different notation.  This risk is why the claim is restricted to the theorem package stated in RESULT.md and carries the “to the best of our knowledge” qualification.

## Value

**PASS.** The source paper presents metric choice as a tunable preconditioner.  The result adds a sharp global phase diagram that local Hessian conditioning does not capture: only p+q=2 is complete and scale/inversion symmetric, while the complete but non-mean region |p-q|>2 makes principal-axis swaps of highly ill-conditioned covariances asymptotically free.  These criteria give concrete geometric diagnostics for metric tuning and expose a meaningful tradeoff between local preconditioning and global geometry.

## Limitations

The angular result is a distance upper bound furnished by one explicit path, not an exact geodesic distance.  It does not establish optimization failure or superiority of any parameter region.  The completeness theorem is for smooth positive homogeneous kernel metrics on the full SPD cone; it does not automatically extend to arbitrary O(n)-invariant metrics outside the kernel class.  No curvature or convergence-rate theorem for the source algorithm is claimed.
