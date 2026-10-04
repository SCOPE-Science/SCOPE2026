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

The proof was checked at three levels. First, the source equation was algebraically rewritten as \((s^2-3t^2)(u^2-3v^2)=4t^2v^2\), and the zero/pole orders of \((s^2-3t^2)/t^2\) on the smooth \((2,2)\)-curve were tracked using this identity. This yields the principal divisor \(2B_\infty-2A_\infty\) and hence the equality of the two squared projection line bundles.

Second, the incidence surface was reconstructed from the two quadratic parametrizations. The two endpoint line subbundles have degrees \(-4\) and \(-4\), so the tautological hyperplane square on their projectivization is \(8\). The published image degree is also \(8\), forcing generic degree one. Three explicit stationary-bisecant parameters rule out a common vertex, hence rule out contracted horizontal curves. Proper plus quasi-finite gives finite, and finite birational from the smooth incidence surface gives the normalization.

Third, `artifacts/verify.py` checks the factor identity, the explicit ruling witnesses, and the exact cross-ratio relation from the four branch points and the \(\mathbb Q(\sqrt5)\) simplification of the branch-point formula to \(24918016/45\). The checker is finite arithmetic support for the displayed symbolic proof; it is not used as a substitute for the normalization argument.

The result does not determine all local analytic singularity types of the image and does not generalize the product conclusion beyond the named example.
