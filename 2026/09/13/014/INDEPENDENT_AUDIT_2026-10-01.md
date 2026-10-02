# Independent audit — 2026-10-01

## Final claim

For the Hou-Zong benchmark, the displayed P_i,Q_i,R_i matrices certify the same Proposition-1 LMI class at mu'=(3.0,1.6,0.64), yielding the componentwise improved MDADT triple (0.54930614,0.18077063,0.22314355).

## Disposition

**passed**

## Correctness — PASS

The benchmark matrices/rates and Hou-Zong Proposition-1 LMI were reconstructed. Re-evaluation of the displayed 10-decimal P_i,Q_i,R_i matrices gives positive definite blocks and LMI maximum eigenvalues approximately -4.8118735e-4, -9.7227899e-5, and -9.5721048e-5; the tightest coupling margin is about -2.7141e-5. The dwell times computed from mu'=(3.0,1.6,0.64) and alpha=(2,2.6,-2) are (0.54930614,0.18077063,0.22314355), strictly improving the paper's reported benchmark values. The actual binary certificate exists at artifacts/cert_matrices.npz.

## Originality — PASS

The primary benchmark provides the original feasible parameters and theorem but not the improved mu' triple. Resultary returned only the record under audit as an exact match. The new result is the feasible certificate itself, which is not a symbolic corollary of the theorem without solving the coupled feasibility problem.

### Equivalent formulations

The claim is equivalently a strict-feasibility witness for three per-mode LMIs plus 18 matrix-order constraints at a smaller dwell-time triple; no equivalent prior certificate was found.

### Broader coverage

The general theorem tells how a feasible certificate implies stability but does not imply feasibility at the proposed smaller mu values.

### Exact database or table

The exact improvement is not a known table recomputation in the sources inspected.

### Claim versus prior implication

The certificate requires new feasibility evidence; it is not mechanically implied by the paper's reported point.

## Scientific value — PASS

A componentwise 11–18% tightening of a published benchmark within exactly the paper's LMI class and rates, accompanied by a reusable feasibility witness, is a motivated finite optimization result. It measures conservatism of a standard sufficient-condition benchmark rather than reporting an arbitrary parameter slice.

## Checked sources

- https://doi.org/10.1109/ACCESS.2018.2886381
- Resultary published-findings semantic search

## Residual risks and limitations

- Verification is floating-point rather than interval-rigorous, though the margins are many orders above ordinary eigensolver roundoff at this matrix scale.
- The search cannot exclude an unindexed later optimization of the same benchmark.
- It does not establish global optimality of the LMI class.

Computational matrix verification rather than interval-rigorous certification; the tightest margins are about 1e-4 for the LMIs and 2.7e-5 for coupling. The delay derivative bound 0.2 is tied to the benchmark delay d(t)=0.2 sin(t).
