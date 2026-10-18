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

# Mathematical verification

The proof in `RESULT.md` establishes the infinite-dimensional exact essential-norm identity, truncation certificate, and sharp Taylor coefficient. The nonstandard steps to verify are: (i) the compactness of the cell-averaging Carleman defect via the squared derivative kernel on distant output cells; (ii) preservation of essential norm when passing to a positive periodic multiplication/convolution operator on the whole logarithmic line; (iii) pointwise domination of each Floquet fiber by the zero-momentum fiber; (iv) the second-order reduced-resolvent correction from the two adjacent frequencies. Each is explicitly addressed in the proof.

The command `python check_spectral.py`, after installing the single dependency listed in `requirements.txt`, constructs the actual finite Jacobi matrices \(P_N B P_N\), verifies norm bounds and evenness in amplitude, and tests the analytic quadratic coefficient for three frequencies and nonzero amplitudes of both signs. The checker uses numerical singular values of finite matrices and **does not independently certify** the infinite-dimensional claims or publication priority.

The finite-section error is an **analytic** estimate, not an empirical error bar: \(\|B-P_NBP_N\|\le(1+|\varepsilon|)c_{N+1}+|\varepsilon|c_N/2\). The asymptotic remainder is valid for each fixed positive frequency and is not uniform as the frequency tends to zero. Literature comparison and possible historically broader Floquet reductions require independent evaluation.
