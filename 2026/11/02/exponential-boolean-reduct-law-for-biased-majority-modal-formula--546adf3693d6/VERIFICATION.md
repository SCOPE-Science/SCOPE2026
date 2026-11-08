---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Reconstructed the recursively defined Boolean reduct: comparison (#phi >= #psi) becomes constant determined by beta(b(phi)) versus beta(b(psi)), all Boolean operators commute with reduct. Structural induction ensures all-vertex equivalence for subformulas except exponentially small probability. For each v the n summands E_vu(1_A(col(u))-1_B(col(u))) are independent, bounded and of mean rho(delta); Hoeffding plus union over n gives exponential simultaneous sign concentration when delta!=0. Full Boolean bias forces identical truth tables at delta=0, hence every term vanishes identically and >= ties are correctly true even with shared colours. Explicit biases pi_i=1/(1+2^(2^i)) give atom weights distinct powers of two over 2^(2^k)-1, realizing each Boolean-probability j/D exactly once. Independently checked unique subset sums for k<=4, including endpoints; this does not replace asymptotic proof. The asserted exponential law and attainable-limit spectrum follow for every fixed formula.

## originality

PASS

The closest 2026 Ghosh–Schwarzentruber article develops graph counting in this modal language and discusses full-bias zero-one conditions, but accessible material does not supply an all-vertex exponential propositional reduct or this exact rational spectrum. GNN zero-one laws cover related but different architectures. The theorem expressly avoids claiming zero-one for unrestricted formulas with free root colours. Lack of full original paper access makes the precise conjecture/appendix comparison a significant originality risk, not itself a scientific disproof.

## value

PASS

A sharp asymptotic normal-form theorem for arbitrary fixed modal nesting (rather than selected one-layer examples) identifies the correct boundary between a zero-one comparison fragment and formulas retaining root-colour probabilities. The explicit rational full-bias construction computes every attainable limit. These are useful exact model-theoretic and probabilistic descriptions; exponential all-vertex control is stronger than a mere limiting probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
