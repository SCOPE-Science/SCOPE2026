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

The proof is analytic, not a finite search. Its critical checks are: (i) obtain \(N(z)=\sup\sigma(J(|z|))\) by phase alignment and Rayleigh quotients; (ii) compute every path-block eigenpair with sine functions, including the infinite path limit; (iii) use the uniform gap \(\delta_m>0\) and the orthogonal decomposition of unit test vectors to control the spectral perturbation remainder by \(O(\|h\|_\infty^2)\); (iv) select a single maximizing run in the tied case and two opposite-signed families of unbounded lengths in the infinite case. The displayed derivative uses the real part of complex perturbations and includes unrestricted perturbations at zero-weight coordinates.

As an illustrative supplementary finite check, a 47-edge model with a unique four-edge run and a two-edge competitor gave numerical radius \(\cos(\pi/6)\). Finite-dimensional symmetric-eigenvalue calculations with perturbation norms \(0.01,0.001,0.0001\) yielded remainders approximately \(3.43\cdot10^{-6},5.03\cdot10^{-8},2.24\cdot10^{-9}\), respectively; the perturbation direction differed between trials. Adding a second tied four-edge run gave one-sided directional slopes \(0.8660254\) and \(0\). These checks are illustrative only; they cannot validate the universal infinite-dimensional statement.

There is no machine-generated universal certificate, and no independent audit or independent validation has been performed. The limitation to binary base weights is essential to the run-length formula.
