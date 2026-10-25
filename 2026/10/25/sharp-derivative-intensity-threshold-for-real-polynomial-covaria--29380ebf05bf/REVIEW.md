# Scientific review

## Correctness — PASS
For all integers \(N\ge1\) and \(0\le K\le N\), the diagonal mixed-derivative data are an invertible triangular transform of the transverse even Taylor coefficients \(f_0,\ldots,f_K\) of the symmetric bivariate matrix polynomial. Exactly their vanishing is divisibility by \((X-Y)^{2K+2}\). The separate-degree constraint yields the kernel dimension without counting only a numerical rank. Below threshold, the explicit kernel matrix produces two strictly positive-definite, observationally identical covariances. Exact rational experiments at degrees 1–12 check the predictions, but the proof holds for all degrees.

## Originality — PASS, with residual priority uncertainty
The closest source is Chen–Wang (arXiv:2304.06206, Theorem 4.1/Lemma 4.2), proving that pure complex polynomial data are phase/conjugation retrievable using only zeroth and first derivative intensities. This is an important stricter novelty boundary: we do not present that pure-state implication as new. Their rank-restricted theorem does not recover every real positive-definite coefficient covariance, whereas the new result has the full kernel, every nullity, and an exact necessary-and-sufficient threshold on the *full* PSD cone. Grohs–Liehr–Rathmair (arXiv:2207.10620) study unrelated STFT sampling with multiple windows. Neither source includes the all-rank PSD statement or the divisibility classification in inspected relevant sections. Specialized older covariance-diagonal jet work may exist under different names; absence of an index match is not conclusive proof of novelty.

## Value — PASS
All-rank covariance reconstruction is the natural convex/lifted version of intensity tomography; it cannot be deduced from the much easier rank-one or rank-two pure-state uniqueness problem. The exact optimal derivative-order threshold, complete kernel dimension, and strictly positive-definite ambiguity examples give a usable criterion for identifiability of mixed signals, together with a finite acquisition scheme. The phenomenon is structural across arbitrary degree and not a selected numerical instance.

## Limitations and closest literature
No noise condition number, distributional identification, or minimal count of spatial sample locations is proved. The recovered matrix must be real symmetric; imaginary skew-Hermitian covariance components would be undetectable. Chen–Wang's 2023 pure-state theorem is explicitly acknowledged as stronger *for pure signals*; mixed-state identifiability is a different question. Possible uninspected historic diagonal-jet covariance theorems remain a priority risk.

Self-review: passed. Independent audit: not yet performed.
