# Self-review

## Correctness
PASS. The all-time sign law is derived from the exact two-dimensional Krylov compression. For \(R>1\) and \(\varepsilon>0\), its Ritz eigenvalues satisfy \(\lambda_-<\lambda_+<0\). The affine interpolant \(p_t\) of the exponential has strictly positive slope for \(t>0\). Three computed coordinates are therefore positive, and the fourth has the sign of \(p_t(-R)\). The criterion for a negative value is precisely \(\lambda_->-R\). A direct compressed-Gram determinant calculation gives
\[
\det(H+RM)=-R\big(R^3\varepsilon^4+2R(R^2-2R+2)\varepsilon^2+2-R\big).
\]
The other Sylvester minor is \(R-1>0\). This proves the complete rate/mass phase diagram. The interpolation formula yields the unique crossing time and the rare-mass limit. The exact rational witness is replayed by an embedded standard-library checker.

## Originality
PASS with explicit residual risk. Saad's full original analysis and Frommer–Güttel–Schweitzer's full archived preprint already supply the Ritz-interpolation identity, matrix-exponential Krylov framework, and norm-error analysis. Those ingredients are acknowledged as prior and do not themselves give a stochastic sign classification. Searches for equivalent Markov generator, rare-mass, rate-contrast, positivity, and Krylov expressions did not locate the displayed determinant criterion or its all-time consequences. A previous diagonal Lanczos spectral-width positivity law is a different worst-case fixed-time statement: it does not determine this fixed Markov generator's exact all-time phase diagram. The closest accessible alternative classical exponential paper was inspected at abstract level only; that is retained as a risk, not a claim of full noncoverage.

## Value
PASS. On two independent reversible Markov links, the exact evolution is stochastic for all times, but ordinary two-step Lanczos can assign a negative probability to a rare fast state. The precise transition depends on both link-rate contrast and initial rare mass, and the first sign violation remains at finite time as that mass tends to zero. This is a complete natural model classification and a useful warning about assessing probability propagation only by Krylov norm error. Renormalizing the computed mass cannot correct the negative sign.

## Closest literature and limitations
The full Saad and Frommer–Güttel–Schweitzer papers give the projection/interpolation framework; the latter is the primary MSC \(65F60\) archive anchor. The proof concerns a reducible symmetric four-state generator, a specified nonnegative initial distribution, and ordinary two-step projection. It does not address arbitrary or irreducible Markov generators, minimal state dimension, restarts, or roundoff. An older less searchable positivity result and the unread full text of Hochbruck–Lubich remain originality risks.

Self-review: passed. Independent audit: not yet performed.
