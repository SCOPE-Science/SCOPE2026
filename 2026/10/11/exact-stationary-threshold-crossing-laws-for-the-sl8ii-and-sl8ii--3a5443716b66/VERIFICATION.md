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

The proof is symbolic. Two exact differential identities drive the result:
\[
\dot x=y^2(\kappa y^{2r-1}-1),
\qquad
\frac{d}{dt}(cy-z)=ac z^2-bx^2.
\]
For a compactly supported invariant probability measure, both observables have zero stationary mean derivative. The sign of the first identity around \(h=\kappa^{-1/(2r-1)}\) gives the support split after separately checking the invariant zero levels \(y=0\) and \(y=h\).

The included `verify.py` uses exact rational arithmetic to replay the two source-parameter ratios and evaluates both algebraic identities at several rational states for \(r=1\) and \(r=2\). It prints `VERIFY_OK`. These finite evaluations are implementation checks only; the infinite statement is proved by the displayed symbolic identities and measure argument.

No independent audit has been performed.
