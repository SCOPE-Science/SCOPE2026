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

For a computational-basis code \(C\), the conditional success probability on survivor set \(S\) is the number of distinct projected words divided by the message count:
\[
P_{\mathrm{succ}}(S)=\frac{N_S(C)}{M},
\qquad
N_S(C)=\left|\{\pi_S(c_m):m\in[M]\}\right|.
\]
The analytic proof exhibits codes with
\[
N_S(C)=\min\{M,2^{|S|}\}
\]
for every \(S\) and every \(M\) when \(n\le3\). The only nontrivial short cores are \(\{00,01,10\}\), \(\{000,011,101\}\), and the even-parity code \(\{000,011,101,110\}\). Adding unused vertices preserves already saturated lower-dimensional projections; after all cube vertices are present, repetitions preserve every projection count.

The accompanying standard-library checker enumerates all survivor sets for the canonical construction for \(1\le n\le3\) and a range of message sizes extending beyond the full-cube threshold. It verifies the projection identity exactly and prints `VERIFY_OK`. This finite computation is corroborative only; the proof for all \(M\) is the explicit case analysis in `RESULT.md`.

The external ingredients independently checked in the primary source are the fixed-pattern dimension bound, the feedback formula for message-independent correlated erasures, and the strict no-feedback gap for \(n=4\), \(M=4\), \(0<p<1\). The result does not determine the exact four-use no-feedback optimum or assert maximum-error equality without feedback.
