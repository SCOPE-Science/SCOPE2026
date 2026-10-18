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
# Verification and reproducibility

This document records direct checks of the stated mathematics, not independent auditing or certification.

**Analytic checks:** The complete-product graph has a balanced \(K_{mn,mn}\) component containing the initial opposite-edge tensor states. The local degree on that component is \(mn\), so the one-step coefficient is \(2/(mn)-\delta\). The two-step coefficient matrix is the reshaped product \(G\otimes G^{\mathsf T}\), divided by \(\sqrt2\). A trace calculation yields \(\operatorname{tr}(GG^{\mathsf T})=1\). Enumerating every nonzero two-by-two minor gives \(4(m-1)(n-1)/(m^2n^2)\) for the product of its nonzero eigenvalues. Thus the two eigenvalues are exactly \(\mu_\pm\) as in RESULT.md. Tensor singular values give the full claim, including multiplicities.

**Executable checks:** Run `python3 verify.py` with Python 3 and NumPy. The script independently constructs all directed arcs and iterates the two-particle state using the unreduced product-graph Grover transition rule. It compares the nonzero squared singular values of the complete amplitude matrix, its entropy and normalization against closed forms at each time from zero through four, for nine graph sizes and both initial signs. The run passed all **90 time/size/sign comparisons**, along with six fixed-edge balancing comparisons. The tests include the exactly rational cases \(K_{2,2}\) and \(K_{2,3}\) and the rank-deficient stars.

**Verified boundaries:** At \(K_{1,1}\), the rank remains two and the entropy is \(\log2\). At \(K_{2,2}\), the time-two spectrum consists of eight equal entries \(1/8\). At \(K_{2,3}\), the time-two spectrum is \((2/9)^{\times2},(1/9)^{\times4},(1/18)^{\times2}\). For both part sizes at least two, the Schmidt rank is eight exactly at residue two and four at odd residues. No exhaustive enumeration over unbounded part sizes is claimed; the all-size argument is the matrix calculation in RESULT.md.

**Limits:** Floating-point tests have explicit tolerances and do not themselves prove integer-uniform results. The treatment does not test alternate coin conventions, graph families, or operational entanglement extraction protocols. The related original literature was inspected for claim coverage; absence of a match is not a mathematical uniqueness certificate.
