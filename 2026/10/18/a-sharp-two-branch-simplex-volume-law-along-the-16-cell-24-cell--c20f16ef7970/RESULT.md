# A sharp two-branch simplex-volume law along the 16-cell–24-cell truncation path

## Finding
Let \(0\le t\le\tfrac12\) and set
\[
K_t=\left\{x\in\mathbb R^4:\sum_{i=1}^4|x_i|\le1,\quad |x_i|\le1-t\ (1\le i\le4)\right\}.
\]
Thus \(K_0\) is the regular 16-cell, \(K_{1/2}\) is a scaled regular 24-cell, and \(K_{1/3}\) is the uniform truncated 16-cell. Write \(M(t)\) for the maximum ordinary four-dimensional volume of any 4-simplex contained in \(K_t\), allowing arbitrary points of the body as its vertices. Put \(r=\sqrt2-1\). The exact maximum is
\[
\boxed{M(t)=\frac1{24}\begin{cases}
2-6t+10t^2-6t^3,&0\le t\le r,\\
4t-4t^2-4t^3+4t^4,&r\le t\le\tfrac12.
\end{cases}}
\]
It decreases strictly on the whole interval and has one interior nondifferentiability at \(r\), with right-minus-left derivative jump \((40\sqrt2-56)/24>0\).

For \(0<t<r\), there are exactly 192 maximizing vertex-supported 4-simplices, and **every** maximizing contained simplex is one of them. For \(r<t<\tfrac12\), exactly 96 vertex-supported simplices maximize, but the complete equality locus consists instead of 48 distinct one-parameter families: in each, four vertices are fixed vertices of \(K_t\) and the fifth ranges along a segment between two other vertices of \(K_t\). At \(t=r\), exactly 288 vertex-supported simplices maximize; no exhaustive description of nonvertex maximizers at this single transition is claimed. At the uniform truncation parameter \(t=\tfrac13\), the maximum is \(1/27\), which is \(9/154\) of the body volume.

## Assumptions and scope
All simplices are four-dimensional, and all volumes are ordinary Euclidean four-volumes in the coordinates displayed. No optimization restriction to the containing body's vertices is imposed. The phrase *vertex-supported* specifically means that all five simplex vertices belong to the finite vertex set of \(K_t\); these are counted as unoriented, unordered geometric 4-simplices. The 192, 96, and 288 counts apply only at the stated interior parameters and have no implicit assertion about endpoint multiplicities. The shape \(K_t\) is the cross-polytope cut by eight symmetric coordinate hyperplanes, not the unrelated truncated 24-cell.

## Proof
**1. The polytope and vertex reduction.** For \(0<t<\tfrac12\), the 48 distinct vertices of \(K_t\) are exactly
\[
v(i,s;j,u)=(1-t)s e_i+tu e_j,
\quad i,j\in\{1,2,3,4\},\ i\ne j,\ s,u\in\{-1,1\}.
\]
Indeed, the eight original tips \(\pm e_i\) of the cross-polytope are each removed by one coordinate hyperplane. The eight chopped caps have disjoint interiors because \(2(1-t)>1\), and every new vertex is the intersection of an original edge \([s e_i,u e_j]\) with the cap plane \(x_i=s(1-t)\). At the two endpoints the same 48 formulas exhaust the vertices but include repetitions.

The signed determinant \(\det(p_1-p_0,\ldots,p_4-p_0)\) is affine separately in each of the five arguments. Expanding arbitrary \(p_i\in K_t\) into convex combinations of its vertices shows that its absolute value cannot exceed the maximum absolute determinant of a five-vertex choice. Hence an unrestricted maximal simplex is always attained at vertices, and an exact bound on all vertex determinants is a bound on *all* contained simplices.

**2. Two candidate determinants.** Number the 48 formal vertices lexicographically with indices starting at zero, ordering first \(i=1,\ldots,4\), then \(s=-1,+1\), then \(j\ne i\) increasingly, and then \(u=-1,+1\). The anchor is vertex index 0, namely \(v(1,-1;2,-1)\). The unordered index sets \(\{0,6,20,34,47\}\) and \(\{0,6,20,41,47\}\) have respective determinant magnitudes
\[
A(t)=2-6t+10t^2-6t^3,\qquad
B(t)=4t-4t^2-4t^3+4t^4.
\]
Their difference factors exactly as
\[
A(t)-B(t)=-2(t-1)(2t-1)(t^2+2t-1).
\]
Since the two first factors are positive in product for \(0\le t<1/2\), \(A>B\) precisely for \(0\le t<\sqrt2-1\), and \(B>A\) precisely for \(\sqrt2-1<t<1/2\). Both are nonnegative on the full domain, and the active branch is strictly positive. Derivative factorization proves strict decrease for both branches on their active intervals; substituting \(r\) in the derivatives gives the jump in the Finding.

