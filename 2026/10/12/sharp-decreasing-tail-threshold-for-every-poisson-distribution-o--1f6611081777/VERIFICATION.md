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

For all finite k≥2, using p_n=e^{kλ}Pr(X=n), the exact block formula p_{k+2+t}−p_{k+1+t}=λ²(S_{k+t}−T_t) for 0≤t≤k−2 follows from Q(z)=exp(λz/(1−z)) and P=Q exp(−λ z^{k+1}/(1−z)). Vandermonde expansion and (i+j+2)!≥(i+1)!(j+2)! prove S_{k+t}≤S_k T_t. For k≥3 the first edge has λ*<1; k=2 separately follows from λ*=2(√7−2) and λ*S_1(λ*)<1. The positive-coefficient recurrence n p_n=λΣj p_{n−j} extends a k+1-long initial decreasing block to every n≥k. At the threshold p_{k+2}=p_{k+1}, above it reversal, proving necessity. Independently reproduced 44 exact Fraction initial coefficient identities for k=2..9; this is supporting finite evidence, not the infinite proof.

## originality

PASS

The inspected source explicitly conjectures the precise all-order strict tail boundary, and the earlier related Mane article proves only a smaller sufficient λ regime. The submitted convolution lemma and induction bridge the open implication; no matching prior proof was established in accessible material. The primary full text was not completely retrieved, retaining possible later/prior coverage risk.

## value

PASS

Solving an explicitly stated sharp threshold conjecture uniformly in the order k identifies the exact first tail crossover and is not a routine numerical table or a slight parameter change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
