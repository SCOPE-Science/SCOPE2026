# Sharp two-endpoint diameter laws for random central tetrahedral sections

## Finding

Let \(T\subset\mathbb R^3\) be the regular tetrahedron with vertices
\[
A=(1,1,1),\quad B=(1,-1,-1),\quad C=(-1,1,-1),\quad D=(-1,-1,1).
\]
Let \(U\) be uniformly distributed on the Euclidean unit sphere \(S^2\), and let \(L(U)=\operatorname{diam}_2(T\cap U^\perp)\) be the ambient Euclidean diameter of the plane section through the tetrahedron's centroid. Its exact support is \([2,2\sqrt2]\). Its only minimizing unoriented section planes have coordinate-axis normals; its only maximizing planes are the six planes through the centroid and an edge of \(T\).

The two tails have **different sharp exponents and explicit leading coefficients**:
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\Pr\{L(U)\le2+\varepsilon\}}{\varepsilon}=\frac6\pi,\qquad
\lim_{\varepsilon\downarrow0}\frac{\Pr\{L(U)\ge2\sqrt2-\varepsilon\}}{\varepsilon^2}=\frac3{\pi\sqrt2}.}
\]
Both limits are strictly positive and finite. They are accompanied by local conditional limit laws. Conditional on the lower-tail event and a chosen minimizing normal near \((1,0,0)\), write the unit normal as \((1,y,z)/\sqrt{1+y^2+z^2}\). Then \((y,z)/\sqrt\varepsilon\) converges to uniform area measure on \([-1,1]^2\). Conditional on the upper-tail event near the maximizing normal \(u_0=(0,1,-1)/\sqrt2\), write
\[
U=\frac{u_0+x(1,0,0)+y(0,1,1)/\sqrt2}{\sqrt{1+x^2+y^2}}.
\]
Then \((x,y)/\varepsilon\) converges to uniform area measure on \([-1/2,1/2]\times[-1/(2\sqrt2),1/(2\sqrt2)]\). By tetrahedral symmetry each of the six minimizing *oriented* normals and each of the twelve maximizing oriented normals contributes equally in the respective tail; unoriented planes are obtained by identifying opposite normals.

## Assumptions and scope

The four vertices listed above have pairwise distance \(2\sqrt2\), and their centroid is the origin. Planes are linear (central), rather than affine planes with random offsets. Directions have rotation-invariant probability \(d\sigma/(4\pi)\) on \(S^2\). The diameter of a compact section is its maximal Euclidean point-to-point distance. Thus neither the in-plane inradius nor the three-dimensional width is the quantity measured. The limit sends a distance threshold to one of two fixed endpoints; there is no high-dimensional limit. No claim of an elementary formula for the entire cumulative distribution is made.

## Proof

**1. Enumerating sections and determining the minimum.** Write \(s_V=u\cdot V\) for each tetrahedron vertex. Since \(A+B+C+D=0\), the four numbers sum to zero. Away from measure-zero vertex-plane coincidences, their signs are either two positive and two negative, or one against three. Every vertex of the section is the intersection of a tetrahedral edge joining opposite-sign vertices.

In the two-positive/two-negative case, symmetries and reversal of the normal reduce to \(u=(1,y,z)\) with \(|y|+|z|<1\). The quadrilateral has opposite vertex pairs on edges \((AC,BD)\) and \((AD,BC)\). Direct interpolation on those four edges yields their squared diagonal lengths
\[
\begin{split}
Q_y(y,z)&=4\left(1+\frac{y^2(1+z^2)}{(1-z^2)^2}\right),\\
Q_z(y,z)&=4\left(1+\frac{z^2(1+y^2)}{(1-y^2)^2}\right).
\end{split}
\]
For clarity, the two vertices on \(AC\) and \(BD\) are respectively
\[
\left(-\frac y{1+z},1,-\frac y{1+z}\right),\qquad
\left(\frac y{1-z},-1,-\frac y{1-z}\right),
\]
which directly give \(Q_y\); swapping the two secondary coordinates gives \(Q_z\). Each diagonal length is at least \(2\), and both equal \(2\) only for \(y=z=0\). The section diameter is no smaller than either diagonal, so equality at the lower endpoint in this case occurs only at the coordinate-axis planes.

