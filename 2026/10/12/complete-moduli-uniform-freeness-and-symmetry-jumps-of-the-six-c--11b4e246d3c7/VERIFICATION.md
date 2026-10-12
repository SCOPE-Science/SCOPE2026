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

# Reproducibility and limits

Execute the included standalone file `verify.py` using Python 3. It has no third-party dependencies. Arithmetic is exact over integers and rational numbers. It checks the universal defining identities for the degree-eight polynomial with an indeterminate parameter, verifies the degree-two Jacobian syzygy, exhaustively enumerates the fifteen pairs of six fixed chord lines into four ordinary triple-line vertices and three diagonal double-line points, and verifies conic incidence at an admissible rational parameter. It checks the generic anharmonic orbit and harmonic orbit, and the exact values and invariance of the classical \(j\)-invariant at rational parameters.

Expected output:

`VERIFY_OK universal_syzygy=True singularities=4_ordinary_quadruples+3_nodes mdr_upper=2 generic_anharmonic_orbit=6 harmonic_orbit=3 j_harmonic=1728`

A finite enumeration of the six fixed chord lines does not by itself prove the universal normal form, and rational examples do not prove completeness over all complex parameters. The mathematical proof in `RESULT.md` separately establishes Bézout exhaustion, the projective normal form, the absence of degree-one syzygies, the free-curve criterion and the full complex stabilizer groups. This verification does not constitute independent audit or external certification.
