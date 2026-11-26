---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Retaining exactly one oriented two-letter word per edge and killing all words of length three or more makes the stated basis a monomial quotient. Any product of three nonunits is zero, and their span is a nilpotent two-sided ideal with field quotient, hence the Jacobson radical. Squaring in that ideal gives one coefficient c_i c_j per edge, never 2c_i c_j, and leaves all m edge coordinates free. The resulting edge ideal equals the intersection of coordinate primes obtained by setting c_i=0 outside maximal independent sets: a monomial avoids the edge ideal exactly when its support lies in some such set. This proves reducedness over every field and identifies the components and their dimensions. In the whole algebra the scalar equation is lambda²=0, so the radical contains lambda; modulo lambda the ideal is the same reduced edge ideal. The independent-support strata have affine-times-torus class and point counts as stated, while the monomials of exact support S contribute (t/(1−t))^|S|, with an extra free factor (1−t)^(-m). Over F2, the explicit table is polynomial size, and division of the full or radical count by 2^m recovers the independent-set count; the conclusion is Turing hardness, not parsimony. In characteristic two over an algebraically closed field, commutativity makes every square-coordinate equation a square of a linear form, proving the reduced-linearity obstruction. An edge forces two distinct maximal independent sets, so its locus is reducible.

## originality

PASS

Best-of-knowledge pass for the uniform realization of arbitrary graph edge ideals, up to the stated free factor, as square equations in this particularly short associative monomial class. The standard Stanley–Reisner geometry and enumerators are not new in isolation. The closest retrieved graph/square-zero results concern a different operator equation or different varieties. A potentially related two-generator example could not be inspected and remains an explicit risk, not grounds by itself for failure.

## value

PASS

This is a uniform link between two natural structures, not a recomputation of graph enumerators: even a cube-zero radical in a short monomial algebra can have arbitrary graph independence-complex component patterns in its squaring locus. The characteristic-two contrast explains why order of multiplication matters, and the explicit sparse multiplication rule yields a hardness transfer in a restricted finite-field class. The standard formulas for edge ideals become geometric and computational information about the chosen algebra after the realization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
