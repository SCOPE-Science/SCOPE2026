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

# Verification and limits

Run `python check_pineapple.py` with SymPy. The program checks five universal symbolic rational-function identities for the objective differences and exact full-matrix inverse traces for all distinct two-vertex leader sets on the finite graphs with \(2\le r\le9\), at six positive rational gains. Each computed matrix is the combinatorial Laplacian with the two selected diagonal entries increased by the gain. The graph's all-order proof is in RESULT.md; the program does not establish the infinite quantifier. All order assumptions, tie cases and positivity arguments are stated there. Independent audit has not been performed.
