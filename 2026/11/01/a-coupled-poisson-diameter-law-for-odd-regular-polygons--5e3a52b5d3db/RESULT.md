# A coupled Poisson diameter law for odd regular polygons

## Finding

Fix an odd integer \(m=2r+1\ge3\). Let \(K_m\) be the regular \(m\)-gon with circumradius one, and let \(X_1,X_2,\ldots\) be independent points uniformly distributed with respect to planar area in \(K_m\). Write
\[
\mathcal D_N=\max_{1\le i<j\le N}\|X_i-X_j\|_2,
\qquad D_m=2\cos\!\left(\frac{\pi}{2m}\right).
\]
The maximum-sample-distance deficit has the following **complete weak limit**:
\[
\boxed{\sqrt N\,(D_m-\mathcal D_N)\xrightarrow{\mathrm d} Z_m:=\min_{j\in\mathbb Z/m\mathbb Z}\bigl(U_j+V_{j+r}\bigr).}
\]
The \(m\) bivariate random vectors \((U_j,V_j)\) are independent and identically distributed, but their two coordinates are *not* independent. Their joint law is specified explicitly below. This dependence records the fact that every vertex is an endpoint of two different longest diagonals. In particular it is not legitimate to replace these variables by \(2m\) independent Weibull variables.

Set
\[
p=\sin\!\left(\frac{\pi}{2m}\right),\qquad
q=\sin\!\left(\frac{3\pi}{2m}\right),\qquad
\lambda_m=\frac{1}{mpq};\qquad 0<p<q.
\]
Define the nonnegative area function, for \(s,t\ge0\), by
\[
I_{p,q}(s,t)=
\begin{cases}
\dfrac{t^2}{2pq},&t\le ps/q,\\[5pt]
\dfrac{2qst-p(s^2+t^2)}{2q(q^2-p^2)},&ps/q<t<qs/p,\\[5pt]
\dfrac{s^2}{2pq},&t\ge qs/p.
\end{cases}
\]
Then the full bivariate survival function is
\[
\boxed{\Pr(U_j>s,V_j>t)
=\exp\!\left[-\lambda_m(s^2+t^2)+\frac{2}{m}I_{p,q}(s,t)\right].}
\]
Consequently each coordinate has Weibull survival
\(\Pr(U_j>s)=\Pr(V_j>s)=e^{-\lambda_m s^2}\), while for \(s,t>0\) their joint survival is strictly greater than the product of the marginal survivals. The displayed independent-bivariate-vector representation therefore gives an explicit, simulation-ready limit for every odd regular polygon, including the triangle.

The lower tail of this limit is also exact to first order:
\[
\boxed{\Pr(Z_m\le t)=c_m t^4+O_m(t^6),\qquad
c_m=\frac{1}{6m\sin^2(\pi/(2m))\sin^2(3\pi/(2m))},\quad t\downarrow0.}
\]
For comparison, the established even-sided independent-diagonal limit yields \(c_m^{\mathrm{even}}=1/[12m\sin^4(\pi/m)]\) for an even \(m\)-gon of circumradius one. Hence **taking the small-tail limit first, then the number of sides to infinity**, the normalized coefficients have distinct parity constants:
\[
\lim_{\substack{m\to\infty\\m\ \mathrm{odd}}}\frac{c_m}{m^3}=
\frac{8}{27\pi^4},\qquad
\lim_{\substack{m\to\infty\\m\ \mathrm{even}}}\frac{c_m^{\mathrm{even}}}{m^3}=
\frac{1}{12\pi^4}.
\]
Their ratio is \(32/9\). No uniform joint limit in the polygon side count and sample size is asserted.

## Assumptions and scope

The polygon is nondegenerate, regular, has an *odd* fixed number \(m\ge3\) of sides, and has Euclidean circumradius one. The sample is independent and **area-uniform in the interior**, not arclength-uniform on its boundary. The number \(N\) of sampled points tends to infinity with \(m\) fixed. The long diagonals join precisely the unordered pairs \(\{v_j,v_{j+r}\}\), where \(v_j=(\cos(2\pi j/m),\sin(2\pi j/m))\), and their common length is \(D_m\). Each vertex belongs to exactly two such pairs. All probabilistic limits are ordinary weak convergence of real random variables at continuity points of the limiting law.

