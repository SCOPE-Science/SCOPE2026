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

The proof is analytic. The executable check `verify.py` is supplementary and uses only the Python standard library.

For each tested \(\kappa>1\), the script solves
\[
y-\log y=1+\log\kappa,
\qquad y>1,
\]
by bisection. It then checks the equivalent stationary equation, the identities
\[
\theta_\kappa=\frac{y}{y-1},
\qquad
m(\kappa)=1-e^{-y}=1-\left(\frac{\theta_\kappa-1}{\kappa\theta_\kappa}\right)^{\theta_\kappa},
\]
and strict improvement over nearby shape values. For small \(q=\sqrt{2\log\kappa}\), it checks that the errors after the displayed truncations are consistent with \(O(q^3)\) for \(\theta_\kappa\) and \(O(q^4)\) for \(m(\kappa)\).

The script also checks the exact complement identity
\[
1-m(\kappa)=\frac{1}{e\kappa y}
\]
for large \(\kappa\). These finite checks do not certify uniqueness or asymptotic validity; those facts are established in the proof by monotonicity and local series inversion.

Scientific limits: the result concerns the Pareto type-I finite-mean regime and fixed \(\kappa>1\). No independent audit has been performed.
