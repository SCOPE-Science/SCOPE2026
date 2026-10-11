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
# Verification

The final claim was checked by a direct proof replay.

1. For \(H=\operatorname{lat}(C(I)\otimes C(I))\), each \(h\in H\) is a finite difference of finite lattice suprema, so at each point it equals one of finitely many algebraic-tensor branches.
2. The coincidence sets with those branches are closed and cover \(I^2\). Baire category gives a nonempty open rectangle in \((0,1)^2\) on which \(h\) equals one algebraic tensor, hence has finite-dimensional section span.
3. A basis \(h(\cdot,t_j)\) of that local section span admits evaluation points \(s_i\) for which \((h(s_i,t_j))\) is invertible; otherwise the basis functions would be linearly dependent.
4. Solving this fixed linear system with right-hand side \((h(s_i,t))\) gives coefficient functions that are real-analytic for \(0<t<1\) and continuous on \(I\).
5. The difference between \(h\) and the resulting separated sum is real-analytic on \((0,1)^2\) and vanishes on the Baire rectangle. The real-analytic identity theorem makes it vanish on the full connected interior. Continuity extends the formula to the closed square.
6. If the local section span has dimension zero, the same identity theorem gives \(h=0\) globally.

The focal arXiv source was inspected in full for the tensor realization and the finite-branch/Baire step. No numerical experiment, finite enumeration, or external certificate enters the proof. The literature comparison has an explicit residual risk from older decomposition/approximation papers for which only public abstract or bibliographic material was inspected; this does not affect correctness of the mathematical statement.
