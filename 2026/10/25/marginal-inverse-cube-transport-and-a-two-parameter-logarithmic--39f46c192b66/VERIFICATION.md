---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the defined one-sided integral, v_p²=S_p′²/(2ζ(p)S_p). Put L=log t, k_t=(2ζ(3)/(γtL))^(1/2), and H_ε(x)=∫_0^x exp(−εv)dv. Splitting the two sums at n≤1/k gives leading terms k²H_ε(log(1/k))/2 and kH_ε(log(1/k)), with errors O(k²+k^(2+ε)) and O(k+k^(1+ε)). At k=k_tu, H_(s/L)/L tends locally uniformly to Φ(s)/2. Thus the collision exponent tends to Φ(s)u² and the moving velocity square divided by L tends to Φ(r)/(2ζ(3)). To justify uniform tails, for k≤t^(−1/4) the lower harmonic sum gives H_ε≥c_K L for |ε|≤K/L, hence an exp(−c_Ku²) bound. On k≥t^(−1/4) the n=1 collision term gives exp(−c√t). The derivative split and the sum lower bound give v²≤C(1+H_ε) for small k, using exp(−εx)≤1+|ε|H_ε(x); at u≤1 its L-normalized bound is C_K(1+|log u|)u^(−1/2) for large t, and at u≥1 it is bounded. For fixed δ in (2,3), separate convergent Riemann sums for Sδ and Sδ′, with integration by parts on their coefficients, give v²∼Zδ k^(δ−3), an integrable power; at and above 3 use the logarithmic and finite-second-moment limits. These bounds justify the Gaussian/Mellin integration uniformly on compact parameter sets, which recovers all fixed amplitudes and both ratios with the stated factors of 2. No quadrature is needed to establish the limits.

## originality

PASS

The kinetic integral and interaction-only logarithmic endpoint are prior work. Pass for the inverse-cube collision endpoint in this integral and the compact-uniform crossover when one or both exponents are tuned within 1/log t. The strongest inspected same-model analysis excludes the integer exponents from its leading fixed-exponent classification, and the strongest inspected endpoint comparator keeps the exchange short range.

## value

PASS

The exact spectral integral is motivated by an existing kinetic calculation that leaves out integer-range leading asymptotics. The result fills a boundary of that model and quantifies the scale over which the fixed-power regimes cease to approximate it. In particular, the numerator's enhancement and Gaussian-width suppression can be varied independently, and neither treating both as constants nor independently interpolating the fixed-exponent powers gives the uniform ratio.

The dated certificate retains the supplied scientific assessment, sources and limitations.
