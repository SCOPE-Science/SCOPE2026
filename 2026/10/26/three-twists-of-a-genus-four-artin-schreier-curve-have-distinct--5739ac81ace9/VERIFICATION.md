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

# Reproduction of exact arithmetic

Execute `python3 verify.py` using Python 3.9+ with its standard library only. On successful exact reproduction the program prints `VERIFY_OK`, followed by the point-count and polynomial coefficient tables.

The program verifies that the four degree-\(1\) through degree-\(4\) finite-field moduli are irreducible over \(\mathbb F_3\); computes finite-field traces of \(x^2+x+x^{-2}\) for every nonzero field element; independently checks solutions of the equation by testing every affine pair \((x,y)\) for each \(c\in\{0,1,2\}\) and \(m=1,2,3,4\); confirms exactly two rational pole points and all twelve point totals; derives the four initial Weil coefficients by Newton identities and the rest by genus-four reciprocity; and checks exact reductions/factorizations modulo \(2\) and \(5\). For every claimed irreducible factor, it applies a finite-field gcd-and-power irreducibility test. Incompatible possible factor degrees prove rational irreducibility; no exhaustive infinite-field experiment is claimed.

The proof additionally invokes the published automorphism-group calculation of the source (Proposition 4.2) and the classical cohomological classification of forms and Tate finite-field isogeny criterion. Their mathematical hypotheses and finite-field scope appear in RESULT.md. No separate independent audit is asserted.
