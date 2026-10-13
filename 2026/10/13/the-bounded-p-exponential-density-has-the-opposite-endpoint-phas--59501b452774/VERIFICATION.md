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
The exact density is
\[
f_p(x)=\frac{p}{(p+1)^p}(p+1-x)^{p-1}.
\]
Therefore
\[
f_p'(x)=-\frac{p(p-1)}{(p+1)^p}(p+1-x)^{p-2}.
\]
This gives strict increase for \(0<p<1\), constancy at \(p=1\), and strict decrease for \(p>1\).

Writing \(\delta=p+1-x\),
\[
f_p(p+1-\delta)\delta^{1-p}=\frac{p}{(p+1)^p}.
\]
Hence the right-endpoint density diverges only for \(0<p<1\), is constant for \(p=1\), and vanishes for \(p>1\).

The log-density curvature is
\[
\frac{d^2}{dx^2}\log f_p(x)=-\frac{p-1}{(p+1-x)^2},
\]
and
\[
h_p'(x)=\frac{p}{(p+1-x)^2}>0.
\]

The included checker evaluates these identities on representative parameter values and verifies density normalization numerically. The phase classification itself is analytic.
