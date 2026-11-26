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

For the powerful part beta of the independent valuation model its weight is zeta(2)^−1 beta^−1 ∏_{p|beta} p/(p+1): at p not dividing beta the event E_p≤1 has probability 1−p^−2, and at p|beta the fixed exponent contributes (1−1/p)p^−e. The odd part of tau(beta) equals V on this event, so the expectation equals Campbell's actual c3. The proxy divides V and can differ only for a middle prime with exponent ≥4 or an omitted prime with exponent ≥2. The integral bounds give a one-sided loss at most 1/(3·1000^3)+10^−8. The package's floor transitions preserve lower masses, and the upper sum must add the entire deficit and use ceiling reciprocal contributions; these inequalities are valid. Independently replayed with python3 /workspace/reproductions/divisor_enclosure.py (not the uploaded checker). For each small-prime state v=3^a w with 3∤w, integrate x^a ∏(1−u_p(1−x))/tau(w) over [0,1]. Pointwise Bonferroni orders 3 and 4 give lower and upper polynomials; the first three elementary symmetric coefficients come from bounded power sums, and e4≤(Σu_p)^4/24. A segmented sieve processed 5,761,287 middle primes, and 765 small-product states left less than 10^−15 probability unrepresented. Exact rational arithmetic with outward display gave [0.83670132148021748910, 0.83670133181355127258], strictly inside both announced endpoints. This verifies the valuation expectation enclosure, not the asymptotic theorem or a specific asymptotic error term.

## originality

PASS

The supported distinct claim is the narrow certified interval only. The asymptotic, powerful-part series, and identically weighted expectation are prior or equivalent. Campbell gives only broad bounds in the inspected passages; an earlier Resultary numerical partial sum has no comparable precision or infinite-tail certificate. This is a bounded best-of-knowledge assessment.

## value

PASS

This is the leading coefficient of a motivated reciprocal iterated-divisor asymptotic, not a parameter chosen after computation. The certificate shrinks the broad known interval of width about 0.392 to about 1.03×10^−8, which supplies a usable target for other analytic bounds and numerical evaluations. The divisor count couples equal odd prime factors across outcomes, so a product of scalar local means would not give this benchmark. Neither a new asymptotic nor a unique rounding to eight decimal places is needed for the stated interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
