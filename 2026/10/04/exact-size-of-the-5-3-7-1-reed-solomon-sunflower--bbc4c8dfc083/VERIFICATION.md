---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The finite theorem was independently reconstructed from field arithmetic rather than trusted from a saved log. Affine normalization gives exactly 60 distinct \([5,3]_7\) row spaces. Fresh modular row reduction over \(\mathbb F_7\) reproduced 1200 compatible pairs of intersection dimension one, 570 pairs of dimension two, and a 40-regular compatibility graph. An independently implemented Bron--Kerbosch enumeration gave maximal-clique histogram \(30,1920,5070,1800,138\) at sizes \(6,7,8,9,10\), respectively, with clique number 10. This independently matches the displayed ten-code witness and establishes the finite upper bound.

## originality

PASS

The current primary abstract introduces Reed--Solomon sunflowers, gives the generalized V-matrix framework, solves dimension two, and for fixed \(k\ge3\), \(\ell\ge2k-1\) advertises asymptotic recursive and greedy lower bounds rather than an exact finite \((5,3,7;1)\) optimum. Targeted Resultary searching did not locate an earlier exact value for these parameters. The full current preprint could not be read in this run: the open full-text route was unavailable and the permitted institutional retrieval returned an Oxford worker error. Accordingly the assessment is best-of-knowledge with the unread remainder explicitly retained as a residual risk.

## value

PASS

This is the minimal-length higher-dimensional regime \(\ell=2k-1\) with \(k=3\), and \(q=7\) is the first prime field above the boundary field size \(q=5\) with a substantially nontrivial 60-code compatibility graph. The exact optimum therefore supplies a natural finite benchmark for an explicitly introduced extremal problem, including a complete finite upper certificate rather than an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
