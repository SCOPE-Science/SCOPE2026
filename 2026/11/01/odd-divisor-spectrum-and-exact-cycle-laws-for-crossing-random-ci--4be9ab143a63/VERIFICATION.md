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

# Reproducibility and mathematical verification

The analytic argument derives the independent midpoint/half-angle law from two independent uniform circular endpoints. Its decisive nonstandard steps are the exact angular Fourier coefficients, Green-function derivative jump, mixed Dirichlet/Neumann boundary conditions, and odd-factor multiplicity count. Each is stated in `RESULT.md` with its domain and normalizations.

The standalone script `verification/check_chord_spectrum.py` uses only Python standard-library modules and successfully runs with output ending `ALL_CHECKS_PASSED`. It independently verifies 30,000 direct crossing decisions against shorter-arc coordinates; six Fourier coefficient identities; ten Fourier-mode eigenfunction quadratures at four radial sites each; all signed multiplicities for odd denominators through 101; and full enumeration of labeled cyclic crossing diagrams for three, four and five chords. A finite partial-spectrum calculation checks rational small-cycle benchmarks.

These finite tests do not prove the complete spectral theorem or exact all-length formula. Those claims are supported by Fourier completeness, Sturm--Liouville Green inversion, integer-factor counting, trace-class powers and convergent Dirichlet series. The full text of one older finite-chord moment comparator could not be obtained; the associated historical-priority limitation is retained.
