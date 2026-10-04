# Exact finite-parameter 1-type counting in Henson graphs is #P-complete

## Finding
Fix an integer \(r\ge 3\), and let \(H_r\) be the countable universal homogeneous \(K_r\)-free (Henson) graph with complete theory \(T_r\). For a finite induced subgraph \(A\subseteq H_r\), define the nonalgebraic 1-type neighborhood enumerator
\[
\Theta_{r,A}(y)=\sum_{p\in S_1^{T_r}(A)\setminus S_1^{\mathrm{alg}}(A)}y^{\nu_A(p)},
\qquad
\nu_A(p)=\bigl|\{a\in A:E(x,a)\in p\}\bigr|.
\]
Also define the \(K_{r-1}\)-free induced-subset polynomial
\[
C_{r-1}(A;y)=\sum_{\substack{S\subseteq A\\A[S]\text{ is }K_{r-1}\text{-free}}}y^{|S|}.
\]
Then
\[
\boxed{\Theta_{r,A}(y)=C_{r-1}(A;y)}
\]
and therefore
\[
\boxed{|S_1^{T_r}(A)|=|A|+C_{r-1}(A;1)}.
\]
For \(r=3\), \(K_2\)-free means independent, so \(C_2(A;y)\) is exactly the ordinary independence polynomial \(I_A(y)\). Thus the nonalgebraic 1-type neighborhood distribution over a finite parameter graph is literally its independence polynomial.