The limit vectors have an equivalent geometric definition. Let \(\Pi_j\), independently for \(j\in\mathbb Z/m\mathbb Z\), be homogeneous Poisson point processes of intensity \(2/m\) with respect to Lebesgue area in the positive quadrant. Define
\[
U_j=\inf_{(x,y)\in\Pi_j}(qx+py),\qquad
V_j=\inf_{(x,y)\in\Pi_j}(px+qy).
\]
All infima exist and are finite and strictly positive almost surely. Either this construction or the joint survival formula in the Finding section specifies the complete law. If the polygon is rescaled by a positive factor \(a\), the limit \(Z_m\) is rescaled by the same factor \(a\).

## Proof

**1. Diameter geometry.** The Euclidean distance is convex separately in each argument over the polygon, so a diametral pair can be chosen among vertices. The longest chord of an odd regular polygon spans \(r\) or \(r+1\) vertex steps; the resulting unordered pairs are exactly \(\{v_j,v_{j+r}\}\), indexed without duplication by \(j\in\mathbb Z/m\mathbb Z\). Their distance is \(D_m\). All other vertex-pair distances are separated from this value by a positive gap (depending on fixed \(m\)). On each incident edge at either endpoint of a longest chord, motion inward has strictly positive first-order distance cost, because the outgoing chord makes an angle strictly smaller than a right angle with both inward edge directions. Thus the finite set of diametral vertex pairs consists of isolated, strictly transverse maximizers of distance on \(K_m\times K_m\).

**2. Explicit cone coordinates and first derivatives.** At each vertex use the two unit edge directions as a basis for the interior tangent cone. A point near \(v_j\) can be written \(v_j+a e_j^+ +b e_j^-\), with \(a,b\ge0\) and sufficiently small. With \(m=2r+1\), the direction from \(v_j\) to \(v_{j+r}\) has scalar products \(q\) and \(p\), respectively, with the two incident inward unit edges, after consistent cyclic labelling. The direction from \(v_j\) to \(v_{j-r}\) exchanges these scalar products. Consequently the two directional losses at \(v_j\), in these cone coordinates, are
\[
L_j^+(a,b)=qa+pb,\qquad L_j^-(a,b)=pa+qb.
\]
For points near the endpoints of one longest diagonal, a Taylor expansion of the Euclidean norm gives, uniformly in a fixed sufficiently small vertex neighborhood,
\[
D_m-\|X-Y\|_2
=L_j^+(a,b)+L_{j+r}^-(c,d)
+O_m\bigl((a+b+c+d)^2\bigr).
\]
The elementary trigonometry comes from the angles \(\pi/2-3\pi/(2m)\) and \(\pi/2-\pi/(2m)\), whose cosines are \(q\) and \(p\). At an arbitrary fixed vertex the two directional linear forms are different because \(p<q\).

**3. Corner point processes.** The determinant of the two unit edge directions is \(\sin(2\pi/m)\). The polygon area is \(A_m=(m/2)\sin(2\pi/m)\). Therefore the area-uniform intensity in cone coefficients equals their Jacobian divided by the polygon area, namely \(2/m\). In the coordinates \((\sqrt N a,\sqrt N b)\), the binomial sample converges jointly at all \(m\) vertices, on bounded subsets of the quadrant, to independent homogeneous Poisson processes \(\Pi_j\) of intensity \(2/m\). To see this directly, take finitely many disjoint bounded regions in scaled, distinct corner charts. Their probabilities for one sampled point are their limiting cone areas divided by \(N\), up to \(o(N^{-1})\). The multinomial probability-generating function converges to the product of the corresponding Poisson generating functions. The corner processes are therefore independent across vertices but single processes must be reused for the two outgoing diameter directions at each vertex.

