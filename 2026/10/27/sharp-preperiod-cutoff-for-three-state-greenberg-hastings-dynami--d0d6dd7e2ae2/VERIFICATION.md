---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

From time one every 1 has a neighboring 2 (its previous-time exciter). If a right-moving head at j appears at the next time, j was resting and j−1 was excited; the requisite refractory neighbor of j−1 had to be j−2. This is a unique right-moving ancestor; conversely a head advances exactly when its target rests. Reflection gives the other direction. For opposite heads at time one the clockwise separation d lies in 0..n−2; d=n−1 would give an excited head and a refractory body at the same vertex. If both survive, after floor(d/2) advances they share a head surrounded by refractory sites (even d), or have mutually blocking adjacent heads (odd d). Thus by time floor(n/2)+1 at most one direction remains. Then any head's forward site is resting: a 2 there would make the opposite particle, while a 1 there needs its own forward refractory body and would also make an opposite particle. One further update drops all unpaired refractory sites and realizes a clean rotating train, or gives zero if no excitation remains. The rotation relation persists by translation-equivariance, so the period divides n. With one initial 1 all forward sites on the intervening arc are resting until the two heads meet or become adjacent, at time floor(n/2); excitation disappears next and the last refractory cells disappear one update later. This also handles n=3 (100→211→022→000), and eventual zero rules out earlier periodic entrance in the witness. Independent enumeration, without invoking the supplied verifier, checked 265707 states for n=3..11, giving depths 3,4,4,5,5,6,6,7,7 and only zero or translating recurrent states. Replay algorithm: use ternary state indices and the displayed local update; peel indegree-zero vertices, assign depth zero to the remaining cycles, then propagate depths backward in reverse peel order. The source verify.py and its documented invocation were inspected, not executed. These finite checks only corroborate the all-size particle proof.

## originality

PASS

The supported distinct claim is the exact universal least-preperiod cutoff for all initial states on the undirected finite cycle, including entry into rotating states. One-dimensional traveling pulses, their annihilation, and activity/winding relations are not new here. The inspected strongest comparisons did not establish the same uniform finite entrance bound.

## value

PASS

The exact cutoff bounds the time necessary to identify an attractor for every coloring in a standard finite excitable automaton. It uses the geometry of two annihilating fronts and applies also to nonsynchronizing states, so it is more informative than an entropy or long-run-activity statement. Sharpness is realized by a natural minimal excitation and tracks the exact final refractory delay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
