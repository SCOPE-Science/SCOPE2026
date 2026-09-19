# Odd-power Weingarten surfaces force nonzero umbilics in every positive-curvature component

## Statement

Let \(p\ge 3\) be an odd integer, let \(c\in\mathbb R\), and let
\[
X:M\longrightarrow \mathbb R^3
\]
be a \(C^3\) immersion of a nonempty compact smooth surface without boundary. Suppose that at every point the unordered principal curvatures satisfy
\[
(\kappa_1-c\kappa_2^p)(\kappa_2-c\kappa_1^p)=0.
\tag{1}
\]
Then necessarily \(c>0\), the Gaussian curvature is nonnegative, and
\[
K=0\quad\Longleftrightarrow\quad A=0.
\tag{2}
\]
Every connected component of \(M\) contains a point where \(K>0\).

More strongly, if \(U\) is any connected component of
\[
\Omega:=\{x\in M:K(x)>0\},
\]
then \(U\) contains a nonzero umbilic. With the positive normal on \(U\), every such forced umbilic has
\[
\boxed{\kappa_1=\kappa_2=c^{-1/(p-1)}.}
\tag{3}
\]
Consequently, the number of positive-curvature components is a lower bound for the number of nonzero umbilic points.

For \(p=3\), the componentwise nonzero-umbilic assertion is Proposition 4.3 of Cheng's recent cubic paper. The new part is that the same conclusion holds for every higher odd exponent \(p=5,7,9,\ldots\) at the same \(C^3\) regularity. The proof also identifies the cubic case as the endpoint of the cutoff estimate: the higher powers carry an additional factor \(\delta^{p-3}\).

## Proof

### 1. Positivity and normalization

Fix a connected component of \(M\) and a point \(a\in\mathbb R^3\). At a maximum point of \(|X-a|^2/2\), write \(R=|X-a|>0\) and choose the local unit normal
\[
N=\frac{a-X}{R}.
\]
The second derivative test gives
\[
0\ge \operatorname{Hess}\frac{|X-a|^2}{2}(V,V)
=|V|^2-Rh(V,V),
\]
so \(A\ge R^{-1}\operatorname{Id}\) there. Both principal curvatures are positive. Equation (1) therefore forces \(c>0\).

At an arbitrary point, one of the two factors in (1) vanishes. If, for example, \(\kappa_1=c\kappa_2^p\), then
\[
K=\kappa_1\kappa_2=c\kappa_2^{p+1}\ge0,
\]
because \(p+1\) is even. The other branch is identical. Moreover \(K=0\) forces both principal curvatures to vanish, proving (2). The farthest-point argument also proves that each connected component has a point with \(K>0\).

Scale the immersion by
\[
\widetilde X=c^{-1/(p-1)}X.
\]
If \(\widetilde\kappa_i\) are the new principal curvatures, then (1) becomes the normalized relation with coefficient one. It is therefore enough to prove the theorem for \(c=1\), and rescale at the end.

On \(\Omega\), the shape operator is positive definite for the unique positive normal. There is a unique positive \(C^1\) function \(t\) such that
\[
\operatorname{spec}A=\{t,t^p\},\qquad
K=t^{p+1},\qquad
\operatorname{tr}A=t+t^p.
\tag{4}
\]
The uniqueness follows because \(s\mapsto s+s^p\) is strictly increasing on \((0,\infty)\). In particular,
\[
t=1\quad\Longleftrightarrow\quad A=\operatorname{Id},
\tag{5}
\]
so \(t=1\) is exactly the nonzero-umbilic condition in the normalized geometry.

Let \(\mathbf H\) be the mean-curvature vector and define \(\tau:M\to[0,\infty)\) by
\[
\tau+\tau^p=2|\mathbf H|.
\tag{6}
\]
Then \(\tau\) is continuous, equals \(t\) on \(\Omega\), and vanishes exactly on \(M\setminus\Omega\). Since \(X\) is \(C^3\), \(\mathbf H\) is \(C^1\), and on \(\Omega\)
\[
|\nabla t|\le L:=2\sup_M|D\mathbf H|<\infty.
\tag{7}
\]

