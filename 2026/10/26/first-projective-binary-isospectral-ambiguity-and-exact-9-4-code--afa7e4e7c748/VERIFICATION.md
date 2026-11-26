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

A full-rank binary generator with distinct nonzero columns is a set of projective points; coordinate permutations and change of basis identify exactly its GL orbit. An independent replay enumerated all ordered bases to generate GL(k,2) explicitly (rather than growing the orbit by transvections). For k=1 through 4 every subset was inspected or marked as an image in an orbit; a zero weight for a nonzero information vector detects lack of full rank. The resulting 1, 2, 6 and 36 full-rank classes have pairwise distinct sorted nonzero weight lists in each dimension. The dimension-zero projective case allows only length zero. For length ≤7 and dimension ≥5, an independent short proof replaces the frozen small-length census: the dual has dimension at most two and its enumerator is fixed by MacWilliams. In dimension two the three nonzero weights, assigned up to GL(2,2)=S_3, determine the three nonzero column multiplicities by the pairwise-sum equations and the common length then gives the zero multiplicity. Dual dimensions zero and one are immediate. Dualizing commutes with coordinate permutation. The two [8,5] witnesses are full-rank and projective, and direct exact enumeration confirms both the indicated polynomial and the weight-two information-vector sets {8,16,24} and {2,8,16}. Their different ranks force, under every isomorphism, both a stretch ≥3/2 on a source weight-two word and a stretch ≤2/3 for some target weight-two word's preimage. The stated independent basis images yield the full weight-pair table and exactly those extrema, proving 9/4. This value concerns the designated pair only; the exclusion census assumes projectivity.

## originality

PASS

Credit the prior classes and aggregate counts entirely to Bouyukliev, and the general exact distortion problem to Bennett–Fox–Morrell. The short-length exclusion is also an elementary consequence of MacWilliams and the dimension-at-most-two dual calculation, not a standalone new classification. The supported distinction is the combined first projective binary full-enumerator collision boundary and the weight-layer rank obstruction and attaining map for the designated pair. The historical classification contains both classes and could be used as input to calculate the spectra, but the inspected aggregate tables do not determine the full spectra or their collisions, and the complete online representative data could not be inspected. A prior nonprojective isospectral distortion family does not violate or settle this boundary.

## value

PASS

Weight enumerators are basic invariants and projectivity excludes multiplication of columns, a natural mechanism behind easy counterexamples. Giving both sharp exclusion axes and a smallest projective collision answers when this strong invariant first ceases to classify. In the first dimension and length, inequivalence has a compact geometric explanation in the minimum layer, which also provides the exact optimal distortion rather than merely detecting its difference from one. This ties the independently useful boundary to an intrinsic metric comparison; the class counts are not counted again as a contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
