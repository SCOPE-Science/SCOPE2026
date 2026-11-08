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

On cyclic Markov Q=P−I, truncating exp gives coefficients c_{p,n,r}=sum_{j<=p,j≡r mod n} h^j E_{p−j}(−h)/j!. All are nonnegative for h∈[0,1]. For n>=p and p>=2, unique coefficient h^(p−1)(1−h)/(p−1)! is negative for every h>1; p=1 similarly. The three short-cycle exceptions have unique algebraic boundaries: (p,n)=(3,2) root 2h³−3h²+3h−3; (4,2) root h³−2h²+3h−3; (4,3) root h⁴−4h²+8h−8. Their other coefficients stay nonnegative and monotonicity excludes later reentry. For an arbitrary two-state Markov Q, projector decomposition gives R4(hQ)=Π+E4(−hλ)(I−Π), with E4(−x)>0; entrywise nonnegativity iff its nonstationary eigenvalue lies in the unit disk. At n=3,h=3/2 the exact coefficient vector (−1,39,90)/128 has negative diagonal but spectral radius 79/128. Independent Fraction arithmetic checked 192 (n,p,h) combinations and exact spectral witness; these supplement the coefficient proof.

## originality

PASS

Classical RK4 polynomial, scalar stability and the nonnegativity-vs-spectral-stability distinction are established and credited. Blanes–Iserles–Macnamara treat positivity-preserving ODE methods and use RK4 as comparator, not the all-cycle exact table. Gottlieb–Grant–Higgs SSP theory establishes method-wide monotonicity bounds, not the generator-specific positive horizon. Related published SCOPE Gauss–Legendre [2/2] Padé, SSP-SDIRK and Crank–Nicolson have different R(z), so their sharp Markov counterexamples do not imply this one. A specialist circulant RK4 positivity classification remains a residual risk.

## value

PASS

The complete exact positivity horizons on directed cycles are natural Markov integrator diagnostics; the n=3 exception exceeding n=2 and minimal spectrally stable but nonstochastic 3-state witness are meaningful boundaries distinguishing physical transition preservation from purely spectral stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
