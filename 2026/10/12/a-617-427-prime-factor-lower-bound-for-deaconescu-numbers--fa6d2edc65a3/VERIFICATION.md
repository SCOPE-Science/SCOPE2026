---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Reconstructed squarefree odd reduction from MS2(n)=phi(n)-1; M odd>=3, mod-3 trichotomy and M congruences, and mod-5 incompatibility for the only M=3/5 branches. Since (p-1)/(p-2) decreases, the seven fixed-count prime-stream products dominate all smaller supports. Independent Eratosthenes sieve through 30,000,000 reproduced seven exact terminal primes; log-sum gaps include -1.68808882428e-8 at p=26375263 and +2.10334192285e-8 at p=26375269. Inspect source integer outward-rounding code with K=12 and log threshold bounding: float replay alone is not an exact certificate, so the symbolic reduction and the inspected integer-interval method remain necessary. Conclusion omega(n)>=617427; no existence asserted.

## originality

PASS

PASS (best of knowledge): Old theorem omega>=2859 never implies omega>=617427; the omitted mod-5 structural condition is indispensable to the claimed strict increase. Neither inspected result dominates the stricter modulo-5-constrained extremal products; the 2026 bound 2859 is quantitatively much weaker, even though it uses the same general ratio. Residual literature/access risks are explicitly recorded.

## value

PASS

PASS: This significant support obstruction for a classical unresolved Schemmel-totient divisibility problem strengthens the closest located general theorem omega>=2859 by >200-fold. The additional mod-5 restriction is structurally motivated by forced small odd multiplier and cutoff is the actual transition of the final restricted prime stream, not an arbitrary parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
