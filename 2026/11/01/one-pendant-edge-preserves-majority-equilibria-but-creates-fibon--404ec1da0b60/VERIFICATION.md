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

# Computational verification

Run `python3 verify.py` with Python 3; no third-party packages are used. The included `verification_output.txt` records a successful local execution.

The verification program independently implements one synchronous graph-neighbor update, enumerates all binary configurations for each \(3\le n\le17\), and counts returns of temporal length exactly one or two. This checks \(524272\) configurations in total, without presupposing that all states are recurrent. It independently calculates the composition formula, the Fibonacci/period-six formula, the four-state transfer trace, and the closed Lucas/cosine expression; these match for all \(3\le n\le100\). For \(3\le n\le13\), every detected primitive two-cycle is checked to have exactly the flip set asserted in the theorem, and each root–leaf-only orbit is checked against the opposite-end, minimum-run-length conditions.

The software does not perform exhaustive symbolic verification for unbounded \(n\), nor is it used to prove the period restriction on arbitrary initial states; those rely on the analytic potential and combinatorial proof in `RESULT.md`. The 1980 period-two paper's full text was not available during literature comparison, which remains an originality limitation rather than a numerical verification issue.
