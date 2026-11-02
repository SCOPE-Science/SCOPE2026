---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For q=r²=e^-L the Laurent monomial norms give H(t)=πtK=1/L+∑_{n≠0}n t^n/(1-q^n). On the negative axis t=-e^-Lv, Poisson summation of g(y)=1/(4cosh²(y/2)), with Fourier transform πω/sinh(πω), yields exactly H=-4π²/L²∑_{k≥1} k cos(2πkv)/sinh(2π²k/L). With E=e^-2π²/L, at v=1/4 the first nonzero even harmonic gives H=16π² E²/L² (1+O(E²)), while H_v=16π³ E/L²(1+O(E²)); uniform first-harmonic domination in an O(E) neighborhood places the outer root at v=1/4-E/π+o(E). Then Δ=2e^-L/4 sinh(L(1/4-v)) ~ (2L/π)e^-L/4 E = (4sqrt(r)/π)log(1/r) exp(-π²/log(1/r)). Verified direct logistic-series/Poisson duality numerically at multiple L with high precision, checking the prefactor. Gustafsson–Sebbar Theorem 6.1 is used explicitly, not re-proved, for the exact full zero-free band identification.

## originality

PASS

Best-of-knowledge originality from distinct actual primary statements and implications: An implicit elliptic characterization may permit derivation but is not itself the same explicit exponential asymptotic statement or prefactor; older Sebbar–Falliero remains a priority risk. A broad qualitative all-r theorem is mathematically compatible with, but not automatically quantitatively dominating, the exact thin-annulus expansion. Missing full 2007 text prevents excluding an equivalent asymptotic there. The root is an instance of the established classification, but the asymptotic coefficient is additional unless explicit modular transformation asymptotics are already present in the inaccessible earlier paper.

## value

PASS

The zero-free band separating two known Bergman-kernel zero regimes collapses nonperturbatively as r→1. Identifying both the exponent π²/log(1/r) and leading coefficient 4/π is a sharp natural geometric boundary-layer invariant useful in Lu Qi-Keng kernel-zero asymptotics, not merely a first numerical approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
