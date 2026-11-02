# Sixteen rigid root classes of minimum resolving bases in the five-cube

## Finding
Let \(Q_5\) have vertex set \(\{0,1\}^5\), with Hamming distance. A landmark set \(S\) **resolves** \(Q_5\) if the distance vectors \((d(x,s))_{s\in S}\), for \(x\in V(Q_5)\), are pairwise different. A **metric basis** is a resolving set of minimum cardinality. Write \(x\oplus e_j\) for toggling coordinate \(j\) of \(x\), and \(\bar x\) for its bitwise complement.

The metric dimension is \(4\), and there are exactly \(1280\) metric bases. They have the following complete and uniquely indexed description. Choose one of the \(16\) unordered complementary root pairs \(\{b,\bar b\}\). Form the five pairwise disjoint antipodal landmark pairs
\[
P_j(b)=\{b\oplus e_j,\overline{b\oplus e_j}\},\qquad j\in\{1,2,3,4,5\}.
\]
Choose a hole \(i\in\{1,2,3,4,5\}\). A metric basis is obtained by choosing exactly one vertex from each of the four \(P_j(b)\), \(j\ne i\), and none from \(P_i(b)\). Conversely **every** such choice is a metric basis and different root pairs give disjoint families. Consequently each root pair has \(5\cdot2^4=80\) bases.

Define the **one-exchange metric-basis graph** \(\mathcal B\) to have those \(1280\) bases as vertices, adjacent if and only if one landmark is deleted and one other vertex is inserted, leaving a metric basis. Then
\[
\mathcal B\;\cong\;\bigsqcup_{16}\mathcal A,
\]
where each component \(\mathcal A\) has \(80\) vertices, \(480\) edges, is \(12\)-regular, and has diameter \(4\). For any two bases \(S,T\) in the same component,
\[
d_{\mathcal A}(S,T)=4-|S\cap T|.
\]
From every base, the numbers of bases at distances \(0,1,2,3,4\) are, respectively, \(1,12,30,28,9\). The entire graph has \(7680\) edges. No one-for-one replacement can change the complementary root pair, although each of the sixteen components is internally connected.

## Assumptions and scope
All graphs are simple and unweighted; vertices of \(Q_5\) are labeled binary words. The reconfiguration operation is unrestricted **one-token jumping** (one arbitrary replacement), not an edge-constrained slide or simultaneous multi-token move. Each basis is an unordered set. The unit vector \(e_j\) indexes the \(j\)-th of the five coordinates. The root pair \(\{b,\bar b\}\), not one choice of representative \(b\), labels a component. Primary classification: MSC2020 \(05\mathrm C12\), distance in graphs and metric bases.

## Proof
**1. Resolving versus a ternary kernel.** For each binary landmark \(s\), define its sign vector \(r(s)=(1-2s_j)_{j=1}^5\in\{-1,1\}^5\). For binary test vertices \(x,y\), elementary coordinatewise subtraction gives
\[
d(x,s)-d(y,s)=\sum_{j=1}^5(x_j-y_j)(1-2s_j).
\]
Conversely every \(z\in\{-1,0,1\}^5\) is \(x-y\) for some binary \(x,y\). Thus \(S\) resolves if and only if the matrix \(M\) with rows \(r(s)\), \(s\in S\), has **no nonzero ternary vector** in its real kernel. This equivalence itself is known from earlier hypercube resolving-set research; we use it as a tool.

**2. Four landmarks are necessary.** A matrix of at most three sign rows has five sign columns, each representing one of at most \(2^{|S|-1}\le4\) patterns up to negation. Therefore two columns are equal or opposite. Their difference or sum gives a nonzero vector in \(\{-1,0,1\}^5\) annihilated by all rows. Hence no such set resolves.

**3. All resolving four-row matrices have one distinguished kernel.** Suppose \(M\) has four sign rows and resolves. If its real rank were below four, its five sign columns would belong to a subspace of \(\mathbb R^4\) of dimension at most three. A linear projection onto independent row coordinates injects this subspace into \(\mathbb R^3\), so it contains at most \(2^3\) sign columns and at most four classes modulo negation. Two of the five columns would again be equal or opposite, a contradiction. Thus \(\operatorname{rank}M=4\).

