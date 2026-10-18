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

## Executed checks
The standalone commands `python3 verify_paley13.py` and `python3 verify_alexander_dual.py` completed successfully from the actual files included in this package, and their output matched `expected_output.txt` and `expected_dual_output.txt`, respectively. No third-party dependencies, external data files or remote services are required.

The first program reconstructs Paley adjacency from the six nonzero quadratic residues of \(\mathbb F_{13}\); verifies parameters \((13,6,2,3)\); exhausts all \(\binom{13}{3}=286\) triples; constructs every nonempty face of the ordinary three-cut complex; and verifies the complete face-count vector, \(3,936\) matching pairs, \(50,076\) covering incidences and directed acyclicity across all \(7,878\) simplices. Its exact integer reduction gives two equal boundary columns \((-1,-1,1)\).

The independently written second program enumerates the Alexander-dual faces directly by requiring every induced triple to be connected. Its augmented face vector is \((1,13,78,143,78)\); modular boundary ranks \((12,66,76)\) agree over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{101}\).

## Meaning and limits
The full integral homotopy conclusion uses the acyclic discrete-Morse theorem and the primitive integral attaching matrix, **not** merely Euler characteristics or several finite-field checks. The modular computation provides a structurally distinct corroboration of Betti ranks. The literature comparison could miss unindexed equivalent works; no independent external mathematical audit has been performed.
