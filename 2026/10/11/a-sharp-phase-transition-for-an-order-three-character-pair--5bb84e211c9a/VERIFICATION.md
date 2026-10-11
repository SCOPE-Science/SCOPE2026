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
The theorem is proved analytically in `RESULT.md`.

The reduction to three samples is exact because an order-three character pushes normalized Haar measure to the uniform measure on the cube roots of unity. The coefficient-balance maximization uses convexity, and the phase maximization uses an exact cubic with fixed first two elementary symmetric functions. Its derivative is a second divided difference of \(t^{s-1}\), so its sign is controlled by \((s-1)(s-2)t^{s-3}\).

The accompanying `verify.py` performs deterministic corroborative checks of the elementary symmetric identities, the two endpoint moment formulas, phase-independence at \(p=4\), and representative coefficient/phase grids for exponents below and above \(4\). These finite checks are not a proof of the all-\(p\) statement and are not used as one.

The packaged checker was replayed successfully with:

`VERIFY_OK grid_checks=263169 max_excess=8.882e-16 symerr=3.109e-15`
