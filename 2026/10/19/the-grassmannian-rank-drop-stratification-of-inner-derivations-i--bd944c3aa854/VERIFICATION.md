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

# Verification summary

The standalone script `verify_exterior_rank.py` constructs exterior products of all \(32\) basis monomials and calculates the ordinary commutator rank directly. It verifies \(400\) reproducibly seeded random odd elements over each of \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\); it also enumerates all \(3^{10}=59049\) degree-three coefficient vectors over \(\mathbb F_3\), obtaining frequencies \(1,2420,56628\) in ranks \(0,2,4\). The first \(100000\) degree-three coefficient vectors over \(\mathbb F_5\) are checked, explicitly not exhaustive. A successful run prints `VERIFY_OK`. The Python standard library suffices. 

The proof for every odd prime-power field uses graded exterior multiplication, an algebra automorphism for a nonzero linear part, the rank theorem for alternating bilinear forms, Gaussian-binomial counting, and elementary Grassmannian cone geometry. Numerical checks by themselves do not establish those general claims. Independent assessment remains unperformed.
