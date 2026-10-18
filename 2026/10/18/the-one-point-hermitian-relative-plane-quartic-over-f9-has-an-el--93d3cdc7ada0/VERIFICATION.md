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

# Computational verification

Run `python3 verify_curve.py` in the same directory. The verifier has no non-standard package dependencies, checks irreducibility of the monic polynomials used to construct finite fields, and enumerates projective points on the quartic in two logically separate ways (fourth-power frequency versus direct affine evaluation). The expected counts in the three extensions are \(1,109,892\); the infinity contributions are \(0,4,0\). The code reconstructs the complete genus-three Weil numerator by Newton's identities and the functional equation, factors it by integer multiplication, and independently counts rational points on the displayed elliptic curve. The actual execution completed with `VERIFICATION_OK`.

Mathematical inputs not reducible to testing are smooth plane-curve genus, Weil functional equation, and Tate's finite-field isogeny theorem. These are stated in `RESULT.md`. The code does not construct an explicit isogeny map or verify any compatible principal polarization.
