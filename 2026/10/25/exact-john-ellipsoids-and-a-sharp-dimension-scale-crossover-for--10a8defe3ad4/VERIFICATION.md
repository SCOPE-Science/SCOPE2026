---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For each d>=2 and 0<h<1, the proposed axial/transverse axes a,b obey a^2+((d+1)/sqrt d) h a+h^2=1, b^2=a^2+h a sqrt d. A point of the candidate ellipsoid boundary at axial fraction u=|x|/a has exact lens inequality slack h a sqrt d (u-1/sqrt d)^2; strictly positive off the two contact latitudes. After ellipsoid normalization, four signed contact points per transverse basis direction at (±1/sqrt d,±sqrt((d-1)/d)e_j), each weight d/[4(d-1)], sum to zero and have weighted second moment I_d. John’s global contact theorem certifies unique maximal-volume inscribed ellipsoid among all rotations/translations, and unique contacts. Direct quadratic expansion proves dimension scaling h sqrt d→tau with limiting A_tau exp(-tau(A_tau+tau)/2), and fixed-h asymptotic e^-1/2 (1-h^2)^((d+1)/2)/(h sqrt d); monotonicity follows from strict nested lens inclusions and uniqueness. Independent numeric checks in dimensions 2,3,8,23 rederived the exact identity and normalized contact covariance to floating precision, not a proof of continuum.

## originality

PASS

Best-of-knowledge PASS: inspected classical global ellipsoid-contact criteria and lens metric papers do not give the stated d,h axes, all contact latitudes and asymptotic crossover. Applying John’s theorem is classical but the explicit positive contact design and exact candidate are specific.

## value

PASS

The intersection of two congruent balls is a canonical symmetric lens. A complete all-dimensional global John ellipsoid and precise contact set provide an exact affine approximation invariant, and its critical d^-1/2 volume crossover is substantive geometry rather than a routine substitution or isolated table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
