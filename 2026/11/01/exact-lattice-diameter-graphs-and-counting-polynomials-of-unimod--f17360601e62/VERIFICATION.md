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

# Reproducibility and mathematical checks

Run the included standard-library script using `python3 verify.py`. It enumerates integer points from first principles, examines *every* unordered pair in each finite instance, calculates coordinate-difference gcds, constructs the diameter graph, traverses the connected components, checks complete adjacency within each component, and compares computed values against the claimed formula. It does not obtain graph edges from the claimed equality characterization. It also transforms boxes by explicit unimodular integral matrices and verifies that the same counts persist.

The actual script execution returned `PASS 207 independent finite axis-box and unimodular-image instances (all pairs enumerated)`. Exhaustive parameter sweep: all positive integer side-length vectors with dimensions one through four and lengths one through three; dilations one in every dimension and also two in dimensions at most three; plus 48 unimodular image cases. Representative output is displayed by running the script. No third-party libraries, network, or unspecified data are needed.

The infinite proof uses four independently inspectable deductions: (1) every gcd is bounded by the longest dilated side length; (2) equality forces each difference coordinate to be zero or its full longest-side displacement; (3) the endpoint/interior pattern gives pairwise-adjacent binary corner choices and freezes all other values; (4) a binomial sum gives the segment count and a componentwise falling-factorial product gives the chromatic polynomial. An integer unimodular matrix preserves lattice points and gcd because both the matrix and inverse have integral coefficients.

Finite checks support but do not establish any quantification over arbitrary dimensions or side lengths. The result does not cover arbitrary lattice parallelepipeds whose edge basis has determinant of absolute value greater than one, nor nonintegral dilations. The best-knowledge historical comparison is not a substitute for an independent literature audit.
