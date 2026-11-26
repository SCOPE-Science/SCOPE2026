---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A matched edge in the cubic prism covers at most six vertices; selecting ceiling(n/3) rungs with cyclic gaps at most three hits that bound. The local alphabet records each physical edge once, compatibility checks shared endpoints, and each cyclic transition checks domination for the central column. For n=3 the repeated window positions identify the same columns and do not introduce an extra matching or constraint. The trace fixes the column origin and counts labelled edge sets, not cyclic orbits or endpoint sets. Independent replay (python3 /workspace/branches/reproduction/prism.py) constructs options by physical incidence, verifies 49 states, 147 arcs and an integer potential, certifies the two zero-cost SCC cycles of lengths 3 and 6, and proves the other three rational trace identities exactly by multiplying the series by the determinant or its square and testing all numerator coefficients up to the adjugate degree bounds 48 or 96. The log-determinant expansion to reduced costs 0,1,2 then yields the all-n minimum coefficients. In the cost-2 case the single-mark term contributes 2-(-1)^k after division by n; the two-mark term extracts half of [w^(k-1)](15-20w+11w²-2w³)/(1-w)^4, giving the stated cubic factor. Independent recursion by smallest available vertex agrees with complete transfer histograms at every n=3..10 (108691 matchings), including c4=42 and c7=147. Finite enumerations alone are not the infinite proof.

## originality

PASS

Pass for the explicit full enumerator and the all-class minimum classification as an extension, not for the known minimum size or the n≡2 (mod 3) formula in isolation. A preceding dated Resultary record already gives exactly the latter coefficient through uniqueness of the matching on every optimal vertex set. A later-dated catalogue record is mathematically equivalent on the whole invariant and classification, via a different smaller matrix; it is not evidence of a pre-existing full result. No inspected antecedent gives the full enumerator or the remaining residue-class formulas.

## value

PASS

Extremal paired domination says how many endpoints are needed, not how many distinct certificates realize that optimum. On the natural circular ladder family, the full polynomial distinguishes redundancies and matching sizes, while the exact residue-class classification shows periodic variability and large differences between orders. Neither the known optimum nor the preceding one-residue result gives this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
