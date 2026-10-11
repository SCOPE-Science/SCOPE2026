# Sharp Euclidean facet-distance spectrum and inball-center parity for fan-graph symmetric edge polytopes

## Finding
For every integer \(m\ge3\), let \(F_m=K_1*P_m\) be the fan graph: a path on vertices \(v_1,\ldots,v_m\) together with one hub \(h\) adjacent to every path vertex. Let
\[
\mathcal P_m=\operatorname{conv}\{\pm(e_a-e_b):ab\in E(F_m)\}
\subset H_m=\{y\in\mathbb R^{m+1}:\sum_a y_a=0\},
\]
with the inherited standard Euclidean metric. Write \(N=m+1\). A complete generating function for its facet-distance spectrum is
\[
\Phi_m(u,v,w)=(u,v,0,w)T(u,v,w)^{m-1}(1,1,1,0)^{\mathsf T},
\qquad
T=\begin{pmatrix}
u&0&w&0\\
0&v&w&0\\
u&v&0&w\\
u&v&0&0
\end{pmatrix}.
\]
For each triple of nonnegative integers \((p,q,z)\) with \(p+q+z=m\), the coefficient \([u^pv^qw^z]\Phi_m\) is the number of facets whose (polar) outward normal has squared norm
\[
L(p,q,z)=p+q-\frac{(p-q)^2}{N}.
\]
Thus the corresponding supporting-hyperplane distance from the origin is \(L(p,q,z)^{-1/2}\), and coefficients of equal \(L\) are added to obtain the distance multiplicities. The exact radius of a largest inscribed Euclidean ball is
\[
r(\mathcal P_m)=\left(m-1-\frac{\varepsilon_m}{m+1}\right)^{-1/2},
\qquad
\varepsilon_m=\begin{cases}0,&m\text{ odd},\\1,&m\text{ even}.\end{cases}
\]
Exactly two facets (odd \(m\)) or four facets (even \(m\)) touch the origin-centered ball of this radius. If \(\mathcal C_m\) is the set of centers of all maximum-radius Euclidean balls contained in \(\mathcal P_m\), then
\[
\dim\operatorname{aff}(\mathcal C_m)=
\begin{cases}m-1,&m\text{ odd},\\m-2,&m\text{ even}.\end{cases}
\]

## Assumptions and scope
The graph is simple, undirected, and unweighted. The metric on \(H_m\) is the standard Euclidean metric induced by the coordinates \((h,v_1,\ldots,v_m)\); arbitrary lattice equivalences are not assumed Euclidean. We assume \(m\ge3\). The small excluded graph \(F_2=K_3\) has six equally distant facets, so the claimed parity formula does not extend to it. The generating polynomial counts facets with multiplicity; different triples may determine the same distance. The result is about the polytope itself, not solely its graph-theoretic adjacency or Ehrhart data.

## Proof
**Polar vertices and their exact norms.** In the zero-sum hyperplane, the polar is
\[
\mathcal P_m^\circ=\{f\in H_m:|f_a-f_b|\le1\text{ for every }ab\in E(F_m)\}.
\]
An inequality is tight on an edge exactly when the potential difference has absolute value one. An element of this polar is a vertex if and only if the graph of tight edges is connected: the tight edge differences span the \(m\)-dimensional zero-sum space exactly when this graph is connected. Consequently, for a vertex the potential difference from the hub is integer, because a tight spanning tree connects every vertex to the hub. The hub edges bound those differences by one, hence every vertex has a representative \((0,x_1,\ldots,x_m)\) with \(x_i\in\{-1,0,1\}\). Adjacent opposite signs are impossible because a path-edge difference of two violates the polar constraint. Every nonzero path value gives a tight hub edge. A zero path vertex is not tight to the hub; it is connected in the tight graph if and only if at least one neighboring path value is nonzero. These conditions are sufficient for a connected tight-edge graph and hence characterize all polar vertices without duplication. Centering the representative by subtracting its coordinate mean, with \(p\) positive, \(q\) negative and \(z\) zero path entries, gives
\[
\|f\|_2^2=p+q-\frac{(p-q)^2}{m+1}.
\]
Each polar vertex determines a facet plane \(\langle f,y\rangle=1\), at distance \(1/\|f\|_2\) from the origin.

**Transfer matrix and the full spectrum.** Read the path values from left to right, using four states: positive, negative, zero already supported by a nonzero immediate left neighbor, and zero still requiring a nonzero immediate right neighbor. A positive value may be followed only by another positive value or a satisfied zero; a negative value obeys the analogous rule. A satisfied zero may be followed by a positive value, a negative value, or a pending zero. A pending zero must be followed by a nonzero value. Weight each positive, negative and zero by \(u,v,w\), respectively. The first-value weight row is \((u,v,0,w)\), and only the first three final states are accepted. This yields exactly \(\Phi_m\) above and proves both that every allowed path is counted once and that no forbidden path is counted. The norm formula then converts every coefficient into the full facet-distance spectrum.

