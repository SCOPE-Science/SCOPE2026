# Residual-forest characterization and power-domination polynomials for multipartite line graphs

## Finding

Let \(H=K_{a_1,\ldots,a_r}\), with \(r\ge2\) and positive integer part sizes \(a_i\), and let \(G=L(H)\). Define the power-domination polynomial by \(\mathcal P_G(z)=\sum_S z^{|S|}\), over all power-dominating sets of the labelled vertices of \(G\).

The full polynomial has a compact sum over part profiles. For \(0\le u_i\le a_i\), write \(|\mathbf u|=\sum_i u_i\), \(J(\mathbf u)=\{i:u_i>0\}\), and put
\[
 \Gamma(\mathbf u)=1-|J(\mathbf u)|+
   \sum_{\substack{i<j\\i,j\in J(\mathbf u)}}(u_i+u_j-u_i u_j),\qquad
 e(\mathbf v)=\sum_{i<j}v_i v_j.
\]
Set \(\delta=1\) if \(r=2\) and \(\min(a_1,a_2)=1\), and \(\delta=0\) otherwise. Then
\[
 \boxed{\displaystyle
 \mathcal P_G(z)=\sum_{0\le\mathbf u\le\mathbf a}
 (-1)^{|\mathbf u|}\Gamma(\mathbf u)\prod_i\binom{a_i}{u_i}
 (1+z)^{e(\mathbf a-\mathbf u)}-\delta.}
\]
Equivalently, the number of size-\(k\) sets is given by replacing the power \((1+z)^{e(\mathbf a-\mathbf u)}\) by \(\binom{e(\mathbf a-\mathbf u)}{k}\) and subtracting \(\delta\) only when \(k=0\). This uses \(\prod_i(a_i+1)\) summands before dropping zeros or collecting equal exponents. It covers arbitrary mixed part sizes, not just bipartite roots or complete roots. For example, the profile \((1,2,3)\) is neither of those cases and gives two size-one and 49 size-two power-dominating sets.

## Assumptions and scope

Graphs are finite, simple, undirected and labelled. The line graph has the edges of \(H\) as vertices; adjacency means sharing an endpoint. Power domination first observes the closed neighborhood of \(S\), then permits any observed vertex with exactly one unobserved neighbor to observe it. The empty set does not power dominate any graph in the stated family. An empty or edgeless graph counts as a forest. The case of only one part is not included.

## Proof

**1. Structural input: unused endpoints.** Given \(S\ne\varnothing\) as an original edge set, denote its endpoints by \(U\) and let \(W=V(H)\setminus U\). The initially unobserved edges are precisely those of \(H[W]\). A cycle there cannot be broken: the first forced edge on the cycle would require a forcing source incident to one of its endpoints, and that source sees both unobserved cycle edges at that endpoint. Conversely, if the unobserved edges form a nonempty forest, pick a leaf \(v\) in a component with an edge. A selected original edge meets two different parts, so \(v\) has a neighbor \(u\in U\) in another part. The initially observed edge \(uv\) has exactly one unobserved neighbor in the line graph, the unobserved leaf edge. Forcing it and repeating strips all remaining edges. Thus the successful nonempty selections are characterized by \(H[W]\) being a forest. In a complete multipartite graph this is precisely the condition \(\mathscr F(\mathbf t)\) that at most one part of the residual profile \(\mathbf t\) is nonempty, or exactly two are nonempty and at least one has size one. Three occupied parts give a triangle and two parts of size at least two give a four-cycle. The other profiles give edgeless graphs or stars.

**2. A sum on forbidden endpoints.** On subsets \(T\subseteq V(H)\), set \(f(T)=1\) if \(H[T]\) is a forest and zero otherwise. Define
\[
 \alpha(B)=\sum_{T\subseteq B}(-1)^{|B|-|T|}f(T).
\]
By cancellation on the subset lattice, \(f(W)=\sum_{B\subseteq W}\alpha(B)\). Now sum this identity over all edge sets \(S\), including the empty set for the moment, each weighted by \(z^{|S|}\), using for \(W\) the complement of the endpoints of \(S\). The sets satisfying \(B\subseteq W\) are precisely those made from edges internal to \(V(H)\setminus B\). Their sum of weights is \((1+z)^{e(\mathbf a-\mathbf u)}\), with \(u_i=|B\cap A_i|\) for the parts \(A_i\). For each \(\mathbf u\) there are \(\prod_i\binom{a_i}{u_i}\) choices of \(B\), all having the same \(\alpha(B)\). Finally the empty edge set contributes \(f(V(H))=\delta\) to this auxiliary sum, so it must be subtracted.