In the one-versus-three case, reverse the normal if needed and call the unique negative vertex \(D\). Let \(s_D=-S<0\), and let the three positive dot products be \(p_1,p_2,p_3\). Since \(\sum p_i=S\), the three section vertices are \(D+t_i(V_i-D)\) with
\[
t_i=\frac S{S+p_i},\qquad \sum_{i=1}^3\frac1{t_i}=4.
\]
Cauchy--Schwarz implies \(\sum_i t_i\ge9/4\). Two tetrahedral edges emanating from \(D\) meet at angle \(60^\circ\) and have length \(2\sqrt2\); hence the section side joining parameters \(t_i,t_j\) has squared length
\[
8\bigl(t_i^2+t_j^2-t_it_j\bigr)
=8\left[\left(\frac{t_i+t_j}{2}\right)^2+\frac34(t_i-t_j)^2\right].
\]
Some pair satisfies \((t_i+t_j)/2\ge(\sum t_i)/3\ge3/4\). Thus this section has diameter at least \(3\sqrt2/2>2\), with equality in the one-versus-three minimum precisely when all \(t_i=3/4\). Continuity handles normals with zero dot products. The global minimum is therefore \(2\), attained at exactly the three unoriented axis-normal planes.

**2. Determining the maximum.** Every plane section lies inside \(T\), whose diameter is its edge length \(2\sqrt2\). In a nondegenerate simplex, any pair of points at its maximal interpoint distance must be a pair of vertices: strict convexity of squared Euclidean distance along a nonconstant segment shows that replacing an interior convex combination by a suitable vertex strictly increases at least one endpoint distance. Therefore a central section reaches the tetrahedron's diameter exactly when it contains a whole tetrahedral edge. For each of the six edges, its two endpoints and the origin span a unique plane; these six planes are distinct. This proves the maximal value and all its equality cases. The diameter depends continuously on the plane orientation, and the normal sphere is connected; therefore every intermediate value between the two extrema occurs and the stated closed interval is exactly the support of the Haar law.

**3. Local geometry and lower-tail measure.** Near \(u=(1,0,0)\), the section is quadrilateral. Its two diagonals are the longest chords because the other four pairwise distances tend to \(\sqrt2\), whereas both diagonals tend to \(2\). The displayed exact identities imply uniformly as \((y,z)\to0\)
\[
L\left(\frac{(1,y,z)}{\sqrt{1+y^2+z^2}}\right)
=2+\max\{y^2,z^2\}+O((y^2+z^2)^2).
\]
Thus the scaled event \(L\le2+\varepsilon\) converges in this chart to the unit square in coordinates \((y,z)/\sqrt\varepsilon\). The spherical surface-area element in the chart is \((1+y^2+z^2)^{-3/2}\,dy\,dz\). The local event has area \(4\varepsilon+o(\varepsilon)\). Compactness and the unique equality classification from Step 1 ensure no other parts of the sphere contribute at this scale. There are six oriented axis normals, giving
\[
\Pr\{L\le2+\varepsilon\}=\frac{6(4\varepsilon+o(\varepsilon))}{4\pi}=\frac6\pi\varepsilon+o(\varepsilon).
\]
The same chart argument, after normalization by the event probability, proves the asserted uniform-square conditional law.

