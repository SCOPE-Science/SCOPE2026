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

# Reproduction and proof checkpoints

From the directory containing the complete package, execute `python3 check_bem.py` using a standard Python 3 interpreter. No nonstandard modules or downloaded datasets are required.

Observed outputs from the packaged checker:

```
posets n=1: 2 basic frames, 2 validating frames
posets n=2: 34 basic frames, 26 validating frames
posets n=3: 2942 basic frames, 1262 validating frames
chain n=1: valid=2, strong=2
chain n=2: valid=5, strong=4
chain n=3: valid=22, strong=8
chain n=4: valid=157, strong=16
two-world strict witness: verified
All checks passed
```

The checker lists every labelled partial order on up to three points, enumerates every relation satisfying \(x\leq y\wedge yRz\Rightarrow xRz\), and tests every upward-closed valuation of the atom \(p\) against the original truth clauses. It separately computes the explicit first-order correspondence. Agreement across these finite cases is supplemental to the general proof in `RESULT.md`. The chain enumerator independently tests the closed formula through four points. These tests do not establish infinite-cardinality correspondence or absence of earlier literature; those statements require the symbolic proof and source comparison, respectively.

The proof's critical general steps are: (i) persistent truth sets are upsets; (ii) failure of the proposed inclusion admits the countervaluation \(p=\uparrow R(y)\); (iii) the inclusion makes boxed truth constant along comparable worlds; (iv) on chains, each successor above the common least successor has an independent initial-segment cutoff. The empty-row and one-point boundary cases are explicitly included.
