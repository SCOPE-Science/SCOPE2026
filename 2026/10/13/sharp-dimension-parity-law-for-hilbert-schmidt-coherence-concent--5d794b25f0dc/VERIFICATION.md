---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a qubit, the maximum expectation of an equatorial Pauli observable is twice the modulus of its off-diagonal entry, whereas its Hilbert–Schmidt coherence is √2 times that modulus. The adjoint of a trace-preserving positive map preserves the order interval [−I,I], and diagonal-state preservation makes the adjoint image H of each such observable zero on the diagonal. For the trace-zero Hermitian contraction H, let r be the sum of its positive eigenvalues, also the sum of the absolute negative eigenvalues. If their counts are p and q, then Tr(H²)≤2r≤2min(p,q)≤2 floor(d/2). Pairing with the input off-diagonal part by Hilbert–Schmidt Cauchy–Schwarz proves the claimed factor. For equality put m=floor(d/2) and use the pair-folding Kraus matrices and the singleton on odd dimensions. Their initial supports partition all basis vectors, giving trace preservation, and the row and column sparsity gives strict incoherence. The input I/d+εZ has unit trace and minimum eigenvalue 1/d−ε>0; its paired entries give coherences ε√(2m) at input and √2 mε at output. This gives exact equality for all d≥2, including d=2,3; input with zero coherence maps to zero coherence by hypothesis.

## originality

PASS

The prior ancilla example already gives the amplification mechanism, including the even-dimensional lower bound and, with an unused basis state, the odd-dimensional lower mechanism. Neither that example nor the closest compared catalog records establishes the universal parity-sensitive upper bound for all diagonal-preserving d-to-qubit channels. Credit attaches to that exact class-wide bound and matching classification, not to nonmonotonicity, the even-dimensional witness in isolation, or the elementary trace-zero spectral inequality.

## value

PASS

Knowing that Hilbert–Schmidt coherence is not generally monotone does not quantify the maximum attainable increase. The universal sharp bound for a natural fixed qubit output gives a complete dimension classification, including exact contractivity in dimension three and an odd-dimensional improvement over the unrefined √(d/2) estimate. Full-rank SIO saturation shows that neither boundary inputs nor larger operation classes are needed to attain it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
