# Integral tight Fourier sampling and tree-complement designs for regular tournaments

## Finding
For every odd integer \(n\ge 3\), let \(\mathcal R_n\) be the nonempty set of regular tournaments on vertices \(\{1,\ldots,n\}\), and put \(m=\binom n2\), \(d=(n-1)(n-2)/2\). Orient each edge \(e=\{i,j\}\), \(i<j\), by the reference direction \(i\to j\); write \(\chi_e(T)=+1\) when the tournament agrees with this direction and \(-1\) otherwise. These are the first-degree Walsh characters of the edge-orientation cube. Denote the signed vertex-edge incidence matrix of \(K_n\) by \(B\), so the column indexed by \(\{i,j\}\), \(i<j\), is \(e_i-e_j\).

**Theorem (one first-band sampling classification).** The integral span of all differences of binary orientation incidence vectors of regular tournaments equals the entire integer circulation lattice \(\ker_{\mathbb Z}B\). Thus, under every full-support probability law \(\mu\) on \(\mathcal R_n\), the covariance \(C_\mu\) of \((\chi_e)_{e\in E(K_n)}\) has rank \(d\) and kernel \(\operatorname{im}B^{\mathsf T}\). If \(S\subseteq E(K_n)\) is selected and \(F=(V,E(K_n)\setminus S)\) is the graph of omitted edges (isolated vertices retained), then
\[
\operatorname{nullity}((C_\mu)_{S,S})=c(F)-1.
\]
Consequently, the largest independent family of nonconstant edge characters has \(d\) members; its selections are exactly the complements of spanning trees of \(K_n\), numbering \(n^{n-2}\). All such selections have the same probability-normalized Gram determinant for the constant character and the selected nonconstant characters,
\[
\det G_\mu(S)=\frac{\operatorname{pdet}C_\mu}{n^{n-2}},
\]
while every other \(d\)-character selection has determinant zero. This holds for **every** full-support law, without any exchangeability assumption.

Under the **uniform** law the complete covariance is
\[
C_{\rm unif}=\frac{n}{n-2}I_m-\frac{1}{n-2}B^{\mathsf T}B
=\frac{n}{n-2}P_{\ker B}.
\]
It has eigenvalues \(0\) (multiplicity \(n-1\)) and \(n/(n-2)\) (multiplicity \(d\)); the constant character contributes a separate Gram eigenvalue \(1\). Thus the maximal nonconstant band is exactly tight on the circulation space, and for every spanning-tree complement \(S\),
\[
\det G_{\rm unif}(S)=\frac{1}{n^{n-2}}\left(\frac{n}{n-2}\right)^d.
\]
Under uniform sampling, edge characters indexed by any matching are **jointly independent fair signs**, not merely pairwise uncorrelated. After radial normalization, the entire set of regular-tournament orientation vectors forms a spherical \(3\)-design in its \(d\)-dimensional circulation space; for \(n\ge5\) it is not a spherical \(4\)-design. For \(n=3\), the two opposite sign vectors constitute the entire zero-dimensional sphere.

## Assumptions and scope
A regular tournament has indegree and outdegree both \((n-1)/2\) at every vertex, so \(n\) must be odd. The reference signs affect matrix entries but not the results. Covariance uses probability normalization (not division by one less than the sample count). “Full support” means every labelled regular tournament has strictly positive probability. For a selected set \(S\), the Gram matrix is indexed by \(1\) and \((\chi_e)_{e\in S}\); the Schur complement of its leading \(1\) is exactly the covariance principal submatrix. \(\operatorname{pdet}\) denotes the product of strictly positive eigenvalues. The graph \(F\) contains all \(n\) labelled vertices, including isolated ones.

