---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Keep Exner–Holzmann's geometric and decay hypotheses, including injectivity of the coordinates and the weighted integrability in Theorem 3.2. In that theorem the coefficient is 1/8 times the gamma L² norm squared minus the derivative-kernel term with the additional factor 1/2. Under the stated Fourier convention the transform of exp(−ρ_n|s|) is 2ρ_n/(ρ_n²+ξ²); the derivative contributes ξ². Thus Parseval gives 1/(16π) times the integral with symbol 1−Σ_n |(χ_n,uχ_1)|²ρ_n² ξ²/(ρ_n²+ξ²). The sine integral for n≥2, with only even n nonzero, gives precisely w_j=|(χ_2j,uχ_1)|²ρ_2j². The printed transverse expression is understood for the summed modes n≥2 (the separate n=1 element is zero by parity). The identity Σ_j w_j=1 turns the symbol into the asserted positive weighted sum; the exchange is justified by summability and the bounded frequency fractions. To check the summation, put x=q² and A=4j²−1: (A+1)/(A²(A+x))=(x−1)(1/A−1/(A+x))/x²+1/(xA²). The cotangent partial fractions with r²=1−x give exactly the printed formula, its r=0 limit gives 4−32/π², and imaginary r gives coth. The two additional sums in the proof give Σw_j=1 and Σw_jA_j=4 directly by combining inverse powers of A; the series controls q=0 without cancellation. Every term decreases strictly, the lower bound uses A≥3, the upper uses Jensen's inequality and the mean 4, and domination by w_jA_j gives q²M(q)→4. Squaring the inherited square-root law and rationalizing the dispersion relation give the stated coefficient and O(β⁵) at the positive spectral threshold, not a splitting of the two signed states.

## originality

PASS

Credit Exner–Holzmann for the weak-bending expansion, spectral correspondence and unsummed coefficient, and the earlier Dirichlet literature for the input asymptotic, including the positivity and Fourier-series representation attributed to the monograph by the frozen record. The quartic order and algebraic transfer to the Dirac threshold are direct consequences of the published theorems, not an independent novelty. The supported distinct contribution is the evaluated elementary frequency response and its structural consequences, including strict frequency decay, explicit rational bounds and high-frequency constant. The verified precursor expression leaves the transverse response unevaluated; the strongest other compared catalogue statements have different operators, geometries or observables. I did not find established coverage of the elementary identity in material actually inspected.

## value

PASS

The canonical leading binding coefficient is motivated by the known weak-bending theorem. Evaluating its transverse response at every frequency makes curvature-scale sensitivity explicit, with strict decay, usable uniform bounds and a quantified high-frequency tail, rather than merely giving another way to compute the coefficient at one input. This information is meaningful for profiles at different longitudinal scales; the elementary Dirac conversion alone would not supply that value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
