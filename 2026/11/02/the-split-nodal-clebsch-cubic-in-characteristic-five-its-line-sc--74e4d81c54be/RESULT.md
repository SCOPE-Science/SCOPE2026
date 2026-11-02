# The split nodal Clebsch cubic in characteristic five: its line scheme and zeta function

## Finding
Let \(R=\mathbb Z_{(5)}\). In the hyperplane \(\sum_{i=0}^{4}X_i=0\) in \(\mathbb P^4_R\), let \(\mathcal X\) be the cubic \(\sum_{i=0}^{4}X_i^3=0\), and set \(X=\mathcal X_{\mathbb F_5}\). Then \(X\) has exactly one geometric singularity, the ordinary node \(P=[1:1:1:1:1]\). Its minimal resolution is \(\operatorname{Bl}_{B}\mathbb P^2_{\mathbb F_5}\), where \(B\) is the entire set of six \(\mathbb F_5\)-points of a smooth conic. The exceptional conic is contracted to \(P\).

The relative Fano scheme of lines \(F_1(\mathcal X/R)\) is finite flat of degree \(27\) over \(R\). Its special fiber has exactly \(21\) geometric support points, all rational over \(\mathbb F_5\): fifteen reduced points and six with local ring \(\mathbb F_5[\epsilon]/(\epsilon^2)\). The six double points represent the lines through \(P\), while the fifteen simple points represent lines avoiding \(P\). Thus, twelve of the twenty-seven geometric characteristic-zero lines merge pairwise in characteristic five.

For every integer \(m\ge1\), put \(q=5^m\). Then
\[
\#X(\mathbb F_q)=q^2+6q+1,
\qquad
Z(X/\mathbb F_5,T)=\frac1{(1-T)(1-5T)^6(1-25T)}.
\]
All twenty-one reduced lines are defined over \(\mathbb F_5\), hence over each \(\mathbb F_q\).

## Assumptions and scope
The stated Fano scheme is the Hilbert scheme of projective lines contained in the **specified integral model** \(\mathcal X\), not the line scheme of an arbitrary cubic or the Fano variety of its minimal resolution. All local rings in the special-fiber assertion are geometric or \(\mathbb F_5\)-rational Artin local rings as indicated. The point-count formula is for the singular projective surface \(X\), not its resolution. The generic fiber is the classical smooth Clebsch diagonal cubic surface.

## Proof
**(1) Unique node and the six-point blowup.** In characteristic five write
\[
(X_0,X_1,X_2,X_3,X_4)=(T,T+a,T+b,T+c,T-a-b-c).
\]
The hyperplane equation holds automatically, and the cubic becomes, after dividing by \(3\in\mathbb F_5^\times\),
\[
TQ(a,b,c)=H(a,b,c),\quad
Q=a^2+b^2+c^2+(a+b+c)^2,\quad
H=(a+b)(b+c)(c+a).
\]
The quadratic form \(Q\) has matrix \(I_3+J_3\), with determinant \(4\ne0\) in \(\mathbb F_5\). The tangent-cone equation at \(P=[1:0:0:0]\) is therefore a nondegenerate quadratic cone. There are no other singularities: the partial derivatives of \(\sum X_i^3\), restricted to \(\sum X_i=0\), can simultaneously vanish only when all five squared coordinates agree. Thus each \(X_i\) is a common scalar times a sign; the signed sum of five signs is zero modulo five only when all signs agree. This gives \(P\).

