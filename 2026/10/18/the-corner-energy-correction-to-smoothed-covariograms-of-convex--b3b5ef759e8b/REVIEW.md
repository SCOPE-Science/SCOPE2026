# Scientific review: planar corner correction

## Correctness — PASS

The claimed coefficient was reconstructed from the definition of the radial \((-p)\)-mean and the polar-area formula, not solely from asymptotic tables. Away from vertex rays, the exact translated radial ratio is \(1+a_i/p\) and the edge correction is \(W_i[-a_i^2A'(a_i)-2A(a_i)^2]\). A moving vertex ray creates a strip of angular width \(O(p^{-1})\), and the change of slope of the two radial candidates has modulus \(\|v\|^2\sin\Delta_i/(h_i h_{i+1})\). The rescaled switching integral is therefore \(\Gamma_iJ(a_i,a_{i+1})\). Finite edges and uniformly bounded displacements justify the remainder \(O_{P,Y}(p^{-2})\) after integrating the \(O(p^{-1})\) strip corrections. The divergence identity converts the leading \(A\)-sum into the even \(\log\cosh\)-sum. A monotonicity argument shows that the corner term vanishes only at zero displacement. The triangle cubic coefficient follows from a Taylor expansion of \(J(a,b)-J(-a,-b)\).

The supplied standard-library checker independently integrates the original defining radial profile at three smoothing parameters on three different polygons and checks the triangle antisymmetry at two scales; its observed output is `VERIFY_OK polygons=3 angular_integrals=9 cubic_asymmetry=2`. Finite numerical evidence is supportive and not an infinite proof. Mathematical scope is all fixed full-dimensional planar convex polygons containing the origin strictly inside.

## Originality — PASS, with documented residual risk

The directly relevant primary source is Haddad–Jiménez–Resende Guedes, arXiv:2610.11700v1 (2026-10-08), inspected in full HTML, particularly its definitions and critical-regime analysis in Section 5. It derives the first critical \(\log\cosh\) functional for smooth bodies; the paper does not specify an explicit finite-smoothing \(p^{-1}\) coefficient for polygons or a vertex-switch energy. An accessible related record extends the critical convergence to nonsmooth bodies and bounds the polytope error by \(O(1/p)\). That bound is **strictly weaker** than a formula for the next coefficient and does not imply the sign, its quadratic energy, or the asymmetry example.

Additional searches for polytope covariance smoothing, angular boundary layers, second-order critical radial means, Orlicz projection bodies and equivalent vertex energies did not identify a directly covering result. The nearest indexed radial-mean differentiability paper concerns a different \(R_p\)-body and fixed-parameter regularity, rather than the covariogram double limit. The earlier Orlicz projection-body construction supplies the leading geometric vocabulary, not a finite-parameter corner correction. Complete historical priority is not independently established: unindexed integral geometry literature or unpublished technical calculations might contain a related expression.

## Mathematical value — PASS

The first-order critical transition in a newly introduced smoothed covariogram leaves the leading finite-parameter error undetermined. The finding resolves that error exactly on the natural and infinite class of convex planar polygons; the coefficient is not merely a restatement of the first-order term. Its decomposition isolates a strictly positive, geometrically weighted vertex energy and exhibits an odd correction inaccessible to the even leading profile. These features have direct relevance to quantitative endpoint approximation and the effects of nonsmooth normal fans. A general higher-dimensional result is not asserted.

## Residual limitations

The error constants depend on the polygon and the compact displacement set; degenerating edges and angles are not controlled uniformly. The finite tests do not independently certify the theorem, and equivalence with unidentified old literature cannot be logically excluded by database searching alone.

Self-review: passed. Independent audit: not yet performed.
