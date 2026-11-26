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

A doubly-yellow arm's leaf has to be ignited yellow, no later than the round its intermediate burns; if they burn together the intermediate must spread before that leaf ignition. With a yellow center the intermediate would spread green immediately after a yellow leaf ignition, and cannot spread yellow simultaneously with the leaf. With a green center first burned in round T, a doubly-yellow arm with ignited intermediate needs the green center to keep it tied at the first spread after its leaf ignition. The center cannot predate that ignition, since otherwise it spreads yellow to the still-unburned intermediate before or during the leaf's ignition round. This forces leaf ignition in T. With a spread-burned yellow intermediate, its leaf must still be unburned at the start of the spread, and the green center would produce positive influence on the first spread after T. The intermediate therefore spreads in T+1 and its leaf must be ignited in T+1. One ignition per round bounds the two types by one each. Independent replay of RESULT.md line 30: each of a1, b2, b3, a2 is unburned at its ignition; the center and b1 are green after round 2, intermediates j>=3 are yellow after round 3, and leaves j>=4 turn green in round 4. The two center/leaf contributions to a2 cancel until its ignition. This gives exactly two double arms and m+2 yellow vertices for every m>=3. Color reversal gives the plurality bound. The cited path formula gives P3 and P5 values 2 and 3. Inspected verify.py's simultaneous labelled and orbit transitions without execution; the recorded finite checks are not the proof.

## originality

PASS

The checked earlier exact results cover paths and ordinary stars, not the two-edge arms of this all-negative signed tree, and the tree parameter match from domination theory is a different invariant. Pass is confined to the branching plurality formula and sharp two-arm obstruction.

## value

PASS

An exact all-order terminal-color optimum for a natural first branching family answers a concrete part of the signed-tree problem. The center's two-slot timing obstruction is structural, and a uniform legal construction saturates it rather than extrapolating a census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
