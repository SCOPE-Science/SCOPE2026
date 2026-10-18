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

# Verification

Run `python verify_link_dynamics.py` with Python 3; no external packages or data are needed. All graph states, graph isomorphism permutations, moment matrices and fraction operations are generated from the source code. The verifier checks the moment defining equations by substitution and asserts exact class counts \((1,2,6,21)\), edge-addition counts \((0,1,11,80)\), opposed-sign pair counts \(((0,0),(0,0),(3,0),(0,1))\) for continuous-time and discrete clocks, and the two exact witness sign pairs. It terminates by printing `ALL EXACT CERTIFICATES PASSED` on success. These calculations were run successfully against the packaged code contents.

The code proves only finite-size exhaustive claims; the complete-coverage argument is that every simple labeled graph is enumerated, tested for connectivity, then canonicalized under all vertex permutations, and every possible nonedge is explored. No search of larger graph orders or independent human audit is asserted.
