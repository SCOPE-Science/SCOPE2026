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

The scientific claim is finite and reproducible with standard Python 3. Run `python3 verify_direct.py` and `python3 verify_characterization.py` from the folder containing the included files. Compare their standard outputs with `verify_direct.out` and `verify_characterization.out`. The former uses full distance vectors and exchange graph traversal; the latter uses shortest-path-derived pair-separation masks and exhaustive equality checks against the explicit formula and translation families. Both enumerate every four-subset of each 16-vertex graph, and all smaller subsets for the lower bound. All two-exchange breadth-first searches run from every minimum basis.

The proofs of the rook metric dimension and general rook resolving-set criterion are previously published (Cáceres et al., arXiv:math/0507527). The Shrikhande dimension-four value is also previously published (Bailey, arXiv:1312.4973). The new finite structure and capacity statements are checked as described in the included programs and the Result proof. No unbounded parameter range or mathematical uniqueness beyond the two specified graph isomorphism types is asserted.

Independent scientific audit has not been performed. The checks are computational verification, not third-party certification.
