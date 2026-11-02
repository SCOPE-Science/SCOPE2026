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

## Exact independent enumeration

The accompanying `verify_component_motif.py` uses integer-weight enumeration over all \(2^{\binom n2}\) simple labeled graphs for sizes \(n=4,5\). It enumerates component isomorphism classes independently of the proof and counts induced and non-induced connected motif occurrences by vertex injections; all probabilities and covariances use `fractions.Fraction` and exact integer graph-state weights. Run `python3 verify_component_motif.py`; it must print `PASS 94 independent exhaustive probability identities; no sampling` after checking the stated 94 identities.

The verification includes \(H\) equal to a single edge, three-vertex path, triangle, four-vertex path, four-vertex star, four-cycle, and four-clique, and \(F\) equal to an edge, a three-vertex path, or a triangle. It checks the two motif conventions and rational edge probabilities \(1/5,1/2,4/5\), plus extra sign-transition cases. Both direct finite enumeration and the closed form agree. These are finite checks; the all-size proof uses conditional component isolation and strict one-variable monotonicity.

## Proof boundaries

The connectedness hypothesis is essential for eliminating a motif copy straddling a component boundary. No claim about disconnected motifs, fixed-edge graphs, or independence at a zero covariance is made. The two-sign rule for induced noncliques follows from the unique maximum of \(p^e(1-p)^s\); the sharp tree-shape bounds follow from the degree-excess sum \(\sum_v(d_v-1)=h-2\). The literature check is not a priority certification; the inaccessible full text of Frank (1979) remains a historical risk.
