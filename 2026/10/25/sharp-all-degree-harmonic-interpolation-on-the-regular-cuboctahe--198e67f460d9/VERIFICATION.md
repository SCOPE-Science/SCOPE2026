---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The addition theorem with probability-surface-measure normalization yields Gram G_ell(x,y)=P_ell(x dot y). Antipodal vertex-pair row symmetry forces a six-dimensional relevant parity space and six zero eigenvalues, except when listed parity eigenvalues vanish at low degrees. For odd ell, signed-root geometry has eigenvalues +2 and -2, each multiplicity 3, giving 2(1+2a),2(1-2a); for even ell, three eigenbranches 2(1+4a+b), 2(1-b),2(1-2a+b) with multiplicities 1,3,2, where a=P_ell(1/2),b=P_ell(0). Independently used exact rational Legendre recurrence for all ell=0..19, obtaining ranks 1,3,5,6,... and unique minimal 65/32768 at ell10 of multiplicity one. Constructed 12-by-12 Gram directly from independently enumerated vertices and scipy Legendre at ell=0,1,2,3,4,7,10,19,50,100; sorted eigenvalues match branches within 2.2e-12. The required infinite proof is Bernstein |P_ell(cos theta)|<sqrt(2/(pi*ell*sin theta)): for ell>=20, |a|<1/5 and |b|<11/60, giving all even eigenbranches >1/30 and all odd >6/5, hence larger than 65/32768. The finite enumeration is a certificate only for ell<=19, not the infinite conclusion.

## originality

PASS

Classical harmonic addition formulas, signed-root symmetry, and harmonic-index spherical-design literature are prior mathematics. The asserted complete point-set-specific degree-by-degree Gram spectrum is not claimed novel solely for its representation formulas; the discriminating contribution is the *global* exact all-degree conditioning minimum at ell10 and full parity surjectivity from ell3, which are not found in the inspected spherical-design or bandlimited-transform claims.

## value

PASS

The cuboctahedron is a canonical Archimedean vertex set. An exact optimal all-degree frame conditioning lower bound and the unexpectedly nearly singular degree-ten constant sector are natural harmonic sampling invariants. Determining whether a fixed configuration is uniformly stably interpolating for every sufficiently high degree is mathematically motivated beyond an arbitrary finite eigenvalue table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
