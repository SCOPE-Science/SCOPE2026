---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A color dominates exactly if it meets the universal clique U or occupies all of the independent part I. For the lower bounds, prioritize U in the cases requiring only floor(u/2) Alice turns there; for odd u in the Bob-first game, if Alice gets only (u−1)/2 such turns under that policy then Bob has already supplied the first clique color, so Alice takes a fresh clique color on every turn that still needs one. For even u=2q in the higher-value cases, Alice can play second in every same-zone pair (opening in I first if Alice starts and m is odd): Bob supplies the first clique color and her q replies give q more. For the upper bounds, Bob copies a represented color on clique replies, and uses either a repeated clique color in I or two different colors in I to kill the exceptional dominating independent set. When Bob starts in U, the remaining U has u−1 vertices, with at most ceil((u−1)/2) Alice turns there under the reply rule. The same count applies after an initial Alice U move and Bob’s same-color response, with one fewer U vertex if that response is in U; for u=1 the response instead goes to I. A first unpaired Alice move in I due to odd residual size can force one Bob initiation in U; this is allowed in the even-u Alice-first odd-m bound, and m≥3 ensures there is an earlier I pair to make bichromatic. When Bob starts in I and m is odd, both residual zones are even. Each upper strategy works at the first excluded palette size and any larger size (it needs at most two colors for the obstruction). This recovers q versus q+1 exactly when u is even, and (u+1)/2 for both starts when u is odd. The independent exact symmetry-reduced minimax (`python3 /workspace/checks/finite.py 3`) checked both palette thresholds for 100 profiles with u≤8, m≤8 and u+m≤13. It is regression evidence; the same-zone argument treats all allowed sizes.

## originality

PASS

The supported distinct claim is the two-parameter classification for the complete split family, excluding novelty credit for the star or the already exact K_{1,1,m} slice. The strongest indexed exact overlap has only two universal vertices and decides a two-color game. Its parity pairing is a genuine antecedent, but its statements and proof do not handle increasing palette size or the odd-clique and unmatched-reply cases. The primary universal-vertex and degree theorems do not select the starting-player thresholds.

## value

PASS

The family is a natural class where dominating colors have just two possible forms. The exact pair of game numbers for all clique and independent-set sizes resolves both the one-color slack in the general degree bound and when changing the opening player changes the value. It shows the previously known parity reversal persists for every even clique size and disappears for every odd one. This is a family classification, not a recomputation of the two-universal-vertex table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
