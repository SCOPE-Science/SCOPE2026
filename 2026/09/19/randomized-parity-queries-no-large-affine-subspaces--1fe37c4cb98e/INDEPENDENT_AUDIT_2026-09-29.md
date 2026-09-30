# Independent Audit — 2026/09/19/randomized-parity-queries-no-large-affine-subspaces--1fe37c4cb98e

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `e8cb6b3cc4ebdab8638ff9bc7fd7cb75f0cddb47`
- Disposition: **PASSED**

## Correctness

**PASS** — The XOR quotient and parity-query simulation are correct. Wang-Wu's total communication function depends on the complete inputs only through z=x xor y and the table entries c_j=u_j xor v_j, so it is exactly F(a,b)=phi(a xor b). Their address stage samples q=ceil(18 ln(6k)) singleton coordinates in each of k blocks, which is directly a kq-query parity algorithm. Their certificate test uses four linear queries over F_{2^{4k}}; after fixing an F_2 basis, the 4k coordinates of each answer are ordinary binary linear forms, so 16k parity queries recover the same information and preserve the protocol's error bound. For a monochromatic affine subspace C=a+H of codimension r, H times (a+H) is a monochromatic rectangle for F of density 2^{-2r}. Wang-Wu's rectangle bound 2^{-m/(8k)} therefore forces r>=m/(16k). With m=2^k and their polynomial-size input parameterization this is N^{Omega(1)}. Finally every deterministic parity-decision-tree leaf is an affine subspace of codimension at most the depth, giving the same deterministic lower bound.

## Originality

**PASS** — Gavinsky explicitly posed whether efficient randomized parity-query protocols force a large monochromatic affine subspace. Wang-Wu's September 2026 result separates randomized communication from monochromatic rectangles but does not formulate the one-variable XOR quotient or the resulting answer to Gavinsky's question. The deduction uses special features of their protocol—coordinate sampling and fully linear finite-field queries—and is not a generic XOR simulation theorem. Targeted searches found no prior statement of this parity-query consequence. Because it is a short consequence of a very recent source, near-simultaneous priority remains a material risk but no covering result was located.

## Scientific value

**PASS** — The result gives a quantitative negative answer to an explicit structural question: polylogarithmic randomized parity-query complexity can coexist with polynomial codimension for every monochromatic affine subspace and hence polynomial deterministic parity complexity. It also identifies a concrete route by which communication lower bounds can transfer back to parity queries when the protocol itself respects XOR-linear structure.

## Sources

- **Efficient Randomized Communication Without Large Monochromatic Rectangles** — Haoyu Wang; Pei Wu. https://eccc.weizmann.ac.il/report/2026/190/ — Primary 2026 source. Definition 3.8 has the XOR dependence, Theorem 3.7 gives four F_{2^{4k}}-linear queries, Theorem 4.1 gives the O(k log k) randomized protocol, and Theorem 5.1 gives the rectangle-density bound.
- **Unambiguous Parity-Query Complexity** — Dmytro Gavinsky. https://doi.org/10.1002/rsa.70010 — Poses the large-monochromatic-affine-subspace question for efficient randomized parity-query protocols.
- **Structure of Protocols for XOR Functions** — Hamed Hatami; Kaave Hosseini; Shachar Lovett. https://doi.org/10.1137/17M1136869 — Deterministic communication/parity-query structural background; does not provide the general randomized simulation that the record carefully avoids claiming.

## Limitations

- The parity-query simulation uses the special linear/XOR form of Wang-Wu's protocol and is not a general randomized communication-to-parity-query simulation for XOR functions.
- The polynomial affine-codimension exponent is inherited from Wang-Wu's parameters and is not optimized.
- The corollary is concise and based on a very recent source, so concurrent or folklore priority is a material residual risk.

## Independent checks

```json
{
  "wang_wu_definition_3_8_checked": true,
  "wang_wu_theorem_3_7_checked": true,
  "wang_wu_theorem_4_1_checked": true,
  "wang_wu_theorem_5_1_checked": true,
  "source_pdf_screenshots_checked": true,
  "xor_rectangle_lift_checked": true,
  "binary_query_count": "k*ceil(18 ln(6k))+16k",
  "affine_codimension_lower_bound": "m/(16k)",
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive source remained inaccessible, so Oxford Download was not required.
