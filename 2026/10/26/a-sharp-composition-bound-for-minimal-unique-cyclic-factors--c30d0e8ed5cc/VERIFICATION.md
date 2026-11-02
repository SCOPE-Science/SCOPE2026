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

A minimal unique factor is non-prefix-comparable to any other minimal unique factor, so each start contributes at most one, giving M_a<=n_a. For u=av of length≥2, minimality forces v to repeat at a different position t; the preceding symbol there must differ from a, or u repeats. This contrasting position is injectively assigned: if two v begin at the same t they are prefix-comparable, forcing their corresponding minimal uniques to be prefix-comparable. Therefore M_a<=n−n_a; length-one unique-letter exception is handled separately. Summing yields the total bound, with de Bruijn cyclic witnesses attaining equality at n=q^r. Independently enumerated 5,320 small cyclic words directly by wraparound occurrence multiplicities.

## originality

PASS

The predecessor paper already proves the non-nesting property, algorithms and linearized de Bruijn extremality for minimum unique substrings. The assessed result is the new composition-sensitive per-start-symbol bound min(n_a,n−n_a) for directed cyclic factors, proved by an injection into positions bearing a different letter. This stronger sparse-composition bound is not stated by the inspected linear-string theorem, though the de Bruijn extremality mechanism is prior.

## value

PASS

A natural content-dependent strengthening of the linear one-per-start upper bound for minimal unique factors of circular strings: it can reduce the count drastically when one symbol dominates, and de Bruijn sequences prove coefficient sharpness at infinitely many lengths. The bound is relevant to exact factor-spectrum and unique-marker enumeration with fixed letter counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
