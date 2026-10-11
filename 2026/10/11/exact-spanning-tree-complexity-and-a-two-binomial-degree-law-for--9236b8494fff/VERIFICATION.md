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

# Reproducibility of the signohedral tree identities

Run `python3 verify.py` using Python 3's standard library from the directory containing the source file. The program constructs the ternary-grid graph by enumerating all nonzero signed ternary strings, and independently assembles its reduced integer Laplacian. An exact fraction-free Bareiss cofactor computes \(\tau(G_m)\), which is compared against the closed product for \(m=2,3,4\).

For the completed grid, the same graph builder adds one grounded center with edge weight \(t\) to each of the \(2m\) unit-vector neighbors. For every \(t\in\{0,1,\ldots,2m+1\}\) and each tested \(m\), a second exact determinant checks the weighted central-degree polynomial. Since the polynomial has degree at most \(2m\), the \(2m+2\) values for each \(m\) determine the entire polynomial for those test cases. The terminal line is `VERIFY_OK exact Bareiss minors, all stated sample values, and weighted tree polynomials`.

The observed punctured-tree counts are \(8\), \(301056000000\), and \(477039212109540892237246917021020454912000000000000\). They are exact integers, not floating-point approximations. The proof for arbitrary \(m\ge2\) is mathematical and separate: its essential nonstandard step is an explicit spectral calculation of the two nonconstant eigenvalues of a grounded neighbor Green matrix, yielding the displayed two-binomial law. The verifier checks only the declared finite dimensions and does not certify novelty, all-dimensional truth, or independent validation.
