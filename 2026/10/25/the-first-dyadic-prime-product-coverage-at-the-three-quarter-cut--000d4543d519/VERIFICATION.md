---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The finite theorem reduces to exact enumeration of all unordered pairs of odd primes p<=floor(2^(3m/4)); the exact cutoff is computed as isqrt(isqrt(2^(3m))). A complete Eratosthenes sieve and pair-product bitset indexed by all 2^(m-1) odd unit classes proves both coverage and noncoverage for EVERY integer m in [1,21], not a sample. Independent implementation reconstructed all 21 missing-count values (1,2,3,3,5,11,17,30,54,70,121,162,190,240,216,183,92,42,7,3,0), verifying the first complete case m=21 and that m=20 has precisely three unrepresented residues 122299,333455,414971. At m=21, full coverage first occurs at prime cutoff 50923, with prior prime 50909 and last obstruction 745135, represented by 50923*7757 modulo 2^21. Independent modular-inverse obstruction reconfirmed that no earlier prime cutoff represents this last residue. This proves only the finite interval and no perpetuation for m>21.

## originality

PASS

The two cited October/September 2026 prime-product studies concern almost-all classes at large prime-power modulus with larger prime cutoff, and a Granville random-prime model at exponents strictly greater than 3/4; these do not logically entail complete actual-prime coverage at q^(3/4) for q=2^21 nor the exact least cutoff 50923. Search located no matching finite table, but unindexed prime residue computation tables remain a priority risk. A directly relevant 2026 paper could not be downloaded and read in full, so its noncoverage is not asserted on abstract alone.

## value

PASS

The exponent 3/4 is a mathematically motivated critical boundary of prime-product covering in a recent random model, not a hand-picked computational ratio. The first sharp dyadic full coverage at that endpoint and adjacent three-hole failure provide an exact and reproducible benchmark for an important open covering problem. A meaningful finite sharp cutoff does not require proving an infinite theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
