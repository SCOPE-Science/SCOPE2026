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
# Verification and limits

The mathematical proof of the all-even-size theorem is given in `RESULT.md`. The finite checks here serve only to detect possible mistakes in low-order cases.

Execute `python3 verify_bruteforce.py` and `python3 verify_evenfiber.py` with Python 3 and its standard library; compare their terminal output with `verify_bruteforce.out` and `verify_evenfiber.out` respectively. The first program constructs the actual four-by-four rook graph and performs recursive exact perfect-matching tests, not an assumed even-fiber characterization. The second implements the parity-fiber characterization directly and independently, exhaustively for orders four and six, verifies the connectivity of the specified within-orientation two-vertex reassignment graph, and checks the explicit cross-orientation witness and coefficient formula through order eight.

The first check yields 80 size-four optima, 720 batch-two edges and a uniform distance vector \((1,18,57,4)\). The second yields 40 and 2,256 row-orientation states at sizes four and six and full reachability under two-row moves. Both agree on 80 total minimum sets at order four. The exact graph-wide count and connectivity for larger even orders are proved combinatorially; these scripts do not enumerate their entire reconfiguration graphs.

The historical literature comparison has unavoidable residual priority uncertainty, and no independent external audit has been conducted.
