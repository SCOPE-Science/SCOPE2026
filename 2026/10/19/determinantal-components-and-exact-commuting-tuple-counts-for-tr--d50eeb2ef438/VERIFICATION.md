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

The companion `verify.py` uses only the Python standard library. It computes the truncated Witt commutator coefficients directly and enumerates all ordered commuting pairs or triples for the following admissible \((n,s,q)\): \((2,2,5)\), \((2,3,5)\), \((3,2,5)\), and \((3,3,5)\). The verified totals are respectively \(145\), \(745\), \(1225\), and \(18725\). In the small enumerations it also checks equality, point by point, between the commutation equations and the union of rank-one determinantal conditions.

An independent modular Gaussian-elimination calculation checks the adjoint-rank distribution for \((n,q)=(2,5),(3,5),(4,7),(5,7)\). All cases returned `VERIFY_OK`. The source code was extracted again from the saved row and replayed successfully against those cases.

The algebraic proof, not the checks, establishes all characteristics and all tuple lengths within the stated domain. The tests do not establish reducedness of the unreduced commuting scheme, nor do they independently certify geometric irreducibility. There is no independent audit or external mathematical certification.
