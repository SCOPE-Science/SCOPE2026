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

Let
\[
F_0=F(\omega_0),
\qquad
m=\mu(\{\omega_0\}),
\qquad
\ell=m\langle F_0,S^{-1}F_0\rangle.
\]
The critical hypothesis \(\ell=1\) implies \(m>0\). Therefore no measurable set containing \(\omega_0\) can have measure zero.

The erased frame operator is obtained by subtracting exactly the singleton contribution:
\[
S_{-0}=S-m\theta_{F_0,F_0}.
\]
With
\[
u=\sqrt m\,S^{-1/2}F_0,
\]
conjugation gives
\[
S^{-1/2}S_{-0}S^{-1/2}=I-\theta_{u,u}.
\]
The only nontrivial eigenvalue of this rank-one perturbation is
\[
1-\|u\|^2=1-\ell.
\]
Since \(S_{-0}\ge0\), \(0\le\ell\le1\). Since \(S^{1/2}\) is invertible, the erased mapping is a continuous frame exactly when \(1-\ell>0\).

At \(\ell=1\),
\[
S_{-0}S^{-1}F_0=(1-\ell)F_0=0.
\]
Thus \(S^{-1}F_0\ne0\) is an explicit witness to loss of the lower frame bound.

The source's full proof was inspected. Its almost-everywhere conclusion off \(\omega_0\) is compatible with the calculation above, but the set it defines contains the positive-measure atom, so its total measure is \(m\), not zero. The earlier 2006 robustness theorem was also checked and supplies only the noncritical branch.
