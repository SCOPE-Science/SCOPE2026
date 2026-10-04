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

The proof is analytic and has no external numerical certificate dependency.

For \(m\le c\sigma_q<m+1\), exact summation gives \(1-2q^{m+1}/(1+q)\). The band boundary \(c\sigma_q=s\) is parameterized by \(q_s=e^{-2t_s}\) with \(t_s=\operatorname{arsinh}(c/(\sqrt2 s))\). The complementary boundary mass is \(T_s=e^{-(2s-1)t_s}/\cosh t_s\), and
\[
\frac{d}{ds}\log T_s=-2t_s+\frac{2s-1+\tanh t_s}{s}\tanh t_s< -2t_s+2\tanh t_s<0.
\]
Thus all higher lattice bands have strictly larger infima than the first band. At the first boundary, \((1-q_1)/(1+q_1)=\tanh t_1=c/\sqrt{c^2+2}\). The closed event jumps upward when the atoms at \(\pm1\) enter, whereas the open event excludes them and attains the boundary value.

Finite numerical stress tests were used only to look for counterexamples before acceptance; they are not evidence for the universal quantifiers.
