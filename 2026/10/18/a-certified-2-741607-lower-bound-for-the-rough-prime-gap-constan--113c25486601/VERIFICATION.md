---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For each even h>=4 the admissible endpoint residues modulo the primorial are enumerated by Chinese remainder theorem. An exact survivor-mask dynamic program over odd primes p<h exhausts every admissible residue tuple, deleting even inner offsets as residue classes strike them. An independently implemented complete finite CRT program reproduced ALL 31 Omega_h counts for h=4,6,...,64 (including all 14 new h>=38 values); a structurally distinct inclusion-exclusion sum independently reproduced 15 entries through h=32. The exact partial sum through 64 is 61370211356863231369/29555095284933631875. A separate integer sieve and sequential floor product over 78497 odd primes <=10^6 reproduced L=1320323721179642234 on 1e18 scale; product tail >=999998/999999; their exact rational product equals 1841554176617798769290824758236675208498257/671706039314507885031093750000000000000000 >2741607/1000000. Nonnegative uncomputed h terms justify unconditional strict lower bound on defined constant, not prime-gap asymptotics.

## originality

PASS

Best-of-knowledge noncoverage of the specific new claim: This extends a natural published exact local sieve table by fourteen difficult prime-gap lengths and turns an approximate previously sampled value near 2. Prior overlapping premises and historical-priority caveats are explicitly credited and scoped.

## value

PASS

This extends a natural published exact local sieve table by fourteen difficult prime-gap lengths and turns an approximate previously sampled value near 2.7416 into a rigorous six-decimal lower threshold for a named singular-series constant. Exact arithmetic beyond the former h=36 cutoff is a mathematically motivated finite extension of the constant, not arbitrary numerology; it does not purport to determine the infinite sum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
