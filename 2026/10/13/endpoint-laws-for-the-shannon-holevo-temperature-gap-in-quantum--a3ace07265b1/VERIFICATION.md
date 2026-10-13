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

The exact formulas were reconstructed from the channel-capacity and temperature equations before any numerical evaluation. The identity
\[
\operatorname{asech}(2\sqrt{q(1-q)})=\operatorname{atanh}(1-2q)
\]
was checked on the branch \(0<q<1/2\) by applying \(\operatorname{sech}\) to the right-hand side and using \(1-(1-2q)^2=4q(1-q)\).

The proof uses the two standard local binary-entropy expansions
\[
1-h_2(1/2-\delta)=\frac{2\delta^2}{\log2}+O(\delta^4)
\]
and
\[
h_2(p)=\frac{p\log(1/p)+p+O(p^2)}{\log2}.
\]
Asymptotic inversion was carried out explicitly in the proof, including the \(\log\log(1/R)\) correction at low rate.

The accompanying script evaluates the exact boundaries and normalized endpoint expressions for decreasing rate deficits. Its output is only a consistency check: the proof does not infer any infinite-limit statement from those finite samples.

The scientific scope was also checked against the assumptions of the anchor: the statement is restricted to the uniformly coupled commuting reduction and to information-theoretic capacity boundaries. It does not claim efficient Holevo-bound achievability or optimality outside QD-HDQI.
