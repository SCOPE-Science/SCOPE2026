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
# Verification

To replay exact symbolic checks, run `python verify_genus3_fibers.py` with Python 3 and SymPy installed. The checks verify the biquadratic discriminant and its factorization, square identities at the cubic roots of unity, nonrepeated binary quartics in the five four-line cases, and the Euler-characteristic identity. The polynomial identities are for symbolic parameters in characteristic zero; the proof in `RESULT.md` establishes completeness of the singular-fiber classification and explains the local analytic singularities. Neither finite specialization nor solver output is substituted for the all-parameter argument. Independent scientific audit has not been performed.
