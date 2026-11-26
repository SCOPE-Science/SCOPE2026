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

Using the full-support rate theorem, I reconstructed each block's tuple classes directly from f. The a,b,c singletons split X into sizes 1 and 2, so their entropy is h(1/3)=L-2/3, L=log₂3. The d singleton and all larger blocks have three singleton classes. The first-merge entropy drop is (p_i+p_j)h(p_i/(p_i+p_j)); dividing the rate increase by its negative gives bc = -2/3, ab and ac = -(2/3)/h(4/9), ad = -8/[15h(4/5)], and bd and cd = -5/[9h(1/6)]. The last five are strictly smaller using h(4/9)<1, 5^5<2^12, and 6^6<32·5^5. Partitions P and Q have block masses (4,10,1)/15 and (10,5)/15, with rate difference (L-h(1/3))/15=2/45 and entropy difference (5 log₂5-8)/15>0 since 5^5>2^8. For independent X,Y, coarsening replaces the block partitions of X by their common refinement under the same X law, increasing rate weakly. For |Y|≤3 a strictly better two-block alternative improves both deltas from the singleton start and so has strictly larger slope; neither endpoint can strictly dominate. For |X|≤2 with independence, blocks are either constant-only or distinguishing; same-type merges have zero rate cost and mixed merges positive cost if both source symbols have positive probability. The algorithm therefore remains at minimum rate until the one-block endpoint. This checks the dimension statement in the stated independent-source regime. Independent numeric replay, node /workspace/replays/4.js, recomputes all 15 partitions from the function table: unique first slope -0.666666666667 and gaps approximately 0.240642698296 and 0.044444444444. The proof, not these decimal results, establishes strictness and minimality; the uploaded checker was not executed.

## originality

PASS

The full-support entropy formula and the greedy algorithm are prior. The distinct content is a unique first choice strictly dominated in both objectives, and the impossibility of that failure at smaller stated alphabet dimensions. The inspected literature does not give either result or claim a general guarantee that the witness would contradict.

## value

PASS

For a specified heuristic used to avoid enumerating the partition lattice, an iterate that is worse in both objectives is a meaningful failure mode, stronger than simply missing a feasible tradeoff. The unique first merge removes any tie-breaking explanation, and the lower-dimension obstruction shows why this instance is a natural smallest counterexample under independence rather than an arbitrary finite test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