### 2. Principal-frame structure equations

Let \(U\) be a connected component of \(\Omega\), and suppose for contradiction that \(t\ne1\) throughout \(U\). The eigenvalues are then distinct. Choose a positively oriented local principal frame \(e_1,e_2\) with
\[
Ae_1=t e_1,\qquad Ae_2=t^p e_2.
\]
Write
\[
a=e_1(t),\qquad b=e_2(t),\qquad D=1-t^{p-1},
\]
and let \(\omega\) be the connection form, \(\nabla e_1=\omega e_2\). Codazzi gives
\[
\boxed{
\omega(e_1)=\frac{b}{tD},\qquad
\omega(e_2)=\frac{p t^{p-2}a}{D}.
}
\tag{8}
\]
Hence
\[
\boxed{
dt\wedge\omega
=\frac{p t^{p-2}a^2-b^2/t}{1-t^{p-1}}\,d\mu.
}
\tag{9}
\]
For \(p=3\), these are precisely Cheng's cubic formulas.

Two oriented principal frames with the prescribed eigenvalue order differ on overlaps only by simultaneous sign reversal. This leaves \(\omega\) unchanged, so \(\omega\) is a globally defined continuous one-form on \(U\). As in the cubic argument, the weak Gauss equation is
\[
\boxed{d\omega=-K\,d\mu}
\tag{10}
\]
in the sense of distributions. This requires only the \(C^3\) immersion regularity: locally the principal connection is a \(C^1\) reference connection plus the differential of a \(C^1\) angle.

Every point of \(\overline U\setminus U\) lies in \(\{\tau=0\}\). Indeed, if such a point had positive Gaussian curvature, a connected coordinate neighborhood inside \(\Omega\) would meet \(U\) and belong to the same component. Since \(U\) is connected and avoids \(t=1\), either
\[
t>1\quad\text{everywhere on }U,
\qquad\text{or}\qquad
0<t<1\quad\text{everywhere on }U.
\tag{11}
\]

### 3. The branch \(t>1\)

If \(t>1\) on \(U\), continuity of \(\tau\) excludes any boundary point with \(\tau=0\). Thus \(U\) is closed in the compact surface and is itself compact without boundary. Integrating (10) gives
\[
0=\int_U d\omega=-\int_U K\,d\mu,
\]
a contradiction because \(K>0\) on the nonempty open set \(U\).

### 4. The branch \(0<t<1\): the cutoff estimate