## Proof
**1. Exact integer affine span.** Let \(a_e(T)=(1+\chi_e(T))/2\) be the binary incidence vector and let \(L=\ker_{\mathbb Z}B\). Since every regular tournament is balanced, \(B\chi(T)=0\), hence \(B(a(T)-a(T'))=0\). To prove the reverse lattice inclusion, let \(n=2k+1\) and orient the cyclic tournament on \(\mathbb Z/n\mathbb Z\) by \(u\to v\) iff \(v-u\in\{1,\ldots,k\}\) modulo \(n\). Its arcs \(0\to1\), \(1\to k+1\), \(k+1\to0\) form a directed triangle. Reversing exactly these three arcs preserves all outdegrees and gives another regular tournament. Relabelling realizes the same flip on **every** prescribed directed triangle; its binary-incidence difference is precisely the signed integral triangle circulation. For a fixed vertex \(r\), the triangle circulations \(r\to i\to j\to r\), for all edges \(\{i,j\}\) with \(i,j\ne r\), form a \(\mathbb Z\)-basis of \(L\): delete each chord coordinate from an arbitrary integral circulation by its corresponding triangle, leaving a circulation supported on a star, necessarily zero. Therefore the integer difference span is \(L\), and the real affine span is \(\ker B\) (dimension \(d\)).

**2. Kernel, all selected nullities, and exact saturated determinants.** For any full-support law, the variance of a real linear functional of \(\chi\) vanishes iff it is constant on all sampled vectors. By step 1, this holds exactly for vectors orthogonal to \(\ker B\), namely \(\operatorname{im}B^{\mathsf T}\). Thus \(C_\mu\) is positive definite on \(\ker B\). A vector in this kernel supported on a retained set \(S\) has the form \(B^{\mathsf T}y\), where \(y_i=y_j\) along every omitted edge in \(F\). Such vectors have dimension \(c(F)-1\); this proves the asserted nullity formula.

To prove the determinant identity, fix a spanning tree \(T_0\) and let \(Z\) be the \(m\)-by-\(d\) **integer fundamental-cycle matrix** whose column for every off-tree edge is that edge plus the uniquely determined signed tree path. Its columns form an integral basis of \(L\), and any positive covariance with range \(\ker B\) factors as \(C_\mu=ZKZ^{\mathsf T}\) with \(K\) positive definite. For any set \(S\) of \(d\) edges, \(\det(C_\mu)_{S,S}=\det(K)\det(Z_S)^2\). The incidence-network unimodularity argument gives \(\det Z_S\in\{0,\pm1\}\), nonzero precisely when its omitted edges form a spanning tree: this follows by solving the divergence equations on the omitted edges, which is uniquely possible with integer data iff they form a tree. The Cauchy–Binet formula and Cayley's tree formula yield
\[
\det(Z^{\mathsf T}Z)=\sum_{|S|=d}\det(Z_S)^2=n^{n-2}.
\]
Since \(\operatorname{pdet}(ZKZ^{\mathsf T})=\det K\det(Z^{\mathsf T}Z)\), the common Gram determinant is \(\operatorname{pdet}C_\mu/n^{n-2}\). The constant-character Schur complement supplies exactly that same determinant, independently of nonzero coordinate means.

**3. Complete uniform spectrum.** Tournament reversal gives \(\mathbb E\chi_e=0\) and \(\mathbb E\chi_e^2=1\). For disjoint edges, transposing the endpoints of one edge changes its sign but preserves the other and the uniform law, so their covariance vanishes. If two edge orientations agree at a shared vertex, symmetry makes their covariance a common value \(r\); opposite reference incidences change its sign. Multiply the degree-balance identity \(\sum_{j\ne i}\chi_{i\to j}=0\) by one selected outgoing sign and take expectations: \(1+(n-2)r=0\). Therefore \(r=-1/(n-2)\), giving \(C=\frac n{n-2}I-\frac1{n-2}B^{\mathsf T}B\). For the complete graph, \(BB^{\mathsf T}=nI-J\), so \(B^{\mathsf T}B/n\) is the orthogonal projection onto the cut space. The stated eigenvalues, multiplicities and uniform determinant follow.

**4. Joint matching independence and exact design strength.** For a matching of \(h\) distinct edges, the \(h\) commuting permutations swapping each pair of endpoints independently preserve all regular tournaments and flip precisely one chosen coordinate at a time. Thus the \(2^h\) sign patterns occur with equal frequency. For spherical design, each signed vector lies in \(\ker B\) on the sphere of radius \(\sqrt m\), and step 3 gives mean zero and covariance \((m/d)P_{\ker B}\). Reversal of all arcs makes the third centered tensor zero, matching the first three moments of the rotationally invariant sphere law. For \(n\ge5\), \(d>1\); a selected edge coordinate has second and fourth moments both \(1\), whereas its fourth moment on the uniform sphere of radius \(\sqrt m\) in this \(d\)-dimensional subspace is \(3d/(d+2)>1\), as follows from the standard spherical fourth-moment formula and its variance \(1\). Hence the design strength is exactly three.

## Verification
The standalone `check_regular_tournaments.py` uses exact rational arithmetic, exhaustively lists labelled regular tournaments at orders \(3\) and \(5\), and checks the full covariance matrix, affine rank, and realizability of each prescribed oriented triangle. At order \(5\) it enumerates all \(125\) spanning-tree complements and all non-tree candidates of the same size, checking uniform and explicitly nonuniform positive-weight Gram determinants. Running the embedded checker prints `all exact finite checks PASS`. The universal statements follow from the proof, not the finite run.

## Relationship to prior work
Kühn–Osthus–Treglown (first publicly posted 24 August 2009) studies Hamilton-cycle decompositions of regular tournaments, not the associated first-degree Walsh covariance or coordinate Gram determinants. Classical score-sequence, graphical-zonotope, and spanning-tree theories supply background ingredients. Kolesnik–Sanchez's full-text 2023 treatment of random-tournament geometry proves zonotopal forest representations (Theorem 4.1) but does not identify the full-support covariance kernel, weighted D-optimal coordinate minors, uniform tight spectrum, or exact spherical design strength for the regular-score fibre. The general graphic-tree minor mechanism also appears in earlier sampling models; the subject-specific positive-support spanning theorem and uniform regular-tournament isotropy are verified here, rather than assumed.

## Limitations
The theorem concerns labelled **regular** tournaments on complete graphs, and first-degree edge characters only. It does not assert higher-band spectral bounds, any result about nonregular score fibres, or independence of selected edge signs outside matchings. Full-support laws yield determinant equality but not generally a tight covariance.

## References
- D. Kühn, D. Osthus, A. Treglown, *Hamilton decompositions of regular tournaments*, arXiv:0908.3411 (first posted 2009-08-24), full text https://arxiv.org/abs/0908.3411.
- B. Kolesnik, M. Sanchez, *The Geometry of Random Tournaments*, Discrete & Computational Geometry (published online 2023-09-21), full text https://link.springer.com/article/10.1007/s00454-023-00571-4, especially Theorems 1.1, 1.2, 4.1 and Lemma 4.4.
- J. W. Moon, *An extension of Landau's theorem on tournaments*, Pacific J. Math. 13 (1963), 1343–1345 (classical score-sequence background).
- A. Cayley, classical labelled-tree enumeration; the matrix-tree/Cauchy–Binet and integral fundamental-cycle basis arguments are used as established graph linear algebra.
