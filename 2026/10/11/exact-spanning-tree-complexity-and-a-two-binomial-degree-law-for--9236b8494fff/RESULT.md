# Exact spanning-tree complexity and a two-binomial degree law for signohedral flip graphs

## Finding

Let \(n\geq3\) and put \(m=n-1\). For the standard cross-polytope \(\operatorname{conv}\{\pm e_1,\ldots,\pm e_n\}\) and a generic functional satisfying \(0<\varphi(e_1)<\cdots<\varphi(e_n)\), let \(G_m\) denote the one-skeleton of its coherent monotone-path polytope (the signohedron). The published sign-vector correspondence identifies \(G_m\) with the graph induced on \(\{-1,0,1\}^m\setminus\{\mathbf0\}\), where two vectors are adjacent exactly when they differ by one in a single coordinate. Write \(H_m=P_3^{\square m}\) for the same ternary Cartesian grid **including** its center \(o=\mathbf0\).

Set
\[
T_m=\frac1{3^m}\prod_{\substack{a,b\geq0\\1\leq a+b\leq m}}
(a+3b)^{\frac{m!}{a!\,b!\,(m-a-b)!}},
\qquad
\alpha_m=\frac1{3^{m-1}}\sum_{k=0}^{m-1}\binom{m-1}{k}\frac{2^k}{1+3k},
\qquad
\beta_m=\frac{1-3^{-(m-1)}}{2(m-1)}.
\]
Then \(T_m\) is the number of spanning trees of \(H_m\). If \(\mathcal T\) is a uniformly random spanning tree of \(H_m\), the **entire exact distribution of the degree of its central vertex** is
\[
\boxed{\deg_{\mathcal T}(o)\ \overset{d}=\ 1+X_m+Y_m,\quad
X_m\sim\operatorname{Bin}(m,\alpha_m),\quad
Y_m\sim\operatorname{Bin}(m-1,\beta_m),\quad X_m\perp Y_m.}
\]
Consequently the number of spanning trees of the signohedral flip graph is
\[
\boxed{\tau(G_m)=\frac{T_m}{2m}
(1-\alpha_m)^m(1-\beta_m)^{m-1}.}
\]
Moreover,
\[
\deg_{\mathcal T}(o)\ \xrightarrow[m\to\infty]{d}\ 1+\operatorname{Pois}(1),
\qquad
\lim_{m\to\infty}\frac{2m\,\tau(G_m)}{\tau(H_m)}=e^{-1}.
\]
For \(m=2,3,4\), the exact signohedral spanning-tree counts are respectively
\(8\), \(301056000000\), and \(477039212109540892237246917021020454912000000000000\).

## Assumptions and scope

The graph \(P_3\) is the three-vertex **path**, not the triangle or a cyclic ternary Hamming graph. All edges have unit weight unless a variable edge weight is explicitly introduced. The distribution concerns uniformly sampled unrooted spanning trees of the *completed graph* \(H_m\); the tree-count formula concerns the *deleted-center graph* \(G_m\), the one-skeleton of the signohedron. A spanning tree of the underlying cross-polytope and an oriented monotone-path arborescence are different objects.

The range \(m\geq2\) is essential: deleting the middle vertex from \(P_3\) produces two isolated vertices when \(m=1\). The product \(T_m\) is integer by the matrix-tree theorem, and the fractional expression for \(\tau(G_m)\) evaluates to an integer by the leaf-deletion bijection below. All identities are exact and hold for every integer \(m\geq2\).

## Proof

**1. The Cartesian spectral baseline.** The Laplacian of \(P_3\) has orthonormal eigenvectors
\[
q_0=\frac1{\sqrt3}(1,1,1),\quad
q_1=\frac1{\sqrt2}(1,0,-1),\quad
q_3=\frac1{\sqrt6}(1,-2,1),
\]
with respective eigenvalues \(0,1,3\); coordinates are ordered \((-1,0,+1)\). The Laplacian of \(H_m\) is the tensor sum of these one-coordinate Laplacians. Eigenvalue \(a+3b\) occurs with multiplicity \(m!/(a!b!(m-a-b)!)\). The matrix-tree theorem, omitting the sole zero eigenvalue and dividing by \(3^m\), gives \(\tau(H_m)=T_m\).

