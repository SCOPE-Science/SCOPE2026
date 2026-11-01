---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

From λ≡3 mod4, B=(1−λ)+8Z2 consists of v2(x)=1 and f² maps B into itself. For x,y∈B, f²(x)−f²(y)=(x−y)(x+y)(x²+y²−2λ), where x+y divisible by 4 and the third factor has v2=1, giving contraction ≥3 valuation gains per two iterations; Banach gives unique β, α=f(β) odd. Every odd x maps into B in one step, even in two. For u=y−β with k=v2(u)≥3, f(y)−α=u(2β+u) has v2=k+2; expansion f²(β+u)−β=u[4αβ+(6β²−2λ)u+4βu²+u³] has leading bracket valuation exactly3 and all others >3, proving k+3 per even iteration by induction. The h_N depth formula handles even/odd offsets; global branch exceptions for already-on-cycle and immediate one-step hits give the genuinely least T_N. Independent direct iteration through all residues mod 2^N (N=1..11) for λ=3,7,11,15,19,23 returned 24,564 exact agreement checks. Analytic valuation proof covers all Z2 parameters; finite experiments alone do not.

## originality

PASS

Fan–Liao established qualitative unique attracting 2-cycle for precisely λ≡3 mod4. Their cited primary theorem scope is global attraction and minimal decomposition; the submitted nonstandard quantitative refinement is an exact three-bit/two-step valuation gain and globally pointwise least preperiod on every mod 2^N quotient. These details are not stated in accessible summaries, but could be implicit in proof of qualitative contraction.

## value

PASS

Minimal preperiod of every residue modulo 2^N is a natural invariant of p-adic dynamics and finite quotient phase portraits. The exact three-bit/two-step contraction is a useful quantitative refinement of qualitative attraction; the formula handles all finite precision levels and early-hit exceptions, not an arbitrary tiny case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
