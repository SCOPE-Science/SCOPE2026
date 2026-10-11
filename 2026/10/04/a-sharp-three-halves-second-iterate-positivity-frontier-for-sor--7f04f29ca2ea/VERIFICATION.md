---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

From \(x^{(0)}=0\), one forward SOR step for a nonsingular \(M\)-matrix is nonnegative because the lower-triangular SOR factor has a finite nonnegative inverse. In one dimension \(x^{(k)}=(1-(1-\omega)^k)b/a\) is nonnegative for \(0<\omega<2\). After positive diagonal scaling, the \(2\times2\) Stieltjes case has the displayed second-response matrix; every entry is manifestly nonnegative except the lower-left factor \(\rho\omega^2(3-2\omega+\omega^2\rho^2)\). Its quadratic sign gives the fixed-coupling criterion and robust threshold \(\omega=3/2\); above it sufficiently small positive \(\rho\) and then small positive second forcing give a negative second coordinate. Independent exact-rational reconstruction reproduced the witness \(\rho=1/5,\omega=5/3,g=(1,1/10)^{\mathsf T}\) with second iterate \((43/54,-4/81)^{\mathsf T}\) and positive exact solution.

## originality

PASS

The classical sources concern convergence, spectral-radius bounds, and regular/weak-regular splittings; the closest Yun note proves only that overrelaxed SOR splittings of an \(M\)-matrix cannot be weak regular for \(\omega>1\). That obstruction begins at \(1\), whereas the audited finite-horizon positivity statement remains uniformly true through the strictly larger sharp value \(3/2\), so it is not implied. Resultary searches found no prior second-iterate phase law.

## value

PASS

The exact transient positivity boundary and earliest dimension/iterate counterexample are mathematically motivated by the gap between asymptotic SOR convergence and order preservation. The sharp \(3/2\) frontier is a meaningful boundary with a positive-data counterfamily, not merely a type or normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
