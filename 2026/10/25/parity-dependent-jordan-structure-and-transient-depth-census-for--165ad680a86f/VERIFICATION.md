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

# Verification of the mathematical classification

Run `python3 kautz_parity_verify.py` from the directory containing the two accompanying reproducibility artifacts. The program independently generates all admissible Kautz words, builds outgoing-neighbour adjacency, performs exact binary linear algebra, and exhaustively simulates every initial binary configuration when the graph has at most twelve vertices. Its output is retained in `verification_output.txt`.

The program checks the power-rank law for 26 parameter pairs, 149 GF(2) matrix-power identities, and a total of 8,788 exhaustive initial configurations. The checks include both alphabet parities, length-one graphs, and the two-letter degeneracy. The complete all-parameter theorem depends on the explicit algebraic proof, not on numerical extrapolation.

The originality search was limited by unavailable full text of one related 2008 article. No independent external audit or certification has been conducted.
