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

# Verification and reproducibility

For the exact game equations and positive parameters, differentiation gives \(\ddot z=[S_\lambda'(z)-1]\dot z-\alpha[S_\lambda(z)-1/2]\). Thus \(f_\lambda(z)=1-S_\lambda'(z)\), \(g=\alpha(S_\lambda(z)-1/2)\). These are exact identities, checked numerically and independently by differentiating the explicit logistic function.

At the critical parameter, \(f_4(z)=\tanh^2(2z)\). The Lyapunov energy is proper, and no nonconstant complete trajectory lies in the \(\dot E=0\) set. Above criticality, \(F=z-\tfrac12\tanh(\lambda z/2)\) has a unique positive zero; existence, uniqueness and stability use the classical Liénard theorem, not simulation.

For the amplitude, the calculation retains terms through \(\delta A^2\) and \(A^4\) in mean energy drift; the result is \(\delta\alpha A^2/8-\alpha A^4/2\). These coefficients follow from the exact derivatives \(S_\lambda'(0)=\lambda/4\) and \(S_\lambda^{(3)}(0)=-\lambda^3/8\). The cycle expansion is local and requires \(\alpha>0\) fixed. The included program `verify.py` reports computed amplitudes at finite, not infinitesimal, \(\delta\), so small finite residuals are expected.

To reproduce: use Python 3.10 or later and `pip install -r requirements.txt`, then run `python verify.py`. All files are present in this package. Numerical checks provide consistency only, not independent proof of global dynamics, nonexistence, or parameter-uniform asymptotics.
