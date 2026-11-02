---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For every real d the adjacent-pair cancellation x_(2k+2)=x_(2k) proves x_even=1 and y_(2j)=d-1, y_(2j+1)=d*y_j-1; induction yields y_k=u_(nu_2(k+1)). Exact counts c_r(K)=floor(K/2^r)-floor(K/2^(r+1)) differ from K/2^(r+1) by at most 1, giving total variation O((1+log N)/N) uniformly in d even when values collide. Solving u_r=C_d*d^r+1/(d-1), with the separate d=1 case u_r=-r, proves precisely bounded d in [-1,1) union {2}, and the all-real positive-moment threshold. For |d|>1,d!=2 the critical |d|^p=2 Cesaro sum of geometric-level contributions gives exactly |C_d|^p/4 times log_2 N. Errors at criticality are O(1) and finite-order cases have vanishing weighted count discrepancy. Independent exact recurrence computation checked nine rational d parameters for 8192 indices each and all valuation levels. A finite check supplements, not proves, the universal analytical argument.

## originality

PASS

Prior proportional-delay work treats the same recurrence but sufficient stability, envelopes and finite-horizon RMS quantities, not the all-d exact atomic time-occupation law with total-variation convergence and singular-observable moment criticality. The analytically distinct exceptional multiplier lambda=-1 lies outside earlier sufficient decay bounds. Two-adic valuation densities are classical; the mathematical contribution is their exact realization in this feedback orbit and sharp moment law. Remaining older pantograph literature may have an equivalent boundary-slice formulation; best-of-knowledge PASS rather than uniqueness certification.

## value

PASS

The resonant delay recurrence is a concrete, natural boundary of proportional-delay stability. The complete atomic occupation distribution, uniform TV rate, and sharp high-moment transition show why time-typical behavior differs radically from rare excursions, including the d=1 case with unbounded orbits but all finite moments. The exact log-critical coefficient is useful for interpreting amplitude/RMS diagnostics; this motivated law does not claim the full two-parameter pantograph phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
