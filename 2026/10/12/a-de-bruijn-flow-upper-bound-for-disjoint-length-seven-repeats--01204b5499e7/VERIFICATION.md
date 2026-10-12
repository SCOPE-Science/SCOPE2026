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
# Verification

Run `python3 verify.py` in the same directory as `certificate.json`.

The checker reconstructs the binary order-\(6\) de Bruijn graph from first principles. For every length-\(7\) word it recomputes the least period and the capacity
\[
\left\lceil\frac{7}{\operatorname{per}(w)}\right\rceil.
\]
It verifies total capacity \(236\).

For each possible walk incidence pattern—one closed case and every ordered pair of distinct start and end vertices—the certificate provides an integer potential. The verifier checks the corresponding linear-programming dual inequality exactly with integer arithmetic. Every case requires deletion of at least \(16\) capacity units.

A matching feasible deleted-edge vector of total multiplicity \(16\) is checked directly against the incidence equations and capacity bounds. Therefore the relaxation optimum is exactly
\[
236-16=220
\]
windows, and every admissible binary word has length at most
\[
220+6=226.
\]

The verification establishes the flow relaxation and its numerical optimum. It relies on the cited published occurrence lemma to connect an admissible word to the edge capacities. It does not claim that the relaxation itself is realizable by a word.
