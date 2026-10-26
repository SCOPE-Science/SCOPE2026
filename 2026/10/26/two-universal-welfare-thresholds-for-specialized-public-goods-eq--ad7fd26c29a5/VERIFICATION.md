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

# Verification and reproducibility

Run `python3 verify.py` in the directory containing the six scientific documents and `verification_output.txt`. It uses Python's standard library only. The exact verifier enumerates specialized Nash configurations as maximal independent binary strings of paths \(P_n\) for \(2\le n\le23\), computes specialist counts and doubly served nonspecialists, then compares every attainable profile's exact rational score against the closed-form phase-diagram candidates for \(t\in\{1/10,1/4,1/3,2/5,1/2,3/5,3/4,9/10\}\).

The verifier separately reconstructs the three concrete length-twelve configurations. The expected output is embedded verbatim in `verification_output.txt`. These finite checks are reproducible consistency checks, not infinite proof certificates. The theorem for every \(n\ge2\) is justified by the explicit binary-gap bijection, feasible end-zero constructions and affine-score comparisons in `RESULT.md`. In particular, the critical reductions \(J_M-J_u=t-1\) for odd paths and \(J_M-J_u=2t-1\) for even paths are proved symbolically there.

The Nash model, first-online date and specialized-equilibrium correspondence were checked against [1]. The novelty claim is not independently audited; potentially equivalent graph-theoretic enumerations and restrictions of later models remain a bibliographic risk. All parameter statements concern exactly the assumptions in `RESULT.md`.
