# Sharp overlap-matching bounds for one-point types of the generic tetrahedron-free 3-hypergraph

## Finding
Let \(M\) be the countable homogeneous tetrahedron-free 3-uniform hypergraph (the Fraïssé limit of finite 3-graphs containing no complete four-vertex 3-graph). Let \(A\subset M\) be any finite induced parameter hypergraph with \(n\) vertices and \(m\) hyperedges. Put \(N=\binom n2\). The *overlap graph* \(J(A)\) has as vertices the hyperedges of \(A\), with two adjacent when they share exactly two vertices; let \(\nu(A)\) be its matching number.

Each complete nonalgebraic one-point type over the individually named base \(A\) determines a link-edge set \(S\subseteq\binom A2\). Define the weighted type polynomial
\[
P_A(z)=\sum_{\text{nonalgebraic one-point types }q}z^{|S(q)|},
\]
and its Bernoulli normalization \(F_A(p)=(1-p)^N P_A(p/(1-p))\), where \(0<p<1\). Then
\[
\boxed{F_A(p)\ \ge\ (1-p^3)^{m-2\nu(A)}(1-2p^3+p^5)^{\nu(A)}.}
\]
For every \(0<p<1\), equality holds **if and only if** \(J(A)\) is a disjoint union of isolated edges and isolated vertices. In particular, writing \(t(A)=P_A(1)\),
\[
\boxed{t(A)\ \ge\ 2^N\left(\frac78\right)^m\left(\frac{50}{49}\right)^{\nu(A)}.}
\]
Both bounds are sharp: for every pair of integers \(m\ge0\) and \(0\le\nu\le\lfloor m/2\rfloor\), some finite tetrahedron-free parameter hypergraph has \(m\) hyperedges, overlap matching number \(\nu\), and equality at all \(p\in(0,1)\).

The independent-obstruction value \(F_A(p)=(1-p^3)^m\) holds exactly when \(A\) is a *linear* 3-hypergraph (no two old edges share two vertices). At the first nontrivial four-vertex base with two old triples sharing a pair, there are exactly \(50\) nonalgebraic types, rather than the independent-obstruction prediction \(49\).

## Assumptions and scope
Every hypergraph in the theorem is finite, simple, 3-uniform, and has no four vertices spanning all four triples. The structure \(M\) uses one symmetric irreflexive ternary relation; the base \(A\) is individually named. Only types of points outside \(A\) are counted. The two-fold intersection in \(J(A)\) is intersection of old triples, not adjacency in the link graph of a new point. The matching number is the ordinary maximum cardinality of pairwise vertex-disjoint edges in \(J(A)\).

Empty bases and edge-free bases are allowed (the usual empty products equal one). The weighted theorem holds for all real probabilities strictly between zero and one, and for all finite bases of the specified homogeneous structure.

## Proof
**1. Complete types as avoiding assignments.** The class of finite tetrahedron-free 3-graphs has free amalgamation: when two structures are amalgamated over a common induced substructure, add no triples using vertices from both new sides. This cannot create a tetrahedron. Its Fraïssé limit is homogeneous, and quantifier-free one-point diagrams over finite bases determine complete types. Every admissible diagram has infinitely many realizations, by repeated free amalgamation, and so determines a nonalgebraic type.

For a proposed new point \(x\), choose independently for each old pair \(\{a,b\}\) whether the new triple \(\{x,a,b\}\) is present; write its indicator as \(X_{ab}\). The four-set \(\{x,a,b,c\}\) becomes a forbidden tetrahedron precisely when the old triple \(\{a,b,c\}\) exists and \(X_{ab}=X_{ac}=X_{bc}=1\). Therefore admissible diagrams are exactly assignments satisfying all clauses
\[
D_{abc}=\neg(X_{ab}=X_{ac}=X_{bc}=1),\qquad abc\in E(A).
\]
Under independent Bernoulli-\(p\) pair indicators, the probability that all clauses hold equals \(F_A(p)\), by the defining weighted polynomial.

**2. Exact one-clause and paired-clause probabilities.** Each clause is decreasing, with probability \(1-p^3\). If two distinct old triples overlap in two vertices, their clauses share exactly one Bernoulli coordinate. Their simultaneous satisfaction probability is
\[
\Pr(D_e\cap D_f)=1-2p^3+p^5,
\]
by inclusion-exclusion, because the union of the two three-coordinate supports has five coordinates. If two old triples share at most one vertex, their clauses use disjoint coordinates and are independent.

**3. The matching enhancement.** Choose a matching of size \(\nu(A)\) in \(J(A)\), partition the \(m\) clauses into its \(\nu(A)\) paired blocks and \(m-2\nu(A)\) singleton blocks, and let \(G_j\) be the joint satisfaction event for a block. Every \(G_j\) is decreasing in the independent Boolean coordinates. The Harris correlation inequality, iterated over these events, gives
\[
\Pr(\bigcap_jG_j)\ge\prod_j\Pr(G_j)
=(1-p^3)^{m-2\nu(A)}(1-2p^3+p^5)^{\nu(A)}.
\]
The unweighted formula follows by putting \(p=1/2\) and multiplying by \(2^N\), since
\[
\frac{1-2(1/2)^3+(1/2)^5}{(1-(1/2)^3)^2}=\frac{50}{49}.
\]

