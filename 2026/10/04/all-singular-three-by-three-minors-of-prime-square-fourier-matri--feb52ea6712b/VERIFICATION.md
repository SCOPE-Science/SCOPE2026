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

The theorem is established by the symbolic proof in `RESULT.md`. The executable check is corroborative.

`verify.py` uses exact integer coordinates in the cyclotomic basis for a primitive \(p^2\)-th root, with reduction by \(\Phi_{p^2}(X)=1+X^p+\cdots+X^{(p-1)p}\). It checks every pair of translation-normalized three-subsets for \(p=3\) and \(p=5\); every translation orbit has a representative containing \(0\), and translating either row or column indices changes a minor only by nonzero diagonal phase factors.

For each pair it computes the determinant exactly, computes the rank using exact two-by-two minors when the determinant vanishes, and compares with the residue-occupancy prediction. It also enumerates all three-subsets for the same primes to check the closed formulas for type-B and type-C counts.

The finite replay does not prove the theorem for all primes; the infinite conclusion rests on the symbolic case analysis. A successful run prints `VERIFY_OK`.
