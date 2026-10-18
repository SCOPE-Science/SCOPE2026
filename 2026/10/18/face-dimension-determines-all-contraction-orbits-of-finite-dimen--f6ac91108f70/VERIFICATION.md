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

The analytic proof in `RESULT.md` has three critical checks: (1) the preimage under a contraction of a target face, intersected with the unit ball, is a face and contains the source minimal face; (2) a dimension-preserving isomorphism between exposing-kernel hyperplanes can send the source face-tangent span into the target face-tangent span exactly when the source dimension is at most the target dimension; (3) a sufficiently small common positive parameter controls all finitely many vertices, with the cases exposed-source, opposite-exposed-source, and strict interior of the exposing functional exhaustive. Invertibility is checked using the target exposing functional, not presumed from a numerical determinant.

The reproducible example `check_faces.py` uses exact rational arithmetic and the twelve vertices of a hexagonal prism whose norm is \(\max\{|u|,|v|,|u-v|,|w|\}\). Run `python3 check_faces.py` with SymPy installed. The program checks six permitted face-dimension transitions using an explicit construction, verifies an invertible matrix and the prescribed image, and verifies the norm bound at all twelve vertices for each transition. Successful finite replay supports only those finite examples and does not replace the general proof.

Relevant prior statements were compared by implication rather than keyword alone: the 2022 flat-target result covers the facet target stratum but not intermediate ranks; the previously published coordinate classification concerns only cubes and cross-polytopes. Full-text access to the 2019 near-transitivity article was not obtained, leaving an explicitly stated originality risk. No third-party or external independent verification is asserted.
