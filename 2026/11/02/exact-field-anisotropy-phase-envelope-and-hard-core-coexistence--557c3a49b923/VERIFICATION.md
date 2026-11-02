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

# Computational and analytical verification

Run `python3 checker.py` in the directory containing `convex_certificate.json`. The checker is self-contained and uses only Python's standard library. It constructs the ten vertices of \(KG(5,2)\) as all two-subsets of a five-set and exactly reproduces the 15 edges from disjointness, checking degree three at each vertex.

Two structurally distinct complete enumerations of all \(59049\) three-valued spin configurations produce identical counts for all 318 nonempty \((b,k,m)\) classes. The checker verifies the exact minimum bond energy in every one of the 36 nonnegative-magnetization occupancy sectors and all 36 rational convex-mixture witnesses. Each witness certifies a continuum lower bound in the anisotropy and field variables, not just a sampled point. The seven displayed branches have individually checked strict-exposure parameter witnesses and exact interior counts of 5, 20, 10, 5, 5, 1, and 1 configurations.

At the saturation junction the independently counted Petersen independence polynomial is \(1+10z+30z^2+30z^3+5z^4\). Insertion of \(z=1\) and \(z=2\) returns 76 and 461, as derived algebraically. Seven additional exact-rational critical-point degeneracies are reproduced. The text in `checker_output.txt` is the output of a successful replay.

The proof is restricted to a finite homogeneous classical Hamiltonian. No computer search proves priority over unseen publications, physical realization, thermodynamic-limit behavior, or external scientific certification. Independent audit has not been performed.
