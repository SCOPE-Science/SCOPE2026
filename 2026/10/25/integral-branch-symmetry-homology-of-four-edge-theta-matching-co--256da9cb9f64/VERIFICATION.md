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

# Reproducibility and evidence

The integral assertion is established mathematically in `RESULT.md`, using a free-face collapse, a natural long exact sequence of a pair, and an explicit orientation character. Its hypotheses include every integer \(m\ge2\).

Run `python3 verify_theta.py` with Python 3 and only the standard library. The included `verification_output.txt` is a recorded successful execution. The program independently constructs every matching face by vertex-disjoint edge enumeration and by arm-state restrictions. It then checks the exact descending-dimension face collapses, computes simplicial boundary ranks over \(\mathbb F_2\), and calculates signed fixed-simplex Lefschetz traces under \(S_m\times C_2\). Complete groups are checked for \(m\le5\); selected elements are checked for \(m=6,7\). It reports 320 action checks overall and concludes with `REPRODUCIBLE_CHECKS_OK total_signed_action_checks=320`.

The finite checks do not establish the infinite-family classification and do not check integral torsion by Smith normal form. Integrality follows from the natural exact sequence of free abelian groups in the proof, not from the finite field computation. The verifier uses the combinatorial face model defined in `RESULT.md`; it does not independently search mathematical literature or determine originality. No external independent validation has been performed.
