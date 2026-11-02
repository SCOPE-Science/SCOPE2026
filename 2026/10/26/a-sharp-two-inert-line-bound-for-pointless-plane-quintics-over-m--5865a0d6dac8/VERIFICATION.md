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

For homogeneous degree-5 forms over F2, independent evaluation of the seven rational point constraints gives 7 independent conditions in 21 coefficients, exactly 2^14=16,384 pointfree equations. With no linear factor on a rational line, binary degree-five restriction is irreducible iff gcd(P(s,1),s^4+s)=1. Independently enumerated all 2,097,152 forms and recomputed seven line restrictions for all 16,384 pointfree masks, verifying 104/104 supplied orbit representatives. Independently generated all 168 invertible 3x3 GF2 coordinate transformations and verified each of 104 stated projective orbit sizes, no overlaps, and complete 16,384-element union. Independently recomputed each of 104 representative projective smoothness tests by Groebner unit ideals in all three affine charts, agreeing with the 98 smooth / 6 singular certificate flags. The resulting exact orbit-size-weighted histogram is I=2:168,3:1120,4:2352,5:5208,6:4928,7:2016, totaling 15,792; the unique minimal I=2 orbit has size 168. Thus this finite classification is exhaustively verified, not extrapolated from sample tests; derived coordinates/embedding constraints are explicit.

## originality

PASS

Huang–Kedlaya–Lau already enumerate genus-six curves and their plane-quintic locus over F2, giving a prior complete class source from which these statistics might be recomputed. Their inspected Section 3.3 and class-data descriptions do not directly list the seven-line irreducibility spectrum or minimal two-inert-line orbit uniqueness; obtaining it requires the new line-restriction and embedded projective-orbit calculation. Entin’s asymptotic Frobenius-section results concern growing fields, not this exact F2 histogram. PASS on best-of-knowledge originality of the explicit geometric invariant classification, with substantial indirect-derivability risk from prior complete census.

## value

PASS

The number of rational hyperplanes whose section is one degree-five inert point is a natural arithmetic-geometric invariant of an embedded pointfree genus-six quintic. An exact nonzero lower bound 2, unique extremal projective orbit, and full weighted spectrum are useful fine embedding data not mechanically read off abstract isomorphism-class counts. This is a complete motivated finite geometry classification rather than an arbitrary mask slice or a claim about all genus-six curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
