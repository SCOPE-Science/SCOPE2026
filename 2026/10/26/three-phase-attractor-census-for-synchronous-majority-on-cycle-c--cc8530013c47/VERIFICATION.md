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

# Verification and reproducibility

Run `python3 VERIFY.py` (standard library only) in a folder containing the supplied Python script. The accompanying `VERIFY.out` gives the passing output of that execution. The checker uses independent direct majority updates on the complete labelled graph rather than only the phase-reduced transfer construction.

The exact integer checks reconstruct the characteristic polynomial of the explicitly defined 16-state matrix via Newton's identities; they verify that `trace(M^n)` equals direct uniform-leaf pair counts for n=3,...,9. Exhaustive iteration of all binary labelled states checks fixed and two-periodic populations for n=3,...,9 at one leaf, n=3,...,6 at two leaves, n=3,...,4 at three leaves, and n=3 at four leaves. A total of 751424 labelled initial configurations was checked, including the predicted one-step periodic entry whenever at least three private leaves occur.

Limits: a finite case census is not a proof for unrestricted n. The all-size proof is symbolic and given in `RESULT.md`. There is no formal proof-assistant certification or independent external audit. Historical completeness is qualified by the listed source access limits.
