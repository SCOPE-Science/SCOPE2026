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

The frozen last paragraph of proof is false as an order-preserving strategy: with four rounds and lengths 12 and 11, choose opposite points in length 12; next choose the midpoint of the length-six gap whose matched gap has length at most five. Unless the diagram already fails, an order-preserving response has a directed subgap of length two where the corresponding length is three. The last move witnesses that two-edge path. Thus the frozen proof does not establish its upper bound, but the theorem survives. The replacement maintains exact clockwise distances up to 2^r with r rounds left. Copy signed offsets within 2^(r−1); comparing two such offsets uses a signed difference of magnitude at most 2^r, so consistency transfers in both directions. For a move remote from all k=q−r previous selections, at most k(2^r+1)<2^(q−1)+3 vertices are forbidden in the response cycle, so a remote response exists. Rank zero then preserves S and equality. The independent lower-bound proof uses two distance balls, of radii a,b ≤2^(q−3), covering the cycle. Contiguous intervals give a length cutoff 2a+2b+2, or 2a+2b+1 when enforcing overlap by a distance bound between the centers. Boolean composition and binary splitting of distances keep the sentence within rank q. These cutoffs fill all lengths through 2^(q−1)+2 and transfer via E(x,y)=S(x,y)∨S(y,x). The small-rank cases and the relational scope are checked separately.

## originality

PASS

The accepted distinct content is the sharp all-rank directed upper bound and, in combination with the known undirected profile, the all-rank equality of partitions. The indexed exact directed profile through five and the rank-two colored comparison cover genuine portions, but neither yields the sharp tail at arbitrary ranks. The replacement supplies a stronger uniform bound than the 2^q general directed bound of the strongest finite-rank source. No novelty is credited for the undirected thresholds, EF characterization, or low-rank overlapping cases.

## value

PASS

The repaired theorem determines the least logical depths separating every pair of sizes in a natural relational signature and shows exactly that orienting the cycle gives no gain in this invariant. The distinction between the optimal directed bound and the usual order-preserving sufficient bound matters at every rank q≥4. The usable signed-offset strategy explains this gap rather than just confirming a list of small sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
