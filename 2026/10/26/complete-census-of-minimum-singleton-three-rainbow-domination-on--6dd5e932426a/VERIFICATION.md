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

At weight n+2 the zeros are an independent set, with exactly one per rung outside the two completely colored rungs. For a run, the two end-neighbor colors and the run's positive colors in between form a sequence whose sliding triples must have all three colors, so the first two distinct labels force the rest by period three. Its endpoint matrix is 2I if the run length is 2 mod 3, J−I otherwise. For adjacent holes there are 108 colorings per unordered pair, including n=3. With nonadjacent holes the zero-row difference between the two run ends changes parity by n−4. Thus for odd n one hole shares its constrained vertex and one does not, giving 144 colorings per pair; summing gives 108n+144(C(n,2)−n)=36n(2n−3). For 6|n, two orientations have both endpoints shared, two neither. For the shared case the count before free colors is tr(R_p R_q), correctly using symmetry to reverse one run. The directed-distance counts are 288,180,180 for the three residues of d mod 3, each occurring n/3−1 times, and the directed sum must be halved even for opposite holes. Adding adjacent holes gives 108n(n−2). This proves the replacement without assuming the minimum theorem. The same kernel gives the frozen rest of the table: no holes require both cyclic periods two and three; one hole shares the endpoint iff n is even; for the remaining even two-hole cases the trace values reduce to 6 and 0, with 180 at one distance residue and 72 at the other two. No falsity is alleged for those removed branches.

## originality

PASS

The earlier same-model minimum-weight theorem and the distinct indexed census have substantial coverage of the frozen claim. Neither determines the two repaired branches where weight n+2 is nonoptimal. The full cylinder paper was recovered via the open static PDF, and its relevant theorems are bounds/exact weights, not the claimed counts. The repair claims only the nonminimum weight-(n+2) cases, not either minimum invariant or priority.

## value

PASS

The two nonminimum branches finish a natural low-weight coefficient across all circumferences, after accounting for the complementary classes where the optimum census already supplies it. These are exhaustive symbolic counts for infinite classes, not an arbitrary set of extra examples, and the contrast between odd (one shared hole) and even (two or none) explains the differing multiplicities. A researcher using low-weight terms of the labeling polynomial cannot substitute the optimum count for these branches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
