# Scientific review: crown-graph random greedy matching

## Correctness — PASS

The claim concerns the uniform random-edge greedy process on \(K_{n,n}\) with exactly the diagonal matching removed. The transition counts \(r(r-1)\), \(2r(k-r)\), and \((k-r)^2\) partition all \(k^2-r\) currently feasible edges. They establish the exact deficiency recurrence and show that premature termination is possible only with one pair of unmatched vertices. The telescoping first-moment identity is algebraically exact. A separate second-factorial-moment contraction proves a \(k^4/n^2\) bound, and substituting that bound yields the displayed \(16H_n/n^2\) finite error. All denominators are positive for the specified integer domain \(n\ge2\). The independent bit-mask dynamic program and a complete size-three edge-order enumeration agree with the overlap-chain calculations. Numerical diagnostics are not used to justify the infinite-size limit.

## Originality — PASS, subject to historical-priority limitations

The specific assertion is an exact crown-graph failure-probability recurrence together with the sharp asymptotic constant \(2\) and an explicit harmonic error bound. The closest directly inspected source, Arnosti (2021), treats comparisons among greedy matching algorithms when the bipartite edge set itself is random. Tang, Wu and Zhang (2019/2023) treat approximation guarantees in oblivious matching; neither of those statements implies the rare terminal obstruction in the fixed crown graph. Dyer and Frieze (1991) give the classical random-edge greedy algorithm and broad performance bounds, but the accessible abstract does not establish a crown-graph sharp constant. Searches for crown-graph random greedy matching, a forbidden diagonal, a terminal pair and an asymptotic \(2/n\) law did not identify an equivalent result. Search absence is not proof of novelty, and historical priority remains a real residual risk.

## Value — PASS

A crown graph is a canonical, dense bipartite graph with exactly one forbidden partner per vertex. The existence of perfect matchings is obvious for \(n\ge2\), but a sequential maximal matching can fail. The result quantifies that failure at the sharp \(1/n\) scale and explains why the coefficient is \(2\), instead of the \(1\) obtained from independent, uniformly random final labels. The proof's overlap-count lumping and factorial-moment contraction provide a reusable method for rare terminal obstructions in dense greedy algorithms, without claiming a result for other deleted-edge patterns.

## Closest work and limits

- Arnosti, *Greedy Matching in Bipartite Random Graphs*, https://doi.org/10.1287/stsy.2021.0082 — full-text algorithm and theorem comparisons, distinct random-edge-set model.
- Tang, Wu and Zhang, *Towards a Better Understanding of Randomized Greedy Matching*, https://arxiv.org/abs/1907.05135 — full-text approximation-ratio results, no stated crown deficiency law.
- Dyer and Frieze, *Randomized greedy matching*, https://doi.org/10.1002/rsa.3240020104 — classical algorithm, abstract inspected, older full text not verified in this comparison.

The result is specific to uniform random feasible-edge selection on crown graphs; the numerical constant in the stated error is not optimized. Its historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
