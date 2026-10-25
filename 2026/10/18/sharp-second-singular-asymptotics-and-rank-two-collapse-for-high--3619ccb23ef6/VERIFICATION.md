---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

After independent unitary scaling of input/output near opposite endpoints, Γ(α+1)I^α becomes the selfadjoint Hankel kernel (1-(u+v)/α)_+^(α-1). For epsilon=1/alpha expand e^(-s)[1+epsilon(s-s²/2)] with uniform HS remainder O(epsilon²), using ∫∫F(u+v)² dudv=∫s F(s)²ds and exponential tail. With g=e^-u, h=(u-1/2)e^-u, a=(u/2-u²/2+1/8)e^-u, independently checked symbolic identity a(u)g(v)+g(u)a(v)-h(u)h(v)=e^(-(u+v))[(u+v)-(u+v)²/2]. Since <g,h>=0 and ||h||²=1/8, the rank-two model has one order-one positive and one -epsilon/8 negative eigenvalue: minmax and best-rank approximation imply s2=epsilon/8+O(epsilon²), higher squared singular tail O(epsilon^4). Exact total HS²=1/(4-2epsilon) gives s1=1/2+epsilon/8+epsilon²/32+O(epsilon³). Independent SymPy expansion reproduces 1/32. The asymptotics depend on analytic uniform HS bound, not Nyström numerics.

## originality

PASS

Eveson's 2003 Journal of Operator Theory article and his complete 2004 arXiv followup were directly materially read. Their same-operator large-power results establish leading Γ(α+1)||I^α||→1/2 and qualitative rank-one collapse, but inspected statements do not specify α s2→1/8, the rank-two HS tail, or the 1/32 second-order norm correction. Thorpe (1998) and Dostanić (2001) are particularly plausible closer precursors but full works inaccessible in this run; this limitation is explicitly recorded as priority risk, not an access-only FAIL.

## value

PASS

The second singular mode and exact first two norm corrections quantify how fast a classical compact Volterra power becomes rank one, and the sharp rank-two tail can support more refined approximate spectral calculations. This is a nontrivial quantitative spectral refinement with natural fixed-order singular index, not a routine restatement of leading norm asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
