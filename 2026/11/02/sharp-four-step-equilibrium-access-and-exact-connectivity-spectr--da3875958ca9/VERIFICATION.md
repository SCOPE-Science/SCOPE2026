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

# Exact finite verification

The attached `verify.py` is a stand-alone Python 3 program with no nonstandard dependencies. Execute `python3 verify.py` from the directory containing this file. The expected first line is `VERIFY_OK`; the remaining lines list the two- and three-player orientation counts and the sharpness witness distances. The program enumerates every bit string for the twelve edges of the three-cube, applies two different exact shortest-path algorithms (reverse breadth-first search and Floyd–Warshall), and checks the identical results for each graph, with a separate inclusion–exclusion denominator check.

The analytic cube-layer argument in `RESULT.md` proves the uniform four-step bound; the finite exhaustive computation proves the stated exact frequency distribution, verifies the graph-theoretic connectivity test, and certifies the sharpness witness. All arithmetic is integer-valued. No symbolic or numerical approximation, random sampling, timeout, or extrapolation is used. The statement is about existentially chosen improving actions, not arbitrary activation sequences. Published quantitative priority cannot be guaranteed from the inspected literature alone.
