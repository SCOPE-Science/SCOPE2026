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

# Reproduction and scope

The attached `verify_census.cpp` was compiled with C++17 `-O3` and successfully run. It enumerated every one of the \(1{,}048{,}575\) nonzero binary cubics and all \(35\) rational lines, generated the complete set of \(840\) extremal coefficient masks in `extremal_coefficients.txt`, and produced `census_output.txt`.

The independent `verify_numpy.py` was executed with NumPy. It expands each restricted monomial by a separate parity algorithm, computes the list of squarefree binary cubics by polynomial Euclidean gcd, checks rational singularity conditions on all forms at or below the claimed threshold, and compares the entire \(840\)-mask set. Its actual output is `numpy_output.txt`.

The `verify_orbit.py` script was executed with SymPy. It independently builds the complete \(20{,}160\)-element linear group from four generators, calculates the orbit of coefficient mask `67194`, checks literal set equality with the certificate, and symbolically verifies all four derivatives used in the smoothness argument. See `orbit_output.txt`.

All commands assume the files are unpacked into one working directory: `g++ -O3 -std=c++17 verify_census.cpp -o verify_census && ./verify_census`; then `python verify_numpy.py` and `python verify_orbit.py`.

The lower bound uses the *necessary* condition of nonsingularity at rational points to safely discard candidates, while the representative's full geometric smoothness plus orbit coverage establishes the *sufficiency* for all extremizers. No finite extension sampling substitutes for a geometric proof. This is a bounded exhaustive proof only for the \(20\)-dimensional space over \(\mathbf F_2\); it is not a claim about higher fields or degrees.
