# Review of the two-power Bergman kernel transition

## Correctness

**PASS, self-review.** Normalized radial moments are beta integrals. Euler transformation gives a zero-preserving factorization into a nonvanishing analytic prefactor and an integral \(G\). At the critical parameters, \(G\) is an explicit degree-five polynomial with exactly two simple unit-circle zeros and no zeros in the open disk. Uniform parameter continuity on the *closed* disk and Rouché's theorem exclude unexpected roots, including near the singular point of the other hypergeometric factor. Two explicit parameter derivatives and the nonzero radial derivative establish a real-analytic transverse crossing curve. A symbolic checker separately verifies the exact tangent, and numerical quadrature checks nearby crossings. The numerical tests are not substitutes for the analytic global-in-\(u\) argument.

## Originality

**PASS, provisional.** Perälä's radial-kernel work constructs and bounds finite zero sets but does not classify this two-parameter Jacobi-power phase boundary. Jacobson's meromorphic multiplier theorem covers the *integer* origin exponent at the base point and supplies a known route to the unperturbed formula; neither its general identity nor its weighted-kernel zero examples imply the noninteger-parameter zero-entry classification or the tangent coefficient. Miña-Díaz gives explicit representations for powers of Blaschke factors with unweighted area measure; his theorem is not the simultaneous boundary-power family. Nearby published classifications for alternative Euclidean-distance weights, zero-jet kernels and other radial factors do not imply this curve by identification of their weight functions. Classical hypergeometric zero-counting theorems, including DLMF §15.13, count roots in a slit-plane sector rather than classify their entry into the unit disk as the exponents vary; an earlier unit-disk location theorem in a different parameterization remains a priority risk.

## Value

**PASS.** Zero-freeness of a weighted Bergman kernel is a structural analytic distinction relevant to zero-free kernel methods and Bergman representative coordinates. The result gives a *sharp* local zero-free/two-zero phase classification for a natural two-parameter family, and the explicit nonzero derivative establishes the robustness and direction of the first complex-conjugate zero entry under fractional origin-weight perturbations. This is more than an evaluation of a single low-order moment or an unmotivated numerical root: the classification controls every kernel zero in the disk in a whole parameter neighborhood.

## Closest literature and limits

The closest sources are Jacobson (arXiv:1309.4800, Theorem 4), Perälä (arXiv:1703.05976, Theorems 3.1 and 3.3), and Miña-Díaz (arXiv:2212.08118, Theorem 1.1). The theorem gives an unspecified but positive parameter neighborhood, not a global phase diagram; independent historical-priority and mathematical reviews remain outstanding. The critical simple-root identities and the numerical checks were re-evaluated against the final standalone checker.

Self-review: passed. Independent audit: not yet performed.