**2. Weighted trees and the grounded Green matrix.** Let \(N(o)\) be the \(2m\) unit-vector neighbors of \(o\), let \(K\) be the Laplacian of \(H_m\) with the row and column indexed by \(o\) removed, and let \(D\) be diagonal on the remaining vertices with entries \(1\) precisely at \(N(o)\) and \(0\) elsewhere. The punctured graph is connected for \(m\geq2\), so \(K\) is positive definite. If each edge incident to \(o\) receives weight \(t\), the weighted matrix-tree theorem yields
\[
Z_m(t):=\sum_{\mathcal T\text{ spanning tree of }H_m}t^{\deg_{\mathcal T}(o)}
=\det(K+(t-1)D).
\]
Write \(M=(K^{-1})_{N(o),N(o)}\). The determinant lemma gives
\[
Z_m(t)=T_m\det(I_{2m}+(t-1)M).
\]
Since \(K\mathbf1=D\mathbf1\), it follows that \(M\mathbf1=\mathbf1\), so \(1\) is an eigenvalue of \(M\) on the constant neighbor vector.

**3. The two other invariant subspaces.** Signed coordinate permutations fix the center and act transitively on the \(2m\) neighbors. Accordingly, entries of \(M\) depend only on whether a pair consists of the same neighbor, the opposite pair in one coordinate, or neighbors in distinct coordinates. Denote these entries by \(A,B,C\), respectively. Besides the constant eigenvector, the antisymmetric contrasts \(e_{+i}-e_{-i}\) span an \(m\)-dimensional eigenspace of eigenvalue \(\alpha=A-B\). The vectors constant on each opposite pair and summing to zero across pairs span an \((m-1)\)-dimensional eigenspace of eigenvalue \(\beta=A+B-2C\). We calculate both eigenvalues rather than assuming their values.

For every vector \(w\) supported outside \(o\) with coordinate sum zero, grounding at \(o\) and the full-Laplacian pseudoinverse give the same quadratic form:
\(w^{\mathsf T}K^{-1}w=w^{\mathsf T}L(H_m)^+w\).
Take \(w=e_{+i}-e_{-i}\), of squared norm \(2\). In the tensor eigenbasis, only \(q_1\) on coordinate \(i\) contributes, together with arbitrary \(q_0,q_3\) on the other \(m-1\) coordinates. Each other coordinate contributes squared central amplitudes \(1/3,2/3\), respectively. Thus
\[
2\alpha=w^{\mathsf T}K^{-1}w
=2\sum_{k=0}^{m-1}\binom{m-1}{k}
\frac{(1/3)^{m-1-k}(2/3)^k}{1+3k},
\]
which is the stated \(\alpha_m\).

Now take \(w=e_{+i}+e_{-i}-e_{+j}-e_{-j}\) for \(i\ne j\); its squared norm is \(4\) and \(w^{\mathsf T}K^{-1}w=4\beta\). The sum of endpoint values of \(q_0\) is twice its value at the center, whereas the corresponding ratio for \(q_3\) is minus one. Hence the tensor projection of \(w\) vanishes unless exactly one of coordinates \(i,j\) carries \(q_3\); both cases together give squared spectral mass \(4\) times the probability weights from the remaining \(m-2\) coordinates. Its eigenvalue is \(3(1+k)\) if \(k\) other coordinates carry \(q_3\). Therefore, for \(J\sim\operatorname{Bin}(m-2,2/3)\),
\[
4\beta=\frac43\mathbb E\frac1{1+J},
\qquad
\beta=\frac13\mathbb E\frac1{1+J}
=\frac{1-3^{-(m-1)}}{2(m-1)}.
\]
The last equality follows by expanding \(1/(k+1)=\int_0^1 u^k\,du\), or directly summing the binomial identity.

**4. Exact central degree and punctured-tree count.** We have found the full spectrum
\[
\operatorname{spec}(M)=\{1^{(1)},\alpha_m^{(m)},\beta_m^{(m-1)}\}.
\]
The expectation formulas show that \(0<\alpha_m,\beta_m<1\) for every \(m\ge2\), so the displayed binomial factors are genuine probability generating functions. It follows that
\[
\frac{Z_m(t)}{T_m}=
 t(1-\alpha_m+\alpha_m t)^m
 (1-\beta_m+\beta_m t)^{m-1}.
\]
Because this is the probability generating function of \(\deg_{\mathcal T}(o)\), it proves the asserted sum of **independent** binomial random variables plus one. The coefficient of \(t\) in \(Z_m(t)\) counts spanning trees in which \(o\) is a leaf. Every such tree arises uniquely by taking a spanning tree of \(G_m\) and adjoining \(o\) along exactly one of its \(2m\) incident edges. Therefore
\[
[t]Z_m(t)=2m\,\tau(G_m),
\]
and the boxed tree-count identity follows.

