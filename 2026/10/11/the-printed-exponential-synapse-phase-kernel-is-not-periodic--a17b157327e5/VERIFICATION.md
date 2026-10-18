---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS. For exponential decay ds/dt=-beta s with reset s->1 at every presynaptic spike, the unique periodic gate (up to spike value conventions) is exp[-beta((t+phi) mod T)], with its reset at t=T-phi. In contrast the printed single branch over the full t integral factors H_print(phi)=A exp(-beta phi), H_odd=-2A sinh(beta phi), either nonperiodic for A!=0 with no anti-phase zero or identically zero when A=0. The full primary article’s reset rule, interaction integral, equation (23) and anti-phase discussion were inspected in lawful accessible HTML. This is a correction to the printed model equation, NOT proof that author code, numerical plots or first-order reduction itself are wrong. Pure algebra, no finite simulation.

## originality

PASS

PASS best-of-knowledge for diagnosis of this specific 2026 printed equation, not for the general elementary periodic-extension rule. Primary Cheng–Campbell weak-coupling equation (23) literally omits the reset wrap and its own text assumes periodicity and anti-phase; neither that source nor targeted Resultary/online searches showed an acknowledged correction. General integrate-and-fire synapse literature knows cyclic reset gates, which are used as a premise; the specific published contradiction and concrete two-branch correction are the claimed original observation. Unindexed erratum/typographical clarification remains possible.

## value

PASS

PASS narrowly. Although periodic extension is elementary, failure of this explicit equation removes the nontrivial anti-phase equilibrium on which the particular weakly coupled-neuron phase analysis relies if printed formula is implemented literally. The minimal two-branch correction is necessary to specify and reproduce the central phase interaction. This motivates the targeted counterexample beyond a trivial sign/normalization typo. It does not claim numerical figures were computed wrongly; if the paper’s code correctly handled resets, practical impact is limited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
