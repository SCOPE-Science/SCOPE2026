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

Scalar matrices act by zero in characteristic two. In coordinates (s,t,w) a generator T_(lambda,u) sends these to (omega(u,w),0,lambda w+ut) by direct multiplication. The two-factor parameters are (lambda*mu,mu*u,lambda*v,omega(u,v)). On the traceless subspace every generator kills the central summand and acts by a scalar on the quotient by the center, so T_(lambda,u) T_(mu,v) T_(nu,w) = T_(lambda,u) T_(mu*nu,mu*w). This reduces every nonempty word of length at least two to exactly two letters. When the first parameter h is nonzero the equation h*c0=omega(p,a) is necessary and sufficient by taking mu=1, lambda=h. When h=0 one of p,a vanishes; any residual c0 can be chosen by the nondegenerate alternating form, including p=a=0 using two trace-zero generators. The nonzero one-letter cases with h=0 and p=a are excluded from every longer word. Normal-form parameters are unique as matrix coefficients. For h nonzero the image is a graph over the two-dimensional W; the zero-h two-letter cases have rank one except for zero; the exceptional generators have independent central and W images of total rank two. Counting gives all displayed cardinalities. Independently, /workspace/review_evidence/check_3_5.py evaluates operators via ordinary 2-by-2 products on matrix units over GF(2) and GF(4), enumerates exact length sets one, two and three, checks equality of the latter two, and computes each rank from image size. It reproduces (generators, doubles, total)=(8,30,33) and (64,892,907), with ranks (1,13,19) and (1,123,783) for ranks 0,1,2. This finite reproduction does not replace the general argument. The frozen verifier was inspected, not executed.

## originality

PASS

The strongest inspected primary source proves the full semigroup theorem for normalized Jordan multiplication in characteristic different from two, and explicitly records only the scalar-kernel/traceless-image obstruction for the unnormalized operators in characteristic two. None of the inspected comparisons classifies the images of nonempty words here, solves the two-letter factorizations, or enumerates the semigroup. Nearby results count other objects. The conclusion is limited to the stated characteristic-two M2 semigroup, not historical priority.

## value

PASS

This natural smallest matrix-algebra case resolves the characteristic-two boundary where normalized Jordan theory is unavailable. The standard kernel/image obstruction says only that the full endomorphism semigroup is impossible. In contrast, the result gives exact membership, a sharp factor-length dichotomy, and the full finite rank distribution, which answer structural questions beyond exclusion or a small-field check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
