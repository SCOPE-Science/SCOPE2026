---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

After translating projected apex to origin, a tilted unit normal u=re+sqrt(1−r²)n has exact width rb+max(ra,h sqrt(1−r²)), a=h_C(e), b=h_C(−e). With projection in base a,b>=0, branch switch r0=h/sqrt(h²+a²); initial concave branch has endpoint minimum and second branch is nondecreasing, yielding min{h,h(a+b)/sqrt(h²+a²)}; reversing e gives symmetric max-denominator condition. Projection outside base yields b<0 in a separating direction and w<h for small r. The Bakaev–Polyanskii uncovered-volume bound with w=h is matched by the base-adjacent plank via similarity volume factor (1−W/h)^d. This is a symbolic proof, not a finite sweep.

## originality

PASS

The known partial-plank theorem and its simplex equality case take the altitude=minimal-width condition as a hypothesis. The audited support-function criterion verifies exactly when it holds for arbitrary convex pyramids and gives a formula when the apex projects into base. Averkov–Martini addresses reducedness rather than this explicit formula in available material; older unnoticed formulas remain a risk.

## value

PASS

Exact width of arbitrary nonsymmetric pyramid with in-base apex projection and sharp if-and-only-if altitude criterion are structurally natural. The resulting plank equality class is an application of known sharp machinery rather than claimed new plank bound; natural complete criterion has independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
