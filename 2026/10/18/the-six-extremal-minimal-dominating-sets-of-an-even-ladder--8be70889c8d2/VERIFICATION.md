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

# Verification of the extremal-ladder classification

Run `python3 verify.py` with Python 3.10 or later, without external modules. Its stdout must match `verification_output.txt` exactly.

The program constructs all five-column local transitions from the fundamental private-witness condition. It checks that the reachable finite state graph has 229 states, 471 arcs, and ten terminal states. It computes an integer potential, verifies **each arc inequality**, that all terminal potentials are at most zero, and that relaxation stabilizes without a positive-weight cycle. These facts prove the global cardinality bound for paths of arbitrary length.

It then restricts to tight arcs leading to a zero-potential terminal and intersects their language with an explicit six-prefix periodic pattern tracker. Of the 91 reachable product states, none is a terminal with no compatible periodic pattern. This is an **exhaustive finite automaton containment test** applicable to all \(n\), not a bounded enumeration of \(n\). The theorem's six constructions and parity boundaries are independently checked by direct neighborhood reasoning in RESULT.md.

Separately, it enumerates every vertex subset of \(L_n\) for \(1\le n\le9\), tests domination and private witnesses directly from closed-neighborhood bit masks, and checks the stated extremal families. These 349,524 subset tests provide an independent cross-check of the local state predicate, but are not used to extrapolate the theorem.

These checks do not constitute an independent external audit. Equivalent prior literature beyond the inspected sources remains a possible limitation.
