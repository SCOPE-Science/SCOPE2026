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

# Verification and limitations

The proof reduces the endpoint norm to a two-component discrete Fourier kernel, compares it to the continuous-frequency infinite-lattice transfer-current kernel by Gaussian-Abel periodization and fourfold image cancellation, and sums the resulting angular \(r^{-2}\) tail. The comparison error is uniformly \(O(n^{-2})\) on centered torus residues, hence contributes \(O(1)\) to the column norm. The angular absolute integral is exactly eight. This is a mathematical asymptotic argument, not an exhaustive finite certificate.

Run `python3 verify_torus.py` with the Python standard library; no downloaded dependencies are required. It independently constructs rational incidence/Laplacian projections for every column when \(n=3,4,5,6\), compares against Fourier reconstruction, tests the exact complementary gap and prints larger Fourier evaluations. Expected exact cut/cycle pairs for those four sizes are \((2,19/9)\), \((5/2,41/16)\), \((68/25,69/25)\), and \((317/105,3839/1260)\). A successful run reports 172 checked columns.

There is no independent mathematical audit or external validation. No conclusion is asserted for minimum projection norms among all linear projections or for a limiting constant in the bounded remainder.
