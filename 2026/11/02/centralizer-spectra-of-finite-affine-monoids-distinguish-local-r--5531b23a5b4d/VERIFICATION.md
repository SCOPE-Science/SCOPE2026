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

# Verification of affine centralizer spectra

The full proof is in `RESULT.md`. The executable `verify.py` is standard-library Python. Running `python verify.py` enumerates all affine maps \(f_{a,b}\), directly computes composition in both orders against all other affine maps, and compares the resulting centralizer count with the size of the generated ideal \((a-1,b)\). It separately checks the spectrum multiplicities and the exact rational commuting probabilities. Tests do not substitute for unrestricted proofs.

Actual successful tests were run for truncated-polynomial chain rings over prime fields with \((q,k)=(2,1),(2,2),(2,3),(2,4),(3,2),(3,3)\); square-zero extensions with \((q,d)=(2,2),(2,3),(3,2)\); and integer residue rings \(\mathbb Z/p^k\mathbb Z\) with \((p,k)=(2,2),(2,3),(3,2)\). All twelve cases printed `CHECK_OK`, followed by `VERIFY_OK`. Particularly, two rings of order eight have respective spectra \((48,12,3,1)\) and \((48,6,9,1)\) at centralizer sizes \((8,16,32,64)\), with commuting probabilities \(23/128\) and \(13/64\).

The code uses explicit tuple arithmetic for truncated polynomial and square-zero rings, integer modular arithmetic for mixed-characteristic chain rings, complete finite enumeration of commuting pairs, independent additive ideal generation, and exact rational arithmetic. Its tests cover prime residue fields, not all extension fields; the proof uses only finite-field vector-space counting and therefore does not require an exhaustive test over every prime power.
