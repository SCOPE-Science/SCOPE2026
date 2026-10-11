---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Black's rule was reimplemented directly from pairwise majorities plus the Borda fallback. Independent exact enumeration over all anonymous profile pairs gives zero reinforcement failures for totals 2 through 8 and exactly 12 at total 9, split 6 of size 1+8 and 6 of size 4+5. Candidate symmetry gives exactly two pair classes of orbit size 6; the 12 pairs have six distinct unions, each occurring twice, and those unions form one candidate orbit. The two independent route logic in the assigned verifier is consistent with this replay.

## originality

PASS

The sharp nine-voter existence is prior, but the complete boundary structure was not found in the inspected literature. The audited result identifies all 12 unordered pairs, exactly two pair orbits, one union orbit, exactly two paradox-producing decompositions per union, and the distinct Condorcet/Borda mechanism patterns.

## value

PASS

A complete classification of the first reinforcement boundary for Black's canonical Condorcet-then-Borda rule is a natural finite structural result. The pair-orbit, union-orbit, partition multiplicity, and rule-branch split add mathematically meaningful information beyond a minimal witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
