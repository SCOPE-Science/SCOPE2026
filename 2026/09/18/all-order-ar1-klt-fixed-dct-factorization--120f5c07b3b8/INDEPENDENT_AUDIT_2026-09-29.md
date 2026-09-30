# Independent Audit — 2026/09/18/all-order-ar1-klt-fixed-dct-factorization--120f5c07b3b8

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `9ae97cd2fda0e1ac5f2a8d28934c9974ac6df337`
- Disposition: **PASSED**

## Correctness

**PASS** — The all-order identity is exact. Writing L_N=T_N(1), the decomposition T_N(ρ)=ρL_N+(1-ρ)^2I+ρ(1-ρ)(e_0e_0^T+e_{N-1}e_{N-1}^T) follows entrywise. DCT-II diagonalizes L_N and maps the two endpoint vectors to q and Sq, yielding the displayed diagonal-plus-two-rank-one formula and exact parity decoupling. I independently reconstructed this identity for N=2,3,4,5,7,9,12 and ρ∈{0.13,0.37,0.71,0.94}; the maximum entrywise residual was below 7.4×10^-15. Within each parity class the positive rank-one secular equation and strict pole interlacing are standard. Because the tridiagonal AR(1) inverse is an irreducible centrosymmetric Jacobi matrix, Sturm ordering alternates symmetric and antisymmetric eigenvectors, justifying the final interleaving. The submitted verifier also confirms the odd DCT-VI/DCT-VIII split to double-precision roundoff.

## Originality

**PASS** — Reznik's fixed-core companion theorem is explicitly restricted to even N and uses half-size DCT-II/DCT-IV cores, while his earlier all-order paper treats odd N through two residual-KLT copies plus an arrowhead stage and recursion. The present record gives an explicit nonrecursive odd-order DCT-VI/DCT-VIII rank-one correction and a simpler full-order DCT-II parity identity valid for every N. Targeted searches did not locate that all-order fixed-DCT statement in prior AR(1) KLT work.

## Scientific value

**PASS** — The improvement is structural rather than asymptotic—the earlier recursive method is already O(N log N)—but the result puts every order into the same fixed-transform plus secular-correction architecture. That simplifies implementation, analysis, and comparison with fast Cauchy/FMM eigensolver machinery, and closes the odd-order gap left by the companion theorem.

## Sources

- Exact fast factorizations of the AR(1) Karhunen-Loeve transform (Yuriy A. Reznik): https://arxiv.org/abs/2609.20221 — Fixed-core DCT-II/DCT-IV rank-one factorization stated for even order N.
- Direct Factorization of the Karhunen-Loève Transform of AR(1) Sources (Yuriy A. Reznik): https://arxiv.org/abs/2608.06522 — All-order recursive factorization; odd N uses residual KLT blocks and an arrowhead stage.
- Relationship between DCT-II, DCT-VI, and DST-VII transforms (Yuriy A. Reznik): https://doi.org/10.1109/ICASSP.2013.6638744 — Classical odd DCT parity relation, but not the rho-dependent exact AR(1) rank-one correction theorem.

## Limitations

- The result is for real stationary AR(1) covariance with 0<ρ<1 and does not add a floating-point backward-stability theorem.
- Fast application of the dense correction factors remains accuracy-controlled rather than exact arithmetic O(N log N).
- The originality assessment carries residual simultaneous-work risk because the relevant Reznik preprints are very recent.

## Independent checks

```json
{
  "implementation": "fresh NumPy reconstruction independent of the submitted verifier",
  "orders": [
    2,
    3,
    4,
    5,
    7,
    9,
    12
  ],
  "rho_values": [
    0.13,
    0.37,
    0.71,
    0.94
  ],
  "max_full_dct_identity_residual": 7.4e-15,
  "submitted_odd_split_residual": 2.304e-15,
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; Oxford Download was not needed in this record.
