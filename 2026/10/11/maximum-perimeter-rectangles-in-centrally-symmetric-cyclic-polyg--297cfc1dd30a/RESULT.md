# Maximum-perimeter rectangles in centrally symmetric cyclic polygons

## Finding

Let \(K\subset\mathbb R^2\) be a nondegenerate, centrally symmetric convex polygon with \(2m\ge4\) vertices, all on the circle of radius \(R>0\) centered at its symmetry center, which is taken to be the origin. Let \(\Theta\subset\mathbb R/\pi\mathbb Z\) consist of the \(m\) unoriented lines from the origin through its antipodal vertex pairs. For representatives \(\theta,\phi\in[0,\pi)\), set
\[
d_\pi(\theta,\phi)=\min\{|\theta-\phi|,\pi-|\theta-\phi|\},\qquad
\varepsilon(K)=\min_{\theta\ne\phi\in\Theta}\left(\frac\pi2-d_\pi(\theta,\phi)\right).
\]
Thus \(0\le\varepsilon(K)<\pi/2\) measures how close any two vertex diameters come to perpendicularity.

**Theorem.** Among all nondegenerate Euclidean rectangles contained in \(K\), with arbitrary orientation and center, the largest perimeter is
\[
\boxed{\mathcal P(K)=4\sqrt2\,R\cos\left(\frac{\varepsilon(K)}2\right).}
\]
Every maximizing rectangle is centered at the origin and has all four corners at vertices of \(K\). Its two diagonals are exactly two vertex-diameter lines achieving \(\varepsilon(K)\); conversely every such pair gives a maximizing rectangle. When the vertices are supplied in cyclic order, one can find the exact optimal vertex pair and all maximizing pairs in \(O(m)\) geometric comparisons by a two-pointer angular scan.

For a regular even \(n\)-gon \(P_n\), \(n\ge4\), of circumradius \(R\), this gives
\[
\boxed{\mathcal P(P_n)=
\begin{cases}
4\sqrt2\,R,&n\equiv0\pmod4,\\
4\sqrt2\,R\cos\bigl(\pi/(2n)\bigr),&n\equiv2\pmod4.
\end{cases}}
\]
There are exactly \(n/4\) distinct maximizing squares in the first case and \(n/2\) maximizing nonsquare rectangles in the second. In particular, the regular-hexagon maximum is \(2(1+\sqrt3)R\), and the circumdisk-sharp perimeter deficit in the second case satisfies
\[
4\sqrt2 R-\mathcal P(P_n)=4\sqrt2 R\left(1-\cos\frac{\pi}{2n}\right)
\sim\frac{\sqrt2\pi^2R}{2n^2}.
\]

## Assumptions and scope

The polygon must be centrally symmetric **and** cyclic with respect to its symmetry center; its vertices all have the same Euclidean norm. Each rectangle must lie inside the whole polygon. Degenerate line-segment rectangles are allowed in intermediate convexity bounds but cannot maximize the perimeter for a nondegenerate polygon of this class. Distances and perimeters are Euclidean, and the cyclic vertex order is assumed known for the linear-time computation. No theorem is asserted for odd cyclic polygons, noncyclic centrally symmetric polygons, or rectangles with a fixed prescribed aspect ratio.

## Proof

**1. Centering is harmless.** Write any rectangle contained in \(K\) as
\[
Q=c+[-u,u]+[-v,v],\qquad u\perp v.
\]
Central symmetry gives \(-Q\subseteq K\). Their Minkowski average \((Q+(-Q))/2\) is the rectangle \(Q_0=[-u,u]+[-v,v]\), also contained in \(K\), with the same side lengths and perimeter. Hence a perimeter maximizer may be taken centered.

