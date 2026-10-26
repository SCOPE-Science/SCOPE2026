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

# Mathematical verification

The source `verify.py` uses exact integer arithmetic and no nonstandard libraries. The state of a candidate representation stores two previous one-bit flags and one bounded carry. For every given input bit, it exhausts all four possible summand digit pairs subject to the adjacent-one restriction and the carry parity rule. Determinization collects all reachable states. This exact automaton is compared with deterministic recognizers for the six proposed complements.

The complete finite product-state tables are in `state_table.txt`. Reachable state counts for multipliers \(1\) through \(6\) are \(4,6,18,9,41,29\). Every outgoing final-one transition from each reachable state is checked for opposite acceptance by the two automata; the canonical numeral for zero is checked separately. This checks all positive integers at all bit lengths by induction on the input word, rather than only finite samples.

For a secondary, independently structured check, the verifier enumerates fibbinary elements directly by the bitwise criterion and all sums no larger than \(10000\), confirming all six asserted formulas throughout that range. It does not use that bounded enumeration as the infinite proof.

To run, execute `python3 verify.py`. To reproduce the transition table, execute `python3 verify.py --write-certificate state_table.txt` in a fresh directory and compare it with the supplied table. The proof establishes only the six stated dilations; published-source completeness and independent mathematical review are not certified.