The five signed maximal minors of any \(4\times5\) sign matrix give a nonzero integral kernel vector. Every \(4\times4\) sign determinant is divisible by \(8\): subtract the first row from the other three rows and extract a factor \(2\) from each. The Hadamard determinant bound gives absolute value at most \(16\), so every such minor is \(0\), \(8\), or \(16\) in absolute value. If none had absolute value \(16\), dividing the cofactor vector by \(8\) would yield a nonzero ternary kernel vector. Therefore some four columns form a sign Hadamard matrix \(H\) with \(|\det H|=16\), and hence \(H^{\mathsf T}H=4I\).

Let \(y\) be the remaining sign column. It cannot equal \(\pm\) a column of \(H\), for then the matrix would have a ternary dependency. The four entries of \(H^{\mathsf T}y\) are even. They satisfy \(\|H^{\mathsf T}y\|^2=16\) by orthogonality and \(\|y\|^2=4\). An entry of absolute value \(4\) would force \(y\) to be a signed Hadamard column; therefore all four entries have absolute value \(2\). Solving \(Hc=y\) gives \(c=\tfrac14H^{\mathsf T}y\), with every \(c_j\in\{-\tfrac12,\tfrac12\}\). The one-dimensional real kernel thus has a primitive integral generator \(a\) with
\[
\{|a_1|,\ldots,|a_5|\}=\{2,1,1,1,1\}.
\]
Conversely, whenever a four-row sign matrix has rank four and its primitive kernel generator has that absolute-value pattern, it resolves: every nonzero integral vector in its one-dimensional kernel is an integer multiple of \(a\) up to normalization, so no nonzero ternary vector can be in that kernel. (One can also note directly that any rational multiple of this primitive \(a\) which is integral must have integral multiplier.)

**4. Recover the sixteen root classes and five holes.** Let \(i\) denote the unique coordinate with \(|a_i|=2\). Set \(b_j=\operatorname{sgn}(a_j)\) for \(j\ne i\), and \(b_i=-\operatorname{sgn}(a_i)\). The vector \(b\in\{-1,1\}^5\) is defined up to simultaneous negation because \(a\) is. Identify this sign root with the unique binary root word \(b^{\mathrm{bin}}\in\{0,1\}^5\) satisfying \(r(b^{\mathrm{bin}})=b\); its complementary pair is unchanged by replacing \(a\) with \(-a\). The equation \(a\cdot r=0\), for \(r\in\{-1,1\}^5\), becomes
\[
\sum_{j\ne i}b_jr_j=2b_ir_i.
\]
Exactly three of the four signs \(b_jr_j\), \(j\ne i\), equal \(b_ir_i\), while precisely one has the opposite sign. Therefore the permitted row vectors are exactly the eight vectors obtained by toggling **one** coordinate \(j\ne i\) of \(b\) or its antipode. Under the sign-to-binary identification just specified, they form precisely four antipodal pairs \(P_j(b^{\mathrm{bin}})\), \(j\ne i\).

A resolving four-row matrix cannot contain both members of an antipodal pair, since such rows are linearly dependent; it therefore selects one row from each of those four pairs. Conversely, for any such transversal, sign-conjugation and row flips identify its four-by-four incidence matrix with the matrix having diagonal \(-1\) and off-diagonal \(+1\), namely \(J_4-2I_4\), up to sign and coordinate permutation. Its determinant has absolute value \(16\), and its one-dimensional kernel is exactly the specified \(a\), with pattern \((2,1,1,1,1)\) in absolute value. Thus it resolves. The root pair and hole are recovered uniquely from the primitive null vector. There are \(16\) roots modulo antipodes, \(5\) holes for each root, and \(2^4\) transversals for each hole: exactly \(1280\) bases.

**5. Classify every exchange.** For a fixed root \(\{b,\bar b\}\), all bases use four of the five disjoint pairs \(P_j(b)\). Two bases from the same root share exactly three landmarks precisely when either (a) they have the same hole and the selected representative in one occupied pair is flipped to its antipode, or (b) their holes differ, one representative is removed from the now-vacant pair and either member of the formerly empty pair is inserted. Hence each basis has \(4+4\cdot2=12\) neighbors.

For distinct complementary root pairs, choose representatives at Hamming distance one or two (the minimum complementary distance is always one or two). At distance one, the two ten-vertex unions \(\bigcup_jP_j(b)\) are disjoint. At distance two, the unions meet in precisely two antipodal pairs, and each basis can occupy at most one vertex from each. Thus bases belonging to different root pairs share at most two landmarks. They cannot be exchange-adjacent, which requires an intersection of size three. The sixteen root families are therefore exactly distinct connected components once internal connectivity is established.

