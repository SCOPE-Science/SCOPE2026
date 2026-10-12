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

# Finite verification and proof boundaries

Run `python3 verify.py` with Python 3.10 or later and the standard library. The script explicitly constructs the triangular graph, computes all closed edge neighborhoods, and independently tests both clauses of liar's vertex-edge domination for subsets of the two smallest candidate cardinalities through \(n=6\). It checks the exact triple-incidence reduction to cardinality \(n=8\), and checks the labeled-tree counting identities through \(n=24\). Captured output is `verification_output.txt`.

The verifier does not exhaustively enumerate every cardinality for larger graphs and does not prove the infinite theorem or global literature novelty. The theorem's infinite lower bound, construction, component classification, and enumeration are proved in `RESULT.md`. Independent audit has not been performed.
