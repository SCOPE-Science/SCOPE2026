# A sharp three-translate test for directional convexity and an exact weighted hole functional

## Finding
For an arbitrary bounded measurable subset \(E\subset\mathbb R^d\), \(d\ge2\), and a fixed direction \(v\), the discrepancy between the actual three-translate union volume and a prediction involving only adjacent covariogram values is a nonnegative **hole detector**. Its integral over two translation distances is an exact, finite weighted measure of holes in directional fibers. The resulting directional-convexity criterion holds for arbitrary measurable bodies, without any boundary regularity, and gives a dimension-independent **sharp interquantile stability inequality**.

For \(a,b>0\), write
\[
 g_v(s)=|E\cap(E+sv)|,\qquad
 U_v(a,b)=|E\cup(E+av)\cup(E+(a+b)v)|,
\]
\[
 \delta_v(a,b)=3|E|-g_v(a)-g_v(b)-U_v(a,b).
\]
Then \(\delta_v(a,b)\ge0\) for every \(a,b>0\). Put \(E_y=\{x\in\mathbb R:y+xv\in E\}\) for \(y\in v^\perp\), and let
\[
 L_y(x)=|E_y\cap(-\infty,x)|,\qquad R_y(x)=|E_y\cap(x,\infty)|.
\]
The exact identity is
\[
 \boxed{\mathcal H_v(E):=\int_0^\infty\!\int_0^\infty\delta_v(a,b)\,da\,db
 =\int_{v^\perp}\int_{\mathbb R\setminus E_y} L_y(x)R_y(x)\,dx\,dy.}
\]
In particular, \(\mathcal H_v(E)=0\) if and only if for almost every \(y\), the fiber \(E_y\) is an interval, possibly empty, up to one-dimensional null sets. In that case, for every \(m\ge1\) and every \(t_0<t_1<\cdots<t_m\),
\[
\boxed{\left|\bigcup_{j=0}^m(E+t_jv)\right|=|E|+\sum_{j=1}^m\bigl(|E|-g_v(t_j-t_{j-1})\bigr).}
\]
Conversely, the displayed finite-translate identity for **three** translates at all positive consecutive gaps already forces the interval-fiber property. The criterion even follows if it is checked only for all pairs of positive rational gaps.

For any fixed \(0<\alpha<1/2\), let \(m_y=|E_y|\), and, for \(m_y>0\), let \(q_p(y)=\inf\{x:|E_y\cap(-\infty,x]|\ge p m_y\}\) for \(p=\alpha,1-\alpha\). Fibers of mass zero contribute zero. Then
\[
\boxed{\mathcal H_v(E)\ge\alpha(1-\alpha)\int_{v^\perp}m_y^2\,|[q_\alpha(y),q_{1-\alpha}(y)]\setminus E_y|\,dy.}
\]
The constant \(\alpha(1-\alpha)\) cannot be increased, for any \(d\ge2\) or \(\alpha\) in the stated range.

## Assumptions and scope
Lebesgue measure in the ambient dimension is denoted by \(|\cdot|\); directional fiber lengths use one-dimensional Lebesgue measure. Assume \(E\) is bounded and Lebesgue measurable, \(d\ge2\), and \(|v|=1\). Fibers and their quantiles are defined for almost every \(y\). Boundedness ensures all displayed integrals are finite (up to changes of \(E\) on null sets). All equalities and the zero-defect characterization are modulo Lebesgue null sets. The result does not assert that one direction of interval fibers makes \(E\) globally convex.

## Proof
**Three-translate defect.** Three-set inclusion–exclusion gives
\[
U_v(a,b)=3|E|-g_v(a)-g_v(b)-g_v(a+b)+h_v(a,b),
\]
where \(h_v(a,b)=|E\cap(E+av)\cap(E+(a+b)v)|\). Therefore
\[
\delta_v(a,b)=g_v(a+b)-h_v(a,b)
=\int_{\mathbb R^d}1_E(z)1_E(z-(a+b)v)[1-1_E(z-av)]\,dz\ge0.
\]
The integrand counts an occupied pair with a missing point strictly between its endpoints, at the two specified offsets.

**Exact integrated identity.** Decompose \(z=y+rv\), with \(y\in v^\perp\), and set \(\ell=r-a-b\), \(x=r-a\). The map \((r,a,b)\mapsto(\ell,x,r)\) has Jacobian of absolute value \(1\); its positive-gap region corresponds exactly to \(\ell<x<r\). By Tonelli,
\[
\begin{aligned}
\mathcal H_v(E)&=\int_{v^\perp}\int_{\ell<x<r}
1_{E_y}(\ell)[1-1_{E_y}(x)]1_{E_y}(r)\,d\ell\,dx\,dr\,dy\\
&=\int_{v^\perp}\int_{\mathbb R\setminus E_y}L_y(x)R_y(x)\,dx\,dy.
\end{aligned}
\]
Finiteness follows since \(E\) lies inside some ball of radius \(R\): relevant triples have all three coordinates within its directional span, of length at most \(2R\), and \(\mathcal H_v(E)\) is bounded by a constant times \(|E|R^2\).

