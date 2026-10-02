# Independent audit — 2026-09-30

**Record:** `2026/09/08/034`  
**Audited source tree:** `20246e9ab65d046eb6b86dbfab9a7031e2a0721d`

## Final claim assessed

Kronecker-square fingerprints separate S_6-S_8 irreps up to sign

## Correctness — PASS

A fresh Murnaghan-Nakayama implementation, with independently generated rim hooks and exact class-size arithmetic, reproduces the S6, S7, and S8 character tables and passes full orthogonality. Exact Kronecker-square vectors then form exactly 6, 8, and 12 groups, and those groups coincide with partition-conjugation classes. The stated 109 cross-class separations follow from distinct vectors; the committed verifier also checks lexicographic firstness coefficient by coefficient.

## Originality — PASS

The closest inspected primary literature classifies multiplicity-free Kronecker products and studies constituents of important tensor squares, but it does not assert that equality of complete square-decomposition vectors determines the factor up to sign twist for S6 through S8, nor does it tabulate the 109 first separating coordinates. Resultary searches return this finite fingerprint result as the exact match and later related square-splitting work as a different invariant. No inspected theorem implies the finite separation statement.

The comparison explicitly checked equivalent formulations, broader coverage, exact database/table matches, and whether prior results logically imply the claim. An unsuccessful search was not treated as proof of novelty.

## Scientific value — PASS

Factor recovery from a tensor-square fingerprint is a natural representation-theoretic identification problem. The complete consecutive S6-S8 classification and minimal separating constituents provide exact benchmark data for character-recognition and Kronecker algorithms. The result is narrow but is a natural complete classification, not an arbitrary slice or a mere recomputation of a published table.

## Source inspections

- **Bessenrodt and Bowman — Multiplicity-free Kronecker products of characters of the symmetric groups** — Full-text PDF: abstract, Theorem 1.1, square-product discussion, and Proposition 3.3 context. Classifies multiplicity-free products and some square decompositions; it does not classify collisions of complete square vectors across irreducible factors. https://arxiv.org/abs/1609.03596
- **Pak, Panova, Vallejo — Kronecker products, characters, partitions, and the tensor square conjectures** — Abstract and stated main result on constituents of staircase tensor squares. Addresses positivity/containment in selected tensor squares, not uniqueness of the factor from its full square decomposition. https://arxiv.org/abs/1304.0738
- **Resultary semantic search for Kronecker-square fingerprints** — Top ranked result set and related square-splitting records. The exact S6-S8 fingerprint statement is this record; nearby records study symmetric/alternating splitting or other Kronecker statistics. https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE034

## Residual risks

- The theorem is intentionally finite: it provides no evidence that the same separation continues for n at least 9.
- The originality search cannot rule out unpublished or non-indexed character-table computations, although no covering published theorem or table was found.

## Disposition

**PASS.** Correctness, originality, and scientific value each pass for the final claim stated above.
