---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For a b=2 block each column takes uniformly ±e1 or ±e2. Multiplying by fixed orthogonal 2×2 Hadamard H2 sends the four states bijectively to (±1,±1)/√2, making all transformed matrix entries independent Rademacher/√(2ζ), block and column independence being preserved. Hence whole-matrix distribution and joint Gram laws match all deterministic-input dense-sign sketches. At b=1 identical law is immediate. For m≥2 and b≥3, one offdiagonal Gram entry has fourth-moment difference (b−1)(b−2)/(b³ζ³)>0, derived using centered independent block collision variables and 3Σpair second-moment products. This excludes Gram equality for all ζ. For m=1 Gram is identically one at all b and is properly excluded. Independent exhaustive finite Gram distribution checks in 5 small configurations and 126 exact rational parameter moment checks succeeded.

## originality

PASS

SparseStack construction and embedding results give approximations or couplings to independent sparse/three-point distributions. They do not imply the deterministic b=2 Hadamard image is exactly a dense iid-sign matrix and the iff b≤2 Gram boundary. Classical Hadamard algebra/moment formulas are credited. Unindexed identity possible.

## value

PASS

Block width is a practical structural parameter of SparseStack, and an exact law transfers every Gram-based distributional statement between two-bucket sparse and dense independent-sign sketches. The sharp fourth-moment obstruction at widths ≥3 delineates precisely where the shortcut ceases; claims carefully avoid GPU speed, adaptivity and floating point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
