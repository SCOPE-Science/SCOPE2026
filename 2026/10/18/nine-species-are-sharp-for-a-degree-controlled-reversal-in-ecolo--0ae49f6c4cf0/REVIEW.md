# Scientific review: degree-controlled ecological matching-capacity reversal

## Correctness
PASS. The Bernoulli survivor-subset formula for expected maximum matching size is exact. For the sharp lower bound, every labeled binary interaction matrix with both guilds nonempty and total species at most eight is enumerated; only connected graphs are compared. Each survivor subset's matching size is optimized through exact recursive enumeration of injective allocations, rather than heuristic matching. All 70,492 eligible connected matrices and all 21 distinct coefficient-vector comparisons support coefficientwise dominance within degree-matched groups. The four-by-five witness was separately checked with an exhaustive assignment implementation and an exact integer polynomial identity. The finite enumeration supports exactly the stated finite bound.

## Originality
PASS under the searched literature, with unresolved bibliographic risk. Li–Zhang (2017) show that fixed degree sequences need not control static matching size, but do not address node-loss probability ordering or the nine-vertex threshold. Olesen et al. (2008) and Kaiser-Bunbury et al. (2010) address temporal network structure and species loss without this capacity functional. The accessible full Simmons et al. (2019) study explains motif-level ecological information not captured by degrees without deriving matching-capacity crossover bounds. Searches for matching reliability, expected maximum matching under vertex failures and exact small-size rank reversal did not reveal the same result; publication-level novelty is not independently certified.

## Mathematical value
PASS. A capacity-constrained one-to-one assignment is a natural benchmark when each surviving partner can serve only one target at a time. The result proves a tight structural boundary: below nine species degree-controlled allocation robustness rankings cannot reverse under independent species loss, but at nine they reverse exactly at a simple algebraic probability. It separates the implications of degree statistics, initial maximum capacity, and failure-robust capacity. It is not a claim about unrestricted real-world pollination, where partners can service many species.

## Closest sources and scientific limits
Li and Zhang (arXiv:1703.09041) is closest on degree-matched maximum matching; its static scale-free construction does not compare failure polynomials. Simmons et al. (DOI 10.1111/2041-210X.13149) is closest on degree-controlled ecological motif differences. The model is finite, unweighted, binary, connected, one-to-one, and uses independent exchangeable pollinator failures. Inaccessible supplementary materials and alternative graph-reliability terminology remain originality risks.

Self-review: passed. Independent audit: not yet performed.
