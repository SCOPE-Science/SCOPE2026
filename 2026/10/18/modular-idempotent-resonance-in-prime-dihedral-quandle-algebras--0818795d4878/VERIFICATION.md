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

The ordinary truncated-ring coordinate identities are proved algebraically in `RESULT.md`; the standalone `check_idempotents.py` constructs the finite group algebra and evaluates every quandle basis multiplication directly. This is a check of the claimed identity, not merely a rerun of the coefficient-resonance formula.

The checker exhausts \\(3^3\\) vectors in \\(\\mathbb F_3[R_3]\\), \\(5^5\\) vectors in \\(\\mathbb F_5[R_5]\\), and \\(9^3\\) vectors in \\(\\mathbb F_9[R_3]\\); it confirms the complete counts \\(4,6,10\\), respectively. It tests the multiplication law on independently sampled parameters at primes \\(3,5,7,11,13,17,19,23,31,41\\); explicitly checks the \\(p=17\\) witness \\(\\exp(X^9)\\) with direct multiplication, and produces `ALL_EXACT_CHECKS_PASSED`.

A hand-checkable independent witness of a length-three idempotent takes \\(\\mathbb F_9=\\mathbb F_3[\\alpha]/(\\alpha^2+1)\\) and \\(h=2e_0+(1+\\alpha)e_1+(1+2\\alpha)e_2\\). In the commutative dihedral quandle \\(R_3\\), the coordinates of the square of \\(ae_0+be_1+ce_2\\) are \\((a^2+2bc,b^2+2ac,c^2+2ab)\\). They reproduce the coefficients of \\(h\\), all nonzero. This provides a direct check that the general length-three assertion in arxiv:2608.01550 Theorem 3.6, as literally formulated, is too broad.

The checker uses no external libraries, hardcoded classification tables, external services, or private data. Finite computations corroborate but do not replace the proof for all primes and fields. Independent mathematical audit has not been performed.
