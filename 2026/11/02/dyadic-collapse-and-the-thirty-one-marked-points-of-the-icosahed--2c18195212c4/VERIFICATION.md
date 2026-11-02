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

# Verification details

Run `python3 verify_icosahedral.py` using Python 3.9 or newer, without third-party packages. The verifier checks the 15-line orbit of Calvo’s displayed reflection matrices, then enumerates all 455 line-triple determinants in \(\mathbb Z[\varphi]\), groups all 105 pair intersections, computes the four-line characteristic-two fiber and every primitive marked section, and checks the smooth conic and its point-incidence table. Expected status: `ICOSAHEDRAL_15_MODULAR_COLLISIONS_AND_NEFDIVISOR_OK`.

The analytic assertion for infinitely many symbolic powers is proved by the explicit products and the nef divisor in RESULT.md. The verifier checks the finite algebraic premises, not the infinite nefness argument as a black box. Marked-section weights are distinct from intrinsic singular-scheme lengths. Source identity and older general Waldschmidt results are credited in RESULT.md; independent audit is not performed.
