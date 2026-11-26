---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed the rank using the Gram span of the vertexwise products ψ_E,i overline(ψ_E,j) within common energy spaces, from the complex-Hermitian Cesàro projection. A nonzero Bloch block has energies ±|a+b exp(iθ)| and flat intensities, so simple levels all give the same all-ones direction. Since ab>0, distinct cell angles can share a positive magnitude only as negatives of each other, which requires 0 or π flux modulo 2π. For such a pair the product lies at cell shift frequency ±(j−k), with two-sublattice line of coordinate ratio equal to one of the squared phases of a+b exp(iθ). The signed energy blocks generate the same product lines. At odd m the congruence 2j=ℓ or 2j+1=ℓ has one solution for each ℓ≠0, giving one line per activated frequency. At even m it has either two or no solutions. The two angles differ by π; parallel lines would make the quotient of the two complex off-diagonal entries real, contrary to Im[(a+b exp(iθ))(a−b exp(−iθ))]=2ab sinθ. At the self-inverse nonzero frequency the two orientations of a single collision still give independent conjugate lines, since θ=±π/2 and a,b are both positive. The counts are m/2−1 nonzero even frequencies at zero flux and m/2 odd frequencies at π. Finally a=b and θ=π produces two independent sublattice intensities at frequency zero rather than just the uniform direction. It occurs exactly at the claimed parity and twist boundary. This accounts for all product vectors, including m=2 and a=b, and gives exactly the stated table without tolerance-based rank inference.

## originality

PASS

Credit is limited to the joint two-band exceptional-flux rank law for genuinely dimerized rings and its rank transition at gap closing relative to the known uniform cases. The equal-hopping slices have material prior coverage; generic rank one uses the standard flat-simple-eigenvector argument. The passages inspected do not already yield the exact exceptional-flux collision ranks at arbitrary positive alternating hoppings.

## value

PASS

Rank of the stationary Cesàro transition map measures the dimension of distinguishable initial-site information in time-averaged position readout. The exceptional ranks give a complete classification for a natural clean dimerized ring, and isolate exactly when a closing band gap adds a sublattice memory mode. That distinction is not available from generic flat-eigenvector mixing or the uniform cycle alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
