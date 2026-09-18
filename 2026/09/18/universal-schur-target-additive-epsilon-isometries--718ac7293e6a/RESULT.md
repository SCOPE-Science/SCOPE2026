# A single Schur target is additively epsilon-isometrically universal for separable Banach spaces

## Result

There exists a single separable real Banach space \(Y\) with the Schur property such that the following holds.

For every nonzero separable real Banach space \(X\) and every \(\varepsilon>0\), there is a standard exact \(\varepsilon\)-isometry
\[
f_{X,\varepsilon}:X\longrightarrow Y
\]
with one-sided distortion
\[
0\le \|f_{X,\varepsilon}(x)-f_{X,\varepsilon}(y)\|-\|x-y\|\le \varepsilon
\qquad (x,y\in X).
\]
Moreover, \(f_{X,\varepsilon}\) is injective and uniformly continuous, and its inverse on its range is \(1\)-Lipschitz.

At the same time, if \(X\) does not have the Schur property, then there is no isometric embedding \(X\to Y\), even if the embedding is allowed to be nonlinear.

Thus one fixed separable Schur space is additively \(\varepsilon\)-isometrically universal for all separable Banach spaces at every positive additive scale, while it excludes exact isometric copies of every separable non-Schur Banach space.

A metric version also holds: every pointed separable metric space admits, for every \(\varepsilon>0\), a basepoint-preserving embedding into the same \(Y\) whose distance excess lies in \([0,\varepsilon]\). Exact attainment of the error \(\varepsilon\) is automatic for every nonzero Banach domain.

## Construction

Let
\[
U=C([0,1],\mathbb R)
\]
with the supremum norm and define
\[
\omega(t)=\max\{t,\sqrt t\},\qquad t\ge0.
\]
Equip \(U\) with the metric
\[
\rho(u,v)=\omega(\|u-v\|_\infty).
\]
The function \(\omega\) is a nontrivial gauge in the sense used by Kalton: it is increasing, continuous and subadditive, and
\[
\lim_{t\downarrow0}\frac{\omega(t)}t=\infty.
\]
Let
\[
Y=\mathcal F(U,\rho)
\]
be the Lipschitz-free Banach space over the pointed metric space \((U,\rho,0)\).

Kalton's theorem says that \(\mathcal F(M,\omega\circ d)\) has the Schur property for every metric space \(M\) and every nontrivial gauge \(\omega\). Hence \(Y\) has the Schur property. Since \(U\) is separable and \(\rho\) induces the same topology as the norm metric, \(Y\) is separable.

Now let \(X\) be a separable real Banach space. By the Banach--Mazur theorem there is a linear isometry
\[
J_X:X\longrightarrow U.
\]
For \(\varepsilon>0\), put \(c=4\varepsilon\), and write
\[
\delta_\rho:U\longrightarrow \mathcal F(U,\rho)
\]
for the canonical metric embedding. Define
\[
f_{X,\varepsilon}(x)
=
c\,\delta_\rho\!\left(\frac{J_Xx}{c}\right).
\]

## Exact distance formula

For \(x,y\in X\), set \(r=\|x-y\|\). By the defining property of a Lipschitz-free space,
\[
\begin{aligned}
\|f_{X,\varepsilon}(x)-f_{X,\varepsilon}(y)\|
&=
c\,\rho\!\left(\frac{J_Xx}{c},\frac{J_Xy}{c}\right)\\
&=
c\,\omega(r/c)\\
&=
\max\{r,\,2\sqrt{\varepsilon r}\}.
\end{aligned}
\]
Therefore
\[
\|f_{X,\varepsilon}(x)-f_{X,\varepsilon}(y)\|-\|x-y\|
=
\max\{0,2\sqrt{\varepsilon r}-r\}.
\]
The elementary identity
\[
2\sqrt{\varepsilon r}-r
=
\varepsilon-(\sqrt r-\sqrt\varepsilon)^2
\]
gives
\[
0\le
\|f_{X,\varepsilon}(x)-f_{X,\varepsilon}(y)\|-\|x-y\|
\le \varepsilon.
\]
If \(X\ne\{0\}\), choose \(x,y\) with \(\|x-y\|=\varepsilon\). Then the upper bound is attained, so the map is an exact \(\varepsilon\)-isometry.

The same formula immediately gives
\[
\|x-y\|
\le
\|f_{X,\varepsilon}(x)-f_{X,\varepsilon}(y)\|,
\]
so \(f_{X,\varepsilon}\) is injective and its inverse on the range is \(1\)-Lipschitz. Also
\[
\|f_{X,\varepsilon}(x)-f_{X,\varepsilon}(y)\|
\le
\max\{\|x-y\|,\,2\sqrt{\varepsilon\|x-y\|}\},
\]
which tends to zero with \(\|x-y\|\); hence \(f_{X,\varepsilon}\) is uniformly continuous.

## Exact-isometry obstruction

