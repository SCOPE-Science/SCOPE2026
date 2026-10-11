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

The argument is analytic and uses no finite experiment as proof.

The source identities checked directly are:

1. The balance law is
\[
Y_0'=-\frac1k\Lambda_\alpha Y_0+f_{\alpha,k}(Y_0).
\]
2. Quasi-homogeneity gives, componentwise,
\[
f_{\alpha,k}(s^{\Lambda_\alpha}Y)=s^k s^{\Lambda_\alpha}f_{\alpha,k}(Y).
\]
3. Under full rank of \([Y_0',\Lambda_\alpha Y_0]\), the source's Corollary 4.5 gives multipliers \(1\) and \(e^{T_\eta}>1\).
4. The source's Theorem 5.1 converts a simple unit multiplier and absence of any other unit-circle multiplier into a finite-time type-I periodic blow-up.

For the new rank step, suppose dependence holds for every time. Positivity of \(p_\alpha(Y_0)\) implies \(\Lambda_\alpha Y_0\neq0\), hence \(Y_0'=a\Lambda_\alpha Y_0\). Integration gives \(Y_0=s^{\Lambda_\alpha}Y_0(0)\). Evaluating the balance law at the initial point gives \(f_{\alpha,k}(Y_0(0))=b\Lambda_\alpha Y_0(0)\). Quasi-homogeneity then makes the entire scaling ray invariant and reduces the profile to
\[
u'=-\frac1k+b e^{ku},\qquad u=\log s.
\]
A nonconstant periodic orbit of this scalar autonomous equation is impossible. Because the original profile is periodic and has a nonzero positively weighted coordinate, its scaling factor must return to \(1\) after one period. Therefore persistent dependence contradicts nonconstancy.

Once independence occurs at one time, the source propagates it to all times. In two dimensions the distinguished invariant subbundle is the whole variational space, so no unexamined quotient multiplier remains.

Limit: this verification does not prove existence of the periodic balance profile and does not extend the spectral exhaustion to dimensions greater than two.
