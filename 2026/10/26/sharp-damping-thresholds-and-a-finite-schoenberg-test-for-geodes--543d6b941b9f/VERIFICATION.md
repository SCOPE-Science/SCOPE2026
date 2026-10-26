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

# Checks and limits

The analytical proof derives the normalized Schoenberg coefficient and checks that the rational denominator is nonzero for every \(a>0\) and \(\omega\ge0\). Sign reduction to the quadratic polynomial is exact. The finite test covers negative, zero, and positive leading coefficients with equality, and strictness uses infinite positivity of both parity tails. At integer frequency \(m\), direct algebra establishes
\[
\operatorname{Re}(z\overline{Q_z(X)})=a[(X+a^2+m^2-1)^2+4(a^2+m^2)(1-m^2)],
\]
whose derivative in the bracket is positive for \(X\ge1\). The value at \(X=1\) is \(a(a^2+m^2)(a^2+4-3m^2)\). These identities were independently expanded symbolically.

Running `python3 check.py` gives 40 Simpson integration comparisons against the explicit harmonic coefficients, 500 deterministic finite-sign comparisons against degrees \(0\) to \(899\), and 20 integer-boundary-side tests. The executed checks passed. They are finite diagnostics and not proofs for all degrees or equality under rounded arithmetic. No independent audit or independent validation has been performed.
