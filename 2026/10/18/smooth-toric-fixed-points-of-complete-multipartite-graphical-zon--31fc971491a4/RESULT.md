# Smooth toric fixed points of complete-multipartite graphical zonotopes

## Finding
For every integer \(r\ge3\) and every tuple of positive integers \(\mathbf a=(a_1,\ldots,a_r)\), let \(X_{\mathbf a}\) be the normal projective toric variety of the **normal fan** of the graphical zonotope of the complete multipartite graph \(K_{a_1,\ldots,a_r}\). Write \(s_{\mathbf a}\) for its number of smooth torus-fixed points and \(t_{\mathbf a}\) for all its torus-fixed points.

Let \(x_1,\ldots,x_r\) be indeterminates, \(u_i=e^{x_i}-1\), \(D=\operatorname{diag}(x_1,\ldots,x_r)\), \(U=\operatorname{diag}(u_1,\ldots,u_r)\), and let \(H\) be the \(r\times r\) matrix having diagonal zero and off-diagonal entries one. View \(\mathbf u=(u_1,\ldots,u_r)^\top\) as a column vector. Define formal multivariate exponential generating functions by
\[
S_r(\mathbf x)=\sum_{\mathbf a\ge\mathbf1}\frac{s_{\mathbf a}}{a_1!\cdots a_r!}\prod_{i=1}^r x_i^{a_i},\qquad
T_r(\mathbf x)=\sum_{\mathbf a\ge\mathbf1}\frac{t_{\mathbf a}}{a_1!\cdots a_r!}\prod_{i=1}^r x_i^{a_i}.
\]
Then, taking the part divisible by every \(x_i\) on the right sides,
\[
\boxed{\begin{aligned}
S_r(\mathbf x)&=\left[\prod_{i=1}^r x_i>0\right]
\left(\sum_{i\ne j}(x_i u_j+u_i x_j-x_i x_j)+
\mathbf u^\top H D(I-HD)^{-1}H\mathbf u\right),\\
T_r(\mathbf x)&=\left[\prod_{i=1}^r x_i>0\right]
\mathbf u^\top H(I-UH)^{-1}\mathbf u.
\end{aligned}}
\]
Here the bracket means retaining only monomials with positive exponent in **every** variable, and the inverses are formal power series with constant term the identity. Equivalently, the coefficient of \(\prod x_i^{a_i}\) in the unprojected right side gives the stated count whenever every \(a_i\ge1\).

A fixed point is smooth **if and only if** the canonical alternating sequence of its maximal monochromatic blocks has exactly two blocks with one singleton, or has at least three blocks and every strictly interior block is a singleton. For \(r\ge3\) and all color classes nonempty, only the latter case occurs. This completely classifies smooth torus-fixed points across the multipartite family, over any algebraically closed field and in arbitrary characteristic.

For example, the triples \(\mathbf a=(1,2,2),(2,2,2),(2,2,3)\) have respectively \(58,288,1240\) smooth torus-fixed points out of \(78,426,2286\) total.

## Assumptions and scope
Let \(n=\sum_{i=1}^r a_i\), \(M=\{(m_1,\ldots,m_n)\in\mathbb Z^n:\sum m_i=0\}\), and \(N=\operatorname{Hom}(M,\mathbb Z)\). In \(M_{\mathbb R}\) form the graphical zonotope as the sum of edge segments \([0,e_i-e_j]\) over pairs in different color classes. The variety uses the **normal fan** in \(N_{\mathbb R}\), not the face fan or the projective edge-monomial toric variety. Only smoothness and counts of zero-dimensional torus orbits are asserted. The known two-color specialization is background; the theorem is stated for at least three colors.

## Proof
**Orientations and blocks.** Vertices of a graphical zonotope correspond to acyclic orientations of the graph. In any acyclic orientation, all topological orders differ by adjacent swaps of incomparable vertices. Vertices in different color classes are joined by an edge and thus are comparable; therefore the ordered word of color classes is uniquely determined by the orientation. Maximal same-color runs yield an intrinsic ordered sequence \(B_1,\ldots,B_\ell\) of nonempty blocks with different colors in successive positions. Conversely, each such labeled block sequence defines exactly one acyclic orientation by directing every edge from its earlier block to its later block. Every vertex appears in exactly one block.

