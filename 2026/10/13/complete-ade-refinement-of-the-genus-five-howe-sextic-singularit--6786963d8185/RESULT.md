# Complete ADE refinement of the genus-five Howe sextic singularity table

## Finding
Let \(k\) be an algebraically closed field of characteristic \(0\) or characteristic at least \(5\). Let
\[
\phi_1(x)=\prod_{i=1}^4(x-\alpha_i),\qquad
\phi_2(x)=\prod_{i=1}^4(x-\beta_i),
\]
where the eight branch points are pairwise distinct, and let \(\widetilde C\subset\mathbb P^2_k\) be the projective closure of Kudo's sextic
\[
f(x,y)=y^4-2\bigl(\phi_1(x)+\phi_2(x)\bigr)y^2+\bigl(\phi_1(x)-\phi_2(x)\bigr)^2.
\]
Write \(d_i=\sigma_i-\tau_i\), where \(\sigma_i\) and \(\tau_i\) are the elementary symmetric functions in the \(\alpha\)'s and \(\beta\)'s, and set
\[
h_1(x)=d_1x^3-d_2x^2+d_3x-d_4.
\]
Then every singularity in Kudo's seven strata is an ADE singularity of type \(A_1\), \(A_3\), or \(A_5\). More precisely, the complete baskets are
\[
\begin{array}{c|c}
\text{stratum}&\text{singularity basket}\\ \hline
\mathrm{I\!-1}&3A_1+A_3\\
\mathrm{I\!-2}&A_1+2A_3\\
\mathrm{I\!-3}&A_3+A_5\\
\mathrm{II\!-1}&3A_1+A_3\\
\mathrm{II\!-2}&A_1+2A_3\\
\mathrm{II\!-3}&A_1+2A_3\\
\mathrm{II\!-4}&A_3+A_5.
\end{array}
\]
Thus the generic member has three nodes and one tacnode, not four nodes. In every stratum the sum of the local \(\delta\)-invariants is \(5\), exactly the genus defect \(10-5\) of a plane sextic whose normalization is the genus-five Howe curve.

## Assumptions and scope
The statement concerns exactly the plane sextic model of Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, for the case of two genus-one double covers with no common ramification point. The characteristic restriction and the pairwise-distinctness hypothesis are the source's hypotheses. The result refines the source's multiplicity-two classification; it does not address the distinct sextic model treated in Moriya--Kudo, part I.

Kudo's strata are as follows. In type I, \(d_1\ne0\), and the affine singularities correspond to the roots of the cubic \(h_1\): three simple roots in I-1, one double plus one simple root in I-2, and one triple root in I-3. In type II, \(d_1=0\). If \(d_2\ne0\), the affine roots are two simple roots in II-1 or one double root in II-2; if \(d_2=0\) and \(d_3\ne0\), II-3 has one simple affine root; if \(d_2=d_3=0\), II-4 has no affine root. The point \(P_\infty=(0:1:0)\) is always singular, while \(Q_\infty=(1:0:0)\) is singular exactly when \(d_1=0\).

## Proof
Put \(a(x)=\phi_1(x)+\phi_2(x)\) and \(b(x)=\phi_1(x)-\phi_2(x)=-h_1(x)\). Let \((\xi:0:1)\) be an affine singular point, so \(b(\xi)=0\). Because the two branch sets are disjoint, \(\phi_1(\xi)=\phi_2(\xi)\ne0\), hence \(a(\xi)\ne0\). In local coordinates \(u=x-\xi\), \(v=y\),
\[
f=b(\xi+u)^2-2a(\xi+u)v^2+v^4.
\]
The second derivative in the \(v\)-direction is a unit at the origin. The formal Morse lemma therefore gives an analytic change of coordinates reducing the germ to
\[
V^2+b(\xi+u)^2.
\]
If \(\xi\) has multiplicity \(m\in\{1,2,3\}\) as a root of \(h_1\), then \(b(\xi+u)=u^m\varepsilon(u)\) with \(\varepsilon(0)\ne0\). Since \(2m\in\{2,4,6\}\) is prime to the allowed characteristics, a unit can be absorbed into a local coordinate, giving
\[
V^2-U^{2m}=0.
\]
Thus a simple, double, or triple root of \(h_1\) gives respectively \(A_1\), \(A_3\), or \(A_5\).

