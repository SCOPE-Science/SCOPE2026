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
The checker enumerates every degree-\(d\) monomial for
\[
2\le n\le8,
\qquad
2\le d\le10.
\]

For each format it chooses
\[
B=d+1
\]
and verifies that the weights
\[
\sum_i\alpha_i B^i
\]
are pairwise distinct over all exponent vectors
\[
\alpha_i\ge0,
\qquad
\sum_i\alpha_i=d.
\]

It classifies a monomial projective hypersurface as smooth exactly in the unique case
\[
(n,d)=(2,2)
\]
with exponent vector
\[
(1,1).
\]

The checker therefore confirms the fixed-point counts
\[
\#(\mathcal U_{n,d})^{\mathbb C^*}=0
\]
outside the exceptional pair and
\[
\#(\mathcal U_{2,2})^{\mathbb C^*}=1.
\]

Finite checks are regression evidence only. The infinite theorem follows from base-\(B\) uniqueness, the symbolic monomial smoothness classification, and Euler localization.
