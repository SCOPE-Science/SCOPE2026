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

For connected simple noncomplete strongly regular graphs, the Laplacian spectrum {0,alpha=k-r,beta=k-s} has alpha+beta=S=2k-lambda+mu and alpha beta=P=mu v. Exact rational functional calculus with g(z)=12z/(z²+6z+12) and the two nonconstant projectors gives adjacent off-diagonal 12h(12+6mu h-mu(v-S)h²)/D and nonedge 12mu h²(6+S h)/D, where D=d(alpha h)d(beta h)>0. Adjacent entries have exactly one positive zero H=(3+sqrt(9+12(v-S)/mu))/(v-S) when v-S>0; for v-S<=0 they remain positive. Nonedge entries stay positive. The scalar Padé stability R(z)=((z-3)²+3)/(z²+6z+12) is in (0,1] for z>=0, so the matrix is SPD, row stochastic algebraically, and norm 1 for all h. Three independent exact rational C5 inverse matrix checks matched the offdiagonal formulas, but the spectral calculation establishes the universal theorem.

## originality

PASS

Previous SSP/absolute monotonicity literature and negative Padé examples do not give the same necessary-and-sufficient end-step formula for all strongly regular graphs. Prior Resultary directed eight-state Padé and reversible Crank–Nicolson records involve different generators or rational maps. Best-of-knowledge subject to specialized spectral-association scheme treatments.

## value

PASS

Exact all-parameter sharp positive-time horizon for a natural infinite family of reversible graph diffusions under a fourth-order implicit integrator. Separates positivity from spectral stability and exhibits permanent edge-sign loss; covers primitive as well as imprimitive strongly regular graphs. The parameter formula is potentially useful for deciding admissible steps from graph invariants alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
