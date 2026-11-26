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

For a named point, a second variable falls into equality or exactly one of the four strict quadrants. A rank-one formula therefore depends only on their nonemptiness, and any rank-two sentence is a Boolean combination of outer quantifications over such one-point types. Conversely, a rank-two existence sentence selects any prescribed mask. The first and last points contribute at most two endpoint masks; the other points have both a left and a right witness and hence nine possible masks. Types 6 and 9 cannot coexist: whichever of their points comes first, the two required value comparisons disagree. This leaves eight internal types. Equality needs all the remaining internal masks, including both global extrema (5 and 10), which force endpoint masks 12 and 3. A type-15 point inflated into an increasing block retains all four external witnesses, and no exterior point changes mask. The n=1,2 cases and all smaller sharp bounds were checked in a fresh enumeration. The independent positional-bitset sweep exhausted all 4,037,913 permutations through length ten; it recovered encoded spectra 64744 and 65192 with 164 each. The dihedral fixed-point counts [328,0,0,0,20,0,0,20] give 46 orbits by Burnside, and stabilizer sizes give 10 size-four and 36 size-eight orbits. This uses a different mask computation and orbit count from the supplied code.

## originality

PASS

The logical mask equivalence is already explicit for unrestricted permutations in the earlier Resultary record 7fe7e8086c11, which also gives witnesses for both ten-mask spectra. These are not distinct contributions here. Credit is for the unrestricted sharp ceiling by size, the forced form of every maximal spectrum with persistence at all lengths, and the exact unrestricted minimal-extremizer and symmetry census. The strongest earlier record answers a different extremal question restricted to separable permutations; its result and certificate do not give the unrestricted upper bound or the census.

## value

PASS

The number of realized logical types offers a natural finite measure of how much a single permutation can exhibit at rank two. The theorem pins down both the first length at which the uniform ceiling is reached and the precise two ways the maximum can look at the level of types. The complete census and symmetry breakdown at the first feasible length are motivated exact invariants of that extremal class, not an arbitrary small-n table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