**4. Local geometry and upper-tail measure.** Fix the edge \(AB\) and its maximizing normal \(u_0=(0,1,-1)/\sqrt2\). Use the orthonormal tangent basis \(e=(1,0,0)\), \(f=(0,1,1)/\sqrt2\), and an unnormalized nearby normal \(u=u_0+xe+yf\). The four vertex dot products are exactly
\[
a=u\cdot A=x+\sqrt2y,\quad b=u\cdot B=x-\sqrt2y,\quad
c=u\cdot C=\sqrt2-x,\quad d=u\cdot D=-\sqrt2-x.
\]
The point of the section approaching \(A\) lies on \(AD\) if \(a>0\), and on \(AC\) if \(a<0\); the analogous point approaching \(B\) lies on \(BD\) or \(BC\). Edge interpolation, followed by projection along the unit vector \((A-B)/(2\sqrt2)\), gives the chord-length expansion
\[
|X(u)-Y(u)|=2\sqrt2-|a|-|b|+O(x^2+y^2).
\]
For sufficiently small \((x,y)\), this chord realizes the section diameter. Indeed the other edge intersection on \(CD\) tends to \((-1,0,0)\), whose distance to either \(A\) or \(B\) is only \(\sqrt6<2\sqrt2\). If \(a,b\) have opposite signs, there is additionally a crossing point \(Z\) on \(AB\). Write \(q=|a|\), \(r=|b|\). Its distances along that edge from the two endpoints are \(2\sqrt2\,q/(q+r)\) and \(2\sqrt2\,r/(q+r)\). By the exact barycentric Euclidean identity \(|P-Q|^2=4\sum_{i=1}^4(\lambda_i(P)-\lambda_i(Q))^2\), the squared distance from \(Z\) to the near-\(B\) point is smaller than \(|X-Y|^2\) whenever \(q+r\) is small: if the near-\(A\) edge parameter is \(\alpha=O(q)\) and the near-\(B\) parameter is \(\beta=O(r)\), the difference divided by \(8\) is
\[
\frac q{q+r}\left(2-\frac q{q+r}-\beta\right)-\alpha(1-\alpha)>0.
\]
For instance the first term is at least \(q/[2(q+r)]\) while the second is at most \(Cq\), uniformly for sufficiently small \(q+r\). The symmetric comparison applies to \(|Z-X|\). When \(a,b\) have the same sign, no point on \(AB\) is created. This establishes the diameter expansion in every adjacent sign chamber, uniformly across their boundaries:
\[
2\sqrt2-L\left(\frac{u}{\|u\|_2}\right)
=|x+\sqrt2y|+|x-\sqrt2y|+O(x^2+y^2)
=2\max\{|x|,\sqrt2|y|\}+O(x^2+y^2).
\]
Consequently the scaled upper-tail event in coordinates \((x,y)/\varepsilon\) tends to the rectangle \([-1/2,1/2]\times[-1/(2\sqrt2),1/(2\sqrt2)]\), of area \(1/\sqrt2\). Its spherical area is \(\varepsilon^2/\sqrt2+o(\varepsilon^2)\), since the chart Jacobian is \((1+x^2+y^2)^{-3/2}\). Step 2 isolates exactly twelve oriented edge-plane normals. Their neighborhoods are disjoint when sufficiently small, and therefore
\[
\Pr\{L\ge2\sqrt2-\varepsilon\}
=\frac{12(\varepsilon^2/\sqrt2+o(\varepsilon^2))}{4\pi}
=\frac3{\pi\sqrt2}\varepsilon^2+o(\varepsilon^2).
\]
The uniform-rectangle conditional law follows from the same scaled local area calculation. Reflection of a normal and tetrahedral symmetries account for the equal mixture weights.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It independently reconstructs every tetrahedral edge-plane intersection, checks the two quadrilateral diagonal formulas with exact rational arithmetic on a lattice, verifies both sharp global endpoint bounds on a separate grid of normals, and checks the candidate upper-diameter chord against all section vertex pairs in 2,200 randomly selected nearby directions (including both triangle and quadrilateral sign chambers). Two independent deterministic spherical-chart integrations give lower-tail and upper-tail normalized ratios near \(1.908\) and \(0.674\) at respective thresholds \(0.001\) and \(0.002\), consistent with the analytically proved coefficients \(6/\pi\approx1.90986\) and \(3/(\pi\sqrt2)\approx0.67524\). Run `python3 verify.py`; success prints `VERIFY_OK`. All asymptotic and equality statements are proved analytically above; no finite check or sampling statement is used as a substitute for their proofs.

## Relationship to prior work

Guédon, Litvak, Tatarko and Vritsiou, *On random diameters of convex bodies* (2026, arXiv:2609.24131), derive high-probability bounds for random section diameters of general convex bodies and study high-dimensional \(p\)-ellipsoids. The present computation instead determines the **sharp small-threshold probabilities and local direction laws** for central planar sections of the regular tetrahedron. The source's abstract is available, but its complete mathematical text was not accessible in the available environment; hence possible uninspected special-case calculations are a priority risk, not claimed absent.

The published *Exact Haar diameter law for central sections of the regular octahedron* and *Exact diameter law and exponential endpoint fluctuations for random cross-polytope hyperplane sections* establish different diameter laws for centrally symmetric \(\ell_1\) bodies, using antipodal radial pairs. Those identities do not apply to the noncentrally symmetric tetrahedron: its section diameter generally does not equal twice a section radius, and its lower and upper endpoint geometry has a different mechanism. *Exactly seven centroidal hyperplane sections of every tetrahedron* classifies planes with a centroid condition on the section, not diameter distributions under random orientation. Dirksen's *Sections of the regular simplex: Volume formulas and estimates* (2017) concerns section volume, not the diameter distribution or sharp endpoint probabilities.

## Limitations

The theorem is for one fixed three-dimensional regular tetrahedron and Haar-random planes through its centroid. It does not cover affine-offset sections, unequal-edge tetrahedra, higher-dimensional simplices, or the full central-section diameter cumulative distribution. The two limits concern asymptotically small endpoint neighborhoods. Numerical checks are supporting computations, not certificates of infinite statements. Earlier equivalent formulas in unindexed stochastic-geometry or regular-simplex section literature remain possible, and full-text inspection of the recent motivating paper could not be completed. An independent mathematical audit has not been performed.

## References

- O. Guédon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131 (initial public submission 2026-09-21).
- *Exact Haar diameter law for central sections of the regular octahedron*, published mathematical result, available in the public published-finding corpus research archive (2026).
- *Exact diameter law and exponential endpoint fluctuations for random cross-polytope hyperplane sections*, published mathematical result, public published-finding corpus research archive (2026).
- *Exactly seven centroidal hyperplane sections of every tetrahedron*, published mathematical result, public published-finding corpus research archive (2026).
- H. Dirksen, *Sections of the regular simplex: Volume formulas and estimates*, Mathematische Nachrichten 290 (2017), 2567–2584, doi:10.1002/mana.201600109.
