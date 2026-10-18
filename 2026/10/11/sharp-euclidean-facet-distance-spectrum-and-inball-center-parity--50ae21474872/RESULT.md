# Exact Euclidean facet-distance spectrum and inball-center parity for fan-graph symmetric edge polytopes

## Finding

Let \(m\ge3\), let \(F_m=K_1*P_m\) be the fan formed from a path \(v_1,\ldots,v_m\) and a hub \(h\), and give
\[
H_m=\left\{y\in\mathbb R^{m+1}:\sum_{a\in V(F_m)}y_a=0\right\}
\]
the Euclidean metric inherited from \(\mathbb R^{m+1}\). Put
\[
\mathcal P_m=\operatorname{conv}\{\pm(e_a-e_b):ab\in E(F_m)\}\subset H_m,
\qquad N=m+1.
\]
The generating polynomial of *all facets*, classified by the numbers of positive, negative and zero entries in a hub-relative polar potential, is
\[
\boxed{\Phi_m(u,v,w)=(u,v,0,w)
\begin{pmatrix}
 u&0&w&0\\
 0&v&w&0\\
 u&v&0&w\\
 u&v&0&0
\end{pmatrix}^{m-1}
\begin{pmatrix}1\\1\\1\\0\end{pmatrix}.}
\]
Precisely, \([u^pv^qw^z]\Phi_m\), for \(p+q+z=m\), counts facets whose outward polar normal has squared Euclidean norm
\[
\boxed{L(p,q,z)=p+q-\frac{(p-q)^2}{m+1}.}
\]
Each such facet has supporting-hyperplane distance \(L(p,q,z)^{-1/2}\) from the origin. The full distance multiplicity distribution is obtained by summing coefficients with equal \(L\); different monomials can produce the same distance.

Let \(\varepsilon_m=0\) for odd \(m\), and \(\varepsilon_m=1\) for even \(m\). The Euclidean inradius, maximized over **all** possible centers, is
\[
\boxed{r(\mathcal P_m)=\left(m-1-\frac{\varepsilon_m}{m+1}\right)^{-1/2}.}
\]
The origin-centered optimal ball touches exactly two facets for odd \(m\), and exactly four for even \(m\). If \(\mathcal C_m\) denotes the set of centers of *every* optimal-radius inscribed ball, then
\[
\boxed{\dim\operatorname{aff}(\mathcal C_m)=
\begin{cases}m-1,&m\text{ odd},\\m-2,&m\text{ even}.\end{cases}}
\]

## Hypotheses and conventions

All graph edges are simple, unweighted and undirected. The coordinates above use the canonical orthonormal basis of \(\mathbb R^{m+1}\); an arbitrary lattice or affine equivalence need not preserve these distances. For \(m=2\), the fan is a triangle whose six polar vertices have the same squared norm \(2/3\); the contact-count and center-dimension statements above are not asserted there. The generating polynomial records **facets** (equivalently, polar vertices), not face-lattice or Ehrhart classes.

## Proof

### 1. Polar facets as constrained path words

Taking the polar in \(H_m\) gives
\[
\mathcal P_m^\circ=\{f\in H_m: |f_a-f_b|\le1\text{ for all }ab\in E(F_m)\}.
\]
A point of this full-dimensional polytope is a vertex exactly when the normals of its tight edge inequalities span \(H_m\). The incidence vectors of a graph span its zero-sum hyperplane exactly when that graph is connected. Hence a polar point is a vertex exactly when its **tight-edge graph is connected**.

Choose the hub as the potential origin and write \(x_i=f_{v_i}-f_h\). Every vertex has a tight spanning tree, so each \(x_i\) is an integer sum of unit jumps along that tree. Since the hub edges impose \(|x_i|\le1\), we have \(x_i\in\{-1,0,1\}\). The path constraints prohibit adjacent opposite signs, since their potential difference would have absolute value two. Every nonzero \(x_i\) connects directly to the hub by a tight edge. A zero \(x_i\) has no tight hub edge, so it belongs to the tight component of the hub exactly when at least one adjacent path entry is nonzero. Therefore the exact polar vertices, one per facet, correspond bijectively to the words \(x\in\{-1,0,1\}^m\) satisfying
\[
|x_i-x_{i+1}|\le1\quad(1\le i<m),
\qquad
x_i=0\implies(x_{i-1}\ne0\text{ or }x_{i+1}\ne0),
\]
where only existing neighbors are used at the endpoints. Necessity has just been shown; sufficiency follows because every path vertex is then incident to a tight hub edge or a tight path edge joining it to a vertex already joined to the hub. The hub-relative representation is unique.

For a word with \(p\) plus signs, \(q\) minus signs and \(z\) zeros, center its representative \((0,x_1,\ldots,x_m)\) by subtracting the mean \((p-q)/(m+1)\). The squared Euclidean norm is
\[
\sum_{i=1}^m x_i^2-\frac{(\sum_i x_i)^2}{m+1}
=p+q-\frac{(p-q)^2}{m+1}=L(p,q,z).
\]
Since the facet plane corresponding to this polar normal \(f\) is \(\langle f,y\rangle=1\), its distance from zero is \(1/\|f\|_2\).

### 2. A complete four-state transfer law

