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

Run `python3 verify.py` using Python 3 and its standard library. The verifier reconstitutes every simplex as a subset of a closed cube neighborhood, tests every signed simplicial trace under all affine automorphisms in dimensions two through five, and compares the value with the independent cycle-parity expression. It checks the translated average against \(\binom{a_1}{2}-a_2\) for every coordinate permutation and tests thirty-five further full-group elements in dimension six. The completed local run printed:

```
n=2: 8 automorphisms, 14 nonempty faces, H2 dimension 1, all character traces and invariant exterior-square characters agree
n=3: 48 automorphisms, 72 nonempty faces, H2 dimension 7, all character traces and invariant exterior-square characters agree
n=4: 384 automorphisms, 352 nonempty faces, H2 dimension 31, all character traces and invariant exterior-square characters agree
n=5: 3840 automorphisms, 1616 nonempty faces, H2 dimension 111, all character traces and invariant exterior-square characters agree
n=6: 35 selected automorphisms, 7072 nonempty faces, all traces agree
VERIFY_OK
```

The code operates directly on enumerated face sets, not on stored matrices from another calculation. These computations are finite checks, not a substitute for the uniform proof. The topological concentration is independently supplied by Adams–Shukla–Singh, arXiv:2212.05871, Theorem 4.1. No independent audit has been conducted.
