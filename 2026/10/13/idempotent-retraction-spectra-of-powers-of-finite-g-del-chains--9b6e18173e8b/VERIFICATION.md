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

The standalone verifier `verify.py` uses the Python standard library. Run from this folder with `python verify.py`.

The independent finite enumerator scans all set-functions on disjoint unions of nonempty finite chains for ten parameter pairs, retaining exactly those preserving the order and satisfying the successor-set equality. The enumeration is exhaustive for each listed finite poset, not a sample. It computes the actual image poset and image-rank polynomial and separately classifies idempotent maps by direct composition. The predictions come from a distinct closed-form combinatorial implementation. Further checks compute, for every verified p-morphism in five small cases, pullbacks of all upsets and verify the Heyting implication equation for every pair of upsets; image sizes are also cross-checked by constructing the algebraic image. Twenty additional binomial counts independently test the number of possible image isomorphism types.

A completed replay returned:

`VERIFY_OK 19555 exact comparisons; exhaustive maps for ten parameter pairs; algebraic implication preservation through 6 dual points`

Important exact examples include \(I_{2,2}(z)=2z^2+4z^3+z^4+2z^6+z^9\) and a total of 59 idempotents on \(C_3^3\). The tests do not exhaust unbounded parameter pairs and do not replace the general duality proof. No independent mathematical audit has been performed.
