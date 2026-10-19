# Scientific review

## Correctness — PASS

The theorem quantifies over every dimension \(n\ge2\), every continuous nonincreasing real zonal kernel and every measurable boundary map into the closed ball. The proof derives a nonzero nonatomic Stieltjes measure from nonconstancy, propagates equality through the published mean-width/cap rearrangement inequality, and chooses an active radius avoiding the countable zero set of all nonconstant-degree spherical cap multipliers. Equality in strict Jensen concavity forces sphere-valued boundary data; harmonic completeness forces uniform pushforward; uniqueness of the fixed-mass bathtub selector yields exact cap pullbacks. Preservation of cap symmetric-difference measure makes their center map locally distance-preserving and hence globally orthogonal. Constant kernels and converse orthogonal maps are checked separately. The hemisphere-step example demonstrates the discontinuous boundary. Finite numerical checks are not used as the infinite proof.

## Originality — PASS, with historical-priority risk

Zhong–Kalaj, arXiv:2609.09316 (first public 2026-09-08), establishes the numerical sharp inequality under continuity and monotonicity, but restricts its asserted equality classification to strictly decreasing kernels. The new theorem extends that classification to the entire nonconstant continuous nonincreasing class, including plateau and singular monotone kernels. Its mechanism of a generic charged cap radius and fixed-radius cap-pullback rigidity is not supplied by the inspected original equality argument. Related single-radius cap spectral literature, notably arXiv:2308.00694, addresses discrepancy rather than equality in this width inequality. Relevant searches found no stronger covering statement, but search absence does not establish absolute priority; older cap-preserver results in alternate language may exist.

## Value — PASS

The improvement resolves the natural equality question left between the original theorem's broad inequality hypotheses and narrower equality hypotheses. It applies to nonsmooth and singular Stieltjes kernels for which strict-decrease reasoning is unavailable, and the explicit nonorthogonal extremizer for a jump kernel identifies a meaningful boundary of the extension. The result is not a numerical adjustment or a restatement of the strict case.

## Reproducibility and limitations

The complete analytic derivation, hypotheses, degree-by-degree spectral argument and fixed-radius rigidity lemma are in `RESULT.md`; `verify_examples.py` gives elementary corroboration on the circle, not independent universal certification. The result does not strengthen the original inequality constant; it strengthens only the equality classification. Historical priority remains qualified and an independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
