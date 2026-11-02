---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The exact payoff along a finite functional-graph walk is sum prefix q-products p_j(τ-|x_i-x_j|); its no-distance component is τ(1-Q_S), with distance penalty bounded by Δqmax. Any strategy adding a missing visited voter gives at least τ pmin Q/qmax, and replacing a maximal-abstention cycle C by another T with Q_T≤Q_C yields the same strict lower bound. Hamiltonian cycles lose visited voters under any nontrivial redirection, hence strict NE. Any other functional digraph has multiple cycles or an in-tree to its sole cycle, giving a profitable deviation. Robustness bound Δ<τ pmin Q/qmax² proves exact NE set, count (n-1)!. Three-person d=(2,1,2) equivalent zero-based (1,0,1) exact inequalities b≥max(2a,(1+a)/2) follow all deviations; two persons cannot be nonspanning NE under mutual acceptance. Independently enumerated all profiles n=2,3,4 for homogeneous and heterogeneous p and exact boundary grid.

## originality

PASS

The original probabilistic default-delegation model and component cycle theorems from Brill et al are explicitly prior; inspected full conference paper Theorems 5 and 8 provide local component constraints, not all-and-only spanning cycles under uniform small-diameter bound, exact heterogeneous turnout equilibrium count, or the exact specified 3-voter failure boundary. Other liquid-democracy temporal/iterated delegation models have distinct payoff semantics. Expanded 2026 preprint not fully read, so priority is qualified.

## value

PASS

A global pure-Nash equilibrium classification and factorial count under a quantitative, heterogeneous-turnout robustness regime is a natural structural game-theoretic theorem. The sharp inequality for a minimal 3-voter nonspanning counterexample exposes the boundary between strict closeness and mere mutual acceptability; these are meaningful distinctions for default-delegation equilibrium structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
