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

The proof was reconstructed from the actual Green-operator formulas in arXiv:2609.40039v1 rather than inferred from its theorem statement alone.

For the topological fixed point, the stable and unstable integrals were bounded separately, producing \(D\varepsilon_s/\delta_s\) and \(D\varepsilon_u/\delta_u\). Their sum is the displayed contraction factor \(q\).

For the forward Hölder estimate, the source's two branch inequalities were replayed with \(\varepsilon_s\) multiplying the entire stable contribution and \(\varepsilon_u\) multiplying the entire unstable contribution. The projection norm estimate \(\|Pz\|,\|Qz\|\le D\|z\|\) then gives exactly the stated \(K_\alpha\). The invariant-ball radius is \(K_\alpha/(1-K_\alpha)\).

For the inverse, the projected hypotheses imply the full min-bound with coefficient \(\varepsilon_s+\varepsilon_u\). Substitution into the source's Gronwall estimate gives nonlinear-flow growth exponent increments \(2D^2(\varepsilon_s+\varepsilon_u)\). The final stable and unstable inverse Green integrals retain their own coefficients \(\varepsilon_s\) and \(\varepsilon_u\), yielding the displayed inverse Hölder constant.

The strict-gain example was simplified symbolically and uses no approximation:
\[
\frac{1}{1-\alpha}+\frac{1}{1+\alpha}=\frac{2}{1-\alpha^2},
\qquad
\frac{\lambda(1-\alpha^2)/2}{\lambda(1-\alpha)/4}=2(1+\alpha).
\]

Limits: the result is a sufficient criterion in the classical trivial-bundle setting. No optimality, necessity, or full abstract-bundle extension is verified. The 2011 comparison source was available only through its abstract and bibliographic record, which remains an originality risk.
