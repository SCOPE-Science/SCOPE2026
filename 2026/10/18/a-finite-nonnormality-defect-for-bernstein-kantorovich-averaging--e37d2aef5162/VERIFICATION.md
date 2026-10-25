---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: Polynomial bin means N∫bin t^m dt have leading k^m coefficient N^{-m}; Bernstein expectation sends this to (n)_m/N^m x^m, so nonzero eigenvalues of the n+1 dimensional range are simple λ=(n)_m/(n+1)^m. Squared kernel integrated over disjoint equal bins gives HS²=N/(2n+1) Σ binom(n,k)^2/binom(2n,2k), and the central-binomial convolution identity reduces it exactly to N/(2n+1)4^n/binom(2n,n). In k≈√N scaling, log λ²=−x²−h(x+x³/3)−h²(x²/2+x⁴/6)+O(h³P(x)), h=N^{-1/2}; exponential coefficient Q=x⁴/6+x⁶/18, Gaussian half-line Euler–Maclaurin gives Σλ²=√π/(2h)−1/6+11√π h/96+O(h²). Stirling HS²=√π/(2h)+√π h/16+O(h³) yields Δ=1/6−5√π h/96+O(h²). Strict Δ>0 from Schur decomposition and K_n kernel asymmetric on bin x<t<1/N (normality with nonnegative simple eigenvalues would force self-adjointness). Independently checked rational HS identity and Δ positivity through n=28 and residual at n=200,1000,10000; the asymptotic remainder proof relies on uniform Gaussian tails, not numerics.

## originality

PASS

PASS (best-of-knowledge): Classical Bernstein–Kantorovich papers supply moment, polynomial and approximation formulas; the exact HS norm follows from beta integrals but a nonnormality spectral-singular energy deficit and its finite nonzero asymptotic constant require a different comparison. Full 2019 Acu–Gonska primary paper examined and does not state this defect in the material read. The 2011 higher-order source full text was not accessible; priority risk acknowledged without drawing whole-document noncoverage from abstract.

## value

PASS

PASS: The limit 1/6 is a nonzero finite obstruction to spectral-energy accounting by eigenvalues despite approximation to the identity. It quantifies an intrinsic nonnormality invariant of a familiar finite-rank integral approximation operator; second correction shows precise stabilization, not a generic textbook spectrum statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
