# Uniform rigid holes in the space of metrics on every discrete set

## Result

Let \(X\) be a discrete topological space with \(|X|\ge 3\). Write \(\operatorname{Met}(X)\) for the compatible metrics on \(X\), equipped with the extended supremum metric
\[
\mathcal D_X(d,e)=\sup_{x,y\in X}|d(x,y)-e(x,y)|,
\]
and let \(\mathrm R(X)\subseteq\operatorname{Met}(X)\) be the metrics whose only bijective self-isometry is the identity.

For every \(d\in\operatorname{Met}(X)\) and every \(R>0\), there exists \(e\in\operatorname{Met}(X)\) such that
\[
B_{\mathcal D_X}(e,R/24)\subseteq B_{\mathcal D_X}(d,R)\cap \mathrm R(X).
\]
If \(|X|\ge 8\) (in particular, for every infinite \(X\)), the radius \(R/24\) may be replaced by \(R/12\).

Consequently, the interior of \(\mathrm R(X)\) is dense in \(\operatorname{Met}(X)\), the nonrigid locus is nowhere dense, and \(\mathrm R(X)\) is comeager. In the usual local terminology on each finite-\(\mathcal D_X\) component, the nonrigid locus is uniformly porous, with the displayed constants.

This answers Question 6.1 of Ishiki (2026) for arbitrary-cardinality discrete spaces, and does so in a quantitatively stronger form. The cardinality point is essential: if \(|X|>\mathfrak c\), no strongly rigid metric can exist because \([X]^2\) has cardinality \(|X|>\mathfrak c\) while all metric values are real, whereas the theorem above still gives robustly generic ordinary rigidity.

## Proof

We use two elementary ingredients: a finite-spectrum rigid marker metric and lattice rounding of the target metric.

### 1. A finite-spectrum rigid marker

There is a rigid metric \(\rho\) on \(X\) whose nonzero values lie in \(\{1,3/2,2\}\), and if \(|X|\ge 8\) one may take its nonzero values in \(\{1,2\}\).

For \(|X|\ge 8\), Hedrlín and Pultr proved that every set of cardinality at least \(8\), finite or infinite, admits a symmetric relation with only the identity endomorphism. Such a relation is loopless when \(|X|>1\): a loop at \(x\) would make the constant map to \(x\) an endomorphism. Define
\[
\rho(x,y)=
\begin{cases}
0,&x=y,\\
1,&x\ne y\text{ and }(x,y)\text{ is in the relation},\\
2,&\text{otherwise}.
\end{cases}
\]
Because all nonzero distances are \(1\) or \(2\), this is a metric. Every \(\rho\)-isometry preserves the relation and hence is the identity.

For \(3\le |X|=n\le7\), enumerate \(X=\{x_1,\dots,x_n\}\) and put
\[
\rho(x_1,x_2)=3/2,\qquad
\rho(x_i,x_{i+1})=1\ (2\le i<n),
\]
with every remaining nonzero distance equal to \(2\). Again this is a metric, since every nonzero distance lies in \([1,2]\). The unique \(3/2\)-pair is preserved by every isometry; its endpoint \(x_1\) has no distance-\(1\) neighbor while \(x_2\) does, so both are fixed. The distance-\(1\) chain \(x_2,x_3,\dots,x_n\) then fixes all remaining points.

Let
\[
\sigma=\min\{|u-v|:u\ne v,\ u,v\in \rho([X]^2)\}.
\]
Thus \(\sigma=1\) when \(|X|\ge8\), while \(\sigma=1/2\) in the explicit small finite construction.

### 2. Round the target metric and insert the marker

Fix \(d\in\operatorname{Met}(X)\) and \(R>0\), and set
\[
\delta=R/2,\qquad a=R/6=\delta/3.
\]
For distinct \(x,y\), define
\[
q(x,y)=\delta\left\lceil\frac{d(x,y)}{\delta}\right\rceil,
\qquad q(x,x)=0.
\]
Then \(q\) is a metric. Indeed,
\[
\left\lceil\frac{d(x,y)}\delta\right\rceil
\le
\left\lceil\frac{d(x,z)+d(z,y)}\delta\right\rceil
\le
\left\lceil\frac{d(x,z)}\delta\right\rceil+
\left\lceil\frac{d(z,y)}\delta\right\rceil.
\]
Moreover \(0\le q(x,y)-d(x,y)<\delta\) off the diagonal, and \(q(x,y)\ge\delta\) for \(x\ne y\). Thus \(q\) is compatible with the discrete topology. This is the same basic lattice-rounding mechanism used in Ishiki's earlier work on spaces of metrics.

