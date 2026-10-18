---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: Let P_m(n) be coefficients of the m-th product term. Expansion in y=e^{−t}−1 with integral coefficients divisible by y^m implies m!|P_m(n), uniformly truncating m≥3r modulo 3^r. For m<3r inclusion-exclusion expresses terms as sums of K_S^n and Euler/Carmichael periodicity gives eventual period 2·3^{r−1}. For r≥2, normalized first-third-shift at h=2·3^{r−2} depends on K_S modulo 9; the factor with 2j−1=9 (j=5) pairs/cancels all m≥5. Exact m≤4 subset sums produce residue 2 for even n and zero for odd. Modulo three a(n) alternates, so all eventual periods are even; the nonzero first-third shift excludes all proper divisors. Independent dual coefficient recurrences plus direct subset-residue check corroborated r=1..4 at tested indices, not the infinite statement.

## originality

PASS

PASS: Read Kallat's entire seven-page 2026 arXiv manuscript and its theorem/proof of the all-moduli Carmichael eventual period. It supplies an upper period for 3^r, but no proof that the period is minimal nor the parity-dependent first-third-shift obstruction. OEIS A158690 describes Bala's conjecture and initial values. Thus the exact all-r ternary least period is not an immediate implication of the cited upper bound. Unindexed equivalent work remains possible.

## value

PASS

PASS: The least eventual period is the sharp invariant behind Bala's periodicity question. Proving the Carmichael period is attained at every ternary prime-power modulus, with a uniform explicit nonzero half-shift digit, resolves the first odd-primary sharpness tower and explains its contrast with dyadic reductions. This is an infinite statement with a structural cancellation argument, not a small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
