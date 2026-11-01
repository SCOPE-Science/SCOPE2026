---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Exact component generator: negative-to-positive δ b_v(S)/2 and positive-to-negative (1−δ/2)q contributions. For every nonempty proper S within connected C, q_C(S)>0, so zero-δ transient chain drains to empty with invertible triangular generator. Recursive first-step perturbation gives probability hδ(S)=δ^{m−|S|}H_C(S)+O(δ^{m−|S|+1}). Each excursion out of empty succeeds with probability δ^{m−1}k_C/r_C+O(δ^m), while excursions have bounded moments and empty waiting is Exp(δr_C). Geometric thinning therefore yields Exp(k_C) on δ^{−m} time, with mean/UI. Components use independent clocks; global hitting is max, smaller components vanish on leading scale. Separate exact CTMC on 3-vertex path (one zealot) yields Eτ=4(1+δ)/δ², limit 4, confirming exponent and coefficient.

## originality

PASS

Best-of-knowledge originality with disclosed antecedents and material access limits. Compared finite-state metastable hitting/excursion, voter consensus, rare-mutation fixation and connected-component barriers rather than title matches; the exact fixed-graph subset recursion is not an immediate result of mean-field phase diagrams. No checked published theorem directly yields largest-free-component exponent and exact coefficient on every fixed connected graph; do not equate generic exponential-metastability principles with this model-specific constant.

## value

PASS

The largest induced dissenting component rather than total dissenters controls the consensus delay, a structurally motivated graph invariant under near-zealotry. Explicit rational rate recursion quantifies the asymptotic law beyond a generic metastability existence statement, with finite example contrasting connected and disconnected components.

The dated certificate retains the supplied scientific assessment, sources and limitations.
