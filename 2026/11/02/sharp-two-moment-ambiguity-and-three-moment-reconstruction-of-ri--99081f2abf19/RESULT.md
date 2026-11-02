# Sharp two-moment ambiguity and three-moment reconstruction of ring-torus surfaces

## Finding

Let \(\mathcal T(R,r)\subset\mathbb R^3\) be the standard embedded circular ring-torus surface, with major radius \(R\), minor radius \(r\), and \(0<r<R\). Select independent points \(X,Y\) uniformly by surface area on \(\mathcal T(R,r)\), and put \(D=\|X-Y\|_2\) (Euclidean chord distance, **not** intrinsic geodesic distance). Write \(m_{2j}=\mathbb E[D^{2j}]\) for \(j=1,2,3\). Define the squared aspect ratio \(x=(r/R)^2\in(0,1)\) and the scale-free moment ratios

\[
K=\frac{m_4}{m_2^2},\qquad J=\frac{m_6}{m_2^3}.
\]

The exact formulas are

\[
\begin{aligned}
m_2&=2(R^2+2r^2),\\
m_4&=\tfrac12(12R^4+52R^2r^2+39r^4),\\
m_6&=\tfrac12(40R^6+312R^4r^2+516R^2r^4+187r^6),\\
K(x)&=\frac{12+52x+39x^2}{8(1+2x)^2},\\
J(x)&=\frac{40+312x+516x^2+187x^3}{16(1+2x)^3}.
\end{aligned}
\]

**Sharp two-moment classification.** The complete realizable \((m_2,m_4)\) region is

\[
m_2>0,\qquad \frac{103}{72}<\frac{m_4}{m_2^2}\leq\frac{26}{17}.
\]

For \(3/2<K<26/17\), there are **exactly two** noncongruent positive-radius ring tori giving that pair of moments. For \(103/72<K\leq3/2\), and for \(K=26/17\), there is **exactly one**. If two different aspect ratios \(x,y\in(0,1)\) have equal \(K\), they are exchanged by the involution

\[
y=\frac{4-9x}{52x+9},\qquad 0<x<\frac49.
\]

**Three-moment rigidity and sharp inverse bound.** The contrast

\[
T=J-6K=-\frac{104+600x+1200x^2+749x^3}{16(1+2x)^3}
\]

is strictly increasing on \((0,1)\), because

\[
T'(x)=\frac{3(51x^2+8)}{16(1+2x)^4}>0.
\]

Thus the first three consecutive even moments reconstruct \(x\) uniquely by the unique \(x\in(0,1)\) satisfying the displayed contrast equation, and then

\[
R^2=\frac{m_2}{2(1+2x)},\qquad r^2=\frac{x m_2}{2(1+2x)}.
\]

Moreover, for any two ring tori with dimensionless contrasts \(T_1,T_2\) and squared aspect ratios \(x_1,x_2\),

\[
|x_1-x_2|\leq\frac{432}{59}|T_1-T_2|.
\]

The coefficient \(432/59\) is the **smallest possible universal coefficient**. For the unsquared ratio \(r/R=\sqrt{x}\) a global Hölder estimate with exponent \(1/2\) follows; that exponent is optimal near the collapsing-tube limit \(x\downarrow0\). Hence three *consecutive* even moments are necessary and sufficient for universal ring-torus reconstruction; no assertion is made about all other possible pairs of moments.

## Assumptions and scope

The surfaces are boundaries only, not solid tori. They have revolution radii \(R>r>0\), are smooth and embedded, and are sampled according to normalized two-dimensional Hausdorff (surface-area) measure. The two samples are independent. Rigid congruence of such ring tori corresponds to equality of their ordered major and minor radii. The sampled distance is the ambient Euclidean chord length. All moment identities and inequalities are for exact population moments, with no measurement noise assumptions.

A standard parameterization with \(0\leq\theta,\phi<2\pi\) is

\[
F(\theta,\phi)=((R+r\cos\theta)\cos\phi,\ (R+r\cos\theta)\sin\phi,\ r\sin\theta).
\]

