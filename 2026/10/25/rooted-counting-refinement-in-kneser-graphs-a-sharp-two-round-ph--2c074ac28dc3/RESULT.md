# Rooted counting refinement in Kneser graphs: a sharp two-round phase and the odd-graph depth

## Finding
Let \(k\ge1\), \(n\ge 2k+1\), and let \(\mathrm{KG}(n,k)\) be the simple graph on the \(k\)-subsets of \([n]\), adjacent exactly when disjoint. Uniquely colour one vertex \(R\) and initially colour all other vertices alike. Apply synchronous ordinary one-dimensional counting colour refinement, retaining the old colour and the multiset of neighbour colours in every round. Write \(\mathcal T_t=\{X:|X\cap R|=t\}\) for \(0\le t\le k\).

**Theorem.** For every \(n\ge2k+1\), the final colour classes are exactly \(\mathcal T_0,\ldots,\mathcal T_k\), and they are reached within \(k\) rounds. Each has size
\[
|\mathcal T_t|=\binom{k}{t}\binom{n-k}{k-t}.
\]
For \(k=1\) the initial partition is already final; for \(k=2\) exactly one round is needed. For \(k\ge3\), **exactly two rounds** suffice if and only if \(n\ge3k-2\). On the sparse boundary \(n=2k+1\) (the odd graph), the exact number of rounds is \(k-1\), so the refinement time is unbounded as \(k\) grows even though the stable partition is orbit-exact. On the excluded matching boundary \(n=2k\), when \(k\ge3\), the stable partition has only the three sets \(\mathcal T_k\), \(\mathcal T_0\), and \(\bigcup_{t=1}^{k-1}\mathcal T_t\); it does not resolve the natural intersection strata. These assertions concern the orbit partition in the **given marked graph**, not identification among all graphs.

The sets \(\mathcal T_t\) are precisely the orbits of the natural permutations of \([n]\) fixing \(R\) setwise; therefore they are also the full marked-graph automorphism orbits when \(n>2k\), by the standard automorphism theorem for Kneser graphs. The main partition assertion itself does not require that automorphism theorem.

## Assumptions and scope
All graphs are finite, undirected, simple, and unweighted. The singled-out vertex has a colour distinct from the common colour of all other vertices. A refinement round simultaneously replaces each colour by the pair consisting of its previous colour and the counts of neighbours of every previous colour. The number of rounds is the least \(r\ge0\) for which the partition after round \(r\) is already stable; the first recolouring is round one. The assertion \(n\ge2k+1\) is essential to the spectral argument and avoids the disjoint matching case. The theorem concerns exact counting refinement, not non-counting refinement, higher-dimensional refinement, or global graph identification.

## Proof
**1. The orbital quotient.** Put \(m=n-2k\). The group \(S_R\times S_{[n]\setminus R}\) acts transitively on each \(\mathcal T_t\). If \(X\in\mathcal T_t\), the number of its neighbours in \(\mathcal T_u\) is
\[
B_{tu}=\binom{k-t}{u}\binom{m+t}{k-u},\qquad 0\le t,u\le k,
\]
with out-of-range binomial coefficients interpreted as zero: choose \(u\) elements from \(R\setminus X\) and the remaining \(k-u\) from the \(m+t\) elements outside \(R\cup X\). Hence every refinement colour is constant on each \(\mathcal T_t\), and no refinement can split one such stratum.

**2. Spectral separation for every connected Kneser graph.** Let \(A\) be the adjacency operator on real functions on the vertex set. The space \(U\) of functions constant on the \(k+1\) strata has dimension \(k+1\). For \(0\le j\le k\), define \(\phi_j(X)=\binom{|X\cap R|}{j}\). These functions form a basis of \(U\). Counting pairs consisting of a neighbour \(Y\) of \(X\) and a \(j\)-subset of \(Y\cap R\) gives
\[
(A\phi_j)(X)=\binom{n-k-j}{k-j}\binom{k-|X\cap R|}{j}.
\]
In the ordered polynomial basis \(\phi_0,\ldots,\phi_k\), the restriction \(A|_U\) is triangular with diagonal values
\[
\lambda_j=(-1)^j\binom{n-k-j}{k-j}\quad(0\le j\le k).
\]
These are all distinct when \(n>2k\), since their absolute values strictly decrease with \(j\).

There are only \(k+1\) orbits of the full symmetric group on ordered pairs of \(k\)-sets, classified by intersection size. Thus the real algebra of matrices commuting with its action has dimension \(k+1\). Since it contains all powers of \(A\), the symmetric matrix \(A\) has at most \(k+1\) distinct eigenvalues. The restriction to \(U\) already supplies \(k+1\), so \(\lambda_0,\ldots,\lambda_k\) are precisely all the distinct eigenvalues of \(A\).

Let \(e_R\) be the indicator of the distinguished vertex. Each orthogonal spectral projector \(P_j\) of \(A\) is nonzero and commutes with the vertex-transitive action of \(S_n\). Its diagonal is constant and equals \(\operatorname{rank}(P_j)/\binom nk>0\), so \(P_j e_R\ne0\). The Vandermonde matrix on the distinct \(\lambda_j\) now shows that \(e_R,Ae_R,\ldots,A^k e_R\) are linearly independent. All lie in \(U\), so they form a basis of \(U\).

