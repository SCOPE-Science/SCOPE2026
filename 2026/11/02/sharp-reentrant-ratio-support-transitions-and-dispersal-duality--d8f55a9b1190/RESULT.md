# Sharp reentrant ratio-support transitions in two-habitat stochastic growth

## Finding

Consider positive populations governed by \(x(t+1)=DM(t)x(t)\) in two labeled habitats, where
\[
D=\begin{pmatrix}1-q&qs\\qs&1-q\end{pmatrix}
\]
and \(M(t)\) is independently and equally likely to be either \(\operatorname{diag}(m_+,m_-)\) or \(\operatorname{diag}(m_-,m_+)\). Assume \(0<m_-<m_+\), \(0<q<1\), and \(0<s\le1\). Set \(a=m_+/m_->1\), \(\theta=qs/(1-q)\), \(\tau=\min(\theta,1/\theta)\), and
\[
Q_-=\frac{a}{a+s(a^2+a+1)},\qquad Q_0=\frac{1}{1+s},\qquad Q_+=\frac{a^2+a+1}{a^2+a+1+as}.
\]
The ratio \(r=x_2/x_1\) has a unique stationary law \(\nu_q\), the weak limit from any positive starting ratio. The support of \(\nu_q\) is:

- a nondegenerate closed interval for \(0<q\le Q_-\) or \(Q_+\le q<1\);
- a Cantor set for \(Q_-<q<Q_0\) or \(Q_0<q<Q_+\);
- the known singleton \(\{1\}\) when \(q=Q_0\).

In all regimes the endpoints are \(1/R,R\), where
\[
R=\frac{a-1+\sqrt{(a-1)^2+4a\tau^2}}{2a\tau}.
\]
In the separated regime the first gap is \((X,1/X)\) for \(X=(R/a+\tau)/(1+\tau R/a)<1\). At either nondegenerate topology transition \(X=1\). Here a Cantor set is a nonempty compact, perfect and totally disconnected set. The contribution is the exact support transition, with its critical parameters, endpoints and gap. Neither the fact that the ratio is a contractive Möbius system nor the reciprocal stationary-law reduction below is claimed as a new result.

## Proof

### Contraction and a prior-law reduction

Morita and Yoshimura's ratio recursion gives two maps with equal probabilities in the specified anticorrelated submodel:
\[
F_{\theta,\epsilon}(r)=\frac{a^\epsilon r+\theta}{1+\theta a^\epsilon r},\qquad\epsilon\in\{-1,1\}.
\]
In logarithmic coordinates they are \(u\mapsto H_\delta(u+\epsilon\log a)\), with \(\delta=(1-\theta)/(1+\theta)\) and \(H_\delta(z)=2\operatorname{artanh}(\delta\tanh(z/2))\). The maps have bounded images and a common Lipschitz constant \(|\delta|<1\), since
\[
|H_\delta'(z)|=|\delta|\frac{1-\tanh^2(z/2)}{1-\delta^2\tanh^2(z/2)}\le|\delta|.
\]
After one step all orbits lie in a compact interval. Coupling with common signs gives uniqueness and weak convergence of the stationary law. Because both branch probabilities are positive, its compact support is invariant under the union-of-images map; the latter is contractive in Hausdorff distance and has a unique nonempty compact fixed set.

Write \(I(r)=1/r\). Directly, \(I F_{\theta,\epsilon}=F_{\theta,-\epsilon} I\), so the uniqueness and equal weights give the reciprocal symmetry described by Morita and Yoshimura. Also \(F_{1/\theta,\epsilon}=I F_{\theta,\epsilon}\). Thus the symmetric stationary law for one parameter is invariant for the reciprocal parameter as well. In terms of \(q\), the paired parameter is \((1-q)/(1-q+s^2q)\). This is a direct consequence of the prior recursion and symmetry, used here only to reduce the support calculation to \(\theta=\tau\le1\). At \(\tau=1\) both maps are constant at one, giving the previously known singleton.

### Endpoints and the contact equation

Let \(0<\tau<1\). The maps are strictly increasing, and the support is symmetric under inversion. If \(R\) is its maximum then invariance gives \(R=F_{\tau,+}(R)\), since that branch is pointwise larger than the other one. This yields \(a\tau R^2+(1-a)R-\tau=0\). The polynomial has exactly one positive root, the stated \(R\); its value at one is \((a-1)(\tau-1)<0\), so \(R>1\). The minimum is \(1/R\).

On the hull \([1/R,R]\), the images are \([1/R,X]\) and \([1/X,R]\), using monotonicity and reciprocal symmetry. They touch or overlap precisely when \(X\ge1\). The map \(z\mapsto(z+\tau)/(1+\tau z)\) is increasing and fixes one, so this is equivalent to \(R\ge a\). At \(R=a\) the polynomial equals \((a-1)[\tau(a^2+a+1)-a]\); since it changes sign from negative to positive at its unique positive root, \(R\ge a\) holds exactly when \(\tau\le a/(a^2+a+1)\).

When the images touch or overlap, their union is the hull; uniqueness of the compact invariant set then gives interval support. Otherwise the first images are strictly disjoint and leave the stated central gap. All successive image intervals are disjoint within each generation by injectivity, and their logarithmic diameters shrink geometrically. Each infinite binary address therefore determines exactly one support point, and distinct addresses determine distinct points. The continuous address map is a homeomorphism by compactness, proving the Cantor case. Finally, \(\theta=qs/(1-q)\) increases strictly with \(q\), and the two equations \(\theta=a/(a^2+a+1)\) and \(\theta=(a^2+a+1)/a\) yield \(Q_-\) and \(Q_+\). The equation \(\theta=1\) gives \(Q_0\), strictly between them.

## Checks and scope

For \(a=2,s=1\) the transition values are \(2/9,1/2,7/9\). At \(q=1/6\) the computed endpoint is \((5+\sqrt{33})/4>2\), giving overlap. At \(q=1/3\) it is \((1+\sqrt{3})/2<2\), giving separation. These are finite examples; the proof uses the exact contact equation for all admissible parameters. The accompanying `checker.py` checks map identities, threshold equations and endpoint orderings. The theorem concerns topological support, not absolute abundance or long-run growth, densities in the interval regime, or dimension in the Cantor regime. It does not treat nonfair, temporally dependent or non-antiphase states, or \(q=0,1\).

## Prior work and distinct contribution

- S. Morita and J. Yoshimura, *Analytical Solution of Metapopulation Dynamics in Stochastic Environment*, Phys. Rev. E **86**, 045102 (2012), [arXiv:1207.4618](https://arxiv.org/abs/1207.4618), pp. 3–4. The model, Möbius recursion, reciprocal symmetry and singleton criterion are prior work. The reciprocal-parameter equality of stationary laws follows from the known recursion and symmetry; it is not counted as a separate result here.
- M. Barnsley and A. Vince, *Developments in fractal geometry*, Bull. Math. Sci. **3**, 299–348 (2013), [DOI:10.1007/s13373-013-0041-3](https://doi.org/10.1007/s13373-013-0041-3), pp. 319–320. The separation and coding tools are standard. The specific endpoint equation and ecological contact thresholds are the distinct calculation; the general attractor theorem does not state them.
