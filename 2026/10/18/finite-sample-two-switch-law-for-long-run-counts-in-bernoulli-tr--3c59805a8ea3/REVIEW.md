# Scientific review: finite-sample two-switch law for long-run counts

## Correctness — PASS
For independent Bernoulli trials and maximal success-run starts, a long-run indicator at position \(j\) forces exactly one compatible ordinary run start locally. Starts outside the neighborhood \([j-1,j+k]\) are independent of that indicator. Summing \(\operatorname{Cov}(R_n,B_j)=\mathbb EB_j(1-\sum_{i\in F_j}\mathbb EA_i)\) gives the exact covariance polynomial, including its distinct \(n=k\) boundary. Its values at \(0\), \(1/2\), and \(1\), plus the exact \(k=2\) factorization, establish every claimed sign phase. Independently enumerating all binary words through length 12 and comparing exact rational moments reproduces the formula at 198 parameter triples. The complete proof is symbolic, not inferred from finite enumeration.

## Originality — PASS, residual qualification
Makri–Psillakis, *On Success Runs of Length Exceeded a Threshold* (online July 18, 2009; DOI 10.1007/s11009-009-9147-1), provide marginal distribution and moments for the number of sufficiently long success runs. Stefanov (2000; DOI 10.1016/S0378-3758(99)00191-3) and Mytalas–Zazanis (2013; DOI 10.1016/j.jspi.2012.07.014) provide broader multivariate/asymptotic run statistics. The leading large-\(n\) dependence is consistent with that literature and is not separately claimed. Searches comparing the exact finite cross-covariance and equivalent start-indicator or two-threshold formulations did not locate the finite two-root classification, the \(n=2k+1\) feasibility threshold, or the degenerate \(k=2\) window. Published fixed-composition binary transition covariances and maximum-composition-block regressions concern distinct models/parameters. The finite classification is accepted as a best-knowledge contribution rather than independently verified priority; an older joint-run distribution could imply its polynomial after extraction.

## Mathematical value — PASS
The theorem completely classifies a natural cross-run statistic for every finite \(n\), threshold \(k\), and success probability \(p\). It captures a three-phase sign reversal exactly when two disjoint long runs become combinatorially feasible, and a separate collapsing interval for threshold two. These are interpretable finite-sample dependence boundaries and are not a marginal enumeration or arbitrary isolated parameter slice.

## Limitations and nearest literature
Assumes independent identically distributed Bernoulli trials; no extension to Markov words, unequal trial probabilities, or circular runs. Published general joint-count generating functions may imply the covariance without stating its threshold classification. There has been no external correctness or novelty certification.

Self-review: passed. Independent audit: not yet performed.