**3. Exhaustive exact polynomial certificate.** The hyperoctahedral signed-permutation group acts transitively on the 48 vertices whenever \(0<t<1/2\). Every five-vertex simplex is therefore congruent to one containing index 0. Consequently only \(\binom{47}{4}=178365\) anchored sets need be enumerated. The supplied `enumerate.cpp` generates all those sets by nested increasing loops and expands each 4-by-4 determinant using the 24 terms of its Leibniz permutation formula, producing an integer polynomial of degree at most four in \(t\). Identifying a polynomial with its negative leaves precisely 258 distinct coefficient profiles, with exact multiplicities summing to 178365.

For *every* such signed polynomial \(P\), the supplied `verify.py` proves the two inequalities
\[
A(t)\pm P(t)\ge0\quad(0\le t\le r),\qquad
B(t)\pm P(t)\ge0\quad(r\le t\le\tfrac12)
\]
with **exact** arithmetic in \(\mathbb Q(\sqrt2)\). For each difference polynomial and interval, substitution \(t=a+(b-a)u\) produces the degree-four Bernstein expansion \(\sum_{j=0}^4\beta_j\binom4j u^j(1-u)^{4-j}\). All 5,160 resulting exact coefficients are nonnegative. This rigorously establishes the inequalities for every real parameter, not just a finite sample. The full checker regenerates the polynomials; it does not trust a downloaded coefficient table or floating-point grid. It separately tests representatives with an independent rational Leibniz determinant implementation.

Each Bernstein basis function is strictly positive for \(0<u<1\). Thus equality in the interior of either interval requires the deficit polynomial to vanish identically. The only winning anchored profiles are the negative of \(A\), appearing 20 times, and the negative of \(B\), appearing 10 times; the canonical sign normalization accounts for these minus signs. At \(t=r\), exact evaluation in \(\mathbb Q(\sqrt2)\) shows no third profile ties. Transitivity and double-counting the five choices of an anchor give \(48\cdot20/5=192\), \(48\cdot10/5=96\), and \(48\cdot30/5=288\) distinct vertex-supported maximizers, respectively.

**4. All nonvertex equality cases in the open phases.** Applying all 384 signed-coordinate permutations to the two witness quintuple sets generates exactly the 192 and 96 maximizers just counted, with disjoint orbits. Direct finite incidence checks in `verify.py` show: no two of the 192 first-phase sets share four vertices; among the 96 second-phase sets, exactly 48 distinct four-vertex sets each belong to exactly two maximizers, while every other four-set belongs to only one. The 96 second-phase maximizers therefore form 48 disjoint pairs under adjacency by a common four-vertex face. The independent rational determinant check also shows that the two possible fifth vertices in every pair yield the **same signed** maximal determinant when a consistent ordering of the common four vertices is held fixed.

For completeness, expand an arbitrary maximizing contained simplex's five vertices into convex combinations of vertices of \(K_t\). Equality in the triangle inequality for the resulting determinant average forces every vertex selection with positive product weight to be a maximizing five-vertex set of the same signed orientation. If two or more original simplex vertices were nonvertices, choosing two distinct positive-weight atoms in each would create four different maximal vertex sets forming a four-cycle under common-four-vertex adjacency. This cannot occur in the first phase (the adjacency graph is empty) or the second phase (it is a matching). Consequently, first-phase maximizers are all vertex-supported. In the second phase at most one vertex may move, and its support lies in one of the 48 adjacent endpoint pairs; conversely the affine determinant identity proves that each such full closed segment consists of maximizers. This yields the asserted complete description. At the isolated transition we assert only the exact vertex-supported count, leaving possible higher-dimensional movable families unclassified.

