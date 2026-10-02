# Independent audit — 2026-10-01

## Final claim

If \(|\sum_{j=1}^m X_j|\ge I_d\) and \(d\ge m(k-1)+1\), then \(\lambda_k(\sum_j|X_j|)\ge m^{-1/2}\); for two summands this gives the sharp \(1/\sqrt2\) median barrier in the stated odd and even dimensions.

## Correctness — PASS

The dimension-leakage proof is correct. The low spectral subspace \(E\) has dimension \(d-k+1\); intersecting the kernels of the first \(m-1\) leakage maps loses at most \((m-1)(k-1)\) dimensions, so the hypothesis leaves a nonzero vector. The sum of leakage maps is zero because \(E\) is a spectral subspace of \(Q\), forcing the last leakage to vanish too. Positive compressions satisfy \(0\le C_j\le cI\), hence \(C_j^2\le cC_j\), which gives \(\sum_j\|X_jx\|^2\le c^2\); expansivity and Cauchy--Schwarz give \(1\le mc^2\). For the explicit sharp family I independently formed \(|A_t|+|B_t|\): its middle eigenvalue was 0.91268 at \(t=1\), 0.74072 at \(t=10\), 0.71062 at \(t=100\), and 0.707460 at \(t=1000\), converging to \(1/\sqrt2\) as claimed. The direct-sum counting then gives the stated sharp odd and even dimensions.

Checked sources:
- J.-C. Bourin, E.-Y. Lee, Triangle inequalities for the operator symmetric modulus, arXiv:2602.19607 (2026)
- T. Zhang, Operator symmetric moduli and sharp triangle inequalities, arXiv:2603.01046 (2026)
- M. A. Aouichaoui, E.-Y. Lee, Solutions to some open problems in matrix analysis, arXiv:2609.20094 (2026)
- Resultary record SCOPE-polar-wandering-symmetric-modulus-von-neumann--66cc75173a62
- Independent numerical replay of the explicit \(3\times3\) sharp family

Residual risks:
- The general \(m^{-1/2}\) lower bound is only claimed under \(d\ge m(k-1)+1\), and sharpness is not claimed for every triple.

## Originality — PASS

Best-of-knowledge originality passes for the ordinary-modulus dimension-leakage theorem and sharp two-summand median consequence. The inspected primary abstracts concern symmetric moduli and three-summand ordinary-modulus counterexamples; Resultary's earlier polar-wandering theorem is also for symmetric moduli. Those statements do not imply a \(1/\sqrt2\) lower bound for \(|A|+|B|\). No stronger ordinary-modulus result with the same dimension threshold was located.

### Equivalent formulations

Searches:
- Resultary query: expansive ordinary modulus median eigenvalue two summands 1/sqrt(2)
- Resultary query: ordinary operator modulus expansive sum eigenvalue median two matrices

Evidence:
- The assigned record was the only exact ordinary-modulus median hit. The strongest nearby SCOPE record concerns the symmetric modulus in von Neumann algebras.

Reasoning: The relevant aliases are middle eigenvalue/singular-value lower bounds for sums of ordinary moduli under an expansive total sum and leakage/rank-nullity formulations.

### Broader coverage

Searches:
- Bourin--Lee arXiv:2602.19607
- Zhang arXiv:2603.01046
- Aouichaoui--Lee arXiv:2609.20094
- SCOPE-polar-wandering-symmetric-modulus-von-neumann--66cc75173a62

Evidence:
- The first two sources study symmetric moduli; Aouichaoui--Lee's accessible abstract includes a three-summand ordinary-modulus inequality/counterexample context; the prior SCOPE result explicitly concerns symmetric moduli.

Reasoning: Symmetric-modulus bounds involve \((|X|+|X^*|)/2\) and do not mechanically control the ordinary sum \(\sum|X_j|\) in the required direction. The three-summand result demonstrates a boundary rather than covering the two-summand theorem.

### Exact database or table

Searches:
- Resultary exact ordinary-modulus searches
- Targeted web searches for the Bourin--Lee/Zhang/Aouichaoui--Lee papers and the constant \(1/\sqrt2\)

Evidence:
- No prior exact table/formula for the two-summand ordinary-modulus median constant was located.

Reasoning: The sharpness statement is constructive and structural; search absence is only best-of-knowledge evidence.

### Claim versus prior implication

Searches:
- Bourin--Lee problem context
- Aouichaoui--Lee three-summand ordinary-modulus result
- Assigned dimension-leakage proof

Evidence:
- The prior literature motivates middle-eigenvalue questions and supplies the contrasting three-summand behavior, but an additional common-kernel argument is needed to obtain the audited two-summand bound.

Reasoning: No inspected stronger theorem was found from which the final claim follows as a special case.

### Source inspections

- **Triangle inequalities for the operator symmetric modulus** (https://arxiv.org/abs/2602.19607): trigger — Motivating median-eigenvalue questions and neighboring symmetric-modulus inequalities; material read — Primary abstract plus publicly available article summary/full-text excerpt; method — Primary/authorized public-text inspection; assessment — Neighboring but not covering; its principal object is the symmetric modulus.; evidence — The paper studies \((|Z|+|Z^*|)/2\) and broader symmetric-modulus triangle inequalities.
- **Solutions to some open problems in matrix analysis** (https://arxiv.org/abs/2609.20094): trigger — Recent solution paper containing three-summand ordinary-modulus phenomena; material read — Primary abstract and bibliographic record; method — Primary-source abstract inspection; assessment — Provides the contrasting three-summand context, not the audited two-summand median theorem.; evidence — The abstract states a sharp three-contraction inequality and an eigenvalue inequality involving the symmetric modulus.

Checked sources:
- J.-C. Bourin, E.-Y. Lee, Triangle inequalities for the operator symmetric modulus, arXiv:2602.19607 (2026)
- T. Zhang, Operator symmetric moduli and sharp triangle inequalities, arXiv:2603.01046 (2026)
- M. A. Aouichaoui, E.-Y. Lee, Solutions to some open problems in matrix analysis, arXiv:2609.20094 (2026)
- Resultary record SCOPE-polar-wandering-symmetric-modulus-von-neumann--66cc75173a62
- Independent numerical replay of the explicit \(3\times3\) sharp family

Residual risks:
- Older matrix-inequality literature may contain a differently phrased ordinary-modulus singular-value consequence; no such implication was located in the searches performed.
- The exact two-summand median constant in dimension four remains open, as the record states.

## Scientific value — PASS

The theorem gives a sharp positive barrier in the two-summand case of a recent matrix-analysis question and explains, through an exact dimension threshold, why the corresponding three-summand critical example can collapse. The general leakage lemma and sharp families are reusable structural information, not merely a numerical improvement.

Checked sources:
- J.-C. Bourin, E.-Y. Lee, Triangle inequalities for the operator symmetric modulus, arXiv:2602.19607 (2026)
- T. Zhang, Operator symmetric moduli and sharp triangle inequalities, arXiv:2603.01046 (2026)
- M. A. Aouichaoui, E.-Y. Lee, Solutions to some open problems in matrix analysis, arXiv:2609.20094 (2026)
- Resultary record SCOPE-polar-wandering-symmetric-modulus-von-neumann--66cc75173a62
- Independent numerical replay of the explicit \(3\times3\) sharp family

Residual risks:
- Older matrix-inequality literature may contain a differently phrased ordinary-modulus singular-value consequence; no such implication was located in the searches performed.
- The exact two-summand median constant in dimension four remains open, as the record states.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
