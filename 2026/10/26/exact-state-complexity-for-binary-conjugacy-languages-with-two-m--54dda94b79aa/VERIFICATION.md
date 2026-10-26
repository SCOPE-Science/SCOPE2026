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

## Scope

The proved result applies to every pair of nonnegative integers \(a,b\), to the language consisting of all distinct cyclic rotations of \(1\,0^a1\,0^b\), and to the state count of its smallest **complete deterministic** finite automaton. Independent external validation has not been conducted.

## Reproduction

Run `python3 checker.py` with Python 3 and no installed dependencies. The checker creates the set of cyclic rotations without assuming they are all distinct. It constructs a prefix trie and computes bottom-up Myhill–Nerode equivalence classes using the final status and ordered child states, counting one explicit dead state. It separately constructs and counts the complete sets of right quotients at every prefix length in smaller cases. These two implementations do not use the proof's rectangle-collision counting argument.

The full finite test set is all \(0\leq a\leq b<24\) (300 minimizations), all \(0\leq a\leq b<9\) (45 quotient inventories), plus 121 ordered pairs through ten for cyclic-gap symmetry. Expected representative state counts: \((0,0)\mapsto4\), \((1,1)\mapsto9\), \((2,2)\mapsto16\), \((2,5)\mapsto31\), \((3,5)\mapsto41\), \((5,10)\mapsto94\).

## Proof obligation and limits

Finite computations only corroborate the theorem. The infinite quantifiers are discharged by enumerating all possible nonempty right quotients and proving that only a translated square family of A-only/B-only prefixes can coincide. The source-word boundary cases \(a=b=0\) and \(a=b>0\) are explicitly included. The argument is not asserted for other weights or nondeterministic automata. Priority caveats appear in the scientific review; there has been no independent external audit.
