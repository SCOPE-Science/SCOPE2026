---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Read RESULT.md and check.py. Injective tensor H⊗G is exactly N(u,v)=max(||u||,||v||,||u+v||); the three evaluation vectors (u,v,-u-v) permit every permutation by common linear isometries. The chosen positive convex quadratic minorant E=a(||u||²+||v||²)+c||u+v||², 2a+c=1, has P^-1=[[B,-1/2],[-1/2,B]], B=1+sqrt(3)/2. For unequal active indices, the Hilbert map L(x,y)=(u+s,v-t) has squared norm D=2+sqrt(3) relative to E, while equal indices obey parallelogram, yielding C_NJ<=B. The orthonormal h,k witness in RESULT attains equality. Canonical projective tensor dual to L(H,G*) and the isometry (u,v)->(u,-v), plus C_NJ(X)=C_NJ(X*), transfers the bound and attainment to projective, also for arbitrary Hilbert dimension. Independently computed SymPy P inverse exactly, B≈1.8660254038 and verified scalar equalities; finite 9000 checks in source script are supplementary, not substitutes for the all-H proof.

## originality

PASS

The exact same hexagonal tensor family appears in Zhang–Xu–Liu–Li (2026) Example 3.12, where only strict C_NJ<2 is shown for infinite Hilbert factors. The inspected Theorem 3.11 gives an orthogonal-contact criterion for the maximal endpoint 2, not the exact nonmaximal value 1+sqrt(3)/2. The new sharp finite-dimensional witness and universal bound strictly strengthen but do not follow from that qualitative theorem.

## value

PASS

The original 2026 paper explicitly singled out this hexagonal plane as a strict submaximal tensor example while leaving the numerical constant unknown. This result determines the exact invariant for both canonical tensor norms, gives an attained low-dimensional extremizer and proves stability under arbitrary enlargement of the real Hilbert factor. The sharp exact value is a natural targeted answer to that published geometric gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
