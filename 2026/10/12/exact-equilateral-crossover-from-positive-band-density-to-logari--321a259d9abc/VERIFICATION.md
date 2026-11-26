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

Using Exner–Pekař Eq. (2.10) and Sec. 4 (not the low-energy Eq. (3.5)), the equilateral coefficients have a common sin(πk) factor. Its positive-integer zeros are flat for every phase. For k>0 off the integers the divisor 8k²ℓ²(1+c)² sin(πk), c=cos(πt/3), is nonzero. I independently expanded the normalized polynomial, obtaining 9(y+1)² sin²(πk)+4(3y+1)(cos θ−1), and checked 9(y+1)²−8(3y+1)=(3y−1)² for y=b_t²k². Thus real θ gives precisely the stated inequality over the whole t range. At fixed b_t>0 the threshold is 2√6/(3b_t k)+O(k⁻³), varies by O(n⁻²) on a large cell [n,n+1], and 2arcsin(A)/π is Lipschitz in A there. Freezing between cell extrema and summing C/n+O(n⁻²) gives C log K+O(1) with C=4√6/(3πb_t). In the scaled limit the thresholds converge uniformly after writing k=Kx. The min/max cell comparison still works at A=1 by uniform continuity of arcsin on [0,1], so a Riemann sum proves the profile; the last cell is negligible. At τ=0 the constant fraction is 0.783653104061… . With a=πℓτ/6, averaging 2arcsin(A(z²))/π over [0,a] gives (4√6/(3π)) log(a)/a+O(1/a), yielding the stated prefactor. Flat bands and k=0 cannot change Lebesgue measure. Read VERIFICATION.md and verify.py without executing the bundled script; a separate exact polynomial expansion corroborated the analytic reduction.

## originality

PASS

The general determinant, commensurate flat bands, endpoint checks and qualitative loss of band density have substantial prior coverage. The distinct supported result is the quantitative fixed-interpolation logarithmic measure and the integrated t=τ/K profile, both obtained from the interior equilateral reduction.

## value

PASS

The source has different order-of-limits behavior at and away from the Kirchhoff endpoint. The exact cutoff-dependent crossover resolves which intermediate scales of interaction still give positive momentum density and quantifies the subsequent decline. The logarithmic coefficient adds a rate and constant not encoded by qualitative zero density. These are usable benchmarks in a symmetric instance of the interpolation, without claiming unequal-edge, energy-measure or negative-spectrum results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
