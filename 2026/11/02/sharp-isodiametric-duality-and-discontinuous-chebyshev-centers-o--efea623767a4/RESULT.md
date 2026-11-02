# Sharp isodiametric duality and discontinuous Chebyshev centers of rectangular flat Möbius bands

## Finding

For the rectangular flat Möbius band \(M_{L,w}\), the intrinsic diameter \(D\) and intrinsic Chebyshev radius \(R\) admit complete, piecewise elementary formulas. In particular, its area \(S=2wL\) satisfies the sharp inequality
\[
D^2\ge\frac{4\sqrt3}{9}S,
\]
with equality for precisely the **two** nonisometric aspect ratios \(2w/L=1/\sqrt3\) and \(2w/L=\sqrt3\). A reciprocal symmetry of the normalized squared diameter exchanges the equality cases. A different transition occurs in the set of intrinsic Chebyshev centers: as \(w\) increases through \(7\sqrt{15}L/30\), the minimizing transverse coordinate jumps discontinuously from the core to an off-core circle.

More explicitly, putting \(r=2w/L\),
\[
D=\frac{L(1+r^2)}{2\max\{1,r\}},\qquad
\frac{D^2}{S}=\frac{(1+r^2)^2}{4r\max\{1,r\}^2}.
\]
The Chebyshev radius is
\[
R=\begin{cases}
\sqrt{L^2/4+w^2},&0<w\le 7\sqrt{15}L/30,\\
\bigl(3\sqrt{w^2+2L^2}-w\bigr)/4,&w\ge7\sqrt{15}L/30.
\end{cases}
\]
At the transition both branches equal \(4L/\sqrt{15}\), but their one-sided derivatives with respect to \(w\) are \(7/8\) and \(2/13\). Below the transition all Chebyshev centers lie on the central core; above it they lie on the transverse level \(|y|=(w+\sqrt{w^2+2L^2})/4\); at the transition both loci occur. Thus the optimal-center locus changes discontinuously, even though the radius is continuous.

## Assumptions and scope

Let \(L,w>0\), and let \(M_{L,w}\) be the compact flat length-metric quotient
\[
\bigl(\mathbb R\times[-w,w]\bigr)/\langle g\rangle,
\qquad g(x,y)=(x+L,-y).
\]
The ambient strip is endowed with Euclidean length and includes its horizontal boundary; the quotient has area \(S=2wL\). All distances, diameters and centers are **intrinsic** (not ambient distances of a physical embedding). Write \(e(p)=\max_{q\in M_{L,w}}d(p,q)\), \(D=\max_p e(p)\), and \(R=\min_p e(p)\). Translation along the longitudinal coordinate is an isometry, and reflection in the core allows any source to be represented as \(p=[(0,u)]\) with \(0\le u\le w\).

For \(0\le t\le L\), \(-w\le v\le w\), the exact distance to \(q=[(t,v)]\) is
\[
d(p,q)^2=\min\{t^2+(v-u)^2,\ (L-t)^2+(v+u)^2\}.
\]
The set of Chebyshev centers is interpreted as a subset of this quotient, not just as a transverse-coordinate value.

## Proof

**1. The exact point-eccentricity profile.** An even deck transformation acts by longitudinal translation through a multiple of \(2L\); an odd one flips the transverse coordinate and translates by an odd multiple of \(L\). For \(t\in[0,L]\) the two closest possibilities are the two expressions above. The Euclidean strip is convex, so the realizing line segment stays in the strip, giving equality in the distance formula.

The squared-distance function is the minimum of two convex quadratics on the rectangle \([0,L]\times[-w,w]\). Their equality locus (the Voronoi bisector) is
\[
t=\frac L2+\frac{2uv}{L}.
\]
Partition the rectangle by this line. On each convex polygon the active squared distance is a convex quadratic, so a maximum is attained at a polygon vertex. Thus only rectangle corners and intersections of the bisector with rectangle sides must be evaluated.

Put \(c=L^2/4\). When \(uw\le c\), the bisector meets the top and bottom sides. The greatest squared distance on the bisector is \(L^2/4+w^2+u^2+4u^2w^2/L^2\). The largest corner squared-distance is \((w+u)^2\); their difference is \((L/2-2uw/L)^2\), which is nonnegative. Consequently
\[
e(u)^2=\frac{L^2}{4}+w^2+u^2+\frac{4u^2w^2}{L^2}\qquad(uw\le L^2/4).
\]
When \(uw\ge c\), the bisector meets the two vertical sides. Its squared distance there is \((u+c/u)^2\); the greatest corner squared distance is \(L^2+(w-u)^2\). Consequently
\[
e(u)=\max\left\{u+\frac{L^2}{4u},\ \sqrt{L^2+(w-u)^2}\right\}\qquad(uw\ge L^2/4).
\]
These expressions agree at the threshold \(uw=L^2/4\). They therefore give the full eccentricity function, including every source location and every positive aspect ratio.

**2. Intrinsic diameter.** If \(w\le L/2\), only the first branch is present and is increasing with \(u\); its maximum is \(e(w)=L/2+2w^2/L\). If \(w>L/2\), the first branch increases to \(u_0=L^2/(4w)\). On the second branch set \(A(u)=u+c/u\), \(B(u)=\sqrt{L^2+(w-u)^2}\). An exact factorization gives
\[
A(u)^2-B(u)^2=\left(2u-w-\frac cu\right)\left(w-\frac cu\right).
\]
For \(u>u_0\), the second factor is positive and the first changes sign once, at
\[
u_*=(w+\sqrt{w^2+2L^2})/4\in(L/2,w).
\]
Thus \(e(u)=B(u)\) decreases on \([u_0,u_*]\), while \(e(u)=A(u)\) increases on \([u_*,w]\). The two endpoint maxima coincide:
\[
e(u_0)=e(w)=w+\frac{L^2}{4w}.
\]
This proves the stated two-branch diameter, the location of the farthest sources, and the reciprocal closed form for \(D\).

