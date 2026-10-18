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

# Verification scope

The reproducible program `triangular_tube_verify.py` constructs the local three-column condition and the independent vertex-neighbour geometry. It checks component sizes \(31\) and \(7\), internal arrow counts \(79\) and \(10\), and the two exact characteristic-polynomial identities using integer arithmetic in SymPy. The full 64-state transfer graphs are specified by the same local rule as the mathematical proof, so checking their finite structure is a finite exact certificate, not a simulation over unbounded lengths.

The program independently enumerates all site occupancy bitsets for \(n=4,5,6\), both thresholds, and matches their counts against transfer traces and the three-choice vacancy-gas formula where applicable. Length seven is separately compared against transfer and hard-core counts. A rational positive-vector Collatz bound localizes the threshold-four Perron root, and exact Sturm counts identify its ninth-degree factor. Numerical eigensolutions approximate densities and the positive empty-column probability.

Execute with `python triangular_tube_verify.py`, using Python 3 and SymPy plus NumPy for the final numerical values. The exact infinite-length claims rest on the cyclic-walk bijection, matrix polynomial identities and Perron theory, not on the small-system enumeration. The historical 1981 article's complete text was unavailable for originality comparison; external independent validation has not occurred.
