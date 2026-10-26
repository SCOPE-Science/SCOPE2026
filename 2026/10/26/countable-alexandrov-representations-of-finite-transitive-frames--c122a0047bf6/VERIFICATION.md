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

The standalone `checker.py` was run directly from the scientific package source, returning:

`ALL_CHECKS_OK transitive_frames= 4180 counting_and_modal_checks= 779484`

It enumerates every transitive labelled relation with one to four worlds, verifies antisymmetry/transitivity of the proposed finite restriction of the Alexandrov order, and checks the explicit affine formula for counts of lifted successors at two truncations. Positivity of its unbounded coefficient agrees with ordinary Kripke \(\Diamond\) for all source subsets. The irreflexive boundary receives a separate structural test.

The infinite counting argument, preservation of arbitrary modal-formula depth, and the exact single-space logics are mathematical proofs in `RESULT.md`; finite diagnostic enumeration is not a substitute. Established finite-frame completeness of \(\mathsf{K4}\) and \(\mathsf{GL}\) and topological soundness for \(\omega\)-accumulation are cited metatheorems. No independent audit has been performed.
