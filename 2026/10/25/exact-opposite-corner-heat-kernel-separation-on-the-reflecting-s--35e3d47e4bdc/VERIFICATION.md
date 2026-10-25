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
# Verification record
The package fixes \(Q=[0,1]^2\) and the Neumann heat generator \(\Delta\). Exact total variation is half the \(L^1\) density difference, equivalently the best measurable test. The proof establishes the triangle sign by the strictly decreasing one-dimensional likelihood ratio, evaluates the Fourier series by explicit triangle integrals, and derives the short-time coefficient using a Gaussian unfolding error smaller than the leading contribution.

Run `python3 verify.py` in the extracted package. It tests five positive times by independent triangular quadrature versus the double spectral series, verifies the predicted sign on sample interior points, and prints small-/large-time comparisons. Numerical agreement alone is not a global or asymptotic proof.

The full-text comparisons were performed with accessible versions of Kolokoltsov (arXiv:1002.4773), Gaubert–Qu (arXiv:1302.5226), and Loper (DOI 10.1007/s10959-018-0848-7). The earlier Karlin–McGregor report could be identified bibliographically but not read in full. Global optimality over every square starting pair is not established.
