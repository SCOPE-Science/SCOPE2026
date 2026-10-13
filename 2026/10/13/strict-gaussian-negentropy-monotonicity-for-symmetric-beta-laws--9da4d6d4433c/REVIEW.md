# Scientific review: symmetric beta Gaussian negentropy

## Correctness — PASS

The claim concerns all strictly positive real symmetric beta shapes, forward KL divergence, and the unique moment-matched Gaussian. The Gaussian cross-entropy minimization is exact. Differentiation of the beta entropy and trigamma duplication yield a single derivative equation; the integral representation of its trigamma difference and strict AM–GM prove its sign globally. The decisive denominator comparison is the identity \((2a-1/2)^2-2(a-1)(2a+1)=9/4\), valid in the only regime where the positive term must be bounded. Integrating the proven large-shape derivative asymptotic establishes \(3/16\), and the exact beta law of odd uniform-sample medians supplies the stated \(3/4\) constant. The standalone verifier passed its independent finite diagnostics. Numerical checks do not substitute for either universal proof.

## Originality — PASS, with outstanding priority risk

The fully inspected arXiv:2205.04621v1 treats general order-statistic entropic convergence, includes an exact entropy lemma and remarks on a second-order symmetric approximation, but not the asserted strict *optimal Gaussian* negentropy monotonicity for every real symmetric beta shape; the asymptotic coefficient here is not claimed independently of that entropy formula. The fully inspected arXiv:2101.02094v5 studies beta concentration and central moments rather than KL-projection monotonicity. Searches using Gaussian negentropy, entropy gap, symmetric-beta KL, central uniform median, and trigamma aliases did not identify an implication that supplies the all-shape strict sign. The published 2023 journal expansion of the order-statistics work explicitly mentions monotonicity in its abstract and could contain closer material than the accessible preprint; its full text remains uninspected and is a specific priority risk. The review does not assert uniqueness against unpublished or inaccessible work.

## Value — PASS

A symmetric beta law passes from boundary-singular and U-shaped through uniform to interior-unimodal as its positive real shape varies; showing strictly improving moment-standardized Gaussianity across the entire family is not a discrete normal-approximation heuristic. The derivative proof supplies a global entropy ordering, while the median specialization gives an exact best-Gaussian projection and sharp finite-sample convergence constant, with strict improvement at every odd sample-size increment. The observation is natural for assessing the finite-sample Gaussian approximation of robust central order statistics. It does not establish the corresponding assertion for asymmetric shape profiles, arbitrary parents, or reverse KL divergence.

Self-review: passed. Independent audit: not yet performed.
