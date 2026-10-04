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

The analytic verification has two exhaustive steps. First, every positive-definite quadratic pullback is averaged over signed coordinate permutations; invariance of the Lorentz norm preserves the same comparison constants, and the averaged form is scalar Euclidean. Second, on one symmetry sector the radial ratio is
\[
F(s)=\frac{(1+\omega s^q)^{1/q}}{\sqrt{1+s^2}},\qquad 0\le s\le1,
\]
with logarithmic derivative
\[
\frac{F'(s)}{F(s)}=\frac{s(\omega s^{q-2}-1)}{(1+\omega s^q)(1+s^2)}.
\]
For \(1<q<2\) this has the unique interior zero \(s_*=\omega^{1/(2-q)}\), where the radial ratio is maximal. Comparing the two endpoint values \(1\) and \((1+\omega)^{1/q}/\sqrt2\) produces the unique phase boundary \(\omega=2^{q/2}-1\). These steps prove the displayed distance formula for all allowed parameters.

Representative numerical minimizations over unrestricted positive-definite quadratic forms were consistent with the analytic value. Those computations are only a sanity check and are not used to extend a finite sample to the quantified theorem.

Limits: no endpoint, higher-dimensional, complex, or alternate-weight-convention claim is made. Literature checks do not constitute a proof of worldwide novelty; the recorded residual risks remain.
