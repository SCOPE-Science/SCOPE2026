# Sharp Euclidean inballs and contact-facet transitions for bistar symmetric edge polytopes

## Finding
Let \(T_{a,b}\) be the tree formed from two adjacent hubs, with \(a\) leaves at the first hub and \(b\) at the second, for integers \(a,b\ge2\). In the standard Euclidean coordinate space on its \(N=a+b+2\) vertices, set
\[
H=\{z\in\mathbb R^{N}:\sum_v z_v=0\},\qquad
P_{a,b}=\operatorname{conv}\{\pm(e_v-e_w):vw\in E(T_{a,b})\}\subset H.
\]
Write \(L=\max\{a,b\}\), \(U=\min\{a,b\}\), and let \(\epsilon_L=1\) for even \(L\) and \(0\) for odd \(L\). Define
\[
M_{a,b}=\begin{cases}
\dfrac{9ab+5(a+b)+1}{N},&L\le2U+1,\\[3pt]
L+4U+1-\dfrac{\epsilon_L}{N},&L\ge2U+2.
\end{cases}
\]
The largest Euclidean ball that can be contained in \(P_{a,b}\) has radius exactly \(M_{a,b}^{-1/2}\). The origin is a center of such a ball.

Exactly \(F_{a,b}\) facets of \(P_{a,b}\) are tangent to that origin-centered ball, with
\[
F_{a,b}=\begin{cases}
2,&L\le2U+1,\\[3pt]
2\binom{L}{(L-2U-1)/2},&L\ge2U+3\ \text{odd},\\[3pt]
2\left[\binom{L}{(L-2U-2)/2}+\binom{L}{(L-2U)/2}\right],&L\ge2U+2\ \text{even}.
\end{cases}
\]
Let \(\mathcal C_{a,b}\subset H\) be the full set of centers of balls of that maximum radius. Its affine dimension is
\[
\dim\operatorname{aff}(\mathcal C_{a,b})=
\begin{cases}
a+b,&L\le2U+1,\\
U+1,&L\ge2U+3\ \text{odd},\\
U,&L\ge2U+2\ \text{even}.
\end{cases}
\]
In particular, at the first unbalanced value \(L=2U+2\), the number of contact facets jumps from two to \(2(L+1)\), and the dimension of allowable maximum-ball centers drops sharply.

## Assumptions and scope
All lengths, orthogonality relations, facet distances, and inballs are measured in the Euclidean metric induced by the displayed embedding of \(H\) in \(\mathbb R^N\). No affinely transformed or lattice-normalized metric is used. Every edge vector has Euclidean length \(\sqrt2\). Each tree incidence vector is independent of the others, so \(P_{a,b}\) is full-dimensional in \(H\). Its polar is defined intrinsically as \(P_{a,b}^{\circ}=\{f\in H:\langle f,z\rangle\le1\ \forall z\in P_{a,b}\}\).

## Proof
**1. Facets as signed edge potentials.** The definition gives
\[
P_{a,b}^{\circ}=\{f\in H:|f_v-f_w|\le1\text{ for each edge }vw\}.
\]
Because the graph is a tree, the map from \(f\in H\) to its \(N-1\) oriented edge differences is a linear isomorphism. Thus the polar is a parallelotope. Each of its \(2^{N-1}\) vertices is an edge potential with every oriented edge difference equal to \(\pm1\); these and only these label the facets of \(P_{a,b}\).

**2. A two-variable norm formula.** Interchange the hubs as necessary so that the smaller leaf set has size \(U\) and the larger has size \(L\). Antipodal symmetry allows the two hub potentials to be fixed as \(0\) and \(1\), in this order, before subtracting the coordinate mean. Let \(k\) of the \(U\) leaves at the \(0\)-hub have potential \(+1\) (all others \(-1\)); let \(\ell\) of the \(L\) leaves at the \(1\)-hub have potential \(2\) (all others \(0\)). Directly,
\[
\sum_v f_v=2(k+\ell)-U+1,\quad
\sum_v f_v^2=U+1+4\ell,
\]
so the squared centered Euclidean norm is
\[
S(k,\ell)=U+1+4\ell-
\frac{[2(k+\ell)-U+1]^2}{N},
\qquad 0\le k\le U,\ 0\le\ell\le L.
\]
For a fixed sum \(k+\ell\), replacing a small-side \(+1\)-leaf with a large-side \(2\)-leaf increases \(S\) by exactly \(4\). Therefore every maximizer has \(k=0\) or \(\ell=L\). In the latter case, for \(k>0\) the square term strictly increases with \(k\), since \(L\ge U\), while the other terms stay fixed. Thus no maximum has \(k>0\). The global maximum is that of
\[
S(0,\ell)=U+1+4\ell-
\frac{(2\ell-U+1)^2}{N}
\quad (0\le\ell\le L).
\]
Its consecutive increments are exactly
\[
S(0,\ell+1)-S(0,\ell)=\frac{4(2U+L-2\ell)}{N}.
\]
If \(L\le2U+1\), the unique maximizing count is \(\ell=L\). If \(L\ge2U+3\) is odd, it is \(\ell=U+(L+1)/2\). If \(L\ge2U+2\) is even, the two maximizing counts are \(\ell=U+L/2\) and \(\ell=U+L/2+1\). Substitution proves the stated two branches of \(M_{a,b}\). For the balanced branch, expansion yields \([9UL+5(U+L)+1]/N\). The odd and even unbalanced branches simplify to \(L+4U+1\) and \(L+4U+1-1/N\), respectively.

