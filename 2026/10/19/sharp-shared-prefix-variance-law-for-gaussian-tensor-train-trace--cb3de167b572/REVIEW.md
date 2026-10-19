# Scientific assessment

## Correctness — PASS

For normalized independent Gaussian TT cores, Gaussian isotropy gives the exact conditional squared-projection law \(\mathbb E[(u^{\mathsf T}\omega)^2\mid\mathcal F_k]=S_k\). Conditional Gaussian fourth-moment contraction yields \(\mathbb E S_k^2\le(1+2/r)^k\), with equality for separable unit tensors. Positive-semidefinite spectral decomposition, the centered \(L^2\) triangle inequality, and conditional independence between suffixes establish both terms of the sharp variance envelope simultaneously. For separable rank-one targets the same moments are equalities, and a product of independent chi-square factors gives the strong-law limit. The gamma-ratio expansion proves the proportional-order lognormal limit. The local reproduction program passed 11,529 exact rational / finite asymptotic / supporting Gaussian-contraction checks; finite experiments were not used as proofs.

## Originality — PASS (subject to residual indexing risk)

Closest directly relevant source: Bujanović, Kressner and Olić, arXiv:2606.15679v1, Definition 1, Lemma 4, Theorem 5, Theorem 7. It establishes marginal Gaussian TT fourth moments and concentration using independent complete TT vectors; those facts are acknowledged and provide an ingredient, not the exact joint-law variance for samples with shared initial cores. Cazeaux, Dupuy and Figueroa Justiniano, arXiv:2603.11009 (full PDF, §§3–5), analyze TTStack independent row blocks and cross-mode partial sketches but not correlated Hutchinson trace repetitions of the specified kind. Meyer and Avron, arXiv:2309.04952 (full PDF, §§1–3), study independent Kronecker probes rather than shared prefixes at general TT rank. Bujanović and Kressner, arXiv:2004.06433, concern independent rank-one structured probes. Searches for these titles, source IDs, common-core aliases, conditional cross moments and shared-prefix sampling in published mathematical records disclosed no identical or stronger coverage. Search failure alone is not proof of novelty. The largest residual risk is an unindexed treatment of correlated structured trace probes; the theorem has no independent literature audit.

## Value — PASS

The paper's independent-vector concentration guarantees invite a natural implementation question: can many TT probes reuse already-generated cores while independently completing the remaining tensors? The exact two-term extremal law determines the price of that sharing, including a strictly positive sampling-error floor for every finite bond rank and any nonempty common prefix. Its sharpness over every PSD matrix and the proportional-order phase law yield mathematically precise configuration criteria, not an arbitrary isolated example or a routine sign/normalization check. The phenomenon matters when exploiting tensor structure for stochastic numerical trace estimation; no runtime speedup is claimed.

## Scientific boundaries

The result is restricted to a fully shared prefix of real standard Gaussian TT cores with a common bond rank, a deterministic PSD target and an exact trace estimator. The rank-one witness demonstrates worst-case nonconsistency but does not imply every target has this behavior. The lognormal statement requires simultaneous proportional rank/core limits. No comparison of stochastic runtime costs or finite-precision schemes is attempted. Bibliographic uniqueness has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
