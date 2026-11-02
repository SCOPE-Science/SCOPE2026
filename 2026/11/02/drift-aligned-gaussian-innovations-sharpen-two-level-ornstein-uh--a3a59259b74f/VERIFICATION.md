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
# Reproduction and limits

Execute `python verify.py` in an environment with Python 3 and its standard library. The script was run successfully, reporting `VERIFY_OK 624 exact rational and numerical identities, including limiting rates`. The exact rational cases include the strict one-block witness and 127 finite geometric-sum identities; numerical checks compare the alternative variance representations and their limits. The proof of all dimensions of the claim is the algebra in RESULT.md; finite tests are not substituted for infinite proofs.

The established optimality is within independent-block, correct-marginal couplings only. An independent mathematical audit has not been performed.
