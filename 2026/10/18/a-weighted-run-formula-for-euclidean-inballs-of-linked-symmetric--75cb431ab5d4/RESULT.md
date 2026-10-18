# A weighted-run formula for Euclidean inballs of linked symmetric snake-path polytopes

## Finding
Let \(n\ge2\) and \(S\subseteq\{1,\ldots,n-1\}\). Write \(\varepsilon_i=1\) if \(i\in S\), and \(\varepsilon_i=0\) otherwise. Consider the full-dimensional feasible polytope \(P_{n,S}=P(\Delta[S,S\cup\{n\}])\) of the linked symmetric snake-path delta matroid, in its **original Euclidean coordinates** \(x\in\mathbb R^n\). Its defining inequalities are
\[
0\le x_i\le1,\qquad
|S\cap\{i,\ldots,n\}|\le\sum_{j=i}^n x_j\le |S\cap\{i,\ldots,n\}|+1
\quad(1\le i\le n).
\]

A **constant run** is a maximal nonempty interval \([u,v]\subseteq\{1,\ldots,n-1\}\) on which all \(\varepsilon_i\) agree. Define
\[
H_{n,S}=\max_{[u,v]\text{ a constant run}}
\left(v-u+1+\sqrt{n-u+1}+\sqrt{n-v}\right).
\]
Then the exact ambient Euclidean inradius is
\[
\boxed{r_{\rm in}(P_{n,S})=\frac1{H_{n,S}}.}
\]
The formula is computable in linear time from the run decomposition of the word.

Every center of a maximum-radius Euclidean ball admits the following complete description. Put
\[
t_i=\sum_{j=i}^n x_j-|S\cap\{i,\ldots,n\}|,\qquad a_i=\sqrt{n-i+1}.
\]
With \(r=H_{n,S}^{-1}\), the full incenter set consists **exactly** of all vectors \(x\) for which
\[
r a_i\le t_i\le1-r a_i\quad(1\le i\le n),
\]
and
\[
\begin{cases}
t_i-t_{i+1}\ge r,&\varepsilon_i=0,\\
t_{i+1}-t_i\ge r,&\varepsilon_i=1
\end{cases}
\quad(1\le i<n).
\]
In particular, every maximizing directed run forces equality in both endpoint suffix inequalities and in every coordinate inequality along that run, for **every** incenter.

The run formula gives sharp uniform bounds
\[
\boxed{\frac1{n+\sqrt n}\le r_{\rm in}(P_{n,S})
\le\frac1{1+\sqrt n+\sqrt{n-1}}.}
\]
The lower bound is attained precisely when all \(\varepsilon_i\) are equal; alternating words attain the upper bound. Thus the attainable inradii range from order \(n^{-1}\) to order \(n^{-1/2}\) in the same dimension.

