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

# Verification of the shortest ternary crucial Abelian-cube-free classification

`verify.py` is a standalone Python 3 program using no packages beyond the standard library. Execute:

```
python3 verify.py
```

The program implements the Abelian-cube predicate directly by comparing three adjacent factor Parikh vectors. It enumerates all ternary words of lengths below eleven to test the known minimum, then independently enumerates all \(177147\) words of length eleven. It counts \(50520\) cube-free words and \(264\) crucial ones, constructs the asserted \(44\) normal-form representatives from the separate formula, obtains their six alphabet relabelings, and checks exact set equality. It also verifies the \(44\) distinct relabeling orbits and all six permutations of witness block lengths \(1,2,4\).

Observed successful output:

```
PASS: no ternary crucial Abelian-cube-free words below length 11;
PASS: 3^11=177147 words checked; 50520 Abelian-cube-free;
PASS: 264 crucial words; 44 alphabet-relabeling orbits;
PASS: 12 x 4 - 4 = 44 canonical constructions;
PASS: all six length-witness permutations (1,2,4), 44 each;
PASS: exact agreement of exhaustive and structural descriptions.
```

All assertions must succeed for these lines to print. Exhaustion is conclusive for the specifically stated finite length and alphabet; the structural steps in `RESULT.md` explain why the family is exhaustive rather than merely empirically observed. The cited older minimum-length theorem is independent prior work. The package does not establish originality against all possible publications and has not undergone independent audit.