**6. Distances and counts.** For two bases \(S,T\) in the same root family, every exchange can fix at most one landmark missing from the target, so \(d(S,T)\ge4-|S\cap T|\). If the two holes are different, first insert the desired target representative of the currently missing pair while removing the representative in the pair omitted by the target. All further disagreements are antipodal choices within occupied pairs, and each is fixed with one flip. If the holes coincide, only flips are necessary. This constructs a route of length \(4-|S\cap T|\) in every case, proving equality, connectivity, and diameter four.

For any fixed basis, there are \(\binom4j\) target bases with the same hole at distance \(j\), and \(8\binom3{j-1}\) targets with a different hole at distance \(j\). This gives the distance-shell distribution \((1,12,30,28,9)\). A component has \(80\cdot12/2=480\) edges, so the sixteen components have \(7680\) total edges. This completes the proof.

## Verification
Two standalone standard-library checkers accompany the result. `artifacts/direct_check.py` enumerates every one of the \(\binom{32}{4}=35960\) candidate four-vertex sets, directly compares all 32 binary distance signatures, checks that no smaller set resolves, constructs every one-replacement edge, and runs breadth-first search from all \(1280\) bases. It checks the sixteen components and every claimed distance shell.

`artifacts/algebraic_check.py` independently generates the root/hole/transversal families, verifies their primitive integer null vectors and lack of nonzero ternary kernel vectors, checks all interchange pairs, and enumerates all \(2^{16}=65536\) order-four sign matrices to validate the determinant value restriction. Both programs complete with explicit PASS markers. These exact finite computations corroborate the independently written argument above; they are not being substituted for the classification proof.

## Relationship to prior work
Classical metric-dimension results and hypercube linear-algebra criteria already exist: Bailey and Cameron (2011) discuss metric dimension and bases, Beardon (2013) reduces hypercube resolvability to linear equations, and Laird, Tillquist, Becker and Lladser (2019 preprint) give the no-nonzero-ternary-kernel test used in step 1. Kelenc and coauthors (2021 preprint) already prove that replacing a landmark by its antipode preserves a hypercube resolving set. None of those underlying lemmas is presented as new. The known value \(\dim(Q_5)=4\) is not the claimed contribution.

A previously published treatment of the signed Johnson one-skeleton of a cube–cross-polytope intersection gives the graph whose vertices are signed four-support vectors in five coordinates with **support-replacement** adjacency. This is a proper spanning subgraph of the component here: the prior graph has degree \(8\) and does **not** include the four same-support antipodal sign flips, whereas the present metric-basis component has degree \(12\). Its diameter formula therefore does not imply the present metric-basis exchange theorem. The contribution here is the complete list of \(1280\) optimizers, their separation into sixteen root classes under **all** one-replacement exchanges, and their exact distances and degree structure.

## Limitations
The theorem is specific to the ordinary metric dimension of the five-dimensional binary hypercube and to one arbitrary landmark replacement. It does not determine analogous graphs for other dimensions, edge metric dimension, mixed metric dimension, or simultaneous multiple replacements. Earlier sources concerning Beardon (2013) and a recent thesis on metric-basis reconfiguration were not available in complete text for the final comparison, so an equivalent historical presentation under different terminology cannot be fully excluded. No independent scholarly audit is asserted.

## References
1. R. F. Bailey and P. J. Cameron, *Base size, metric dimension and other invariants of groups and graphs*, Bulletin of the London Mathematical Society (2011), DOI: 10.1112/blms/bdq096; first available online 2011-01-21.
2. A. F. Beardon, *Resolving the hypercube*, Discrete Applied Mathematics 161 (2013), 1882–1887, DOI: 10.1016/j.dam.2013.02.012.
3. L. Laird, R. C. Tillquist, S. Becker and M. E. Lladser, *Resolvability of Hamming Graphs*, arXiv:1907.05974, first public 2019-07-12; SIAM Journal on Discrete Mathematics 34 (2020), 2063–2081.
4. A. Kelenc and collaborators, *On Metric Dimensions of Hypercubes*, arXiv:2102.10916, first public 2021-02-22.
5. *Exact shortest-path metric of the cube–cross-polytope intersection balls*, mathematical research record first public 2026-10-04; signed Johnson support-swap one-skeleton result (distinct from the one-replacement graph studied here).
