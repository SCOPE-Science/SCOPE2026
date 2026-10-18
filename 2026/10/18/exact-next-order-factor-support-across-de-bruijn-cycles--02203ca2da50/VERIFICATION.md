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

# Reproduction of finite support checks
Run `python3 verify.py` from the directory containing `verify.py`. Python 3 standard library suffices. The program builds each full order-\(n\) de Bruijn graph, contracts the arcs corresponding to a proposed length-\(n+1\) word, computes a shortcut Euler circuit, expands it, and checks all cyclic windows. Cases cover \(q=2\), \(2\le n\le7\); \(q=3\), \(2\le n\le4\); and \(q=4\), \(2\le n\le3\). There are 1,175 candidates. A separate recursive traversal exhausts all binary cycles for \(2\le n\le4\) and verifies the exact union in these cases; the numbers of cycles are 1, 2, 16. See `verification_output.txt` for the recorded output ending in `ALL CHECKS PASSED; contracted instances=1175`.

Finite checks cannot establish the infinite quantified theorem. The proof is the vertex-deletion Hamilton-path lemma plus the complete one-vertex residual-degree analysis after arc contraction. No independently performed audit or external formal verification is represented by this file.
