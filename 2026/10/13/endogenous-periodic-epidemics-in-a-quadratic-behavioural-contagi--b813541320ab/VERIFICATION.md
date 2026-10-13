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

# Verification of an endemic periodic orbit in a quadratic behavioural SIS system

The full source model is the transmission-modulated case \(q_s=0\) of Plank et al., arXiv:2604.10995v1, equations (1)–(8), with the invariant initial relation \(S_B(0)=S(0)B(0)\). In the reduced coordinates \(I=1-S\) and behaviour prevalence \(B\), use the exact parameter tuple \((\mathcal R_0,q_c,\tau,\chi,\alpha)=(640/437,1,39/10,1,2)\).

**Reproduce the algebra.** Run `python3 verify.py`. The program depends only on the Python standard library and prints `VERIFY_OK` after checking the two exact equilibrium identities, the unique-root derivative lower bound, the full Jacobian and its spectral-sign invariants, disease-free hyperbolicity, the feasible-square vector-field faces, and the persistence barrier inequalities. It performs only exact rational computations.

**Verify the infinite-time implication.** The proof in `RESULT.md` shows \(I(t)e^{-30B(t)}\) cannot cross a positive lower barrier, yielding a compact forward invariant interior rectangle depending on each positive initial condition. The interior equilibrium has a repelling hyperbolic linearization and is unique. Poincaré–Bendixson therefore supplies nonconstant periodic \(\omega\)-limit sets for every non-equilibrium interior orbit. Neither the finite arithmetic checker nor any finite time-series simulation is used as a substitute for this dynamical theorem.

**Boundaries and nonclaims.** This statement is restricted to the deterministic factorized initial-condition submodel; no assertion is made for arbitrary nonfactorized four-compartment histories, finite stochastic populations, exact limit-cycle counts, or numerical period values. The small left-neighbourhood extension in \(q_c\) is qualitative and does not assert a certified numeric perturbation radius. Literature novelty is a reasoned comparison rather than an automated proof of priority.
