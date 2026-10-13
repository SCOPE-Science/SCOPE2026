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

The claim was checked by direct reconstruction from the published overhead form of the single-shot failure theorem.

For fixed \(p<p_{\rm RG}\), write the source estimate as
\[
P_{\rm fail}(T)\le CTn\exp(-cm^\alpha)
\]
with \(C,c>0\). For any fixed \(s,r\ge0\), choose \(K\) with \(cK^\alpha>s+r+1\). If \(T\le n^s\) and \(m=\lceil K(\log n)^{1/\alpha}\rceil\), then
\[
P_{\rm fail}(T)\le Cn^{s+1-cK^\alpha}\le n^{-r}
\]
for all sufficiently large \(n\).

The total output size is \(N=nm\). Since \(m=\Theta((\log n)^{1/\alpha})\), one has \(\log N=\log n+O(\log\log n)\), so \(m=\Theta((\log N)^{1/\alpha})\). A positive-rate seed has \(k=\Theta(n)\), giving
\[
k=\Theta\!\left(\frac{N}{(\log N)^{1/\alpha}}\right).
\]
The source decoder time \(O(\log m)\) becomes \(O(\log\log N)\).

No finite experiment is used. The verification does not establish necessity of this overhead, optimality of the rate, transformed-code distance scaling, or sharpness of \(\alpha\).
