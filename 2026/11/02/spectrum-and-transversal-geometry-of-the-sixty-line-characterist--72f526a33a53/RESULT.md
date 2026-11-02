# Spectrum and transversal geometry of the sixty-line characteristic-two quartic

## Finding
Let \(\alpha\in\mathbb F_{16}\) be a primitive fifth root of unity and set \(\mu=1+\alpha^2+\alpha^3\in\mathbb F_4\). Let \(X\) be the smooth quartic K3 surface
\[
X=V(s_1,s_4+\mu s_2^2)\subset\mathbb P^4_{\mathbb F_4},
\]
where \(s_i\) is the elementary symmetric polynomial of degree \(i\) in the five ambient coordinates. Let \(G\) be the simple graph on the sixty geometric lines of \(X\), with two vertices adjacent precisely when the corresponding lines intersect.

**Theorem.** The graph \(G\) is connected and \(17\)-regular, with \(510\) edges and adjacency characteristic polynomial
\[
\boxed{\chi_G(t)=(t-17)(t-2)^{40}(t+3)^5(t+4)^4(t+5)^5(t+8)^4(t+9).}
\]
For distinct lines \(L,M\), let \(c(L,M)\) be the number of other geometric lines meeting both. The complete unordered-pair census is

| Geometry of \(L,M\) | \(c(L,M)\) | Number of unordered pairs |
|---|---:|---:|
| Intersecting | \(0\) | \(150\) |
| Intersecting | \(2\) | \(360\) |
| Skew | \(4\) | \(150\) |
| Skew | \(5\) | \(360\) |
| Skew | \(6\) | \(360\) |
| Skew | \(7\) | \(240\) |
| Skew | \(8\) | \(150\) |

In particular, \(G\) has diameter two and exactly \(240\) triangles. Under the natural \(S_5\)-action, the \(150\) skew pairs with the maximum eight common transversals form exactly three orbits, of sizes \(30,60,60\). The \(30\)-element orbit is precisely the set of \(\mathbb F_4\)-Frobenius-conjugate line pairs. Each conjugate pair is skew and has exactly eight common transversals.

## Assumptions and scope
All arithmetic is in characteristic two. The scheme \(X\) and its sixty lines are the concrete Rams–Schütt quartic; their smoothness and line-orbit construction are established in the cited 2015 source, and geometric completeness follows from the cited 2016 nonsupersingular bound. The graph uses *geometric* intersection over \(\overline{\mathbb F}_2\), not just rational-point intersection. A transversal means one of the other sixty lines meeting both specified lines. The statements about pairs concern unordered pairs of distinct geometric lines. The line-set Frobenius in this theorem is the fourth-power map associated with the base \(\mathbb F_4\).

## Proof
Write the five homogeneous coordinates as \((x_0,x_1,x_2,x_3,x_4)\). The cited source provides a line \(\ell\subset X\) given by
\[
s_1=x_3+x_2+(\alpha^3+\alpha+1)x_1
=x_4+(\alpha^3+\alpha^2+\alpha+1)x_2+\alpha x_1=0.
\]
Its \(S_5\)-orbit consists of sixty distinct lines; these are all geometric lines by the characteristic-two bound for nonsupersingular quartics. With \(x_1,x_2\) as free coordinates, the line is spanned by
\[
u=(\alpha^3,1,0,\alpha^3+\alpha+1,\alpha),\qquad
v=(\alpha^4,0,1,1,\alpha^4).
\]
Work in \(\mathbb F_{16}=\mathbb F_2[\theta]/(\theta^4+\theta+1)\). Represent field elements by coefficient-bit masks: \(\alpha=\theta^3\) has integer representation \(8\) and satisfies \(\alpha^5=1\); the corresponding \(\mu\) has representation \(7\). Enumerate all \(120\) coordinate permutations of \((u,v)\), and use the ten Plücker coordinates \(u_iv_j-u_jv_i\), up to nonzero scalar, to identify equal projective lines. This produces exactly sixty distinct lines.

Two distinct lines spanned by \((u,v)\) and \((w,z)\) intersect if and only if the \(5\times4\) matrix with columns \((u,v,w,z)\) has rank at most three, equivalently if all five of its \(4\times4\) maximal minors vanish. This is a finite exact identity over \(\mathbb F_{16}\), not a numerical approximation. Build the symmetric integer adjacency matrix \(A\) from these five-minor tests. Exact integer characteristic-polynomial computation gives the displayed factorization, and the row sums all equal seventeen. Its simple eigenvalue seventeen proves connectivity.

