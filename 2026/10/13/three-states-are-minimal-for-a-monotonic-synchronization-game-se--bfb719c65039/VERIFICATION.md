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

Run `python3 verify.py` beside `certificate.json`.

The verifier generates every nondecreasing self-map of the normalized chain for \(n=1,2,3\), then every ordered binary pair of such maps. Ordinary synchronizability is checked by breadth-first search in the subset automaton.

Game outcomes are computed independently in two ways. The first solver works on all nonempty active subsets. The second works only on endpoint pairs and uses monotonicity to reduce synchronization of a subset to merging its minimum and maximum. Their outcomes must agree for every transition pair.

The exact three-state exceptional list is checked, as is its single orbit under letter interchange and chain reversal. For the representative \(a=(0,0,1)\), \(b=(0,2,2)\), the verifier checks \(aa\) as a reset word and checks that Bob's constant response \(b\) restores \(\{0,2\}\) after either Alice move.

As an independent literature-boundary check, the displayed three-state Bob-winning automaton from the 2024 paper is tested against all six state orders and is confirmed nonmonotonic.

Independent audit has not been performed.
