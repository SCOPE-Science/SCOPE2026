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

# Reproducibility and scope

Run `python3 verify_theta.py` using Python 3 and no third-party packages. The program independently enumerates the combinatorial zero-, one- and two-cells for lengths-three theta-arm subdivisions; computes oriented action traces on every cubical chain group for every arm permutation through five arms, with and without pole interchange; and checks mod-two incidence-matrix ranks for three through six arms.

Expected final marker: `VERIFY_OK_THETA_TWO_PARTICLES`. For arm counts three through six the cell counts are respectively `(28,54,24)`, `(45,96,46)`, `(66,150,75)` and `(91,216,111)`. In each case the computed two-boundary has full column rank over the field of two elements. These are finite crosschecks, not substitutes for the all-arm proof.

The full proof in `RESULT.md` uses the integral two-dimensional cellular-chain injection into the product of graph chain complexes, full signed fixed-cell enumeration, and equality of finite-group rational characters. It does not establish an integral representation isomorphism for arbitrary arm count. Independent audit: not performed.
