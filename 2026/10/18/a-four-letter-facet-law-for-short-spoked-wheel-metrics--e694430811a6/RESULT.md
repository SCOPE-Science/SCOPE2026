# A four-letter facet law for short-spoked wheel metrics

## Finding

For an integer \(m\ge4\) and a real parameter \(1/2<r<1\), let \(M_{m,r}\) be the \((m+1)\)-point shortest-path metric obtained from a cycle of \(m\) unit-length edges by adjoining a hub with spokes of length \(r\). Let \(\mathcal F(M_{m,r})\) be the **real Lipschitz-free Banach space** of this metric space. The unit ball of \(\mathcal F(M_{m,r})\) has exactly
\[
F_m=\operatorname{tr}(T^m)
=2\cos\!\left(\frac{\pi m}{3}\right)+\lambda_1^m+\lambda_2^m+\lambda_3^m
\]
facets, where \(\lambda_1,\lambda_2,\lambda_3\) are the three complex roots, counted with multiplicity, of
\[
z^3-z^2-3z-2=0.
\]
The integer \(F_m\) is independent of \(r\) throughout the strict interval \((1/2,1)\). Equivalently, the sequence is computed by the \(14\)-state transfer matrix defined below, whose exact characteristic polynomial is
\[
\det(zI-T)=z^9(z^2-z+1)(z^3-z^2-3z-2).
\]
For \(m=4,5,6,7,8,9,10\), these facet counts are respectively \(38,102,252,632,1582,3974,9986\). Their exponential growth rate is the unique positive root \(\alpha\approx2.51154714169453\) of the displayed cubic: \(F_m/\alpha^m\to1\).

This interior law makes the two boundary degenerations explicit. At \(r=1/2\), the number of facets equals \(2^m\). At \(r=1\), the unit wheel has the **previously established** facet count of D'Alì, Delucchi and Michałek (2019, Proposition 4.22); its first values at \(m=4,5,6\) are \(26,62,138\). The new interior value at \(m=4\) is \(38\), compared with \(16\) and \(26\) at the two endpoints. The endpoint results themselves are not asserted to be new.

## Assumptions and scope

All spaces, coordinates and duality pairings are real. Write the vertices of the cycle as \(v_0,\ldots,v_{m-1}\), with subscripts interpreted modulo \(m\), and write \(o\) for the hub. Each rim edge has weight \(1\); each spoke \(ov_i\) has weight \(r\). For \(r\ge1/2\), the induced shortest-path metric satisfies \(d(o,v_i)=r\) and \(d(v_i,v_{i+1})=1\). We consider \(1/2\le r\le1\) only for the endpoint comparisons; the new interior formula requires \(1/2<r<1\).

The dual of \(\mathcal F(M_{m,r})\), with basepoint \(o\), is the real space \(\operatorname{Lip}_0(M_{m,r})\). Its full-dimensional unit ball is
\[
P_{m,r}=\left\{(x_0,\ldots,x_{m-1})\in\mathbb R^m:\ |x_i|\le r,\quad |x_i-x_{i+1}|\le1\quad(0\le i<m)\right\}.
\]
Constraints for nonadjacent pairs follow by summing constraints along shortest paths. Since the zero vector is interior, polar duality identifies facets of the primal unit ball with vertices of \(P_{m,r}\).

## Proof

**1. Exact tight-graph vertex criterion.** Given \(x\in P_{m,r}\), form a graph on \(\{o,v_0,\ldots,v_{m-1}\}\) containing a spoke \(ov_i\) exactly when \(|x_i|=r\), and containing a rim edge \(v_iv_{i+1}\) exactly when \(|x_i-x_{i+1}|=1\). The active normal of any constraint is, up to sign, its graph-edge incidence vector after fixing the hub coordinate to zero. The incidence rank of a graph with \(m+1\) vertices and \(c\) connected components is \(m+1-c\). Consequently the active normals span \(\mathbb R^m\), and hence \(x\) is a vertex, **if and only if** its tight-edge graph is connected. This accounts for every active-constraint degeneracy, without a generic-position hypothesis.

