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

# Verification instructions
Run `python3 verify.py` using Python 3 and its standard library. It reconstructs multiplication in the square-zero unital local algebra and checks the weight-zero Rota–Baxter identity on basis pairs, independently of the proof reduction. It enumerates all square-zero endomorphisms and compatible vector parameters for \((n,q)=(2,2),(2,3),(2,4),(3,2)\), checks rank-stratified counts, and enumerates conjugacy orbits under all invertible matrices for \((2,2),(2,3),(3,2)\). Expected terminal marker: `VERIFY_OK`. These checks are finite and do not establish the theorem for unbounded dimension or arbitrary fields. The full proof is in RESULT.md.
