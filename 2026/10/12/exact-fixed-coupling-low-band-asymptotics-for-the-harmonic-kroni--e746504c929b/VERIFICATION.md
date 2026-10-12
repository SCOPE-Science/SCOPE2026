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

The proof uses the exact parity-resolved band-edge equations from arXiv:2610.00879v1 and the large-positive-argument Kummer expansion in DLMF §13.7.

For \(n=2m\), the source-normalized even solution at \(E=2n\) has leading decaying coefficient \((-1)^m2^{2m}m!/(2m)!\), while its energy derivative has leading growing coefficient \((-1)^{m+1}\sqrt\pi\,m!/4\). Their quotient yields \(2^{n+2}/(\sqrt\pi\,n!)\).

For \(n=2m+1\), the corresponding odd coefficients are \((-1)^m2^{2m+1/2}m!/(2m+1)!\) and \((-1)^{m+1}\sqrt{2\pi}\,m!/8\), yielding the same \(2^{n+2}/(\sqrt\pi\,n!)\).

The decaying logarithmic derivative is \(-a+n/a+O(a^{-3})\); the growing energy-derivative logarithmic derivative is \(a-(n+1)/a+O(a^{-3})\). Therefore the Robin-to-Dirichlet displacement ratio is
\[
\frac{-a+\gamma+n/a+O(a^{-3})}{a+\gamma-(n+1)/a+O(a^{-3})}=-1+\frac{2\gamma}{a}+O(a^{-2}).
\]

The included checker was replayed from its packaged path. It verifies the parity prefactor identities over several integer indices and checks that the first-order quotient residual scales as \(O(a^{-2})\) for representative fixed parameters. These finite checks are corroborative only.

Limit: the result is proved for each fixed \((n,\gamma)\). It does not establish a uniform band asymptotic when either parameter grows with \(a\).