There is also an infinite lattice-versus-metric separation. For every \(n\ge4\), the two linked snake polytopes associated with \(S=\{1\}\) and \(S'=\{n-1\}\) are affinely unimodularly equivalent, and hence Ehrhart equivalent, but have distinct Euclidean inradii:
\[
\boxed{
r_{\rm in}(P_{n,\{1\}})=\frac1{n-1+\sqrt{n-1}}
>\frac1{n-2+\sqrt n+\sqrt2}
=r_{\rm in}(P_{n,\{n-1\}}).}
\]

## Assumptions and scope
The Euclidean norm is the standard one in the original binary incidence coordinates \(x\), not the pulled-back metric in the auxiliary \(t\)-variables. This distinction matters: the change of coordinates is unimodular but not orthogonal. The specified intervals are exactly the linked toric intervals of Chen, Sanchez, Veliz, and Ying (Proposition 5.3 and Corollary 5.4 of their first public preprint). Their feasible polytopes are full-dimensional.

The single-coordinate case \(n=1\) is the segment \([0,1]\), with inradius \(1/2\); the run formula is stated for \(n\ge2\).

## Proof
**1. The exact halfspace system in difference coordinates.** Write \(s_i=\varepsilon_i\) for \(i<n\), and \(s_n=0\). Set \(t_{n+1}=0\). The source's suffix inequalities become \(0\le t_i\le1\). Their inverse is
\[
x_i=s_i+t_i-t_{i+1}\quad(i<n),\qquad x_n=t_n.
\]
If \(s_i=0\), the constraint \(0\le x_i\le1\) is equivalent, in the unit cube of the \(t\)-variables, to \(t_i\ge t_{i+1}\). If \(s_i=1\), it is equivalent to \(t_{i+1}\ge t_i\). Thus the source polytope is exactly the intersection of the \(2n\) suffix halfspaces with these \(n-1\) oriented coordinate halfspaces. There are no omitted geometric restrictions.

**2. Convert inball containment to potential inequalities.** The functional \(t_i\) has \(x\)-normal \(e_i+\cdots+e_n\), of Euclidean norm \(a_i=\sqrt{n-i+1}\). The relevant coordinate inequality has normal \(\pm e_i\), of norm one. Consequently a Euclidean ball \(B(x,r)\) lies in \(P_{n,S}\) if and only if its center satisfies
\[
r a_i\le t_i\le1-r a_i
\]
for every \(i\), plus the oriented edge gaps stated in the finding. The condition is an exact ball-containment equivalence, even if some displayed source inequalities are redundant.

**3. Necessary longest-path barriers.** Orient the path on vertices \(1,\ldots,n\) so that \(i\to i+1\) when \(s_i=0\), and \(i+1\to i\) when \(s_i=1\). Every directed edge \(a\to b\) imposes \(t_a\ge t_b+r\). A directed path of \(d\) edges between indices \(i\) and \(j\) therefore gives
\[
1\ge r(a_i+a_j+d).
\]
A zero-edge path gives \(1\ge2r a_i\). Since the underlying graph is a path, a nonzero directed path traverses a constant-sign run. Its barrier strictly increases upon extension inside that run: for adjacent suffix weights,
\[
1+\sqrt{k-1}-\sqrt k>0\qquad(k\ge2).
\]
Thus it suffices to consider maximal constant runs. Also the first-edge barrier \(1+\sqrt n+\sqrt{n-1}\) exceeds every zero-edge barrier \(2a_i\). It follows that \(r\le H_{n,S}^{-1}\).

**4. Attaining the bound for every word.** Define a directed-path potential
\[
L_i=\max\left\{a_j+d:\ i\leadsto j\text{ is a directed path of length }d\ge0\right\}.
\]
There are finitely many paths, and the orientation is acyclic. For every directed edge \(i\to j\), \(L_i\ge1+L_j\). Put \(r=H_{n,S}^{-1}\) and \(t_i=rL_i\). The zero-edge paths give \(t_i\ge r a_i\). Every path is bounded by \(H_{n,S}\), so \(a_i+L_i\le H_{n,S}\) and \(t_i\le1-r a_i\). The directed edge gaps hold automatically. Reconstructing \(x\) from \(t\) therefore yields an actual center of a contained ball of radius \(r\). This proves the exact radius and the stated all-center halfspace description.

If a directed path attains \(H_{n,S}\), its endpoint and edge inequalities sum to \(1\ge rH_{n,S}=1\). Each individual slack is nonnegative, so all of those inequalities are equalities at every optimal center.

**5. Extremal words.** Every word has the first-edge run subpath, hence \(H_{n,S}\ge1+\sqrt n+\sqrt{n-1}\). An alternating word has only one-edge runs, and the first edge is the largest, giving equality. For any path \(i<j\), writing \(k=n-j+1\) yields
\[
(j-i)+a_j\le(j-i)+(n-j+1)=n-i+1,
\]
and hence \(a_i+a_j+(j-i)\le n+\sqrt n\). Equality requires the full path from \(1\) to \(n\), so \(H_{n,S}=n+\sqrt n\) precisely for constant-sign words.

**6. Ehrhart-equivalent but metrically different members.** The affine change \(x=s+Dt\), where \(D\) is the upper-bidiagonal integer matrix with ones on its diagonal and minus ones immediately above, is unimodular. The transformation \(t'_i=1-t_{n+1-i}\) is also integer affine unimodular and maps the orientation word \((s_1,\ldots,s_{n-1})\) to its reversal. Conjugating by \(D\) therefore provides an integer affine unimodular equivalence between \(P_{n,\{1\}}\) and \(P_{n,\{n-1\}}\). Their maximal constant runs give the two displayed radius formulas; the second denominator exceeds the first by
\[
\sqrt2-1+\sqrt n-\sqrt{n-1}>0.
\]
The distinct radii rule out Euclidean isometry, while unimodular equivalence proves the same Ehrhart polynomial.

## Verification
A separate executable checker, `verify.py`, independently constructs all source halfspaces and solves the Euclidean Chebyshev linear program for every binary orientation word in dimensions \(1\) through \(10\). It compares the numerical optimum with the run formula and verifies containment of the explicit directed-path center. The complete sweep comprises 1,023 words and 36,868 shifted inequalities, all passing. The checker also tests 72 binary vertices of the unimodularly paired families in dimensions \(4\) through \(9\). This is a finite consistency check; the proof above establishes the infinite statement.

Run `python verify.py` with NumPy and SciPy installed. No external files or fetched results are required by the checker.

## Relationship to prior work
Chen, Sanchez, Veliz, and Ying introduce lattice-path delta matroid polytopes. Their Theorem A supplies the complete suffix and coordinate inequalities, while their Proposition 5.3 identifies the linked toric/symmetric-snake subfamily and their Theorem B computes its triangulations and volumes via prescribed ascent sets. The inspected primary text does not derive Euclidean inradii, Chebyshev centers, or the weighted-run law in the original coordinates.

Results for ordinary or generalized snake **order** polytopes concern a different standard-Euclidean realization; unimodular changes of coordinates do not transfer metric inradii. Likewise, known longest-path formulas for signed or marked order polytopes use their own facet normals and metric weights, rather than the suffix normals of length \(\sqrt{n-i+1}\) that drive this theorem. The present result determines those weights and proves the full-run collapse for all linked symmetric snake intervals, not just an unconstrained generic potential-feasibility rule.

## Limitations
The theorem concerns only the linked toric/symmetric-snake intervals \(\Delta[S,S\cup\{n\}]\); it does not establish a corresponding closed run formula for general lattice-path delta matroids. The incenter polytope is described by exact inequalities but its affine dimension and vertex count are not separately classified. Euclidean inradius is realization-dependent. A previously unpublished or differently indexed formulation of the weighted-run law cannot be excluded by literature searches. Independent mathematical audit has not been performed.

## References
1. Douglas M. Chen, Mario Sanchez, John Veliz, and Zhiyan Ying, *Lattice Path Delta Matroids*, arXiv:2311.15441v1, first public 2023-11-26, especially Theorem A, Proposition 5.3, Corollary 5.4, and Theorem B. https://arxiv.org/html/2311.15441v1
2. Matias von Bell et al., *Triangulations, Order Polytopes, and Generalized Snake Posets*, arXiv:2102.11306, first public 2021-02-22 (a distinct family of standard order polytopes).
3. Matthias Beck and Max Hlavacek, *Signed Poset Polytopes*, arXiv:2311.04409, first public 2023-11-08 (different facet normals and signed-poset realization).
4. Christoph Pegel, *The Face Structure and Geometry of Marked Order Polyhedra*, arXiv:1610.01393, first public 2016-10-05 (marked order facets in a distinct realization).
