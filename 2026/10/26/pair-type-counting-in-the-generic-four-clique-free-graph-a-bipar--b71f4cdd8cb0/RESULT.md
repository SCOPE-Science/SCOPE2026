# Pair-type counting in the generic four-clique-free graph: a bipartite complexity jump

## Finding
Let \(H_4\) be the countable homogeneous universal \(K_4\)-free graph. Let \(G\subseteq H_4\) be any finite induced \(K_4\)-free parameter graph. Denote by \(T_2(G)\) the number of complete types over the individually named vertices of \(G\) of **ordered distinct** vertices \((x,y)\), both outside \(G\). Define
\[
F(G)=\bigl|\{A\subseteq V(G):G[A]\text{ contains no triangle}\}\bigr|
\]
and
\[
Q(G)=\bigl|\{(A,B):G[A],G[B]\text{ are triangle-free},\ G[A\cap B]\text{ has no edge}\}\bigr|.
\]
Then the exact two-type count is
\[
\boxed{T_2(G)=F(G)^2+Q(G).}
\]
In particular, whenever \(G\) is **bipartite**, of order \(n\), with independence polynomial
\[
I_G(z)=\sum_{\substack{S\subseteq V(G)\\S\text{ independent}}}z^{|S|},
\]
the pair-count polynomial by the edge status of the new tuple is
\[
\boxed{\Theta_{2,G}(u)=4^n+u\sum_{S\text{ independent}}3^{n-|S|}
=4^n+u\,3^n I_G(1/3).}
\]
In particular, \(T_2(G)=\Theta_{2,G}(1)\). Computing this integer exactly from a bipartite parameter graph is **\(\#\mathrm P\)-complete under polynomial-time Turing reductions**. In contrast, over the same bipartite parameter graphs, the number of complete nonalgebraic **one**-types is simply \(2^n\). This is an exact arity-one-to-arity-two counting-complexity jump on a fixed natural class of parameters.

## Assumptions and scope
All graphs are simple, undirected and loopless. The ambient structure is the fixed countable homogeneous universal \(K_4\)-free graph \(H_4\), in the graph language. Parameter vertices are pointwise named. Types count different complete first-order types of the ordered pair \((x,y)\), constrained by \(x\ne y\) and \(x,y\notin V(G)\); algebraic tuple types and repetitions are not included. The bipartite parameter graph may be disconnected or empty. The complexity problem uses an ordinary finite bipartite graph as input; a non-bipartite encoded input is rejected. The computational complexity assertion concerns *exact* counting and polynomial-time Turing reductions only.

## Proof
**1. Why finite extensions count complete types.** Homogeneity and universality of \(H_4\) imply that every finite induced \(K_4\)-free extension of \(G\) embeds over \(G\), and two ordered pairs inducing the same labelled extension lie in the same orbit of the pointwise stabilizer of \(G\). Such orbits are exactly complete types: the pair's quantifier-free diagram determines all its formulas by ultrahomogeneity/quantifier elimination. Thus it suffices to count the permitted edge status \(xy\) and the labelled neighborhoods \(A=N(x)\cap G\), \(B=N(y)\cap G\).

**2. Exact constraints for general \(G\).** A forbidden \(K_4\) involving exactly one of \(x,y\) exists precisely when \(G[A]\) or \(G[B]\) contains a triangle. If \(xy\) is absent, no forbidden \(K_4\) can involve both new vertices. This gives exactly \(F(G)^2\) nonedge extensions. If \(xy\) is present, a forbidden \(K_4\) using both new vertices exists precisely when there is an edge in \(G[A\cap B]\). The triangle-free conditions remain necessary and sufficient for the cases using one new vertex. This gives exactly \(Q(G)\) edge extensions. Conversely, when those conditions hold, the full finite extension is \(K_4\)-free and hence is realized over \(G\). Adding both disjoint possibilities proves \(T_2(G)=F(G)^2+Q(G)\).

**3. Bipartite specialization and the contrast with one-types.** Every subset of a bipartite graph is triangle-free, so \(F(G)=2^n\). When \(xy\) is an edge, set \(S=A\cap B\). The common-neighborhood condition is precisely that \(S\) is independent. For each vertex outside \(S\), there are exactly three membership possibilities: in \(A\setminus B\), in \(B\setminus A\), or in neither. Therefore the number of edge extensions is exactly \(\sum_{S\text{ independent}}3^{n-|S|}=3^n I_G(1/3)\), which is an integer. If \(xy\) is absent, the two neighborhoods are arbitrary, giving \(4^n\) possibilities. For a single new vertex, every one of the \(2^n\) neighborhoods is valid; that yields the claimed one-type count. For example, \(T_2(E_n)=2\cdot4^n\), and for a complete bipartite graph \(K_{a,b}\),
\[
T_2(K_{a,b})=4^{a+b}+4^a3^b+3^a4^b-3^{a+b}.
\]

**4. Membership in \(\#\mathrm P\).** A nondeterministic polynomial-time machine guesses one bit for \(xy\) and two \(n\)-bit neighborhood indicators. It checks that the finite extension has no \(K_4\) (and that the input is bipartite); there is one accepting computation for each counted pair type. Thus this function lies in \(\#\mathrm P\).

**5. Hardness via rational evaluation interpolation.** Exact counting of independent sets of bipartite graphs (\(\#\mathrm{BIS}\)) is \(\#\mathrm P\)-complete; equivalently, count bipartite vertex covers and complement each chosen cover. Given a bipartite graph \(B\) with \(n\ge1\) vertices, for each \(t=1,\ldots,n+1\) form \(B^{(t)}\) by replacing every vertex with \(t\) independent clones and every original edge with all \(t^2\) cross edges. Every \(B^{(t)}\) remains bipartite, with \(nt\) vertices. An independent set in the clone graph may choose a nonempty subset of the clones of exactly those original vertices forming an independent set. Consequently, for every indeterminate \(z\),
\[
I_{B^{(t)}}(z)=I_B((1+z)^t-1).
\]
Our pair-type oracle at \(B^{(t)}\) returns
\[
T_2(B^{(t)})=4^{nt}+3^{nt}I_{B^{(t)}}(1/3).
\]
Therefore one oracle call gives the exact rational value
\[
I_B(z_t)=\frac{T_2(B^{(t)})-4^{nt}}{3^{nt}},\qquad
z_t=(4/3)^t-1.
\]
The \(n+1\) rational numbers \(z_t\) are distinct. Since \(I_B(z)\) has degree at most \(n\), exact polynomial interpolation reconstructs \(I_B\) and in particular \(I_B(1)=\#\mathrm{BIS}(B)\). All constructed graphs have at most \(n(n+1)\) vertices. Exponents, oracle outputs, interpolation nodes, and the rational arithmetic have polynomial bit length. This is a polynomial-time Turing reduction from \(\#\mathrm{BIS}\), proving \(\#\mathrm P\)-hardness and hence the theorem. For \(n=0\) the answer to \(\#\mathrm{BIS}\) is directly \(1\).

## Verification
Run the standalone Python standard-library checker `verify.py`. It independently enumerates all ordered two-neighborhood diagrams and tests the resulting finite extensions for forbidden four-cliques, rather than assuming the displayed formula. It checks 75 \(K_4\)-free input graphs through four vertices, including 52 bipartite graphs, and independently validates clone substitutions plus exact rational Lagrange interpolation on 51 bipartite input configurations. An execution record is in `verify.log`. The finite tests corroborate the general proof; no experiment establishes the universal assertion by itself.

## Relationship to prior work
Henson's 1971 construction establishes the homogeneous universal \(K_r\)-free graph and its extension property (Theorem 2.3). Conant's arXiv:1401.1570v1, especially Section 3, treats finite tuple diagrams and type realization in Henson graphs; these foundational facts are used, not claimed as new. Provan and Ball's 1983 result that counting bipartite vertex covers is \(\#\mathrm P\)-complete supplies the source problem. A published one-type result for Henson graphs already identifies the \(K_{r-1}\)-free subset polynomial and proves general-parameter one-type hardness. For the four-clique-free graph, that earlier hardness reduction introduces a universal join vertex and does not establish hardness **restricted to bipartite parameters**; over bipartite parameters one-types instead have the elementary count \(2^n\).

The retained contribution is the joint-neighborhood compatibility identity and the resulting arity-two complexity jump under bipartite parameters. Searches for equivalent two-type formulas, weighted independence-polynomial specializations, and reductions did not identify a prior theorem with this precise content. This is a bounded prior-art comparison, not a proof of publication priority.

## Limitations
No independence of the present work from every unpublished or unindexed source is claimed. The theorem concerns complete types of a distinct pair outside the parameter set, not all two-variable types with equality and algebraic assignments. It neither implies approximate-counting hardness nor supplies a single-call many-one/metric reduction. A rational-interpolation Turing reduction is proved. The general \(K_4\)-free identity is exact, but the hardness claim is specifically stated on bipartite parameters. No independent scientific audit has been conducted.

## References
1. C. W. Henson, “A family of countable homogeneous graphs,” *Pacific Journal of Mathematics* 38 (1971), 69–83, Theorem 2.3. DOI: 10.2140/pjm.1971.38.69. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-p.pdf
2. G. Conant, “Forking and dividing in Henson graphs,” arXiv:1401.1570v1 (first public 2014-01-08), especially Section 3. https://arxiv.org/pdf/1401.1570
3. J. S. Provan and M. O. Ball, “The complexity of counting cuts and of computing the probability that a graph is connected,” *SIAM Journal on Computing* 12 (1983), 777–788. DOI: 10.1137/0212053.
4. “Exact finite-parameter 1-type counting in Henson graphs is #P-complete,” published research finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650 .
