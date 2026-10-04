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
The finding was checked analytically from the stated definitions.

The published input used is
\[
\operatorname{Var}(T)=
\frac{(1-p)(1+ps)-2q\,s g'(s)}{p^2q^2}.
\]
The new proof independently establishes the exact feasible range of \(M=s g'(s)\) subject to \(g(s)=p\) for positive-integer \(T_0\).

Critical checks:
- \(X=s^{T_0}\) lies on the discrete geometric lattice and has mean \(p\).
- \(\phi(x)=x\log(x)/\log(s)\) is strictly concave because \(\log(s)<0\).
- The polygonal interpolation through consecutive lattice points is concave and agrees with \(T_0s^{T_0}\) on the support.
- Jensen therefore gives the adjacent-support maximum.
- The pointwise inequality \(T_0s^{T_0}\ge s^{T_0}\) gives the lower bound.
- The explicit \(\{1,N\}\) family preserves \(p\) and approaches the lower endpoint because \(Ns^N\to0\).
- Convex mixtures preserving \(p\) fill the full intermediate interval.
- The variance formula is strictly decreasing in \(M\), so its interval endpoints reverse.
- At \(p=s\), \(s^{T_0}\le s\) with equality only at \(T_0=1\), forcing the boundary law.

Finite numerical evaluations for several \(s,p\) pairs were used only as stress checks of the closed forms; they are not part of the proof.

No claim is made about higher moments, full stochastic order, non-memoryless catastrophe, or non-integer base completion times.