The area form is \(r(R+r\cos\theta)\,d\theta\,d\phi\); its total mass is \(4\pi^2Rr\). Therefore \(\phi\) is uniform and independent of \(\theta\), whose normalized density is \((1+(r/R)\cos\theta)/(2\pi)\). Equal-uniform angle sampling is **not** uniform in surface area.

## Proof

Set \(A=\|X\|_2^2\) and \(C=\mathbb E[XX^{\mathsf T}]\). The surface measure is invariant under \(X\mapsto-X\), so all odd tensor moments vanish. Direct integration of powers of \(\cos\theta\) under the weighted angular measure gives

\[
\begin{aligned}
\mathbb E A &=R^2+2r^2,\\
\mathbb E A^2&=R^4+6R^2r^2+3r^4,\\
\mathbb E A^3&=R^6+12R^4r^2+18R^2r^4+4r^6,\\
C&=\operatorname{diag}\left(\frac{2R^2+3r^2}{4},\frac{2R^2+3r^2}{4},\frac{r^2}{2}\right).
\end{aligned}
\]

For \(B=\mathbb E[A XX^{\mathsf T}]\), the same integration yields

\[
B=\operatorname{diag}\left(\frac{4R^4+22R^2r^2+9r^4}{8},\frac{4R^4+22R^2r^2+9r^4}{8},\frac{r^2(2R^2+3r^2)}{4}\right).
\]

With independent copies \(X,Y\), expanding \(D^2=\|X\|^2+\|Y\|^2-2X\cdot Y\), independence and central symmetry give

\[
\begin{aligned}
\mathbb E D^2&=2\mathbb E A,\\
\mathbb E D^4&=2\mathbb E A^2+2(\mathbb E A)^2+4\operatorname{tr}(C^2),\\
\mathbb E D^6&=2\mathbb E A^3+6\mathbb E A^2\,\mathbb E A+24\operatorname{tr}(BC).
\end{aligned}
\]

The last formula uses \(\mathbb E[(X\cdot Y)^3]=0\) and \(\mathbb E[(\|X\|^2+\|Y\|^2)^2 X\cdot Y]=0\), valid under the stated symmetry. Substitution proves the three moment polynomials and hence the rational expressions for \(K\) and \(J\).

For the two-moment classification, differentiate:

\[
K'(x)=\frac{2-13x}{4(1+2x)^3}.
\]

It is positive for \(0<x<2/13\), zero at \(2/13\), and negative for \(2/13<x<1\). Direct evaluation gives \(K(0)=3/2\), \(K(2/13)=26/17\), \(K(1)=103/72\). The endpoint values at \(x=0,1\) are excluded by \(0<r<R\). For two distinct parameters \(x,y\), clearing the positive denominators yields

\[
K(x)-K(y)=-\frac{(x-y)(52xy+9x+9y-4)}{8(1+2x)^2(1+2y)^2}.
\]

Thus equal moments with \(x\neq y\) force \(y=(4-9x)/(52x+9)\). The partner is positive exactly when \(0<x<4/9\). Both branches intersect each horizontal value in \((3/2,26/17)\) once, while outside this interval the unique solution lies on the decreasing branch. After choosing an aspect ratio, \(m_2\) determines the absolute scale by the displayed formula for \(R^2\). This proves the complete feasibility and multiplicity classification.

For the three-moment claim, put \(T(x)=J(x)-6K(x)\). Elementary polynomial arithmetic gives

\[
T'(x)=\frac{3(51x^2+8)}{16(1+2x)^4},\qquad
T''(x)=-\frac{3(102x^2-51x+32)}{8(1+2x)^5}.
\]

