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

Factoring the common character reduces every two-frequency idempotent to \(1+e_N(dx)\). With \(g=\gcd(d,N)\) and \(L=N/g\), the denominator is exactly \(2gS_L\), while the target numerator is controlled by a unit residue modulo \(L\). Reducing units from \(L\) to \(L/\gcd(a,L)\) shows the maximum absolute cosine occurs at the residue classes \(\pm1\), giving the divisor-and-gcd formula. The finite cosine sums evaluate to the stated cosecant/cotangent forms. A fresh brute-force check over every target for \(2\le N<15\) agreed with the closed formula.

## originality

PASS

Bonami--Révész formulate the finite cyclic \(L^1\) idempotent concentration problem for arbitrary frequency sets and analyze the unrestricted prime-modulus behavior, but searchable full text contains no two-frequency specialization. Targeted searches under two-frequency, two-term and sum-of-two-characters language found no divisor-and-gcd formula. The assigned result is therefore a bounded exact slice of the broader open concentration problem rather than a restatement of an inspected theorem.

## value

PASS

Spectral cardinality two is the smallest nontrivial idempotent slice of a documented \(L^1\) concentration problem. An exact classification for every cyclic modulus and target, including the composite divisor dependence and sharp prime asymptotic, supplies a natural benchmark that future work on larger spectra can compare against.

The dated certificate retains the supplied scientific assessment, sources and limitations.
