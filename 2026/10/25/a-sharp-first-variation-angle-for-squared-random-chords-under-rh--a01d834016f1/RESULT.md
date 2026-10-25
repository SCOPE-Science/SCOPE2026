# A sharp first-variation angle for squared random chords under rhombus truncation

## Finding
Let \(u,v\in\mathbb R^2\) be unit vectors with \(\det(u,v)>0\), put \(c=\langle u,v\rangle\in(-1,1)\), and, for \(0\le t<1\), define the convex polygon
\[
K_t=\operatorname{conv}\{0,u,u+(1-t)v,(1-t)u+v,v\}.
\]
Thus \(K_0\) is a unit-sided rhombus and every \(K_t\) with \(0<t<1\) is a genuine pentagon made by truncating one corner. For independent area-uniform points \(I_t,I_t'\) and independent arclength-uniform boundary points \(B_t,B_t'\), let
\[
\mathcal R(t,c)=\frac{\mathbb E\|B_t-B_t'\|^2}{\mathbb E\|I_t-I_t'\|^2}.
\]
Then, for every \(-1<c<1\),
\[
\mathcal R(0,c)=2,\qquad
\partial_t\mathcal R(0^+,c)=\frac{(\sqrt{2-2c}-2)(1+3c)}4.
\]
Consequently, for every \(c<-1/3\), all sufficiently small positive truncations have \(\mathcal R(t,c)>2\), while for every \(c>-1/3\), all sufficiently small positive truncations have \(\mathcal R(t,c)<2\). The threshold \(c=-1/3\) is exactly the zero of the first variation; no higher-order sign is claimed there.

An explicit integer-coordinate strictly convex pentagon, in counterclockwise order, has vertices
\[
(0,0),\ (5070,0),\ (1619,3480),\ (1331,3600),\ (-3570,3600).
\]
For this pentagon the exact amplification is
\[
\mathcal R=\frac{3586477854403938963}{1792478301783239474}
=2+\frac{1521250837460015}{1792478301783239474}>2.
\]
In particular, the factor-two upper bound suggested by the equality of all rhombi (and of disks) does **not** hold for all planar convex bodies. This is an upper-bound counterexample for the squared-distance ratio, not a counterexample to the boundary-versus-interior *lower* moment inequality.

## Assumptions and scope
The Euclidean norm, planar Lebesgue area, and one-dimensional Euclidean arclength on the boundary are used throughout. All four random points in the definition of \(\mathcal R\) are independent within their respective pairs. The body is nondegenerate because \(\det(u,v)>0\). The parameter \(t\) measures the common fraction removed from the two incident unit edges; the new edge has length \(t\sqrt{2-2c}\). The assertion about the sign concerns a right-hand neighbourhood of \(t=0\), not all \(0<t<1\). The theorem does not determine the best amplification over all convex polygons.

