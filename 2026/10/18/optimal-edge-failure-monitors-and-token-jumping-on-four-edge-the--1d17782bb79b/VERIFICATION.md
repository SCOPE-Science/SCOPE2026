---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Without a selected internal vertex on an arm no chosen pair can force any of its edges, because an entire terminal-to-terminal arm has alternate equal geodesics. Thus every MEG set has ≥r selected interiors. Exactly r forces all centers c_i, which monitor no edge, yielding lower bound r+1. With r+1, classify by whether terminal u, v or neither is selected: respectively U(B), V(A) with nonempty B,A, and one doubled arm W_i choosing a_i,b_i. Strict comparison of cross-arm routes p+q versus 8−p−q checks all witness pairs and completeness. Exactly 2(2^r−1)+r sets follow. One-token changes form two punctured cubes joined by r two-edge links; direct Hamming metric gives edge count r2^r and diameter 2r. Independent deletion-distance masks exhaust all r and r+1 candidate sets and reconfiguration for r=3,4,5; observed (optima,edges,diameter)=(17,24,6),(34,64,8),(67,160,10).

## originality

PASS

This is a precise optimizer and reconfiguration classification in the original two-endpoint MEG parameter, not a general scalar bound or an adjacent graph covering notion.

## value

PASS

A complete exact optimum-set structure and connected reconfiguration network for a natural once-subdivided complete bipartite family; characterizing all optima and diameter supplies structural reconfiguration information absent from a mere minimum cardinality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