For each pair of distinct vertices \(i,j\), the off-diagonal entry \((A^2)_{ij}=\sum_k A_{ik}A_{kj}\) counts common adjacent lines. Separating pairs according to \(A_{ij}\in\{0,1\}\) and counting the integral entries of \(A^2\) proves the seven-row table: \(510\) adjacent pairs and \(1260\) skew pairs, altogether \(\binom{60}{2}=1770\). Each skew pair has at least four common neighbors, so every two vertices have graph distance at most two; the graph is not complete, hence its diameter is exactly two. Each of the \(360\) edges with two common neighbors lies in exactly two triangles, while the other \(150\) edges lie in none; counting triangle-edge incidences gives \(360\cdot2/3=240\).

For the final orbit statement, represent all \(120\) coordinate permutations on the canonical Plücker list and act on the \(150\) unordered skew pairs satisfying \((A^2)_{ij}=8\). Exhaustive orbit closure gives exactly three orbits with sizes \(30,60,60\). Raising the ten Plücker coordinates to their fourth power gives the Frobenius permutation \(F\); direct finite-field calculation shows \(F^2=1\), with no fixed vertex. All \(30\) conjugate pairs \(\{i,F(i)\}\) are skew and have eight common neighbors. They form the unique orbit of size thirty. This completes the finite proof.

## Verification
Run `python verify.py` with Python 3.10 or newer and SymPy (`requirements.txt`). The code implements finite-field arithmetic, enumerates all sixty lines and their exact pairwise rank tests, computes the integer characteristic polynomial and two-step census, checks all \(S_5\)-orbits and the Frobenius relation, and performs a separate reduced-row-echelon census of all \(357\) ambient lines over \(\mathbb F_4\) and \(70161\) over \(\mathbb F_{16}\). The latter gives zero and sixty contained lines, respectively. The last line of the supplied actual execution output is `VERIFY_OK`. The finite projective-line census and all matrix computations are exhaustive; no inference about arbitrary extension degrees is made from sampling.

## Relationship to prior work
Rams and Schütt (first posted 2015-12-04) constructed \(X\), its sixty-line \(S_5\)-orbit, and the full geometric Néron–Severi lattice of rank twenty and discriminant \(-55\). These are *inputs*, not claimed discoveries. Degtyarev, Itenberg, and Sertöz (first posted 2016-01-17) classified large complex quartic line configurations, including the \(\mathbf X''_{60}\) configuration, and recorded local pencil types. Degtyarev (first posted 2016-04-20) discussed large configurations in positive characteristic. These sources do not explicitly give the displayed adjacency spectrum, seven-stratum two-step incidence census, or the Frobenius-specified maximal-transversal orbit. A separately published spectrum/common-transversal study of the *sixty-four* Schur lines is about a different surface; its results do not determine the present sixty-vertex graph.

## Limitations
The mathematical conclusions are finite-configuration invariants of this explicit characteristic-two surface. This does not classify all quartic line graphs, prove that the graph has no automorphisms outside the specified \(S_5\), or determine integral lattice saturation anew. Since the geometric line configuration is already known, the new information is the exact global spectral/transversal refinement and its arithmetic orbit identification, not the existence or total number of lines. The classification literature may encode enough of the graph to recompute these invariants; no assertion of certified historical priority is made.

## References
1. S. Rams and M. Schütt, *At most 64 lines on smooth quartic surfaces (characteristic 2)*, arXiv:1512.01358 (first posted 2015-12-04), Section 8. https://arxiv.org/abs/1512.01358 ; full-text article: https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/at-most-64-lines-on-smooth-quartic-surfaces-characteristic-2/C9B044DE0B53285E120F886B2761CDA8
2. A. Degtyarev, I. Itenberg, A. S. Sertöz, *Lines on quartic surfaces*, arXiv:1601.04238 (first posted 2016-01-17), especially the large-configuration table. https://arxiv.org/abs/1601.04238
3. A. Degtyarev, *Lines in supersingular quartics*, arXiv:1604.05836 (first posted 2016-04-20), especially Section 8.3. https://arxiv.org/abs/1604.05836