**3. Inradius and contacts.** Every facet supporting inequality of \(P_{a,b}\) has the form \(\langle f,z\rangle\le1\), for some vertex \(f\) of the polar, and lies at Euclidean distance \(1/\|f\|_2\) from the origin. Therefore the largest centered ball has radius \(1/\sqrt{M_{a,b}}\). This is also the unrestricted inradius: if a radius-\(r\) ball is contained in the centrally symmetric body about some center \(c\), its reflected ball about \(-c\) also lies in the body; their midpoint ball of radius \(r\) lies in the body by convexity. The maximizers in Step 2 are precisely the centered facet normals touching the origin ball. Each choice of \(\ell\) labels \(\binom L\ell\) signed edge potentials for each of the two possible hub signs. The displayed formula for \(F_{a,b}\) follows, including the transition case where both \(\ell=L-1\) and \(\ell=L\) maximize.

**4. All optimal centers.** Let \(\mathcal N\) be the set of the contacting polar vertices and let \(W=\operatorname{span}(\mathcal N)\subset H\). An arbitrary center \(c\) of a ball of radius \(M_{a,b}^{-1/2}\) must satisfy \(\langle f,c\rangle=0\) for every \(f\in\mathcal N\), because both \(\pm f\) attain the limiting facet distance. Conversely, the finitely many noncontact facets have strictly positive slack at \(c=0\). Hence a neighborhood of \(0\) in \(W^\perp\cap H\) consists of valid centers. Thus \(\operatorname{aff}(\mathcal C_{a,b})=W^\perp\cap H\), and its dimension is \(N-1-\dim W\).

In the balanced regime there is one positive-hub contact potential, together with its negative, so \(\dim W=1\). In the odd unbalanced regime, the positive-hub contacts correspond to all \(\ell\)-subsets of the large leaf set, where \(1\le\ell\le L-1\). Differences of these vectors span the \(L-1\)-dimensional large-leaf contrast space; adding any one contact vector supplies one further independent direction, witnessed by its nonzero hub difference. Thus \(\dim W=L\). In the even unbalanced regime, two consecutive cardinalities of the large-leaf subset are present. Again their differences span all \(L-1\) leaf contrasts. The two orbit averages are independent modulo that contrast space: each has the same nonzero hub difference, but their large-leaf averages differ. Therefore \(\dim W=L+1\). Subtraction from \(N-1=U+L+1\) yields the center-dimension formula.

## Verification
The accompanying standalone `verify.py` uses only Python's standard library. It reconstructs the full polar vertex set by all \(2^{a+b+1}\) signed edge differences, computes the squared centered norms as exact rational numbers, counts their maximizers, and computes the rational rank of their contact-normal span. For \(36\) parameter pairs it compares all three invariants with the formulas above. Execute `python3 verify.py` from a directory containing the extracted script. Representative exact triples \((M,F,\dim W)\) are \((19/2,2,1)\) at \((a,b)=(2,2)\), \((149/10,14,7)\) at \((2,6)\), and \((521/18,156,13)\) at \((4,12)\). These finite tests are not an exhaustive proof for unbounded \(a,b\); Steps 1–4 supply that proof.

## Relationship to prior work
Symmetric edge polytopes and their connection with graph geometry are established in the references. Existing results that all tree symmetric edge polytopes are unimodularly equivalent to cross-polytopes describe their lattice or combinatorial class, not the intrinsic Euclidean metric of this coordinate realization. The general tight-edge facet-potential criterion is compatible with Step 1; it does not by itself evaluate the polar Euclidean norm extremum or the contact/center transitions. The present statement concerns exactly those Euclidean metric invariants for the first family with two branching hubs. In particular, unimodular equivalence is not Euclidean congruence.

## Limitations
The theorem assumes two adjacent hubs with at least two leaves at each hub, unit edge vectors, the specified coordinate embedding, and the ordinary Euclidean metric. It does not classify arbitrary tree inballs, general weighted-edge realizations, or ellipsoids. An equivalent maximum-variance formula for unit-Lipschitz functions might exist under alternative terminology; no claim of exhaustive bibliographic novelty or independent validation is made.

## References
1. A. D'Alì, E. Delucchi, and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193 (first public preprint October 11, 2019), https://arxiv.org/abs/1910.05193.
2. A. Higashitani, K. Jochemko, and M. Michałek, *Arithmetic Aspects of Symmetric Edge Polytopes*, arXiv:1807.07678, https://arxiv.org/abs/1807.07678.
3. E. Delucchi and L. Hoessly, *Fundamental Polytopes of Metric Trees via Parallel Connections of Matroids*, arXiv:1612.05534, https://arxiv.org/abs/1612.05534.
4. A. D'Alì, M. Juhnke-Kubitzke, and D. Koch, *On a Generalization of Symmetric Edge Polytopes to Regular Matroids*, arXiv:2307.04933, https://arxiv.org/abs/2307.04933.