**3. Evaluation of the subset weight.** Remove the factor \((-1)^{|B|}\) from \(\alpha(B)\). The empty \(T\) contributes one. For a fixed occupied part \(i\in J(\mathbf u)\), the total contribution of nonempty selections confined to that part is \(\sum_{t=1}^{u_i}(-1)^t\binom{u_i}{t}=-1\). For exactly two occupied parts \(i,j\in J(\mathbf u)\), the condition is \(t_i=1\) or \(t_j=1\). The contribution with \(t_i=1\) equals \((-u_i)(-1)=u_i\); likewise the contribution with \(t_j=1\) is \(u_j\). Their overlap has contribution \(u_i u_j\), counted twice. No other support is allowed, so \(\alpha(B)=(-1)^{|\mathbf u|}\Gamma(\mathbf u)\). Inserting this into Step 2 proves the displayed formula.

**4. Boundary and comparison formulas.** When \(H=K_{1,b}\), every nonempty set power dominates the complete graph \(L(H)=K_b\), giving \((1+z)^b-1\); the subtraction is essential there. For another form of the sum, fix the exact unused profile \(\mathbf t\) with \(\mathscr F(\mathbf t)\) and put \(\mathbf b=\mathbf a-\mathbf t\). After choosing the unused vertices in \(\prod_i\binom{a_i}{t_i}\) ways, the selected edges must leave no isolate in the complementary profile. Their weight enumerator is
\[
 \sum_{0\le j_i\le b_i}(-1)^{\sum_i j_i}\prod_i\binom{b_i}{j_i}
             (1+z)^{e(\mathbf b-\mathbf j)}
\]
by inclusion–exclusion on isolated vertices. Summing over the stated forest profiles with \(\sum b_i\ge2\) gives a two-sum version. The compact formula evaluates the corresponding subset transform in closed form rather than running an inner inclusion–exclusion independently for each unused profile.

## Verification

Run `python3 verify_compact_polynomial.py` (Python 3.10 or newer, standard library). The verifier builds labelled multipartite line graphs, simulates closed-neighborhood observation and parallel legal forces, and compares the full coefficient list to the compact formula for every sorted profile with two to five parts of sizes at most four and at most thirteen edges. It checks the mixed example and the star boundary. The exact proof, not the finite comparisons, establishes the formula for all profiles. The accompanying original `verify_power_multipartite.py` and `verification_output.txt` provide checks of the two-sum version and known specializations.

## Relationship to prior work and limitations

Brimkov, Patel, Suriyanarayana and Teich, *Power domination polynomials of graphs*, arXiv:1805.10984, introduce the polynomial and give results for other graph families and a finite census. The structural criterion used here is covered on minimum-degree-at-least-two roots by *An edge-endpoint forest criterion and the complete power-domination landscape of the Petersen line graph* (Resultary df97bef8930a); a complete multipartite root with a vertex of degree one is a star. The rook minimum was already known to Soh and Koh (2014, DOI:10.1080/09728600.2014.12088762). The full rook and triangular specializations, including minimum-set multiplicities, are also covered by *Complete power-domination-set classification and polynomial of rectangular rook graphs* (48ce98e1f82f) and *Power domination of triangular graphs: star-forest rigidity and full enumerators* (b7c1b689a10e). No novelty is asserted for those statements, the ordinary inclusion–exclusion identity, or general subset Möbius inversion.

The distinct calculation is the explicit evaluated coefficient weight \(\Gamma(\mathbf u)\) giving a single profile sum for all labelled complete multipartite roots. Unlike separate rook or triangular formulas, it allows any number of parts and nonuniform multiplicities in three or more parts. The number of summands is polynomial in the total root order for fixed \(r\), not uniformly so for variable \(r\). This is a cardinality enumerator and makes no assertion about unlabeled selections, connected power domination, or arbitrary line graphs. The comparisons distinguish mathematical coverage, not historical priority; other equivalent formulas may exist outside the inspected sources.
