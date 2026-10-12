---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof has two independent components.

First, the published distance-class estimates for a uniquely decodable binary-adder pair give
\[
N_k\le {3\choose k}\min(2^k,2^{3-k}),
\]
so summing over \(k=0,1,2,3\) yields \(1+6+6+1=14\).

Second, the equality analysis is direct: product \(14\) forces cardinalities \(2\) and \(7\). If the two words on the small side have Hamming distance \(r\), then there are exactly \(2^{3-r}\) disjoint potential cross-row collision pairs among words of the full cube. Removing only one word can eliminate all collisions exactly when \(r=3\), and then that removed word must be one of the antipodal endpoints.

`verify.py` exhaustively enumerates every ordered pair of nonempty subsets of the eight-word cube and checks injectivity of ordinary integer-coordinate addition. It reports maximum product `14`, exactly `16` ordered extremizers, only size profiles `2x7` and `7x2`, and the claimed antipodal-minus-one structure. `verification_output.txt` records the replay output.

The computation is finite and exhaustive for block length \(3\). It is not used as evidence for any larger block length.
