# A linear-time nearest-vertex covering certificate for every demihypercube

## Finding

For each integer \(n\ge4\), set
\[
V_n=\{v\in\{-1,1\}^n:\prod_{i=1}^n v_i=1\},\qquad P_n=\operatorname{conv}(V_n).
\]
The key theorem is a **nearest-vertex covering certificate**: for every \(x\in P_n\), **every** vertex \(v\in V_n\) maximizing \(\langle x,v\rangle\) satisfies
\[
\boxed{\frac{nx-v}{n-1}\in P_n}.
\]
A maximizing vertex is computable in \(O(n)\) arithmetic operations: take the signs of the coordinates of \(x\), adjusting zero signs freely; if all coordinates are nonzero and the signs have odd parity, flip one sign of minimum absolute coordinate. Thus the covering uses **all nearest vertices**, not an arbitrary existential vertex witness among the \(2^{n-1}\) choices.

As a sharp consequence, the Schneider convexification threshold and vertex-generation weight are
\[
\boxed{c(V_n)=n-1},\qquad
\boxed{\eta(P_n)=1/n},
\]
where \(c(V_n)=\inf\{\lambda\ge0:V_n+\lambda P_n\text{ is convex}\}\) and \(\eta\) is the largest coefficient in \(P_n=\eta V_n+(1-\eta)P_n\). Equivalently, \(V_n+(n-1)P_n=nP_n\), and that equality fails for every \(0\le\lambda<n-1\) with the corresponding scaling \((1+\lambda)P_n\). The three-dimensional exceptional case is a simplex with \(c(V_3)=3\) and \(\eta(P_3)=1/4\).

The *index equality alone is not claimed to be new*: it is also obtainable by combining the general vertex-generation boundary principle of Artstein-Avidan, Falah and Slomka with the classical simplex facets and the inclusion \(-P_n\subseteq(n-1)P_n\). The distinct theorem here is that **every Euclidean-nearest vertex provides the exact optimal decomposition, with linear-time construction**, uniformly in every dimension.

## Assumptions and scope

All convexity and Minkowski sums are Euclidean and ordinary (no closure or asymptotic limit). The integer \(n\ge4\) is arbitrary, the parity restriction uses the product of coordinate signs, and \(P_n\) is full dimensional. A *nearest vertex* is Euclidean nearest, equivalently maximizes \(\langle x,v\rangle\), since all vertices have norm \(\sqrt n\). Tie-breaking is arbitrary. In particular, when some coordinate of \(x\) vanishes, choose its sign to obtain even parity, while when every coordinate is nonzero with odd sign parity, flip a sign of minimum absolute coordinate. Our threshold convention is \(\lambda\) multiplying the convex hull in \(V+\lambda\operatorname{conv}(V)\). For the vertex-generation parameter, \(\eta=1/(1+\lambda)\). An explicit description of the parity-polytope facets is proved below rather than assumed.

## Proof

**1. Complete halfspace description.** Let \(S_n=\{s\in\{-1,1\}^n:\prod_i s_i=-1\}\). We first prove
\[
P_n=\left\{z\in[-1,1]^n:\sum_i s_i z_i\le n-2\text{ for every }s\in S_n\right\}=:Q_n.
\]
Every even vertex belongs to \(Q_n\): against an odd sign vector it disagrees in an odd and therefore nonzero number of coordinates. Conversely take any real linear functional \(z\mapsto\langle a,z\rangle\). If some \(a_i=0\), one can choose signs on zero coordinates to make an even vertex attaining the cube maximum \(\sum_i|a_i|\), so \(\max_{Q_n}\langle a,z\rangle=\max_{P_n}\langle a,z\rangle=\sum_i|a_i|\). If all coordinates are nonzero and the sign vector of \(a\) is even, the same conclusion holds. If it is odd, put \(m=\min_i|a_i|>0\), \(s_i=\operatorname{sgn}(a_i)\), and write \(a_i=s_i(m+|a_i|-m)\). For \(z\in Q_n\),
\[
\langle a,z\rangle=m\langle s,z\rangle+
\sum_i(|a_i|-m)s_i z_i
\le m(n-2)+\sum_i(|a_i|-m)=\sum_i|a_i|-2m.
\]
Flipping one minimum-absolute-value sign of \(s\) gives an even vertex with equality. Thus \(Q_n\) and \(P_n\) have identical support functions in every direction, so they coincide.

