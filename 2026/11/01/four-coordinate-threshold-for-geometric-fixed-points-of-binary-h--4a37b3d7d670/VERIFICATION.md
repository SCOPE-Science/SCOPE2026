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
# Reproducibility and scope

Run `python3 orbit_fixed_checker.py` and `python3 homology_check.py` in the directory containing both scripts (Python 3.10 or newer, which supplies integer `bit_count`). These are self-contained tests with no third-party packages.

`orbit_fixed_checker.py` enumerates orbit representatives independently and computes every pairwise Hamming distance. It checks all four permutation block lengths \(4\le k\le7\) with \(0\le f\le3\), plus \((4,4)\) and \((5,4)\): 18 parameter cases. It explicitly enumerates all cliques to verify component counts and Euler characteristics. `homology_check.py` independently constructs all simplices, assembles mod-two boundary matrices and performs exact elimination for \(k=4,5\), \(0\le f\le3\): eight cases. The expected first Betti numbers for \(k=4\) are \(1,3,7,15\) for \(f=0,1,2,3\), and all the \(k=5\) cases have two components and vanishing positive homology.

The tests do not cover arbitrarily large parameters, do not prove a PL identification with the wedge spaces, and do not furnish independent auditing. The proof in `RESULT.md` establishes the all-parameter result using exact orbit diameters, strong simplicial collapses, and a graph-of-spaces decomposition. No mathematical certification external to the supplied proof is claimed.
