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
At every spatial location the age-structured system has no dependence on any different location. For an initially disease-free point, \(Q=I=0\), \(S=S_0\) is an exact solution; local uniqueness proves infection-support nonexpansion.

With \(f(a)=\ell(a)\exp(-\int_0^a\ell(s)ds)\ge0\), \(\int f\le1\), and \(u=c\lambda\), the source transform is
\[
\mathcal L(c,\lambda)=\frac{\eta(1-\gamma)S_0}{q+u}\int_0^\infty e^{-ua}f(a)\,da=F(u).
\]
For \(u>0\) its derivative is strictly negative when the exit distribution has positive mass. The bound
\[
0\le F(u)\le\frac{\eta(1-\gamma)S_0}{q+u}
\]
proves that the source's speed infimum is zero, and \(\partial_\lambda\mathcal L=cF'(c\lambda)<0\) excludes positive critical-speed double roots.

The included exact-rational program checks the admissible \(\ell\equiv1\) witness, including \(F(0)=4\), \(F(1)=1\), \(F(2)=4/9\), and strict negative derivatives for several positive rational speeds. It is illustrative, not an exhaustive proof of the general result. The theorem does not assert stationary contours for everywhere-positive initial infectious data.
