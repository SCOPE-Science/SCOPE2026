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

# Reproduction and limits

Run `python3 verify_binary_jr.py` in the directory containing the script. The verifier enumerates all nonempty two-alternative approval ballots (the three subsets of a two-element alternative set) for \(n=3,\ell=3\) and \(n=3,\ell=4\). It computes the unconstrained welfare and all \(2^\ell\) outcomes, with JR tested by satisfaction of every voter, using exact integers and `fractions.Fraction`. It checks the sharp bound and the exact extremizer characterization and counts all equality profiles. Additional deterministic four-voter testing probes beyond the exhaustive sizes.

Expected successful output is:

```
CHECK_OK n=3 horizon=3 profiles=19683 equality=24 sharp=6/5
CHECK_OK n=3 horizon=4 profiles=531441 equality=48 sharp=8/7
CHECK_OK n=4 horizon=4 deterministic_samples=1000 sharp=6/5
```

Exhaustion for small \(n,\ell\) does not constitute an infinite proof. The proof is in `RESULT.md`; no randomized test can rule out an untested counterexample in the full domain. The numerical exactness of the computations does not establish bibliographic priority or independent review.
