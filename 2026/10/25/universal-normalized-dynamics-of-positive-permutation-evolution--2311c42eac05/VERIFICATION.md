---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Each strictly positive weighted permutation evolution algebra has a_i>0 and permutation pi on n coordinates; T(x)_{pi(i)}=a_i x_i^2/sum_j a_j x_j^2 on the closed nonnegative simplex. On each pi-cycle, the recurrence gamma_pi(i)*a_i=gamma_i^2 uniquely determines positive diagonal gauge gamma via the explicit (2^ell-1)-th root, so H(x)_i=gamma_i x_i/sum gamma_j x_j conjugates T to U(y)_{pi(i)}=y_i^2/sum_j y_j^2. Coordinatewise powers commute with pi, giving exact U^t(y)_{pi^t(i)}=y_i^(2^t)/sum_j y_j^(2^t). If I is the set of tied maximizers of y, all other coordinate ratios shrink at rho^(2^t), rho<1, so each orbit phase-shadows u_{pi^t I} superexponentially. Any periodic y becomes fixed by some pure normalized power under pi^L, forcing uniform positive entries on its support; thus all and only 2^n-1 nonempty support uniforms are periodic, with least periods equal to orbit lengths of pi acting on subsets. The exact counts #Fix(T^r)=2^{c(pi^r)}-1 and least-period orbit Möbius formula follow; the single n-cycle case reduces to nonempty binary necklaces. Perturbing any tied maximum to a unique maximum shows all support-size>1 periodic orbits are unstable; strict-max neighborhoods contract and show vertex cycles attract. Pointwise convergence of every trajectory iff pi is the identity, since a moved vertex creates periodic motion. Finite checker independently enumerates all 873 permutations through dimension six and sample gauges; infinite-dimensional assertion is proved algebraically, not inferred from finite tests.

## originality

PASS

The natural equivalence is a projective positive monomial power map / normalized quadratic stochastic coordinate map. The 2026 evolution-algebra survey motivates normalized squaring and asks graph-based stability criteria, but the survey complete manuscript was not accessible in this run; we cannot claim total noncoverage. Existing expander linear operator and permutation polynomial QSO are different dynamical maps. The full explicit all-dimensional orbit/stability classification is independently motivated, qualified by possible classical projective-monomial dynamics coverage.

## value

PASS

The 2026 evolution-algebra survey explicitly motivates determining normalized quadratic dynamics from the graph. An entire infinite, natural class of positive weighted permutation graphs is solved with sharp phase basins, superexponential attraction, complete periodic state counts and stability. These exact structural outputs are useful even though diagonal gauge and Burnside steps are elementary once identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