Now assume \(0<t<1\) on \(U\). Compactness of \(\overline U\) and the boundary behavior imply
\[
t\le b_0<1
\]
on \(U\); otherwise a limit point with \(\tau=1\) would lie in \(U\). Put
\[
d_0=1-b_0^{p-1}>0.
\]
Choose a smooth nondecreasing cutoff \(\chi:[0,\infty)\to[0,1]\) with \(\chi=0\) on \([0,1]\), \(\chi=1\) on \([2,\infty)\). For \(\delta>0\), the one-form \(\chi(t/\delta)\omega\) has compact support in \(U\). Applying (10), the product rule, and (9) gives
\[
I_\delta:=\int_U\chi(t/\delta)K\,d\mu
=
\int_U\frac{\chi'(t/\delta)}{\delta}
\frac{p t^{p-2}a^2-b^2/t}{1-t^{p-1}}\,d\mu.
\tag{12}
\]
Since \(I_\delta\ge0\), discard the negative square. On the support of \(\chi'(t/\delta)\) one has \(\delta<t<2\delta\), while \(|a|\le|\nabla t|\le L\). Therefore
\[
0\le I_\delta
\le
\frac{p2^{p-2}\|\chi'\|_\infty L^2}{d_0}
\,\delta^{p-3}\,
\operatorname{Area}\{x\in U:\delta<t(x)<2\delta\}.
\tag{13}
\]
For \(p=3\), the power of \(\delta\) is zero and the boundary-layer area tends to zero by dominated convergence. For every \(p>3\), there is in addition the factor \(\delta^{p-3}\to0\). Thus in all odd cases \(p\ge3\),
\[
I_\delta\longrightarrow0.
\tag{14}
\]
On the other hand, \(\chi(t/\delta)\to1\) pointwise on \(U\), and \(0\le\chi K\le K\). Dominated convergence gives
\[
I_\delta\longrightarrow\int_UK\,d\mu>0,
\tag{15}
\]
a contradiction.

Thus every positive-curvature component contains a point with \(t=1\). Undoing the scaling gives (3).

## Why the exponent three is the cutoff endpoint

The principal-frame identity (9) is valid for all odd \(p\ge3\). The only potentially positive term after cutoff is proportional to
\[
\frac1\delta t^{p-2}|\nabla t|^2.
\]
On the transition layer \(t\asymp\delta\), this is \(O(\delta^{p-3})\). Hence the cubic relation is exactly the scale-invariant endpoint of this argument; every higher odd monomial has strictly better decay. This explains why Cheng's cubic componentwise-umbilic lemma extends without any extra regularity to all higher odd powers even though the later local and global classification steps in the cubic paper are genuinely cubic.

## Context and relation to known results

Cheng proves the \(p=3\) statement as the starting point for the global classification of compact cubic Weingarten surfaces, eventually obtaining ellipsoids of revolution under \(C^4\) regularity. The theorem above only extends the preceding \(C^3\) nonzero-umbilic mechanism; it does **not** claim an analogous classification for \(p\ge5\).

The higher-power regime is nonvacuous. Kühnel and Steller construct, for every \(\alpha>1\) and \(c>0\), one-parameter families of closed convex rotational \(C^2\) surfaces satisfying \(\kappa=c\lambda^\alpha\); they are analytic exactly when \(\alpha\) is an odd integer. In particular \(\alpha=5,7,9,\ldots\) gives analytic generalized ellipsoid families, whereas \(\alpha=3\) gives the classical ellipsoids of revolution. Those constructions establish examples but do not provide the arbitrary-immersion, per-positive-curvature-component forcing theorem above.

Classical Hopf--Chern--Hartman--Wintner sphere theorems concern regular or elliptic Weingarten relations under additional hypotheses. The unordered monomial relation here has a crossing curvature diagram at its nonzero umbilic and admits the nonround generalized Hopf examples just mentioned, so those sphere-rigidity results do not subsume the present statement.

## Limitations

- The result is an umbilic-existence theorem, not a classification of compact odd-power Weingarten surfaces for \(p\ge5\).
- Oddness of \(p\) is used to obtain \(K\ge0\) globally from the unordered monomial relation. No analogous assertion is made here for even powers.
- The proof requires a \(C^3\) immersion so that the shape operator is \(C^1\), the mean-curvature vector has the needed derivative bound, and the weak connection-form calculation is available.
- The new contribution is the extension from the known cubic case to \(p=5,7,9,\ldots\); the farthest-point argument and the weak Gauss-equation mechanism are adapted from the cubic setting.
- No lower bound on the number of positive-curvature components is asserted, so the theorem does not by itself give a universal numerical lower bound stronger than existence on each connected component of the surface.

## References

1. H. Cheng, *Umbilic slopes and cubic Weingarten surfaces*, arXiv:2609.19188 (2026). https://arxiv.org/abs/2609.19188
2. W. Kühnel and M. Steller, *On closed Weingarten surfaces*, Monatsh. Math. 146 (2005), 113--126. https://doi.org/10.1007/s00605-005-0313-4
3. P. Hartman and A. Wintner, *Umbilical points and W-surfaces*, Amer. J. Math. 76 (1954), 502--508. https://doi.org/10.2307/2372698
4. K. Voss, *Über geschlossene Weingartensche Flächen*, Math. Ann. 138 (1959), 42--54.
