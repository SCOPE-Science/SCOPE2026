---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Read RESULT.md and exact edge_erasure_checker.py from source blobs. The complete-biclique gradient subspace is the two-way additive arrays, with projector P_{(i,j),(k,l)}=δ_{ik}/b+δ_{jl}/a−1/(ab). Its negative entries are exactly disjoint-edge columns, yielding full norm. Because K_ab minus one edge remains connected even at a=b=2, restriction to retained edges is injective on gradients. Sherman–Morrison on the restricted Gram matrix proves P_minus=RPRᵀ+(RPe)(RPe)ᵀ/(1−P_ee). The three retained-edge row orbits have explicit negative masses and row sums L_A,L_B,L_C; differences L_C−L_A=2(a−2)/[b(a−1)(b−1)] and L_C−L_B=2(b−2)/[a(a−1)(b−1)] are nonnegative, yielding precise max and boundary ties. Every row norm attained with sign input; holds over real/complex arrays. Independently inverted grounded rational incidence matrices for five (a,b) test graphs, all orbit row norms checked. All integers follow from algebraic sign formulas, not finite tests.

## originality

PASS

Relevant published research-index and primary literature comparisons found no directly covering exact claim, subject to the explicit priority limitations. The novel result is the exact claim stated, not its previously known foundational object or general theory.

## value

PASS

Gradient projection is the least-squares potential recovery operator in network Hodge theory. Single-link erasure on a complete rectangular bipartite measurement design is a natural robustness operation; the exact two-parameter decrement, row maximizers and boundary exceptional ties quantify worst-coordinate amplification rather than an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
