---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Orthogonal distinct-prime monomials yield <Ce_m,Ce_n>=(mn)^(−1/2−A−delta)prod_j I0(2a_j sqrt(log m log n)), hence the exact nonnegative double Gram/Schatten-four trace. For delta>0, I0(z)<=e^z and 2sqrt(tu)<=t+u bound by (mn)^(−1−2delta). At delta=0 the weighted-harmonic sum vs logarithmic Lebesgue double integral has a C¹ correction: the measure sum 1/n at log n differs from dt by constant plus exponentially decaying integration-by-parts primitive; derivatives of the Bessel kernel are controlled after boundary terms, so the correction is O(delta). Diagonal change x=(t+u)/2,v=(t−u)/sqrt(x), Jacobian sqrt(x), Bessel I0 asymptotic and Gaussian domination yield Q_d(x)~K_d x^(1/2−d), K_d=(4pi)^(−d)(prod a_j)^(−1)sqrt(2pi/A). Abelian Laplace analysis gives d1 coefficient 1/(4sqrt2 a1^(3/2)) of delta^(−1/2), d2 difference 4sqrt(pi)K2 sqrt(delta), d>=3 derivative 2L_d delta by exact positive series. K2 at a1=a2=1 gives 1/(4pi). Independent scaled-Bessel diagonal profile quadrature at x=1200 gave ratios 1.00013,1.00027,1.00053,1.01489 for four tested amplitude vectors, compatible with non-uniform small-amplitude convergence. Finite profile checks do not replace the integration-by-parts/Abelian proof.

## originality

PASS

Bayart–Kouroupis arXiv:2306.05733 is essential prior art for general Schatten membership, counting approaches, and even-Schatten trace identities; none of the inspected full primary text gives the specialized finite-prime coupled-Bessel boundary translation cusp with exact coefficient. Bayart–Brevig arXiv:1505.02944 concerns finite-prime approximation numbers, not this trace asymptotic. Related one-prime Hilbert–Schmidt sums have a different one-index diagonal and dimension threshold. A broader earlier Laplace/spectral edge theorem may imply the asymptotic, retained as qualified priority risk.

## value

PASS

Schatten-four is a natural first coupled even Schatten trace beyond Hilbert–Schmidt for composition operators; the two-prime boundary retains finite fourth trace but has singular square-root derivative. The exact amplitude-dependent cusp and dimension threshold quantify operator-ideal regularity and are not simply a membership or numerical test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
