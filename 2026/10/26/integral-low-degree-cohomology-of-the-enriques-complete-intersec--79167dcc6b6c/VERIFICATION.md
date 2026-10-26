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

# Verification record
The theorem is proven symbolically in RESULT.md. Its checkable inputs are (i) the generic smooth invariant \((2m+1)\)-quadric complete intersection and fixed-locus avoidance, (ii) integral Lefschetz isomorphisms below complex dimension \(2m\), (iii) the multiplicative Cartan–Leray comparison, and (iv) the integral projective-bundle relation for the sum of trivial and sign lines over \(BC_2\). The statement is strictly truncated below middle cohomological degree.

The standalone sanity checker `verify.py` tests the enumerated monomial bases for \(2\le m\le12\), confirms their torsion ranks and the absence of odd-degree generators below \(2m\), and prints a success marker. It cannot certify Lefschetz, equivariant collapse, the global geometric construction, or novelty; those depend on the complete written proof and the cited primary materials. Independent audit was not performed.
