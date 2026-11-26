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

Read inverse letters right-to-left in a forward word. Inverse a rotates occupancy and crossing indices by -1; inverse b copies the bit at d into 0. A shrinking copy clears 0 when d is empty; its incoming edge loses any crossing, and the outgoing edge still cannot be a 0-to-1 crossing. Non-growing copies thus cannot create crossings. In every path to a larger set the first growth is a copy, with some original surviving crossing rotated to 0; fewer than r=min E_d rotations cannot do that. The word ba^r attains r+1. No crossings means constant occupancy on each d-orbit; rotations preserve this condition and copies then fix the set, so the infinity case covers precisely the unions of the orbits. With gcd=1, ignoring starting edges i>=t leaves disjoint directed paths for t<n, each allowing exactly the nonincreasing binary strings, v+1 per path. At t=n only the two constants remain, and differences cancel those constants at all lengths. The final deleted edge has source n-1 and the path starts at n-1+d, proving the unique longest set of each size; d=1 gives the single explicit path and isolated vertices. Independent preimage-layer BFS, using preimages built from forward maps, agreed on 45 automata and 16,298 nontrivial subsets, both n=7 example vectors, all coprime path products, and the claimed extremizers. Finite enumeration is supplemental.

## originality

PASS

The exact d=1 overlap is explicit in the published catalogue, but its date is later and its theorem does not cover general d. The simultaneous bounds at arbitrary displacement (including absence of extension) and displacement-dependent coprime spectrum are distinct from the strongest compared statements.

## value

PASS

The invariant already arises in extension proofs in the literature. Counting exactly when the bound n-1 fails, including one extreme subset per size, yields information unavailable from reachability or an example of failure. The complete labeled length distribution discriminates displacements even when coprimality gives identical existence answers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
