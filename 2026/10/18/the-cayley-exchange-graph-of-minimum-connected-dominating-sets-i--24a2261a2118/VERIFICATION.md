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

# Finite reproducibility checks

Two standalone Python 3 programs with only standard-library imports implement different exhaustive constructions. Execute `python3 verify_subsets.py` and `python3 verify_group.py`. Captured outputs are included as `verify_subsets.out` and `verify_group.out`; each ends in `VERIFY_OK`.

The subset program visits every \(k\)-element subset of the sixteen-vertex four-cube for \(1\le k\le6\), checks induced connectivity and domination, builds all one-token jump and adjacent slide edges, computes all-root shortest-path histograms and shortest odd closed walks via a parity double-cover. It verifies \(\gamma_c=6\), exactly \(192\) minima, degree four, \(384\) jump edges, zero slides, the uniform distance layers \((1,4,10,23,45,76,30,3)\), and odd girth \(11\).

The second program instead grows all connected subsets by frontier extension, constructs the special direction-word paths, enumerates the affine even-permutation group of order \(192\), verifies its free and transitive action on minima, and checks every generator-defined edge against an independent token-jump test. It then computes all Cayley word lengths and the shortest odd relation. This directly checks the critical structural group identification rather than merely repeating graph statistics.

These are exhaustive verifications of a finite claim. No untested higher-dimensional extrapolation is asserted. They do not establish historical originality, and no independent external scientific audit has been performed.
