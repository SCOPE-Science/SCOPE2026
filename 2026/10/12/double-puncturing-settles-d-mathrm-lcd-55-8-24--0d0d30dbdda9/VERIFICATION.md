---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Independently expanded the eight published hex generator strings MSB-first, omitted three padding zeros, recomputed GF(2) row rank=8, Gram rank=8 and d=25 by enumerating 255 nonzero words. Independently traversed all binom(57,2)=1596 double coordinate punctures and checked row rank, Gram nonsingularity and all 256 words: 756 punctures LCD; exactly four have minimum distance 24. The (9,18) witness has spectrum 1+49 z^24+98 z^26+53 z^28+9 z^30+10 z^32+28 z^34+7 z^36+z^38. Grassl online table directly reports ordinary binary linear [55,8] lower=upper=24 with its upper deduced from (30,7) <=12; LCD is a subclass, proving the exact value. These are exhaustive finite calculations, not sampled experiments.

## originality

PASS

The source Lim–An–Kim Sept 2026 preprint reports a [57,8,25] LCD code and a shortest-embedding dimension-eight [55,8,23] instance, not by accessible abstract any 24-distance LCD [55,8]. Grassl established ordinary optimal distance 24 in 2001, but an unrestricted [55,8,24] generator does not imply it is LCD; independently nondegenerate punctured Gram matrices close that gap. A decisive residual risk is that the full very-recent preprint or another new LCD table contains the same witness: its primary full text was inaccessible and the authorized Oxford access was safety-blocked.

## value

PASS

Finding exact optimal minimum distance at a named binary LCD length/dimension is a natural coding-theory classification gap; the verified witness improves the published nearby construction to the sharp unrestricted distance and gives four optimal puncturing choices within a specific generator. This is substantive certificate-backed existence, not an arbitrary partial search or a claim of all-code classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
