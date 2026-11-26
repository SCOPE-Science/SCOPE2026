---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Unitary Schur form gives rI+aN, a>=0, and the determinant and positive leading pivot of I-T*T give a<=1-r^2. For epsilon=1-r, a=c epsilon, x=n epsilon, the exact defect norm is xr^n h(c|x/r-1|), where h(u)=sqrt(1+u^2/4)+u/2. It is nondecreasing in a at each integer n, so the contraction boundary maximizes the supremum at every r. Compact uniform convergence and the uniform tail xe^(-x)[1+C(2x+1)] justify the mesh limit, including c=2-epsilon, and convergence of every rescaled maximizing index under uniqueness. Reflection x to 2-x raises the scalar factor below x=1 without changing the shear factor. Above one, the log derivative is c/sqrt(4+c^2 y^2)-y/(1+y), strictly decreasing through zero for c>0. At c=0 the unique scalar maximum is e^(-1) at x=1; for c>0 strict shear monotonicity plus the interior maximum proves strict increase of the optimized value. At c=2 the stationary equation gives the stated quartic. The expansion of y is c/2+c^2/4+c^3/8+O(c^4); in log(R(c)/R(0)) the quadratic and cubic terms are c^2/8+c^3/24. The left stationary term is 1/sqrt(y^2+4/c^2), which increases in c and bounds y_c strictly above zero and below the golden ratio; its limit gives y_c increasing to that ratio and the claimed slope. A standalone 60-digit calculation verified the constant and scaled time; discrete recursive matrix calculations corroborated their limits on bounded grids.

## originality

PASS

The supported contribution is the exact repeated-real-eigenvalue contraction-class optimization, its rescaled maximizing-power limit and quantitative coupling profile. Prior operator characterizations, displacement and resolvent norm-gap theorems do not state that result. A distinct later-dated geometric-direct-sum result has the identical two-site envelope, block contraction criterion, and continuous peak optimization; those pieces are not credited as distinct from that record. It optimizes lattice phases in a single infinite direct sum, not the supremum over powers and all two-dimensional contractions at each fixed r, and it does not state the contraction-class asymptotic with its varying boundary coupling, or the two coupling expansions. This distinction is a comparison of statements, not evidence of provenance from record dates.

## value

PASS

The repeated-real-eigenvalue case isolates the impact of admissible nonnormality on a quantitative Ritt power defect. The maximal shear increases the limiting constant from e^(-1) to about 0.6794 and shifts the concentration of maximizing powers from scale 1 to about 2.3953. The finite-class extremizer and precise time localization make these figures useful as a sharp benchmark, not just a tabulation of a Jordan norm or an example of a Ritt characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
