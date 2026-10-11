---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Sufficiency is given by direct nonnegative integer factorizations when \(c\mid n\) or \(b\mid n\). For necessity, \(A=RS\), \(B=SR\), and \(\det A\ne0\) force \(R\) and \(S\) nonsingular and hence \(AR=RB\). Writing \(R=\begin{pmatrix}p&q\\r&s\end{pmatrix}\), the intertwining equations give \(q=br\) and \(s=cp\). Solving \(S=R^{-1}A\) yields nonnegative integers \(U,V\) with \(S=\begin{pmatrix}cV&bU\\U&V\end{pmatrix}\). The \((1,2)\) entry of \(RS=A\) gives \(pU+rV=1\), so one of the nonnegative integer products is one and the other zero. The \((1,1)\) entry then forces \(n=cp\) or \(n=br\), proving \(c\mid n\) or \(b\mid n\). Fresh bounded enumeration of the reduced intertwiner form for \(1\le n\le8\) and \(1\le b,c\le5\) found an elementary factorization exactly in the predicted divisibility cases.

## originality

PASS

Baker's classical theorem concerns strong shift equivalence through a chain and explicitly uses higher-dimensional intermediate matrices; it does not classify a single elementary factorization. Jeandel's recent work returns to Baker-type examples and gives explicit multi-step SSE proofs for small parameters, but the accessible primary abstract/author companion does not state the all-parameter one-step divisibility criterion. Targeted Resultary search returned the assigned record as the direct exact hit and no earlier elementary classification. Full Jeandel text could not be obtained in this run, so that source remains an explicit access residual rather than negative evidence.

## value

PASS

Elementary SSE is the atomic move underlying strong shift equivalence, and recent work is explicitly constructing and shortening paths for difficult two-by-two examples. An exact all-parameter criterion identifying when a natural diagonal Baker-type family collapses to one step is therefore a motivated structural classification, with a simple divisibility obstruction that can guide path searches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