**4. Localization and the diameter limit.** Fix \(T>0\). By compactness and the isolation in step 1, there is a positive gap below \(D_m\) when a pair is outside fixed neighborhoods of all diametral vertex pairs. Within those neighborhoods, the positive coefficients \(p,q\) yield a lower bound \(c_m(\|X-v_j\|+\|Y-v_{j+r}\|)\) on the distance deficit for some \(c_m>0\), after shrinking the neighborhoods. Hence any pair with \(D_m-\|X-Y\|\le T/\sqrt N\) has both corner coefficient pairs bounded by a constant multiple of \(T/\sqrt N\). On these bounded rescaled charts the quadratic norm remainder is \(O_m(N^{-1})\), uniformly, and the joint limiting corner Poisson processes have almost surely no points on the finitely many relevant linear decision boundaries. Applying the continuous mapping theorem to the minimum over all diameter-edge pairs now gives
\[
\sqrt N(D_m-\mathcal D_N)\Longrightarrow
\min_j\left[\inf_{(x,y)\in\Pi_j}(qx+py)
+\inf_{(x,y)\in\Pi_{j+r}}(px+qy)\right].
\]
A standard bounded-window truncation completes this mapping: with probability approaching one as the truncation radius grows, each relevant Poisson linear minimum is achieved in that bounded window. This is the asserted \(Z_m\).

**5. Joint survival calculation.** For \(s,t\ge0\), the event \(U_j>s,V_j>t\) requires that \(\Pi_j\) avoid the union of the right triangles
\[
T_1(s)=\{(x,y)\ge0:qx+py\le s\},\qquad
T_2(t)=\{(x,y)\ge0:px+qy\le t\}.
\]
Their respective areas are \(s^2/(2pq)\) and \(t^2/(2pq)\). Their intersection area is \(I_{p,q}(s,t)\): if one triangle contains the other the first or third formula applies; otherwise the sloping sides cross at
\[
\left(\frac{qs-pt}{q^2-p^2},\frac{qt-ps}{q^2-p^2}\right),
\]
and a two-dimensional shoelace calculation yields the middle formula. The Poisson void probability at intensity \(2/m\) is precisely the boxed joint survival law. Since both triangles contain a neighborhood of the origin whenever \(s,t>0\), their intersection has positive area, proving strict nonindependence.

**6. Exact lower-tail coefficient.** For a fixed pair \(j,j+r\), its two one-sided deficits \(U_j\) and \(V_{j+r}\) come from different corner processes and are independent, each with cumulative distribution \(1-e^{-\lambda_m t^2}\). Therefore their sum has lower tail
\[
\Pr(U_j+V_{j+r}\le t)
=\int_0^t 2\lambda_m u e^{-\lambda_m u^2}
\bigl(1-e^{-\lambda_m(t-u)^2}\bigr)\,du
=\frac{\lambda_m^2}{6}t^4+O_m(t^6).
\]
Two different longest-diagonal events use either four different corner processes (joint probability \(O_m(t^8)\)) or three distinct corner processes when the diagonals share an endpoint (joint probability \(O_m(t^6)\)). The latter bound uses that each participating corner must contain a Poisson point in a triangle of area \(O_m(t^2)\), regardless of whether the shared corner contributes one or two such points. There are finitely many diagonal pairs for fixed \(m\). Inclusion–exclusion thus yields
\[
\Pr(Z_m\le t)=m\,\frac{\lambda_m^2}{6}t^4+O_m(t^6)
=\frac{t^4}{6mp^2q^2}+O_m(t^6).
\]
Finally, the even-sided coefficient follows from the established independent-diametral-axis law with \(m/2\) independent pairs and marginal Weibull parameter \(1/[m\sin^2(\pi/m)]\); the stated parity constants are immediate from \(\sin x\sim x\). This comparison uses successive limits, not a uniform limit as \(m\) and \(N\) vary jointly. \(\square\)

## Verification

