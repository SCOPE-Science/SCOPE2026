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

The included `verify.py` uses exact symbolic matrix algebra (SymPy) and exact-rational finite-block enumeration. Run it with `python3 verify.py` from the directory containing the script after installing SymPy. During preparation, the command printed:

`VERIFY_OK: polynomial_identities=11, rational_block_enumerations=18, resonance=2`

The program checks the complete two-by-two Gram identities for paired drift/kick products, the affine coupling multiplier, the exact transition-factor roots, the resonant square identities, the independent-coupling identity and 18 exact enumerated block expectations at six settings. It checks what the proof claims, rather than attempting to infer universal identities from finite samples. The symbolic identities are exact over the polynomial ring and the proof gives the required infinite-horizon induction. No independent audit has been performed. The program does not certify publication priority, nonlinear extensions or almost-sure energy growth.
