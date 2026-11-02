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

# Verification protocol and limits

The standalone verifier `verify.py` has no external dependencies. Run `python3 verify.py` in the same directory. The direct oracle builds every binary word on \(3\le n\le15\), excludes the two monochromatic words, evaluates every pair of opposite-type positions, and recomputes both participants' payoffs after the exchange. It uses ordinal ranks \((1,2,0)\) indexed by the numbers of same-type neighbors \(0,1,2\), which are equivalent to the specified payoff function when \(\Lambda>1/2\). A separate structural oracle checks the two forbidden-factor conditions. A third oracle computes coefficient lists of traces of three transfer matrices using order-three binary states.

There are 65,502 complete mixed binary words across those cycle lengths and 3,014,652 eligible distinct-color pairs checked by the direct oracle; every direct stability decision equals the forbidden-factor oracle, and every labeled count matches the transfer trace. The same script independently forms the integer transfer matrices, calculates eight traces and recovers both characteristic polynomials by the Newton identities, checking the two stated factors exactly.

This executable finite test cannot prove statements for all \(n\), exclude an unsearched equivalent publication, or certify every detail of the Perron argument. The universal theorem follows from the explicit neighbor-count identities, run constructions, regular-language bijection, and strict Perron–Frobenius comparison given in `RESULT.md`. Independent audit has not been performed.
