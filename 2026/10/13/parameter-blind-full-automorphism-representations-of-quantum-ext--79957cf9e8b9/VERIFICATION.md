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

# Reproducibility

Run `python3 verify.py` with Python 3 standard library in the directory containing this file. The script represents \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_9\) by explicit irreducible-polynomial quotient arithmetic and uses ordinary modular arithmetic for the other fields. It independently enumerates all admissible images of the two generators and all finite-dimensional radical subspaces, rather than merely iterating the claimed automorphism normal form. It verifies the group representation for every generic parameter and independently computes the fixed-space histogram, complete element orbits, ideal count, and ideal orbit partition.

Observed field orders: \(4,5,7,8,9\). Observed automorphism orders: \(144,400,1764,3136,5184\). Observed fixed-dimension distributions \((N_1,N_2,N_3,N_4)\): \((32,96,15,1)\), \((150,225,24,1)\), \((980,735,48,1)\), \((1920,1152,63,1)\), \((3402,1701,80,1)\). Full element-orbit counts: \(20,25,35,40,45\); ideal-orbit count \(7\) in each case. Successful termination prints `VERIFY_OK`.

Finite-field enumeration does not certify the universal statement. The universal result is supported by the explicit filtration, monomial-matrix and orbit proofs in `RESULT.md`; no machine-formal proof or independent human audit is claimed.
