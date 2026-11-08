---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For n>=1, domain ||z||²<|w|<1 with w-bar-eta product real t∈(0,1), integrate z^alpha w^beta over complex ball radius |w|^(1/2) and punctured disk to obtain norm²=2*pi^(n+1)*alpha!/((ell+n)!*(2beta+ell+n+2)), admissible beta>=−floor((ell+n+1)/2). Summing the Laurent orthogonal basis in degree ell converges absolutely for |s|<sqrt(t), and parity decomposition yields K proportional to ((1+sqrt(t))²D−(1−sqrt(t))²E) for even n, plus sign for odd n, with D=(1−y)^−(n+1), E=(1+y)^−(n+1). Therefore zero exactly when Cayley(y)^(n+1)=(-1)^n*((1−sqrt(t))/(1+sqrt(t)))². Cayley maps disk to right half-plane: retain precisely root angles with positive cosine; counts n even 1+2 floor((n+1)/4), n odd 2 floor((n+1)/4), including n=1 no positive-slice zeros. All roots simple and realizable by actual strict-domain point pairs. q_t~(1−t)/4 implies sharp boundary fan coefficient 2^(1−4/(n+1)). Independently checked 126 admissible roots over n=1..12 and t=.16,.49,.81 against exact root equations. No off-slice or other exponent assertions.

## originality

PASS

Fu–Deng–Cao (2022) explicitly derives the general Bergman kernel for the same ball-fibre Hartogs family, so kernel itself is prior. The present contribution is the full admissible scalar zero-fibre count/realization and boundary condensation for every dimension. Edholm concerns two-dimensional power-Hartogs triangles, Park 2018 uses nested coordinate-domain inequalities rather than Euclidean ball fibres, and related Resultary rational diagonal Hartogs results have different geometry. The closest known general explicit formula may make the root equation a fairly immediate corollary; the detailed all-dimensional root count and geometric admissibility still require stated deductions. Explicit full priority uncertainty retained.

## value

PASS

The Lu Qi-Keng zero problem and realizability of kernel zeros are natural geometric-analytic invariants. This result settles a positive radial-product slice in all complex-ball fibre dimensions, exhibits the first dimension n=2 with genuine zeros, supplies all distinct roots and a sharp boundary exponent/parity-dependent count. It is more than a few-dimensional table and does not claim a new kernel formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
