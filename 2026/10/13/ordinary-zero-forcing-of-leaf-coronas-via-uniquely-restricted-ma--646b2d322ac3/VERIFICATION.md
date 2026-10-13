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

# Verification of leaf-corona zero forcing

Run `python3 verify.py` in any Python 3 environment. The script uses the standard library only and reconstructs the actual adjacency matrix of each attached-leaf corona, followed by an ordinary forcing process. It separately reconstructs donor peeling from initially selected leaves and empty pairs; it compares the entire coefficient distribution against a separate sum over disjoint cut parts. It tests all base graphs with at most four vertices and all their initial blue sets, then seeded graph samples up to seven vertices, for 500,260 boolean comparisons, plus 5,421 direct matching-versus-peeling comparisons. For \(K_n\circ K_1\), with \(2\le n\le9\), it checks each coefficient against \((2x+x^2)^n+n((2x+x^2)^{n-1}-x^{n-1})\) and minimum-set counts; for \(2\le n\le8\), it additionally checks inclusion-minimality by removing each chosen vertex.

Expected output is provided in `verify_output.txt` and terminates in `VERIFY_OK`. These tests do not exhaust all graphs beyond four vertices, and do not independently certify the infinitely many quantified cases. The theorem's universal assertion is established by the written proof, not by finite sampling. The literature comparison does not eliminate every possible unindexed equivalent theorem.
