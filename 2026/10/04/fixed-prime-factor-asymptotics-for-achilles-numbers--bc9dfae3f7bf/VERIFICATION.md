---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The corrected final proof was reconstructed at exponent level. Achilles means every exponent >=2 and exponent gcd 1, so at least one exponent is odd. The principal layer has a unique form p^(2j+1)m^2 with j>=1, p not dividing squarefree m, omega(m)=r-1; it is automatically Achilles. Fixed-order Landau counting for m gives the main term, and on the polylogarithmic truncation log Y=(1/2+o(1))log X, producing the factor 2. The absolutely convergent weight sum is sum_p p^(-3/2)/(1-p^-1). Uniform exclusion of the distinguished prime is lower order. Every nonprincipal pattern has at least two exceptional exponents; summing their p^(-e/2) weights leaves one fewer Landau loglog degree for r>=3, while r=2 is O(X^(1/3+o(1))). Thus the remainder is lower order. The finite verifier's 10^8 enumeration is corroborative only. The ready repair restores TeX control-sequence bytes in RESULT.md without changing the mathematics.

## originality

PASS

PASS. OEIS A052486 gives the Achilles object and aggregate enumeration, while A393816 tabulates the exact two-distinct-prime stratum; neither supplies the fixed-r counting asymptotic or prime-series constant. Das--Kuo--Liu's full arXiv HTML was inspected around Theorem 1.2 and its proof: it establishes first/second moments of omega over all h-full integers and normal order, not fixed-r counts after deleting perfect powers; in-document searches found no 'Achilles' or 'perfect power'. Resultary returned the audited record as the direct match and no independent covering fixed-r theorem among the checked hits.

## value

PASS

The theorem identifies the first non-perfect-power layer inside a classical thin multiplicative set and resolves every fixed number of distinct prime factors with one explicit universal prime-series constant. It explains how removing the dominant square layer changes the fixed-r scale and is a natural asymptotic classification, not a recomputation of a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
