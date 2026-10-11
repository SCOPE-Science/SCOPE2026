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

For normalized
\[
p(z)=1+a_1z+\cdots+a_{n-1}z^{n-1}+z^n,
\]
the polar factor is
\[
q(z)=p(z)-\frac{zp'(z)}n
=1+\sum_{j=1}^{n-1}\left(1-\frac jn\right)a_jz^j.
\]
Thus \(q\) is constant exactly for the binomial extremal.

For simple boundary zeros and \(r=2a>0\), the checked primary identity is
\[
\mathcal P_{2a}
=
\frac{M_{Q_n}(2a)}{an}
\int_{\mathbb D}
\operatorname{Re}H_a(B(z))
|(q^a)'(z)|^2\,dA(z),
\]
with
\[
\operatorname{Re}H_a>0
\]
in \(\mathbb D\). The root-splitting approximants satisfy \(|B(z)|\le|z|\). On any compact disk where the limiting \((q^a)'\) is bounded away from zero, the integrands therefore admit a uniform positive lower bound. This supplies strictness after passage to repeated roots.

For \(0<a\le1\), the checked kernel estimate is
\[
\operatorname{Re}H_a(w)
\ge
\frac1{a+1}
\left(1-\sum_{k\ge1}\frac{|w|^k}{k(k+1)}\right).
\]
The radial integral used in the coefficient bound is
\[
\int_0^1
\frac1{a+1}
\left(1-\sum_{k\ge1}\frac{\rho^k}{k(k+1)}\right)
\rho^{2m-1}\,d\rho
=
\frac{H_{2m}-1}{2m(2m-1)(a+1)}.
\]
The packaged symbolic checker verifies the partial-fraction identity behind this formula and the resulting constant.

The proof does not infer strictness from numerical experiments. The only computation is an algebra audit of a closed-form sum; positivity and multiplicity passage are analytic.
