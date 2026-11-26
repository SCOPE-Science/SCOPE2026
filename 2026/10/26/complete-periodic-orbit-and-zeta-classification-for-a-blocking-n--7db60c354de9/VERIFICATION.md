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

The rule number and polynomial describe disjoint swaps of each isolated zero with the 1 immediately to its left (also consistent on rings of size 1 and 2). Once a zero belongs to an adjacent pair it never moves; while mobile it advances one site each step and hence cannot complete a circuit past an original permanent zero pair. This proves the bound and recurrent split. The only word avoiding both forbidden blocks is all ones. Pair-state closed walks give the indexed cyclic no-101 word count (including the small-ring repeated indices); the characteristic polynomial is u(u³−2u²+u−1) and the first traces are 2,2,5. The matrix is irreducible with a loop, hence primitive. The complementary traveling sector repeats an admissible word of length gcd(N,t) under the t-th iterate, giving the Lucas term and Möbius cycle and zeta formulas. Independent functional-graph enumeration from the integer truth table reproduced every sector, transient bound and iterate count for N=1–14 and t=1–2N; replay: python3 /workspace/branches/replay_3_4_5.py 3. The frozen verifier's loop actually checks fixedness after N+1 steps, not N (verify.py lines 43, 49–50). The independent replay checks true entry time, and the universal bound follows from the proof, not the frozen computation.

## originality

PASS

Credit the local particle dynamics to the earlier rule papers, the fixed/traveling languages to that dynamics, and the counting tools to standard transfer and necklace methods. The assessed contribution is the exact finite-ring temporal spectrum for this particular rule: a global capture/translation argument identifies which two spatial languages suffice, and their indexed counts yield every time-iterate trace and primitive period. Neither inspected rule paper gives that finite-ring result or a more general orbit formula specializing to it.

## value

PASS

For an established blocking, number-conserving rule, the exact temporal orbit spectrum answers which finite periodic motions survive and how many trajectories have each primitive period, across all ring sizes. It gives concrete counts for fixed points, translating states and the asymptotic dominance of the frozen sector without constructing exponentially large transition graphs. Its value is the complete finite-ring invariant, not a new local motion law or a new general zeta method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
