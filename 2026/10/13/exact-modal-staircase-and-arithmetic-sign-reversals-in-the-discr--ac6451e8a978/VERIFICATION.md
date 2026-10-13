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

# Verification record

The exact source pmf was independently rewritten as \(C\tau(1+t)e^{-\theta t}\) on the merged grids. Adjacent logarithmic score ratios were checked symbolically; strict concavity of \(\log(1+t)\) and the limits of its successive secants establish the complete infinite staircase. Coprime arithmetic shows that double labels occur at integer multiples of \(ab\) on the scaled grid when \(\tau^2=a/b\).

Run the accompanying ordinary Python script using `python3 verify_modes.py`. Its standard-library numerical experiments include direct closed-form pmf reconstruction; checks of the predicted mode sets for the first twenty-one nonzero sites for \(\tau=\sqrt{3/2}\); boundary equality tests; and numerical normalization for four parameter choices. The observed terminal status was `normalized weights, transition ties, and direct mode scans: PASS`. The script proves neither the infinite statements nor priority; those are assessed through the written mathematical argument and scholarly comparison, respectively.

The proof assumes exactly the source's support \(\mathbb Z\) and strictly positive \(\theta,\tau\). It does not cover the nonnormalizable endpoint \(\theta=0\), nor permit floating-point tests to decide exact rationality. No independent audit has been performed.
