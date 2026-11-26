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

Independently regenerated h^6(0) and verified all twelve listed phase windows of the two third iterates by cyclic indexing (python3 /workspace/review_evidence/check_morphic_seed.py). The overhang induction starts at any offset s=0 or 1 inside an image block. The two appended preimage letters are not 22, so their two image lengths total at least 3≥s+2. The image thus contains the requisite translated window, and occurs in p since h(p)=p. The image has no cyclic 22 because each 2 lies at the start of 21. In the fixed-point parsing every 1 ends an image block; 2 is always followed by 1, ruling out 20 and 22. This rules out 00 at a block boundary by descending to 20 or 22, and 11 is excluded because no image starts with 1. A square h^k(a)^2 would end in 1 at a true block boundary. The suffix-free code {01,21,0} forces each successively decoded block to coincide with the actual block, until the entire square descends to h^{k−1}(a)^2. Iteration gives the forbidden aa. Lengths strictly increase since the images of 0 and 1 have length two and both families retain a final 1. This proves the two quantified statements and the Lie-complexity consequence; there is no claim about the squares of other rotations or the entirety of the factor set. The bound script was inspected, not executed; its longer finite run is source-reported.

## originality

PASS

The supported distinct claim is universal occurrence of two extra letters at every cyclic phase of each of the two image-root families in this particular fixed point, together with exclusion of the canonical square. Earlier work on this fixed point gives exact forbidden factors and occurrence of periods of longer overlaps, but these statements do not give the all-phase test with the specified roots. Results on full rotations without squares in other words, including the same-day catalogue comparison, do not cover this assertion. This is a best-of-knowledge statement, not a priority guarantee for general Lie-complexity positivity or for the forbidden pairs.

## value

PASS

The result distinguishes two natural notions of periodicity in a well-studied non-square-free fixed point: every phase of a period can survive two more letters without the canonical two-fold concatenation occurring. It does so uniformly along two unbounded morphic scales. The all-phase propagation and complementary desubstitution give useful structural information beyond a short factor table or positivity of Lie complexity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
