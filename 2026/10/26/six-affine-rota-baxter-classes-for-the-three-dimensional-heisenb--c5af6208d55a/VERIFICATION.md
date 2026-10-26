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

The mathematical proof directly derives the affine Rota–Baxter identity, enumerates every ordered Heisenberg subalgebra decomposition, and classifies translation parameters under every canonical affine automorphism. No result relies on extrapolating a finite computation.

Execute \(\texttt{python verify.py}\) with standard Python 3. The checker requires no downloads or packages. For \(\mathbb F_3\), it explicitly constructs all \(244\) operators, verifies the defining identity at all \(27^2=729\) ordered input pairs for each operator, enumerates all \(1296\) permitted affine automorphisms, and confirms orbit sizes \(1,3,24,36,72,108\). For \(\mathbb F_5\), it constructs all \(1626\) operators, checks the formula by rank, and tests \(25\) input pairs per operator. The larger field is not exhaustively tested for all inputs or all conjugacies.

The code assumes the field order passed is prime. The mathematical result covers every odd prime power using projective line/plane counting over finite fields, not merely the two checked prime fields. Self-review has been completed; independent audit has not been performed.