**2. A convex upper bound is attained by polygon vertices.** Put \(p=u+v\) and \(q=u-v\). The four corners of \(Q_0\) are \(\{p,q,-p,-q\}\), and \(\|p\|=\|q\|\). Conversely, any two linearly independent equal-norm vectors \(p,q\in K\) determine a centered rectangle in \(K\). Its perimeter is
\[
\operatorname{per}(Q_0)=2F(p,q),\qquad F(p,q)=\|p+q\|+\|p-q\|.
\]
The function \(F\) is convex separately in each variable. Writing arbitrary \(p,q\in K\) as convex combinations of polygon vertices \(v_i\), \(v_j\) therefore yields
\[
F(p,q)\le\max_{i,j}F(v_i,v_j).
\]
All vertices have norm \(R\). Consequently, each linearly independent vertex pair \(v_i,v_j\) supplies an *actual* contained rectangle \(\operatorname{conv}\{\pm v_i,\pm v_j\}\). A nonparallel pair has \(F(v_i,v_j)>2R\), whereas a parallel pair has \(F(v_i,v_j)=2R\). Therefore the maximum occurs at a nonparallel vertex pair and the preceding upper bound is attained. It follows that
\[
\mathcal P(K)=2\max_{i,j} F(v_i,v_j).
\]

**3. All equality cases are vertex-supported.** At any nondegenerate centered maximizing rectangle, \(p,q\) are linearly independent. For a nonzero perturbation \(w\), the second directional derivative of \(F(\cdot,q)\), wherever \(p\pm q\ne0\), is
\[
D^2_pF(p,q)[w,w]=\sum_{z\in\{p+q,p-q\}}
\frac{\|w\|^2\|z\|^2-\langle z,w\rangle^2}{\|z\|^3}.
\]
Each summand is nonnegative by Cauchy--Schwarz, and they cannot both vanish for \(w\ne0\), because \(p+q\) and \(p-q\) are linearly independent. Thus \(F(\cdot,q)\) is strictly convex on every sufficiently short segment through \(p\). If \(p\) were not a vertex of \(K\), it would lie in the relative interior of a nontrivial segment in \(K\); strict convexity on a short subsegment would contradict global maximality of \(F(p,q)\) over \(K\times K\). Hence \(p\) is a vertex; symmetry of \(F\) yields the same for \(q\).

The centered optimum has \(\|p\|=R\). If an off-center rectangle \(Q=c+Q_0\) had the same perimeter, the centered version would also maximize and have such a vertex \(p\). But \(c+p,c-p\in K\subseteq RB_2^2\) would imply
\[
2R^2+2\|c\|^2=\|c+p\|^2+\|c-p\|^2\le2R^2,
\]
so \(c=0\). Hence **every** maximizing rectangle is centered and vertex-supported.

**4. Exact angular law.** If the smaller oriented angle between the radius vectors \(v_i,v_j\) is \(\delta\in(0,\pi)\), then
\[
\|v_i+v_j\|=2R\cos(\delta/2),\qquad
\|v_i-v_j\|=2R\sin(\delta/2).
\]
Therefore
\[
2F(v_i,v_j)=4R\left(\cos\frac\delta2+\sin\frac\delta2\right)
=4\sqrt2 R\cos\left(\frac{\delta-\pi/2}{2}\right).
\]
Replacing oriented vertex vectors with their unoriented diameter lines turns \(|\delta-\pi/2|\) into \(\pi/2-d_\pi(\theta_i,\theta_j)\). The cosine is strictly decreasing on the relevant nonnegative interval. This proves the exact perimeter formula and the complete equality classification.

**5. Linear-time selection and the regular case.** List the \(m\) diameter-line angles \(0\le\theta_1<\cdots<\theta_m<\pi\), and append \(\theta_i+\pi\) to obtain a sorted doubled list. For each \(i\), a partner whose angle is nearest to \(\theta_i+\pi/2\) in the doubled list minimizes the perpendicularity defect. The target angles increase with \(i\), so one forward pointer and its immediate neighbors find all optimal partners in \(O(m)\) time. To report all tied pairs, process equal minimal discrepancies once each; at most \(O(m)\) neighboring pairs occur.

