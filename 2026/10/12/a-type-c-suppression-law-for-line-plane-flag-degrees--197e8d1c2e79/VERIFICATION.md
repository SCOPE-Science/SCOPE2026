---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The checker independently reconstructs the complementary root products for the ordinary and symplectic line-plane flag varieties for
\[
2\le n\le100.
\]
It verifies the closed formulas
\[
\deg A_n=\frac{2^{2n-2}(4n-3)!}{(2n-1)!(2n-2)!}
\]
and
\[
\deg C_n=\frac{3\,2^{2n-3}(4n-4)!}{(2n-1)!(2n-3)!},
\]
together with the Weyl-coset Euler counts and both cross-type ratios.

It also checks the exact normalized suppression factor
\[
\frac{3(2n-1)}{2(4n-3)}
\]
and its strict decrease for every tested consecutive pair.

Finite computation is regression evidence only. The infinite theorem is the symbolic root-product calculation in `RESULT.md`.
