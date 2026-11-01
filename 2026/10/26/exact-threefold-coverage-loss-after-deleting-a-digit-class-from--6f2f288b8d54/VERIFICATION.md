---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Group base-g digits into H=g³ blocks. For three summands each confined to W0 or W1, every block contribution is s_j+g v_j≤3g(g−1)<H so there is no interblock carry. With q of 3 summands of type W0, q=1 has full interval T1={0,…,2g²−g−1}; q=2,3 are subsets, and q=0 gives multiples-of-g T0 with 3g−2 elements. |T1∩T0|=2g−1, so allowing zeros, size=(2g²−g)^k+(3g−2)^k−(2g−1)^k. A separate digit-allocation proof enforces all three summands positive: only T1 words with quotient digits B=0 and total remainder R≤2 are excluded, exactly binom(k+2,2) weak compositions; T0\T1 all admit 3 positive type-W1 summands. Thus exact formula for every g≥4,k≥1 and θ_g=log_{g³}(2g²−g)<1. Independent direct enumeration verifies nine parameter pairs incl. g=4,k=3 (22599), not an infinite proof.

## originality

PASS

The complete three-class union is a minimal asymptotic basis by Tang; this theorem deletes one ENTIRE infinite digit-position class and computes the exact size, dominant exponent and positivity correction for the remaining threefold sumset at all full-block cutoffs. Tang’s accessible full primary paper proves minimality/essentiality for the original complete family, not this complete residual-count formula. Generic g-adic sumset or carry automata might implicitly give it; no covering theorem in inspected material.

## value

PASS

Minimality of a full g-adic basis motivates studying how the representation count deteriorates on removal of an entire infinite digit class. The exact three-exponential inclusion–exclusion law plus polynomial positivity correction and sharp sublinear coverage exponent are natural structural invariants, not a random cutoff table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
