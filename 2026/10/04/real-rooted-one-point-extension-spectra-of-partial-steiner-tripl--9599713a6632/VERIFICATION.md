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

The proof is deductive; the checker supplies finite independent sanity checks.

`verify.py` enumerates every labelled partial Steiner triple system on \(n\le7\) old points by backtracking subject to pair-disjointness of blocks. The census is
\[
1,1,2,5,26,271,5596
\]
for \(n=1,\dots,7\), totaling \(5902\) systems.

For every such system it forms the leave and computes
\[
\sum_k m_k(L)z^k
\]
by an exact vertex-deletion dynamic program. It checks the normalized Newton inequalities coefficientwise and verifies
\[
E_A(1)\le I_n
\]
with a unique maximizer, the empty partial triple system. The maximum totals through seven points are
\[
1,2,4,10,26,76,232.
\]

As an independent check of the central bijection, for every labelled partial Steiner triple system on at most five old points (\(35\) systems total), the script directly enumerates every subset of candidate new blocks \(\{x,u,v\}\), tests pair uniqueness, and compares the resulting rank counts with the matching-DP coefficients. All agree.

It separately checks the Fano Steiner triple system, whose leave is empty and whose polynomial is \(1\), and checks the complete-graph matching coefficient rows for empty systems through seven points. Running the script prints `VERIFY_OK`.

The finite checks do not prove real-rootedness for arbitrary size. That step in `RESULT.md` invokes the Heilmann-Lieb theorem for graph matching polynomials and the exact change of variables \(\mu_G(t)=t^nE_A(-t^{-2})\).
