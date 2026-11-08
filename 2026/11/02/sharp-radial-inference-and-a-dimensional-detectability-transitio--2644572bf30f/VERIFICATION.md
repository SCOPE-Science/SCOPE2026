---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The stationary on/off switching model uses a single common Markov switch and Brownian coordinates with dimensionless Z=sqrt(k/D)X. Conditional on past switch path, Z is N_d(0,(1+V)I), with V governed by −V in the on state and +1 in off; its joint stationary densities obey p_off(v)=v p_on(v), with p_on proportional to v^(a−1)exp(−bv), a=q_on/(2k), b=q_off/(2k). Thus the exact posterior odds R_d(r)=E[V| ||Z||=r] compare integrated Gaussian kernels including stationary priors. Covariance differentiation with −1/[2(1+V)] proves strict radial increase for r>0; covariance with log(1+V) proves R_d(0) strictly decreases in real d. Its d=0 value a/b and d→∞ value 0 give the unique critical d_c if a>b and the all-d radial crossing if a<=b. A large-r Laplace saddle makes R_d→∞. At r²=2d+c+h/d, v=1+z/sqrt d, saddle Gaussian z~N(0,8); direct symbolic expansion yields R−1=[8(a−b)+c]/d +[16(a−b)+h−16]/d²+O(d^-3) after c=8(b−a). Hence threshold r_d²=2d+8(b−a)+16(1+b−a)/d+O(d^-2). An independent SymPy expansion and Gaussian-moment evaluation confirmed these algebraic coefficients; independent SciPy quadrature at d=100,300,800 and multiple (a,b) corroborated thresholds (finite diagnostics only). Conditional LLN ||Z||²/d→1+V then gives the positive gamma-mixture Bayes-error limit, including (1−e^-1)/2 at a=b=1. There is no assertion of full temporal-path inference or rates growing with dimension.

## originality

PASS

Stationary fluctuating-trap Gaussian/gamma-mixture laws are known from Frydel and Santra–Das–Nath; they are not presented as original here. The new claim concerns the optimal decision about the current latent switch from one d-vector snapshot, exact threshold transition in d, two correction coefficients and nonzero high-dimensional Bayes error. Inspected primary literature did not identify these inference formulas. The highly relevant July 2026 Frydel age-structured manuscript was found but its complete full text could not be accessed through lawful open routes and authorized institutional access; its possible implicit coverage remains material risk, not automatic failure.

## value

PASS

This is a motivated inference problem: high d nearly identifies a common random variance but never fully resolves which hidden switching state generated that variance. The monotone likelihood ratio and a critical dimension classify every finite d, while the two-correction threshold and exact positive error floor explain a sharp detectability limitation. The object, parameters and asymptotic invariant have natural probabilistic meaning; the stationary mixture alone is not the asserted contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
