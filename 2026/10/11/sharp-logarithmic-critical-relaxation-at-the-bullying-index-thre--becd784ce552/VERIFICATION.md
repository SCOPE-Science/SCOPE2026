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

At αA=cβ, x*=c/α=A/β, q=x/x*−1 leads exactly to q'=−βq−b(1+q)y, y'=cqy. The Lyapunov function V=x−x*−x*log(x/x*)+(b/α)y has V'=−β(x−x*)²/x and compact positive-state sublevels; the only invariant part of {V'=0} is (x*,0), giving global convergence for interior data. Defect r=q+(b/β)y solves r'=−βr+[b(c−β)/β]qy; variation of constants and y'/y→0 yield r/y→0, whence (1/y)'→bc/β and t y→β/(bc), t(x−x*)→−1/α. With a2=b²(β−c)/β³, second defect s=q+(b/β)y−a2y² obeys the exact stable equation printed in RESULT.md with cubic/quartic forcing; independently SymPy-simplified both sides and obtained zero residual. The bound s/y²→0 follows from stable variation of constants; then (1/y)'=bc/β−(c a2)y+o(y). As 1/y~(bc/β)t, integration yields logarithmic coefficient −(c a2)/(bc/β)=b(c−β)/β². All constants hold for any strictly positive initial x,y, not just near the fixed point; the y=0 invariant boundary is properly excluded.

## originality

PASS

New claim and its implications assessed against named primary papers and fresh Resultary published-finding searches. Self-indexed candidate hit ignored as evidence of novelty. The four mandatory checks, material actually read, and risks follow.

## value

PASS

The natural threshold R0=αA/(cβ)=1 removes the hyperbolic relaxation mode and prompts an exact global critical decay law. The universal leading constants and first logarithmic term distinguish c=β from c≠β, giving a genuinely motivated boundary invariant beyond the source qualitative transcritical stability. Generic normal-form folklore suggests 1/t but does not specify these actual global coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