For a regular \(n=2m\)-gon, the diameter lines are spaced by \(2\pi/n\) modulo \(\pi\). A perpendicular pair exists exactly when \(4\mid n\). Otherwise the minimum perpendicularity defect is \(\pi/n\). The first case has \(n/4\) orthogonal unordered diameter pairs and the second case has \(n/2\) nearest-perpendicular unordered pairs. Substitution proves the formulas and counts. The displayed asymptotic follows from \(1-\cos t\sim t^2/2\) as \(t\to0\).

## Verification

The complete proof is analytic and covers every stated polygon and rectangle. The standalone diagnostic `verify_rectangle.py`, runnable with the Python standard library, separately compares the vertex-pair perimeter maximum with the exact angular formula for regular even polygons of orders \(4\) through \(602\), and for \(104\) deterministic pseudo-random centrally symmetric cyclic polygons. It also compares the two-pointer angular scan against a quadratic pair scan and tests \(26{,}000\) randomly sampled contained centered rectangles. Its recorded result was `VERIFY_OK regular_cases=300 cyclic_polygons=104 interior_rectangle_checks=26000`. These finite tests check implementation and normalization only; they do not establish the universal theorem.

## Relationship to prior work

Cabello, Cheong, Knauer, and Schlipf (2014) establish an exact cubic-time procedure for a maximum-perimeter rectangle in **any** convex polygon (Theorem 5). Their general algorithm establishes computability but does not give the geometric vertex-pair reduction, perpendicularity-defect formula, all-maximizer classification, or linear-time special-family algorithm proved here. Knauer, Schlipf, Schmidt, and Tiwary (2012) discuss largest inscribed **area** rectangles and identify perimeter optimization as a separate direction in their Section 6. Choi, Lee, and Ahn (2021) subsequently treat maximum-perimeter rectangles in general polygons, again algorithmically. A published calculation of largest-area rectangles in regular even polygons gives a related area formula; maximizing area does not by itself imply the different perimeter optimum or the cyclic-polygon vertex principle. The two objectives happen to select the same vertex rectangles on regular even polygons, but the perimeter inequality and all-cyclic extension need the separate proof above.

## Limitations

The equality theorem relies on both cyclicity and central symmetry; neither assumption is removed. The time bound uses vertices supplied in cyclic order and an exact real-geometric comparison model, not a bit-complexity bound for arbitrary algebraic coordinates. No claim is made about globally optimal rectangles under non-Euclidean perimeter or prescribed aspect ratio. Published general algorithms do apply to this class, so the claimed advance is an explicit structural formula, full equality classification, and a class-specific linear-time method, not a solution of the general polygon problem. Earlier unindexed or differently worded treatments might have established this special-case principle; independent external validation has not been performed.

## References

1. S. Cabello, O. Cheong, C. Knauer, and L. Schlipf, “Finding Largest Rectangles in Convex Polygons,” arXiv:1405.1223, first public version 2014-05-06; especially Theorem 5. https://arxiv.org/abs/1405.1223
2. C. Knauer, L. Schlipf, J. M. Schmidt, and H. R. Tiwary, “Largest Inscribed Rectangles in Convex Polygons,” Journal of Discrete Algorithms 13 (2012), 78–85, DOI 10.1016/j.jda.2012.01.002. Open manuscript: https://kam.mff.cuni.cz/~hansraj/publications/rectangle.pdf
3. Y. Choi, S. Lee, and H.-K. Ahn, “Maximum-area and maximum-perimeter rectangles in polygons,” Computational Geometry 94 (2021), 101710, DOI 10.1016/j.comgeo.2020.101710. Earlier open version: https://arxiv.org/abs/1910.08686
4. “Exact maximum-area rectangles in every regular even polygon,” public mathematical record, identifier 10bad5e59427 (2026); distinguished from the perimeter objective treated here.
