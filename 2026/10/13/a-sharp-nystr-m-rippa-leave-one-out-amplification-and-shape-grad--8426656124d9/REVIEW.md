# Scientific review

## Correctness — PASS

The claim is an exact two-by-two matrix identity plus sharp scalar optimization. Direct inverse calculation produces the pair of Rippa leave-one-out maps. Their difference has one nonzero matrix entry, making its operator norm and attaining vector immediate. The derivative numerator \(\lambda-(1+3\lambda)t^2-t^4\) has exactly one zero in \((0,1)\), giving the sharp maximizer and the \(\lambda^{-1/2}\) limit. The independent derivative for squared loss has the factor \(\lambda-t^2\), establishing the phase. Rational inverse checks and numerical peak checks in `verify.py` passed. No finite check is used as a proof of the continuous or asymptotic result.

## Originality — PASS, with residual risk

The closest complete primary comparison is Lyu–Veiga (arXiv:2602.10248v1), whose Sections 2–3 introduce the same surrogate and discuss gradients; Section 5 notes empirical instability but does not derive the sharp two-site amplification, singular regularization limit, or exact opposite-gradient region. Rippa (1999) gives the classical inverse-diagonal relation. Bucci–Nakatsukasa–Park (arXiv:2511.15583v2) studies numerical stability of the Nyström core in the presence of roundoff; here the core equals one and the phenomenon is exact arithmetic. Searches of related published mathematical results and the relevant prior research claims found no equivalent statement. A disguised equivalent in kernel approximation or Gaussian-process leave-one-out literature remains possible, and the proof uses elementary identities; novelty should not be mistaken for an exhaustive literature certificate.

## Value — PASS

The claim directly answers a mathematically motivated gap in a recent shape-parameter tuning method: when does its surrogate objective's *direction* disagree with the matched-ridge full objective? It provides a complete, exact two-site phase diagram, an attained sharp worst-data amplification and its asymptotic constant, and identifies a failure mechanism not explained by conditioning of the original kernel. The example is a legitimate inverse-multiquadric Gram matrix, not an artificial nonkernel system. This is a usable diagnostic boundary for any small-ridge low-rank kernel leave-one-out calculation, although higher-rank behavior and algorithmic prevalence are not determined.

## Residual limitations

One landmark and two sites are a small special case; low-rank accuracy is poor at the amplification peak even though the full kernel is well-conditioned. The ridge is positive and exact arithmetic is assumed. The false stationary point is a **maximum**, so no trapping claim is made. Independent historical originality assessment and empirical significance for large landmark budgets remain unresolved.

Self-review: passed. Independent audit: not yet performed.
