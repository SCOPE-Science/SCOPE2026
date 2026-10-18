# Exact Hilbert distortion of cocktail-party transportation spaces

## Finding

Let \(G_k=K_{2,2,\ldots,2}\) be the complete \(k\)-partite unit-edge graph with exactly two vertices in each part, \(k\ge2\). Equip its \(2k\) vertices with the shortest-path metric and let \(\mathcal F(G_k)\) be the real Lipschitz-free (transportation-cost) space. Its dimension is \(2k-1\). The exact multiplicative Banach--Mazur distance to Hilbert space is
\[
 d_{\mathrm{BM}}\bigl(\mathcal F(G_k),\ell_2^{2k-1}\bigr)^2=
 \begin{cases}
 3,&k=2,\\
 10/3,&k=3,\\
 k,&k\ge4.
 \end{cases}
\]
The \(k=2\) case is the familiar four-cycle boundary case; the new all-parameter assertion concerns \(k\ge3\), including the six-vertex exception and a sharp stabilization of the canonical Euclidean shape from \(k=4\) onward.

More precisely, place the free-space ball in the zero-sum Euclidean hyperplane \(H=\{x\in\mathbb R^{2k}:\sum_v x_v=0\}\) as
\[
 P_k=\operatorname{conv}\{\pm(e_u-e_v):u,v\text{ lie in different pairs}\}.
\]
Decompose orthogonally \(H=U\oplus W\), where \(U\) consists of vectors anti-constant inside every pair and \(W\) consists of vectors constant inside pairs and of global sum zero. An optimal symmetry-invariant positive quadratic form, with the normalization \(\alpha+\beta=1\), is
\[
 q_k(x)=\alpha_k\|\operatorname{pr}_U x\|_2^2+(1-\alpha_k)\|\operatorname{pr}_W x\|_2^2,
 \qquad
 \alpha_k=\begin{cases}2/3,&k=2,\\3/5,&k=3,\\1/2,&k\ge4.\end{cases}
\]
Thus the canonical centered Euclidean form is already optimal exactly for \(k\ge4\) within the full class of Hilbertian forms. In this range the distortion is \(\sqrt{k}\), whose ratio to the maximal John bound \(\sqrt{2k-1}\) tends to \(1/\sqrt2\).

## Assumptions and scope

All scalars are real; the metric is the unweighted shortest-path metric on \(G_k\); and \(d_{\mathrm{BM}}(X,Y)=\inf_T\|T\|\|T^{-1}\|\), the infimum extending over all invertible real linear maps. The Euclidean inner product is the usual one on \(H\). Each omitted matching edge has metric distance \(2\), and each graph edge has distance \(1\). No restriction is made on the linear isomorphism being optimized. The center of every considered ellipsoid may be taken to be zero because \(P_k\) is centrally symmetric.

## Proof

**1. The two geometric orbits.** Duality gives
\[
 Q_k=P_k^\circ=\{y\in H: |y_u-y_v|\le1\text{ whenever }u,v\text{ lie in different pairs}\}.
\]
A point of \(Q_k\) is a vertex precisely when its tight-edge graph (edges across pairs satisfying \(|y_u-y_v|=1\)) is connected: the edge equalities have rank \(2k-1\) on \(H\) exactly in that case. A connected spanning tight graph forces all potential differences to be integers. Since all graph distances are at most \(2\), an extreme potential, after shifting by a constant, is either a \(0/1\) labeling or has values \(0,1,2\). In the second case the \(0\)-vertex and \(2\)-vertex must form a nonedge, hence one distinguished pair; every other vertex must have value \(1\). After centering, this is the vector with values \(+1,-1\) on that pair and zero elsewhere. Consequently every vertex of \(Q_k\) belongs to one of two explicit classes: centered \(0/1\) cuts or the \(2k\) special vectors. This is also consistent with the published complete-multipartite facet classification [2, Proposition 3.5]. We need only this exhaustive inclusion and the explicit extremality of the test cuts below.

**2. Symmetry reduction does not lose generality.** For a positive-definite form \(q(x)=\langle Ax,x\rangle\), set
\[
 a(A)=\max_{v\in P_k}v^{\mathsf T}Av,\qquad
 b(A)=\max_{y\in Q_k}y^{\mathsf T}A^{-1}y.
\]
The squared Euclidean Banach--Mazur distance is \(\inf_{A\succ0}a(A)b(A)\). By positive scaling, restrict to \(a(A)\le1\) and minimize \(b(A)\). The former constraint is convex in \(A\); the function \(y^{\mathsf T}A^{-1}y\) is convex in \(A\), so \(b(A)\) is convex. Averaging any feasible \(A\) under permutations of the pairs and independent swaps within pairs therefore cannot increase \(b\). The invariant forms on \(H\) are exactly \(\alpha\operatorname{pr}_U+\beta\operatorname{pr}_W\), with \(\alpha,\beta>0\): independent swaps kill cross terms and the permutation action is scalar on each irreducible summand. Every root joining distinct pairs has squared \(U\)- and \(W\)-projection norms both equal to \(1\). Hence \(a=\alpha+\beta\); normalize \(\alpha+\beta=1\). It remains to minimize
\[
 F_k(\alpha)=\max_{y\in\operatorname{vert}(Q_k)}
 \left(\frac{\|\operatorname{pr}_U y\|^2}{\alpha}
 +\frac{\|\operatorname{pr}_W y\|^2}{1-\alpha}\right),\quad 0<\alpha<1.
\]

