# A sharp three-to-one contact transition for type-B symmetric edge polytopes of complete split graphs

## Finding

For integers \(p,q\ge2\), let \(G_{p,q}=K_p\vee\overline{K_q}\) denote the graph consisting of a clique of size \(p\), an independent set of size \(q\), and all edges between the two classes. In the standard Euclidean realization, its type-B symmetric edge polytope is
\[
\mathcal B_{p,q}=\operatorname{conv}\bigl(\{\pm e_i:1\le i\le p+q\}\cup\{\epsilon e_i+\eta e_j:ij\in E(G_{p,q}),\ \epsilon,\eta\in\{-1,1\}\}\bigr).
\]
The largest inscribed Euclidean ball has exact radius
\[
r_{p,q}=\frac1{\sqrt{\max\{q,(p+q)/4\}}}.
\]
Its origin-centered instance has exactly
\[
F_{p,q}=\begin{cases}2^q,&p<3q,\\2^q+2^{p+q},&p=3q,\\2^{p+q},&p>3q\end{cases}
\]
tangent facets. The affine dimension of the complete set of optimal inball centers is
\[
\dim\operatorname{aff}\mathcal I_{p,q}=\begin{cases}p,&p<3q,\\0,&p\ge3q.\end{cases}
\]
The circumradius is \(\sqrt2\) and the enclosing sphere touches precisely the \(4\bigl(\binom p2+pq\bigr)\) signed edge-root vertices. Both centered spheres are unique as enclosing spheres of minimum radius and as centered candidates, respectively; the inscribed ball itself is nonunique exactly when \(p<3q\).

## Assumptions and scope

The coordinates have their ordinary Euclidean metric, without a scaling or a lattice-metric change. The two classes are labeled, but the result depends only on their sizes. We assume \(p,q\ge2\); the theorem makes no assertion about the different boundary family with \(q=1\). Tangent facets are genuine codimension-one faces, not repeated supporting inequalities. An inball center is any \(c\in\mathbb R^{p+q}\) such that \(c+r_{p,q}B_2^{p+q}\subseteq\mathcal B_{p,q}\).

## Proof

**1. Polar inequalities.** Every coordinate vector and every signed edge-root belongs to the generating set. Hence the polar, using \(\langle x,y\rangle\le1\), is precisely
\[
\mathcal B_{p,q}^{\circ}=\{y\in\mathbb R^{p+q}:|y_i|\le1,\quad |y_i|+|y_j|\le1\ \text{for every edge }ij\in E(G_{p,q})\}.
\]
It is compact and full-dimensional. Because the polytope is unconditional, maximizing \(\|y\|_2^2\) reduces to nonnegative coordinates. Write \(a_1,\ldots,a_p\) for the clique coordinates, \(b_1,\ldots,b_q\) for the independent coordinates, and \(M=\max_i a_i\). Then \(0\le M\le1\) and every \(b_j\le1-M\).

**2. Sharp maximum and equality cases.** If \(0\le M\le1/2\), all clique coordinates are bounded by \(M\). Therefore
\[
\|y\|_2^2\le pM^2+q(1-M)^2\le\max\{q,(p+q)/4\},
\]
where the second bound follows from strict convexity in \(M\). Equality at \(M=0\) gives exactly \((a,b)=(0_p,\mathbf1_q)\); equality at \(M=1/2\) gives exactly \((\mathbf1_p/2,\mathbf1_q/2)\).

If \(1/2\le M\le1\), choose \(i\) with \(a_i=M\). All other clique coordinates are at most \(1-M\), because the clique is complete. Together with the independent bound this gives
\[
\|y\|_2^2\le M^2+(p+q-1)(1-M)^2\le\max\{(p+q)/4,1\}.
\]
Strict convexity again makes the second inequality sharp only at an endpoint. Because \(q\ge2\), the value \(1\) cannot maximize globally. Consequently
\[
\max_{y\in\mathcal B_{p,q}^{\circ}}\|y\|_2^2=\max\{q,(p+q)/4\},
\]
and **every** maximizer is one of the following signed configurations:
\[
Y_q=\{(0_p,\sigma_1,\ldots,\sigma_q):\sigma_j\in\{\pm1\}\},
\qquad
Y_{1/2}=\{(\sigma_1/2,\ldots,\sigma_{p+q}/2):\sigma_i\in\{\pm1\}\}.
\]
The first family alone maximizes for \(p<3q\), the second alone for \(p>3q\), and both maximize at equality. Since a strictly convex function on a compact polytope has no maximizer in the relative interior of a positive-dimensional face, every listed maximizer is a polar vertex. Thus each determines a genuine primal facet \(\langle y,x\rangle=1\), and distinct vectors give distinct facets.