**2. A nearest vertex always gives a decomposition.** Fix \(x\in P_n\) and any maximizing \(v\in V_n\). Multiply coordinate \(i\) by \(v_i\), preserving parity and \(P_n\), to reduce to \(v=\mathbf1\) and a new point \(z\in P_n\) for which \(\mathbf1\) maximizes \(\langle z,w\rangle\) over all even vertices \(w\). In particular, flipping any two coordinates yields
\[
z_i+z_j\ge0\qquad(i\ne j).
\]
We show that \(y=(nz-\mathbf1)/(n-1)\) lies in \(P_n\). The upper coordinate bounds \(y_i\le1\) follow from \(z_i\le1\). For a negative coordinate \(z_i\), every other coordinate satisfies \(z_j\ge-z_i\); the odd sign vector having one negative sign at position \(i\) therefore gives
\[
n(-z_i)\le-z_i+\sum_{j\ne i}z_j\le n-2.
\]
Hence \(z_i\ge-(n-2)/n\) and \(y_i\ge-1\). The lower bound is immediate when \(z_i\ge0\).

It remains to verify all odd-sign inequalities. Let \(s\in S_n\) have \(d\) negative entries, so \(d\) is odd. For \(d=1\), since \(\langle s,\mathbf1\rangle=n-2\), the inequality \(\langle s,z\rangle\le n-2\) implies
\[
\langle s,y\rangle=\frac{n\langle s,z\rangle-(n-2)}{n-1}\le n-2.
\]
For \(d\ge3\), the pairwise-sum inequalities imply that the sum over **any** set of at least two coordinates is nonnegative: at most one coordinate is negative, and every other is at least its absolute value. Therefore the sum of the \(d\) coordinates carrying a negative sign is nonnegative, while the complementary \(n-d\) coordinates sum to at most \(n-d\). Hence \(\langle s,z\rangle\le n-d\). Consequently
\[
\langle s,y\rangle\le\frac{n(n-d)-(n-2d)}{n-1}\le n-2,
\]
where the final inequality is precisely \((n-2)(d-2)\ge2\), true for every \(n\ge4\), \(d\ge3\). The facet description now yields \(y\in P_n\). Undo the even sign change to obtain \((nx-v)/(n-1)\in P_n\) for **every** maximizing vertex. Therefore \(nP_n\subseteq V_n+(n-1)P_n\); the reverse inclusion is automatic. For \(\lambda>n-1\), the convex combination of the just-constructed witness with \(x\) also gives \((1+\lambda)P_n\subseteq V_n+\lambda P_n\).

**3. Exact sharpness from an exposed simplex.** Fix any odd sign vector \(s\in S_n\). The exposed face \(F_s=P_n\cap\{z:\langle s,z\rangle=n-2\}\) has exactly \(n\) vertices
\[
v^{(j)}=s-2s_j e_j\quad(1\le j\le n),
\]
which are affinely independent; it is an \((n-1)\)-simplex. Its centroid is \(x_s=(1-2/n)s\). If \((1+\lambda)x_s=v+\lambda p\) with \(v\in V_n\), \(p\in P_n\), exposedness forces \(v,p\in F_s\). In the simplex \(F_s\), every barycentric coordinate of \(x_s\) is \(1/n\). The representation \(x_s=(v+\lambda p)/(1+\lambda)\) requires the coordinate of \(v\) to be at least \(1/(1+\lambda)\), so \(1/(1+\lambda)\le1/n\), or \(\lambda\ge n-1\). At \(\lambda=0\), the centroid is not a vertex, so failure holds as well. This gives \(c(V_n)\ge n-1\), completing the equality and proving that the nearest-vertex certificate is sharp in its scaling.

