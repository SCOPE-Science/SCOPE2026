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

# Exact verification and limits

Run `python3 verify.py` using a standard Python 3 installation. No third-party libraries are required. The checker explicitly enumerates all \(120\) permutations of five residue classes, reduces their affine-equivalent directions to six classes, verifies the defining power sums in \(\mathbb F_5\), computes the degree-zero through degree-three evaluation ranks \((1,3,5,6)\), tests the nondegeneracy of the quadratic, and checks the full permutation-group orbit and stabilizer. The expected terminal marker is `VERIFY_OK`.

The exact script is finite arithmetic, while the proof of the scheme-theoretic decomposition and normalization defect is algebraic and given in RESULT.md. No formal proof assistant or independent external review was employed. Historic priority has not been independently certified.
