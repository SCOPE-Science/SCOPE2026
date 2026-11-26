---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With a zero share one can give that agent nothing: a positive-share agent's singleton part blocks at most one part of a second positive-share agent's three-part partition. In a failure with all shares positive, two distinct singleton goods in different agents' partitions block at most two parts for the third agent and would give a fair allocation. Thus all singleton parts coincide; the other two parts form a matching, and equal matchings for any two agents likewise give a fair allocation. The decisive all-bundles step is that every 3-subset of the remaining four goods already contains an edge of each matching. A newly accepted singleton admits an edge of a different agent avoiding it; a newly accepted nonmatching pair has a complement in another agent's matching. In both cases the remaining agent takes the common singleton. Conversely distinct matchings cannot supply disjoint edges on four vertices. All accepting partitions must use the common singleton by size, giving uniqueness. The binary realization achieves share 1 and the five choices of singleton and six agent assignments give 30 patterns, one relabeling orbit. For at most two goods all shares are zero; on three goods positive-share agents accept each singleton, and on four goods two different singletons and a third avoiding part always exist when needed. Independent bitmask allocation check: `cd /workspace && python audit_checks.py 5`; 1, 216, 15625 profiles at sizes 3, 4, 5, respectively, with 0, 0, 30 failures and all 720 single-bundle extensions restoring feasibility. The finite checker supplements the proof for arbitrary real-valued monotone utilities.

## originality

PASS

The supported contribution is the all-bundles rigidity in every failing profile, equivalently maximality of the obstructing acceptance families: permitting even one formerly unacceptable bundle restores feasibility. The sharp size, the example, the partition-triple necessity and classification, and the resulting count at partition level are already covered and are not independent contributions. The all-bundles claim is explicitly the frozen theorem's main assertion, not a replacement theorem.

## value

PASS

At the first possible failure size this classifies the entire acceptance profile, not just partition witnesses. The maximality statement tells a researcher whether a putative counterexample survives an arbitrary additional threshold bundle, and provides an exact base case for extending rainbow MMS obstructions. The short proof adds a distinct diagnostic even though the partition classification and minimal example already exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
