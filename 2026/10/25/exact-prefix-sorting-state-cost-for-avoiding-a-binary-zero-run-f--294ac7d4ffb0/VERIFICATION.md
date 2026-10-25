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

The proof handles every integer \(r\ge1\). To stress-test its state and edge formulas, execute `python CHECKER.py`. Its deterministic assertions check all target/source Wheeler edge inequalities, exact forbidden-factor recognition, colex interleaving triples, and right-language separating suffixes for \(1\le r\le10\); exhaustive strings are checked through length \(\min(2r+5,14)\), a total of 218358 distinct (parameter,word) pairs. Observed final result: `VERIFY_OK total checked words: 218358`.

The checker does not enumerate all possible alternative WDFAs. Minimality instead follows from the general co-lex convex-fibre consequence of the Wheeler axioms, together with two explicit right-equivalent but interleaved words in each of \(r\) ordinary Myhill–Nerode classes. Finite testing does not establish infinite validity or literature novelty. An independent audit has not been performed.
