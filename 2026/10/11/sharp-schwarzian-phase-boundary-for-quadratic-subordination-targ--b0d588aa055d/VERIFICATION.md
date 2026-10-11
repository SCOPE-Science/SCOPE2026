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

The verification applies to normalized maps whose logarithmic derivative is
\[
\frac{f''}{f'}=v+czv^2,
\]
where \(v\) maps the disk into the closed unit disk. Schwarz--Pick bounds its derivative by \((1-|v|^2)/(1-|z|^2)\).

For \(0\le c\le1/2\), the real quadratic majorant \(F_+(c,r,s)\) is convex in \(c\). The independently expanded endpoint defects are
\[
1-F_+(0,r,s)=r^2+us^2(1-u/2)
\]
and
\[
1-F_+(1/2,r,s)=r^2(1-u/4)+u(s-r/2)^2+rus^3((1+r^2)/2-rus/8).
\]
All factors have proved signs for \(0\le r,s\le1\), \(u=1-r^2\).

For \(c=-d\), \(0\le d\le(\sqrt3-1)/2\), symbolic expansion of the *negative-parameter majorant* gives
\[
\begin{aligned}
1-F_-={}&(r-dus)^2+us^2(1/2-d-d^2)\\
&+ur^2s^2(d^2+d+1/2)\\
&+drus^3(1+r^2-drus/2).
\end{aligned}
\]
Every displayed term is nonnegative, with equality only at \(r=s=0\). The normalized Schwarzian extremizer is therefore uniquely determined by equality in Schwarz's lemma.

Beyond the threshold, the disk automorphism
\[
v(z)=\frac{a-z}{1-az},\qquad a=\frac{r-s}{1-rs},\qquad r=ds,
\]
attains Schwarz--Pick equality at \(z=r\), has \(v(r)=-s\), and aligns all Schwarzian terms. The exact expansion is
\[
F_-(d,ds,s)=1+(d^2+d-1/2)s^2+O_d(s^4),
\]
so sufficiently small \(s>0\) yields strict violation whenever \(d>(\sqrt3-1)/2\).

The embedded `verify.py` was executed with SymPy against its actual package path. It checks the polynomial identities, the automorphism derivative, the asymptotic coefficient, and the positive rational witness
\[
F_-(2/5,1/25,1/10)-1=2159560547/3814697265625>0.
\]
These finite symbolic checks support the algebra only; the infinite-dimensional theorem rests on the analytic argument and sign decompositions in RESULT.md.

The proof does not determine the sharp Schwarzian norm below the phase boundary or the best quasiconformal extension dilatation. Ahlfors--Weill guarantees the extension with maximal dilatation at most \(3\) in the stated phase, but the violation of its norm certificate outside the phase does not disprove such an extension.
