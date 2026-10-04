# Exact scalar-axis Daugavet and \(\Delta\)-constants in \(\ell_p\)-sums
## Finding
Let \(1<p<\infty\), let \(Y\neq\{0\}\) be any real Banach space, and set
\[
Z=\mathbb R\oplus_p Y,
\qquad
\|(s,y)\|=\bigl(|s|^p+\|y\|^p\bigr)^{1/p}.
\]
For every \(t\in[-1,1]\), write \(z_t=(t,0)\in B_Z\). Then
\[
\boxed{\ \operatorname{dc}_Z(z_t)=1-|t|\ },
\qquad
\boxed{\ \delta c_Z(z_t)=\bigl(1-|t|^p\bigr)^{1/p}\ }.
\]
In particular, for \(0<|t|<1\),
\[
\delta c_Z(z_t)>\operatorname{dc}_Z(z_t).
\]
The second identity is independent of every geometric feature of the nonzero transverse summand \(Y\): only the exponent \(p\) and the scalar coordinate \(|t|\) enter.

## Assumptions and scope
All spaces and functionals are real. The pointwise Daugavet and Delta constants are those of Choi and Jung:
\[
\operatorname{dc}(x)=\inf_{S}\sup_{u\in S}\|x-u\|,
\]
where the infimum is over all slices \(S\) of the unit ball, and
\[
\delta c(x)=\inf_{S\ni x}\sup_{u\in S}\|x-u\|,
\]
where the infimum is restricted to slices containing \(x\).

By the scalar sign isometry it suffices to prove the formulas for \(0\le t\le1\). Put
\[
R_t=\bigl(1-t^p\bigr)^{1/p}.
\]
The hypothesis \(Y\neq\{0\}\) is essential for the Delta formula when \(0<t<1\): in the one-dimensional space \(\mathbb R\), the Delta constant is \(1-t\), while the transverse summand creates the larger value \(R_t\).

## Proof
We first compute the Daugavet constant. Every slice of a unit ball contains points whose norm is arbitrarily close to \(1\). Hence, for any slice \(S\subset B_Z\) and every \(\varepsilon>0\), one can choose \(w\in S\) with \(\|w\|>1-\varepsilon\). Therefore
\[
\sup_{w\in S}\|z_t-w\|
\ge 1-\varepsilon-t.
\]
Letting \(\varepsilon\downarrow0\) gives
\[
\operatorname{dc}_Z(z_t)\ge1-t.
\]
For the reverse inequality, for \(\eta>0\) consider the slice
\[
S_\eta=\{(s,y)\in B_Z:s>1-\eta\}.
\]
For \((s,y)\in S_\eta\),
\[
\|(s,y)-z_t\|^p
=|s-t|^p+\|y\|^p
\le |s-t|^p+1-|s|^p.
\]
As \(\eta\downarrow0\), the right-hand side converges uniformly for \(s\in(1-\eta,1]\) to \((1-t)^p\). Consequently
\[
\operatorname{dc}_Z(z_t)\le1-t,
\]
which proves the first identity.

We now prove the Delta formula. Fix an arbitrary slice \(S(\Phi,\alpha)\) of \(B_Z\) containing \(z_t\). The dual is
\[
Z^*=\mathbb R\oplus_q Y^*,
\qquad \frac1p+\frac1q=1,
\]
so write \(\Phi=(a,y^*)\in S_{Z^*}\). Because \(Y\neq\{0\}\), choose \(u\in S_Y\) with \(y^*(u)\ge0\); if \(y^*=0\), any \(u\in S_Y\) works. Define
\[
w=(t,R_tu).
\]
Then
\[
\|w\|^p=t^p+R_t^p=1,
\]
and
\[
\Phi(w)=at+R_ty^*(u)\ge at=\Phi(z_t)>1-\alpha.
\]
Thus \(w\in S(\Phi,\alpha)\), while
\[
\|w-z_t\|=R_t.
\]
Since the slice was arbitrary,
\[
\delta c_Z(z_t)\ge R_t.
\]

