# Twenty-one rational lines and a split nodal resolution of the Clebsch cubic in characteristic \(5\)

## Finding
Let \(X\subset\mathbb P^4_{\mathbb F_5}\) be the cubic surface cut out by
\[
\sum_{i=0}^{4}X_i=0,\qquad \sum_{i=0}^{4}X_i^3=0.
\]
Then \(X\) is geometrically integral and normal, with exactly one geometric singular point \(P=[1:1:1:1:1]\), an ordinary double point of type \(A_1\). Projection from \(P\) resolves by blowing up **all six** \(\mathbb F_5\)-points of a smooth plane conic, then contracting its strict transform (a \((-2)\)-curve). The surface contains exactly \(21\) geometric lines, **all defined over \(\mathbb F_5\)**: six through \(P\) and fifteen disjoint from \(P\). The coordinate-permutation subgroup \(S_5\) acts sharply three-transitively on the six lines through \(P\). For each \(m\ge1\), writing \(q=5^m\),
\[
\#X(\mathbb F_q)=q^2+6q+1,\qquad
Z(X/\mathbb F_5,T)=\frac1{(1-T)(1-5T)^6(1-25T)}.
\]
The claim concerns the literal reduction of these integral equations, not a smooth or stable model of a different integral presentation.

## Assumptions and scope
All geometric assertions are over an algebraic closure of \(\mathbb F_5\); rationality assertions refer to the displayed \(\mathbb F_5\)-model. A geometric line means a reduced projective line on \(X_{\overline{\mathbb F}_5}\). The zeta function uses the conventional generating series \(\exp(\sum_{m\ge1}\#X(\mathbb F_{5^m})T^m/m)\). The six-point symmetry statement concerns the explicitly given coordinate-permutation subgroup; it does not assert that this is the complete automorphism group of the singular surface.

## Proof
**1. The isolated node.** Within the hyperplane \(\sum X_i=0\), a singular point must have \(3X_i^2\) independent of \(i\). Over characteristic \(5\) every coordinate therefore equals \(a\) or \(-a\) with \(a\ne0\). If \(k\) coordinates equal \(a\), the linear equation gives \((2k-5)a=2ka=0\); hence \(k=0\) or \(5\). Thus the unique singular point is \(P\). On the chart \(X_4=1\), put \(X_i=1+u_i\) for \(0\le i\le3\), with \(\sum_{i=0}^3u_i=0\). The defining equation reduces to
\[
3\sum_{i=0}^3u_i^2+\sum_{i=0}^3u_i^3=0.
\]
The quadratic form \(\sum u_i^2\) on the three-space \(\sum u_i=0\) is nondegenerate: the orthogonal complement of that hyperplane is spanned by \((1,1,1,1)\), which is not in it because \(4\ne0\) in \(\mathbb F_5\). Therefore \(P\) is an ordinary node. A reducible cubic hypersurface in \(\mathbb P^3\) has a positive-dimensional singular intersection of components, and a nonreduced one is singular along a component. Thus the isolated-node cubic is geometrically integral. As a hypersurface it is \(S_2\), and its isolated singularity gives \(R_1\), so it is normal.

**2. Exactly six simple base directions.** Write \(e=(1,1,1,1,1)\) and represent a direction modulo \(e\) uniquely by \(v=(u_0,u_1,u_2,u_3,0)\) satisfying \(\sum_{i=0}^3u_i=0\). On its projective plane \(\Pi\cong\mathbb P^2\), put \(Q(v)=\sum u_i^2\) and \(G(v)=\sum u_i^3\). The smooth conic \(Q=0\) and the cubic \(G=0\) meet in exactly six simple \(\mathbb F_5\)-points, namely the six projective classes of the permutations of \((1,2,3,4)\). Every such permutation obeys \(\sum u_i=\sum u_i^2=\sum u_i^3=0\) modulo \(5\). There are \(24/4=6\) classes because the four nonzero scalars act freely on these tuples. At any such tuple the gradients of \(Q\) and \(G\) are transverse inside \(\sum u_i=0\): otherwise, for some \(\lambda,\mu\) the quadratic polynomial \(3t^2-2\lambda t-\mu\) would vanish at all four distinct elements \(1,2,3,4\) of \(\mathbb F_5\). This is impossible. Thus \(Q\) and \(G\) have no common component; Bézout's intersection number \(2\cdot3=6\) proves geometric completeness and reducedness. Since a smooth \(\mathbb F_5\)-conic with a point has exactly six \(\mathbb F_5\)-points, the base locus \(Z=V(Q,G)\) is precisely \(Q(\mathbb F_5)\) with its reduced scheme structure.

**3. Blowup resolution.** On the projective line spanned by \(e\) and \(v\), the cubic equals
\[
\sum_i(se_i+tv_i)^3=t^2\bigl(3sQ(v)+tG(v)\bigr).
\]
Projection from \(P\) has rational inverse
\[
\Phi:\Pi\dashrightarrow X,\qquad [v]\longmapsto[G(v)e-3Q(v)v].
\]
These five cubic coordinates vanish simultaneously exactly at the six simple points of \(Z\). Their linear terms span the ideal \((Q,G)\) locally, so a single blowup resolves the base locus. Put \(Y=\operatorname{Bl}_{Z}(\Pi)\); the resulting morphism \(f:Y\to X\) is birational, since projection is an inverse away from its exceptional set. The strict transform \(D\) of \(Q\) has class \(2H-\sum_{i=1}^6E_i\), self-intersection \(-2\), and intersection zero with \(-K_Y=3H-\sum E_i\). All of \(D\) maps to \(P\); elsewhere the projection description is an inverse. Because \(P\) is an \(A_1\) point, this is its minimal resolution, and \(D\cong Q\cong\mathbb P^1_{\mathbb F_5}\). Each exceptional curve \(E_i\) maps with degree one onto the corresponding line through \(P\). Its direction is its base point in \(Z\), giving precisely six lines through \(P\).

**4. Exactly fifteen more lines.** Every classical diagonal line, obtained by permuting \((s,-s,t,-t,0)\), remains on the defining cubic. There are \(5\cdot3=15\) distinct such \(\mathbb F_5\)-lines, and none contains \(P\). To prove that these exhaust the lines disjoint from \(P\), let \(L\) be any such geometric line and \(C\subset Y\) its inverse image. Since \(f\) is an isomorphism over \(X\setminus\{P\}\), \(C\cong\mathbb P^1\) and \((-K_Y)\cdot C=1\); adjunction gives \(C^2=-1\). A curve different from an exceptional \(E_i\) has class \(dH-\sum m_iE_i\) with integers \(d\ge1\), \(m_i\ge0\). Consequently
\[
3d-\sum m_i=1,\qquad d^2-\sum m_i^2=-1.
\]
Cauchy–Schwarz implies \((3d-1)^2\le6(d^2+1)\), forcing \(d\le2\). For \(d=1\), the only possibility is two multiplicities one: a chord joining two of the six conic points. They give \(\binom62=15\) lines. For \(d=2\), exactly five multiplicities would be one, but the unique plane conic through any five of these six points is \(Q\), which passes through the sixth as well; it cannot represent that class. Therefore there are no other lines. The six lines through the node are the only ones arising from the \(E_i\), proving the total \(21\).

**5. Finite-field arithmetic.** Each of the six blowup centers is \(\mathbb F_5\)-rational, so for every \(q=5^m\),
\[
\#Y(\mathbb F_q)=(q^2+q+1)+6q.
\]
The morphism \(Y\to X\) replaces the rational node by the split conic \(D\cong\mathbb P^1\), with \(q+1\) points. It follows that \(\#X(\mathbb F_q)=\#Y(\mathbb F_q)-(q+1)+1=q^2+6q+1\). The displayed zeta function is obtained by exponentiating these counts.

**6. The exceptional six-point action.** Coordinate permutations preserve both equations and fix \(P\). The six node-lines are the images under \(S_5\) of the line spanned by \(e\) and \((0,1,2,3,4)\). A permutation fixes this line exactly when, on the labels \(\mathbb F_5\), it acts as \(t\mapsto at+b\), with \(a\in\mathbb F_5^\times\) and \(b\in\mathbb F_5\). Its stabilizer therefore has order \(20\), and the orbit has size \(6\). The explicit finite group calculation in the accompanying verification code enumerates all \(120\) coordinate permutations and shows that the images of one ordered triple of distinct lines are all \(6\cdot5\cdot4=120\) ordered triples; the action is sharply three-transitive. This last step is a genuinely exhaustive finite permutation computation, not a claim inferred from samples.

## Verification
The standalone standard-library program `verify.py` works in \(\mathbb F_5\) and \(\mathbb F_{25}=\mathbb F_5[\alpha]/(\alpha^2-3)\). It exhaustively enumerates projective points (obtaining \(56\) and \(776\)); the conic and base intersections (\(6,6\) and \(26,6\)); all \(806\) rational lines of \(\mathbb P^3(\mathbb F_5)\), identifying exactly \(21\) contained lines, six through the node; the fifteen diagonal lines; and all \(120\) permutations for the six-point action. Run `python3 verify.py`; success ends with `VERIFY_OK`. These finite checks support, but do not replace, the geometric completeness and all-extension arguments in Steps 1–5.

## Relationship to prior work
The classical Clebsch cubic and its \(27\) characteristic-zero lines are standard; the \(15\) diagonal lines here are not new by themselves. Dolgachev–Martin (arXiv:2303.16170, initial posting 2023-03-28) state that the Clebsch model becomes singular in characteristic \(5\) but study **smooth** del Pezzo automorphism groups. Vikulova (arXiv:2407.09997, initial posting 2024-07-13) identifies \([1:1:1:1:1]\) as a singular point and likewise concentrates on **smooth** cubic surfaces. Neither inspected paper states the reduced six-point conic base scheme, the full \(21\)-line splitting with arithmetic fields, the exceptional action, or the uniform zeta formula. Published work on \(27\) lines over finite fields treats smooth cubics and does not imply the present special-fiber computation without an additional reduction analysis.

## Limitations
The result makes no claim about the complete automorphism group of this singular surface, the scheme structure of its relative Hilbert scheme of lines over \(\mathbb Z\), or how each non-diagonal characteristic-zero line specializes scheme-theoretically. Historical literature may contain equivalent observations not indexed in the searched records. All assertions about \(\mathbb F_{5^m}\) follow from the proof, not the two displayed numerical checks. Independent audit and independent validation have not been performed.

## References
1. I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, arXiv:2303.16170v1, 2023-03-28, especially the cubic-surface discussion and the characteristic-five remark. https://arxiv.org/html/2303.16170v2
2. A. V. Vikulova, *The most symmetric smooth cubic surface*, arXiv:2407.09997v1, 2024-07-13, Introduction and Proposition 1. https://arxiv.org/html/2407.09997v3
3. S. McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217, 2021, for the distinction between smooth-surface line counts and the present nodal problem. https://arxiv.org/abs/2101.08217
4. F. Karaoglu and A. Betten, *The number of cubic surfaces with 27 lines over a finite field*, Journal of Algebraic Combinatorics 56 (2022), for a smooth-surface six-arc comparison. https://doi.org/10.1007/s10801-020-01009-3