**4. Equality, with no unproved independence assumption.** Suppose two different blocks depend on a common Boolean coordinate \(X\). Their satisfaction indicators \(U,V\) are decreasing, and each depends genuinely on \(X\): choose the other two coordinates of a clause containing \(X\) to be one and all remaining coordinates of its block to be zero. Changing \(X\) from zero to one changes satisfaction, with positive probability under \(0<p<1\). Thus the conditional expectation differences \(\mathbb E[U\mid X=0]-\mathbb E[U\mid X=1]\) and \(\mathbb E[V\mid X=0]-\mathbb E[V\mid X=1]\) are strictly positive. Conditional Harris correlation is nonnegative; the law of total covariance then gives
\[
\operatorname{Cov}(U,V)\ge p(1-p)\big(\mathbb E[U\mid X=0]-\mathbb E[U\mid X=1]\big)\big(\mathbb E[V\mid X=0]-\mathbb E[V\mid X=1]\big)>0.
\]
Applying Harris again to the intersection of these two block events and all remaining block events shows that the product estimate is strictly smaller than the true joint probability. Hence equality forces disjoint coordinate supports between all distinct blocks; equivalently, \(J(A)\) has no edges outside the chosen matching. The matching then consists of all nonisolated components of \(J(A)\), so \(J(A)\) is a matching plus isolates. Conversely, when \(J(A)\) has that form, all blocks use disjoint coordinates and equality holds.

Taking \(\nu=0\) yields equality in the independent-obstruction bound exactly when \(J(A)\) has no edges, which is the linear-hypergraph condition.

**5. Attainment and boundary witnesses.** For each matched edge take an old four-vertex block containing precisely two triples sharing a pair, and for each isolated overlap vertex take a separate old three-vertex block containing exactly one triple. Use disjoint vertex sets for the blocks, with no extra triples. Their union is tetrahedron-free, has the prescribed values \((m,\nu)\), and its overlap graph is a matching plus isolates; it attains equality for every \(p\).

For a four-point base with old triples \(abc,abd\), there are \(N=6\) pair choices and \(m=2\), \(\nu=1\). Its exact type count is \(2^6(1-2/8+1/32)=50\), whereas independent clauses would give \(2^6(7/8)^2=49\). No smaller base can contain two old triples.

To illustrate structural scale, for the *pair pencil* \(\{a,b,c_i\}\) of \(s\ge1\) old triples with all \(c_i\) distinct, conditioning on the single shared pair indicator gives the exact formula
\[
F_A(p)=(1-p)+p(1-p^2)^s,
\qquad
t(A)=2^{\binom{s+2}{2}-1}\left(1+\left(\frac34\right)^s\right).
\]
Thus as \(s\) increases the admissible proportion tends to one half, while the independent-clause benchmark \((7/8)^s\) tends to zero. This separates two natural incidence patterns with the same number of old hyperedges by an exponentially increasing relative factor.

## Verification
The standalone \`verify.py\` enumerates **all** finite tetrahedron-free labelled parameter 3-graphs of orders three through five (785 bases), enumerates all link assignments, and checks the weighted lower bound and its exact equality criterion at \(p=1/3,1/2,2/3\). It performs 35 additional reproducibly sampled admissible six-vertex base tests and checks the pencil normalization in eight instances. Its output is recorded in \`verification_output.txt\`: \`ALL_CHECKS_PASS\`. These computations corroborate but do not replace the unrestricted proof.

## Relationship to prior work
Conant treats generic forbidden-clique hypergraphs as free-amalgamation Fraïssé limits, furnishing the background for the one-point diagram interpretation. Harris's positive-correlation inequality for monotone events, and later refinements studied by Kalai, Keller and Mossel, are prior probabilistic tools **used** in the proof; a positive-correlation inequality in isolation is not claimed new. The contribution considered here is the sharp model-specific overlap-matching factor, complete equality characterization in terms of old-triple intersections, attainment for every matching parameter, and an exact first/large-scale boundary witness.

A published counting result for the generic \(K_4^-\)-free 3-hypergraph treats the different age in which a four-set may contain at most two old triples; that class is more restrictive than the tetrahedron-free age considered here. Neither statement implies the theorem for all the present parameter hypergraphs. Classical correlation theory makes implicit rediscovery possible, and the presented originality conclusion is conditional on the listed searches rather than an assertion of absolute priority.

## Limitations
The bound need not equal the exact type count when the overlap graph has connected components with three or more clause vertices. The polynomial \(P_A(z)\) can be recovered by direct finite enumeration but is not claimed to admit a simple universal closed formula. The theorem concerns only nonalgebraic one-point types; no higher-arity statement or unconditional new correlation theorem is asserted. Complete independence from every equivalent prior formulation has not been independently established.

## References
1. G. Conant, “An axiomatic approach to free amalgamation,” arXiv:1505.00762, first posted 4 May 2015; *Journal of Symbolic Logic* 82 (2017), 648–671. https://arxiv.org/abs/1505.00762 . Later versions contain corrections to results outside the elementary free-amalgamation premise used here.
2. T. E. Harris, “A lower bound for the critical probability in a certain percolation process,” *Proceedings of the Cambridge Philosophical Society* 56 (1960), 13–20, DOI:10.1017/S0305004100034241.
3. G. Kalai, N. Keller and E. Mossel, “On the Correlation of Increasing Families,” arXiv:1511.04600, first posted 14 November 2015. https://arxiv.org/abs/1511.04600 .
4. “Triangle-free envelopes for 1-types in the random \(K_4^-\)-free 3-hypergraph,” published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-triangle-free-envelopes-for-1-types-in-the-random-k4-minus-free--ae10e5d4346d .
