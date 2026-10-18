---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

A near-perfect integer has σ(n)=2n+d for a proper positive divisor d. Partitioning Ω(n)≤4 into exponent shapes (single prime powers; 2+1; 1+1+1; 3+1; 2+2; 2+1+1; 1+1+1+1), the proof excludes deficiency and forces finite prime ranges using positivity and d|n. The delicate squarefree 2pqr shape has v₂(σ(n)−2n)=2 while v₂(n)=1; the 4rs and 2r²s branches are discharged by exact divisibility and finite inequalities, not a scan cutoff. Independently computed divisor sums and Ω over every n≤250000 and recovered precisely n=12,18,20,24,40,56,88,104,196,234,650 and the eleven stated d values. The analytic branch proof, not the scan, establishes infinity-bound exhaustion; no Ω>4 classification.

## originality

PASS

Ren–Chen 2013 explicitly lists 234 and 650 among examples with three distinct primes and proves a complete two-DISTINCT-prime classification for arbitrary exponents. Their theorem neither classifies the mixed ω=3, Ω≤4 slice nor organizes all Ω≤4 even shapes; the eleven cases are thus not new examples, but the total-multiplicity exhaustion appears to be a new classification on the inspected record. Hasanalizade gives context about remaining even cases. Earlier bounded list or unindexed Ω threshold theorem is a risk.

## value

PASS

Total prime-factor multiplicity Ω is a natural arithmetic complexity scale distinct from number of prime supports ω. The proved complete Ω≤4 classification crosses both two-support and three-support families and isolates the first rare three-support cases, useful as a sharp baseline for broader near-perfect classification. This is not just known-term reenumeration because symbolic arguments bound all integers at this multiplicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
