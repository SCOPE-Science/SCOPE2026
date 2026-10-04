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

The theorem is verified by a direct forcing proof. Its critical logical checks are:

1. **Dense separation.** For distinct \(x,y\) and any infinite ground-model \(F\), a finite condition can be extended with fresh distinct \(z_1,\ldots,z_{n-1}\in F\) and opposite relation values on the two resulting \(n\)-sets.
2. **Movement on every block.** If a nontrivial automorphism mapped \(x\) to \(y\ne x\) while fixing an infinite \(F\) pointwise, dense separation would contradict preservation of \(R\).
3. **Root collision.** After \(\Delta\)-system thinning, two distinct source points cannot both be forced to the same root point because a common free amalgam would contradict injectivity.
4. **Cross-petal freshness.** Choosing one source and one image from each of \(n\) different petals makes the source and image \(n\)-sets absent from every individual condition, so free amalgamation leaves both relation values available.
5. **Final contradiction.** Opposite values on those two \(n\)-sets contradict that the forced map is an automorphism.

Run `python3 artifacts/check_amalgam.py`. It checks the finite cross-petal bookkeeping for every arity from \(2\) through \(8\) and prints `VERIFY_OK`.

The script does not verify forcing semantics, uncountability, or the \(\Delta\)-system lemma. Those are proved mathematically in `RESULT.md`; finite testing is not used as evidence for the infinite quantifiers.
