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

# Verification scope

Run `python3 verify.py` beside this file. The program contains exact characteristic-three linear algebra: it enumerates the 18 coefficient specializations over the prime field, computes Laurent Cartier images, and checks the expected ranks and stable rank. It also verifies the only legal genus-five ramification partitions and the nonnegative valuations for five proposed regular forms. Successful output is `VERIFY_OK: ...`.

The universal theorem is established by the symbolic valuations and Cartier identities in RESULT.md; the finite checker is a reproducibility check and is not treated as proof for every algebraically closed field. The dimension statements use Pries–Zhu's theorem and the finite-fiber argument. No external audit was performed.
