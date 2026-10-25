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

Run `python verify.py` using only the standard library. Successful output ends `VERIFY_OK`.

The checker computes exact Fourier products over prime fields for eight odd cyclic dihedral quandles with sizes \(3,5,7,9,11,15,17,31\), plus the Alexander automorphism \(t=3\) on \(\mathbb Z/31\mathbb Z\). It checks every predicted orbit as invariant and closed under the dual maps, and verifies that a basis coordinate generates its full orbit. For the noncyclic group \(C_3\times C_3\), it checks 100 exact products and all five dual orbits. In \(\mathbb F_7[R_3]\), it enumerates every reduced-row-echelon subspace over \(\mathbb F_7\): precisely 116 subspaces, of which four are two-sided ideals, with dimensions 0, 1, 2, 3.

These calculations do not enumerate all subspaces in larger examples or prove the unrestricted theorem. The argument in RESULT.md is the general proof. No independent mathematical validation or external certification was performed.