**Sharp inradius and equality.** If a valid path contains both positive and negative entries, it must contain a zero between them. With at least two zeros, its norm is at most \(m-2\). With exactly one zero, write the counts \(p+q=m-1\). Its squared norm is \(m-1-(p-q)^2/(m+1)\), maximized by balancing the positive and negative counts. The minimum possible value of \(|p-q|\) is zero for odd \(m\), and one for even \(m\). In these cases the single zero must be at the transition between two constant-sign blocks. There are exactly two maximizers for odd \(m\) (opposite signs with zero at the middle) and four for even \(m\) (both signs with the zero at either central position). If a path contains only one sign and zeros, its norm is \(k-k^2/(m+1)\) for some \(0\le k\le m\), which is at most \((m+1)/4\). For \(m\ge3\), this is strictly less than \(m-1-\varepsilon_m/(m+1)\). Thus the stated maximum squared polar-normal norm holds globally and the list of equality cases is complete. By central symmetry, a ball of radius \(r\) centered at \(c\in H_m\) is contained in the polytope exactly when
\[
\langle f,c\rangle+r\|f\|_2\le1\quad\text{for each polar vertex }f.
\]
Applying this inequality to \(f\) and \(-f\) gives \(r\le1/\max_f\|f\|_2\), while equality is achieved at \(c=0\). This proves the global, rather than merely origin-centered, inradius formula.

**All optimal centers.** At the optimal radius the inequalities for contact normal pairs \(\pm f\) force \(\langle f,c\rangle=0\). Conversely, all other polar vertices have a strictly positive slack at the origin; because there are finitely many, an open neighborhood of the origin in the common contact-normal kernel consists of valid optimal centers. Hence the affine dimension of the full optimal-center set is \(m\) minus the rank of the contact normals. For odd \(m\), the two contact normals are antipodes and have rank one. For even \(m\), the four are two distinct antipodal pairs: the two sign-transition patterns have their single zeros at different path positions and are not scalar multiples (indeed each has entries in \(\{-1,0,1\}\) before centering, with different differences from the hub). Thus their rank is two. This yields the asserted dimensions.

## Verification
A standalone standard-library Python checker, `verify.py`, enumerates the tight-edge polar vertices directly for every \(2\le m\le10\), independently checks the four-state transfer counts, computes all squared polar norms exactly as rational numbers, and checks the extremal facet counts and contact-normal ranks. It passes on 6,846 enumerated polar vertices, including the excluded boundary case \(m=2\). The all-dimensional conclusion is a symbolic proof; finite testing alone is not used as proof.

## Relationship to prior work
D’Alì, Delucchi and Michałek developed combinatorial and metric-space perspectives on symmetric edge polytopes (arXiv:1910.05193). Chen, Davis and Korchevskaia established a general relationship between their facets and maximally bipartite subgraphs (arXiv:2107.12315). Braun and Bruegge described tight potential criteria and facets for graphs with few edges (arXiv:2201.13303); Kálmán and Tóthmérész treated graph-polytope \(h^*\)-vectors using activities (arXiv:2203.17127). Those general structural results motivate the present specialization, but the examined passages do not calculate this complete fan-family Euclidean support-distance spectrum, the parity-dependent maximum-distance class, or the affine dimension of all optimal-ball centers. The present result is an exact Euclidean calculation and is not implied by combinatorial equivalence or facet counts alone.

## Limitations
The claimed generating polynomial is specialized to fan graphs \(K_1*P_m\), and the Euclidean conclusions depend on the stated inherited metric. The small graph \(m=2\) is deliberately excluded from the inradius contact-count and optimal-center formula. No assertion is made that the result is the first possible equivalent theorem in other terminology; graph Lipschitz-variance or metric-polytope formulations may overlap with uninspected literature. The finite verifier checks only \(m\le10\); the infinite result relies on the proof.

## References
- A. D’Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first public 2019-10-11), https://arxiv.org/abs/1910.05193.
- T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public 2021-07-26), https://arxiv.org/abs/2107.12315.
- B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303, https://arxiv.org/abs/2201.13303.
- T. Kálmán and L. Tóthmérész, *h*-vectors of graph polytopes using activities of dissecting spanning trees*, arXiv:2203.17127, https://arxiv.org/abs/2203.17127.
