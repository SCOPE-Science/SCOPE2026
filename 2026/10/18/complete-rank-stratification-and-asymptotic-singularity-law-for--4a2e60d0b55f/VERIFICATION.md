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

The proof supplies universal analytic checks: the dyadic closest-pair lemma; exact rank-one and rank-two conditions after Fourier dephasing; a congruence forced by chord-product arguments; the exact determinant factorization; close-pair subset counting; and a dominated geometric-series calculation of the leading singularity probability. Boundary congruences use non-strict inequalities.

The standalone Python verifier `verify_dyadic_minors.py` computes determinants over the exact cyclotomic integer quotient \(\mathbb Z[X]/(X^{N/2}+1)\) and tests every two-by-two minor independently. It exhaustively checks all \(N=4,8,16\) three-row/three-column combinations, then tests 18,000 fixed-seed cases for \(N=32\) and 8,000 for \(N=64\), totaling 342,752 exact comparisons. The reported output was `VERIFY_OK 342752 exact minor-rank comparisons`; in particular, the exact three-rank counts at \(N=16\) were \((256,26624,286720)\).

These finite checks cannot establish the theorem for arbitrarily large \(m\); that conclusion rests on the symbolic arguments in RESULT.md. No independent audit has been performed.
