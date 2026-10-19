# Self-review

**Claim:** The mean-square error of exact one-Gaussian-probe log-determinant estimation with a Gaussian Nyström preconditioner on \(\operatorname{diag}(tI_r,I_s)\) has the exact leading term \(2(r-\ell)_+\log^2(1+t)\), with a nonnegative contrast-uniformly bounded remainder. The sharp uniform boundedness condition is \(\ell\geq r\).

## Correctness: PASS
Gaussian quadratic-form variance is exact. The skipped spike eigenspace is invariant and has dimension \((r-\ell)_+\). On its orthogonal complement, the Nyström variational residual is bounded by \(1+\|VU^+\|^2\), independently of \(t\). A Gaussian minor and its QR chi factors provide the finite half-moment of \(\|U^+\|\), which yields finite expected squared logarithm. These jointly prove the exact leading coefficient and the iff threshold; 1,008 reproducible finite cases independently check the critical matrix identities. No numerical sample is treated as proof of an infinite statement.

## Originality: PASS, with residual risk
The closest complete primary source, Cortinovis--Toni (arXiv:2601.05778, first public 2026-01-09; 2026 publisher version), defines the precise estimator and derives the ideal-truncation variance and a generic Nyström estimate requiring \(p\geq2\). Those assertions do not cover the present zero-oversampling two-level Gaussian-sketch iff criterion. Frangella--Tropp--Udell's Nyström PCG paper treats linear-solve conditioning, not this probe-variance observable. Published similarity and alias searches found conceptually related but non-covering spectral-filter and Gaussian-fluctuation results. Priority is not independently established, and unknown equivalent older arguments remain possible.

## Value: PASS
The sharp sketch dimension \(\ell=r\) answers whether one probe remains mean-square reliable as a fixed number of dominant eigenvalues become arbitrarily large, with an explicit quadratic logarithmic loss below threshold. The result identifies a zero-oversampling regime omitted by the source's general error bound and explains why inverse-Wishart raw-moment difficulties need not doom logarithmic trace estimation.

## Limitations
Only fixed-dimensional two-level positive-definite spectra, independent real Gaussian sketch and probe, exact arithmetic, and exact quadratic forms. No dimension-free constant or bound on Lanczos approximation, finite precision, general spectra, or runtime is proved. Residual priority uncertainty persists; independent audit is not yet performed.

Self-review: passed. Independent audit: not yet performed.
