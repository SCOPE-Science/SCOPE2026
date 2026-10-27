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

The standalone `verify_lines.py` requires Python 3 with no additional packages. Running `python3 verify_lines.py` from the directory containing this file returns `VERIFY_OK Grassmann=5797 F4_lines=8 graph=2K3+2K1 Frobenius=2^4 F2_lines=0 points=(9,81) split_planes=2`.

The two exact enumeration methods are (i) all \(5797\) reduced-row-echelon two-dimensional subspaces of \(\mathbf F_4^5\), with coefficient-by-coefficient cubic substitution, and (ii) pairs of \(\mathbf F_4\)-projective points on the cubic, deduplicated by the five-point set defining their line. Rank, Frobenius, distinct triangle vertices, and split-plane identities are checked separately. The proof does not extrapolate finite data to geometric lines over larger fields.

The equations, complete finite classification and explicit line bases are given in `RESULT.md`. Scientific originality remains subject to further literature scrutiny, and independent audit has not been performed.
