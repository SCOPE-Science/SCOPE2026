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

No four coplanar makes the first four a projective basis, and the fifth has no zero coordinate in that basis. Scaling the four basis vectors uniquely fixes the fifth at [1:1:1:1] projectively. The forbidden planes for the sixth point are the four coordinate planes and the six equality planes obtained from two coordinate points and the all-ones point. Thus a unique normalized ordered sixth entry is (1,b,c,d) with four distinct nonzero coordinates, giving 120 and 2184 classes. Dolgachev §2 Eq. (2) is the defining determinant in the frozen convention. I independently enumerated the zero locus by Gaussian elimination on the actual 4×4 matrices, with no use of the six-term expansion or the uploaded script. For each field the reproduction uses reciprocal irreducible polynomial moduli with an inverse check for every nonzero element, and covers 585 or 4369 projective points by last-nonzero-coordinate normalization. Permutations of b,c,d permute the corresponding projective coordinates and determinant rows, preserving counts; the 20 or 364 sorted triples therefore exhaust all configurations with weight six each. Replay with `python3 /workspace/independent/weddle_census.py` (NumPy) returned {145:120} and {417:1440,433:144,449:600} exactly, with representative chart counts. All counts concern rational points on the singular quartic, with no resolution contribution. F8 and F16 are successive admissible sizes of extensions of F2, not an extension of F8 by F16.

## originality

PASS

The distinct conclusion is the complete two-field histogram on the singular quartic, including the middle F16 stratum and all multiplicities. Dolgachev's equation, normal form and type-D4 geometry are not new. The strongest exact indexed overlap gives two concrete F16 point counts under the same convention, but does not establish the remaining stratum or any complete distribution. This is a best-of-knowledge decision, not an exhaustive novelty certification.

## value

PASS

Projective rational-point count is a standard arithmetic invariant of these geometrically specified singular quartics. The bounds are intrinsic: the smallest admissible field and the next admissible size, where the constant census splits into exactly three count values. The full multiplicities, particularly the middle stratum missing from the two known examples, give a usable benchmark for finite-field algorithms or a proposed explanation of the Frobenius strata. This is a complete natural baseline, not a claim of a new geometric classification or an arbitrarily selected sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
