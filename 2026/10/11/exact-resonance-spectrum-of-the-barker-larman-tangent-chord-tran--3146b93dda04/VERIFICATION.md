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

Let
\[
F(s,\varepsilon)
=
\sqrt{1+s^2}
-
R
-
\varepsilon f(\theta+\arctan s).
\]
At the unperturbed section endpoints
\[
s=\pm S,
\qquad
S=\sqrt{R^2-1},
\]
the derivative
\[
F_s=\pm S/R
\]
is nonzero. The packaged checker applies the implicit-root formula and recovers
\[
s_+'(0)=\frac RS f_+,
\qquad
s_-'(0)=-\frac RS f_-.
\]
It then verifies
\[
D T_R[f]
=
\frac RS(f_++f_-).
\]

For the second-order coefficient, the exact root expansion gives
\[
s_+
=
S
+
\varepsilon\frac RS f_+
+
\varepsilon^2
\left(
\frac{f_+'f_+}{S^2}
-
\frac{f_+^2}{2S^3}
\right)
+
O(\varepsilon^3)
\]
and
\[
s_-
=
-S
-
\varepsilon\frac RS f_-
+
\varepsilon^2
\left(
\frac{f_-'f_-}{S^2}
+
\frac{f_-^2}{2S^3}
\right)
+
O(\varepsilon^3).
\]
Subtracting reproduces the coefficient used in the proof.

The Fourier multiplier is
\[
\lambda_k(R)=\frac{2R}{S}\cos(k\beta).
\]
For reduced
\[
\beta/\pi=a/b,
\]
the checker exhaustively verifies on a finite integer range that multiplier zeros occur exactly when \(b\) is even and \(k\) is an odd multiple of \(b/2\). The universal classification itself is proved arithmetically, not by enumeration.

Finally, substituting a resonant harmonic with
\[
k\beta\equiv\pi/2\pmod\pi
\]
makes the linear term and derivative-product part vanish and leaves
\[
-\frac{\sin^2(k\theta)}{S^3}.
\]

The computation certifies algebraic identities only. Convexity, the full frequency classification, and the uniform remainder are analytic parts of the proof.
