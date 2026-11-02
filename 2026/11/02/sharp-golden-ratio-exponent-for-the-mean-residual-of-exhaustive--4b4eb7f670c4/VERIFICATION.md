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

# Verification of the mean residual power-law theorem

`verify.py` is self-contained and needs only Python's standard library. Running `python verify.py` produces the results recorded in `verification-output.txt` and ends with `VERIFY_OK`.

It computes the exhaustive Peres map recursively from its pairwise definition and checks all \(2^N\) inputs for each \(1\le N\le12\), with exact rational mean comparisons against an independently implemented binomial recurrence. The total number of checked input strings is \(\sum_{N=1}^{12}2^N=8190\). It separately computes both rational expected residual-length and residual-one counts through length 90 and verifies their exact ratio \(2:1\), and checks the stated numerical barriers at these finite lengths.

The analytic all-length evidence is the detailed proof in `RESULT.md`: the binomial smoothing deficit is uniformly bounded by \(4\) using curvature and the Chernoff inequality; lower and upper barriers are established by complete strong inductions, handling the zero-child atom and odd remainders. Finite numerical checks are sanity checks only. There is no formal theorem prover, independent mathematical audit, or claim that enumerating finite strings certifies an infinite statement. Existence of a limiting ratio \(\mathbb E|R_N|/N^\alpha\), the maximum-residual upper exponent and biased-source rates are not established.
