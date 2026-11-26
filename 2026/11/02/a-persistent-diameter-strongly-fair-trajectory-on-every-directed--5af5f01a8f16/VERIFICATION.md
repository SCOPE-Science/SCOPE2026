---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Starting at the unit singleton j, full copies first to j+1 and then to j leave the singleton at j+1; j−1 is distinct from both j and j+1 for n≥3. Each block starts with untouched zero and one anchors. Repeating the actual arc into i leaves the source unchanged and differs from full copy at its endpoint by (1−p_i)^N times the starting difference. Each finite N_m can make that error at most 2^(−m−4), and full copy is 1-Lipschitz in the sup norm, so the block-entry error is strictly below 1/8. The actual anchors never change within their block, proving the diameter bound also at every individual activation. Each arc appears twice per ideal rotation and each real block is finite and nonempty. On two vertices the gap is at most max_i(1−p_i)^t times its initial value, where the intended bound is [max_i(1−p_i)]^t; nested extrema then imply convergence. One vertex cannot fail, and strong connectivity for n≥3 needs at least n arcs, so the three-vertex three-arc example is minimal in both respects.

## originality

PASS

Pass the structural and parameter-uniform claim: every oriented cycle of length at least three, including the minimal three-arc graph, every fixed interior set of weights, and the specified unit-singleton seed with uniform separation. Credit Aranda et al. both the earlier strongly fair failure and the already implicit all-time positive diameter on their four-arc graph; the quantitative-gap feature alone is not original.

## value

PASS

This identifies a sharp failure boundary in network size and arc count and shows that the lack of consensus under infinite edge recurrence does not require a vertex influenced by competing neighbors. The all-activation bound excludes convergence by more than a non-consensus subsequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
