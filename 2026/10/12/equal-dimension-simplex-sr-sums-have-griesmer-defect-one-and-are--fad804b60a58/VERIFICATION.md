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

The weight distribution follows from Kwiatkowski Proposition 4.2 with m=1,l=0; the two nonzero weights (q-1)q^(k-1)(q^k-1) and (q-1)q^(k-1)(q^k-2) have frequencies 2(q^k-1) and (q^k-1)^2, giving full q^(2k) words and rank 2k. The first k Griesmer terms sum to q^(2k)-3q^k+2 and the remaining k ceilings to q^k-2 by the exact floor at j=0; G=N-1. The integer-ceiling increment for d+1 is 1 at every q^i dividing d, giving k increments for q>2 and k+1 for q=2. Independently verified 70 prime-power (q,k) arithmetic pairs and constructed the exact full weight distributions for (q,k)=(2,2),(3,2) from the generator columns. Checks are corroborative, proof all parameters algebraic. Griesmer applies only to q-ary linear codes.

## originality

PASS

Best-of-knowledge original exact near-Griesmer distance boundary. Kwiatkowski Prop 4.2 fully supplies the weights and Thm 4.4 proves equality for unequal dimensions; the paragraph following Thm 4.4 explicitly says equality fails for equal dimensions but does not give the exactly-one defect nor compute the optimal attainable next distance. A result phrased as one-defect Griesmer optimality in older coding sources remains a bounded priority risk.

## value

PASS

Equal-dimension coupling is the canonical omitted parameter boundary of the published construction. Determining its exact defect AND excluding larger distance for all q and k resolves the natural parameterwise optimal-distance question, useful for selecting and benchmarking two-weight linear codes. It is more than a finite table or a trivial parameter renaming, though not a new universal coding bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
