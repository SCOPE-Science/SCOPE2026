# Independent Audit — 2026/09/18/full-morita-corners-join-meet-support-tau-tilting--24a5f318e9fa

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `e2ff53fcfb34fd9b36bcbfb9e0f0ed72db3b8821`
- Disposition: **PASSED**

## Correctness

**PASS** — In a strict Morita context both diagonal idempotents are full, so restriction to either corner is an exact Morita equivalence. Under R_e, the B-corner condition transports by Theta and the prescribed componentwise class is exactly U intersect V. Direct induction transports to X plus Theta(Y); whenever that module is support tau-tilting its factor class is a torsion class containing U and V and is therefore their join. The two bilateral cross conditions are precisely V subset U and U subset V, hence U=V. The functorial-finiteness and equality criteria then follow from equivalence invariance and the support-tau-tilting/functorially-finite-torsion correspondence. For M_2(k^n), the reduction to subset union versus intersection gives all 4^n direct inductions and exactly 2^n compatible diagonal pairs.

## Originality

**PASS** — Zhang's September 2026 paper supplies the bilateral construction, sufficient cross conditions and matrix counterexamples outside the radical-valued converse. Classical Morita theory and Kashu's torsion-lattice correspondences supply the categorical ingredients. Targeted searches did not locate the submitted general full-corner meet-versus-join theorem, the reformulation of both cross conditions as equality of transported torsion classes, or the 4^n versus 2^n family. The novelty is conceptual synthesis rather than a new Morita equivalence theorem, but the exact support-tau-tilting statement appears distinct.

## Scientific value

**PASS** — The theorem gives a complete description of the strict/full-corner extreme complementary to Zhang's radical-valued regime. It explains why prescribed componentwise gluing and direct induction can diverge, gives an exact functorial-finiteness criterion, and quantifies the mismatch exponentially in the semisimple family. This is a useful structural guide for applying or extending the recent bilateral construction.

## Sources

- Support τ-tilting modules over Morita context algebras: A bilateral approximation approach (Yingying Zhang): https://arxiv.org/abs/2609.18746 — Motivating bilateral construction and radical-valued necessity theorem; its indexed abstract does not state the full-corner join/meet classification.
- On equivalence of some subcategories of modules in Morita contexts (A. I. Kashu): https://admjournal.luguniv.edu.ua/index.php/adm/article/view/963 — Classical torsion-lattice correspondences in Morita contexts; supplies background ingredients rather than the support-tau-tilting theorem.
- τ-tilting theory (Takahide Adachi; Osamu Iyama; Idun Reiten): https://arxiv.org/abs/1210.1036 — Support-tau-tilting / functorially finite torsion-class correspondence used in the proof.

## Limitations

- The proof is deliberately an application of classical Morita equivalence plus tau-tilting torsion theory; originality is in the strict-context synthesis.
- Older Morita/torsion-theory literature is broad, so an equivalent lattice observation under older terminology remains a residual originality risk.
- The join statement is conditional on the directly induced module being support tau-tilting, exactly as stated.

GitHub was read only as evidence; no repository mutation was performed. The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. Open-access/preprint material was checked before other sources; no Oxford Download was needed for this record.
