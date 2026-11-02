# Scientific assessment

## Correctness — PASS

The exact Markov transition matrix has stationary law \((1-p,p)\) and second eigenvalue \(\rho\). Conditioning at selected indices gives a product expression for each pool's all-negative event, and summing test costs reduces all fifteen partitions to five pool-size structures. The \(2+1+1\) structure is dominated for every admissible parameter; all other candidates appear in the theorem's minimum. The positive-correlation dominance proof treats the equality \(ua=1/2\) separately. Four exact-rational negative-correlation examples prove all four structures possess nonempty strict winning regions. The general single-pool lemma uses the unique maxima of integer powers of \(\rho\). A standalone full-state exact checker passed 2,223 assertions over 132 feasible rational parameter points. This checker supplements, rather than replaces, the universal algebraic argument.

## Originality — PASS with residual priority risk

Dorfman's original two-stage procedure establishes the cost model, not the spatial dependence result. Hong and Scaglione's full 2008 text treats spatial binary Markov data but its algorithms select contiguous sensor groups and use data-retrieval queries, not an exhaustive unrestricted four-specimen two-stage diagnostic partition. Lendle, Hudgens and Qaqish's full 2011/2012 manuscript derives hierarchical and matrix screening efficiencies for exchangeable clusters and explicitly identifies nonexchangeable within-cluster models as future research. Landolfi and Lall's 2023 full open preprint treats symmetric/exchangeable statuses, so it cannot distinguish the two pairings \(12|34\) and \(13|24\). Searches for 'negative Markov autocorrelation', 'Dorfman four-site grouping', 'noncontiguous parity pools' and aliases did not surface the exact four-regime theorem. No search proves historical priority; more obscure prior group-testing optimization may already imply an equivalent result.

## Value — PASS

The exact parameter-phase classification addresses a natural screening decision: whether to pool an ordered cluster together, split it, or test separately when adjacent outcomes are dependent. It exhibits a strict qualitative failure of the usual intuition that geographically adjacent specimens should be pooled together: negative Markov correlation makes alternating sites more likely jointly disease-free. The four-site problem is the smallest ordered population permitting two disjoint strictly noncontiguous paired pools, and the all-length single-pool gap theorem shows this is a general correlation-sign principle rather than an isolated numerical example. There is no claim of empirical prevalence fit or clinical deployment readiness.

## Closest literature and limitations

Closely related: Dorfman (1943), Hong and Scaglione (2008), Lendle–Hudgens–Qaqish (2011/2012), Landolfi–Lall (2023/2024). Their protocols or distributional assumptions do not imply the exact nonexchangeable four-partition classification as stated, but a historically equivalent optimization may exist. The results assume perfect tests, strictly feasible transition probabilities, unrestricted mixing of specimens, and an exactly first-order stationary binary Markov model.

Self-review: passed. Independent audit: not yet performed.
