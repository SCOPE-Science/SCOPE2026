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

B=<2> modulo 73 has nine elements, its 9*8 ordered nonzero differences fill 1..72 exactly. Its affine stabilizer consists of nine multipliers in B and no nonzero translation, yielding 72*73/9=584 distinct orbit images. The affine signature of A is (0,1,3,7); exactly nine of B's 126 four-subsets have this signature and each is 2^j A; A has trivial affine stabilizer. Therefore exactly nine affine maps whose image contains A, constituting just one distinct B image after dividing by 9. An independent integer implementation exhaustively generated the 584 orbit images and directly found exactly one containing A. The implication for EVERY perfect difference set additionally and explicitly uses Hall/Niu classification of all cyclic (73,9,1) sets as this orbit; the finite orbit calculation does not prove that classification independently.

## originality

PASS

Qualified best-of-knowledge. Alexeev–Mixon (2025/2026) previously give the seed and the same B extension, while Niu (2026) gives the total 584 Singer orbit; those numerical facts are not new. The exact one-completion containment count is a separate finite incidence datum, not a consequence of the orbit cardinality alone. Bounded full-material comparison and primary searches found no assertion of that unique completion, but Niu complete text was not accessible; risk retained.

## value

PASS

The seed {1,2,4,8} is the natural powers-of-two four-term example central to the Sidon-extension question; deciding whether the exhibited order-eight PDS completion is unique is a canonical rigidity question about a nonarbitrary seed. The exact one-completion result is not mechanically determined by PDS existence or total orbit size and can inform extension/counterexample studies. Its finite specificity and dependence on a known classification are material qualifications, not automatic worthlessness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
