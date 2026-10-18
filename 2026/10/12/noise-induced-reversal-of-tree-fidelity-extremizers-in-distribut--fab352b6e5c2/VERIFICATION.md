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

For fixed n-vertex tree, Prüfer excess degree vector t_i>=0 sums n-2. For 0<q<1, strict convexity of log(1+q^d) and majorization make path unique minimum and star unique maximum. For physical q=-r in [-1/3,0), positive excess contributions h_r(k) lie between h_r(2) and h_r(1); inequality 2h_r(2)>h_r(1), equivalent to r(1+r)(1-r-r^3)>0, makes star unique minimum, path maximum. For subcubic trees degree count (k+2,n-2-2k,k) produces exact step factor 1+q(1-q)^2/(1+q²)^2. Independently enumerated all Prüfer words n=4,5,6 for q=+/-1/3, verified endpoints and subcubic ratios. Proof applies to all n>=4, actual physical depolarizing p up to 1.

## originality

PASS

Dutta Theorems 15–16 establish source product; Remarks 17–20 compare positive contraction and four-node trees; no negative-contraction whole-tree star/path reversal or full subcubic k-law. Tanizawa/Numajiri model post-preparation data-qubit noise, not distribution resource-qubit noise. Substantive best-of-knowledge originality, not merely absence of identical wording.

## value

PASS

The source-defined graph-state fidelity has a sharp *physical* sign reversal at completely depolarizing point, all-tree extremizers and a structural subcubic branch-count law. Those results answer topology selection in the idealized protocol, not merely a low-order numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
