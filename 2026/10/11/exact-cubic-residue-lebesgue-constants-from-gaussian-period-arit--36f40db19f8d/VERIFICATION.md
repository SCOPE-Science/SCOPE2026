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

The universal proof is symbolic. The critical steps are:

1. Fourier inversion turns the multiplier \(1_H\) into normalized convolution with \(K(x)=\sum_{h\in H}e^{2\pi i hx/p}\).
2. Multiplicative-coset invariance gives one kernel value for each of the three nonzero cubic-residue cosets, each repeated \((p-1)/3\) times.
3. The cubic Gaussian-period equation supplies the three elementary symmetric functions.
4. The substitution \(X=Z-1/3\) yields \(Z^3-pZ/3-pL/27=0\), giving the stated trigonometric roots.
5. The sign of the product, together with the negative second symmetric sum, determines whether there is one positive period or one negative period. This resolves the absolute values exactly.
6. Endpoint convolution norms equal normalized kernel total variation, yielding the two formulas.

The standalone `verify.py` is a finite corroboration. It enumerates all primes \(p\equiv1\pmod3\) below \(1001\), constructs the periods directly, and checks the polynomial coefficients, root formula, branch signs, and direct kernel norm. Its replay output is:

`VERIFY_OK primes=80 one_positive=43 one_negative=37 max_norm_err=4.690e-13 max_poly_res=4.087e-11 max_imag=3.120e-11`

The numerical tolerances account only for floating-point evaluation of roots of unity. The theorem for arbitrary primes does not depend on this finite computation.
