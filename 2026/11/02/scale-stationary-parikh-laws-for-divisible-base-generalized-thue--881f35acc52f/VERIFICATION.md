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

# Reproducibility and scientific limits

Run `python3 verify.py` with Python 3.10+ (standard library only). Expected success prefix: `VERIFY_OK checks= 199`.

The code computes the displayed rational law by exact `fractions.Fraction` arithmetic for eight parameter pairs, tests normalization, nonnegative support and sign/rotation symmetries, verifies selected exact reference probabilities, and compares the measure against factors of morphism-generated prefixes at multiple substitution powers. Additional explicit residue-block checks test the joint carry-length/letter uniformity lemma.

Empirical comparisons use a finite tolerance only to accommodate boundary and carry tails in finite samples. They do **not** prove equality at infinitely many powers, nor certify an arbitrary excluded base. The infinite natural-density proof is given in `RESULT.md`, which derives a pointwise boundary identity and a tail-controlled geometric limiting law. The test suite and mathematical argument were checked in the same review; no independent scientific audit has been performed.
