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

The proof is replayed by `verify.py` using only Python's standard library. The checker represents numbers of the form \(a+b\sqrt d\) exactly over rational \(a,b\), reconstructs
\[
F_m(t)=
\frac{\frac{t^2}{m}-\frac87t+\frac{m+1}{7}}
{6\left(\frac{t^2}{m}+\frac{(1-t)^2}{6-m}-\frac17\right)}
\]
for \(1\le m\le5\), differentiates numerator and denominator algebraically, and verifies the exact radical maximizers and maximum values.

It also checks that the \(m=1\) maximum dominates the \(m=2\) maximum by an exact squared inequality, that the remaining chambers are below \(1\), that the equality pairing ratio simplifies to
\[
\frac{29-\sqrt{511}}{11},
\]
and that multiplying the normalized maximum by \(12\) gives
\[
6+\frac{2\sqrt{511}}7.
\]

The geometric volume identity is proved in `RESULT.md`; the checker verifies the subsequent algebraic optimization. A separate floating-point convex-hull calculation was used only as a consistency check and is not needed for correctness.

Limit: the verification establishes the six-dimensional theorem only. It does not certify any claim for dimensions \(n\ge7\).
