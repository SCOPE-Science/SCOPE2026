---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The free/fixed positive-definite tridiagonal stiffness has normalized cosine eigenvectors u_jk=sqrt(4/M) cos(pi(2j+1)(2k+1)/(2M)), M=2N+1. Solving stationary scalar damped-oscillator kinetic variance yields Q_kj=u_jk² (the known forward formula). Finite cosine sums imply C1=1/2 1, C²=M/4 I-1/2 J, hence Q²=(I+2J)/M. Thus Q has eigenvalue one in span{1} and eigenvalues of absolute size 1/sqrt M on mean-zero subspace, giving the inverse and exact Euclidean condition number; nonnegative baths are inverse-inequalities. For each row k, modular multiplication by odd m=2k+1 on odd residues mod 2M yields closest residues ±g to zero, giving g maximizing sites; congruence mr=M has (g-1)/2 bath sites when g>1 (perfectly dark), while g=1 gives unique nearest M±2 minimizing site. Linear heat allocation gives extrema and sharp positivity limits. Independent NumPy reconstruction verified Q², inverse geometry and all gcd maxima/minima and multiplicities for every N=2..79, but no claim that finite tests prove all N; original Lyapunov testing inspected as supplied, not independently rerun.

## originality

PASS

PASS best-of-knowledge with close-prior qualification: Falasco et al 2015 derive exactly the forward mixed-boundary squared-eigenvector relation Q and discuss heat repartition, so the dynamical linear response is NOT new. The complete explicit inverse, sharp condition number/feasibility cone, gcd-selected dark baths and exact budget extrema are a motivated additional arithmetic tomography classification not explicitly stated in inspected original.

## value

PASS

Full recovery of local thermal reservoir temperatures from the measurable modal energies, exact attainable-cone conditions, a sharp noise amplification factor and heat allocation extrema/dark-site multiplicities are natural system identification and control invariants. These useful uniform formulas go substantially beyond merely reprinting the existing forward transfer, while crediting the finite-transform algebra as standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
