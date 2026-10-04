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
The checked claim concerns fixed \(0<c<1\), the source space \(X_c\), and its diagonal operator \(D_c\). The proof was reconstructed from the source's property \((M)\), weak nullity of \((e_n)\), explicit norm recursion, and strict norm decrease for \(D_c\).

For a fixed center \(x\), the crucial calculation is
\[
\lim_n\|x+e_n\|=\max\{1,\sqrt{\|x\|^2+c^2}\}.
\]
Property \((M)\) gives the limsup after replacing \(x\) by \(\|x\|e_0\); the latter has an explicit formula from the recursion. Applying the same argument to every subsequence rules out a different liminf. Replacing \(x\) by \(D_cx\), and using \(n/(n+1)\to1\), gives the numerator limit for the normalized one-spike sequence.

Inside \(\|x\|\leq\sqrt{1-c^2}\), both limiting factors equal one. Outside this ball, the source's strict inequality \(\|D_cx\|<\|x\|\) makes the numerator factor strictly smaller than the denominator factor. Thus the if-and-only-if threshold is an infinite-dimensional analytic statement, not an inference from finite sampling.

The source was inspected in full-text form at the relevant definitions, lemmas, proposition, and theorem. Older WMP sources and targeted semantic searches were checked for equivalent formulations and dominating results. No covering statement was located. Residual originality risk remains because the focal source is recent and the extension is concise.
