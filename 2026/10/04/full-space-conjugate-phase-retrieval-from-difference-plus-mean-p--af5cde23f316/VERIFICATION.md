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
# Verification

The analytic proof reduces equal orbit magnitudes to two identities for every ordered pair, then uses classical double centering of squared Euclidean distances. The critical dimension-dependent check is that \(G_z-G_y=(c/2)J\) cannot hold with nonzero \(c\) between two positive-semidefinite Gram matrices of rank at most \(2\) once \(n-1\ge3\). No finite experiment is used to extend the theorem to arbitrary dimension.

The standalone script `verify.py` performs an exact bounded replay at \(n=4\). It enumerates the alphabet \(\{0,1,-1,i,-i\}^4\). After multiplying the measurement coefficient by \(2=\sqrt4\), every squared magnitude is an integer, so the collision test uses only Gaussian-integer arithmetic. Every one of the \(1864\) within-signature pairs is checked to be related by a global unimodular factor, optionally followed by coordinatewise conjugation.

Expected output:

`VERIFY_OK n4_signals=625 signatures=99 max_collision_class=8 collision_pairs=1864`

Limits: the finite replay samples a discrete subset of \(\mathbb C^4\); it is not an exhaustive search over continuous signals and is not a proof for higher dimensions. The proof, rather than the script, establishes the universal quantifiers.
