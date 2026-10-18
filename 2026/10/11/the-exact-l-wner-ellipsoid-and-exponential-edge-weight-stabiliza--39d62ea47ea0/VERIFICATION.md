---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

In H_m of dimension m the weighted incidence covariance S=a L_spoke+b L_rim with m(a+b)=1 has eigenvalues (m+1)a and a+4b sin^2(pi k/m). Strict concavity of logdet S in the affine orbit mass and a Poisson root-of-unity summation establish unique stationarity t_m in [1,2), with t_3=1 and F_m(2)=-m/[3(2^m-1)]. Dihedral symmetry and stationarity force effective resistance equal on spoke/rim orbits; the weighted resistance trace identity then gives R_e=m, placing all ±edge roots on the boundary Q=mS. For an arbitrary nonsymmetric off-center competing ellipsoid, averaging contact inequalities and AGM show det Q>=m^m det S with equality only at center zero and Q=mS. Fourier eigendeterminant gives semiaxes and volume. Uniform convergence f_m->f, f(2)=0 and independent exact symbolic differentiation f'(2)=-1/54 combine with F_m(2)/m=-1/[3(2^m-1)] to give limit 18. Independent bisection of stationarity for m=3,4,5,8,12,20 produced t_3=1, t_4≈1.3660254, t_5≈1.618034, t_20≈1.999982835 with scaled gaps trending to 18. Finite checks corroborate proof.

## originality

PASS

Best-of-knowledge originality: targeted Resultary comparisons, exact primary theorem/parameter inspection and implication tests do not reveal prior coverage of the specifically identified surviving result. A self-indexed copy of the assigned finding is not prior coverage; risks are documented.

## value

PASS

A complete explicit eigenaxis/contact measure/unique Löwner ellipsoid and its exponentially precise optimal orbit weight asymptotic for a natural infinite wheel family is a substantial exact convex-geometric and optimal-design computation, beyond the general existence theorem or arbitrary numerical special cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
