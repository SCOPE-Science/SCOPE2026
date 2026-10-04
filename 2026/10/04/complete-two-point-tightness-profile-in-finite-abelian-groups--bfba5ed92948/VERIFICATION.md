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

The proof was replayed from the normalized matrix
\[
T_\zeta=
\begin{pmatrix}
1&1\\
1&\zeta
\end{pmatrix}.
\]
Its Gram matrix has eigenvalues
\[
2-|1+\zeta|\quad\text{and}\quad2+|1+\zeta|,
\]
so the set-level problem is exactly the minimization of
\[
|\cos(\pi k/m)|
\]
over \(m\)-th roots of unity. The minimum is \(0\) for even \(m\) and \(\sin(\pi/(2m))\) for odd \(m\).

The accompanying `verify.py` was executed from its packaged path and returned `VERIFY_OK`. It exhaustively checks all two-point subsets and all two-character partners in the listed finite abelian groups, then compares the independently optimized numerical quantities with the closed formulas. This finite computation is not used as proof of the universal statement.

The first-public-date field uses the initial arXiv posting date, 2019-04-09, not the 2021 revision date.