The quadratic in the numerator of \(-T''\) is strictly positive on \(\mathbb R\), since its discriminant \(51^2-4\cdot102\cdot32\) is negative. Hence \(T'\) decreases strictly on \((0,1)\), with \(\inf T'=T'(1)=59/432\). The mean-value theorem gives the stated optimal Lipschitz inverse bound. Optimality of the coefficient follows by taking two distinct aspect ratios tending to \(1\). Finally,

\[
|\sqrt{x_1}-\sqrt{x_2}|\leq\sqrt{|x_1-x_2|}
\]

provides the Hölder exponent \(1/2\); as \(x\downarrow0\), \(T(x)-T(0)=\tfrac32 x+O(x^2)\), excluding any larger uniform exponent for recovering \(\sqrt{x}\). All claims follow.

An exact ambiguity witness uses \(x_1=1/16\) and \(x_2=55/196\), with

\[
(R_1^2,r_1^2)=\left(\frac89,\frac1{18}\right),\qquad
(R_2^2,r_2^2)=\left(\frac{98}{153},\frac{55}{306}\right).
\]

Both have \(m_2=2\) and \(K=3943/2592\), but \(J(x_1)-J(x_2)=-29305505/229220928\neq0\). Thus the surfaces are noncongruent and genuinely indistinguishable by their first two even chord moments.

## Verification

The included `verify_torus.py` requires Python 3 with no third-party packages. Execute `python3 verify_torus.py` in the directory containing it. It checks exact rational polynomial relations, the explicit ambiguity witness, inverse-contrast properties, and the integral moment formulas against an independently implemented double-angle quadrature. The angle quadrature analytically averages over the independent longitude difference, avoiding reuse of the tensor expansion. At the time of preparation the script returned `VERIFY_OK independent_angle_moments=30 rational_and_inverse_checks=274`.

The proof above, rather than these finite tests, establishes the universal statements. Independent human proof verification has not been performed.

## Relationship to prior work

Euclidean random-distance distributions and their moments are classical. Tu and Fischbach (public preprint 2002) derive general forward distributions and distance moments for spherical-volume sampling and arbitrary spherically symmetric densities. Sidiropoulos (public preprint 2014) obtains hypersphere-surface chord distributions and moments. Gallatin (2012) relates shape moments to Fourier transforms and geometric inference, principally for volume indicators and polygonal or polyhedral examples. Lellouche and Souris (2019) systematize forward Euclidean-distance distributions for compact sets, especially rectangles, disks and hyperspheres. Their general formulas and moment techniques are not claimed as new here.

The retained result concerns a distinct **surface-area sample on a nonconvex embedded ring torus** and its complete **inverse** two-/three-even-moment classification, with an explicit two-valued involution and an optimal stability coefficient. The relevant sections and full-text scope of these works were compared. No inspected source states or implies the present exact classification, but an equivalent unindexed or unpublished calculation remains a priority risk.

## Limitations

The class is restricted to standard smooth ring-torus surfaces in \(\mathbb R^3\) satisfying \(0<r<R\), sampled uniformly by surface area. The results do not cover solid tori, horn or spindle tori, arbitrary toroidal surfaces, ambient-dimension inference, geodesic distances, or sampling noise. The bound controls the **normalized squared aspect ratio** in terms of **normalized contrast differences**; it is not a claim of absolute radius stability without a scale assumption. The claim of minimality concerns the first *consecutive* even moments \(m_2,m_4,m_6\), not arbitrary selection of two even orders. Historical originality has not been independently certified.

## References

1. S.-J. Tu and E. Fischbach, “Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics,” arXiv:math-ph/0201046, first posted 2002-01-22; https://arxiv.org/html/math-ph/0201046v1 .
2. P. Sidiropoulos, “N-sphere chord length distribution,” arXiv:1411.5639, first posted 2014-11-20; https://arxiv.org/html/1411.5639v1 .
3. G. M. Gallatin, “Fourier, Gauss, Fraunhofer, Porod and the shape from moments problem,” *Journal of Mathematical Physics* 53 (2012), 013509; https://doi.org/10.1063/1.3676310 .
4. S. Lellouche and M. Souris, “Distribution of Distances between Elements in a Compact Set,” *Stats* 3 (2020), 1–15, first published 2019-12-26; https://doi.org/10.3390/stats3010001 .
5. T. Dray, “The Torus,” *Geometry of Differential Forms*, geometric parameterization and area form; https://sites.science.oregonstate.edu/coursewikis/GDF/book/gdf/torus.html .
