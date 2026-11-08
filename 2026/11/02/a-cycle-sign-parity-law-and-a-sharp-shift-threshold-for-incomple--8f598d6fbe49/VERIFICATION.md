---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Diagonal sign conjugation gauges each signed cycle to all negative edges if sigma=(-1)^n and to an antiperiodic positive closing edge otherwise. Spectra give SPD t<1/2 in first sign class and t<1/[2cos(pi/n)] in second. Exact natural-order zero-fill incomplete Cholesky has p1=1, pj=1-t²/p_{j-1} for 2<=j<n, pn=1-t²-t²/p_{n-1}; path continuants D0=D1=1, Dj=D_{j-1}-t²D_{j-2} give pj=Dj/D_{j-1} and pn=D_{n+1}/D_{n-1}. Path spectrum gives first positive root of D_{n+1} at tIC=1/[2cos(pi/(n+2))] and next after SPD boundary; hence the exact sign-class failure interval, earlier positive pivots, and sharp global diagonal shift alpha*>0 from t/(1+alpha)<tIC. Condition-number formulas use exact antiperiodic largest and smallest eigenvalues and yield asymptotic n³/pi², breakdown window pi²/n³. At n=4 signs +++- and t=3/5, eigenvalues 1±3sqrt2/5>0, pivots exactly (1,16/25,7/16,-32/175). Independently reconstructed direct sparse-pattern IC0 for 34 independent cycle/sign instances, including both parity classes; n4 witness verified in rationals. The recurrence, path root structure and asymptotic proof—not floating tests—cover all n>=4.

## originality

PASS

Best-of-knowledge PASS qualified: the M-matrix sufficient IC0 existence theorem, positive-definite non-M-matrix breakdown and global diagonal shifting are all classical. The specific **two sign-product classes of uniformly weighted cycles**, unexpected n+2 path threshold, exact all-size shift and condition-number boundary are a sharper classification not in primary Scott–Tuma or Ferronato material reviewed. Historic existence literature is extensive and Eijkhout 1999 full text not inspected.

## value

PASS

Provides an exact analyzable family of strictly SPD matrices for which basic IC(0) catastrophically fails and a sharp rescue shift, even at n=4 with rational pivots; the spectral condition-number boundary is a meaningful quantitative diagnostic and distinguishes safe M-matrix and unsafe frustration sign classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
