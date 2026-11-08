---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For n>=2 and a cyclic shift plus b(n-1)=0, H(i,j)=nd-i for 2(j-i)<n and (n+1)(n-(j-i))-n-i otherwise. Direct boundary casework at j=n-1 shows no transition lowers H by more than one and exactly one letter lowers it by one, including the n=2 degenerate boundary. Rank intervals for d and n-d partition 1..n(n-1)/2, so each rank occurs once. The unique maximal pair follows a rank-decreasing Hamiltonian path, giving one master word with all optimal suffixes. Independent reverse BFS was recomputed on all 2300 pairs through n=24; all agree. The general n result follows from the rank-descent proof.

## originality

PASS

Best-of-knowledge: Gusev transition data may make the odd-case theorem derivable, a substantial residual O risk; neither inspected paper states the whole both-parity theorem. The exact maximal value itself is explicitly excluded from claimed novelty.

## value

PASS

This completely classifies shortest merging trajectories for each named pair in a fundamental synchronizing automaton, beyond the already known maximum pair length. A rigid distinct distance spectrum and one master suffix supply exact reproducible extremal examples and structural information, useful in synchronization/automata research. This is not a generic BFS table or merely the known upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
