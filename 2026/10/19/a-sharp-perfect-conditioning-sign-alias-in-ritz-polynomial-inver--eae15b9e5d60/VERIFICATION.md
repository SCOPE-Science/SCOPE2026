---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The affine interpolant takes the signed values 1/u, 1/v and -1/(u+v) at u², v² and (u+v)². These are all three roots of z q(z)^2-1, whose leading coefficient is their inverse product. Under the two spectral-anchor hypothesis, any SPD preconditioned matrix of condition 1 must be I, and its only additional distinct eigenvalue of A is thus (u+v)². The threshold ((u+v)/u)^2>4 is strict, with every larger value attained and dimension 3 minimal. Left Arnoldi on B=I returns q(A)b; it attains relative error 2 on the third mode, despite exact evaluation of the preconditioned action. For the full-support pilot, moment orthogonality gives the stated increasing Ritz trace s1 and determinant s0; s1+sqrt(s0) increases from 7 and crosses 9 once, with the sign restriction 9-s1>0 at the positive quadratic root. In fact q_t(1) and q_t(4) stay positive throughout. At the crossing B_t is singular and there is no Arnoldi initialization on b=e3. Away from the crossing the one-mode output is sign(q_t(9))e3/3. At t=0 the first derivatives of the three preconditioned eigenvalues are -400/27, 400/27 and -400/3, giving the claimed quotient expansion for small positive t. The pilot g_t and application b are separate as specified. Independent bounded symbolic and numerical reproduction (`python3 independent_check.py`) rechecked these identities and the leading slope; the original checker was inspected, not executed. Exact arithmetic and the scoped two-node interpolation class are essential.

## originality

PASS

The branch obstruction and the left-preconditioned method with Ritz interpolation (including a separate pilot) are prior. The distinct result established here is the exact identity-preconditioned three-mode classification and sharp original-condition frontier in the anchored class, plus the precise full-support Lanczos branch transition and near-identity conditioning slope. No inspected theorem or indexed result supplies those facts. The broader web lookup was unavailable, so no claim about exhaustive priority is made.

## value

PASS

It shows exactly when perfect squared preconditioning fails to certify the target branch in a basic interpolation model, and that even full-support two-step pilots do not remove the issue: the method can give 200% error with conditioning tending to one. The sharp boundary is useful for separating a condition-number certificate from a branch certificate. The pilot construction complements the exact identity example without purporting to measure generic error rates or the performance of globally positive polynomials.

The dated certificate retains the supplied scientific assessment, sources and limitations.
