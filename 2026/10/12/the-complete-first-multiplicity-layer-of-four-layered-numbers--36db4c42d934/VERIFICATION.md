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
# Reproduction and verification

Place `verify.py` and `partitions.json` in one directory. Run `python3 verify.py` with Python 3. Standard-library integer and rational arithmetic suffices; no optimization package or external service is required.

The search independently tests \(1\le\Omega(n)\le8\) using the Euler-factor envelope, which gives a provable upper bound on **every** as-yet-unchosen prime. The immediate next-prime bound is monotonic and tends to the proper prefix's abundancy, strictly below four by the established lower multiplicity layers, so all search loops terminate. Its output is five exact four-abundant integers, none with smaller multiplicity.

For each of the five, `partitions.json` specifies four integer lists. The checker recomputes prime factorization, exact divisors, the full divisor sum, and tests disjointness, total coverage and equal sums. `verification_output.txt` records the executed checker output. A separate sieve over \(n\le300000\) corroborated the list but is **not** used as an infinite proof. The outer theoretical assumptions, particularly \(\Omega(n)\le8\), are indispensable. This does not constitute an independent external audit.
