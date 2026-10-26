# Self-review

## Correctness — PASS
The legal-word recurrence and integer bijection agree term for term with the source-defined \(f\)-sequence. The bounded-zero-run automaton exactly enforces the gap rule, and a sufficiently long single-one word realizes every endpoint of the period matrix, proving primitivity. Analytic Perron perturbation supplies linear mean and variance; the Poisson martingale decomposition establishes that zero asymptotic variance would make every closed-walk reward equal its length times a common mean. The all-zero closed walk and a one-selection closed walk contradict this. The interval law is exactly one plus the preceding-prefix law. Standalone exhaustive checks support but cannot replace these proofs.

## Originality — PASS, subject to residual risk
The principal 2013 paper asks explicitly in Section 5(3) if arbitrary periodic \(f\)-decompositions are Gaussian; it proves only selected periodic patterns. The broad 2003 Bertoni–Choffrut–Goldwurm–Lonati symbol-count central limit theorem assumes a primitive homogeneous *one-symbol* transition matrix; the natural phase-augmented digit automaton here has period \(m\), while the primitive period-block matrix has rewards \(0,1,\ldots,m\). Thus it does not literally supply the universal specific theorem without a reduction and nondegeneracy check; those steps are proved here. A different encoding could make the result an unreported corollary of general regular-language theory, and that is a material residual novelty risk. Published mathematical sources checked did not state an exact or dominating all-periodic assertion; absence from checked sources is not a proof of uniqueness.

## Value — PASS
The result resolves the arbitrary-periodic case of a numbered, explicitly published question, with no excluded positive period, including zero forbidden gaps and patterns with forbidden distance greater than the period. Strict positivity of the variance makes the conclusion nondegenerate and useful for all growing decomposition intervals. This is more than a routine specialization to one chosen period.

## Literature and limits
Original question: Demontigny et al., arXiv:1309.5599v1, Section 5(3). Strongest generic comparison: Bertoni et al., Theoretical Computer Science 302 (2003), Theorems 2–4, DOI 10.1016/S0304-3975(02)00892-7. Further context: arXiv:1409.0488v1 and arXiv:1309.5600v1. Complete mathematical proof for each fixed period does not give nonperiodic cases, a uniform rate, or independent validation. Subsequent regular-language literature could contain an equivalent statement not found.

Self-review: passed. Independent audit: not yet performed.
