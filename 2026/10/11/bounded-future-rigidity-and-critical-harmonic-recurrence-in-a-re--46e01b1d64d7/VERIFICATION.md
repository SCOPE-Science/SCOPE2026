---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Direct independent SymPy differentiation of the explicit polynomial L=(z^2+(1-y)^2)/2+(x^2-1)(1-y) yields Ldot=2 x^2(1-y)^2-a z^2. For a<0, nonnegative Ldot=0 requires z=0 and x(1-y)=0; imposing invariance leaves exactly E0,Eplus,Eminus. For a=0, its largest invariant zero set is x=0 with harmonic y,z oscillator plus Eplus/Eminus. Forward boundedness ensures global continuation and a compact connected invariant omega-limit set on which L is constant; connectedness and zero-set dynamics leave either an equilibrium or the plane. Off the plane x(t) retains its sign. If its omega-limit lay in the plane, x(t)->0; integrating zdot=x^2-y and bounded z gives Cesaro mean y->0, contradicting (log|x(T)|-log|x(0)|)/T->1 and boundedness. Invariant compactly supported probabilities integrate nonnegative Ldot to zero and disintegrate into uniform angular measures on periodic harmonic orbits. All claims are conditional on forward boundedness; no false global bound on all initial states is needed.

## originality

PASS

The original Sprott article and Li et al. symmetry review were available in full relevant text; both emphasize local equilibrium and positive-parameter chaotic/coexistence regimes. The exact monotone polynomial and complete nonpositive-a bounded-future/invariant-measure classification did not appear in inspected directly relevant sections. This is a qualified best-of-knowledge original global damping-sign result, with an honest unindexed older-analysis risk.

## value

PASS

This exact flow is an established model for reflection-symmetric chaotic behavior at positive parameter values, so proving the sharp complementary nonpositive damping bounded-recurrence regime is a natural dynamical boundary. The explicit globally polynomial Lyapunov identity, forced convergence on open half-spaces, harmonic critical plane, and complete stationary-measure characterization are mutually reinforcing structural results, not a numerical sweep.

The dated certificate retains the supplied scientific assessment, sources and limitations.
