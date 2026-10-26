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

# Reproducible checks and mathematical limits

Run `python3 verify.py` with Python 3, no third-party dependencies. Exact integer and `fractions.Fraction` calculations enumerate all admissible \(m\) for the wedge and two-edge matching motifs on five vertices and the wedge-plus-edge motif on six vertices. These total exactly 32,380 labeled fixed-edge graphs. Each of the three cases checks the mixed covariance and both expectations. Exact sign and cubic-factor checks run over the specified \(n\)-ranges through 100. Expected output: `VERIFY_OK 32380 exhaustively enumerated fixed-edge graphs; 436 exact checks`.

These computations do not establish the claim for arbitrary size or motif. The general proof instead fixes a particular motif occurrence and a vertex, counts forbidden incident edges, and divides by exact positive marginal means. The only algebraic sign steps are the two length-two falling-factorial differences and the displayed cubic. The test script independently enumerates graph edge subsets and motif occurrences to detect arithmetic mistakes.

There is no independent mathematical audit, historical-priority certification, or external verification. The exact formula excludes degenerate zero-mean edge ranges and induced-copy conventions.
