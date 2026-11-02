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

# Verification and limits

The included `verify.py` was run with Python 3 from its final package directory. Its output was:

```
n 2 recursive trees 1 joint probabilities verified
n 3 recursive trees 2 joint probabilities verified
n 4 recursive trees 6 joint probabilities verified
n 5 recursive trees 24 joint probabilities verified
n 6 recursive trees 120 joint probabilities verified
n 7 recursive trees 720 joint probabilities verified
n 8 recursive trees 5040 joint probabilities verified
PASS 210 exact joint probabilities; matching conditional law and beta-binomial tail
```

The program enumerates every rooted recursive tree through size eight, computes fringe sizes and child counts, and compares exact rational joint laws against the conditional root-degree generating function and exact Pólya-urn fringe tail. This is finite exhaustive checking of a finite identity, not an infinite proof. The proof in `RESULT.md` independently gives an all-size conditioning argument, a uniform moment-generating-function bound, exact tail estimates, and the probabilistic limiting argument, relying on the clearly named earlier maximum-degree and maximum-label theorems. Historical novelty is qualified by incomplete access to some older full texts. Independent mathematical audit has not been performed.
