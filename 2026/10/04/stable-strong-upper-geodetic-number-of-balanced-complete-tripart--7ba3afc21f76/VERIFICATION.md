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

The proof was reconstructed from the definitions, including the quantifiers implicit in fixing one geodesic for every selected pair and the capacity restriction that one selected same-part pair supplies only one internal-vertex slot.

The key feasibility step was checked independently by a maximum-flow model rather than by directly coding the displayed Hall inequalities. The verifier exhaustively checks every part-count triple for each \(12\le n\le30\), then checks minimality by all possible one-vertex deletions. It confirms \(\operatorname{sg}^{+}(K_{n,n,n})=n+2\) and exactly the three permutations of \((2,2,n-2)\) as maximum patterns throughout that range.

The finite check is not an infinite proof. The theorem for all \(n\ge12\) rests on the symbolic Hall characterization and deletion inequalities in `RESULT.md`. No independent audit or formal proof-assistant verification has been performed.
