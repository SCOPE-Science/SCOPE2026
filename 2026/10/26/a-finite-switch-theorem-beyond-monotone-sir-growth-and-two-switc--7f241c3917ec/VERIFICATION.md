---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For a finite-time optimal first transversal hit I(T)=epsilon, Pontryagin normality follows because an abnormal extremal would give lambda_S(T)=0 and lambda_I(T)=0 from free-time Hamiltonian and nonzero terminal I-dot, contradicting nontriviality. After normalizing the running-cost multiplier to one, lambda_I(T)>0. At every zero lambda_I=0, the zero Hamiltonian forces lambda_S>0 and the adjoint gives lambda_I-dot=lambda_S S(beta+I beta_I)>0; hence lambda_I has at most one zero. With switching function psi=-S lambda_S, the positive integrating factor converts its derivative to Theta-dot=mu lambda_I S I G, and Theta(T)=0. If G(S(t),I(t)) has at most q distinct zeros on (0,T), Rolle including T gives at most q+1 interior switch zeros, and excludes singular arcs. G(T)>0 yields terminal full vaccination. For models B beta=48 exp(3I-1.5S), gamma=5+2I, and C beta=32(1+2I)(1-0.67S), gamma=5+2I, strictly decreasing S must cross the unique G=0 threshold (2/3 or 50/67) before first exit because beta(S,epsilon)S>gamma on the earlier S range. A terminal tangency would contradict the sign of I-dot just before the first hit, proving transverse exit. Therefore any unrestricted optimum has only patterns 1, 0-to-1, or 1-to-0-to-1 up to null sets. Independently verified derivative identities and endpoint inequalities (32e^-1.5>5+2e-8 and 132/25>5+2e-8). This does not find the optimal switching times.

## originality

PASS

Park–Jang–Kim 2026 is the exactly matching SIR optimal-control model. In its inspected complete primary text the one-switch theorem assumes G>0 on the whole simplex; Section 6.5 numerically explores two switches in two cases violating that hypothesis and explicitly does not provide unrestricted structure. The new result is the finite-zero budget after an at-most-one infected-costate zero plus verified endpoint transversality, making the benchmark two-switch family structurally exhaustive. Earlier Bolzoni and Hynd constant-rate models and Grigorieva fixed-terminal-cost studies are different control questions. A general switching-zero bound in older optimal-control literature may be adaptable; it remains a priority risk.

## value

PASS

For a constrained time-optimal epidemic-control problem, reducing an infinite-dimensional measurable-control class to a finite family of switch patterns is a meaningful structural advance. The theorem handles sign-changing transmission sensitivity and proves completeness of the two-switch search space for naturally published nonmonotone examples, without falsely claiming numerical optimality or clinical effectiveness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
