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

The proof counts prescribed one- and two-point incidences for uniform invertible matrices. The pair count is conditioned on linear independence before and after coordinatewise squaring; in odd characteristic, projective square collisions are classified by the support size.

The standalone Python 3 checker computes idempotent counts for every invertible structure matrix over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_9\) in the explicitly specified dimensions. It evaluates the defining equations directly and checks rational means and factorial moments against the formula.

The checker completed every case and printed `VERIFY_OK`. All finite-field extension arithmetic is implemented locally using the irreducible polynomials \(t^2+t+1\) over \(\mathbb F_2\) and \(t^2+1\) over \(\mathbb F_3\). No claim of independent mathematical audit is made.

Limitation: exhaustive enumeration covers only the listed finite cases; the all-prime-powers theorem is established by the symbolic counting proof.
