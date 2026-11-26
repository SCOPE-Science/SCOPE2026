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

For a divisor d, write k=td+u, 0≤u<d. Select t complete column cosets of the subgroup of size d, plus u more columns. On any fixed residue class of rows modulo d, the columns within one coset have proportional restrictions, so the rank of the complete cosets is at most Σ_j min(t,m_j) for residue sizes m_j. With the extra u columns this gives a singular minor if any m_j<t. If u>0 and a class exceeds t+1, its complementary occupancy is below the corresponding floor for the complement; if u=0 an oversized class forces an undersized one in the original set. Jacobi's identity and F⁻¹=F*/15 give complementary-minor equivalence, so these cases prove necessity. Row translation scales columns and multiplication by a unit permutes columns; hence one representative per affine orbit through size seven suffices. Independent audit_fourier.py exhausts the balanced orbits, classifies them without assuming the exception list, and tests column ranks modulo 31 at an order-15 root. A modular nonzero certifies complex nonvanishing. For ambiguous minors it instead computes the determinant as a wedge-product subset DP in Z[X]/(X¹⁵−1) and divides by Φ₁₅ over Z, an exact complex test. All five listed witnesses have identically zero group-ring coefficient vectors. The five bad orbit sizes are 30,120,120,60,30 in listed order. For the good reps, 53803 minors pass mod 31 and the other 1125 have nonzero cyclotomic remainders. Full-spark counts through size seven are 15,60,60,180,60,180,600 and double by complement to 2310. The full matrix is invertible by Fourier orthogonality.

## originality

PASS

Uniform divisor distribution is a prior necessary condition, and prime-power sufficiency, affine symmetries, and complementary-minor duality are not the contribution. The distinct claim is the complete complex order-15 classification of the balanced failures, including five affine exceptions up to complement and the census resulting from them. The closest preceding catalogue result at the same order treats one unbalanced four-row pattern; it does not classify any of the balanced exceptions. The primary results inspected concern other orders, a necessary condition, or principal minors. Later exact rank tables overlap in specific cardinalities. The frozen prose would be clearer to distinguish previously catalogued classifications at 10, 12, and 14 from journal results; the reviewed sources do not establish a journal attribution for each of those full classifications.

## value

PASS

Order 15 is the smallest odd composite order that is not a prime power. It tests exactly where divisor balance stops being a complete characterization in the odd semiprime setting, and gives a concrete nonmonotone pattern: balanced five-row failures, none at six rows, and four balanced failure orbits at seven rows. The exact orbit witnesses and exhaustive positives give a useful benchmark for uniform sampling and for testing proposed criteria beyond prime powers, not merely an isolated determinant calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
