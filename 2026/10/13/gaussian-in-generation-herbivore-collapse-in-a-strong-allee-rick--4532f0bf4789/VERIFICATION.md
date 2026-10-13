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

# Reproducibility and verification

Run `python verify.py` in the directory containing this file. The checker uses only Python 3 standard-library arithmetic and prints `VERIFY_OK` on success. The checker has been executed on the packaged source and produced `VERIFY_OK` for three distinct positive parameter sets.

The script checks the biomass-partition update against the original two-component recurrence for the first twelve positive iterates. It then follows the exact logarithmic recurrence without prematurely treating extremely small herbivore biomasses as zero and computes the finite partial sums defining the constants \(C,D\). At generations 100, 160 and 230 it compares the normalized plant and herbivore logarithms to their asymptotic constants. The sample runs involve \((r,b,a,x_0,y_0)=(1,0.25,1.3,0.12,0.14)\), \((2,0.2,0.8,0.07,0.4)\), and \((1.5,0.3,2,0.22,0.03)\).

**Mathematical scope.** The verifier is a finite numerical consistency check; it does not certify an infinite-time statement. The proof requires (i) positive eventual contraction \(f(x)\le\rho<1\), (ii) the weighted absolute convergence of \(\delta_j\), (iii) convergence of the analytic correction \(\phi_j\), and (iv) the exact logarithmic product identity. Each step is supplied independently in RESULT.md. The essential assumptions are strict positivity, \(q=f(0)\in(0,1)\), and eventual extinction. Neither coordinate-axis data nor the boundary \(q=1\) are covered.
