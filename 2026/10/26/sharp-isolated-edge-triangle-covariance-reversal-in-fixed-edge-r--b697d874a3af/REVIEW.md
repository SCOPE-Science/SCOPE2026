# Mathematical review

## Correctness: PASS
The count of allowed residual graphs after forcing one isolated edge is exact. Disjoint triangle pairs give \(\mathbb E(ST)\); a triangle sharing any endpoint cannot coexist with an isolated edge. Their ratio simplifies to \(K_n(m-3)/m\); the displayed rational inequalities locate its crossing between consecutive integers for all \(n\ge5\). Zero-support cases and the independent-edge calculation have separate explicit proofs. The sparse limit uses standard falling-factorial/hypergeometric limits, with every normalization checked. Running `CHECK.py` yielded 3,955 exact checks and exhaustive enumeration through six vertices. Finite enumeration was not used as an infinite proof.

## Originality: PASS, with historical-priority risk
Comparisons searched the exact component statistic (isolated \(K_2\)-components), the noninduced triangle census, fixed-edge and independent-edge ensembles, exact moment/covariance identities, and the equivalent conditional expectation \(\mathbb E[T\mid e\text{ isolated}]\). The most relevant accessible full paper, Goldschmidt–Griffiths–Scott (2019), focuses on deviations of noninduced subgraph counts, not isolated component indicators; Ellis–Ferry (2010) treats overlap formulas in \(G(n,p)\). The closest published-result-index match concerns total component-count/triangle covariance for independent bond percolation, not this pair of statistics under fixed edge count. No inspected primary statement subsumed the exact parity-sensitive integer cutoff. The absence of a match is not a proof of historical priority; some older full texts were inaccessible.

## Mathematical value: PASS
The motivated comparison of the fixed-edge (microcanonical) and independent-edge (canonical) graph ensembles produces a sharp, nontrivial **sign reversal** in a natural pair of local and cyclic subgraph statistics, at the critical mean-degree-one window. The complete finite-parameter sign diagram and sparse asymptotic constant go beyond a numerical sample or an arbitrary isolated covariance computation. The claim does not require a general downstream theorem.

## Limits and context
The result establishes covariance signs, not all notions of positive or negative association. Independent replication and a complete historical priority audit remain outstanding. Relevant sources: DOI `10.1002/rsa.10113`, DOI `10.1016/j.dam.2009.11.012`, and `arXiv:1902.06830`.

Self-review: passed. Independent audit: not yet performed.
