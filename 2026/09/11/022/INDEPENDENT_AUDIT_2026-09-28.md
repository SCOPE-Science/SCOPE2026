# Independent Audit — 2026-09-28

**Record:** `2026/09/11/022`  
**Title:** Low-quotient-degree exclusion for B(2,M,4) on a general genus-6 curve  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `3472c14f409b6cc8659bdae9ae9cc7be8426ab1f`  
**Disposition:** **REPAIRED**

## Independent checks

- Recomputed every Brill–Noether number used in the e=6 proof and checked the cohomology inequality.
- Compared the degree-6 extension locus with Newstead’s open-access genus-6 construction.
- Checked modern genus-6 literature confirming that a general genus-6 curve carries minimal degree-4 pencils.

## Three-axis assessment

- **Correctness — PASS**: The core exclusion is correct after one factual repair. Stability of a rank-2 degree-10 bundle forces every line quotient to have degree at least 6. For e=6, the kernel N has degree 4 and h0(E)≤h0(N)+h0(L). On a general genus-6 curve, W^3_6 and W^2_4 are empty, while the only relevant incidence loci lie in W^0_4×W^2_6 and W^1_4×W^1_6, each of dimension 4; their tensor-product images therefore cannot dominate Pic^10, which has dimension 6. Thus a general determinant avoids them. The filed definition incorrectly called a general genus-6 curve gonality 5; a general genus-6 curve is 4-gonal (indeed it has five minimal degree-4 pencils). Changing that phrase to gonality 4 makes the contextual definition consistent with the proof, which itself already uses W^1_4.
- **Originality — LIMITED**: The exclusion is a short consequence of standard Brill–Noether dimensions plus stability. Newstead explicitly constructs degree-6-quotient families in B(2,10,4) and notes that the varying L form a 4-dimensional family, which is fully compatible with the present non-dominance argument for a general fixed determinant. I did not locate the exact fixed-general-determinant e≤6 statement, but the method is elementary rather than a new structural theorem.
- **Scientific Value — PASS**: The corrected statement usefully isolates where any counterexample to general-fixed-determinant emptiness must live: quotient degree at least 7, precisely where the naive incidence dimension can reach Pic^10. This is a meaningful reduction for the open locus question, although it is a modest pruning lemma.

## Findings

- Current main tree exactly equals the assigned source-tree SHA.
- The filed phrase “gonality 5” is false for a general genus-6 curve and conflicts with the same proof’s use of W^1_4; it is repaired to “gonality 4”.
- The stability floor e≥6 and both degree-6 incidence dimensions (4<6) check exactly.
- Newstead’s degree-6 quotient construction varies in dimension 4 and therefore does not contradict exclusion for general M.

## Sources compared

- Repository record 022 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/022/RESULT.md — Contains the low-degree quotient proof and the gonality typo repaired by this audit.
- P. E. Newstead, Some examples of rank-2 Brill–Noether loci: https://doi.org/10.1007/s13163-017-0241-6 — Remark 4.6 constructs genus-6 degree-10 rank-2 bundles from a degree-4 line bundle and a generated degree-6 quotient; the quotient family has dimension 4.
- Hoff–Knutsen, Brill–Noether general K3 surfaces with the maximal number of elliptic pencils of minimal degree: https://doi.org/10.1007/s10711-020-00565-z — States that a general genus-6 curve has five pencils of minimal degree 4, confirming gonality 4 rather than 5.

## Limitations

- Only stable bundles on a general curve with general determinant are covered.
- Quotient degrees e≥7 are untouched; at e=7 the simple incidence dimension count can reach dimension 6.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
