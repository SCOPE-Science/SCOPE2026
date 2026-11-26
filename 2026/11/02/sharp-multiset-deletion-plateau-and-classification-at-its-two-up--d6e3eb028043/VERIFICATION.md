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

Two codewords are confusable exactly when their coordinatewise-minimum sum is at least k. At most q words are heavy, since no coordinate can be >=k in two words. Two light words have intersection at least 2n-qh, which exceeds h for n>floor((q+1)h/2), and none exist for n>qh. The pure words and, in the plateau, any light word attain the bounds. At n=T the two light words have overlap h in the odd-q construction and 2 floor(h/2)<=h in the even-q construction; adjoining the pure words proves the required lower bound q+2, not optimality there. At qh and qh-1 (both above T), a maximal book of size q+1 has one light word and one designated heavy word per coordinate. At qh the light word is all h and each heavy word must be pure. At qh-1 the light word is all h except for one h-1: a heavy word on any other coordinate is forced pure, while the deficit-coordinate word can move at most one unit to a different coordinate. Each such choice is compatible and distinct, giving q^2 books on the labeled alphabet. Independent L1-distance clique enumeration for ternary h=3,4 verified the change at T, the 9 and 1 endpoint counts and the disappearance of four-word books past qh.

## originality

PASS

The exact three-survivor Resultary result substantially overlaps in pattern and proof strategy; the list-capacity result also supplies a heavy-incidence argument that applies at the upper threshold in unique decoding. The supported distinct content is the sharp integral lower threshold and complete plateau for arbitrary survivor budgets in the stated k>=4 regime, including the even-alphabet, odd-h rounding, and the full labeled maximum-book classifications, especially at the penultimate length. The closely matching works do not state those ingredients together or imply them by specializing a stronger theorem. The same-day three-survivor comparison was based on its proof, not priority inferred from the path date.

## value

PASS

The transition identifies when a highly deleting multiset channel can carry just one message beyond the q monochromatic symbols and shows the first length at which the smaller bound ceases to hold. Its endpoint classifications describe how much freedom optimal codebooks have as that extra message is about to disappear: from q^2 labeled choices to one. These are exact invariants of the natural high-deletion regime, not isolated small-parameter checks. Credit is for the sharp full range and extremizer structure, not for reusing the heavy-coordinate idea.

The dated certificate retains the supplied scientific assessment, sources and limitations.
