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

The proof reuses Section 4 of arXiv:2609.37471v1 and changes only the upper bound allowed for \(\delta=(N-|A|)/N\). The three deficit-sensitive checks are:

1. Heavy-prime and final-pool slack:
\[
3073\eta_0<\frac{c_0}2.
\]
2. Small-prime richness at \(p_0=e^{3200}\), uniformly for \(N\ge e^{200000}\):
\[
e^{-200000}+2\eta_0<\frac1{2p_0}.
\]
3. The third failure probability in Lemma 10:
\[
\frac{8\eta_0}{c_0}<\frac18.
\]

For \(\eta_0=e^{-3200}/5\) and \(c_0=e^{-1400}\), these reduce after division by common exponential factors to
\[
\frac{3073}5e^{-1800}<\frac12,\qquad
e^{-196800}+\frac25<\frac12,\qquad
\frac85e^{-1800}<\frac18.
\]
The script `verify.py` evaluates these with 80-digit decimal arithmetic and asserts positive margins. It also checks the logarithm of the improvement factor \(e^{1800}/5\).

Replay command: `python verify.py`

Observed output:

`VERIFY_OK heavy_margin_scaled=5.0000000000000000000000000E-1 pair_margin_scaled=1.0000000000000000000000000E-1 coupling_margin=1.2500000000000000000000000E-1 log_improvement=1798.3905620875658996253992407`

The computation is only a numerical consistency replay of explicit inequalities. The all-\(N\), all-admissible-set conclusion follows from the exact inequalities in RESULT.md together with Li's published lemmas. No independent audit has been performed.
