---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The final claim is for one exact harmonic degree ell>=1, tangential poloidal/toroidal complex L2(S2) fields, standard area measure, and hemispherical restriction. Longitude orthogonality splits the compression into 2x2 m-blocks; equatorial reflection makes both diagonal entries 1/2. The cross-polarization hemisphere integral is 2 pi i m |Y_lm(pi/2)|^2/[ell(ell+1)]; normalized associated Legendre values vanish if ell+m odd and otherwise give mu_lm=m(2ell+1)c_((ell+m)/2)c_((ell-m)/2)/(2ell(ell+1)), with c_j=binom(2j,j)/4^j. For each parity chain, the product ratio under m->m-2 is 1-2(m-1)/[(2a-1)(2b+2)]<1 and the extra m factor decreases, so |m|=ell uniquely maximizes. The degree maxima M_ell=(2ell+1)c_ell/[2(ell+1)] satisfy M_(ell+1)/M_ell=(2ell+3)/(2ell+4)<1 and M_1=3/8. Thus eigenvalues lie in [1/8,7/8], only degree-one |m|=1 with the appropriate polarization attains the endpoints (real eigenspace dimension two). Independent rational checks through ell=50 support the algebra; the exact identities and monotonicity, not those finite checks, prove every ell.

## originality

PASS

Statement/implication comparison of actually read primary theorems and direct published mathematical-finding search supports best-of-knowledge originality for the final narrow claim, with precisely documented broader prior formulas and residual historical risks. Neither a failed search nor literature inaccessibility is treated as a proof of novelty.

## value

PASS

The energy leakage of an exact-frequency tangential field across an arbitrary hemisphere is a natural spectral-localization invariant. A sharp universal 1/8 loss, exact degree dependence, unique angular maximizers, and equality fields give useful localization limits. This is not the much larger mixed-degree Slepian space, in which a uniform leakage bound is false.

The dated certificate retains the supplied scientific assessment, sources and limitations.
