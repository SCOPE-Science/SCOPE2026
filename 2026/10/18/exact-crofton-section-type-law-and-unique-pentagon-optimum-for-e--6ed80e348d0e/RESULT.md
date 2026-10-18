# Exact Crofton section-type law and unique pentagon optimum for equilateral triangular bipyramids

## Finding
For every \(h>0\), put
\[
 B_h=\operatorname{conv}\{(0,0,h),(0,0,-h), (\cos(2\pi j/3),\sin(2\pi j/3),0):j=0,1,2\}\subset\mathbb R^3.
\]
Choose an unoriented affine plane from Euclidean-motion-invariant measure, conditioned on its intersecting the interior of \(B_h\), and write \(N\) for the number of vertices of the intersection polygon. Every generic section has \(N\in\{3,4,5,6\}\). Define
\[
 I(h)=\int_0^{\pi/3}\cos t\arctan\frac{\cos t}{h}\,dt,\qquad
 K(h)=\int_0^{\pi/6}\sin t\arctan\frac{\sin t}{h}\,dt,
\]
\[
 D(h)=\pi h+3I(h),\qquad C=\frac{3\sqrt3\pi}{4}.
\]
Then the **complete four-type probability law** is
\[
\boxed{\begin{aligned}
 \Pr(N=3)&=1-\frac C{D(h)},\\
 \Pr(N=4)&=\frac{3[I(h)-K(h)]}{D(h)},\\
 \Pr(N=5)&=\frac{C-3I(h)}{D(h)},\\
 \Pr(N=6)&=\frac{3K(h)}{D(h)}.
\end{aligned}}
\]
Both integrals are elementary:
\[
\begin{aligned}
 I(h)&=\frac{\sqrt3}{2}\arctan\frac1{2h}+\sqrt{1+h^2}\arctan\frac{\sqrt3h}{\sqrt{1+h^2}}-\frac{\pi h}{3},\\
 K(h)&=-\frac{\sqrt3}{2}\arctan\frac1{2h}+\sqrt{1+h^2}\arctan\frac{\sqrt{1+h^2}}{\sqrt3h}-\frac{\pi h}{6}.
\end{aligned}
\]
The pentagon probability has **exactly one global maximizer** on \((0,\infty)\), namely the unique \(h_*\) satisfying
\[
 D(h_*)=\left(h_*+\frac{3\sqrt3}{4}\right)D'(h_*),\qquad
 D'(h)=\frac{3h}{\sqrt{1+h^2}}\arctan\frac{\sqrt3h}{\sqrt{1+h^2}}.
\]
Numerically \(h_*=1.211448413582648\ldots\) and \(\Pr_{h_*}(N=5)=0.462970871315319\ldots\). In particular, the equilateral-faced triangular bipyramid (\(h=\sqrt2\)) does **not** maximize pentagonal sections.

## Assumptions and scope
The base is an equilateral triangle of circumradius one in the horizontal plane; the apices are opposite points at perpendicular distances \(h\). Other sizes differ by similarity and hence have the same law at the same height-to-circumradius ratio. A plane is specified by \(u\cdot x=t\), where \(u\in S^2\); the invariant unoriented-plane measure is the quotient of \(d\sigma(u)\,dt\) by \((u,t)\sim(-u,-t)\). Conditioning on intersection weights directions by the **full projection width** \(w_h(u)=\max_{x\in B_h}u\cdot x-\min_{x\in B_h}u\cdot x\); it does not leave \(u\) uniformly distributed. Planes containing a vertex are null and are excluded when counting \(N\).

## Proof
**1. Denominator.** Write \(u=(\sqrt{1-z^2}\cos\phi,\sqrt{1-z^2}\sin\phi,z)\) with uniform \(\phi\) and uniform \(z\in[-1,1]\). Put \(m(\phi)=\max_{j=0,1,2}\cos(\phi-2\pi j/3)\). The support function is \(s_h(u)=\max(h|z|,m(\phi)\sqrt{1-z^2})\). Directly splitting the \(|z|\)-integral at \(m/\sqrt{h^2+m^2}\) gives
\[
 \mathbb E_zs_h(u)=\frac h2+\frac{m(\phi)}2\arctan\frac{m(\phi)}h.
\]
On each of three equal angular sectors \(m=\cos\phi\), \(|\phi|\le\pi/3\). Consequently \(\mathbb E_\phi[m\arctan(m/h)]=3I(h)/\pi\). Since \(\int_{S^2}w_h\,d\sigma=2\int_{S^2}s_h\,d\sigma\), the exact normalizing integral is
\[
 \mathcal W(h)=\int_{S^2}w_h(u)\,d\sigma(u)=4\bigl(\pi h+3I(h)\bigr)=4D(h).
\]

**2. Edge-crossing parity.** The one-skeleton of a triangular bipyramid is the complete graph on five vertices with the apex-apex edge deleted. If an offset plane strictly separates \(k\) vertices from the other \(5-k\), its section has
\[
 N=k(5-k)-\mathbf1_{\{\text{apices separated}\}}.
\]
The product \(k(5-k)\) is always even. Thus \(N\) is odd if and only if the two apex heights have opposite signs relative to the cutting level. For fixed \(u\), the total length of offsets producing an odd section is precisely \(2h|z|\). Integrating this length over \(S^2\) gives \(4\pi h\); hence
\[
 \Pr(N=3)+\Pr(N=5)=\frac{\pi h}{D(h)}.
\]
The crossing formula also yields \(N\in\{3,4,5,6\}\) for every generic nonempty section.

