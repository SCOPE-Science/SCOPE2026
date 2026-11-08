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

The specified 21 forms in R=Z[alpha]/(alpha^2+alpha+2) define a primitive homogeneous degree-21 relative effective Cartier divisor, flat over the Dedekind base because each fiber polynomial remains nonzero. Exact independent determinant arithmetic using alpha^2=-alpha-2 reproduced the histogram of all 1330 triples: norm 0:112, 1:169, 2:228, 4:271, 8:320, 16:156, 32:70, 64:4. Every nonzero determinant has only factors 2, so away from dyadic primes all concurrency relations persist, including prime 7; pairwise distinct lines are protected by a unit-norm witness for each pair, and generic pair grouping gives 21 quadruple and 28 triple points. Reducing all forms at the two split primes over 2 (alpha=0 or 1) independently gave XYZ(X+Y)^6(X+Z)^6(Y+Z)^6 and XYZ(X+Y)^2(X+Z)^2(Y+Z)^2(X+Y+Z)^12, respectively. The read exact verification code computes the complete 49-support incidence structure, applies local-uniformizer division to each representative cross-product, checks choice-of-line-pair independence, and verifies the displayed seven-row marked-point specialization table. Properness identifies primitive projective point reductions with actual closures. The statement explicitly does not conflate the 49 colliding labelled sections with a Jacobian-scheme length or an invariant of all coordinate models.

## originality

PASS

PASS, qualified. Gévay–Pokora publish the exact 21 linear forms and generic 21 quadruple/28 triple complex intersection data; these are not original here. The present conclusion is the exhaustive integral good-prime test, two distinct complete scheme-fiber decompositions at the split primes above 2 and specialization census of individually labelled points. Inspected relevant primary sections did not state these reductions; older unindexed modular arrangement literature remains an explicit priority risk.

## value

PASS

This is a complete arithmetic-reduction classification of a natural classical Klein 21-line arrangement over its natural quadratic integer ring, including the exact two exceptional dyadic scheme fibers and all marked intersection specializations. The norm-unit certificate answers uniformly over every nonzero prime and supplies more than a small finite table: it identifies a nontrivial arithmetic boundary and exact multiplicity geometry, with model-dependence correctly acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