Read a valid word from left to right. Use states \(+\), \(-\), \(0_s\) (a zero supported by its immediate left nonzero neighbor), and \(0_p\) (a zero pending support from its immediate right neighbor). The first position contributes weights \((u,v,0,w)\): a first zero must be pending. The admissible transitions, with the weight of the **new** symbol, are
\[
\begin{array}{c|cccc}
 &+&-&0_s&0_p\\\hline
 +&u&0&w&0\\
 -&0&v&w&0\\
 0_s&u&v&0&w\\
 0_p&u&v&0&0
\end{array}
\]
Here an interior pair of zeros can occur when the first is supported on the left and the second is pending support on the right; a run of three zeros is impossible. Pending zeros cannot terminate a word, so the accepting column is \((1,1,1,0)^\mathsf T\). Multiplying the first-position row by the transition matrix \(m-1\) times and the accepting column gives exactly \(\Phi_m\). No word is duplicated and every valid word is counted; the coefficient statement follows from the centered norm formula.

### 3. Global maximum polar norm and the contact facets

If a valid word contains both signs, at least one zero separates positive from negative entries. If it contains at least two zeros, then \(L\le p+q\le m-2\). With exactly one zero, \(p+q=m-1\), so
\[
L=m-1-\frac{(p-q)^2}{m+1}.
\]
Its maximum is attained precisely for a most balanced split: \(p=q\) when \(m\) is odd, and \(|p-q|=1\) when \(m\) is even. With only one zero, the prohibition on adjacent opposite signs forces the word to be a constant-sign block, one zero, then the opposite constant-sign block. The zero is adjacent to both blocks, so these candidates are valid. There are two such words for odd \(m\) and four for even \(m\), counting global sign reversal.

If a word has only one sign, say \(k\) entries of \(+1\), its squared norm is \(k-k^2/(m+1)\le (m+1)/4\). For every \(m\ge3\), this is strictly smaller than \(m-1-\varepsilon_m/(m+1)\). The all-zero word is not a polar vertex. Consequently the **global** maximum of \(\|f\|_2^2\) is \(m-1-\varepsilon_m/(m+1)\), with exactly the two or four listed maximizers.

### 4. Inradius among arbitrary centers

A ball \(B(c,r)\subset H_m\) lies in \(\mathcal P_m\) exactly when
\[
\langle f,c\rangle+r\|f\|_2\le1
\qquad\text{for every polar vertex }f.
\]
The polar vertices are centrally symmetric. Apply this inequality to \(f\) and \(-f\) to obtain \(r\|f\|_2+|\langle f,c\rangle|\le1\), hence \(r\le1/\max_f\|f\|_2\). This bound is attained with center \(c=0\), proving the global inradius formula and counting its exactly tangent facets.

At optimal radius every maximizing antipodal pair forces \(\langle f,c\rangle=0\). Conversely each other facet inequality has **strict** slack when \(c=0\), and there are finitely many facets; therefore a neighborhood of zero *within the common orthogonal kernel of the contact normals* consists of valid optimal centers. Thus
\[
\dim\operatorname{aff}(\mathcal C_m)=m-\operatorname{rank}\operatorname{span}\{\text{contact normals}\}.
\]
For odd \(m\), the two normals are negatives, so their rank is one. For even \(m\), the four are two antipodal pairs from distinct positions of the unique zero. Their hub-relative word vectors are neither equal nor negatives, and their centered representatives are linearly independent (each has a different zero coordinate and a different cut position). Their rank is two. This proves the claimed parity dimensions.

## Finite verification and its limits

As a separate check, exact integer/rational enumeration of ternary path words and an independently implemented four-state transfer recurrence agree for every \(2\le m\le10\), totaling 6,846 polar vertices. Direct squared-norm comparisons give the expected maxima and two/four equality words for \(3\le m\le10\); exact rational linear algebra gives contact-normal rank one/two according to parity. The \(m=2\) boundary has six equal-norm facets. These finite checks neither establish the infinite-family theorem nor establish literature priority; the proof above supplies the all-integer argument.

## Relation to previous mathematics

D'Alì, Delucchi and Michałek (arXiv:1910.05193) develop general combinatorial and metric perspectives on symmetric edge polytopes. Chen, Davis and Korchevskaia (arXiv:2107.12315) describe the general facet/maximal-bipartite-subgraph correspondence. Braun and Bruegge (arXiv:2201.13303; Journal of Integer Sequences 26 (2023), Article 23.7.2) study facets of sparse graph families using tight-potential criteria. Kálmán and Tóthmérész (arXiv:2203.17127) study lattice and Ehrhart invariants using spanning-tree activities. These starting points do not, by themselves, compute the Euclidean length spectrum of all fan normals or the dimension of the optimal inball-center locus. This formulation is an exact result for the fan family in its *inherited* Euclidean metric, not a new general facet criterion.

## Limitations

No conclusion is asserted for arbitrary graphs, weighted edges, alternative Euclidean normalizations, or the exceptional \(m=2\) contact law. An equivalent result might exist under graph-Lipschitz or support-function terminology; comparison of cited facet theorems alone does not certify absolute novelty. All historical proof and computation claims refer solely to their explicitly stated mathematical scopes.

## References

1. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193.
2. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315; Discrete Applied Mathematics (2022).
3. B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303; Journal of Integer Sequences 26 (2023), Article 23.7.2.
4. T. Kálmán and L. Tóthmérész, *h-vectors of graph polytopes using activities of dissecting spanning trees*, arXiv:2203.17127.
