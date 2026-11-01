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
# Reproduction and verification

The files `verify_tietze_higher_independence.py` and `tietze_higher_independence_certificate.json` are standalone and sufficient for a full finite replay. Run `python3 verify_tietze_higher_independence.py tietze_higher_independence_certificate.json`. There are no optional numerical libraries or external proof checkers. The separate file `tietze_verification_output.txt` contains the actual successful replay output.

The checker verifies independent connectivity-based membership for all 4,096 vertex masks; for every \(r=1,\dots,12\), it enumerates all simplices, replays every matching pair and every Hasse incidence, checks matching acyclicity with a complete DAG topological sort, recomputes the exact signed Morse differential, exact integral rank, determinant-one maximal-rank minor, reduced integral homology and independent mod-two simplicial homology. The computed certificates total 33,248 nonempty faces, 16,345 matched pairs and 184,650 Hasse incidences across the twelve cutoffs. All computed data are compared with the embedded JSON certificate.

Integral homotopy follows from the stated application of Forman's theorem and elementary homotopy cancellation for primitive attachments between simply connected wedge-of-spheres skeleta, not just from field-homology ranks. No larger graph family, cutoffs with different definitions, or filtration inclusion maps are verified.

Successful replay markers: `SAVED_CERTIFICATE_FULL_REPLAY_PASS` and `TIETZE_COMPLETE_HIGHER_INDEPENDENCE_HOMOTOPY_VERIFIED`.
