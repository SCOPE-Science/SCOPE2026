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

# Reproducibility and verification

The self-contained `verify.py` script uses Python 3 standard-library modules only. Run `python verify.py` from the directory containing this file and the script. It checks exact integer certificates for the strict escape example, a rational identity, numerical pair recurrences, convergent mean-shift series with a proven nonnegative remainder bound, critical-parameter bisection, and representative checks on the asymptotic laws.

For the initial opinions \(0,1\), utility \(U(x)=3^x\), confidence threshold greater than one and \(\mu=3/4\), the program reports the consensus \(1.009641160060\ldots\) and fixed-utility critical learning rate \(0.745320731512\ldots\). The exact proof of escape is the three-term radical comparison in RESULT.md, not this decimal output. In numerical series evaluation, the remaining tail after the loop is at most \(\mu\eta r^{2K}/(1-r^2)\), where \(K\) is the number of terms used and \(r=|1-2\mu|\).

The finite program neither proves the uniqueness of the threshold, which uses an analytic strict-monotonicity argument, nor proves the infinite-parameter limits, which use geometric bounds and Riemann sums. No nonzero-noise stochastic model was verified or claimed. Independent audit has not been performed.
