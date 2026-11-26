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

Doubly stochasticity and P²=Π make N=P−Π square zero on the two-dimensional centered plane, with rank one and representation σuvᵀ for an orthonormal pair. The centered mixture then squares to σ²p(1−p)(I−Π), and its two-by-two block gives the signed eigenvalues and all stated powers and correlations, including the nilpotent endpoints. Independently, the symmetric part S=(N+Nᵀ)/2 is traceless with row sums zero. Its three off-diagonal entries a,b,c sum to zero; its diagonal entries are a,b,c up to permutation, so 3(a²+b²+c²)=||S||_F²=σ²/2. At least one of a,b,c is ≤−σ/6: otherwise (a+σ/6,b+σ/6,c+σ/6) has strictly positive coordinates of sum σ/2 and square-sum strictly below (σ/2)², a contradiction. The skew part is σ/2 times an oriented quarter rotation on the centered plane; its three cyclic entries have magnitude σ/(2√3) (from zero row sums and its Frobenius norm). For the pair at that minimum, one ordering gives an entry of N at most −σ(1+√3)/6. This proves the sharp upper bound from nonnegativity independently of the sine argument. Exact symbolic substitution of the literal P_* confirms nonnegativity, double stochasticity, P_*²=Π, singular norm √3−1, the mixture identity and expansion of every nonempty branch. Interpolation toward Π gives strictly positive witnesses approaching the norm bound; nonattainment refers to σ, or to the mixture modulus for 0<p<1 (at p=0,1 the modulus is always zero). The branch construction preserves cellwise uniform densities, hence the asserted coarse correlations; its invariant sector is a transfer-operator sector, not a claim that pullbacks of cellwise observables remain cellwise constant. A nonzero square-zero centered operator is impossible for fewer than three states.

## originality

PASS

Best-of-knowledge pass on the sharp three-state time-reversal optimization and its explicit realization, not on the general phenomenon of spectral changes under annealing or on the general piecewise-affine matrix realization framework.

## value

PASS

Three is the first possible state count under the exact two-step constraint. In this minimal class the result determines both the complete result of reversal mixing on centered two-point correlations and the maximum possible nonzero eigenvalue modulus for every mixture weight, with an expanding-map witness. Sharpness matters because the general averaging framework alone cannot quantify how much memory can be created.

The dated certificate retains the supplied scientific assessment, sources and limitations.