Suppose that a separable Banach space \(X\) admits an isometric embedding
\[
g:X\longrightarrow Y,
\]
with no linearity assumption on \(g\). The isometric linearization theorem of Godefroy and Kalton states that if a separable Banach space embeds isometrically into a Banach space, then the target contains a linearly isometric copy of the domain. Therefore \(Y\) contains a closed linear subspace linearly isometric to \(X\).

The Schur property passes to closed subspaces. Since \(Y\) has the Schur property, \(X\) must have the Schur property. Consequently every separable non-Schur Banach space is excluded from \(Y\) as an exact metric isometric copy.

In particular, spaces such as \(c_0\), \(\ell_p\) for \(1<p<\infty\), and infinite-dimensional Hilbert space admit exact standard \(\varepsilon\)-isometries into this same fixed \(Y\) for every \(\varepsilon>0\), but no exact isometric embedding into \(Y\).

## Metric-space extension

Let \((M,d,0)\) be any pointed separable metric space. Its Lipschitz-free space \(\mathcal F(M)\) is a separable real Banach space and the canonical map
\[
\delta_M:M\to\mathcal F(M)
\]
is an isometric embedding. By Banach--Mazur there is a linear isometry
\[
J:\mathcal F(M)\to U.
\]
Thus \(h=J\circ\delta_M:M\to U\) is a basepoint-preserving metric isometry. Defining
\[
F_{M,\varepsilon}(x)
=
4\varepsilon\,
\delta_\rho\!\left(\frac{h(x)}{4\varepsilon}\right)
\]
gives, for all \(x,y\in M\),
\[
\|F_{M,\varepsilon}(x)-F_{M,\varepsilon}(y)\|
=
\max\{d(x,y),2\sqrt{\varepsilon d(x,y)}\},
\]
and therefore distance excess in \([0,\varepsilon]\).

So the fixed \(Y\) is additively \(\varepsilon\)-universal even for all separable metric spaces in the non-exact-at-every-scale sense.

## Relation to recent work

Sun and Zhang (2026) construct two fixed separable real Banach spaces
\[
X=\ell_2,\qquad Y_X=\mathcal F_\omega(\ell_2),
\]
such that for every \(\varepsilon>0\) there is a standard exact \(\varepsilon\)-isometry \(X\to Y_X\), yet no isometric embedding \(X\to Y_X\) exists, even nonlinearly. Their construction uses precisely the gauge
\(\omega(t)=\max\{t,\sqrt t\}\), Kalton's Schur theorem and the Godefroy--Kalton linearization theorem.

The present observation changes the quantifiers: the target is chosen once, independently of \(X\). Banach--Mazur universality of \(C([0,1])\) lets all separable Banach domains be placed in a common ambient metric before applying the same snowflaked free-space construction. The resulting target remains separable and Schur.

The distinction from classical universal Banach spaces is sharp. \(C([0,1])\) contains an exact linear isometric copy of every separable Banach space. The space \(Y\) above instead gives arbitrarily accurate additive embeddings of all of them while exact metric embeddings are ruled out for every non-Schur domain.

## Limitations and originality

The ingredients are classical except for the motivating 2026 construction: Banach--Mazur universality, Kalton's Schur theorem for free spaces over nontrivially gauged metrics, and Godefroy--Kalton isometric linearization. The contribution is their universal-target synthesis and its quantifier strengthening of the recent fixed-pair construction.

To the best of our knowledge, searches for universal-target formulations of additive \(\varepsilon\)-isometries, Schur targets, and snowflaked Lipschitz-free spaces did not locate this statement. Older \(\varepsilon\)-isometry stability literature uses several different notions of universality, so an equivalent formulation under different terminology remains the principal residual originality risk.

The theorem is stated over the real scalars because both the Banach--Mazur host and the cited Godefroy--Kalton formulation used here are in the real Banach-space setting. No claim is made here about an optimally analogous fixed target in every complex-linear formulation.

## References

1. Longfa Sun and Yipeng Zhang, *\(\varepsilon\)-isometries without isometric embeddings*, arXiv:2609.13937 (2026). https://arxiv.org/abs/2609.13937
2. N. J. Kalton, *Spaces of Lipschitz and Hölder functions and their applications*, Collectanea Mathematica 55 (2004), 171--217. DOI: 10.1344/CM.V55I2.4055.
3. G. Godefroy and N. J. Kalton, *Lipschitz-free Banach spaces*, Studia Mathematica 159 (2003), 121--141. DOI: 10.4064/sm159-1-6.
4. Robert H. Lohman, *An Embedding Theorem for Separable Locally Convex Spaces*, Canadian Mathematical Bulletin 14 (1971), 119--120. DOI: 10.4153/CMB-1971-023-1. The introduction records the classical Banach--Mazur theorem that every separable Banach space embeds linearly isometrically into \(C[0,1]\).
5. R. J. Aliaga, C. Petitjean and A. Procházka, *Lipschitz-free spaces and Schur properties*, Journal of Mathematical Analysis and Applications 461 (2018), 1083--1102. DOI: 10.1016/j.jmaa.2017.04.047; see its discussion of Kalton's Theorem 4.6.