**5. Limit.** If \(K_m\sim\operatorname{Bin}(m-1,2/3)\), then \(\alpha_m=\mathbb E[1/(1+3K_m)]\). Binomial concentration and an exponential bound on the lower tail imply \(m\alpha_m\to1/2\). The explicit formula gives \((m-1)\beta_m\to1/2\). Consequently the two independent binomials converge to independent \(\operatorname{Pois}(1/2)\) variables, establishing \(1+\operatorname{Pois}(1)\). Taking their zero-event probabilities gives \((1-\alpha_m)^m(1-\beta_m)^{m-1}\to e^{-1}\), proving the second limit.

## Verification

Run `python3 verify.py` in the same directory as this result. The Python standard-library program constructs the unit-weight adjacency of \(G_m\) independently from the formulas, computes exact Kirchhoff cofactors with integer Bareiss elimination, and checks the resulting spanning-tree counts for \(m=2,3,4\). It then adds the center as a grounded vertex with incident edges of weights \(t=0,1,\ldots,2m+1\), recomputes exact weighted Kirchhoff determinants, and compares them with the predicted central-degree generating polynomial. Its terminal success line is `VERIFY_OK exact Bareiss minors, all stated sample values, and weighted tree polynomials`. The general theorem is established by the proof, not by these finite tests.

## Relationship to prior work

Black and De Loera (2021) identify the signohedral one-skeleton with this punctured ternary Cartesian graph and determine vertex counts and its diameter, but do not state spanning-tree complexity or a central uniform-spanning-tree degree law. Athanasiadis, De Loera, and Zhang (2020) count **oriented arborescences of a linear-functional orientation of a polytope graph** and monotone paths; their trees are not undirected spanning trees of the coherent-path flip graph. A related published calculation of the **pairwise flip-distance enumerator** on the same signohedral graph determines a Wiener index, a different invariant that does not determine the Kirchhoff tree count or the central degree distribution.

The general matrix-tree theorem, Laplacian spectra of Cartesian products, and grounded Green/transfer-current methods are classical tools; originality is claimed for the evaluated two-eigenvalue decomposition, the explicit two-binomial law and its resulting full closed complexity formula in this particular natural geometric family, not for those classical tools or for an abstract determinantal formula. A cyclic three-ary cube uses a triangular coordinate graph and is not the Cartesian product of three-vertex paths used here.

## Limitations

The tree count is for the graph of **coherent** monotone paths, not the larger graph of all monotone paths. The auxiliary probability law is for a random tree of the completed Cartesian grid, not for a random tree of the punctured graph. The formula is exact, but no independent external mathematical audit has been performed. As with any targeted literature comparison, unrelated terminology for vertex-deleted Cartesian grids may conceal an equivalent published count; the asymptotic Poisson phenomenon in more general highly connected graph sequences is not claimed to originate here.

## References

1. A. E. Black and J. A. De Loera, *Monotone Paths on Cross-Polytopes*, arXiv:2102.01237, first publicly submitted 2021-02-02; *Discrete & Computational Geometry* 70 (2023), 1245–1265, DOI: 10.1007/s00454-023-00563-4. Theorem 1.1(c,f) supplies the graph identification.
2. C. A. Athanasiadis, J. A. De Loera, and Z. Zhang, *Enumerative problems for arborescences and monotone paths on polytope graphs*, arXiv:2002.00999, first publicly submitted 2020-02-03; *Journal of Graph Theory* 99 (2022), 58–81. Section 3 distinguishes oriented arborescences from the tree invariant here.
3. *Exact flip-distance enumerator of cross-polytope coherent monotone paths*, publicly available research note, 2026-10-04, repository `published-finding corpus/2026`, publication identifier ending `defb8aa48da1`. Provides the same graph model and exact metric, not a Kirchhoff-tree formula.
4. G. Kirchhoff, classical matrix-tree theorem, and standard tensor-sum Laplacian spectral decomposition (used in the proofs above).
