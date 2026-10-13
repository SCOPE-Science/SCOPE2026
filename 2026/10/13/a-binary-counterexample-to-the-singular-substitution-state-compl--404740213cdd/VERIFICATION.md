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

# Verification of the singular-substitution counterexample

Place `certificate.json`, `check_certificate.py`, and `nfa_crosscheck.py` together. With Python 3 and no third-party packages, execute:

```text
python3 check_certificate.py
python3 nfa_crosscheck.py
```

The first program validates all \(15+8+127=150\) distinct canonical quotient states and \(300\) binary transition entries of the three complete DFAs. It independently recomputes all first-occurrence suffix residuals, checks canonical antichains, start states, transition closure, and reachability. Because each state labels the unique maximal-generator antichain of a finite downward-closed language, uniqueness of the labels is a mathematical distinguishing argument establishing **minimality**, not only an upper bound.

Expected first output:

```text
VERIFY_OK complete_reachable_quotients L=15 K=8 substitution=127 product=120 excess=7
```

The second program directly enumerates the short input languages, constructs a separate epsilon-NFA for the singular substitution, determinizes its \(337\) reachable subsets, and minimizes them by partition refinement. It does not read or reuse the transition certificate. Expected second output:

```text
VERIFY_OK independent_epsilon_NFA=337 deterministic_subsets minimum=127 originals=15,8
```

All integers are exact. These algorithms exhaust the finite quotient automata; they are not finite sampling offered as an infinite theorem. The formal mathematics separately proves why those finite automata recognize exactly the languages stated. Independent external audit has not been performed.
