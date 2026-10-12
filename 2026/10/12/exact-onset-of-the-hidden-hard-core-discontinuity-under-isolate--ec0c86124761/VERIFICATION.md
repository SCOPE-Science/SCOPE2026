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
The proof uses two exact interfaces. First, the all-zero second-layer preimage is the hard-core independent-set gas with activity \(\lambda=p/(1-p)\). Its regular-tree directed-edge recursion is \(r\mapsto\lambda/(1+r)^d\), with the exact uniqueness threshold \(\lambda_{\mathrm{hc}}(d)=d^d/(d-1)^{d+1}\). Second, Lemma 1 and Remark 2 of arXiv:2304.03102v2 transfer a persistent parity gap in the first-layer alternating cylinder into a contradiction with second-layer quasilocality.

For a root of degree \(q=d+1\), the alternating local cylinder has exact probability
\[
P_q(r)=\frac{r^q}{(1+r)^q+\lambda},
\]
and
\[
P_q'(r)=\frac{q r^{q-1}((1+r)^{q-1}+\lambda)}{((1+r)^q+\lambda)^2}>0.
\]
Hence the two hard-core cavity limits remain visible in precisely the local quantity used by the source.

The standalone `verify.py` checks the critical identity exactly with rational arithmetic and replays representative above-threshold parity iterations at high precision. The numerical part is corroborative only. It is not used to prove convergence, uniqueness, non-uniqueness, or the infinite-volume quasilocality statement.

The theorem does not establish Gibbsianness at or below \(p_{\mathrm{hc}}(d)\); it establishes the exact onset of the specified all-zero hidden-hard-core witness and non-quasilocality strictly above it.
