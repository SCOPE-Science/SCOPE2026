# A unique boundary-clearance crossover between cubic-lattice Voronoi cells

## Finding
Let \(B\) be the regular truncated-octahedral Voronoi cell of a body-centered cubic lattice, normalized as
\[
B=\{x\in\mathbb R^3: |x_i|\le1\ (i=1,2,3),\quad |x_1|+|x_2|+|x_3|\le\tfrac32\},
\]
and let \(F\) be the volume-matched rhombic-dodecahedral Voronoi cell of a face-centered cubic lattice,
\[
H=\{x\in\mathbb R^3:|x_i|+|x_j|\le 2\text{ for }1\le i<j\le3\},\quad F=4^{-1/3}H.
\]
Both cells have volume \(4\). If \(X_K\) is uniform in \(K\in\{B,F\}\), define its **boundary clearance** by \(D_K=\operatorname{dist}(X_K,\partial K)\), and the survival function \(S_K(t)=\mathbb P(D_K\ge t)\) for \(t\ge0\). Put
\[
T=\frac{1+\sqrt3}{4},\quad r_B=\frac{\sqrt3}{2},\quad r_F=2^{-1/6},\quad b(t)=\frac32-\sqrt3\,t,\quad c(t)=\frac12-(\sqrt3-1)t.
\]
Then the **complete clearance distributions** are
\[
S_B(t)=\begin{cases}
\dfrac{b(t)^3}{3}-c(t)^3,&0\le t\le T,\\
\dfrac{b(t)^3}{3},&T\le t\le r_B,\\
0,&t\ge r_B,
\end{cases}
\qquad
S_F(t)=\begin{cases}(1-t/r_F)^3,&0\le t\le r_F,\\0,&t\ge r_F.\end{cases}
\]
There is **exactly one** positive nonterminal crossover \(t_*\in(0,T)\), given as the unique zero there of
\[
Q(t)=\left(\frac3{r_F}-\frac{3\sqrt3}{2}-\frac34\right)
+\left(-\frac32+3\sqrt3-\frac3{r_F^2}\right)t
+\left(-10+5\sqrt3+\sqrt2\right)t^2.
\]
Numerically \(t_*=0.3250593022539285\ldots\). One has \(S_B(t)>S_F(t)\) for \(0<t<t_*\), and \(S_B(t)<S_F(t)\) for \(t_*<t<r_F\). Despite the initial BCC advantage and its smaller surface area, the **mean** boundary clearances satisfy
\[
\boxed{\mathbb E D_B=\frac{17\sqrt3-1}{128}=0.2222254978802415\ldots
\;<\;\mathbb E D_F=\frac{2^{-1/6}}4=0.2227246795350848\ldots.}
\]
The comparison is specific to these two equal-volume canonical lattice cells; it does not assert an optimizer among all lattices or all parallelohedra.

## Assumptions and scope
All distances and eroded bodies use the ordinary Euclidean metric. The cells are full-dimensional, centered, and compared at equal volume \(4\); a common scaling multiplies every clearance and the crossover depth by that scale. Uniform sampling means normalized three-dimensional Lebesgue measure, not uniform sampling of a boundary, direction, or lattice point. Equality of probabilities at \(t=0\) and after both survivals vanish is excluded from the unique *positive nonterminal crossover* assertion.

## Proof
**Geometry of the cells.** The body-centered lattice \(2\mathbb Z^3\cup((1,1,1)+2\mathbb Z^3)\) has the displayed Voronoi halfspaces from its nearest axial and body-diagonal neighbor vectors. The FCC cell \(H\) is the regular rhombic dodecahedron with eight vertices \((\pm1,\pm1,\pm1)\) and six vertices \(\pm2e_i\); it consists of the cube \([-1,1]^3\) and six pyramids of height \(1\) over its faces, hence \(\operatorname{vol}(H)=8+6(4/3)=16\). For \(B\), subtract the six disjoint caps \(\{|x_i|>1\}\) from the octahedron \(\{\lVert x\rVert_1\le3/2\}\) to find \(\operatorname{vol}(B)=\tfrac43(\tfrac32)^3-4(\tfrac12)^3=4\).

**Euclidean erosions.** The distance to a polytope boundary is the minimum Euclidean signed distance to its supporting facet hyperplanes. Consequently, \(B_t:=\{x\in B:\operatorname{dist}(x,\partial B)\ge t\}\) is exactly
\[
B_t=\{x:|x_i|\le a(t)=1-t,\quad\lVert x\rVert_1\le b(t)=\tfrac32-\sqrt3\,t\}.
\]
For \(0\le t<T\) one has \(a(t)<b(t)<2a(t)\). Each of the six clipped axial octahedral caps has volume \(\tfrac23(b-a)^3\); distinct caps do not intersect because \(b<2a\). The octahedron itself has volume \(\tfrac43b^3\), so \(\operatorname{vol}(B_t)=\tfrac43b^3-4(b-a)^3\). At \(T\), \(a(T)=b(T)\). For \(T\le t\le r_B\), the cube constraints are redundant and \(B_t\) is a regular octahedron of volume \(\tfrac43b(t)^3\); it vanishes at \(r_B\). Since \(\operatorname{vol}(B)=4\), dividing by \(4\) gives \(S_B\).

