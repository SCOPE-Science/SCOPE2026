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

Independent count: fix F projecting onto U along W, with dimensions s and n−s, and write a varying rank-one E as (x,y)(α,β), modulo the q−1 scalar rescalings, with α(x)=a and β(y)=1−a. The commutator rank is the sum of the indicators for xβ and yα being nonzero, since the two blocks land in different summands. For a=0, y and β must be nonzero and have (q^{n−s}−1)q^{n−s−1} choices together. The orthogonal pairs (x,α) contributing ranks 0, 1 and 2 have counts 1, 2(q^s−1) and (q^s−1)(q^{s−1}−1). For a=1 swap the two summands. For other a both off-diagonal products are nonzero, with (q^s−1)(q^{n−s}−1)q^{n−2} parameter choices. Multiplying by I_q(n,s)/((q^n−1)q^{n−1}) transports this pair census to fixed E; the factor for rank zero at a=0 becomes J_0 by the Gaussian-binomial recurrence, and the complementary calculation gives J_1. Summing yields T(a), and subtraction the stated exceptional rank-two counts, including zero counts when the relevant summand is one-dimensional. Independently, for coordinate E the commutator has off-diagonal blocks b,−d with bd=a(1−a). It is square-zero at rank one; at exceptional rank two it has nonzero C² from db and C³=0, forcing precisely one 3-block. If bd≠0, its cyclic two-dimensional restriction has polynomial t²+bd, with kernel as complementary space, including repeated-root cases in characteristic two. This also proves the field-size distinction and the dimension-four example follows from the counts. Independent replay: python3 /workspace/independent_checks_oct19.py (field_check), exhaustive enumeration in GF(4) for n=2,3 including scalar values not in the prime subfield; all strata agreed with the incidence count. The supplied code was inspected, not executed; its extension-field checks are arithmetic rather than extension-field enumeration.

## originality

PASS

The distinct contribution supported by comparison is the uniform joint trace/commutator-rank distribution for arbitrary partner rank and dimension, plus the resulting similarity counts. The total idempotent count, basic block structure, and the complete dimension-two case must be credited as covered. Later dated catalogue records separately reproduce the boundary-rank and interior-rank counts up to changing which factor is fixed; they are material equivalents in those regimes, not evidence of antecedence or of the relationship between the records.

## value

PASS

Trace and commutator rank are natural simultaneous-conjugacy invariants, and their joint probabilities distinguish nilpotent behavior that the usual total or product-rank counts miss. The uniform finite-field formulas resolve how often all possible commutator types occur, including maximal nilpotency index and characteristic-two effects. This is a complete useful refinement across dimensions, not a recomputation of the known 2×2 case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
