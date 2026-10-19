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

# Verification details

The stationary joint-law construction was checked for shift equivariance and for a common fixed probability law at every site. The key estimate was reconstructed from the conditional probabilities \((1-\varepsilon){\bf1}_{\{|X_j-z_j|\le r\}}+\varepsilon\operatorname{Leb}([z_j-r,z_j+r]\cap[0,1])\) without assuming coordinate independence of the stationary input.

A deterministic all-half input attains the exact finite-cylinder factor \(1-\varepsilon+2r\varepsilon\) at every coordinate; a deterministic all-zero input attains \(\bar d_1=\varepsilon/2\) under every joining. These are separate sharpness witnesses. The entropy proof uses conditional independence of the binned outputs given the full input block and yields \(H_\varepsilon(M)\) for every \(M\ge2\).

The included `check.py` has no nonstandard dependencies; running `python check.py` passed 1,848 exact-rational finite-window/bound instances and 15 floating-point positivity diagnostics for coarse partition entropy. The finite checks do not establish ergodicity, infinite entropy or limiting expansivity; those are proved in `RESULT.md`.

Scientific bounds: \(\varepsilon\in(0,1]\), \(r\in(0,1/2)\), \(N\in\mathbb Z_{\ge0}\). The exact upper bound is for coordinate cylinders, with an inclusion yielding zero infinite Bowen-ball mass. The output has infinite entropy for every positive refresh rate, irrespective of input entropy. No independent audit has been performed.
