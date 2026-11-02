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
# Reproducibility and verification

Run `python3 verify.py` from the extracted files. Only Python 3's standard library is needed; all matrix entries and Schur complements are exact rational numbers. The script constructs the full vertex distance matrix independently of the two-dimensional proof reduction, and builds the Gram matrix for the \(N-1\) difference vectors relative to one basepoint.

The exact positive-semidefiniteness criterion is tested at rational \(t=2^p\) values against the determinant prediction for 1,320 distinct graph/power cases (up to eleven vertices). A separate 10,469-case grid checks the integer \(p=1\) threshold. All graph profiles up to nine vertices are also exhaustively scanned within the specified family to confirm that the first failing profiles are precisely \((4,2,3)\) and \((5,2,2)\) up to exchange. All assertions passed.

The general theorem is proved symbolically in `RESULT.md` and is **not** inferred from the finite tests. In particular, no empirical finite matrix census establishes absence of larger exceptions, and none is claimed. The scientific evidence does not include a separately performed independent audit.
