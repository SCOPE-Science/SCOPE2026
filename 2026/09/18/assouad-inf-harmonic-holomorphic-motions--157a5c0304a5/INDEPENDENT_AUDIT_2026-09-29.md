# Independent audit — Assouad dimension is inf-harmonic under holomorphic motions

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/assouad-inf-harmonic-holomorphic-motions--157a5c0304a5`
**Audited tree:** `e561c327449c37ddf90eda92b2066fa51b0d2b0f`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The proof is correct. The new variable-radius packing criterion for full Assouad dimension follows directly from the equal-radius characterization: lower exponents are witnessed by equal-radius packings, while for t>dim_A an intermediate exponent s and dyadic radius classes give a summable O(2^{-j(t-s)}) bound. This exactly removes the extra radius-versus-ambient scale restriction that Menssen–Younsi need for quasi-Assouad dimension. Their diameter-ratio/implicit-function machinery then transfers divergent normalized sums through the holomorphic motion, and quasiconformal inscribed disks give a valid target packing. The touching-majorant argument yields reciprocal Assouad dimension as an infimum of positive harmonic functions. The symmetric version follows by the same source machinery.

### Independent checks

- Re-proved the variable-radius Assouad criterion from the standard equal-radius definition using dyadic radius bins and an intermediate exponent s between dim_A and t.
- Checked that image inscribed disks remain pairwise disjoint, are centered on E_lambda, lie in a single controlled ambient ball, and require only radius<=ambient radius for full Assouad dimension.
- Checked the implicit-exponent monotonicity and compactness step: 1/s_n has a fixed finite basepoint value, preventing locally uniform divergence to infinity, and any b below the reciprocal limit forces divergent target b-sums.
- Checked that taking the infimum over the touching inf-harmonic majorants is itself inf-harmonic by flattening the union of their positive-harmonic representing families.
- After ordinary arXiv/OA full-text retrieval failed, independently read all 23 pages of arXiv:2609.19522 through authorized institutional retrieval; Question 1.11, the variable-radius quasi-Assouad theorem, and the exact scale-transfer obstruction were confirmed.

## Originality

PASS. Menssen–Younsi arXiv:2609.19522v1 explicitly states that they were unable to prove the Assouad analogue and asks it as Question 1.11. The full source was independently inspected, including Theorem 3.1 and Lemma 4.2: its proof needs the quasi-Assouad radius restriction r<=R^{1+theta}, whereas the submitted variable-radius Assouad lemma removes precisely that step. Searches through 2026-09-29 still locate the Assouad statement as an open problem and no external solution.

### Literature checked

- https://arxiv.org/abs/2609.19522 — Menssen–Younsi, Holomorphic motions, Assouad dimension and quasiconformal mappings; v1 explicitly asks whether the quasi-Assouad inf-harmonic theorem extends to full Assouad dimension.
- https://www.emergentmind.com/open-problems/assouad-dimension-inf-harmonicity-under-holomorphic-motions — Current indexed open-problem page, crawled 2026-09-28, still records the full-Assouad inf-harmonicity statement as unresolved in the source literature.
- https://arxiv.org/abs/2005.03763 — Fraser, Assouad Dimension and Fractal Geometry; standard equal-radius Assouad packing background.

## Scientific value

This directly resolves an explicit current open question and upgrades known two-point quasiconformal Assouad distortion to full inf-harmonic parameter dependence. The symmetric strengthening also transports the result into the Smirnov holomorphic-motion framework. The core new observation is simple but structurally decisive.

## Limitations

- The theorem concerns bounded planar sets and sphere holomorphic motions; no Hausdorff/upper-Minkowski analogue or higher-dimensional extension is proved.
- The variable-radius packing characterization is elementary/folklore-level; the originality is its use to close Question 1.11, not the standalone lemma in isolation.
- The source preprint is extremely recent, so unindexed contemporaneous solutions remain a residual priority risk.
- The quasicircle 1+k^2 numerical consequence is not needed for the originality verdict.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
