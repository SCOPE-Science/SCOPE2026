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

The proof is analytic. Its critical chain is:

1. Specialize the published exact symmetric-chain dispersion relation to \(A\in\mathbb Z+\tfrac12\), obtaining the exact non-flat band condition
\[
|\sin(\pi k)|\le\frac{2k\ell}{k^2\ell^2+1}.
\]
2. On each side of a sufficiently large integer \(n\), monotonicity gives exactly one edge and the scalar equations
\[
\sin(\pi\delta_n^\pm)=\frac{2(n\pm\delta_n^\pm)\ell}{(n\pm\delta_n^\pm)^2\ell^2+1}.
\]
3. The right-hand side is \(2/(\ell n)+O(n^{-3})\) because \(\delta_n^\pm=O(n^{-1})\). Combining this with \(\arcsin x=x+O(x^3)\) gives \(\delta_n^\pm=2/(\pi\ell n)+O(n^{-3})\).
4. The \(n^{-3}\) width remainder is summable, giving the logarithmic momentum law. Under \(E=k^2\), each complete band has width \(8/(\pi\ell)+O(n^{-2})\); summing the convergent remainder gives the \(\sqrt E\) law.

`verify.py` independently solves the exact scalar boundary equations for representative \(\ell\) and \(n\), checks the residuals, and confirms convergence of the scaled momentum and energy widths. It does not certify the infinite statement and is not a substitute for the proof.
