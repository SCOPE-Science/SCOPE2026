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

Input-first Choi vectorization gives C_Xi=(J_A^T tensor J_B) C_Phi: expand J_A E_ij=sum_k (J_A)_ki E_kj and left multiply the output by J_B. Gamma=J_A^T tensor J_B is a Hermitian involution even for a non-real symmetry. If C and Gamma C are both PSD, Hermiticity implies Gamma C=C Gamma, and on the negative eigenspace C and -C are PSD, forcing the block to vanish. Thus C has positive support, Xi=Phi, and the range vectors in every Kraus decomposition satisfy J_B K=K J_A; conversely these vectors give a positive Choi matrix unchanged by the twist. No TP is used here. The TP normalization then gives Phi^*(P_B^±)=P_A^±. At J=Z for qubits, diagonal Kraus coefficient columns have unit norm, so their scalar inner product c has |c|<=1; the displayed pair realizes every c, including the unit circle and zero. For Pauli noise let t=q_X+q_Y. On input |0><0| the target moves mass t to |1><1| and every compatible channel fixes the input, yielding trace norm 2t without ancillas. The proposed I/Z mixture is compatible and the difference is q_X(Ad_X-id)+q_Y(Ad_Y-Ad_Z), whose diamond norm is at most 2t by the unit channel norm. The endpoints t=0 and t=1 cause no exception; depolarizing has t=p/2, hence unhalved distance p. The independent rational grid verifies the Pauli probability mass reassignment and matching l1 upper bound in 3,185 instances; the Choi and norm arguments, not the grid or the frozen checker, prove the continuum statement.

## originality

PASS

The twist and Choi criteria are established. Heo explicitly gives strong intertwining as a sufficient premise (in the same-symmetry case); his inspected criteria concern the two positivities individually, not the necessity of strong intertwining in their intersection. The ordinary qubit disk itself is prior as the d=2 genuinely incoherent/Schur channel class, and the diamond metric for two Pauli channels is prior. The supported distinct content is identifying the simultaneous positivity cone via matching symmetry sectors, identifying that known disk specifically as the qubit intersection, and giving the attained separation from the full compatible class. This is not a priority claim for the disk, the metric, or the elementary Pauli probability calculation.

## value

PASS

It is a natural physical realizability question whether maps constructed using an indefinite positivity notion are also ordinary CP. A structural answer for arbitrary finite input and output sectors, without assuming equal signs or a trace normalization to prove necessity, shows exactly which population transfers physical compatible maps forbid. The Pauli formula translates that obstruction into a sharp operational separation even allowing all coherent phases in the free comparator. The value lies in that intersection and its quantitative interpretation, not in renaming the familiar Schur-channel disk or proposing a new diamond-norm method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
