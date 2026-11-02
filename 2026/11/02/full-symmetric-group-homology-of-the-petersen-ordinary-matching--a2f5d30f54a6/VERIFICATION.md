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

The included `petersen_matching_s5_verify.py` is a Python 3 standard-library exact checker. It enumerates all 331 oriented nonempty simplices, constructs full signed cyclic invariant bases for all seven permutations' cycle types, calculates reduced rational Betti numbers of the invariant chain complexes using exact `fractions.Fraction` Gaussian elimination, and then reconstructs the homology characters by induction on element orders. It also independently verifies signed fixed-simplex Lefschetz numbers, and averages the character values over all 120 permutations to compute full and alternating symmetry invariants.

Reproduce with `python3 petersen_matching_s5_verify.py`; compare standard output byte-for-byte to the embedded `petersen_matching_s5_verification.txt`. The expected final marker is `PETERSEN_MATCHING_S5_EXACT_OK`. No random sampling, floating point or external package is involved.

The computed face vector is `(15,75,145,90,6)`, and the identity boundary ranks in degrees one through four are `(14,61,79,6)`. The resulting reduced rational homology is five-dimensional in each of degrees two and three and zero otherwise. The recovered characters on the seven conjugacy classes are exactly `(5,-3,1,2,0,-1,0)` and `(5,1,1,-1,1,-1,0)`, respectively. For the group quotients, averaging gives invariant dimensions `(0,0)` for the full symmetric group and `(1,0)` for the alternating group in degrees two and three.

This is a finite self-contained mathematical verification of rational ranks and characters, not an integral equivariant chain-lattice classification and not an independent scientific audit. The published nonequivariant integral homotopy type is cited separately and not presented as new.
