---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Tridiagonal determinant recurrence yields J^N(U_N(lambda/2J)+i g U_{N-1}(lambda/2J)). Every eigenvalue has strictly negative imaginary part by terminal nonzero eigenvector component. Substitution lambda=-2iJ sinh u yields g=cosh((N+1)u)/sinh(Nu) for even N, and g=sinh((N+1)u)/cosh(Nu) for odd N. The even log has strictly positive second derivative and one minimum; the odd function is strictly increasing. Nonvanishing second derivative at the minimum implies algebraic multiplicity exactly two; irreducible tridiagonal eigenspace dimension one implies a defective second-order EP. Pointwise monotonicity in real N and exponential q_N=e^(-2Nu_N) imply q_N~1/(4N) and the stated logarithmic threshold correction. Independent finite matrix/Chebyshev eigenchecks returned g2=2,g4=1.55302604,g6=1.39202881,g100=1.03542380. The claims are only on the negative imaginary axis; no global off-axis collision assertion.

## originality

PASS

Earlier localized-loss tight-binding work already discusses an edge impurity and an associated EP; this fact is explicitly credited, including Burke–Wiersig–Haque (2019, Appendix D) and Wiersig (2018). The remaining claim is exact all-N parity root-count classification and sharp logarithmic finite-length threshold, neither furnished by the read Appendix D or other inspected material. This is a substantially qualified PASS with direct same-model priority risk, not a claim to have discovered edge-loss EPs.

## value

PASS

The exact all-length parity selection, unique finite-length EP and logarithmic correction determine a physically natural absorbing-boundary spectral boundary with analytic sharp constant; the two-site example and generic EP existence alone are not claimed new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