**2. Four possible values.** Suppose \(x\) is a vertex and \(1/2<r<1\). Every rim vertex has a tight-edge path to the hub. The values along the path change by signed steps from the set \(\{r,1\}\), but, after its first spoke edge, all subsequent edges in the path may be taken along the rim. Thus every coordinate has the form \(\pm r+j\) for an integer \(j\). The bound \(|x_i|\le r\) and \(1/2<r<1\) restrict this set to exactly
\[
A:=r,\qquad a:=r-1,\qquad B:=-r,\qquad b:=1-r.
\]
These four values are pairwise distinct in the strict parameter interval. The only disallowed adjacency of alphabet symbols is an \(A,B\) pair in either order, since \(|A-B|=2r>1\); all other symbol pairs satisfy the rim Lipschitz constraint. Moreover, rim edges are tight **only** for \(A\)-\(a\) and \(B\)-\(b\) pairs. The symbols \(A,B\) have tight spokes and \(a,b\) do not.

Therefore a feasible cyclic word is a vertex precisely when each occurrence of \(a\) has at least one neighboring \(A\), and each occurrence of \(b\) has at least one neighboring \(B\). Necessity follows from the tight-graph connectivity criterion. Sufficiency follows because every \(a\) or \(b\) is then directly tight-adjacent to a vertex \(A\) or \(B\) with a tight spoke. Every rim vertex is in the hub's tight component. This is an exhaustive classification, including alternating and repeated-letter boundary cases.

