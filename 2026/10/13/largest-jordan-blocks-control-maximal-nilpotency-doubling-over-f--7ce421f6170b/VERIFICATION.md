---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

In F_q[eps]/eps^2, (A+eps B)^m=A^m+eps*sum_{i=0}^{m-1} A^i B A^{m-1-i}. If A^r=0 and A^{r-1} nonzero, the 2r power vanishes while the (2r-1) power is eps A^{r-1} B A^{r-1}. For P=A^{r-1}, B->PBP has rank rank(P^T tensor P)=s^2, giving q^(n^2)-q^(n^2-s^2) lifts with maximal index and probability 1-q^(-s^2). Nilpotent Jordan theory identifies s with the number of blocks of size r; includes A=0, r=1. Independently exhausted six small binary Jordan-type strata and agrees.

## originality

PASS

Şentürk--Özbay Theorem 2.5 proves nilpotence equivalence and displays the 2r upper-bound expansion, but does not classify the exact maximal-index stratum, its codimension or finite-field density. A published single Jordan block finite-dual calculation treats s=1, while the present multi-block dependence on multiplicity s gives new exact uniform coverage. Best-of-knowledge PASS with risks of a more general prior result.

## value

PASS

The maximal nilpotency-index condition for arbitrary multi-block real part is a natural sharp stratum of all dual lifts. Its exact density depends only on the number of largest Jordan blocks; this is an independently useful structural classification beyond checking a tiny example or merely reproducing the 2r upper bound. The full lower-index distribution is explicitly outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