The accompanying executable \`verify_odd_polygon_diameter.py\` independently checks the unit-edge projection coefficients against coordinates of the regular polygons, the area of actual polygonal projection caps against the exact \(\lambda_m t^2\) law for sufficiently small \(t\), and the closed intersection-area formula against numerical quadrature in several regimes. It also verifies positivity and symmetry of the bivariate survival law, its marginal bounds, the exact lower-tail coefficient, and simulated Poisson and finite-sample behavior. Run \`python3 verify_odd_polygon_diameter.py\`. The expected output is \`VERIFY_OK 194 deterministic and seeded checks\`.

The analytical proof—not simulations or a finite search—establishes convergence for every fixed odd \(m\ge3\). Sample simulations check only finite choices of \(m,N,t\); they neither certify historical novelty nor prove uniform convergence in the side count.

## Relationship to prior work

The fundamental problem of random-sample diameter asymptotics was studied by Appel, Najim and Russo (2002), Mayer and Molchanov (2006), and Wei Lao (2010). Mayer–Molchanov explicitly characterize the earlier Appel–Najim–Russo theorem as requiring a unique longest chord; this condition fails for every regular polygon here. Mayer–Molchanov study balls, not the positive-codimension shared-endpoint diameter graph of an odd regular polygon. Lao's dissertation, Chapter 6, Theorem 6.8, treats **area-uniform samples in even-sided regular polygons**, where the diameter endpoints are disjoint and independent Weibull deficits apply. Lao's Chapter 5, Section 5.2, treats **arclength-uniform boundary samples in odd-sided polygons**, a different sampling model with a different scaling, and explicitly records its shared-endpoint complications. The present area-uniform odd-sided theorem and bivariate cone law address the missing combination.

The nearby literature on two independently sampled points in a fixed polygon addresses the scalar interpoint-distance distribution, not the maximum of a growing sample coupled through shared near-diametral vertices. The Poisson construction may be expressed equivalently using the cycle of longest-diagonal incidences, so differences in indexing are not proposed as novelty. The contribution is the full coupled weak-limit representation and its sharp small-tail coefficient, not the use of Poisson convergence by itself.

## Limitations

The assertions require fixed odd \(m\ge3\), circumradius-one regularity, and area-uniform independent sampling. The formulas do not cover arbitrary irregular polygons, random points sampled on the boundary, or simultaneous \(N,m\to\infty\) scalings. The small-tail coefficient is for the limiting variable \(Z_m\), with \(t\to0\) *after* \(N\to\infty\). No claim is made about an elementary one-variable closed form for the entire cumulative distribution. Priority comparisons can miss unindexed equivalent theorems; independent historical and mathematical review has not been performed.

## References

1. M. J. B. Appel, C. A. Najim and R. P. Russo, “Limit laws for the diameter of a random point set,” *Advances in Applied Probability* **34** (2002), 1–10, DOI: 10.1239/aap/1019160946. Historical comparison from published abstract and subsequent explicit summary; full primary paper was not available for direct inspection.
2. M. Mayer and I. Molchanov, “A limit theorem for the maximal interpoint distance of a random sample in the unit ball,” arXiv:math/0605289, initially submitted 2006-05-11; see the introduction's characterization of the 2002 hypotheses. https://arxiv.org/abs/math/0605289
3. W. Lao, *Some Weak Limit Laws for the Diameter of Random Point Sets in Bounded Regions*, Karlsruhe Institute of Technology (2010), DOI: 10.5445/KSP/1000019800; especially Chapter 5 §5.2 and Chapter 6 Theorem 6.8. https://publikationen.bibliothek.kit.edu/1000019800
4. S. R. Jammalamadaka and S. Janson, “Asymptotic distribution of the maximum interpoint distance in a sample of random vectors with a spherically symmetric distribution,” *Annals of Applied Probability* **25** (2015), 3571–3591, DOI: 10.1214/14-AAP1082.
5. F. Tong, M. Ahmadi and J. Pan, “Random distances associated with arbitrary triangles: A systematic approach between two random points,” arXiv:1312.2498, initially submitted 2013-11-29; fixed-two-point distance comparison only.
