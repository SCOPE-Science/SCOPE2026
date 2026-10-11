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

# Reproducibility
Run `python3 verify.py` in this directory. The only dependency is the Python standard library (Python 3.9 or later). It must terminate with `VERIFY_OK`. The verifier independently enumerates all edge subsets of sizes one through five for complete graphs on \(4\) through \(7\) vertices; computes domination by testing all vertex sets of size \(n-3\); checks each resulting face vector; and computes every signed simplex trace at a representative of each symmetric-group conjugacy class. It separately checks the three critical local \(S_4\)-orbit representations on disjoint edge pairs, four-vertex paths and four-cycles; computes irreducible characters by the Murnaghan--Nakayama rule; and tests the character identity up to \(n=12\).

These checks verify arithmetic, finite face classification and local representation character tables. They are not an exhaustive computational proof for arbitrary \(n\); that uniform step follows from the published homology-concentration theorem, equivariant Euler--Poincaré, and the horizontal-strip rule as demonstrated in `RESULT.md`. No independent audit or external validation has been performed.
