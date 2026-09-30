# Independent Audit — 2026/09/17/rank-one-shear-cppm-obstruction-p-sums--94018947361a

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `49c3f7e737ba6304f61183e4674620d6d5d87bef`
- Disposition: **PASSED**

## Correctness

**PASS** — The rank-one shear proof is correct for every 1<=p<=infinity. Since N_c^2=0, T_c^{-1}=I+N_c. Comparing norms with the positive scalar shear gives ||T_c^{-1}||<=kappa_p(c), and a sequence y_n in S_Y with f(y_n)->1 realizes the reverse inequality. Any actual norm-attaining vector would force |f(y)|=||y|| because every maximizing scalar pair has a nonzero Y-coordinate, contradicting non-attainment of f; hence T_c does not attain its minimum modulus. For any compact C on the infinite-dimensional space X, C is not bounded below, so a unit sequence with Cu_n->0 gives m(I+C)<=1. Writing T_c+K=I+(K-N_c) yields the universal upper envelope 1, attained by K=N_c. The endpoint formulas and divergence of the defect ratio follow immediately.

## Originality

**PASS** — Han's direct-sum obstruction uses unequal finite exponents p<q, while Raposo-Ribeiro prove the scalar-summand p=infinity case K plus_infinity Y. The submitted theorem fills the diagonal finite-p regime, permits an arbitrary nonzero complementary summand Z, and computes the exact compact-perturbation envelope and an unbounded defect family. Targeted searches found no prior all-p diagonal formulation.

## Scientific value

**PASS** — The result gives a clean structural obstruction covering a broad and natural class of decomposable non-reflexive spaces and quantifies CPPm failure exactly. Although the proof uses classical James-theorem and rank-one-shear ingredients, the all-p statement clarifies the gap between the recent unequal-exponent and infinity-sum results and supplies reusable counterexamples.

## Sources

- Weak minimizing property on pairs of classical Banach spaces (Manwook Han): https://arxiv.org/abs/2601.17316 — Introduces CPPm and contains finite-p direct-sum obstructions with distinct exponents, not the diagonal all-p theorem.
- Weak Minimizing Property and the Compact Perturbation Property for the Minimum Modulus (Anselmo Raposo Jr.; Geivison Ribeiro): https://arxiv.org/abs/2605.01397 — Theorem-level source for failure of CPPm on X=K plus_infinity Y when Y is non-reflexive; this is the p=infinity scalar-summand precursor.
- Characterizations of reflexivity (R. C. James): https://doi.org/10.4064/sm-23-3-205-216 — Classical norm-attainment characterization used to choose a norm-one non-norm-attaining functional on non-reflexive Y.

## Limitations

- The theorem requires the displayed isometric l_p direct-sum decomposition and does not characterize CPPm under arbitrary renormings or non-complemented embeddings.
- The mechanism is elementary and its originality lies in the scope and exact envelope rather than a new operator-theoretic technique.

GitHub was read only as evidence; no repository mutation was performed. Open-access/preprint sources were checked first. Oxford Download was not needed for this record.
