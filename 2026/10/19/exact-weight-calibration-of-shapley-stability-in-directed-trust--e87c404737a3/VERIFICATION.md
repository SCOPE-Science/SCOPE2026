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

The proof in `RESULT.md` is self-contained. The finite program `verify.py` evaluates the coalition worth function from its definition for each subset, evaluates the Shapley allocation by its original factorial-weighted formula, and compares it to the derived graph formula using exact fractions.

Checked: all 771 connected labeled loopless undirected graphs with orders 2–5; positive calibration on an irregular strongly connected four-node network; impossibility for a three-node strongly connected mixed-indegree network with two positive target-weight choices; arbitrary-weight agreement on a pure directed cycle; the exact Shapley vector and Dirichlet energy on the three-node path.

Expected command: `python3 verify.py`. No input files, third-party Python packages, random sampling, numerical tolerances or network access are required.

Limits: this finite exercise does not exhaust all directed networks, weights or sizes; unbounded conclusions rely on the analytical proof. The historical-priority comparison is not independent validation.
