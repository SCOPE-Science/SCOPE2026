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

# Verification of the weighted Walsh-star projection formula

The analytic proof gives the result for all integers \(m\ge2\) and all real weights \(w>0\), with explicit matching upper and lower bounds. It does not depend on a finite search. Independent finite checks construct every vertex and weighted coordinate edge, form the Walsh projection matrix directly from characters, and maximize its output edge differences under all input edge constraints using linear programming. The provided program checks \(m\in\{2,3,4,5\}\) at weights \(0.5,1,1.5,2.5,m,m+1\), giving \(24\) full finite-dimensional parameter instances and \(48\) optimized edge directions. The maximum values agreed with the binomial formula to an absolute tolerance of \(2\cdot10^{-8}\); the program explicitly asserts these comparisons.

Run `python verify_weighted_walsh.py` using NumPy and SciPy. These LP computations are floating point; neither the LP solver nor any finite parameter grid constitutes a formal certificate for the infinite family. The proof's nonstandard step is the radial antipodal bound \(2|g_k|\le m-2k\), obtained from an actual path of that many light-coordinate edges with nested negative-coordinate sets; the same clipped function attains this bound for every radial level simultaneously. The single-edge derivative bounds and the uniqueness of the averaged Fourier projection complete the reduction.
