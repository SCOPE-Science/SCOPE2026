# Review

## Correctness

PASS. Determinant-power tilting changes the real central Wishart degrees of freedom from \(\nu\) to \(\nu+2s\) on an open interval around zero. Differentiating the tilted mean \((\nu+2s)\Sigma\) therefore gives the entrywise identity
\[
\operatorname{Cov}(W,\log\det W)=2\Sigma.
\]
The arbitrary linear-functional covariance follows by trace linearity. The whitened trace has the chi-square Laplace transform with \(\nu p\) degrees of freedom, and Bartlett decomposition gives the exact trigamma variance of the log determinant. The proportional and endpoint limits follow from standard trigamma bounds and harmonic-sum asymptotics. The accompanying transform checker agrees with every displayed formula on a broad parameter grid.

## Originality

PASS, with an explicit residual risk for the proportional-limit corollary. The full Cai--Liang--Zhou manuscript was inspected because it is the closest logdet source in the same Gaussian sample-covariance model. It gives the logdet Bartlett decomposition, exact trigamma variance, and high-dimensional CLT, but a targeted full-text search returns no trace occurrence and the inspected theorems do not state a trace/logdet mixed covariance.

Letac--Massam's Wishart moment paper was inspected at the publisher page. Its stated result concerns invariant polynomials and powers of the matrix or inverse, not logarithmic determinant mixed moments. Bai--Silverstein's general linear-spectral-statistic CLT is broader asymptotically and can plausibly imply the interior proportional covariance after evaluating its covariance functional; this is recorded as a residual risk rather than ignored. It does not, by itself, state or imply an exact finite identity for every \(p,\nu,\Sigma\).

No matching current- or prior-ledger claim was found. Database searches covering Wishart, trace/total scatter, log determinant/log generalized variance, exact covariance, determinant-power tilt, and aspect-ratio correlation returned no matching result.

## Value

PASS. Trace and determinant are the two canonical scalar summaries of multivariate scatter: one is additive in eigenvalues, the other multiplicative and directly tied to Gaussian entropy and generalized variance. Their standardized relationship changes qualitatively with dimension. The result gives an exact finite covariance and a parameter-free correlation law that interpolates from almost perfect alignment in thin dimension to vanishing alignment at the square hard edge. This is a structural dependence statement, not a recomputation of either marginal distribution.

Self-review: passed. Independent audit: not yet performed.


Deterministic replay: `VERIFY_OK mixed_checks=60 t2_checks=60 s2_checks=60 corr_checks=60 aspect_checks=9`.
