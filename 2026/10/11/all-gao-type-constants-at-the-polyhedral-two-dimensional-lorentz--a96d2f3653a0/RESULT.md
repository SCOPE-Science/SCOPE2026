# All Gao-type constants at the polyhedral two-dimensional Lorentz endpoint
## Finding
Let \(0<\omega<1\), and let \(L_\omega=(\mathbb R^2,N_\omega)\) be the two-dimensional Lorentz endpoint plane
\[
N_\omega(s,t)=\max\{|s|,|t|\}+\omega\min\{|s|,|t|\}.
\]
For \(1\le p<\infty\), define the Gao-type constant
\[
c_{\mathrm{NJ}}^{(p)}(L_\omega)
=
\inf_{x,y\in S_{L_\omega}}
\frac{N_\omega(x+y)^p+N_\omega(x-y)^p}{2^p}.
\]
Then \(c_{\mathrm{NJ}}^{(1)}(L_\omega)=1\). For \(p>1\), writing \(p'=p/(p-1)\),
\[
c_{\mathrm{NJ}}^{(p)}(L_\omega)
=
\begin{cases}
\dfrac{(1+\omega)^p}
{\bigl((1+\omega)^{p'}+(1-\omega)^{p'}\bigr)^{p-1}},
&0<\omega\le\sqrt2-1,\\[3mm]
\bigl(1+\omega^{p'}\bigr)^{1-p},
&\sqrt2-1\le\omega<1.
\end{cases}
\]
The phase transition \(\omega=\sqrt2-1\) is independent of \(p\).

For \(p>1\), both branches are attained by explicit unit pairs. Put
\[
\delta=\frac{1-\omega}{1+\omega}.
\]
When \(0<\omega\le\sqrt2-1\), let
\[
\eta=\delta^{1/(p-1)},\qquad
U=\frac1{1+\delta\eta},\qquad
V=\eta U,
\]
and
\[
r=\frac{U+V}{1+\omega},\qquad
s=\frac{U-V}{1+\omega}.
\]
Then
\[
x=(r,s),\qquad y=(s,r)
\]
is extremal. When \(\sqrt2-1\le\omega<1\), let
\[
\eta=\omega^{1/(p-1)},\qquad
U=\frac1{1+\omega\eta},\qquad
V=\eta U;
\]
then
\[
x=(U,V),\qquad y=(U,-V)
\]
is extremal.

## Assumptions and scope
The scalar field is real and the dimension is exactly two. The Lorentz endpoint exponent is \(1\); equivalently,
\[
N_\omega(s,t)
=
\max\{|s|+\omega|t|,\ \omega|s|+|t|\}.
\]
The parameter satisfies \(0<\omega<1\), and the Gao exponent satisfies \(1\le p<\infty\).

The theorem does not claim the corresponding formula for Lorentz exponents strictly between \(1\) and \(2\).

## Proof
Let
\[
B_\omega=\{z:N_\omega(z)\le1\}.
\]
Its eight vertices are
\[
(\pm1,0),\quad(0,\pm1),\quad
\frac1{1+\omega}(\pm1,\pm1).
\]
The dual norm is therefore
\[
N_\omega^*(a,b)
=
\max\left\{
|a|,\ |b|,\ \frac{|a|+|b|}{1+\omega}
\right\}.
\]

The eight facet normals of \(B_\omega\), ordered cyclically, are
\[
f_0=(1,\omega),\quad
f_1=(\omega,1),\quad
f_2=(-\omega,1),\quad
f_3=(-1,\omega),
\]
and
\[
f_{j+4}=-f_j.
\]

Fix \(x,y\in S_{L_\omega}\), and put
\[
u=\frac{x+y}{2},\qquad
v=\frac{x-y}{2}.
\]
Choose active facets \(f_i(x)=1\) and \(f_j(y)=1\). Signed coordinate permutations are isometries of \(N_\omega\), so we may take \(i=0\). Then
\[
(f_0+f_j)(u)+(f_0-f_j)(v)=2.
\]
Consequently
\[
\alpha_jN_\omega(u)+\beta_jN_\omega(v)\ge1,
\]
where
\[
\alpha_j=\frac12N_\omega^*(f_0+f_j),
\qquad
\beta_j=\frac12N_\omega^*(f_0-f_j).
\]

Set
\[
\delta=\frac{1-\omega}{1+\omega},
\qquad
k=\frac12\max\left\{1+\omega,\frac2{1+\omega}\right\}.
\]
A direct evaluation of the eight dual norms gives the exhaustive table
\[
(\alpha_j,\beta_j)
=
(1,0),\ (1,\delta),\ (k,k),\ (\omega,1),
\]
\[
(0,1),\ (\delta,1),\ (k,k),\ (1,\omega).
\]

Assume first that \(p>1\), and write
\[
p'=\frac{p}{p-1}.
\]
Whenever
\[
\alpha a+\beta b\ge1,\qquad a,b\ge0,
\]
Hölder's inequality gives
\[
a^p+b^p
\ge
\left(\alpha^{p'}+\beta^{p'}\right)^{1-p}.
\]
Applying this to the table yields three potentially nontrivial lower bounds:
\[
A_p(\omega)
=
\left(1+\delta^{p'}\right)^{1-p}
=
\frac{(1+\omega)^p}
{\bigl((1+\omega)^{p'}+(1-\omega)^{p'}\bigr)^{p-1}},
\]
\[
B_p(\omega)
=
\left(1+\omega^{p'}\right)^{1-p},
\]
and
\[
C_p(\omega)
=
2^{1-p}k^{-p}.
\]

The first two switch order exactly when
\[
\delta=\omega,
\]
that is, at
\[
\omega=\sqrt2-1.
\]
It remains to show that the \(k\)-case never gives a smaller value.

If \(0<\omega\le\sqrt2-1\), then
\[
k=\frac1{1+\omega},
\qquad
\delta\ge\omega.
\]
Since \(t\mapsto t^{p'}\) is convex,
\[
2
\le
(1+\omega)^{p'}+(1-\omega)^{p'}.
\]
Equivalently,
\[
2k^{p'}\le1+\delta^{p'},
\]
which implies
\[
C_p(\omega)\ge A_p(\omega).
\]

If \(\sqrt2-1\le\omega<1\), then
\[
k=\frac{1+\omega}{2},
\qquad
\omega\ge\delta.
\]
Convexity gives
\[
2\left(\frac{1+\omega}{2}\right)^{p'}
\le
1+\omega^{p'},
\]
hence
\[
C_p(\omega)\ge B_p(\omega).
\]
Thus
\[
c_{\mathrm{NJ}}^{(p)}(L_\omega)
\ge
\min\{A_p(\omega),B_p(\omega)\},
\]
with the stated phase split.

We now attain the lower bounds.

Suppose \(0<\omega\le\sqrt2-1\). Define
\[
\eta=\delta^{1/(p-1)},\quad
U=\frac1{1+\delta\eta},\quad
V=\eta U,
\]
and
\[
r=\frac{U+V}{1+\omega},\qquad
s=\frac{U-V}{1+\omega}.
\]
Then \(r\ge s\ge0\) and
\[
r+\omega s=U+\delta V=1.
\]
Therefore
\[
x=(r,s),\qquad y=(s,r)
\]
belong to the unit sphere. Moreover
\[
N_\omega\!\left(\frac{x+y}{2}\right)=U,
\qquad
N_\omega\!\left(\frac{x-y}{2}\right)=V.
\]
Hence their Gao-type quotient equals
\[
U^p+V^p=A_p(\omega).
\]

Suppose instead that \(\sqrt2-1\le\omega<1\). Define
\[
\eta=\omega^{1/(p-1)},\quad
U=\frac1{1+\omega\eta},\quad
V=\eta U.
\]
Then \(U\ge V\ge0\) and
\[
U+\omega V=1.
\]
Thus
\[
x=(U,V),\qquad y=(U,-V)
\]
are unit vectors, while
\[
N_\omega\!\left(\frac{x+y}{2}\right)=U,
\qquad
N_\omega\!\left(\frac{x-y}{2}\right)=V.
\]
Their quotient is
\[
U^p+V^p=B_p(\omega).
\]

Finally let \(p=1\). For
\[
u=\frac{x+y}{2},\qquad v=\frac{x-y}{2},
\]
the triangle inequality gives
\[
1=N_\omega(x)=N_\omega(u+v)
\le N_\omega(u)+N_\omega(v).
\]
Thus \(c_{\mathrm{NJ}}^{(1)}\ge1\), while taking \(x=y\in S_{L_\omega}\) gives equality.

## Verification
The proof is exhaustive because every unit vector lies on at least one of the eight facets, and signed coordinate permutations move any chosen first facet to \(f_0\). The eight possible relative facet positions are all listed in the coefficient table.

No numerical search is used to prove the lower bound. The only optimization step is the sharp two-variable Hölder inequality under one linear constraint. The equality pairs realize the corresponding Hölder equality conditions exactly.

At \(p=2\), the theorem specializes to
\[
c_{\mathrm{NJ}}^{(2)}(L_\omega)
=
\begin{cases}
\dfrac{(1+\omega)^2}{2(1+\omega^2)},
&0<\omega\le\sqrt2-1,\\[2mm]
\dfrac1{1+\omega^2},
&\sqrt2-1\le\omega<1,
\end{cases}
\]
which agrees with the previously available classical Gao endpoint value.

## Relationship to prior work
Suzuki, Yamano, and Kato study exactly the two-dimensional Lorentz sequence spaces and give the endpoint norm
\[
N_\omega(s,t)=\max\{|s|,|t|\}+\omega\min\{|s|,|t|\}
\]
when the Lorentz exponent is \(1\). Their work concerns the James constant rather than the Gao-type family.

Cui and Wang computed the classical quadratic Gao parameters for two-dimensional Lorentz sequence spaces in the range where their paper states \(2\le q<\infty\). That range does not contain the polyhedral exponent \(1\).

Zuo, Huang, Huang, and Wang define the generalized Gao-type constant used here. Their 2022 paper gives an exact formula for two-dimensional Lorentz spaces when the Lorentz exponent satisfies \(2\le r<\infty\). In its conclusions it explicitly lists the Lorentz range
\[
1\le r<2
\]
among the specific spaces for which Gao-type constants were still not known.

The present theorem resolves the endpoint \(r=1\) simultaneously for every \(1\le p<\infty\). Its \(p=2\) specialization was already available separately; the new content is the complete generalized-\(p\) formula and the fact that the same phase boundary \(\omega=\sqrt2-1\) persists for every \(p>1\).

## Limitations
The theorem does not address \(1<r<2\), so the interior of the open Lorentz range identified in 2022 remains outside the claim.

A later computation under different terminology may exist outside the checked indexes. Exact-formula, endpoint, invariant-name, and phase-transition searches did not locate such a result; this is a residual bibliographic risk rather than a proof of absence.

## References
1. T. Suzuki, A. Yamano, and M. Kato, “The James Constant of 2-Dimensional Lorentz Sequence Spaces,” *Bulletin of the Kyushu Institute of Technology. Pure and Applied Mathematics* 53 (2006), 15--24, DOI 10.18997/00002048; repository issue date 2006-03-30.
2. H. Cui and F. Wang, “Gao's constants of Lorentz sequence spaces,” *Soochow Journal of Mathematics* 33 (2007), 707--717.
3. Z. Zuo, Y. Huang, H. Huang, and J. Wang, “The Gao-Type Constant of Absolute Normalized Norms on \(\mathbb R^2\),” *Mathematics* 10 (2022), 4591, DOI 10.3390/math10234591.