**Vanishing and nearest-neighbor formula.** If almost every \(E_y\) is an interval modulo null sets, every integrand in the hole formula vanishes. Conversely, for any positive-mass fiber \(S=E_y\) that is not an interval modulo null sets, the set \((\operatorname{ess\,inf} S,\operatorname{ess\,sup} S)\setminus S\) has positive measure; at almost every point of this set, \(L_y,R_y>0\). Its hole integral is strictly positive. Thus \(\mathcal H_v(E)=0\) forces intervals for almost every fiber.

For a single interval of length \(L\), the union of translates at increasing sites has length \(L+\sum_{j=1}^m\min\{L,t_j-t_{j-1}\}\): each new interval extends beyond the preceding rightmost endpoint by the smaller of its length and the adjacent gap. The pairwise overlap of the interval with a displacement of size \(s\ge0\) has length \((L-s)_+\), so \(\min(L,s)=L-(L-s)_+\). Integrate the fiber identity over \(v^\perp\) to obtain the claimed union formula. In the opposite direction, applying it with three sites \(0,a,a+b\) says exactly \(\delta_v(a,b)=0\). Vanishing for all such \(a,b\) implies \(\mathcal H_v(E)=0\). Furthermore, since \(s\mapsto1_{E+sv}\) is continuous in \(L^1\), both the covariogram and three-set intersection volumes are jointly continuous in \((a,b)\); hence rational pairs suffice.

**Sharp quantitative estimate.** For a positive-mass fiber with cumulative length \(L_y(x)\), we have for almost every \(x\in[q_\alpha(y),q_{1-\alpha}(y)]\),
\[
\alpha m_y\le L_y(x)\le(1-\alpha)m_y,\quad
L_y(x)R_y(x)=L_y(x)[m_y-L_y(x)]\ge\alpha(1-\alpha)m_y^2.
\]
Integrate over missing points in the interquantile interval and then over \(y\).
For sharpness, take the one-dimensional fiber
\[
S=[0,\alpha m]\cup[\alpha m+h,m+h],\qquad m,h>0.
\]
Its single gap has length \(h\), with exactly \(\alpha m\) occupied length to the left and \((1-\alpha)m\) to the right. Thus its hole functional equals \(\alpha(1-\alpha)m^2h\), and its interquantile gap also has length \(h\). Cartesian multiplication by an arbitrary bounded measurable positive-measure set in \(v^\perp\) gives equality in every dimension, showing sharpness.

## Verification
The proof is analytic and holds in every dimension. The standalone standard-library program `verify.py` checks the inclusion–exclusion defect, interval-translate union identity, exact one-dimensional gap formula, the discrete triple-count version of Tonelli, and sharpness examples with rational data. These finite checks independently exercise the normalization and edge cases; they are not used as a proof of the infinite statements. Run `python3 verify.py` in the extracted package directory.

## Relationship to prior work
Shelley and Tartakovsky, *Union of Translates of a Convex Body* (2026; arXiv:2610.25841), examine sparse inclusion–exclusion formulae over Voronoi nerves for **general-position translates of strictly convex bodies**. Their article does not state the all-measurable-set collinear characterization or the integrated quantitative gap inequality. Their assumptions in fact exclude collinear general-position sites in the central combinatorial setting.

Rataj, *On set covariance and three-point test sets* (2004), studies three-point intersection information, its determination of compact sets, and derivatives tied to curvature and normal measures. The basic three-point intersection itself is therefore **not** presented as a new observable. The present result uses a restricted collinear defect, integrates it to isolate and quantify missing mass between endpoints, and gives the sharp interquantile coefficient for arbitrary measurable fibers. Benassi, Bianchi and D'Ercole (2010) investigate covariograms of nonconvex sets and geometric reconstruction, not this directional defect inequality.

## Limitations
A one-direction criterion certifies only essential convexity of almost every fiber parallel to \(v\), not full convexity of \(E\). The inequality measures holes in the central interquantile bands weighted by squared fiber masses; it gives no uniform unweighted bound on arbitrarily thin fibers, and it does not control missing end regions. Sharpness is within the stated fiber-weighted scale. Historical priority remains uncertain, especially for older mathematical morphology identities about three-point probes; the searched literature does not establish priority. Independent mathematical validation has not been performed.

## References
1. Alec Shelley and Daniel Tartakovsky, *Union of Translates of a Convex Body* (2026), arXiv:2610.25841, first submitted 2026-10-19. https://arxiv.org/abs/2610.25841
2. Jan Rataj, *On set covariance and three-point test sets*, Czechoslovak Mathematical Journal 54 (2004), 205–214. https://dml.cz/handle/10338.dmlcz/127877
3. Carlo Benassi, Gabriele Bianchi and Giuliana D'Ercole, *Covariogram of non-convex sets*, Mathematika 56 (2010), 267–284. https://arxiv.org/abs/1003.4122
