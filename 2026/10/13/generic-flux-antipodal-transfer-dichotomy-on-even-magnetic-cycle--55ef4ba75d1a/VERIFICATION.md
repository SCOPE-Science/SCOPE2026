---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The frozen proof assigns 2 cos(phi+2πk/n) to the positive-exponent mode, but the specified right shift acts on column-vector coordinates by (Tf)(j)=f(j-1). The frozen check_fourier_matrix instead evaluates the opposite shift, so its stated check does not catch this. The replacement files use the negative-exponent mode with the original eigenvalue and the target phase ζ^(jk), and the checker now exercises the stated right shift. For the corrected proof, the balanced relation criterion follows from continuous-time Kronecker on frequency differences, including possible degeneracy. The ± eigenpairs force n|2j. For every odd prime divisor p, the two disjoint length-p cosets based at 0 and 1 have zero eigenvalue sums and opposite target parities. Their rotated phase products differ by 2 in modulus; telescoping and Cauchy–Schwarz bound that difference by 2 sqrt(pn(1-|A|)), giving the stated gap. For power-of-two n and transcendental tangent, rational frequency relations split into two algebraic sums, so cyclotomic divisibility by x^(n/2)+1 forces equal coefficients on the paired indices. As n/2 is even, every balanced relation satisfies the antipodal parity test. At exact transfer two eigenvalue pairs would make 4t cos(phi) and 4t sin(phi) integer multiples of 2π, contrary to transcendental tangent. The parity-reversing index involution k↦n−1−k still cancels antipodal terms at phi=π/n. Algebraic tangent values and poles exclude at most countably many phases, also after projecting to total flux. No theorem hypothesis, conclusion, or quantitative constant changes in the repair.

## originality

PASS

For the corrected finding, the distinct contribution is the uniform magnetic-cycle dichotomy including the phase- and time-uniform p-dependent cap for every odd prime divisor. The unphased criterion, general Hermitian spectral principles and exact half-flux cancellation have verified antecedents and are not credited as distinct contributions. The strongest inspected statements do not establish the full magnetic classification and cap; no uncatalogued equivalent is ruled out.

## value

PASS

Uniform flux is a natural perturbation of the familiar unphased cycle. The correction preserves a phase-uniform robust obstruction with an explicit numerical margin for every odd prime divisor, as well as the contrast with PGST at almost all fluxes on power-of-two cycles. A qualitative failure at selected fluxes is insufficient for this quantitative stability distinction. The already known half-flux cancellation serves only to show why almost-everywhere cannot be replaced by everywhere.

The dated certificate retains the supplied scientific assessment, sources and limitations.
