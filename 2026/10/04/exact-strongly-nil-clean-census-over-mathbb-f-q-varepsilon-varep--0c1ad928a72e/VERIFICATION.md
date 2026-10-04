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

The symbolic verification has four steps.

1. A strongly nil-clean residue matrix has a commuting idempotent, hence a direct sum of a generalized \(1\)-primary block \(I+N_1\) and a generalized \(0\)-primary block \(N_0\). Conversely, the coprime primary decomposition for \(t\) and \(t-1\) constructs that commuting idempotent.
2. For a dual lift \(A+\varepsilon B\), the off-diagonal correction equations are Sylvester equations between the \(1\)-primary and \(0\)-primary blocks. Their minimal polynomials are coprime, so the Sylvester map is invertible over every field. Thus every \(B\) lifts.
3. For fixed generalized \(1\)-primary dimension \(r\), count ordered decompositions by \({n\brack r}_q q^{r(n-r)}\), then use the classical \(q^{m^2-m}\) count for each nilpotent block and multiply by \(q^{n^2}\) arbitrary dual coefficients.
4. Summing over \(0\le r\le n\) gives the displayed formula.

`verify_count.py` independently exhausts the residue matrices for six small prime-field cases and compares the brute-force count to the formula. Its captured output ends in `CHECK_OK`. These finite cases are consistency checks only; no finite enumeration is used to prove the arbitrary-prime-power statement.
