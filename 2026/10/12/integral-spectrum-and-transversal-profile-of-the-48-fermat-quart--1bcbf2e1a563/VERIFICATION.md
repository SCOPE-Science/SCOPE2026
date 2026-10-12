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
The exact checker reconstructs the three \(16\)-line families and every one of the \(\binom{48}{2}\) pair incidences from congruence rules obtained from the line equations.

It verifies:
- \(48\) vertices, uniform degree \(14\), and \(336\) edges;
- exact characteristic polynomial
  \[
  (t-14)(t-2)^{28}(t+2)^{12}(t+6)^6(t+10);
  \]
- exactly \(792\) skew pairs;
- skew-pair common-transversal counts \(2^{\times96},4^{\times192},6^{\times480},10^{\times24}\);
- rank \(20\) for \(A-2I\), with eigenvalue signs giving inertia \((1,19,28)\).

The computation is finite and exhaustive once the complete published 48-line list is accepted. It does not certify any statement about ambient lines outside the Fermat line set.