Every facet of \(H\) is at distance \(\sqrt2\) from the origin. Thus its Euclidean inner parallel bodies are \((1-t/\sqrt2)H\) up to the inradius, so the scaled cell \(F\) has \(S_F(t)=(1-t/r_F)^3\) with \(r_F=\sqrt2\,4^{-1/3}=2^{-1/6}\).

**The unique crossing.** On the first phase, expansion yields \(S_B(t)-S_F(t)=tQ(t)\). Its constant term is positive, its quadratic coefficient is positive, and \(Q(T)<0\). These strict signs follow, for instance, from the rational bounds
\[
1.73205<\sqrt3<1.73206,\quad 1.4142<\sqrt2<1.4143,\quad
0.8908<2^{-1/6}<0.8909.
\]
The last bound follows by raising positive rational endpoints to the sixth power. The quadratic \(Q\), opening upward and negative at \(T\), has exactly one zero in \((0,T)\). Beyond \(T\), compare the **cube roots** of the positive survivals: \(b(t)/\sqrt[3]3\) and \(1-t/r_F\) are affine in \(t\). The former is smaller at \(t=T\) and at \(t=r_B\), so it stays smaller throughout that interval. It is zero afterward while the FCC survival stays positive until \(r_F>r_B\). This proves every asserted strict comparison and uniqueness.

**The mean order.** For any nonnegative clearance, \(\mathbb E D_K=\int_0^\infty S_K(t)\,dt\). Integrating the two BCC cubic phases gives \((17\sqrt3-1)/128\); integrating the FCC cube gives \(r_F/4\). The displayed rational bounds prove the strict ordering without relying on decimal approximations: \(r_F/4>0.2227\), whereas \((17\sqrt3-1)/128<0.2223\).

## Verification
The included standard-library Python program `verify_clearance.py` was executed directly and returned `VERIFY_OK`. It uses exact rational brackets to prove the critical sign inequalities, performs symbolic integration in \(\mathbb Q(\sqrt3)\) for the BCC first and second moments, bisects the crossover with 60-digit decimal arithmetic, and compares the survival formula against a separate deterministic rejection-sampling computation with 240,000 cube points. The geometric halfspace and cap-volume arguments above are analytic and are not inferred from the finite sample.

## Relationship to prior work
Koçak and Ratiu (2010) establish that inner parallel volume of any polytope is piecewise polynomial and describe the general differentiability structure. Their general result does **not** give these two normalized lattice-cell laws, the precise crossover, or the mean-order reversal. Lucarini (2008) studies the BCC and FCC Voronoi geometries and distributions of whole-cell descriptors under perturbed lattices, rather than the distance-to-boundary distribution *inside* the unperturbed cells. Cesaroni and Novaga (2026) prove that the regular truncated octahedron uniquely minimizes surface area at fixed volume among parallelohedra, furnishing the context for the non-preservation of that ranking by mean clearance. Their surface-area theorem neither evaluates nor compares the clearance laws. The initial BCC advantage is also consistent with its strictly smaller surface-to-volume ratio: \(-S_K'(0)\) equals that ratio. Published work on illumination and one-skeleton metrics of the same cube–octahedron intersection family concerns different invariants and does not imply this result.

## Limitations
The full laws, unique crossover, and mean inequality are proved only for the specified equal-volume BCC and FCC shapes. Nothing here compares arbitrary affine distortions, random perturbations of either lattice, or other lattices. No global mean-clearance extremum is claimed. Exhaustive historical novelty cannot be certified; an unindexed contact-distribution calculation for periodic Voronoi boundaries might give equivalent formulas. The review is not independent validation.

## References
1. Ş. Koçak and A. V. Ratiu, *Inner tube formulas for polytopes*, arXiv:1008.2040v1 (first public 2010-08-12); published in Proc. Amer. Math. Soc. 140 (2012), 999–1010.
2. V. Lucarini, *Three-dimensional random Voronoi tessellations: From cubic crystal lattices to Poisson point processes*, arXiv:0805.2705v1 (2008-05-18).
3. A. Cesaroni and M. Novaga, *The truncated octahedron minimizes surface area among parallelohedra of equal volume*, arXiv:2609.02384v1 (2026-09-02).
