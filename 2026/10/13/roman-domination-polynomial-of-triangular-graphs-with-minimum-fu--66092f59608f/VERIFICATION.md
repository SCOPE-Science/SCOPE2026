---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Fix an edge set H carrying label 2 in K_n. The set C of its endpoints must support a graph with no isolated vertices, and every edge among the remaining r=n-|C| vertices is forced to label 1. Choosing C in binom(n,c), the no-isolate graph supports in A_{c,k}, and freely assigning 0/1 to M-k-binom(r,2) remaining edges yields the exact displayed sum plus the no-2 all-ones contribution z^M. The lower bound 2 ceil((n-r)/2)+binom(r,2) has unique extremal r=1 odd and r=2 even, giving matching minima with counts n(n-2)!! and binom(n,2)(n-3)!!. Independently enumerated every label n=3..5 and all minima n=3..12. The proof establishes n>=5, experiments do not generalize it.

## originality

PASS

Zec 2023 gives scalar gamma_R(J(n,2))=n-1 and examples but not all coefficients or exhaustive minimizing function counts. The 2021 polynomial paper defines the same invariant on other families; complete-multipartite formulas cover T3,T4 only. Other edge-Roman scalar results do not imply this full all-weight formula. The later same-repository duplicated n>=3 record was actually imported AFTER this n>=5 original (two minutes later) and is not prior coverage of this earlier research statement.

## value

PASS

Every coefficient of an established domination polynomial for a canonical infinite Johnson-graph family is a natural invariant and the complete equality-case classification explains the parity-dependent set of minima. The result is not a recomputation of the known scalar optimum or a finite arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
