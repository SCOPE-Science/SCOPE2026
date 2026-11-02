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

# Computational verification and scope

Run `python3 verify_fence_spectrum.py` from the same directory. It requires Python 3's standard library and no downloads. The program directly enumerates all subsets for chain sizes 1 through 11; checks every gap-signature multiplicity, the factor count and dimension; enumerates all eligible partial maps for sizes 1 through 7; and checks all pairwise products of the integral Möbius basis for sizes 1 through 6. It returns `VERIFY_OK: matrix-block census and integral Mobius multiplication` on success. All assertions use exact integer arithmetic. The general result is justified by the proof's signature and Möbius arguments, not inferred from finite tests.

A finite check is neither an independent audit nor a proof of publication priority. No independent audit has been performed.
