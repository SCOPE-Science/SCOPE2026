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

# Verification and reproduction

This package includes `check.py`, an executable pure-stdlib Python checker. Run `python3 check.py` from the directory containing the package files. It independently implements Kripke satisfaction directly on nonempty subsets represented by integer bitmasks, with the accessibility test as nonzero bitmask intersection. The canonical quotient is constructed from independent bit-vector atom colors, and formulas use explicit recursive syntax trees rather than a symbolic simplifier.

Observed clean replay:

```
PASS color compression, individual formula-world comparisons: 315460
PASS separator tests: 10466
PASS exact type signatures: 8434
```

The first check compares 315,460 direct evaluations at source worlds and corresponding quotient worlds, using reproducible randomly generated modal formulas up to nesting depth four and finite assignments with \(1\le n\le4\), \(1\le k\le3\). It separately asserts the surjective bounded-morphism back condition on the finite tested instances. The second tests the explicit separating-formula family against complete frames. The third exhaustively enumerates small assignment/state instances and checks the \(\delta_t\), \(\Diamond\delta_t\), and \(\Diamond\Diamond\delta_t\) characterizations and the predicted count of distinct profiles.

These finite experiments are corroboration only; the infinitely quantified result follows from the fully written bounded-morphism argument and explicit distinguishing formulas in `RESULT.md`. No Lean proof or outside expert certification is claimed. Independent audit has not been performed.
