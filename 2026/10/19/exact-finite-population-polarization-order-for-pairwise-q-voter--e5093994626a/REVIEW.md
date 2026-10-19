# Scientific review

## Correctness — PASS

For a complete graph, the opinion count is an irreducible birth–death chain whenever \(0<p<1\). The two distinct sampling schemes give the exact two-point unanimity functions; the proof compares their stationary detailed-balance ratios. The key correction \(j(M-j)\) is reflection-symmetric while the distinct-sampling denominator is strictly increasing, giving a one-crossing radial likelihood ratio. Symmetry converts radial stochastic dominance into a convex-order comparison. For \(N=3\), every ratio is equal; for \(N\ge4\), a strict inner step ensures a strictly smaller variance under repeated sampling. For \(q=3,N=4\), direct finite-state ratios reverse the inequality. Packaged independent microscopic tuple enumeration and rational invariant-distribution checks passed 6,492 assertions. Finite experiments are not relied on as the proof.

## Originality — PASS, with residual literature risk

The closest primary source, Weron–Nyczka–Szwabiński (2024, DOI 10.3390/e26020132), studies exactly the distinction between repeated and distinct influence selection, but develops simulated concentration curves and deterministic mean-field/pair approximations, not the exact finite-size invariant-law likelihood-ratio comparison. Vieira et al. (2020, arXiv:2002.04715) treat a broader threshold \(q\)-voter mechanism but their inspected introduction, model, mean-field equations, phase diagrams, final discussion, and appendices do not establish this finite \(q=2\) convex-order result or its \(q=3,N=4\) reversal. Searches for finite stationary distributions, sampling replacement, stochastic/convex orders, and exact q-voter polarization found no applicable stronger statement. The general birth–death and stochastic-order tools are established; the exact comparison for the influence models is the assessed contribution. Residual risk: the full 2024 publisher document was available in substantial indexed sections but direct retrieval encountered rate limiting; less-indexed mathematical literature may contain an equivalent comparison.

## Value — PASS

This gives an all-population and all-noise distributional inequality, rather than merely comparing simulated means or a few variances. It resolves the precise finite-size effect of influencer repetition for \(q=2\), supplies an exact boundary at \(N=3\), and demonstrates a provable reversal at the smallest admissible three-person influence group. The direction change is directly tied to a modeling choice highlighted by the motivating paper and warns against extrapolating pair-influence intuitions to larger groups. It does not assert a statement for sparse networks or transient distributions.

Self-review: passed. Independent audit: not yet performed.
