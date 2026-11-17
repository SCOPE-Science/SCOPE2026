---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For a labeled configuration with k core and l peripheral ones, the fixed-state inequalities are k>0 ⇒2(k−1+l)≤a+b−1; k<a ⇒2(a−k−1+b−l)≤a+b−1; l>0 ⇒2k≤a; l<b ⇒2k≥a. For mixed core 0<k<a they imply a+b−1≤2(k+l)≤a+b+1. If k<a/2, peripheral zeros force l=b, contradicting 2k+b≤a+1 since b≥a and k≥1. If k>a/2, l=0 contradicts lower bound. Thus k=a/2 even, with l in the central one/two binomial layers; k=0 and k=a yield exactly two oppositely polarized states. Directly reimplemented all synchronous bit updates and compared every state against formula for all a<=5, a<=b<=8. Fixed-a b→∞ entropy follows from Stirling central binomial asymptotics; no claim on transient basins or b<a.

## originality

PASS

For this exact synchronous open-neighborhood tie-retaining minority rule, no located earlier result proves the fixed-state split-graph census or odd/even entropy transition. Published same-graph majority and asynchronous minority results use non-equivalent updates and do not imply this fixed-state count. Inaccessible original 1980 full text is explicitly a residual risk, not an automatic originality failure.

## value

PASS

A complete natural family of split graphs exhibits a sharp parity-controlled qualitative change in the number and entropy of **fixed points**, not merely an isolated small example; this distinction matters for anti-coordination/threshold dynamics and limits on possible attractors. The exact binomial classification has reusable structural meaning independent of any full transient analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