**3. Exact dual vertex energies.** A centered \(0/1\) labeling with \(h\) ones and \(r\) pairs whose entries differ has
\[
 u^2=\|\operatorname{pr}_U y\|_2^2=\frac r2,\quad
 w^2=\|\operatorname{pr}_W y\|_2^2=\frac{h(2k-h)}{2k}-\frac r2.
\]
Here \(0<h<2k\) and \(h\equiv r\pmod2\). In particular \(u^2+w^2\le k/2\). A special potential has \((u^2,w^2)=(2,0)\). When \(k\ge4\), taking \(\alpha=1/2\) gives \(F_k(1/2)\le\max\{k,4\}=k\).

**4. Matching lower bound for even \(k\ge4\).** Select one endpoint of each pair for the upper class: its tight-edge graph is the complete bipartite graph on the two classes minus a perfect matching, which is connected for \(k\ge3\). This cut has \((u^2,w^2)=(k/2,0)\). For even \(k\), choose both endpoints of exactly \(k/2\) pairs for the upper class, giving a second vertex with \((u^2,w^2)=(0,k/2)\). Therefore
\[
 F_k(\alpha)\ge\frac k2\max\left\{\frac1\alpha,\frac1{1-\alpha}\right\}\ge k.
\]
The exact answer is \(k\) and the only minimizing invariant ratio is \(\alpha=1/2\).

**5. Matching lower bound for odd \(k\ge5\).** The all-split cut still gives \(F_k(\alpha)\ge k/(2\alpha)\), which exceeds \(k\) for \(\alpha<1/2\). For \(\alpha>1/2\), take a balanced cut containing one split pair and \((k-1)/2\) entire upper pairs, with the same number of entire lower pairs. Its tight graph is connected and its energies are \((u^2,w^2)=(1/2,(k-1)/2)\). Thus
\[
 F_k(\alpha)\ge \frac1{2\alpha}+\frac{k-1}{2(1-\alpha)}>k\quad(\alpha>1/2).
\]
The last expression equals \(k\) at \(\alpha=1/2\) and is strictly increasing to its right: its derivative is \(-1/(2\alpha^2)+(k-1)/(2(1-\alpha)^2)>0\). Hence \(F_k\) has minimum \(k\), uniquely at the invariant ratio \(\alpha=1/2\).

**6. Exceptional six-vertex and four-vertex cases.** For \(k=3\), a special vertex yields \(2/\alpha\), and a cut consisting of one entire pair yields \((4/3)/(1-\alpha)\). Their maximum is minimized at \(\alpha=3/5\), with value \(10/3\). At that ratio a cut with \(h\) upper vertices and \(r\) split pairs has energy
\[
 \frac52\,\frac{h(6-h)}6-\frac{5r}{12}.
\]
If \(h=1,5\) it is less than \(10/3\); if \(h=2,4\) it is at most \(10/3\); and if \(h=3\), parity forces \(r\ge1\), again giving at most \(10/3\). Every special vertex has energy exactly \(10/3\). Therefore the minimum is exactly \(10/3\). For \(k=2\), a special vertex gives \(2/\alpha\) and a whole-pair cut gives \(1/(1-\alpha)\); their intersection is \(3\) at \(\alpha=2/3\). At this ratio, every cut has total squared energy at most \(1\), hence weighted energy at most \(3\); special vertices have energy \(3\). This proves the boundary case and completes the classification.

## Verification

The bundled `check_exact.py` independently enumerates every \(0/1\) potential and every special \(\pm1\) potential for \(2\le k\le8\), tests vertexhood by exact connectivity of its tight-edge graph, computes the orthogonal projection energies using rational arithmetic, and checks the proposed exact distortion and number of polar vertices. It prints `EXACT_COCKTAIL_DISTORTION_CHECKS_PASS: k=2..8`. It finds respectively \(6,56,246,1012,4082,16368,65518\) vertices for \(k=2,\ldots,8\). These finite checks corroborate but do not replace the all-dimensional proof above. No numerical optimization is necessary for the theorem.

## Relationship to prior work

The graph-metric quotient description of Lipschitz-free spaces is established in [1]. The facet classification of complete multipartite symmetric edge polytopes, including this graph family, is covered by [2, Proposition 3.5]; the present theorem does not claim that facet classification as new. The connection between finite-metric Kantorovich--Rubinstein balls and symmetric edge polytopes is treated in [3]. General Euclidean Banach--Mazur bounds and extremal ellipsoid results are developed in [4]. Unlike these results, the present statement optimizes the exact Hilbertian distortion for every matching-deleted complete graph. The \(k=2\) instance agrees with the known four-cycle value; the substantive all-dimensional determination and the transition from anisotropic to Euclidean optimal invariant forms occur for \(k\ge3\).

## Limitations

The assertion concerns real spaces and equal part sizes two, not arbitrary complete multipartite metrics, weighted deleted edges, or complex scalars. The proof determines one optimal invariant quadratic form and the unique ratio within invariant forms; it does not claim uniqueness among all noninvariant optimal forms. Existing graph-facet theory is an input, not a new contribution. The finite checker does not certify infinite parameter ranges. An equivalent unindexed treatment of the Hilbertian distortion may exist; no independent scientific audit has been performed.

## References

[1] S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1 (10 July 2018), especially Section 1.1 and the edge-flow quotient.

[2] A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (20 July 2018), especially Proposition 3.5.

[3] A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (11 October 2019), especially Sections 2 and 4.

[4] F. Grundbacher, T. Kobos, *On certain extremal Banach--Mazur distances in small dimensions*, arXiv:2407.08829v1 (11 July 2024); subsequent revisions have an expanded title.
