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

# Reproducible checks and limits

Run `python3 verify_star.py` with the Python standard library. The accompanying `verification_output.txt` is the recorded stdout from an executed check.

The checker uses an Abrams cubical discretization after subdividing each arm to length \(n+1\). Every selected graph-cell closure is disjoint from every other; all cells are enumerated. For each conjugacy-class representative in \(\mathfrak S_m\), it enumerates all fixed cubical cells, signs each by the permutation of its oriented edge coordinates, and computes the alternating trace. The established radial-tree graph-braid collapse to a graph identifies \(1-L(\sigma)\) with the trace on first homology. This geometric computation is separate from the polynomial-algebra derivation of the proposed formula.

The finite verification covered eleven \((m,n)\) pairs for \(m\in\{3,4,5\}\) and every conjugacy class of the relevant arm permutation group. Each class calculation agrees with the closed character, and the recorded run ends `VERIFY_OK`. The program does not compute exact integral Smith normal forms, test all arm and particle counts, or prove the comparison theorem; the all-parameter result follows from the algebraic proof and the cited established comparison.

No external or independent mathematical audit is recorded.
