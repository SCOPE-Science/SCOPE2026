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

# Reproducible checks and proved limits

`verify_cone.py` is a self-contained Python 3 script using `itertools` and `collections` only. Run `python3 verify_cone.py` from the directory containing the files. Successful execution prints `PASS` with the graph counts.

The exhaustive finite portion covers every labeled simple graph of orders \(2,3,4,5\) (\(2+8+64+1024=1098\) graphs), plus six explicitly listed graphs on six vertices, for 1,104 graphs in total and 431 bipartite cases. It checks all assignments of edge and spoke signs, their exact integer Euclidean squared norms, the complete-cut equality condition, the bipartite degree identity, and the farthest-vertex multiplicity.

The mathematical argument, rather than the finite sweep, establishes the result for every integer \(m\ge2\). The central step is the exact formula
\[
\|(d+s,-\sum_i s_i)\|_2^2
=\|d\|_2^2+m(m+1)-4\left(|S|(m-|S|)+\sum_{i\in S}d_i\right)
\]
together with \(-\sum_{i\in S}d_i\le |\partial_HS|\le |S|(m-|S|)\). All assumptions, quantifiers and contact-equality criteria are spelled out in `RESULT.md`.

No external proof assistant, independent audit, or exhaustive enumeration beyond the stated finite instances is claimed. The implementation requires no external datasets, network access, or downloaded third-party papers.
