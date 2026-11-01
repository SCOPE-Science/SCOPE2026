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

# Scientific verification
The standalone file `verification/triangular_prism_verify.py` uses only the Python standard library. It reconstructs all radii from the actual graph edges and enumerates exactly \(3^6=729\) possible centered-ball selectors. The integer matrix \(1044I-5T^{\mathsf T}T\) is checked by fraction-free leading-minor elimination against the threshold \(29/20\); exactly \(723\) selectors are certified strictly below it and exactly six exceptions are found. The exception list equals the automorphism orbit of \((0,1,2,1,0,2)\), one for each distance-two pair.

For the exceptional integer Gram matrix \(T^{\mathsf T}T\), exact Faddeev–LeVerrier characteristic coefficients agree with \(x^2(x-144)(x-18)(x^2-246x+7488)\). Dividing eigenvalues by \(144\) gives the radical squared norm. The proof independently derives the positive eigenvector from \(34a^2+73a-17=0\) and verifies all strict maximizing-radius comparisons analytically for \(0<a<1\). Numerical comparisons in the code are consistency tests only.

Run: `python3 verification/triangular_prism_verify.py`.
Expected first line: `CERTIFICATE_OK selections=729 strict=723 exceptional=6 distance_two_pairs=6 characteristic=exact`.

No general graph-family assertion, alternative exponent, or independent scientific certification is inferred from the finite check.