**3. Isodiametric inequality and distinct equality shapes.** With \(r=2w/L\), direct substitution gives
\[
\frac{D^2}{S}=F(r)=\frac{(1+r^2)^2}{4r\max\{1,r\}^2},\quad F(r)=F(1/r).
\]
For \(0<r\le1\), \(4F(r)=r^{-1}+2r+r^3\). Its derivative is \(-r^{-2}+2+3r^2\), which has the unique positive zero \(r=1/\sqrt3\) and changes sign from negative to positive. The reciprocal symmetry gives the unique minimizer \(r=\sqrt3\) on \([1,\infty)\). Both attain \(4\sqrt3/9\), while \(F(1)=1\), proving the sharp inequality and the exact equality set. At a fixed area the two equality surfaces have different core lengths \(L\). Their systoles (shortest noncontractible closed-geodesic lengths) are exactly these different lengths, so the two surfaces are not isometric.

**4. Chebyshev radius and the center-locus transition.** The first eccentricity branch is strictly increasing on \([0,\min\{w,u_0\}]\), with minimum at the core \(u=0\):
\[
R_{\mathrm{core}}=e(0)=\sqrt{L^2/4+w^2}.
\]
If \(w\le L/2\), this is the global minimum. If \(w>L/2\), the factorization in step 2 proves that the second branch decreases to \(u_*\) and increases thereafter. Hence there are exactly two candidate transverse minimizers, \(u=0\) and \(u=u_*\), the latter having eccentricity
\[
R_{\mathrm{off}}=e(u_*)=\frac{3\sqrt{w^2+2L^2}-w}{4}.
\]
The difference \(R_{\mathrm{core}}-R_{\mathrm{off}}\) is strictly increasing for \(w\ge L/2\): its derivative is
\[
\frac{w}{\sqrt{w^2+L^2/4}}-\frac14\left(\frac{3w}{\sqrt{w^2+2L^2}}-1\right)>0,
\]
because the first term is at least \(1/\sqrt2\) and the second term is less than \(1/2\). The difference is negative at \(w=L/2\), and tends to a positive limit or grows positively as \(w\to\infty\). It vanishes exactly at \(w_c=7\sqrt{15}L/30\), as direct substitution shows. There \(u_*=\sqrt{15}L/6\), both radii equal \(4L/\sqrt{15}\), and the one-sided derivatives are \(7/8\) and \(2/13\). The optimizer therefore changes from the core to the off-core locus discontinuously; both are optimal only at equality.

## Verification

The supplied `verify.py` runs without external dependencies. It checks 82,620 sampled source-target distances against the proved eccentricity formula; constructs and checks 1,836 explicit maximizing witnesses; checks 36 diameter and Chebyshev-radius aspect configurations; and tests the reciprocal isodiametric identity and sharp lower bound at 10,000 randomized aspect ratios. All checks passed. These finite tests supplement, but do not replace, the universally quantified analytic proof above. Reproduce with `python verify.py` from a directory containing the script.

## Relationship to prior work

Classical geometry of flat Möbius bands focuses principally on systoles, transverse height and area: Blatter studied global Riemannian geometry of the band; Sabourau and Yassine prove optimal Finsler systolic inequalities; later stability work addresses those inequalities. Sabitov treats isometric immersion and embedding of flat bands into Euclidean spaces. These results involve the same underlying quotient or geometric setting, but do not themselves state the above complete point-eccentricity profile, exact intrinsic diameter, two-shape sharp isodiametric inequality or discontinuous Chebyshev-center transition. Searches also compared general diameter and polygonal farthest-distance results; those have different metric spaces and cannot imply this classification by parameter substitution. This distinction is based on the inspected material, not a proof that no earlier formulation exists.

## Limitations

The theorem applies only to intrinsic flat rectangular Möbius bands with both boundary components inherited from the strip edges (which form one boundary circle after quotient). It does not optimize over arbitrary Riemannian/Finsler metrics, curved or smoothly embedded physical strips, and does not address extrinsic Euclidean diameter. The historical-priority comparison was not exhaustive: an older treatment of diameter or covering radii for a flat Möbius band could contain an equivalent result. No independent mathematical audit has been performed.

## References

- C. Blatter, “Zur Riemannschen Geometrie im Grossen auf dem Möbiusband”, *Compositio Mathematica* **15** (1962–1964), 88–107. https://www.numdam.org/item/CM_1962-1964__15__88_0/
- I. Kh. Sabitov, “Isometric immersions and embeddings of a flat Möbius strip in Euclidean spaces”, *Izvestiya: Mathematics* **71** (2007), 1049–1078. https://doi.org/10.1070/IM2007v071n05ABEH002376
- Stéphane Sabourau and Zeina Yassine, “Optimal systolic inequalities on Finsler Möbius bands”, arXiv:1503.01282 (initial public preprint dated 2015-03-04). https://arxiv.org/abs/1503.01282
- S. Eyll, “Stability of Systolic Inequalities for Möbius Strip and Klein Bottle”, *Journal of Geometric Analysis* (2025). https://doi.org/10.1007/s12220-025-02197-9
