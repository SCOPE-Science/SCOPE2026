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

# Verification of the exact support-cap tail envelope

The mathematical argument is self-contained after the explicitly credited standard two-point mean decomposition, whose mixing coefficients are reproduced and checked in `RESULT.md`. The nontrivial calculations are: the product minimum \(bd\geq L(3-L)\) for \(3/2\leq L\leq2\); the high probability bound \(q\leq1/b\); the monotone gradient of the both-cross functional; and the exact identity
\[
\frac{2t+3t^2}{(1+2t)^2}-\frac12=\frac{2t^2-1}{2(1+2t)^2}.
\]
The proof handles all real caps, nonidentical laws, degenerate means, and both closed-event phase endpoints. Explicit two-point laws attain each piece, including the threshold discontinuity and the \(5/9\) asymptote at a finite cap.

The packaged `check.py` is executable using Python 3 and its standard library alone (`python check.py`). Its actual replay gave `PASS 32397 exact-rational checks; analytic proof still required`. It enumerates paired mean-one two-atom marginals on rational grids over caps \(1\) through \(4\), verifies individual probabilities against the proposed envelope, verifies explicit extremizers for rational caps \(1\) through \(5\), and checks the algebraic phase-comparison identity at rational inputs. The program is *not* an exhaustive enumeration of continuous probability laws and is not a replacement for the analytical proof.

No separate independent audit has been performed. The result does not address other thresholds, dependence, unequal caps, or more summands.
