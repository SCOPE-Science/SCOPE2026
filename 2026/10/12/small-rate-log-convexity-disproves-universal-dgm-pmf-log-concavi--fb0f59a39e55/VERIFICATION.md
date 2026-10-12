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
The DGM survival and PMF are
\[
S_z=
\exp\!\left[
-\alpha z-\frac{\theta}{\mu}(e^{\mu z}-1)
\right],
\qquad
p_z=S_z-S_{z+1}.
\]

Under
\[
\alpha=\varepsilon a,\qquad
\theta=\varepsilon b,\qquad
r=e^\mu,\qquad
c=\frac{b}{\mu}(r-1),
\]
the exact one-step cumulative hazard is
\[
-\log(S_{z+1}/S_z)=\varepsilon(a+c r^z).
\]
For fixed \(z\),
\[
p_z=\varepsilon(a+c r^z)+O(\varepsilon^2).
\]
Therefore
\[
p_z^2-p_{z-1}p_{z+1}
=
-\varepsilon^2 a c r^{z-1}(r-1)^2+O(\varepsilon^3).
\]
The coefficient is strictly negative for every \(a,c>0\) and \(r>1\).

The bundled checker specializes to
\[
\mu=\log2,\qquad
\alpha=\varepsilon,\qquad
\theta=\varepsilon\log2,
\]
where
\[
S_z=e^{-\varepsilon(z+2^z-1)}.
\]
It verifies the negative determinant at \(\varepsilon=0.01\) and checks convergence of the normalized determinant to \(-1\) as \(\varepsilon\downarrow0\).

The computation is only a replayable consistency certificate. The low-rate counterexample family is proved by the expansion above.
