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

The bundled `verify.py` computes the rooted Greg-tree refinement in two exact ways. First it uses the classical triangle recurrence recorded by OEIS A048160. Second it expands the species equation \(G=x e^G+u(e^G-1-G)\) coefficient-by-coefficient with rational arithmetic, without using that triangle recurrence. It checks the published A048160 rows through \(n=7\), agreement of the two methods through \(n=10\), the binary extreme \(g_{n,n-1}=(2n-3)!!\), and the graph-weighted orbit totals displayed in the result.

Replay command: `python3 verify.py`. Expected terminal line: `VERIFY_OK`.
