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

Run `python3 verify_homotopy.py` with Python 3. This program has no nonstandard package dependencies. It enumerates exact signed-permutation coordinates over \(\mathbb Z[t]/(t^3-t^2-t-1)\), and checks the edge relation against squared distance \(2+4t-2t^2\) by integer polynomial coefficients. It independently enumerates every nonempty face and constructs the stated staged matching. It orients all cover edges in the full face poset and topologically sorts the directed graph to establish acyclicity. It computes the signed algebraic Morse boundary via exact gradient cancellation and verifies the prescribed nine-by-nine determinant equals \(-1\).

Run `python3 verify_independent.py` using only Python 3. This separate reconstruction uses 50-digit decimal coordinates, an include/exclude recursion, and bitwise Gaussian elimination of the complete simplicial boundaries over \(\mathbb F_2\). Its expected face vector is \((24,216,912,1854,1680,564,48,3)\); its expected boundary ranks are \((23,193,719,1135,519,45,3)\); its unreduced Betti vector is \((1,0,0,0,26,0,0,0)\).

The proof of the integral homotopy type requires the first program's acyclic matching and unimodular integral Morse boundary. Neither an integral-homology rank computation nor a finite-field homology calculation alone would prove the wedge decomposition. The programs exhaust this fixed finite complex but do not make claims about other snub solids. Independent external validation has not been performed.