**3. Finite transfer matrix.** Let \(\Sigma=\{A,a,B,b\}\), and define the \(14\)-element ordered-pair set
\[
\mathcal S=\{(u,v)\in\Sigma^2:(u,v)\ne(A,B),(B,A)\}.
\]
Index a \(14\times14\) matrix \(T\) by \(\mathcal S\). Its entry from \((u,v)\) to \((v',w)\) is \(1\) precisely when \(v=v'\) and the central symbol \(v\) satisfies the local rules
\[
v=a\Longrightarrow(u=A\ \text{or}\ w=A),\qquad
v=b\Longrightarrow(u=B\ \text{or}\ w=B),
\]
with the entry \(0\) otherwise. By the state definition, all successive pairs in a permitted transition also obey the adjacency restriction. Taking \(\operatorname{tr}(T^m)\) enumerates each length-\(m\) cyclic word satisfying precisely the vertex rules, with its fixed labeled rim positions. No quotient by rotations or reflection is taken. This establishes \(F_m=\operatorname{tr}(T^m)\).

For completeness, compute the characteristic polynomial by the finite, exact determinant (or by Newton's identities applied to the integer traces of \(T,T^2,\ldots,T^{14}\)):
\[
\det(zI-T)=z^9(z^2-z+1)(z^3-z^2-3z-2).
\]
The exact computation is reproduced using only integer arithmetic in the accompanying `VERIFY.py`. The trace of a matrix power equals the sum of its eigenvalues raised to that power, counting algebraic multiplicities. The two roots of \(z^2-z+1\) give \(2\cos(\pi m/3)\), and the remaining roots give the announced cubic-root sum. The cubic has discriminant \(-107<0\) and therefore a single real root \(\alpha>2\). Its conjugate nonreal roots have product \(2/\alpha\), hence each has modulus \(\sqrt{2/\alpha}<1\); the quadratic roots have modulus \(1\). Hence the asymptotic \(F_m\sim\alpha^m\) follows directly.

**4. Endpoint comparison.** For \(r=1/2\), the constraints \(|x_i-x_{i+1}|\le1\) follow from the bounds \(|x_i|\le1/2\). Thus \(P_{m,1/2}\) is a cube, with \(2^m\) vertices. For \(r=1\), the wheel is the unweighted graph metric; the above four symbols collapse to three, and the number of vertices is exactly the already-known wheel facet enumeration of D'Alì, Delucchi and Michałek, Proposition 4.22. This proves the asserted contrast and carefully separates the new strict-interior law from previous endpoint work.

## Verification

Run the bundled standard-library script by `python3 VERIFY.py`. It constructs the \(14\)-state matrix directly from the local rules, computes all \(14\) characteristic coefficients using **integer** Newton identities, checks the polynomial, and compares trace counts to exhaustive cyclic-word enumeration through \(m=8\). Independently, for \(m=3,4,5\) and \(r=3/4\), it enumerates all rational vertices of the original inequality polytope by solving every candidate full-rank active-constraint system; the resulting vertex sets match the four-letter classification exactly. It also crosschecks the endpoint counts with independent rational active-basis enumeration. The executable returns `VERIFY_OK`.

The exact determinant calculation is finite because the transfer matrix has constant size. The infinite-family theorem depends on the connected tight-graph proof, not on extrapolation from finitely many small wheels. The proof does not determine higher face numbers, arbitrary spoke profiles, or other norms.

## Relationship to prior work

D'Alì, Delucchi and Michałek (2019), Section 4.3 and Proposition 4.22, give a cyclic three-letter description and the exact facet-count generating function for **unweighted** wheel symmetric edge polytopes, namely the endpoint \(r=1\). The present polytope is the polar of a genuinely **unequally scaled** edge-root hull when \(1/2<r<1\): the spoke generators have scale \(1/r\) and the rim generators have scale \(1\). The four distinct height values and their \(14\)-state transfer law cannot follow by uniform scaling of that endpoint classification; already \(m=4\) has \(38\) rather than \(26\) facets.

Chen, Davis and Korchevskaia (2021), particularly Sections 3–4, describe faces via maximal bipartite subgraphs for unweighted symmetric edge polytopes. Braun and Bruegge (2022) derive facet enumerations for several sparse unweighted graph families. Neither work's stated fixed unweighted generators yields the spoke-weighted wheel result. Jevtić, Timotijević and Živaljević (2018), Theorem 1.1, treat **weighted cycles without an additional hub**, with a Bier-sphere description under generic polygonal-linkage assumptions. This different combinatorial family does not imply the present nongeneric hub-and-rim count.

Related complete-multipartite Lipschitz-free facet formulas treat one common distance between every pair of different parts and another common distance within each part. Even the \(m=4\) metric here, viewed as a weighted \(K_{1,2,2}\), has **two distinct distances across different parts** (hub-to-rim and cycle edges) and so does not satisfy that hypothesis. Uniform-wheel Euclidean ellipsoid and inradius formulas likewise do not imply the facet count of this nonuniform metric family.

## Limitations

The theorem concerns the **real** scalar field, rim length fixed at \(1\), a single common spoke length strictly between \(1/2\) and \(1\), and \(m\ge4\). It does not characterize nonconstant independently weighted spokes, all higher-dimensional face counts, or Banach-space isomorphism types. The baseline endpoint counts and general tight-graph rank criterion are acknowledged prior facts, not independent novelties. Equivalent unpublished or unindexed weighted-wheel metric-polytope work remains possible. The mathematical argument and checks here have not undergone independent validation.

## References

1. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1, first public 11 October 2019, Section 4.3, Proposition 4.22. https://arxiv.org/abs/1910.05193 ; full text https://arxiv.org/html/1910.05193v1.
2. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1, first public 26 July 2021, Sections 3–4. https://arxiv.org/abs/2107.12315.
3. B. Braun and K. Bruegge, *Facets of symmetric edge polytopes for graphs with few edges*, arXiv:2201.13303v1, first public 31 January 2022. https://arxiv.org/abs/2201.13303.
4. F. D. Jevtić, M. Timotijević and R. T. Živaljević, *Polytopal Bier spheres and Kantorovich–Rubinstein polytopes of weighted cycles*, arXiv:1812.00397v1, first public 2 December 2018, Theorem 1.1. https://arxiv.org/abs/1812.00397.
