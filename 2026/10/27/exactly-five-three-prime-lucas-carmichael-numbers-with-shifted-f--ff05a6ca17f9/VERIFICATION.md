---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 artifacts/verify_g4.py` from this extracted package. The program performs exact trial-division primality and exact positive-divisor enumeration by two methods: (1) divisor candidates for \(q+1\mid(p+1)(p+h)\), and (2) independent direct candidates for \(r+1\mid pq-1\), over the analytically complete range. The two enumerations agree for each of six permissible smallest primes. The verified count of triples with shifted gcd exactly four is five; the table of unrestricted counts is \((1,3,9,9,10,5)\). All five proposed triples were tested directly.

This is a rigorously finite arithmetic certificate once the human proof bounds the least prime and the other two primes. It does not prove general statements about strata of higher gcd from enumeration alone. Exact arithmetic is used throughout, without probabilistic primality assumptions. Independent review is not performed.
