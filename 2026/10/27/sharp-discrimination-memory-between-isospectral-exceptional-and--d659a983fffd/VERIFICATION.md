---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The Kraus weights give rotated dephasing and the nonnegative Pauli probabilities give D=diag(λ,λ²,λ) in Bloch coordinates. Direct substitution gives M−D=buvᵀ with b=(1−λ²)/(1+λ²), u=(1,0,λ), v=(−λ,0,1). Because vᵀu=0 and both vectors lie in the λ-plane of D, this creates exactly a size-two Jordan block and M^n−D^n=nλ^(n−1)buvᵀ. For arbitrary joint input Y, the difference factors through Tr_qubit[((v·σ)⊗I)Y], whose trace norm is at most √(1+λ²) times ||Y||₁ by duality. The remaining tensor factor u·σ has trace norm 2√(1+λ²), and the Bloch-to-Pauli factor is 1/2. A pure eigenstate of v·σ saturates the bound, and measuring the sign of u·σ gives the Helstrom probability 1/2+d_n/4. Consecutive ratios λ(n+1)/n give the ceiling optimizer and its integer tie; n(1−λ)→s gives 2s e^(−s), with optimized limit 2/e. This holds for a single uninterleaved power comparison with a passive ancilla, not adaptive uses. VERIFICATION.md and verify.py were inspected, not executed; the checker has five rational parameters and fifteen powers, not an ancillary proof. The line 53–54 comment misstates the 4/5 tie as 5,6; line 55 correctly tests 4,5, consistent with the finding.

## originality

PASS

Brandão already gives the exact exceptional channel, Jordan block and general product-preparation/projective-measurement signal; the polynomial–exponential transient itself is not a new contribution. The inspected material does not set up the comparison with a physical isospectral Pauli channel or determine its ancilla-uniform discrimination distance and optimized weak-noise crossover. No covering paired-channel statement was established in the inspected sources.

## value

PASS

Matching physical channels by spectrum isolates the operational effect of the Jordan block instead of conflating it with different spectral decay rates. The exact metric gives the attainable single-test success probability, shows an ancillary resource is unnecessary, and quantifies the long-time separation that remains as both one-step channels approach the identity. This is a motivated operational invariant for a specified comparison, not a claim about adaptive queries or optimality among all isospectral comparators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
