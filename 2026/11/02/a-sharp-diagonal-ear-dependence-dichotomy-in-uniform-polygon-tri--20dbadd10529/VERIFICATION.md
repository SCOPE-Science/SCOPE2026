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

# Exact verification and boundaries

Run `python verify.py` from the directory containing this file and `verify.py`; Python 3 standard library suffices. The verifier constructs exact Catalan ear-count laws from combinatorial binomial moments and separately enumerates triangulations by recursive decomposition, then checks all conditional laws for every diagonal in polygons of four through eleven vertices. It also checks exact means, polynomial normalization, the sign classification for all integer parameters with \(2\le n\le80\), and the octagon two-tail counterexample.

Observed execution: `PASS 13138 exact assertions; 6916 triangulations explicitly enumerated`.

The enumeration is finite and provides cross-checks only. The universal theorem relies on the bijective proof and elementary rational sign analysis in `RESULT.md`. No independent mathematical audit has yet been performed. Historical priority and all-parameter proof validity remain subject to external review.
