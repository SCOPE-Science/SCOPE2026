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

Multiplying by two gives \(n(n+1)=2^Aq^\beta\). Coprimality of consecutive factors forces the unordered pair to be \({2^A,q^\beta}\), so \(q^\beta=2^A\pm1\). The plus/minus factorizations exclude every higher exponent except the even plus-branch case \(q=3,\beta=2,A=3\); exponent one gives exactly the Fermat/Mersenne branches. The frozen verifier was read and correctly checks the reduced equations and a bounded triangular scan; the global proof is the factorization argument.

## originality

PASS

The 2026 primary article was read in full open text. It states Tian's two-prime conjecture, proves only a sharp absolute upper bound of four for arbitrary two-prime supports, and says the conjectured general bound remains beyond its results. It does not state this all-odd-prime fixed-support \({2,q}\) classification. Resultary returned no distinct exact same-subfamily theorem.

## value

PASS

This is a natural complete subfamily of a current explicit conjecture: it reaches the conjectured two-solution bound for every support containing the unique even prime and identifies the sole equality support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