**3. Hexagons.** Let \(e_1\le e_2\le e_3\) be the three projected base-vertex heights. Because their sum is zero, \(e_1\le0\le e_3\). The two apex heights are \(\pm h|z|\). A six-edge section occurs exactly when the apices lie on the same side, with zero or one base vertex accompanying them on that side. The total offset length is therefore
\[
 \ell_6(u)=\bigl(|e_2|-h|z|\bigr)_+.
\]
For \(q=|\operatorname{median}_j\cos(\phi-2\pi j/3)|\), we have \(|e_2|=q\sqrt{1-z^2}\). An elementary one-dimensional integration gives
\[
 \mathbb E_{|z|}\bigl(q\sqrt{1-z^2}-h|z|\bigr)_+=\frac q2\arctan\frac qh.
\]
On six equal angular sectors \(q=|\sin(\phi-\pi/6)|\), yielding \(\mathbb E_\phi[q\arctan(q/h)]=6K(h)/\pi\). Hence \(\int_{S^2}\ell_6\,d\sigma=12K(h)\) and \(\Pr(N=6)=3K(h)/D(h)\).

**4. Triangles.** Only the two degree-three apices can be isolated by a triangular generic section. Let \(Q_+\) be the tetrahedron obtained by removing the upper apex; let \(s_{Q_+}\) be its support function. Its upper-apex extreme offset gap is \(s_h-s_{Q_+}\); the lower-end gap is obtained by reversing \(u\). The analogous two gaps occur at the lower apex. Thus the total orientation-offset measure of triangular sections equals
\[
4\int_{S^2}(s_h-s_{Q_+})\,d\sigma.
\]
The support function of \(Q_+\) is \(\max(-hz,m\sqrt{1-z^2})\). The positive and negative halves of the \(z\) integral give
\[
 \mathbb E_zs_{Q_+}=\frac h4+\frac\pi8m+\frac14m\arctan\frac mh.
\]
Also \(\mathbb E_\phi m=3\sqrt3/(2\pi)\). Therefore
\[
 \int_{S^2}s_{Q_+}\,d\sigma=D(h)+C,
 \qquad\int_{S^2}s_h\,d\sigma=2D(h).
\]
The triangular measure is \(4[D(h)-C]\), so \(\Pr(N=3)=1-C/D(h)\).

**5. Remaining types and elementary primitives.** Subtracting the triangle probability from the odd-parity identity yields \(\Pr(N=5)=(C-3I)/D\). Subtracting all other types from one gives \(\Pr(N=4)=3(I-K)/D\). Integration by parts followed by \(\tan t\)-substitution evaluates \(I\) and \(K\) as displayed in the finding. Those formulas also agree with the defining nonnegative integrals for every \(h>0\).

**6. Unique optimum.** Put \(c=3\sqrt3/4\), so \(C=\pi c\). Then \(\Pr(N=5)=\pi(h+c)/D(h)-1\). Differentiating the defining integral of \(I\) (or the displayed primitive) gives
\[
 D'(h)=\frac{3h}{\sqrt{1+h^2}}\arctan\frac{\sqrt3h}{\sqrt{1+h^2}}.
\]
Both positive factors increase strictly, so \(D''(h)>0\). The sign of the derivative of the pentagon probability is the sign of
\[
 Q(h)=D(h)-(h+c)D'(h),\quad Q'(h)=-(h+c)D''(h)<0.
\]
Moreover \(D(0+)=\pi c\), \(D'(0+)=0\), \(D(h)=\pi h+O(h^{-1})\), and \(D'(h)=\pi+O(h^{-2})\) as \(h\to\infty\). Hence \(Q(0+)=\pi c>0\) and \(Q(\infty)=-\pi c<0\). Exactly one critical point exists, and it is the strict global maximum. The equation and numerical value follow.

## Verification
Run `python3 checker.py` with Python 3 standard library. The checker uses a separate spherical midpoint integration: for each sampled normal it sorts the five projected vertex heights, tests crossing of the nine actual edges on each of the four open level intervals, and divides the accumulated lengths of three-, four-, five-, and six-sided sections by the accumulated total width. It compares that independent geometric count with the displayed closed formulas for six aspect ratios and checks the numerical optimum locally. A successful execution prints `BIPYRAMID_CROFTON_CHECK_OK comparison_items=30 samples_per_shape=64800`. These finite numerical tests are diagnostics; the proof of the law and uniqueness is the preceding analytical argument.

## Relationship to prior work
Birkemeyer, Brose, Brandenburg and Prün (2026) study the combinatorics, reconstruction behavior and possible face counts of polytope sections; their Section 3 treats bipyramids, but does not derive the invariant-plane four-type probabilities or optimize a pentagon probability. Brandenburg, De Loera and Meroni (2023/2025) establish general slicing-chamber methods and optimize different section criteria, without this invariant integral-geometry law. De Loera, Lopez-Campos and Torres (2024/2026) consider possible section-vertex counts, not the Euclidean-motion-invariant probabilities computed here. The elementary edge-crossing-count observation alone does not imply the spherical integrals or strict optimum. Related exact random-section laws for rectangular boxes, prisms, pyramids and octahedra concern different bodies and do not imply the formula for the five-vertex bipyramid.

## Limitations
The law concerns the one-parameter **right equilateral triangular bipyramid** family and invariant **affine** planes, not arbitrarily skew bipyramids, uniformly oriented **central** planes, or non-invariant choices of offsets. There is no claim of priority over any inaccessible or unindexed earlier derivation of the same four probabilities. The numerical optimizer is an approximation to the uniquely defined implicit exact solution. There is no claim of independent scientific verification.

## References
- A. Birkemeyer, A. E. Brose, M.-C. Brandenburg and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195v1 (first public September 14, 2026), especially Section 3.
- M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1 (2023); Mathematics of Computation 94 (2025), 1003–1042.
- J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419v1 (2024); later journal version 2026.
