# Scientific review

## Correctness — PASS
The left-end obstruction is exact, not heuristic: any positive-probability thinning parent must be supported at most \(n\) and its unique generating polynomial has a negative penultimate coefficient below \((a+n-1)/(a+b+n-1)\). At the boundary the penultimate coefficient vanishes. A terminating hypergeometric polynomial differential equation yields a descending recursion whose denominators are positive, whose right-side coefficients are nonnegative, and whose top initial mass is positive. This proves all other parent masses positive and summing to one, hence sufficiency and uniqueness. The special case \(n=1\) and all endpoint constraints are handled. Exact rational checks independently reconstruct 162 cases; the universal statement relies on the analytic proof.

## Originality — PASS
The closest source is Kella and Löpker, arXiv:2202.10296v1 / DOI:10.1016/j.indag.2022.09.003. Their Theorem 19 gives an implicit maximum over several signed-moment roots, not the explicit winning root for all Beta shapes. Their Example 10 settles \(\mathrm{Beta}(1,1)\); it is an included special case, not a new discovery. The all-positive-real-beta-shape classification, universal penultimate dominance, parent recursion and \(e^b\) inflation are not directly contained in the inspected text. Peyhardi (DOI:10.1214/23-BJPS585) and Jones (DOI:10.1111/stan.12337) concern generalized quasi-Pólya/convolution thinning identities, not the minimum of a constant ordinary Bernoulli retention probability. Targeted searches did not locate an equivalent explicit formula. An older count-dilation or inverse-beta-binomial formulation remains the main residual bibliographic risk.

## Value — PASS
Beta-binomial counts are the natural finite exchangeable and overdispersed Bernoulli family. The result classifies their exact recoverability by ordinary independent retention for **all** positive real shape parameters and all finite sizes, rather than a parameter-specific example. It identifies the unique boundary parent, its exact support hole and a computable positive recurrence, with a nontrivial general top-atom asymptotic. It is therefore a structural completion of an existing natural thinning-index problem.

## Scope and risk
No inference is claimed for arbitrary mixing distributions, for beta-random retention, or for infinite-population limits of the full parent law. The source's general root characterization is explicitly credited. Bibliographic originality may be affected by a terminology-disguised earlier theorem.

Self-review: passed. Independent audit: not yet performed.