There is also an exact complexity consequence. For every fixed \(r\ge3\), define \(\operatorname{TypeCount}_r(A)\) to be \(|S_1^{T_r}(A)|\) when \(A\) is \(K_r\)-free and \(0\) otherwise. Then
\[
\boxed{\operatorname{TypeCount}_r\text{ is #P-complete under polynomial-time metric reductions.}}
\]
Hardness already holds on the restricted family
\[
A=B\vee K_{r-3},
\]
where \(B\) is bipartite and \(\vee\) denotes graph join. If \(n=|B|\) and \(i(B)\) is the number of independent sets of \(B\), then
\[
C_{r-1}(B\vee K_{r-3};1)
=(2^{r-3}-1)2^n+i(B),
\]
with the same formula valid for \(r=3\) by taking \(K_0\) empty. Hence
\[
i(B)=\operatorname{TypeCount}_r(B\vee K_{r-3})
-|B\vee K_{r-3}|-(2^{r-3}-1)2^n.
\]
Since exact independent-set counting is #P-complete even on bipartite graphs, this is a metric reduction.

Two five-parameter examples show that the polynomial refinement carries information lost by the scalar type count. For \(A=C_5\),
\[
\Theta_{3,A}(y)=1+5y+5y^2,
\qquad |S_1(A)|=16,
\]
whereas for \(A=K_{2,3}\),
\[
\Theta_{3,A}(y)=1+5y+4y^2+y^3,
\qquad |S_1(A)|=16.
\]
The total numbers of 1-types coincide, but their neighborhood-size distributions differ.

## Assumptions and scope
The integer \(r\ge3\) is fixed. Graphs are simple, undirected, and loopless. The parameter set \(A\) is identified with its finite induced graph in \(H_r\). The complexity statement concerns exact counting and polynomial-time metric reductions; it does not assert hardness of approximation and in particular does not resolve the approximation complexity of #BIS.

The eligible primary literature source is Siniora and Solecki's paper on coherent EPPA and free amalgamation. It was first public on 2017-05-04 as arXiv:1705.01888, and the published metadata lists Primary MSC codes including 03C15. Their Example 4.3 explicitly lists the universal homogeneous \(K_n\)-free graph as a free homogeneous structure.

The admissible-neighborhood criterion itself is treated as prior/standard rather than claimed as new. Hubička explicitly packages the triangle-free case as Katětov functions, where the positive coordinates cannot contain an adjacent pair; Letzter and Sahasrabudhe likewise describe the universal homogeneous triangle-free graph by adjoining vertices for all independent neighborhoods. The retained contribution is the finite-parameter generating-polynomial identity for the Henson family together with the exact #P-completeness theorem and its uniform reduction for every fixed \(r\ge3\).

## Proof
Because \(H_r\) is homogeneous in a relational language, finite tuples with the same quantifier-free type lie in the same automorphism orbit; equivalently, \(T_r\) has quantifier elimination in this presentation. Fix finite \(A\subseteq H_r\).

Every algebraic 1-type over \(A\) is \(x=a\) for a unique \(a\in A\), giving exactly \(|A|\) algebraic types. Consider a nonalgebraic realization \(x\notin A\), and put
\[
S=N(x)\cap A.
\]
If \(A[S]\) contained a \(K_{r-1}\), then adjoining \(x\), which is adjacent to every vertex of \(S\), would create a \(K_r\), impossible in \(H_r\). Hence \(S\) must be \(K_{r-1}\)-free.

Conversely, let \(S\subseteq A\) be \(K_{r-1}\)-free. Adjoin a new point \(x\) adjacent exactly to \(S\). The resulting finite graph is still \(K_r\)-free: any new \(K_r\) would have to contain \(x\), and its other \(r-1\) vertices would form a \(K_{r-1}\) inside \(S\). Since the age of \(H_r\) is the class of finite \(K_r\)-free graphs, this one-point extension embeds into \(H_r\) over \(A\). Thus every \(K_{r-1}\)-free subset occurs as a neighborhood pattern.

Finally, two nonalgebraic vertices realizing the same neighborhood subset of \(A\) induce isomorphic finite structures over \(A\); homogeneity extends that isomorphism to an automorphism fixing \(A\). Hence each admissible subset yields exactly one complete nonalgebraic 1-type. Weighting by \(|S|\) proves
\[
\Theta_{r,A}(y)=C_{r-1}(A;y),
\]
and adding the \(|A|\) algebraic types gives the scalar formula.

For #P membership, when \(r\) is fixed one can use witnesses of two forms: an algebraic witness naming one vertex of \(A\), or a subset \(S\subseteq A\) certified to contain no \(K_{r-1}\). The latter condition is decidable in polynomial time for fixed \(r\). If \(A\) is not \(K_r\)-free, reject all witnesses. The number of accepting witnesses is exactly \(\operatorname{TypeCount}_r(A)\).

For hardness, let \(B\) be any bipartite graph on \(n\) vertices and let \(C=K_{r-3}\). The join \(A=B\vee C\) has clique number at most \(2+(r-3)=r-1\), so it is a valid \(K_r\)-free parameter graph. If a candidate subset contains \(t\) vertices of \(C\), then for \(t\le r-4\) every subset of \(B\) is allowed, because its clique number is at most two and hence the total clique number is at most \(r-2\). If \(t=r-3\), the \(B\)-part must have clique number at most one, i.e. it must be independent. Therefore
\[
C_{r-1}(A;1)
=\left(\sum_{t=0}^{r-4}\binom{r-3}{t}\right)2^n+i(B)
=(2^{r-3}-1)2^n+i(B).
\]
The displayed subtraction recovers \(i(B)\) from one call to \(\operatorname{TypeCount}_r\), proving #P-hardness under metric reductions.

## Verification
The bundled `verify.py` independently checks the finite combinatorics without using the displayed proof as an oracle. It exhaustively enumerates \(K_r\)-free graphs through five vertices for \(r=3,4,5\), compares direct one-point \(K_r\)-freeness against the \(K_{r-1}\)-free-neighborhood criterion, and checks coefficient-by-coefficient agreement with the subset polynomial. It separately checks the triangle-free independence-polynomial specialization through six vertices.

For the complexity reduction it exhaustively enumerates all bipartite graphs with parts of size at most three, for every \(3\le r\le7\), constructs \(B\vee K_{r-3}\), and verifies
\[
C_{r-1}(B\vee K_{r-3};1)=(2^{r-3}-1)2^{|B|}+i(B).
\]
The replay covers 2,572 one-point-extension instances and 3,445 hardness-identity instances and terminates with `VERIFY_OK`. This is same-model verification; no independent audit has yet been performed.

## Relationship to prior work
Siniora and Solecki explicitly list the universal homogeneous \(K_n\)-free graph among free homogeneous structures. This supplies an eligible modern foundations source for the Henson family, but their result concerns coherent EPPA and automorphism groups, not finite-parameter type enumeration or counting complexity.

The local one-point admissibility rule is prior. In the triangle-free case, Hubička defines Katětov functions by exactly the condition that no adjacent pair receives the positive value. Letzter and Sahasrabudhe describe the universal homogeneous triangle-free graph as built by adding a vertex with neighborhood \(I\) for every independent set \(I\) in the current finite stage. Thus the statement “admissible neighborhoods are independent sets” is not part of the originality claim.

Conant's work studies complete types, forking, and dividing in the theories of generic \(K_n\)-free graphs, but targeted inspection and searches did not locate the subset-polynomial enumerator or a computational type-count theorem there. On the algorithms side, Goldberg, Lapinskas, and Richerby explicitly note that exact counting of independent sets is #P-complete even in bipartite graphs; that complexity fact is likewise prior and is used as the source problem in the reduction.

Targeted searches for combinations of “Henson graph”, “1-types”, “independence polynomial”, “clique-free subset”, “#P-complete”, and the exact reduction formula found no source stating the present bridge. Semantic searches in published-finding corpus likewise returned no matching finding. An OEIS search surfaced a sequence for big Ramsey degrees of independent sets in a universal triangle-free graph, which is a different invariant. The originality claim is therefore limited to the polynomial/type-count identification as an explicit finite-parameter invariant and the resulting #P-completeness theorem; an unindexed folklore observation remains possible.

## Limitations
The result is about exact finite-parameter 1-type counting only. It does not address approximate counting, higher-arity type spaces, asymptotic typical behavior of parameter graphs, or the case where \(r\) is part of the input. The #P-completeness reduction uses metric reductions, because the independent-set count is recovered by subtracting an explicitly computable offset from the type count. No independent audit has yet been performed. The literature search cannot rule out an equivalent statement hidden under substantially different terminology.

## References
1. D. Siniora and S. Solecki, “Coherent extension of partial automorphisms, free amalgamation, and automorphism groups,” *Journal of Symbolic Logic* 85 (2020), 199–223. arXiv:1705.01888. DOI: 10.1017/jsl.2019.32. https://arxiv.org/abs/1705.01888
2. J. Hubička, “Big Ramsey degrees using parameter spaces,” arXiv:2009.00967; later *Advances in Mathematics*. https://arxiv.org/abs/2009.00967
3. S. Letzter and J. Sahasrabudhe, “On existentially complete triangle-free graphs.” https://www.homepages.ucl.ac.uk/~ucahsle/papers/triangle-free.pdf
4. G. Conant, “Forking and dividing in Henson graphs,” *Notre Dame Journal of Formal Logic* 58 (2017). arXiv:1401.1570. DOI: 10.1215/00294527-2017-0016. https://arxiv.org/abs/1401.1570
5. L. A. Goldberg, J. Lapinskas, and D. Richerby, “Faster exponential-time algorithms for approximately counting independent sets,” *Theoretical Computer Science* 892 (2021), 48–84. arXiv:2005.05070. DOI: 10.1016/j.tcs.2021.09.009. https://arxiv.org/abs/2005.05070
