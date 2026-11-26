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

Each onto monotone map corresponds to nested nonempty proper ideals I strictly inside J. The top world supplies a 2-witness. For a 0-world, extend to a maximal element a of I; it suffices to lift at each such a. If a has a 1-witness above it, the first cover on a saturated chain to that witness is in J but outside I. For the inclusion–exclusion term indexed by S, I is disjoint from U_S and B_n minus U_S is a downset; a downset of the induced remainder gives a downset of B_n on adjoining I, since any predecessor is either in I or still in the remainder. J=I fails and J=B_n passes the frontier test but omits 2, giving precisely the subtraction by one. The rank-capped map witnesses existence for n≥2; cardinality rules out n=0,1. An independently written antichain enumeration through n=5 generated each ideal as the union of the principal ideals of its maximal elements. For each eligible pair it tested the full 0-to-1 lift by taking the downward closure of J minus I, without using covers. It obtained 0,0,3,63,3604,3242450 and the claimed onto-monotone comparison 7805614 at n=5. Replay paths in the frozen package: verification/ideal_pairs.cpp and verification/direct_ternary.cpp with the corresponding logs; verification/verify_ie.py demonstrates inclusion–exclusion at n≤3 only. The uploaded code was inspected, not executed. No enumeration is used to justify the all-n formula.

## originality

PASS

Pass for the Boolean-lattice back-lifting census and its all-dimension frontier formula, not for the p-morphism definition, unrestricted order-map enumeration, or the overlapping small grid cases. The available closest statements do not give the count in general or at dimension five.

## value

PASS

The labelled Boolean lattice is canonical and C3 is the first chain target for which an intermediate lift poses a real obstruction. The formula isolates that obstruction for every dimension, and its exact finite census quantifies it: 4,563,164 of the 7,805,614 onto monotone maps at n=5 fail back. Knowing the ordinary three-colour order-map count does not supply this quotient invariant. No efficiency claim or generalization beyond the stated target is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