**4. Dimension three.** \(V_3\) consists of four affinely independent vertices, so \(P_3\) is a tetrahedron. Its barycenter has four equal barycentric coordinates; the same simplex-coordinate argument gives \(c(V_3)=3\), and the standard maximal-coordinate selection supplies the converse. This is outside the theorem's \(n\ge4\) regime.

## Verification

`verification/check_demicube.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. It checks every defining parity vertex and eight representative forbidden-simplex facets in dimensions \(4\le n\le8\), including all their lower-threshold vertex obstructions. It additionally checks pairwise vertex midpoints and reproducibly sampled rational convex combinations, verifying the complete halfspace description and all tied nearest-vertex decompositions at the claimed threshold; the dimension-three exception is tested. Execute `python3 verification/check_demicube.py` to obtain `EXACT_OK 7927`. These are finite consistency checks, not a proof of the quantified all-dimensional theorem; that proof is given above.

## Relationship to prior work

Meyer's 2026 study of finite convexification develops general exposed-face criteria for \(A+\lambda K\) to become convex and identifies the Schneider index when \(K=\operatorname{conv}(A)\). Artstein-Avidan, Falah and Slomka develop the equivalent vertex-generated-polytope framework, including a **boundary-to-body criterion**: if \(-P\subseteq(n-1)P\) and all facets are \(1/n\)-vertex-generated, then \(P\) is \(1/n\)-vertex-generated. The demihypercube has simplex facets and lower-dimensional demihypercube facets; every facet has universal vertex-generation weight at least \(1/n\). Moreover, \(-P_n\subseteq(n-1)P_n\): when \(n\) is even this follows from central symmetry, and when \(n\) is odd every negative even-sign vertex is an odd sign vector, whose scaling by \(1/(n-1)\) satisfies every coordinate and odd-sign facet inequality. Thus those earlier general principles **already imply** \(\eta(P_n)\ge1/n\), and the simplex facet proves the opposite bound. No originality is asserted for this index identity as an isolated statement.

The new statement is stronger and genuinely *pointwise*: **every Euclidean-nearest vertex** of every \(x\in P_n\) yields a feasible scaled remainder, and this vertex is selected in linear time by a parity-corrected sign rule. The general boundary-to-body criterion and Minkowski finite-convexification theorem merely establish existence of an unspecified vertex; they do not imply that every minimizing Euclidean choice works. The explicit pair-flip inequalities and complete parity-facet verification furnish the additional constructive geometry. The dimension-four demihypercube is a cross-polytope and is not claimed as a new example of an index; the uniform nearest-vertex result, especially for all \(n\ge5\), is the focus. The demihypercube facets themselves are classical.

## Limitations

The sharp formula is established only for alternating vertices of the cube, not arbitrary binary linear codes, general Boolean subpolytopes, or other types of uniform polytopes. The class of all possible vertex witnesses is not classified: the theorem proves that all *nearest* witnesses work. No independent mathematical audit or definitive historical-priority certification has been performed. Search coverage of older terminology for parity polytopes and half-cubes may be incomplete.

## References

1. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1 (first posted 2026-10-19), https://arxiv.org/abs/2610.26744 .
2. Shiri Artstein-Avidan, Tomer Falah and Boaz A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604v1 (2024); *Pure and Applied Functional Analysis* 10 (2025), 1171–1192, https://arxiv.org/abs/2407.20604 .
3. Rolf Schneider, *A measure of convexity for compact sets*, *Pacific Journal of Mathematics* 58 (1975), 617–625.
4. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti and Artem Zvavitch, *The convexification effect of Minkowski summation*, *EMS Surveys in Mathematical Sciences* 5 (2018), 1–64.
