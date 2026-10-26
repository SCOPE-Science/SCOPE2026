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

# Verification record

The standalone Python 3 program `verify_bipartite_ghm.py` uses only the standard library. It checks every one of the \(676\) nonempty capped class-size patterns, preserving state histories only for nonempty classes. This exhaustive, lossless finite quotient verifies that all primitive periods are \(1,3,4\), that all preperiods are at most five, and that preperiod five is exactly the structural thin–fat condition in the proof. The \(676\) patterns are \((3^3-1)^2\); there is no omitted parameter class.

The program independently constructs the labelled vertex transition, exhaustive over all \(560124\) initial configurations on the selected six graphs. It checks the closed terminal-depth count on each, together with maximum depth and recurrent-state counts. Sample outputs include \(144\) maximal-delay configurations on \(K_{3,4}\), \(384\) on \(K_{4,4}\) and \(11040\) on \(K_{6,6}\). The recorded text file `ghm_verification_output.txt` was regenerated from the exact embedded checker.

The general mathematical deduction requires the compression lemma, the finite exact type enumeration and the closed binomial count. Direct finite graph samples are only supplementary. No external certification or independent audit has been performed.
