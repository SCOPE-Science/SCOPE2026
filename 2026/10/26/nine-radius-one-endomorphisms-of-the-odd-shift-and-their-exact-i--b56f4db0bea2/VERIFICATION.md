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

The gap condition is equivalent to support on a single parity, including the zero point and finitely supported points. The only relevant local triples are 000, 001, 010, 100 and 101. The first bit must vanish. If 010 has output one, any active bit for 001, 100 or 101 could be tested on the opposite parity alongside a distant isolated one, violating preservation; the remaining map is identity. Otherwise the three off-center bits are free and act by the eight two-input functions vanishing at (0,0), onto the opposite phase with a harmless shift of coarse index if needed. All five triples occur, so distinct permitted truth tables give distinct restricted maps, and the three irrelevant bits give eight codes per map. Projection, identity and binary difference are onto; the rise/fall images avoid 11 and have explicit predecessors obtained by reading the target directly or shifting it. AND outputs avoid 101, and a preimage of a target b avoiding it is a_k=b_(k-1) OR b_k. Complementing yields the OR image avoiding 010. These three proper coarse languages, the zero image and the full odd shift are distinct, as can be checked using 11, 101 and 010 on the unique nonzero phase. Under the square of the spatial shift, each phase is the corresponding coarse shift; the entropy of their union is the maximum of the two equal coarse entropies. The coarse adjacency polynomials are t^2-t-1 and t(t^3-2t^2+t-1); the cubic's derivative is (3t-1)(t-1), with opposite signs of the cubic at the golden ratio and 2. The entropies therefore have the stated strict ordering and half-log normalization. For difference, fixing one coarse coordinate fixes the entire antecedent recursively in both directions. Nonzero outputs determine their source phase, while at zero the two constant choices on each phase yield three antecedents after counting the common all-zero point just once.

## originality

PASS

The supported distinct claim is the complete centered-radius-one odd-shift self-map census with exact image languages and spatial entropy spectrum. Salo's Rule 18/90 equality is explicitly prior; the fibre formula is an elementary derivative consequence once the phase split is observed, not an independent priority claim. The closest exact table uses the even shift, and the full-shift or finite-ring spectra do not determine which restricted maps preserve the odd shift or what their image languages are.

## value

PASS

This is a complete natural small-radius classification for a standard sofic shift, not just a code count: it identifies the exact proper image subshifts, two distinct images of equal entropy, every onto map and the exceptional zero fibre. These are reusable facts about closure and factor behavior of the odd shift; the easy XOR restriction alone does not supply them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
