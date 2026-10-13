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
The embedded `verify_pg_nucleolus_proper_first_layer.py` performs an exact finite replay using only the Python standard library.

A simple game is represented by its antichain of minimal winning coalitions. Every proper game through four players is enumerated and canonicalized under all player relabelings.

Public Good is computed independently by its normalized participation-count formula and by an explicit player-coalition incidence multiset.

The nucleolus is computed by exact rational successive least-core linear programs. At each stage every vertex of the small feasible polytope is generated from tight constraints, the optimum maximal excess is found exactly, and coalitions whose excess is fixed over the entire optimum face are carried into the next stage until the allocation is unique.

The two divergent classes also have direct certificates. In \(\{AB,AC\}\), player \(A\) is the unique veto player, so the core and nucleolus are \((1,0,0,0)\). In \(\{AB,ACD,BCD\}\), the three key excesses are \(1-a-b\), \(b\), and \(a\), forcing least-core value \(1/3\), \(a=b=1/3\), and \(c+d=1/3\); symmetry then gives \(c=d=1/6\).

The verifier confirms:
- proper-game counts \(1,3,11,80\) for one through four players;
- proper isomorphism-class counts \(1,2,5,14\);
- no Public Good/nucleolus ranking divergence through three players in the proper domain;
- exactly \(18\) divergent labeled proper four-player games;
- exactly two divergent isomorphism classes with orbit sizes \(12\) and \(6\);
- the displayed exact Public Good vectors and nucleoli;
- the displayed weighted representations;
- \(50\) proper four-player games with no dummy and exactly \(6\) nondummy divergences;
- exactly \(3\) nonproper three-player divergences, all in one isomorphism class.

Run:

`python3 verify_pg_nucleolus_proper_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary through four players.
