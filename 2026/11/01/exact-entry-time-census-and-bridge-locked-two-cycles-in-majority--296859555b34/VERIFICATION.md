---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The neighbor-one counts are k-z at a nonbridge clique vertex and k-u+v at its bridge vertex. For odd m=2q+1 the nonbridges settle to clique majority in one step and an exceptional bridge (k,u,v)=(q+1,1,0) or (q,0,1) settles on step 2; inclusion-exclusion gives s2=2H(2^m-H). For even m=2q, the k=q class flips nonbridge colors and transports the opposite bridge bit; all unbalanced classes collapse to uniform. The both-balanced opposite-bridge subset is the complete primitive two-cycle class (C^2/2 states); exactly-one-balanced classes split into 2-,3-,4-step cases and yield s0=4+C^2/2,s1=U^2-4,s2=CU+C^2/2,s3=C 2^{m-1},s4=C(2^{m-1}-C). The m=2 path is separately (6,6,4). Independent direct neighbor-list bit simulation exhausted all 4^m states for m=2..6 and checked histograms and 2-cycle orbits; universal proof is by exhaustive clique case split, not simulation.

## originality

PASS

Bounded best-of-knowledge originality after comparing equivalent mathematical statements, stronger-coverage implications and relevant primary material. No inspected source is shown to imply the target exact statement; incomplete historical coverage is retained as a risk.

## value

PASS

The single bridge between two highly connected communities is a canonical network bottleneck. Exact parity-dependent recurrent oscillation population, complete basin entry histogram, and sharp four-round delay refine broad convergence bounds in a mathematically motivated family; separate recurrence probability and long-delay probability are genuine dynamical invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
