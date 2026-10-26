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

Analytic identities were checked symbolically using SymPy: the two rank-two characteristic polynomials, their discriminants, and the rank-one dipole polynomial. The separate Python program \(\texttt{verify\_quadrupole.py}\) assembles each full spin-\(j\) superoperator without relying on the reduced block matrices, extracts its adjoint-Casimir rank-two subspace and compares its five eigenvalues with the explicit two-plus-three block decomposition. The five spin sizes \(j=1,3/2,2,5/2,3\) and eleven rate values yield 55 comparisons; the worst numerical discrepancy is \(7.35\times10^{-8}\) near an exceptional point. At \(\eta=2.5\), the dipole spectrum is entirely real and the quadrupole even block has two nonreal eigenvalues.

The all-spin assertion is certified only by the exact adjoint-representation argument and algebraic sign analysis in RESULT.md, not by finite samples. The script requires Python, NumPy and SymPy and does not perform independent auditing, priority certification, or experimental validation.
