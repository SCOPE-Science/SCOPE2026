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

# Verification methods and limits

The exact proof decomposes every nonzero rank-one polynomial matrix into monic content and two primitive nonzero vectors, modulo \(q-1\) unit rescalings. The monic polynomial factor series \((1-qz)^{-1}\) and primitive-vector series \((q^k-1)(1-qz)/(1-q^kz)\) establish the joint rational identity in all dimensions. Pole extraction yields the limiting geometric distribution for fixed \(q,m,n\).

Run `python3 verify.py` in this directory. The checker exhaustively enumerates \(2\times2\) polynomial matrices over \(\mathbb F_2\) and \(\mathbb F_3\) and \(2\times3\) polynomial matrices over \(\mathbb F_2\), with every entry of degree at most one. It tests rank one using polynomial minors, computes the gcd-degree by Euclidean division, and compares exact bivariate counts. The actual output is `checks.txt`; no external Python packages are required. These finite experiments are not a proof for all prime powers, dimensions, or degree cutoffs.

The original paper's published \(2\times2\) total with zero matrix counted is recovered by summing the height-shell coefficients and adding one. No independent scholarly audit or external validation was performed.
