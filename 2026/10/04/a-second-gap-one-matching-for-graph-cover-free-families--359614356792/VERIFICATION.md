---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The lower bound is exact: every E14-CFF is a 14-block Sperner family, and Sperner's theorem gives t(1,14)=6 because C(5,2)=10<14<=C(6,3)=20. The displayed fourteen distinct triples on [6], grouped into seven matching edges, satisfy endpoint incomparability and, for each edge, every one of the twelve off-edge blocks has a point outside the endpoint union. Hence they form an E14-CFF on six points. Proposition 5.8 of the primary paper gives t_e(E14)=t(1,7)=5, so t(E14)=6=t_e(E14)+1. A fresh independent bounded replay checked all seven edges and all 84 off-edge containment conditions; the infinite lower bound is theorem-based, not inferred from the finite check.

## originality

PASS

The complete current arXiv v2 primary paper proves t(E8)=t_e(E8)+1 and then explicitly asks in Open Problems 5.12-5.13 for further and complete matching orders. Its general Proposition 5.9 leaves the relevant matching values within a gap of one, but does not determine E14. Current Resultary search found no earlier published E14 exact value or equivalent seven-edge construction. The assigned six-point witness therefore supplies a new exact instance rather than restating the source theorem.

## value

PASS

This is a natural exact invariant at the next explicit matching case of a published classification problem. The six-point construction gives a second concrete gap-one matching beyond E8 and narrows the requested matching phase diagram; the result is finite but structurally motivated rather than an arbitrary census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