On the line \(a+b=0\), the equation \(Q=0\) is \(2(a^2+c^2)=0\), giving \(c=\pm2a\). The other two factors of \(H\) give analogous pairs. The resulting six points are distinct and transverse, and because a smooth plane conic has precisely six rational points over \(\mathbb F_5\), their intersection \(B=V(Q,H)\) is all of \(Q(\mathbb F_5)\). In projective \([a:b:c]\) coordinates, explicitly,
\[
B=\{[1:2:3],[1:2:4],[1:3:2],[1:3:4],[1:4:2],[1:4:3]\}.
\]
Projection from \(P\) has inverse given by the four cubics
\[
[a:b:c]\dashrightarrow[T:a':b':c']=[H:aQ:bQ:cQ].
\]
Their base locus is exactly the reduced complete intersection \(B\). Blowing up \(B\) resolves this map. The strict transform of \(Q\) has class \(2h-\sum E_i\), self-intersection \(-2\), and anticanonical degree zero, hence contracts to the sole node. The morphism from the blowup is the minimal resolution \(Y\to X\).

**(2) The twenty-one lines.** The six exceptional curves \(E_i\) map to six distinct lines through \(P\). A line not through the node has irreducible smooth strict transform \(D\subset Y\) satisfying \((-K_Y)D=1\) and \(D^2=-1\). Write its plane image as a curve of degree \(d\ge1\) with multiplicities \(m_i\ge0\) at \(B\). The equalities are
\[
3d-\sum_i m_i=1,\qquad d^2-\sum_i m_i^2=-1.
\]
Cauchy–Schwarz yields \(d\le2\). For \(d=1\) the only solutions are lines through exactly two base points, giving fifteen curves \(h-E_i-E_j\). For \(d=2\) the class would be a conic through five of the six points. The only such conic is \(Q\), which also passes through the sixth point, so that class has no irreducible representative: its effective divisor is the strict transform of \(Q\) plus the omitted exceptional curve. No other lines exist. All base points and all connecting lines are \(\mathbb F_5\)-rational.

**(3) Local Fano-scheme lengths.** In \(\mathbb P^3\) with coordinates \((x_0,x_1,x_2,x_3)\), put \(x_4=-\sum_{i=0}^{3}x_i\) and \(f=\sum_{i=0}^{3}x_i^3-(\sum_{i=0}^{3}x_i)^3\). A Grassmann chart around the line spanned by \(V,W\) is obtained by replacing the spanning vectors by \(V+A e_0+C e_1\) and \(W+B e_0+D e_1\), provided these four indicated vectors are independent. Requiring all four coefficients of \(f\) on the moving line to vanish gives four equations in \((A,B,C,D)\).

For the ordinary line spanned by \(V=(0,1,4,0)\), \(W=(0,0,0,1)\), the Jacobian at the origin is
\[
J_{\mathrm{ord}}=\begin{pmatrix}0&0&3&0\\0&0&0&3\\2&0&2&0\\0&2&0&2\end{pmatrix},
\qquad \det J_{\mathrm{ord}}=1\in\mathbb F_5.
\]
Its local Fano ring is \(\mathbb F_5\). For the line through the node spanned by \(V=(1,1,1,1)\), \(W=(0,1,4,2)\), the analogous Jacobian is
\[
J_{\mathrm{node}}=\begin{pmatrix}0&0&0&0\\2&0&3&0\\3&2&1&3\\0&3&0&1\end{pmatrix}.
\]
It has rank three and kernel generated by \((4,3,4,1)\). The coefficient of the cubic-basis monomial \(T^3\) restricted to the corresponding tangent vector has nonzero quadratic term \(3t^2\); the remaining three equations have independent linear terms. Formal elimination therefore gives the complete local ring \(\mathbb F_5[[t]]/(t^2)\). Coordinate permutations act transitively on the fifteen lines of the first kind and on the six of the second kind, so these two local calculations cover all lines.

The relative Fano scheme is projective over \(R\); its generic fiber is the classical zero-dimensional reduced scheme of length \(27\), and its special fiber is zero-dimensional of length \(15+6\cdot2=27\). It is consequently finite over \(R\). For a finite module over the DVR \(R\), equality of generic rank and special-fiber length excludes torsion, giving finite flatness of degree \(27\). The six nonreduced special points account for the six pairwise collisions among the twelve remaining generic geometric lines.

**(4) Point counts.** For \(q=5^m\), blowing up each of the six rational points adds \(q\) points, so \(\#Y(\mathbb F_q)=q^2+q+1+6q\). The strict transform of \(Q\) is \(\mathbb P^1_{\mathbb F_5}\); contracting it removes \(q+1\) points and inserts the node. Thus \(\#X(\mathbb F_q)=q^2+6q+1\). Exponentiating these counts gives the stated zeta function.

## Verification
Run \(\texttt{python3 verify_clebsch5.py}\) with Python 3 (standard library only). It recomputes the six rational base points, all twenty-one pairwise distinct line Plücker coordinates and their cubic identities, orbit sizes under coordinate permutations, both Fano-chart Jacobian ranks, and the nonzero quadratic obstruction at the nodal line. Independent direct enumeration gives \(\#X(\mathbb F_5)=56\) and \(\#X(\mathbb F_{25})=776\). The proof, not these finite enumerations, establishes the results for every field extension and the local scheme structure.

## Relationship to prior work
Cynk and van Straten explicitly report that the Clebsch cubic acquires a node upon reduction modulo five, in their discussion of non-liftable Calabi–Yau models (arXiv:0804.0668, pp. 12–13). The classical twenty-seven lines and their two orbit descriptions are explained in the 2016 exposition by Baez; the smooth-surface configuration is not new. Dolgachev and Martin (2024) likewise remark on the characteristic-five singularity in their classification of automorphisms of del Pezzo surfaces. The arithmetic splitness of the six base points, exact finite flat special-fiber line-scheme multiplicities, and the all-extension zeta formula above are the further combined assertions established here. Standard geometry of a single-nodal cubic implies some geometric line counts, but does not by itself establish the rationality of all six blowup points for this specific characteristic-five model. Searches did not locate the full combined statement; this is not a uniqueness or historical-priority guarantee.

## Limitations
The 2024 reference is background only and does not affect the verified 2008 source date used for archival scoping. The proof concerns the specified integral equations and all finite extensions of \(\mathbb F_5\), not every integral model of the Clebsch surface. The nonreduced Fano fiber is not a statement that twenty-seven distinct geometric lines remain in characteristic five. Equivalent computations in older unindexed literature and stronger general nodal-cubic results remain originality risks. No independent audit has been carried out.

## References
1. S. Cynk and D. van Straten, *Small Resolutions and Non-Liftable Calabi–Yau Threefolds*, arXiv:0804.0668 (first submitted 2008-04-04), especially §6.1, pp. 12–13. https://arxiv.org/abs/0804.0668
2. J. Baez, *27 Lines on a Cubic Surface*, AMS Visual Insight, 2016-02-15. https://blogs.ams.org/visualinsight/2016/02/15/27-lines-on-a-cubic-surface/
3. I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, J. London Math. Soc. (2024), DOI:10.1112/jlms.12905, Remark 5.7. https://doi.org/10.1112/jlms.12905
