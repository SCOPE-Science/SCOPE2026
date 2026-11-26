---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The stated symmetric kernel has zero row sums and the degree-Laplacian second differences give L_nG_n=I−11ᵀ/n, including at the endpoint degrees. This identifies the inverse; symmetry equates the absolute row and column norms. At the specified midpoint coordinates, substitution gives G_ij/n=K(x_i,x_j)−1/(12n²). In y, K has slopes y and y−1 on the two sides of x, so |K| is 1-Lipschitz and at most two zeros and the kink give at most three exceptional cell interiors. Summing ordinary midpoint errors bounded by 1/(24n³), exceptional errors bounded by 1/(4n²), and the shift 1/(12n²) gives 7/(8n²). On 0≤x≤1/2 the positive part of K has right boundary 1−√(1/3−x²); its left boundary is zero up to r=1−1/√3, then √(2x−x²−2/3). Differentiating twice the positive-part integral yields the stated first derivative on each regime, negative off the endpoints and center by the displayed factorization. The endpoint value is 2/(9√3); its deficit is x²/√3+O(x⁴) and is at most x²/√3 for x≤r. Taking x_0=1/(2n) proves the two-sided uniform bound and forces every maximizing row to within a bounded offset of an endpoint. For fixed k, the row change is δ=k(k+1)/(2n) plus j−k when j<k. The latter corrections sum to −k(k+1)/2 and occur at eventually positive entries of both rows. The smooth-crossing slope of row zero has magnitude bounded away from zero, so replacing the absolute-value change for the δ term by its signed value costs o(1); its signed sum tends to k(k+1)(2r−1)/2. Thus F_(n,0)−F_(n,k) tends to k(k+1)/√3. This excludes each positive bounded offset by reflection, proving eventual strictness. Row zero decreases through the midpoint root, so summing twice the entries through the last nonnegative index gives the stated floor formula, including the harmless zero-entry case; row signs and column unit masses attain the respective norms. An independent exact flux-balance replay through n=80 confirms all finite comparisons, including strictness against every interior row and the radical error bound. The frozen checker itself only asserts weak endpoint optimality, notwithstanding the source's verification wording; the separate replay does not replace the analytic eventual proof.

## originality

PASS

The pseudoinverse kernel and continuum Neumann Green function are credited as known. The distinct supported contribution is the maximum absolute row sum: its sharp discrete floor formula in the eventual range, endpoint-only attainment there, fixed-offset gap and explicit uniform bound. None of the materially inspected adjacent statements supplies that norm or its maximizing row for the unshifted path inverse. Full text of the most relevant path pseudoinverse paper remains unavailable through the attempted lawful routes, so that comparison is limited, not negative evidence of coverage.

## value

PASS

The maximum row sum is the sharp maximum-amplitude response to a bounded input with automatic mean subtraction on a finite insulated interval. Obtaining both its exact eventual finite-size constant with an extremizing input and its explicit n-uniform error is more useful than just knowing the kernel entries or a continuum estimate. The fixed-offset asymptotic identifies the order-one difference responsible for discrete endpoint selection. The result is bounded to a canonical family and does not claim a general theorem for graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
