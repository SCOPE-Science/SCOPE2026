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
# Verification

The bundled `verify.py` uses only the Python standard library and performs two exact finite checks.

For \(m=1,2,3,4\), it enumerates all labeled unrooted trees by Prüfer codes, chooses every root, keeps those in which the old labels \(0,\ldots,m-1\) form a meet-closed substructure, and then examines generated extensions containing one distinguished new point and at most one additional meet-point. It records the complete meet table of each generated extension over the fixed old labels. For every old meet-tree encountered, exactly \(3m\) distinct nonalgebraic extension signatures occur.

It also enumerates every rooted tree with a topological labeling through seven vertices and every nonempty subset \(P\), computes its closure under pairwise meets, and checks
\[
|\langle P\rangle_\wedge|\le 2|P|-1.
\]

Run with:

```text
python verify.py
```

Expected final line:

```text
VERIFY_OK
```

These finite checks test the combinatorial classification and the sharp closure inequality on all instances in the stated ranges. They do not prove the infinite theorem; that proof additionally uses quantifier elimination, density, infinite ramification, and universality of the generic meet-tree.
