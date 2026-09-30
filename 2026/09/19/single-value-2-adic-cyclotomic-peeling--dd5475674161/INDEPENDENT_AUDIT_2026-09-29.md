# Independent audit — Exact 2-adic peeling from a single cyclotomic value

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/single-value-2-adic-cyclotomic-peeling--dd5475674161`  
**Audited tree:** `41c4d6f06d3d5d6a9acbc8c189c258ccfdcb3051`

## Disposition

**PASSED.**

## Correctness

**PASS.** The 2-adic peeling identities are correct. Radical reduction gives a=v_2(Phi_n(2)-1)=n/rad(n), and the squarefree Möbius product gives C^epsilon=H_a(P). After dividing an initial-support fingerprint, the unique smallest omitted subset is the singleton next prime, so the residual is 1+2^{a p_next} modulo the next power. The false-orientation valuations in the startup cases are exactly a+1 (a>1), p_1+1 (odd squarefree startup), or 3 (binary 2-startup), strictly below the next genuine prime in the stated branches. An independent exact implementation recovered the correct prime support for every 2<=n<350.

## Originality

**PASS.** PASS on a narrow completion boundary. The 2026-09-18 SCOPE record `single-value-padic-cyclotomic-prime-peeling--08dfc55c58fd` already proves the general higher-prefix p-adic residual mechanism and gives single-value binary peeling for nonsquarefree indices; `higher-local-cyclotomic-prime-extraction--01e648b0fd33` is earlier still for the higher-prime residual. The assigned record's genuinely new part is the binary squarefree startup/orientation analysis, using the least-prime extractor plus the special {p1}, {2}, or {2,3} fingerprints to close the remaining x=2, a=1 gap. That yields a complete all-n decoder from one Phi_n(2), which the earlier p-adic record explicitly did not cover.

## Scientific value

**PASS.** The higher-prefix mechanism is not new, but closing the squarefree binary orientation gap is a real structural completion: it turns the earlier conditional/nonsquarefree binary recursion into an all-index theorem at the natural base 2. The incremental value is modest but sufficient if the prior mechanism is explicitly excluded from the novelty claim.

## Originality boundary

The originality pass is limited to resolving the squarefree binary (a=1) startup/orientation problem and thereby obtaining a one-value Phi_n(2) decoder for every n. The general residual recursion and all nonsquarefree binary cases were already available in the 2026-09-18 SCOPE p-adic peeling record.

## Independent checks

- Re-derived C^epsilon=H_a(P) directly from the squarefree Möbius product after radical reduction.
- Checked that after removing H_a(Q_j), the singleton {p_{j+1}} is the unique smallest omitted subset exponent and therefore determines the exact 2-adic valuation a p_{j+1}.
- Recomputed each false-orientation startup valuation: a+1 for a>=2, p_1+1 for odd squarefree p_1, and 3 in the two even-startup branches.
- Implemented the stated decoder independently with exact Fraction arithmetic and SymPy cyclotomic polynomials; every n from 2 through 349 returned exactly sorted(factorint(n)).
- Compared with the 2026-09-18 single-value p-adic SCOPE theorem: its binary corollary stops at nonsquarefree n because the sign extraction fails when a=1, exactly the gap filled here.
- Checked Shunia arXiv:2609.18480: the indexed summary gives the radical valuation and squarefree least-prime extractor, while complete single-value peeling there is logarithmic/Archimedean rather than this rational 2-adic squarefree startup.

## Evidence and literature

- https://arxiv.org/abs/2609.18480 — Shunia, Cyclotomic Prime Extractors; source of the radical valuation and binary least-prime identity.
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/single-value-padic-cyclotomic-prime-peeling--08dfc55c58fd — Earlier SCOPE general p-adic recursion; already covers higher-prefix peeling and nonsquarefree binary indices.
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/higher-local-cyclotomic-prime-extraction--01e648b0fd33 — Earlier SCOPE higher-local residual mechanism; further narrows novelty of the assigned record to startup/orientation completion.
- https://arxiv.org/abs/1903.01962 — Pomerance–Rubinstein-Salzedo cyclotomic radical-reduction/background identities.

## Limitations

- The higher-prefix residual peeling is prior SCOPE work and must not be claimed as new by this record.
- The index n is given; this is not inversion of an unlabeled cyclotomic integer and not a competitive factoring algorithm.
- Exact rational/integer arithmetic is required, and direct fingerprints can have exponential subset complexity.
- The motivating cyclotomic preprint is very recent, leaving residual contemporaneous-priority risk.

## Repository identity

The assigned source-tree SHA `41c4d6f06d3d5d6a9acbc8c189c258ccfdcb3051` exactly matched the current tree at the audited path on `main`; GitHub was read only during this audit.
