---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For algebraically closed k of characteristic two and parameter lambda !=0, the submitted normal form is the Witt length-two class (x,lambda x^3). The upper jumps (1,3) give genus two using the cited source classification. The marked ratio b/a^3 is invariant under affine x scaling/translation, Witt coboundary reduction, and inversion of an unlabelled C4 generator; this key claim depends on the explicit reduction argument, not a finite sample. The Witt-to-quintic substitution was checked as an exact polynomial identity over F2[r,u], with r^4=lambda, giving y^2+y=lambda u^5+(lambda+sqrt(lambda)+1)u^3+(1+fourth_root(lambda))u. General genus-two Artin-Schreier normal-form isomorphisms preserve I=b^5/a^3: quintic and cubic coefficients scale by s^5 and s^3. Converse reduces remaining lower odd coefficient to a solvable degree-16 translation equation (nonzero leading term), and an Artin-Schreier constant; algebraic closure is essential. Consequently I^2=J=(lambda^2+lambda+1)^5/lambda^6. Its reduced numerator degree is ten; derivative J'=(lambda^2+lambda+1)^4/lambda^6 is nonzero, proving separability and ten distinct roots for each nonzero finite j. The two zeros of lambda^2+lambda+1 each have multiplicity five; poles at 0,infinity have orders 6,4. The exact verify.py finite-field arithmetic was examined; it cannot alone prove global uniqueness or priority. A plausible relevant originating paper could not be read fully due to access, so this remains an explicitly qualified correctness reading of its standard normal-form input, not an independently confirmed citation.

## originality

PASS

The degree-ten explicit forgetful invariant and exact subgroup-marked versus unmarked fiber profile are not found in the read general 2-rank-zero hyperelliptic automorphism results. The potentially decisive original Witt-normal-form classification has only accessible abstract and quoted premise, so priority and input-provenance risks remain substantial; this is qualified best-of-knowledge only.

## value

PASS

There is a natural moduli-theoretic distinction between a curve admitting a C4 automorphism and the same curve equipped with an embedded unlabelled order-four subgroup. Identifying the exact degree, branch locus, exceptional fibers and resulting conjugacy classes is a structural classification not supplied merely by the famous 32/160 group orders; a future study of characteristic-two Hurwitz spaces could reasonably need this precise forgetful map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
