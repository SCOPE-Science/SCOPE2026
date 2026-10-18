# Three even moments of random triangle distances determine the triangle

## Finding

Choose independent points \(X,Y\) uniformly from any nondegenerate Euclidean triangle \(T\), and observe only their **unlabeled Euclidean distance** \(D=\|X-Y\|\). Define \(M_k=\mathbb E D^{2k}\) for \(k=1,2,3\). Write \(p,q,r\) for the three squared side lengths and \(e_1=p+q+r\), \(e_2=pq+pr+qr\), \(e_3=pqr\). Then

\[
M_1=\frac{e_1}{18},\qquad
M_2=\frac{e_1^2-2e_2}{60},\qquad
M_3=\frac{23e_1^3}{4200}-\frac{31e_1e_2}{2100}+\frac{e_3}{210}.
\]

Therefore the first **three** even moments determine the three squared side lengths, hence the entire triangle up to congruence and reflection. The cutoff is sharp: the first two moments do not determine triangle shape, even when area is known.

## Assumptions and scope

The triangle is arbitrary and nondegenerate, including acute, right, obtuse, isosceles and equilateral cases. The points are independent and uniform with respect to planar area, not boundary arclength. Distances are absolute Euclidean distances, not normalized by area or perimeter. There is no vertex or side labeling in the observed statistic.

For an exact input triple \((M_1,M_2,M_3)\), reconstruct

\[
e_1=18M_1,\quad e_2=\frac{e_1^2-60M_2}{2},\quad
 e_3=210M_3-\frac{23}{20}e_1^3+\frac{31}{10}e_1e_2.
\]

The squared side lengths are precisely the roots, with multiplicity, of \(z^3-e_1z^2+e_2z-e_3=0\). This gives a complete feasibility criterion: all three roots must be positive real numbers, and their square roots must satisfy every strict triangle inequality. The criterion is necessary and sufficient because such side lengths construct a triangle uniquely up to isometry.

The area \(A\) already follows from two moments by Heron's identity:

\[
16A^2=4e_2-e_1^2.
\]

## Proof

Fix a triangle with vertices \(0,u,v\), where \(\|u\|^2=p\), \(\|v\|^2=q\), and \(\|u-v\|^2=r\). A uniform point has the form \(X=U_1u+U_2v\), where \((U_0,U_1,U_2)\) has the Dirichlet\((1,1,1)\) law; an independent point has coefficients \((V_0,V_1,V_2)\) with the same law. Put \(B=U_1-V_1\) and \(C=U_2-V_2\). The cosine law yields the exact quadratic form

\[
D^2=pB^2+(p+q-r)BC+qC^2.
\]

The Dirichlet integral is explicit for all nonnegative integers \(i,j\):

\[
\mu_{ij}=\mathbb E[U_1^iU_2^j]=\frac{2i!j!}{(i+j+2)!}.
\]

Independence and the binomial theorem give

\[
\mathbb E[B^aC^b]
=\sum_{i=0}^a\sum_{j=0}^b
 (-1)^{a+b-i-j}{a\choose i}{b\choose j}
 \mu_{ij}\mu_{a-i,b-j}.
\]

Substitute this identity into the multinomial expansion of the displayed quadratic form for powers \(k=1,2,3\). Collecting rational coefficients gives

\[
\begin{aligned}
M_1&=(p+q+r)/18,\\
M_2&=(p^2+q^2+r^2)/60,\\
4200M_3&=23(p^3+q^3+r^3)
 +7\sum_{\mathrm{sym}}p^2q-28pqr.
\end{aligned}
\]

Here \(\sum_{\mathrm{sym}}p^2q\) means the six monomials with one squared and one first-power variable. Newton's identities yield the symmetric formulas in the finding. Crucially, the coefficient of \(e_3\) in \(M_3\) is \(1/210\ne0\), so triangular inversion recovers all three elementary symmetric functions without choosing a side ordering. The polynomial with those elementary symmetric coefficients has exactly the squared sides as its roots. The side-side-side congruence theorem completes the inverse proof.

For sharpness, take noncongruent triangles with squared side multisets \((1,4,4)\) and \((2,2,5)\), respectively. Both satisfy strict triangle inequalities. Both have \(e_1=9\) and \(e_2=24\), hence the same first two moments \(M_1=1/2\) and \(M_2=11/20\), as well as the same area \(\sqrt{15}/4\). Their products \(e_3\) are \(16\) and \(20\), so their third moments differ by \(2/105\). Thus two moments are insufficient even when area is also provided. Finally, Heron's identity and the ordinary existence and uniqueness criterion for triangles prove the feasibility statement.

## Verification

Run `python3 check.py` with Python 3 (standard library only). The program independently expands the quadratic form as an exact multivariate polynomial, integrates every term using exact rational Dirichlet moments, checks the three displayed formulas coefficient by coefficient, verifies exact reconstruction and sharpness on six rational squared-side profiles, and compares them against 420000 reproducibly sampled pairs of uniform interior points. It prints `TRIANGLE_PAIR_DISTANCE_MOMENTS_OK` on success. The Monte Carlo checks corroborate the exact algebra; they are not part of the infinite proof.

## Relationship to prior work

Tong, Ahmadi and Pan (2013) derive the **forward** pair-distance density and distribution for a known arbitrary triangle, by a chord-length method. Tong and Pan (2016) derive more general forward polygonal distance distributions using kinematic measure. Those forward constructions subsume the ability to integrate any desired moment *in principle*; they do not give the three triangular moment identities, the exact finite-moment inverse, the sharp two-moment failure, or the realizability criterion established here. The inverse contribution is the finite algebraic identification and cutoff, not a new distance PDF or CDF.

An identity for the first squared-distance moment of two interior-uniform points was previously known. It is not claimed as original. The distinction between a full forward law with known geometry and an explicit finite-moment inverse is substantive but historical priority for equivalent inverse formulations requires broader verification.

## Limitations

Population moments are assumed known exactly. No finite-sample confidence bounds or stable numerical root-finding estimates are established, especially near repeated side lengths or degenerate triangles. The method does not recover position or orientation, only the intrinsic congruence class. It does not handle different point distributions or a single point measured against a fixed vertex. An earlier equivalent finite-moment inversion outside the inspected literature cannot be excluded.

## References

1. F. Tong, M. Ahmadi and J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498 (initial public version, 29 November 2013), https://arxiv.org/abs/1312.2498 .
2. F. Tong and J. Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407 (initial public version, 21 January 2016), https://arxiv.org/abs/1602.03407 .
