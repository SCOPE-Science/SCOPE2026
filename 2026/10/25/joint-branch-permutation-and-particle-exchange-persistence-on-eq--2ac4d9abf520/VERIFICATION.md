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

The standard-library checker `starpair_equivariant_verify.py` builds the oriented crown graph, chooses a spanning tree, constructs a fundamental integral cycle basis for its kernel of cellular boundary, and checks the induced signed homology traces directly (not merely from the edge fixed-point formula). It exhaustively tests every element of \(S_m\times C_2\) at each \(m=3,4,5,6,7\), for 11,820 exact group-action instances. It additionally checks graph connectedness, integral homology rank, the cellular trace formula and the predicted exchange-even/exchange-odd dimensions.

Observed completion marker: `STARPAIR_JOINT_ACTION_VERIFIED 11820`.

These tests check a finite set of dimensions and do not prove the equivariant strong-deformation claims for arbitrarily many arms or all real positive clearances. The general arguments appear in RESULT.md. No independent mathematical audit has been performed.
