# Euclidean Banach–Mazur profile of a classical hexagonal family
## Finding
For every \(\gamma\in[0,1]\), let \(X_\gamma=(\mathbb R^2,\|\cdot\|_\gamma)\) with \(\|(x,y)\|_\gamma=\max\{|y|,|x|+(1-\gamma)|y|\}\). Then \(d_{\mathrm{BM}}(X_\gamma,\ell_2^2)=\sqrt{2/(1+\gamma)}\) for \(0\le\gamma\le1/2\), and \(d_{\mathrm{BM}}(X_\gamma,\ell_2^2)=\sqrt{2/(2-\gamma)}\) for \(1/2\le\gamma\le1\). In particular the distance is uniquely minimized at \(\gamma=1/2\), where it equals \(2/\sqrt3\).

## Assumptions and scope
The scalar field is real. For \(\gamma\in[0,1]\), put \(a=1-\gamma\) and let \(K_\gamma\) be the unit ball of \(X_\gamma\). Then
\[
K_\gamma=\{(x,y): |y|\le1,\ |x+ay|\le1,\ |x-ay|\le1\},
\]
with vertices
\[
\pm(1,0),\qquad \pm(\gamma,1),\qquad \pm(\gamma,-1).
\]
The Banach--Mazur distance from \(X_\gamma\) to \(\ell_2^2\) is equivalently the least \(r\ge1\) for which there is a centered ellipse \(E\) satisfying
\[
E\subseteq K_\gamma\subseteq rE.
\]

## Proof
Write an arbitrary centered ellipse as
\[
E_P=\{u\in\mathbb R^2:u^{\mathsf T}Pu\le1\},
\]
where \(P\) is positive definite, and write \(R=r^2\). For a strip \(|f^{\mathsf T}u|\le1\), the inclusion \(E_P\) in that strip is equivalent to
\[
f^{\mathsf T}P^{-1}f\le1,
\]
or equivalently \(P\succeq ff^{\mathsf T}\). Hence \(E_P\subseteq K_\gamma\) is equivalent to these three positive-semidefinite inequalities for
\[
f_0=(0,1),\qquad f_+=(1,a),\qquad f_-=(1,-a).
\]
The reverse inclusion \(K_\gamma\subseteq rE_P\) is equivalent, by convexity, to
\[
v^{\mathsf T}Pv\le R
\]
for every vertex \(v\) of \(K_\gamma\).

The body \(K_\gamma\) is invariant under both coordinate reflections. If \(P\) is feasible with a given \(R\), conjugating \(P\) by either reflection remains feasible. Averaging the four conjugates preserves all positive-semidefinite strip constraints and all vertex inequalities, and yields a diagonal matrix. Thus an optimal ellipse may be taken with
\[
P=\operatorname{diag}(p,q).
\]
The inner-containment conditions then reduce to
\[
q\ge1,\qquad \frac1p+\frac{a^2}{q}\le1.
\]
For fixed \(q\), decreasing \(p\) can only improve the outer containment, so at an optimum
\[
p=\frac{q}{q-a^2}.
\]
The two distinct outer-vertex constraints are therefore
\[
R\ge p(q),\qquad R\ge F(q):=\gamma^2p(q)+q,
\]
where
\[
p(q)=\frac{q}{q-a^2},\qquad q\ge1.
\]
Here \(p(q)\) is decreasing. Moreover
\[
F'(q)=1-\frac{\gamma^2a^2}{(q-a^2)^2}>0
\]
for \(q\ge1\) and \(0<\gamma<1\), because \(q-a^2\ge1-a^2=\gamma(2-\gamma)>\gamma a\). The endpoint cases follow directly by continuity or the same inequalities.

The unique crossing of \(p(q)\) and \(F(q)\) occurs at
\[
q=2a=2(1-\gamma).
\]
If \(0\le\gamma\le1/2\), this crossing lies in the feasible range \(q\ge1\), so the minimum of \(\max\{p(q),F(q)\}\) occurs there and
\[
R=\frac{2}{1+\gamma}.
\]
If \(1/2\le\gamma\le1\), the crossing lies at or below \(1\); throughout the feasible range \(F(q)\ge p(q)\), and the increasing function \(F\) is minimized at \(q=1\). Hence
\[
R=F(1)=\frac{2}{2-\gamma}.
\]
Taking square roots gives the stated Banach--Mazur distance.