For the points at infinity, let \(\Phi_i(X,Z)\) be the degree-four homogenization of \(\phi_i\), and define the homogeneous cubic
\[
D(X,Z)=\frac{\Phi_1(X,Z)-\Phi_2(X,Z)}{Z}
=-d_1X^3+d_2X^2Z-d_3XZ^2+d_4Z^3.
\]
The homogeneous sextic is
\[
F(X,Y,Z)=Y^4Z^2-2\bigl(\Phi_1(X,Z)+\Phi_2(X,Z)\bigr)Y^2+D(X,Z)^2.
\]
At \(P_\infty\), use the chart \(Y=1\) with \(r=X/Y\), \(s=Z/Y\). Then
\[
G_P(r,s)=s^2-2\bigl(\Phi_1(r,s)+\Phi_2(r,s)\bigr)+D(r,s)^2.
\]
Here \(\Phi_1(r,0)+\Phi_2(r,0)=2r^4\), while \(D\) is homogeneous of degree three. Since the coefficient of \(s^2\) is a unit, formal Morse reduction in \(s\) yields \(S^2+g(r)\). The critical section satisfies \(s=O(r^3)\), so
\[
g(r)=-4r^4+O(r^6).
\]
Hence \(P_\infty\) is always of type \(A_3\).

Suppose now that \(Q_\infty\) occurs, equivalently \(d_1=0\). On the chart \(X=1\), put \(v=Y/X\) and \(s=Z/X\). The local equation is
\[
G_Q(v,s)=v^4s^2-2\bigl(\Phi_1(1,s)+\Phi_2(1,s)\bigr)v^2+D(1,s)^2,
\]
where \(\Phi_1(1,0)+\Phi_2(1,0)=2\) and
\[
D(1,s)=d_2s-d_3s^2+d_4s^3.
\]
The \(v^2\)-coefficient is a unit, and the unique critical section in the \(v\)-direction is \(v=0\). Thus the germ reduces to \(V^2+D(1,s)^2\). Consequently \(Q_\infty\) is \(A_1\) when \(d_2\ne0\), \(A_3\) when \(d_2=0\) and \(d_3\ne0\), and \(A_5\) when \(d_2=d_3=0\); in the last case \(d_4\ne0\) by pairwise distinctness of the branch points.

Combining these local normal forms with the seven root-multiplicity strata gives the displayed table. Finally, \(\delta(A_1)=1\), \(\delta(A_3)=2\), and \(\delta(A_5)=3\). Every listed basket therefore has total \(\delta=5\), agreeing with the source's normalization of genus \(5\) and the arithmetic genus \(10\) of a plane sextic.

## Verification
The accompanying exact symbolic checker reconstructs the source equation from formal symmetric-difference parameters, verifies the affine local reduction data, checks the leading form at \(P_\infty\), checks the three possible orders of \(D(1,s)\) at \(Q_\infty\), and verifies all seven basket and \(\delta\)-sum entries. It is a finite algebraic consistency check; the all-parameter proof is the local argument above.

## Relationship to prior work
Kudo proves that the sextic is irreducible, identifies all singular points, proves that every singularity has multiplicity two, and gives the seven strata by the root pattern of \(h_1\). In the generic stratum the source states only that there are four double points, three affine and one at infinity. It does not identify the ADE analytic types. The companion part-I paper does use the word “tacnode” for a different sextic construction and proves that certain special double points need at least two blowups, but it does not imply the present seven-stratum classification for Kudo's part-II family. The result here is therefore a local-analytic refinement of the part-II singularity table rather than a new construction of the sextic.

## Limitations
The result is restricted to the source's characteristic range and to pairwise-disjoint branch sets. It classifies the completed local plane-curve singularities but does not compute their embedded resolution graphs beyond what follows from the \(A_n\) types, nor does it classify projective equivalence among parameter choices. A residual originality risk is that an equivalent ADE refinement may occur in literature indexed only under Howe-curve or singularity terminology not found in the searches described in the review.

## References
1. Momonari Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760v1 (2024); Journal of Computational Algebra 11 (2024), 100019; DOI: 10.1016/j.jaca.2024.100019.
2. Tomoki Moriya and Momonari Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993v1 (2023); Journal of Computational Algebra 11 (2024), 100018; DOI: 10.1016/j.jaca.2024.100018.
