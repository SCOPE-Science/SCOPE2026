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
The proof uses the integral Gysin exact sequence for the smooth principal divisor \(D\subset B\times\mathbb C^*\), the logarithmic residue/cup product formula, and the Smith normal form of the restriction vector \((m_1,\ldots,m_q)\). All three are stated and applied under their explicit hypotheses in `RESULT.md`. The finite exact-arithmetic checker `verify.py` was executed from the standalone packaged bytes and returned `VERIFY_OK`.

The code checks dehomogenized homogeneous example families for \(2\le a\le12\), root multiplicities, endpoint positivity, two-root Smith invariants with gcd one and two, and the Euler-characteristic consistency identity. It does not calculate the topology of arbitrary complements or independently prove a Gysin theorem; those are mathematical arguments in `RESULT.md`. The principal new step is an integral quotient of degree-two cohomology, not a claim that the cohomology groups have torsion. No independent audit was performed.
