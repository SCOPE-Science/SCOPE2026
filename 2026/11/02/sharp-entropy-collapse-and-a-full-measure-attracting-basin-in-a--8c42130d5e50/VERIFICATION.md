---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For 1<t<2, 0<s<1, ts<1, 0<p<1, T=g_{s,p} o f_t has outer slope ts<1 and inner slope R=t(1-sp)/(1-p). The fixed inner barrier a=p(1-s)/(t(1-sp)-(1-p)) is interior exactly p<p_c. For R<=2 the inner core [a,1-a] is invariant with constant slope ±R, giving log R. For R>2 it has two disjoint inverse branches with contraction 1/R and full two-shift repeller; cylinder lengths yield (1-2a)(2/R)^n and dimension log2/log R, outside attracts to zero. At p>=p_c the image enters a monotone absorbing half interval, so entropy vanishes. The R=2 and p=p_c boundaries are separated. I independently evaluated exact rational thresholds and core widths at p=1/10,1/5,7/10,8/9,9/10 when t=9/5,s=1/2; they match p_*=2/11,p_c=8/9. The source proof, not these samples, covers all parameters.

## originality

PASS

Cánovas 2021 studies exactly this tent-homeomorphism composition, explicitly proves zero-entropy threshold cases and displays numerical kneading plots; its conclusions state analytical region boundaries remain unclear. Generic constant-slope entropy, Cantor similarity theory and unrelated skew-tent/plateau results do not give these exact parameter/basin formulas. The boundary equality case belongs to Cánovas; originality here is the complete phase law and escape geometry.

## value

PASS

Exact entropy plateau versus a full-measure basin of a single attracting fixed point is a coherent dynamical phenomenon in the precise family examined by Cánovas. Sharp critical boundaries, Hausdorff dimension and escape time answer a meaningful published parameter problem rather than an arbitrary toy map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
