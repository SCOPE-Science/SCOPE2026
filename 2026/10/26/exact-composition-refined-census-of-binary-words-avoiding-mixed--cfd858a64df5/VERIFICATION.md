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

A mixed Abelian square has both letters in both halves, so it cannot lie across just one boundary. Across two boundaries it requires an even complete middle run, and an even middle run gives such a factor using one letter of each outside run. The prior five-run obstruction handles either parity of the middle run by adding an endpoint letter when necessary. In four runs a^h b^i a^j b^k, the factors a^j b^i a^j b and a b^i a^j b^i witness failure respectively when h≥j and k≥i, once i,j are odd. Conversely a factor spanning all three boundaries has its midpoint in run two or three, and respectively the counts of a or b cannot agree under h<j and k<i, including the cut between the inner runs. For each positive composition the two orientations and the three-run middle-run parity give the stated first terms; the four-run terms count odd j with x/2<j<x and odd i with y/2<i<y, giving floor(x/4)floor(y/4) per orientation. The monochromatic boundary and omitted empty word are consistent. The one-variable series follows by specialization and has leading pole 1/[8(1−z)^4] at 1 and no other pole of order above two, giving the asserted asymptotic.

## originality

PASS

The five-run obstruction is known, and the proof of the prior sufficient effective-word construction already gives four-run sufficiency using exactly odd inner runs and the two strict outer/inner inequalities. The independent addition is the converse for arbitrary four-run words and the complete composition and length counts, rather than the old obstruction, the sufficiency proof, or just summation of a prior complete characterization.

## value

PASS

The class is motivated by the known lower-bound program for binary words having only trivial squares. The converse distinguishes all such words from examples selected to have few trivial squares, and the exact composition law makes it possible to identify the full admissible class at every weight, rather than list canonical examples. The length asymptotic quantifies the size of that structurally characterized class. The finding does not claim to solve the minimum-square conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
