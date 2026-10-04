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

The proof has two components.

First, the all-dimensional identities are analytic. For the direct family, the normalized product factors as \(\Gamma_n=(D(a_\varepsilon)/D(a_0))I_n\); differentiation gives
\[
\Gamma_n'(0+)=n\left(\mathbb E L_n^2-\mathbb E|L_n|\right).
\]
The ordered-gap parametrization converts the two moments to those of \(S_{n-1}\), a sum of centered independent uniforms. The second moment is \((n-1)/12\), and integrating the truncated-power density gives the stated finite formula for \(A_{n-1}=\mathbb E|S_{n-1}|\).

Second, the sign classification uses exact arithmetic only where a finite check is genuinely needed. `verify_threshold.py` evaluates \(A_d\) as a rational number for \(1\le d\le12\), checks the derivative signs and the identity \(D(b)=2\sum b_j^2\), and prints `VERIFY_OK`. For every \(d\ge13\), the proof does not rely on the checker: Cauchy--Schwarz gives \(A_d\le\sqrt{d/12}<d/12\).

Limits: the verification is local in \(\varepsilon\) and does not test or assert global behavior of the path away from the origin. It also does not establish the unresolved reverse-projection inequality in dimensions four through eight.
