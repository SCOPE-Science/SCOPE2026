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

Every nonscalar 2x2 matrix is cyclic, and its matrix centralizer is span{I,A}; each commuting nonscalar family member therefore has a unique u_j I+v_j A, v_j!=0. Any nonscalar conjugate has entries (a,b;c,t-a), with bc=a(t-a)-d; all offdiagonals nonzero iff a not in Z and all diagonal shifts nonzero iff a not in E. For each eligible a, precisely q-1 nonzero (b,c) products occur, giving N=(q-1)(q-|E union Z|). Centralizer-orbit division establishes the change-of-basis count. The q=2^m obstruction partitions field into pairs {s,s+1}; q=5 pair has E={0,1,2,4}, Z={3}. Independent exhaustive matrix quadruple enumeration over F5 found zero admissible common conjugates and exactly eight per individual member.

## originality

PASS

A scalar orbit parameterization turns published one-matrix fully-nonzero existence into an exact simultaneous count and detects obstruction to combining individually eligible bases. Marcoux et al. abstract covers individual fields and some quaternionic simultaneous results, not a finite-field commuting-tuple counting law in accessible text. The full recent paper could not be read through public or authorized access; maintain explicit possible covering theorem risk.

## value

PASS

For a canonical commuting two-dimensional finite-field problem, the exact count and the threshold q>2k+2 decide simultaneous full-support feasibility; concrete q=5 and infinite even-characteristic obstructions show a mathematically meaningful difference between individual and joint similarity that single-matrix existence cannot reveal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
