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

The initiating full text was checked at Theorems A and B, Section 2.3, Proposition 5.3, Lemma 5.5, Proposition 5.6, and the proof of Theorem B.

For
\[
(E,\varphi)=\bigoplus_{\alpha=1}^{s}(E_\alpha,\varphi_\alpha)\otimes\mathbf C^{m_\alpha},
\]
the commutant of the multiplicity algebra is \(\bigoplus_\alpha\operatorname{End}(E_\alpha)\otimes\operatorname{Id}\). The total trace map is
\[
(u_\alpha)_\alpha\longmapsto\sum_\alpha m_\alpha\operatorname{tr}(u_\alpha),
\]
so its trace-free kernel has rank \(\sum_\alpha d_\alpha^2-1\). Because every stable factor has degree \(0\), this kernel also has degree \(0\).

For a rank-\(R\), degree-\(0\) bundle on a genus-\(g\) curve,
\[
\chi(\mathcal C)=R(1-g),\qquad
\chi(\mathcal C\otimes K)=R(g-1).
\]
Hence the restricted Higgs complex has Euler characteristic \(-2R(g-1)\). Lemma 5.5 gives \(h^0=h^2=s-1\), yielding
\[
h^1=2R(g-1)+2(s-1).
\]
Theorem B identifies this \(h^1\) with the vertical tangent rank. Theorem A makes each stratum a holomorphic submersion over \(\mathcal T_g\), whose complex dimension is \(3g-3\).

For the extremal non-stable statement, if \(s\ge2\) then
\[
\sum_\alpha d_\alpha^2\le(r-s+1)^2+s-1.
\]
Writing \(t=s-1\), the half-dimension gap between this upper bound and the \(s=2\) type is
\[
(t-1)\left((g-1)(2r-t-2)-1\right)\ge0.
\]
If \(s=1\) is non-stable, then the multiplicity is at least \(2\), so \(d_1\le r/2\) and the dimension is smaller. Thus ranks \((r-1,1)\), multiplicities \((1,1)\), maximize the non-stable dimension.

A finite enumeration for \(2\le r\le7\) and \(2\le g\le5\) reproduced the same maximum for every positive rank/multiplicity decomposition. This is a stress test only and is not used as proof.

Limits checked: no claim is made for \(\mathrm{GL}_r\), twisted or parabolic Higgs bundles, unmarked coarse curve moduli, closure incidences, or transverse singularity types.
