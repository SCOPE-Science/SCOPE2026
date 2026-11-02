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

# Finite verification and mathematical limits

The standalone `verify.py` reconstructs divisors of \(2^a p^2\) directly from integer exponents and groups each divisor with its partner under \(d\mapsto n/d\). It independently computes \(\sigma(n)-2n\), tests all omissions with zero, one or two complement orbits, checks the singleton-orbit convention, and identifies the exceptional omitted set.

Execution: `python3 verify.py`.

Observed exact output:

```
VERIFY_OK independent_parameter_pairs=5010 square_root_checks=2505 sole_at_most_two_orbit_case=36 exact_integer_arithmetic=PASS finite_only=YES
```

The finite domain contains every exponent \(1\le a\le30\) and all odd primes \(3\le p\le997\). The output uses integer arithmetic for all claims (the sieve's loop bound is only for enumerating trial divisors within the stated finite range). The infinite theorem is proved in `RESULT.md` by exhaustion of orbit types and algebraic constraints; no inference from this finite grid to an unrestricted range is made. No external or independent audit has been performed.