At round \(r\), the function \(A^r e_R\) is constant on every current colour class: this holds at round zero, and the defining neighbour-count update proves the induction. By round \(k\), every function in \(U\) is constant on each colour class, including every stratum indicator (as a linear combination of these powers). Consequently no two different strata can share a colour. This proves orbit-exactness and the bound of \(k\) rounds.

**3. The sharp two-round phase.** Assume \(k\ge3\). At round one the classes of intersection parameters are exactly \(\{k\}\), \(\{0\}\), and \(\{1,\ldots,k-1\}\). For a vertex in \(\mathcal T_t\) with \(1\le t\le k-1\), the number of neighbours in \(\mathcal T_0\) is
\[
B_{t0}=\binom{m+t}{k}.
\]
Its count of neighbours in \(\mathcal T_k\) is zero, while the degree is fixed; thus these are the only new distinguishing data inside the remaining class. The displayed numbers vanish exactly when \(t<k-m\) and are strictly increasing afterward. They are pairwise distinct over \(1\le t\le k-1\) precisely when at most one of them is zero, equivalently \(m\ge k-2\), or \(n\ge3k-2\). If \(m<k-2\), parameters \(t=1,2\) both have zero counts and cannot split in round two. Since round one leaves at least two such parameters together, exactly two rounds are necessary and sufficient in the claimed range. For \(k=2\), the sole intermediate parameter is already isolated at round one; for \(k=1\), the initial singleton and its complement are the two strata.

**4. Sharp depth on odd graphs.** Set \(m=1\). The quotient formula shows \(B_{tu}\ne0\) only when \(u\in\{k-t-1,k-t\}\) (within \([0,k]\)). Breadth-first search from \(t=k\) in this quotient discovers the distinct strata in the exact order
\[
k,\ 0,\ k-1,\ 1,\ k-2,\ 2,\ldots,
\]
until all \(k+1\) occur. This follows inductively: each newly visited stratum has one edge towards the previously visited end and, unless it is last, one edge towards the next unvisited parameter; no edge skips a parameter in this sequence. Therefore the strata are exactly the distance spheres about \(R\), of distances \(0,1,\ldots,k\), and each sphere is transitive under the natural stabilizer of \(R\).

At round \(r\), for \(0\le r\le k-1\), refinement gives exactly the individual distance spheres \(0,\ldots,r\) together with the union of all spheres at distance at least \(r+1\). Inductively, vertices at distance \(r+1\) have a neighbour in the sphere of radius \(r\), while vertices farther away have none; vertices in the same sphere have equal neighbour counts by transitivity. This isolates exactly the next sphere (for the last step, its complement is the final sphere). For \(r<k-1\) at least two spheres remain merged; at \(r=k-1\) every stratum is separate. Hence the least stable round is exactly \(k-1\), including \(k=1\).

**5. Matching boundary.** If \(n=2k\), each vertex has only its set complement as a neighbour. From the marked root, round one separates the root, its complement, and every other vertex. The last class is invariant, and no further refinement is possible. For \(k\ge3\) this fuses the nonempty parameters \(1,\ldots,k-1\), establishing the asserted failure of intersection-stratum recovery.

## Verification
The standalone program `verify.py` computes the exact orbital quotient, iterates counting refinement on that quotient for \(285\) parameter pairs with \(1\le k\le15\), tests the matching boundary in \(11\) cases, and independently constructs and refines the full labelled graphs in \(10\) small cases of up to \(495\) vertices. Full-graph partitions are compared with the explicit intersection strata; all comparisons passed. Run with `python verify.py` using only the Python standard library. The recorded stdout is in `verify.log`. These finite tests check the formulas and definitions but cannot prove the infinite theorem; the preceding argument supplies that proof.

## Relationship to prior work
One-dimensional counting colour refinement and the associated two-variable counting logic are established subjects; see Kiefer, Schweitzer and Selman (2015). Kneser graphs and their symmetric association schemes are classical; van Dam and Sotirov (2013) describe their orbital matrix algebras for graph partitioning, not this rooted refinement classification. The present contribution is the root-marked partition theorem across all connected Kneser graphs, its sharp two-round density threshold, its linear-in-\(k\) odd-graph depth, and the matching-boundary failure. In particular, a refinement result obtained by **individually colouring two vertices** does not imply the one-anchor theorem: the two initial colours provide strictly more information. Standard Kneser spectral and odd-graph distance-transitivity facts are used as background; the self-contained spectral and quotient proofs above make the logical implication explicit.

## Limitations
This is an orbit-recovery statement for a fixed pointed graph, not a graph-isomorphism identification theorem against arbitrary competitors. The upper bound \(k\) is not asserted optimal for every \((n,k)\); only the two-round criterion and the odd-graph exact depth are asserted sharp. The matching case \(n=2k\) is disconnected and not covered by the universal orbit-stratum statement. Complete publication-priority exclusion cannot be inferred from a bounded literature search; association-scheme folklore may contain an equivalent spectral observation. The finite tests cover only the stated finite range. No independent scientific audit has been performed.

## References
1. E. R. van Dam and R. Sotirov, *Semidefinite programming and eigenvalue bounds for the graph partition problem*, first publicly posted 2013-12-02, arXiv:1312.0332, https://arxiv.org/abs/1312.0332 (notably Sections 2 and 4.3).
2. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, first publicly posted 2015-03-30, arXiv:1503.08792, https://arxiv.org/abs/1503.08792 (notably introduction and counting-logic context).
