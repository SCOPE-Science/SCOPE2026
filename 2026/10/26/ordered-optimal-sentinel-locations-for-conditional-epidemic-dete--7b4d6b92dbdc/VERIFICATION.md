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

PASS. In the exact independent-Bernoulli-bond path model with one uniform nonsentinel seed and deterministic unit travel times, the probability of eventual detection at monitor j is F_j/(n-1), F_j=Σ_{i≠j}p^{|i−j|}; the conditional mean is G_j/F_j=pF′_j/F_j with G_j=Σ_{i≠j}|i−j|p^{|i−j|}. Reflection reduces positions to the left half. The adjacent monitor difference is controlled by comparison with M_j=j−(n−2j)p^{n−2j}/(1−p^{n−2j}); μ_j increases in p by the positive variance of the distance distribution, while M_j decreases, yielding one root per noncentral adjacent comparison. The monotonicity of h(x)=x/(exp(λx)−1) plus x/2, λ=−log p>0, orders the roots strictly, so all left interior locations appear successively and no endpoint minimizes. Detection probability instead maximizes at the center(s). The n=5 first switch is the positive root p²+2p−1, namely √2−1. Independent rational calculations checked conditional objectives and center/nonendpoint behavior at 28 (n,p) pairs, and the actual finite certificate/program enumerates every bond pattern through n=9 and brackets thresholds through n=24. None of these finite tests substitutes for the all-n monotonicity proof; all boundaries 0<p<1, n≥5, n=2–4 special cases, and symmetry were checked.

## originality

PASS

PASS, best-of-knowledge only, for the exact all-path ordered threshold theorem, NOT for the conditional-detection-time objective. Holme (2017) explicitly introduces conditional sentinel discovery time and exact finite-graph SIR analysis, and Holme (2018) studies its distinction from detection frequency. Those earlier statements are acknowledged and involve continuous-time SIR, rather than deterministic travel time on Bernoulli-open path edges, and do not imply a unique strictly ordered sequence of all-n transition thresholds. Resultary comparisons found other path sampling and epidemic detection problems but no stronger coverage of the stated model and theorem. A general theorem about logarithmic derivatives of truncated geometric sums could implicitly cover it; full priority is not certified.

## value

PASS

PASS. Conditional speed and reliability are competing natural surveillance objectives. The proof gives a complete phase diagram over every path length, with an explicit first nontrivial threshold and every intermediate monitor realized on a nonempty parameter interval, whereas optimizing detection probability remains central. This is not just a finite example or a reformulation of the expected detection time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