**5. Container-volume normalization.** The full cross-polytope has volume \(2^4/4!=2/3\). Each of its eight severed tips has volume \(t^4/3\), by slicing the \(\ell_1\)-ball at coordinate distance \(1-t\); the tips overlap only on zero-volume boundaries. Hence
\[
\operatorname{vol}_4(K_t)=\frac23\bigl(1-4t^4\bigr).
\]
Substituting \(t=1/3\) yields \(M(1/3)=1/27\) and normalized occupancy \(9/154\).

## Verification
Run `python3 verify.py` in the directory containing `verify.py` and `enumerate.cpp`, with Python 3 and a C++17 compiler (`g++`) available. The verifier compiles the finite enumerator in a temporary directory and executes it, checks 178365 anchored quadruples and their 258 profiles, checks 1032 exact Bernstein expansions with five coefficients each, checks all endpoint and phase identities, re-evaluates every distinct profile at \(t=1/3\) with an independent rational determinant implementation, and checks all signed-permutation orbits, four-vertex incidences, and 48 same-sign movable-apex pairs. The expected output begins `PASS: 178365 vertex-anchored determinants`.

The analytic vertex-reduction and equality-mixture arguments apply universally. The finite certificate is exhaustive only for the finite, explicitly parametrized vertex set, and its positivity certificate (not a numerical grid) extends the result to the whole continuum of truncation parameters. No independent formal verification has been performed.

## Relationship to prior work
Horváth and Lángi (2014) investigate maximizing spherical polytopes with a prescribed number of vertices, obtaining a regular-simplex extremality principle. Their setting allows the spherical vertices themselves to vary and does not supply the fixed-container maximum for this truncated cross-polytope family.

Di Summa, Eisenbrand, Faenza and Moldenhauer (2014) give approximation and hardness results for maximal-volume simplices and maximal subdeterminants in arbitrary vertex polytopes; their general problem and determinant reduction motivate the exact question, but their results do not imply the two explicit branch polynomials, the transition, or the equality families.

The published computation “Exact largest-simplex volume and equality classification in the regular 24-cell” proves the endpoint corresponding to \(t=1/2\): after the factor-two rescaling between root coordinates and this paper's coordinates it gives \(M(1/2)=1/32\). It does not cover intermediate truncation parameters or movable-apex families. The separate published “Sharp tetrahedral-volume profile in the cube–octahedron intersection family” treats a *three-dimensional* analogue with different determinant degree and phase structure; its explicit scope excludes four dimensions. The published general cube–cross-polytope intersection Mahler-volume formula concerns the different invariant \(\operatorname{vol}(K)\operatorname{vol}(K^\circ)\), not the maximal contained 4-simplex. These distinctions are by objects, parameter ranges and implications, not merely different titles.

## Limitations
The finding concerns this one natural four-dimensional truncation family and its affine images; it does not claim a universal theorem for higher dimensions, all cut polytopes, or arbitrary 4-polytopes. The second-phase equality locus is completely described, but the full continuous equality set at the one transition parameter is not. Historical-priority claims carry residual uncertainty for older unindexed regular-polytope tables and unpublished determinant classifications. The finite profile and incidence counts depend on replaying the supplied exact certificate; the witness determinants alone do not establish the global inequalities or equality counts. The 24-cell endpoint is acknowledged as previously known.

## References
1. Á. G. Horváth and Z. Lángi, “Maximum volume polytopes inscribed in the unit sphere,” arXiv:1402.6496, first public 2014-02-26, full text https://arxiv.org/html/1402.6496v3.
2. M. Di Summa, F. Eisenbrand, Y. Faenza, and C. Moldenhauer, “On largest volume simplices and sub-determinants,” arXiv:1406.3512, first public 2014-06-13, full text https://arxiv.org/html/1406.3512v1.
3. “Exact largest-simplex volume and equality classification in the regular 24-cell,” publicly accessible result, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-largest-simplex-volume-and-equality-classification-in-the--bda0674b8ea5/RESULT.md.
4. “Sharp tetrahedral-volume profile in the cube–octahedron intersection family,” publicly accessible result, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-tetrahedral-volume-profile-in-the-cube-octahedron-intersec--9ba1a511dacf/RESULT.md.
5. “Exact Mahler products for cube–cross-polytope intersections and their three-dimensional phase diagram,” publicly accessible result, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-mahler-products-for-cube-cross-polytope-intersections-and--afc1f44d4eb2/RESULT.md.
