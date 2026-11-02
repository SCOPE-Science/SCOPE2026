---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

An Abelian Cayley shift diagonalizes in the Fourier basis, preserving the two selected mode labels and evolving the corresponding coin vectors by D_f V_t and D_g V_t with the same independent Haar V_t. Their overlap undergoes conjugation by A=D_g^*D_f. For any fixed unit vectors x,y and unitary A of mean trace lambda, Haar invariance yields E<y,V†AV x>=lambda<y,x> and E|<y,V†AV x>|²=d(1-|lambda|²)/(d²-1)+[(d²|lambda|²-1)/(d²-1)]|<y,x>|², using orthogonality of the scalar representation and the traceless adjoint projector of dimension d²-1. Iterating gives the exact stated first and second moments, including gamma<0, t=0 and |lambda|=1. The reduced two-by-two vertex density matrix has off-diagonal coherence Z_t/2, yielding per-realization purity (1+|Z_t|²)/2. Averaging density first gives a different nonlinear expression. Independent rational recurrence checks for dimensions 2–5, 10 steps and trace-zero d=2 verify algebra only; the analytic Haar projector computation proves generality.

## originality

PASS

Quillen’s October 7 2026 primary paper introduces this globally resampled Haar-coin quantum-walk family, characterizes the averaged channel and its Abelian Fourier dephasing, and explicitly notes that nonlinear variance requires second moments not obtained by the averaged channel (its Eq. 95 and discussion). The all-step conditional pair overlap/purity and nonzero trajectory-versus-average gap are not in the materially read complete primary paper. Generic Haar 2-design identities and random-coin entanglement work are acknowledged ingredients, and a general matrix-element fidelity theorem might implicitly cover the algebra. Best-of-knowledge original as a model-specific exact observable.

## value

PASS

An averaged quantum channel cannot characterize a typical trajectory’s nonlinear entanglement/purity; the exact t-dependent two-mode formula and 1/(2d) residual quantify that physical distinction with no vertex-count dependence. It is a natural new observable for the same random-walk model, and the negative-gamma transient is a meaningful boundary, although the calculation uses standard Haar moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
