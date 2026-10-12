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

The proof of each universal assertion is supplied in `RESULT.md`. Run the standalone standard-library-only checker with `python verify.py`.

The checker generates the six characteristic-five lines as spans of the all-ones vector and permutations of the five field elements, confirms that there are six distinct lines containing six points each, pairwise intersecting only at the diagonal vertex, exhaustively enumerates the \(31\) rational points of the fixed three-equation model and identifies its sole singular \(\mathbb F_5\)-point. It checks the exact quadratic and cubic identities coefficientwise by evaluating every triple over \(\mathbb F_5\); every individual variable degree is less than five. It checks linear independence of the conic and cubic gradients at all six directions, giving a finite certificate of transverse intersection and, together with Bézout, scheme-theoretic exhaustiveness. It separately enumerates characteristic-two and characteristic-three surface points and tests their Jacobian ranks, and enumerates smooth-model points over \(\mathbb F_7\), \(\mathbb F_{11}\), and \(\mathbb F_{13}\) as finite cross-checks.

Checks do not compute a stable model and do not independently verify originality. Exhaustive finite-field testing is not a proof of geometric assertions over algebraic closures or over all primes; the symbolic algebra, Jacobian argument, Hilbert series, normalization and finite-field inclusion-exclusion in `RESULT.md` provide those proofs.
