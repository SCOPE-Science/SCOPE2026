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

# Reproducibility and proof boundaries

Extract `verify.py` and `EXPECTED.txt` without changing their bytes and execute `python3 verify.py`. Standard-library exact arithmetic is sufficient; no precomputed database, network connection, external solver, or runtime-dependent random seed is required. The expected stdout is reproduced in `EXPECTED.txt`. Separately execute `python3 verify_alt.py` and compare with `EXPECTED_ALT.txt` for a modular boundary-rank cross-check over four different primes.

The verifier constructs the nine points and all twelve lines from the coordinate equations, builds the face set, and independently checks all 1,260 Hasse incidences and the entire directed incidence graph for cycles. It checks the signed boundary of the displayed 36-term four-cycle, the primitive pairing with a four-cochain annihilating the twelve five-simplex boundaries, and four explicit integer boundary witnesses for the affine group generators. A generated permutation-group closure has order 432, and 432 direct signed Lefschetz counts satisfy the claimed rational character formula.

The finite computation is exhaustive for the named nine-point affine plane only. The derived homotopy equivalence uses the separately stated discrete-Morse and attaching-map arguments; the verifier alone should not be interpreted as an assertion about arbitrary finite planes. The rational module isomorphism uses equality of all finite-group character values. The separate modular rank checks are corroboration, not a proof that all integral torsion vanishes; the integral discrete-Morse argument handles that. No independent mathematical audit has been performed.
