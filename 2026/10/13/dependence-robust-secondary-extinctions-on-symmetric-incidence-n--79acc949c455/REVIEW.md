# Self-review

## Correctness — PASS

For every realized failure set, secondary-extinction count dominates the minimum contained-hyperedge profile at the same cardinality. Convex minorization and Jensen establish the universal lower bound. Automorphism averaging of any minimum-cost fixed-cardinality set gives equal marginals, and mixing at two hull vertices attains the bound for every real marginal. On a cycle, a degree/boundary identity establishes the exact minimum induced-edge count for every cardinality, achieved using independent sets or independent complements. Its integer slopes determine the even/odd phase diagram. A separately executable integer/rational checker verifies profiles, orbit marginals and interpolation for all cycles of size 3 through 12; it does not replace the general proof. No endpoint or parity assumption is omitted.

## Originality — PASS, with explicitly bounded residual risk

The inspected primary ecological works by Memmott et al. (2004) and Bane et al. (2018) model knockout coextinctions and compare robustness, not unrestricted joint failures at fixed equal marginal probabilities. Huber and Marić (2019) fully treat admissible correlations at the single symmetric Bernoulli marginal and therefore cover the underlying symmetric-correlation polytope, not the full all-\(q\) cyclic optimum or the vertex-transitive hypergraph reduction as stated. Chaganty and Joe (2006) give a general Bernoulli-correlation feasibility framework which could implicitly imply a linear optimization formulation; their full text was unavailable, so stronger coverage remains a material risk. Exact objective and implications, rather than titles alone, were compared. Search noncoverage does not establish absolute novelty.

## Value — PASS

The general reduction is an exact distributionally robust ecological benchmark: one can assess how much secondary loss is structurally unavoidable even with maximally favorable dependence. The explicitly evaluated family shows a global consistency obstruction that local pairwise Fréchet bounds entirely miss, and identifies its exact size and shrinking marginal interval on every odd cyclic network. This is a motivated structural classification, not a change of names for a known independence formula or an arbitrary tiny finite example. The result does not assert that its extremizing law is ecologically realizable or typical.

## Evidence, literature proximity, and boundaries

Exact proof and supplementary checks are given in `RESULT.md` and `verify_cycles.py`. Comparators: Memmott et al., DOI 10.1098/rspb.2004.2909; Bane et al., DOI 10.1002/ece3.4529; Huber and Marić, DOI 10.1186/s40488-019-0091-5; Chaganty and Joe, DOI 10.1093/biomet/93.1.197. The inaccessible full text of the last article, plus possible older fixed-magnetization cycle results, leaves residual prior-coverage uncertainty. Any independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
