---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The prefix sigma^8(0) of length 149 of the Tribonacci fixed point gives distinct factor totals 9,17,25,33,41,49 at lengths 4,8,12,16,20,24. The published exact complexity p(m)=2m+1 of the infinite Tribonacci word attains those totals, so these observed sets are the complete global sets—not a potentially incomplete prefix sample. Testing all complete factors for equality of the four consecutive length-n integer symbol sums produces 0,0,0,0,0,1 factors at n=1..6. The sole length-24 witness 102010102010010201010201 splits as 102010|102010|010201|010201, sums 4 each; first occurs at prefix index 76. Independently constructed morphism prefix and recalculated six exhaustive factor sets, counts, and uniqueness. This proves the minimum exactly six for the infinite word, contingent on the established complexity identity.

## originality

PASS

Popoli–Shallit–Stipulanti FSTTCS 2024 Theorem 37 classifies *additive cube orders* using a 4927-state automaton; Problem 38 asks for arbitrary additive k-power orders and notes the fourth-power automaton is computationally expensive. This does not state the order-six minimum or unique 24-symbol witness. The k-binomial-complexity literature gives the factor-complexity counting theorem used as certificate, not the additive-fourth minimum. Scoped web/Resultary queries did not locate a prior exact minimum.

## value

PASS

The smallest occurrence and complete equality layer at that order form a natural sharp finite cutoff inside an explicitly studied difficult open characterization of additive higher powers in the Tribonacci word. The exhaustive factor-complexity certificate is mathematically meaningful even though it does not solve the entire open problem. It is not merely a random substring enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