## Proof
For any independent identically distributed Euclidean random points \(X,X'\) with finite second moments,
\[
\mathbb E\|X-X'\|^2=2\bigl(\mathbb E\|X\|^2-\|\mathbb EX\|^2\bigr)=2\operatorname{Var}(X).
\]
Put \(q=u+v\) and \(m=q/2\). For the rhombus \(K_0\), an area-uniform point has the representation \(m+Su+Tv\), where \(S,T\) are independent uniform variables on \([-1/2,1/2]\). Hence \(\operatorname{Var}(I_0)=1/6\). Every rhombus edge has length one. On each edge, the displacement from \(m\) is of the form \(\pm u/2+Tv\) or \(\pm v/2+Su\), with a uniform coordinate and vanishing cross term after integration. The boundary mean is \(m\) by central symmetry and \(\operatorname{Var}(B_0)=1/3\). Thus \(\mathcal R(0,c)=2\).

The removed corner triangle has vertices \(q,q-tu,q-tv\), hence area \(t^2\det(u,v)/2\); its area fraction in the rhombus is \(t^2/2\). Because every squared distance and coordinate remains bounded as \(t\to0\), removing this triangle alters the interior mean and its raw second moment by \(O(t^2)\). Consequently
\[
\operatorname{Var}(I_t)=\frac16+O(t^2).
\]
Write \(h=\|u-v\|=\sqrt{2-2c}<2\). Truncation removes two boundary segments of length \(t\) and replaces them with a segment of length \(ht\). Its perimeter is \(P_t=4+(h-2)t\). Measured from \(m\), the two deleted segments and the added segment all lie at \(q/2+O(t)\). Therefore the total *unnormalized* boundary first moment from \(m\) is \(O(t)\), whose squared normalized contribution is \(O(t^2)\), while its unnormalized second moment is
\[
G_t=\frac43+(h-2)t\left\|\frac q2\right\|^2+O(t^2)
=\frac43+\frac{(h-2)(1+c)}2t+O(t^2).
\]
Division by the exact perimeter gives
\[
\operatorname{Var}(B_t)=\frac13+\frac{(h-2)(1+3c)}{24}t+O(t^2).
\]
Taking the variance ratio proves
\[
\mathcal R(t,c)=2+\frac{(h-2)(1+3c)}4t+O(t^2),
\]
with the stated sign dichotomy because \(h<2\). This proof is uniform only for fixed nondegenerate \(c\); no endpoint uniformity at \(c=\pm1\) is asserted.

For the explicit pentagon choose \(u=(169,0)\), \(v=(-119,120)\) (both have length \(169\)), take \(t=1/30\), and multiply all coordinates by \(30\). The edge lengths are \(5070,4901,312,4901,5070\), and all oriented consecutive turns are strictly positive. Green's polygon moment formulas and the line-segment moment formulas yield, respectively,
\[
\operatorname{area}(K)=18241860,\quad \operatorname{per}(K)=20254,
\]
\[
\mathbb E\|I-I'\|^2=\frac{249594896357833}{29127609},\qquad
\mathbb E\|B-B'\|^2=\frac{62426829204649}{3641046}.
\]
Their exact quotient is the rational number displayed in the finding. The standalone checker derives both moments afresh from the integer vertices without floating-point arithmetic and compares the quotient with an independent analytic truncation formula.

## Verification
Run `python3 verify_chord_pentagon.py` using Python's standard library. The checker verifies strict convexity, exact edge lengths, perimeter, area, arclength-weighted boundary centroid and second moment, area-weighted interior centroid and second moment, the exact rational inequality, and equality with the analytic removal/addition computation. It also checks the sign and finite-difference approach to the predicted first derivative at the rational sample angle. The finite-difference tests supplement, but do not replace, the analytic first-variation proof.

## Relationship to prior work
Tokmachev's 2026 convex-order work establishes a boundary-versus-interior *lower* comparison under coincident area and boundary centroids. Lotnikov's 2026 study derives relations for second moments of centrally symmetric tangential bodies and studies lower comparisons. Our factor-two question is an *upper* amplification question; neither lower comparison entails an upper bound, and the result supplies a one-corner-breaking mechanism not covered by centrally symmetric formulas. The known indexed fourth-chord-moment profile for parallelograms concerns exponent four and untruncated centrally symmetric bodies, not the exponent-two pentagon first variation. The indexed exact triangular second-moment result concerns a different polygon class and comparison. No claim is made concerning an optimal upper constant for all convex bodies.

## Limitations
The derivative vanishes at \(c=-1/3\); the sign at that exact angle and at non-infinitesimal truncation size is not classified. The explicit example exceeds two by less than one part in a thousand; exact arithmetic is essential to distinguish its sign. The mathematical literature outside the retrieved sources may contain equivalent upper-ratio counterexamples. No independent audit has been performed.

## References
1. A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869v1, first submitted 2026-07-09, https://arxiv.org/html/2607.08869v1.
2. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848, first submitted 2026-08-14, https://arxiv.org/abs/2608.14848.
3. G. Bonnet, A. Gusakova, C. Thäle and D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, Adv. Math. 386 (2021), 107813, https://doi.org/10.1016/j.aim.2021.107813.
