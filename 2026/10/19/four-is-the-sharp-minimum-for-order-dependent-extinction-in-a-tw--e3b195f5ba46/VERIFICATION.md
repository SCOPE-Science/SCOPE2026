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

The independent audit has not been performed. The proof's universal component uses diagonal symmetrization of any irreducible two-stage Metzler generator and spectral invariance under cyclic reordering and transpose reversal of one to three symmetric factors.

The included `verify.py` uses Python standard-library exact fractions. It constructs \(E_0\) from an exponential identity at \(\tau=\log 2\), replays both four-pulse monodromy products, and asserts the stated rational traces, determinants and signs of \(\det(I-P)\). It checks that all pulse survival probabilities lie strictly between zero and one. Its finite permutation enumeration is ancillary and does not certify the universal all-parameter theorem.

The model concerns a full-resistance invariant face and assumes the same treatment block repeats forever. Neither finite-sample experiments nor computations are offered as proof of an infinite-time result. The numerical eigenvalue approximations are illustrations only.
