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

The standalone file `verify.py` uses exact integer bitmasks and standard-library Python 3.10+. Run `python3 verify.py` in the directory containing the code; the expected output is in `verification_output.txt`.

It independently compares closed-neighborhood traces and domination/symmetric-difference hitting constraints on every size-eight and size-nine subset; verifies equality with the geometrical optimizer families; constructs every exchange edge and component; checks the cone description and four explicit Pappus incidence models; and verifies each affine orbit and component eccentricity.

The proof is finite and exhaustive at order three only. A self-review does not establish independent audit or external certification.
