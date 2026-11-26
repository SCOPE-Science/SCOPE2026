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

Each minimal contract edge is itself a minimal obstruction span. Picking a pair that differs at its subfamily-private coordinate gives an identity minor on the chosen private coordinates, hence independent pair differences over F₂, in a difference space of dimension at most |C|−1. This proves the bound regardless of hypothesis count. The zero and edge-indicator contexts are distinct; exact guards ensure that each context has precisely the prescribed singleton explanation family, with no cross-context Horn-rule interference. All dependencies go from sources and hypotheses to terminal heads. Only zero-to-edge pairs are minimal obstructions and the antichain retains all their spans. Without any hypotheses, either no obstruction exists or a singleton obstruction forces the empty edge. In the globally private case, |C|=m+1 and the m independent pair differences exclude repeated pairs and cycles (differences telescope modulo two), giving a spanning tree. For disjoint labels on an arbitrary tree, XOR path assignments are distinct and an opposite-color pair has span the union of its path labels. Adjacent pairs realize every edge and all other opposite-color pairs give supersets; no converse for overlapping labels is asserted. RESULT.md proof steps 1–4 replay these arguments. I read VERIFICATION.md and checker.py without executing the latter. The checks enumerate small antichains, restricted two-choice tables and small labeled trees; the universal result comes from the proof, not finite enumeration.

## originality

PASS

Yang already supplies the same m+1 context upper bound with a two-hypothesis realization, and identifies singleton-explanation tables with rough-set discernibility; neither fact is credited as new. The evaluated differences are the minimum resource of one hypothesis, the private-coordinate lower bound unrestricted in hypothesis count, and its matching witness-structure theorem. In particular the lower bound is not a pairwise-table theorem restricted to unique explanations.

## value

PASS

This is a resource bound for realizing natural observation contracts, rather than another realizability proof. Private coordinates give a computable structural reason why adding more explanation atoms cannot reduce contexts below a threshold, with exact equality on a natural family and a tangible necessary witness tree. The optimal one-atom construction and disjoint-label tree family add explicit economical realizations. The result does not require the lower bound to be sharp on arbitrary overlapping contracts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
