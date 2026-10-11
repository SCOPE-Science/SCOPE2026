---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Because a finite local nonfield has zero-divisor ideal \(\mathfrak m\), the classical total-graph structure theorem gives, after deleting zero, \(K_{s-1}\dot\cup(q-1)K_s\) if \(2\in\mathfrak m\), and \(K_{s-1}\dot\cup((q-1)/2)K_{s,s}\) otherwise. Zero forcing is additive over components, with \(Z(K_t)=t-1\) for \(t\ge2\), \(Z(K_{s,s})=2s-2\), and \(Z(K_1)=1\). Rank-one clique blocks and rank-two complete-bipartite blocks give a pattern matrix of rank \(q\) for \(s\ge3\); the boundary \(s=2\) has \(q=2\) and graph \(K_1\dot\cup K_2\), of real minimum rank one. Thus \(M\le Z\) closes the lower bound. Minimum sets omit exactly one allowed vertex per residue component, giving \((s-1)s^{q-1}\). Fresh direct residue-graph enumeration reproduced \((Z,\#\min)=(2,2),(5,12),(5,18)\) for \(\mathbb Z_4,\mathbb Z_8,\mathbb Z_9\).

## originality

PASS

Anderson--Badawi provide the exact clique/complete-bipartite residue-coset decomposition, but study connectivity and metric/cycle behavior rather than zero forcing or minimum rank. Mishra--Patra do study zero forcing around a total graph, but for \(\mathbb Z_n\) with respect to the nil ideal, with zero retained and a separate reconfiguration graph; their formulas do not state the deleted-zero local-ring theorem or its real minimum rank. Resultary searches found no earlier theorem combining the all-local classification, the deletion boundary, every minimum forcing set, and residue-field recovery.

## value

PASS

The result gives a complete forcing and inverse-eigenvalue classification for an entire natural class, including a sharp small-ring boundary, every minimum forcing set, and recovery of the residue-field and maximal-ideal sizes from graph invariants. This goes beyond a single routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