**3. Global inradius and facet contacts.** For any full-dimensional origin-symmetric convex body \(K\), if \(c+rB_2\subseteq K\), symmetry also gives \(-c+rB_2\subseteq K\). Their midpoint inclusion implies \(rB_2\subseteq K\). In polar form, the radius of this centered ball is \(1/\max_{y\in K^\circ}\|y\|_2\). The preceding calculation therefore proves the asserted **global** inradius and the exact counts of tangent facets; the tangent point for a maximum-norm polar vertex \(y\) is \(y/\|y\|_2^2\).

**4. Complete dimension of the incenter locus.** Let \(r=r_{p,q}\). For any center \(c\), inclusion of \(c+rB_2\) is equivalent to
\[
\langle y,c\rangle+r\|y\|_2\le1\qquad\text{for every vertex }y\text{ of }\mathcal B_{p,q}^{\circ}.
\]
For a maximal-norm polar vertex \(y\), the second term is already \(1\), hence \(\langle y,c\rangle\le0\). Since \(-y\) is also maximal, necessarily \(\langle y,c\rangle=0\). If \(p\ge3q\), the signed half-coordinate family \(Y_{1/2}\) is active, and its span is all of \(\mathbb R^{p+q}\). Thus \(c=0\) is the only inball center. If \(p<3q\), the active family \(Y_q\) spans exactly the independent-coordinate subspace, forcing the independent components of \(c\) to vanish. Every other polar vertex has strictly smaller norm. Finiteness of the polar vertex set leaves a strictly positive slack margin at \(c=0\), so all sufficiently small clique-coordinate translations remain feasible. Therefore the incenter locus has affine dimension exactly \(p\), and the only compulsory zero coordinates are the independent ones.

**5. Outer sphere.** Every generator has norm either \(1\) or \(\sqrt2\). Thus \(\mathcal B_{p,q}\subseteq\sqrt2B_2\), and the signed edge-roots attain this radius. For an origin-symmetric body containing a pair \(\pm v\) at distance \(\sqrt2\) from the origin, any enclosing ball has radius at least \(\sqrt2\); equality forces the center to be the origin by the parallelogram identity. Strict convexity of squared Euclidean norm rules out every nontrivial convex combination of distinct generators as an additional point of norm \(\sqrt2\). The \(\binom p2+pq\) edges yield exactly four distinct signed roots apiece, proving the claimed outer contact count.

## Verification

The accompanying standalone Python program `check_split_type_b.py` uses exact rational arithmetic. It constructs and enumerates polar vertices in four small dimension pairs and checks that their maximal squared norms and equality profiles match the theorem. It also checks extremal witnesses and distinct outer contacts over two hundred dimension profiles. The complete printed transcript is reproducible by running `python3 check_split_type_b.py` from the directory containing this file. These finite checks are evidence of boundary consistency only; the proof above is the justification in arbitrary dimensions.

## Relationship to prior work

Ohsugi and Tsuchiya introduced graph-associated type-B root polytopes and studied reflexivity, triangulations and Ehrhart-theoretic invariants [1]. Their subsequent treatment concerns matching-polynomial descriptions of the associated Ehrhart polynomials [2]. The exact polar norm maximizers, resulting Euclidean inball contact phase transition, and dimension of the whole incenter locus are different invariants and are not supplied by the specific statements inspected in those sources. Type-A symmetric edge polytopes, defined with differences of basis vectors in a sum-zero hyperplane, are a distinct construction and their Euclidean radius formulas do not imply the result for this full-dimensional type-B body. The polar maximization can also be regarded as quadratic optimization over a graph fractional-packing polytope, but the contact and center classification is essential to the present result.

## Limitations

The theorem is for complete split graphs with both class sizes at least two in the unweighted coordinate realization. It does not characterize the exact shape or vertex count of the incenter body below the phase transition, only its affine dimension and forced coordinate directions. Independent mathematical validation is not part of this note. An older equivalent result expressed in graph-packing or root-system terminology remains a bibliographic possibility; no claim of exhaustive literature coverage is made.

## References

[1] Hidefumi Ohsugi and Akiyoshi Tsuchiya, *Reflexive polytopes arising from bipartite graphs with \(\gamma\)-positivity associated to interior polynomials*, first preprint 2018-10-29, arXiv:1810.12258v1, later published in *Selecta Mathematica* 26 (2020). https://arxiv.org/abs/1810.12258

[2] Hidefumi Ohsugi and Akiyoshi Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, first preprint 2020-08-19, arXiv:2008.08621v1, published in *Séminaire Lotharingien de Combinatoire* 2021. https://arxiv.org/abs/2008.08621