The first branch strictly decreases and the second strictly increases, so the unique minimum occurs at \(\gamma=1/2\). Both formulas then give
\[
d_{\mathrm{BM}}(X_{1/2},\ell_2^2)=\frac{2}{\sqrt3}.
\]

## Verification
The optimization ranges over every centered ellipse; axis alignment is derived from the reflection symmetries by convex averaging and is not assumed. The strip criterion follows from the exact support function of an ellipsoid, and the outer constraint is checked on all vertices of the polytope. The resulting one-variable minimization is exact.

At \(\gamma=0\) and \(\gamma=1\), the family is respectively \(\ell_1^2\) and \(\ell_\infty^2\), and both branches give the classical value \(\sqrt2\). The source also records the isometric duality \(X_\gamma^*\cong X_{1-\gamma}\); the displayed distance formula has the same symmetry, as finite-dimensional Banach--Mazur distance is invariant under duality.

No numerical experiment, finite enumeration, or unproved optimization ansatz is used in the proof.

## Relationship to prior work
Martín and Merí introduced exactly this one-parameter family and computed its numerical index. Their full article gives the norm, its six extreme points, and the duality \(X_\gamma^*\cong X_{1-\gamma}\), but contains no Banach--Mazur-distance calculation. Chica and Merí later computed the rank-one numerical index for the same family; their full preprint likewise contains no Banach--Mazur-distance calculation.

Praetorius studied distance ellipsoids and contact configurations in finite-dimensional Banach spaces. The accessible abstract and bibliographic record do not state this hexagonal profile; a full-text comparison could not be completed in the bounded access attempt and is therefore retained as a residual literature risk.

Lassak determined the Banach--Mazur distance between a parallelogram and an affine-regular hexagon, and more generally compared a parallelogram with affine-regular even-gons. That is a different two-body distance problem and does not give the Euclidean distance profile of the present deformation.

Grundbacher and Kobos give a general characterization of distance ellipsoids and planar uniqueness results. Those results provide a broad framework for checking optimal ellipses, but the inspected full text does not state this one-parameter formula; obtaining the displayed profile still requires solving the concrete contact/containment optimization carried out above.

## Limitations
The originality comparison is bounded by accessible literature and indexing. In particular, the full text of Praetorius's 2002 paper was not successfully retrieved during the bounded source check, so an older equivalent computation under distance-ellipsoid terminology remains a residual risk. The mathematical proof of the formula does not depend on that source.

The claim concerns only the real two-dimensional family \(X_\gamma\) and its distance to the Euclidean plane. It does not assert a formula for arbitrary centrally symmetric hexagons or for distances between two non-Euclidean members of the family.

## References
1. M. Martín and J. Merí, “Numerical index of some polyhedral norms on the plane,” Linear and Multilinear Algebra 55 (2007), 175–190. DOI: 10.1080/03081080600628323.
2. M. Chica and J. Merí, “Rank-1 numerical index of some families of norms on the plane,” Linear and Multilinear Algebra 63 (2015), 1817–1828. DOI: 10.1080/03081087.2014.975670.
3. D. Praetorius, “Remarks and examples concerning distance ellipsoids,” Colloquium Mathematicum 93 (2002), 41–53. DOI: 10.4064/cm93-1-5.
4. M. Lassak, “Banach–Mazur Distance from the Parallelogram to the Affine-Regular Hexagon and Other Affine-Regular Even-Gons,” Results in Mathematics 76 (2021), article 62. DOI: 10.1007/s00025-021-01368-8.
5. F. Grundbacher and T. Kobos, “On certain extremal Banach–Mazur distances and Ader's characterization of distance ellipsoids,” Mathematika 72 (2026), e70062. DOI: 10.1112/mtk.70062.