**Hasse diagram and integral regularity.** Between consecutive blocks, every graph edge is a Hasse cover of the reachability order. Edges between nonconsecutive blocks are transitive, witnessed by directed paths through the intervening blocks. The undirected Hasse graph is therefore a chain of complete bipartite graphs on consecutive blocks. It is connected. With two blocks it is a tree exactly when one block is singleton. With three or more blocks, a nonsingleton interior block yields a four-cycle, whereas singleton interior blocks make a tree with possible leaves at its endpoints. The defining inequalities of the full-dimensional normal cone are exactly the Hasse-cover inequalities, with primitive facet normals the signed root vectors \(e_i-e_j\). A cyclic cover graph has more than \(n-1\) distinct facets, so the cone is nonsimplicial. For a tree, its \(n-1\) signed roots form an integral basis of \(M\): deleting one row of the tree incidence matrix leaves determinant \(\pm1\), as follows inductively by peeling leaves. Hence the dual rays form a lattice basis of \(N\), giving a smooth cone. This proves the stated all-characteristic criterion.

**Weighted color walks.** A nonempty labeled block in color \(i\) has exponential weight \(u_i=e^{x_i}-1\); a singleton block has weight \(x_i\). The matrix \(H\) permits a transition precisely when the next block has a different color. For length two, the smooth sequences contribute \(\sum_{i\ne j}(x_i u_j+u_i x_j-x_i x_j)\): inclusion–exclusion handles the two possibilities of a singleton endpoint. For length \(\ell\ge3\), only the two endpoints may have more than one vertex, and all \(\ell-2\) interior blocks are singletons. Their weight-sum is \(\mathbf u^\top H D(HD)^{\ell-3}H\mathbf u\). Summing over lengths is the convergent formal series \(\mathbf u^\top H D(I-HD)^{-1}H\mathbf u\). Without the singleton restriction, a sequence of length \(\ell\ge2\) has total weight \(\mathbf u^\top H(UH)^{\ell-2}\mathbf u\), yielding \(T_r\). Finally extract terms involving every color to ensure all \(r\) classes are present, which proves both formulas.

## Verification
Run `python3 verify.py` using only Python's standard library. For the multipartite color-size patterns \((1,1,1),(1,2,2),(2,2,2),(2,2,3),(1,2,3)\), the script independently enumerates (i) acyclic orientations via all vertex permutations modulo identical directed edge sets and (ii) ordered monochromatic block sequences weighted by labeled multinomial coefficients. Both methods agree on every total and smooth count and the run ends in `VERIFY_OK`. This finite validation is not used as a proof for infinitely many part-size tuples; the symbolic proof is above.

## Relationship to prior work
Postnikov, Reiner and Williams give the general graphical-zonotope/acyclic-orientation correspondence and tree-Hasse-diagram criterion for simple vertices. The bipartite subfamily has already been explicitly enumerated, and is not presented as a new result here. Carballosa, Khera and Reyes use color-run encodings of complete-multipartite acyclic orientations, but their total-orientation census does not supply the regularity-refined multivariate matrix series stated here. Grujić's general zonotope face formula counts faces without imposing the integral local smoothness test. The present extension concerns **all complete multipartite graphs with at least three nonempty color classes**, capturing the proper-color transition matrix absent in the two-class calculation. Targeted searches of simplicial-chamber, smooth-fixed-point and multipartite-graphical-zonotope literature did not locate this full matrix enumeration. That is a qualified comparison, not proof of global novelty.

## Limitations
The result classifies fixed points, not all singular torus orbits or higher-dimensional singular components. It is a combinatorial and lattice statement and therefore does not depend on field characteristic. The old bipartite formula is already known and should not be counted as a separate discovery. Computations verify only the displayed finite parameter instances. An earlier differently phrased complete-multipartite smoothness enumeration remains a possible overlap.

## References
- A. Postnikov, V. Reiner and L. Williams, *Faces of Generalized Permutohedra*, first public arXiv preprint 2006-09-06, arXiv:math/0609184.
- V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931 (2016).
- W. Carballosa, S. Khera and J. Reyes, *Encoding and Enumerating Acyclic Orientations of Graphs*, arXiv:2303.09021 (2023), used as subsequent contextual literature.