For the matching upper bound, first suppose \(0<t<1\). Choose \(0<\eta<t\) and consider the slice containing \(z_t\)
\[
T_\eta=\{(s,y)\in B_Z:s>t-\eta\}.
\]
For \((s,y)\in T_\eta\),
\[
\|(s,y)-z_t\|^p
\le F_t(s):=|s-t|^p+1-|s|^p.
\]
If \(s\in[t,1]\), then
\[
F_t(s)=1-s^p+(s-t)^p
\]
has derivative
\[
p\bigl((s-t)^{p-1}-s^{p-1}\bigr)<0,
\]
so \(F_t(s)\le F_t(t)=1-t^p\). If \(s\in[t-\eta,t]\), then
\[
F_t(s)
=1-s^p+(t-s)^p
\le 1-(t-\eta)^p+\eta^p.
\]
Hence
\[
\sup_{w\in T_\eta}\|w-z_t\|^p
\le 1-(t-\eta)^p+\eta^p.
\]
Letting \(\eta\downarrow0\) gives
\[
\delta c_Z(z_t)\le(1-t^p)^{1/p}=R_t.
\]

At \(t=0\), the lower-bound witness above has distance \(1\), while every point of \(B_Z\) is at distance at most \(1\) from the origin, so \(\delta c_Z(0,0)=1\). At \(t=1\), the slices \(T_\eta=\{(s,y)\in B_Z:s>1-\eta\}\) satisfy
\[
\|(s,y)-(1,0)\|^p
\le (1-s)^p+1-s^p
\le \eta^p+1-(1-\eta)^p,
\]
which tends to \(0\). Thus \(\delta c_Z(1,0)=0\). This completes the proof.

Finally, for \(0<t<1\) and \(p>1\), strict convexity of the scalar function \(r\mapsto r^p\) gives
\[
t^p+(1-t)^p<1.
\]
Therefore
\[
1-t^p>(1-t)^p,
\]
and hence
\[
(1-t^p)^{1/p}>1-t.
\]
So the two constants are strictly separated at every nontrivial interior scalar-axis point.

## Verification
The proof is analytic and works for arbitrary nonzero \(Y\). The accompanying `verify_scalar_axis_lp.py` performs an exact-rational replay for integer exponents \(2\le p\le6\). It checks the scalar optimization inequalities used in the upper bounds, the powered identity behind the transverse witness, and the strict gap at interior rational values of \(t\). The checker is a consistency test only; it is not used to replace the slice argument or the arbitrary-Banach-space reasoning.

Two limiting comparisons are useful. When \(p=2\), the Delta formula becomes
\[
\delta c_Z(z_t)=\sqrt{1-t^2},
\]
matching the Hilbert-space formula on this axis even when \(Y\) is not Hilbert. In contrast, the one-dimensional scalar space has
\[
\delta c_{\mathbb R}(t)=1-|t|,
\]
so adjoining any nonzero transverse \(p\)-summand produces an exact quantitative amplification for \(0<|t|<1\).

## Relationship to prior work
Haller, Pirk, and Veeorg study Daugavet and Delta points in absolute sums at the qualitative, unit-sphere level. Their results determine when extremal distance-two behavior can pass between summands, but they do not define or compute pointwise quantitative constants at interior scalar-axis points.

Choi and Jung introduce the pointwise Daugavet and Delta constants and develop quantitative stability estimates for absolute sums. Their Proposition 4.9 gives general lower stability for the Delta constant, Corollary 4.10 specializes this to \(\ell_1\)- and \(\ell_\infty\)-sums, and Proposition 4.11 gives an exact zero-component identity for the \(\ell_1\)-sum on the unit sphere. Their Proposition 2.11 computes the Hilbert-space Delta constant. None of those statements yields the exact formula
\[
\delta c_{\mathbb R\oplus_pY}(t,0)=(1-|t|^p)^{1/p}
\]
for arbitrary nonzero \(Y\) and \(1<p<\infty\), nor the resulting universal strict gap from the Daugavet constant at interior axis points.

Targeted semantic searches for scalar-axis Delta constants, quantitative \(p\)-sum formulas, slice-radius formulations, and direct-sum equivalents returned no matching statement. This is evidence of noncoverage, not a proof that no equivalent formulation exists outside the inspected literature.

## Limitations
The theorem is for real scalars, \(1<p<\infty\), a one-dimensional scalar first summand, and an arbitrary nonzero Banach second summand. It does not claim a formula for a general point \((x,y)\), for a higher-dimensional first summand, for complex scalars, or for \(p=\infty\). The finite checker covers only integer exponents and rational grids; the full real-exponent result rests on the analytic proof.

## References
1. R. Haller, K. Pirk, and T. Veeorg, *Daugavet- and Delta-points in absolute sums of Banach spaces*, arXiv:2001.06197, first posted 2020-01-17; Journal of Convex Analysis 28 (2021), 41--54.
2. G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647, first posted 2023-07-20; version 3 dated 2024-06-24; DOI 10.1017/prm.2024.83.