Now put
\[
e=q+a\rho.
\]
The sum of two metrics is a metric, and it is again compatible with the discrete topology. Since \(\rho\le2\),
\[
\mathcal D_X(d,e)<\delta+2a=\frac{5R}{6}.
\]

For an unordered pair \(p=\{x,y\}\), write
\[
e(p)=m_p\delta+a\rho(p),\qquad m_p\in\mathbb Z_{\ge1}.
\]
The residue term satisfies \(a\rho(p)\in[a,2a]=[\delta/3,2\delta/3]\). If \(\rho(p)\ne\rho(p')\), then
\[
|e(p)-e(p')|\ge a\sigma.
\]
Indeed, if \(m_p=m_{p'}\) this is the definition of \(\sigma\); if the integers differ, the distance is at least \(\delta-a=2\delta/3\ge a\sigma\).

Let \(e'\in\operatorname{Met}(X)\) satisfy
\[
\mathcal D_X(e,e')<\frac{a\sigma}{2}.
\]
If \(f\) is an \(e'\)-isometry and \(p=\{x,y\}\), then, with \(f(p)=\{f(x),f(y)\}\),
\[
|e(p)-e(f(p))|
< a\sigma.
\]
Hence \(\rho(p)=\rho(f(p))\) for every pair \(p\). Therefore \(f\) is a \(\rho\)-isometry and must be the identity. We have proved
\[
B_{\mathcal D_X}\left(e,\frac{a\sigma}{2}\right)\subseteq \mathrm R(X).
\]
Since \(a\sigma/2=R\sigma/12\), this radius is \(R/12\) for \(|X|\ge8\) and \(R/24\) for \(3\le|X|\le7\). Finally,
\[
\frac{5R}{6}+\frac{R}{12}<R,
\]
so in either case the rigid subball lies inside \(B_{\mathcal D_X}(d,R)\). This proves the theorem.

## Relation to prior work

Ishiki's 2026 paper asks whether \(\mathrm R(X)\) is dense in \(\operatorname{Met}(X)\) for every metrizable \(X\) with at least three points. It records positive results for strongly zero-dimensional spaces of cardinality at most the continuum, for compact spaces, and for totally bounded target metrics, while emphasizing that the general uniform-topology problem remains open. Ishiki's 2024 work already contains the lattice-rounding lemma used above and obtains strongly rigid approximations under the continuum-cardinality restriction.

The graph-theoretic ingredient is classical: Hedrlín and Pultr proved the existence of rigid symmetric relations on every set of cardinality at least \(8\), including every infinite cardinal. The new point here is the quantitative combination of a finite-spectrum rigid marker with metric lattice rounding: it produces an entire rigid ball inside every ball of \(\operatorname{Met}(X)\), removes all cardinality restrictions for discrete spaces, and yields the uniform hole constants above.

Targeted searches for rigid metrics on arbitrary discrete spaces, dense interior of the rigid locus, nowhere-dense nonrigid metrics, and porosity of the nonrigid locus did not locate a prior statement of this quantitative theorem.

## Limitations

The result concerns discrete underlying topology. It does not settle Ishiki's density question for general nondiscrete metrizable spaces, and it does not address the Borel-complexity question for \(\mathrm R(X)\). The constants \(1/24\) and \(1/12\) are convenient explicit constants and are not claimed optimal. For discrete spaces of cardinality at most \(\mathfrak c\), bare density and category conclusions were already accessible through prior strong-rigidity results; the new assertion there is the quantitative dense-interior/rigid-subball property. The motivating preprint is extremely recent, so unindexed parallel work remains a residual originality risk.

## References

1. Yoshito Ishiki, *Algebraically independent distances and rigid metrics*, arXiv:2609.19773 (2026). https://arxiv.org/abs/2609.19773
2. Yoshito Ishiki, *Strongly rigid metrics in spaces of metrics*, Topology Proceedings 63 (2024), 125–148; arXiv:2210.02170. https://arxiv.org/abs/2210.02170
3. Z. Hedrlín and A. Pultr, *On Rigid Undirected Graphs*, Canadian Journal of Mathematics 18 (1966), 1237–1242. https://doi.org/10.4153/CJM-1966-121-7
