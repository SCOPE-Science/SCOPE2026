# Rare catastrophic jamming from bounded-degree exclusions in dense bipartite adsorption

## Finding
Let \(H_n\) be a finite simple bipartite graph with vertex classes \(A_n,B_n\), each of cardinality \(n\), and maximum degree at most a **fixed** integer \(D\ge1\). Define the adsorption-exclusion graph \(G_n=K_{n,n}\setminus E(H_n)\), and let \(X_n\) be the total number of accepted vertices in single-attempt random sequential adsorption: inspect all \(2n\) vertices in a uniformly random order and accept a vertex if no earlier accepted vertex is adjacent to it in \(G_n\). Write \(m_n=|E(H_n)|\).

**Theorem (rare-jamming universality).** Uniformly over all such \(H_n\), for fixed \(D\) and \(n\to\infty\),
\[
\begin{aligned}
\Pr(X_n<n)&=\frac{m_n}{n^2}+O_D(n^{-2}),\\
\mathbb E X_n&=n-\frac{m_n}{n}+O_D(n^{-1}),\\
\operatorname{Var}(X_n)&=m_n+O_D(1).
\end{aligned}
\]
For every sufficiently large \(n>2D\), the terminal set either has exactly \(n\) occupied vertices, all in one bipartition class, or has between \(2\) and \(2D\) occupied vertices drawn from both classes. In particular, if \(m_n/n\to c\in[0,D]\), then \(X_n/n\to1\) in probability but \(\operatorname{Var}(X_n)/n\to c\), and for each fixed integer \(r\ge2\),
\[
\lim_{n\to\infty}\frac{\mathbb E[(X_n-\mathbb E X_n)^r]}{n^{r-1}}=(-1)^r c.
\]
Thus the nonzero linear variance, and higher macroscopic central moments, arise from events of probability of order \(n^{-1}\) rather than Gaussian-size fluctuations.

**Exact two-point family.** Suppose \(H_n\) is **any** simple bipartite \(2\)-regular graph on these parts with no four-cycle; equivalently, it is a disjoint union of even cycles of length at least six. For every \(n\ge4\), independently of the numbers and lengths of its cycle components,
\[
\boxed{\Pr(X_n=3)=\frac{2n}{n^2-1},\qquad
\Pr(X_n=n)=1-\frac{2n}{n^2-1}.}
\]
In particular, \(\mathbb E X_n=n-2+O(n^{-1})\) and \(\operatorname{Var}(X_n)=2n+O(1)\). As an additional exact benchmark, if \(H_n\) is a matching of cardinality \(k\), then for \(n\ge3\) the output equals \(2\) with probability \(k/n^2\) and equals \(n\) otherwise.

## Assumptions and scope
The graph \(H_n\) consists of **deleted cross edges**: every pair in \(A_n\times B_n\) is an edge of \(G_n\) unless it belongs to \(E(H_n)\), and there are no edges inside either class of \(G_n\). No assumptions of connectedness, randomness, regularity, or uniform degree are made on \(H_n\) in the universal part. The degree bound \(D\) is independent of \(n\); the error constants may depend on \(D\) but not on the graph. Ties among priorities have probability zero. This concerns the final occupied **count**, not the time needed to reach jamming or the full set-valued distribution. The exact two-point family requires every vertex to have missing degree two and no four-cycle; the special case \(n=3\) has deterministic count three and is excluded from that two-point count statement.

## Proof
**1. Configuration dichotomy.** The first inspected vertex is always accepted. If no vertex from the opposite class is ever accepted, every vertex on the initial side will be accepted, since same-side vertices have no edges, so \(X_n=n\). If vertices \(x\in A_n\) and \(y\in B_n\) are both accepted, then they must be nonadjacent in \(G_n\), i.e. \(xy\in E(H_n)\). Every occupied \(A_n\)-vertex belongs to the \(H_n\)-neighborhood of \(y\), and every occupied \(B_n\)-vertex belongs to that of \(x\). Thus the mixed output has cardinality between \(2\) and \(2D\). For \(n>2D\), the event \(C_n\) that both sides are occupied is exactly \(\{X_n<n\}\).

**2. Exact characterization of the rare event.** Assign independent continuous uniform arrival labels \(T_v\); their ranks give the greedy order. Condition on a particular first vertex \(x\in A_n\). For each \(y\in N_{H_n}(x)\), define
\[
 F_y=\{T_y< T_z\text{ for every }z\in A_n\setminus N_{H_n}(y)\}.
\]
Then \(C_n=\bigcup_{y\in N_{H_n}(x)}F_y\). Indeed, if \(F_y\) holds, no earlier-arriving \(A_n\)-vertex is adjacent in \(G_n\) to \(y\), so \(y\) is accepted. Conversely, take the first accepted vertex \(y\in B_n\). Before its arrival, no \(B_n\)-vertex was accepted, so every earlier-arriving \(A_n\)-vertex was accepted; consequently all must be \(H_n\)-neighbors of \(y\), which is exactly \(F_y\). Conditional on \(x\) being first, the remaining labels have uniform relative order. Therefore
\[
 \Pr(F_y\mid x\text{ first})=\frac{1}{n-\deg_{H_n}(y)+1}.
\]
For distinct \(y,z\in N_{H_n}(x)\), both events require \(y,z\) to precede every vertex in the common set of \(A_n\)-vertices adjacent to both of them in \(G_n\). That set contains at least \(n-2D\) vertices. Hence, for \(n>2D\),
\[
 \Pr(F_y\cap F_z\mid x\text{ first})
 \le\frac{2}{(n-2D+1)(n-2D+2)}.
\]
The union bound and the second Bonferroni inequality now yield, uniformly in \(x\),
\[
\Pr(C_n\mid x\text{ first})=\frac{\deg_{H_n}(x)}{n}+O_D(n^{-2}).
\]
The same holds for a first vertex in \(B_n\). Averaging over the \(2n\) equally likely first vertices and using the bipartite degree sum \(\sum_v\deg_{H_n}(v)=2m_n\), we obtain
\[
 \Pr(C_n)=\frac{m_n}{n^2}+O_D(n^{-2}).
\]
Since \(m_n\le Dn\), this is \(O_D(n^{-1})\).

**3. Moments.** Let \(Z_n=n-X_n\). It vanishes off \(C_n\), while \(n-2D\le Z_n\le n-2\) on \(C_n\). Therefore \(\mathbb EZ_n=n\Pr(C_n)+O_D(\Pr(C_n))=m_n/n+O_D(n^{-1})\). Similarly \(\mathbb EZ_n^2=n^2\Pr(C_n)+O_D(n\Pr(C_n))=m_n+O_D(1)\). Subtracting \((\mathbb EZ_n)^2=O_D(1)\) proves the variance statement. If \(m_n/n\to c\), the event \(C_n\) has probability \(c/n+o(n^{-1})\); on that event \((X_n-\mathbb EX_n)/n\to-1\) uniformly, and on its complement the centered variable is bounded. Splitting the expectation over these two events gives the stated limit for each fixed \(r\ge2\). Also \(\Pr(X_n/n\ne1)=O_D(n^{-1})\), proving convergence in probability.

**4. Exact cycle-complement law.** Let \(H_n\) be bipartite \(2\)-regular with no four-cycle. Conditional on any first \(x\), its two missing-edge neighbors \(y,z\) each have one additional neighbor on the initial side, and those two additional neighbors are distinct. Hence \(\Pr(F_y)=\Pr(F_z)=1/(n-1)\). Relabel the remaining priorities as independent uniforms \(u=T_y\) and \(v=T_z\), and let \(W\) be the other \(n-3\) vertices in the initial side outside the union of their \(H_n\)-neighborhoods. Independence of priorities gives
\[
\begin{aligned}
\Pr(F_y\cap F_z\mid x\text{ first})
&=\int_0^1\!\int_0^1(1-u)(1-v)(1-\max\{u,v\})^{n-3}\,du\,dv\\
&=\frac{2}{n^2-1}.
\end{aligned}
\]
Inclusion-exclusion gives \(\Pr(C_n\mid x\text{ first})=2/(n-1)-2/(n^2-1)=2n/(n^2-1)\), independent of \(x\). Every terminal mixed independent set of \(G_n\) is a maximal complete bipartite subgraph of \(H_n\) using both parts. A \(2\)-regular bipartite graph without four-cycles has only three-vertex stars as its maximal nonempty two-sided bicliques; thus mixed outputs have cardinality exactly three. Unmixed outputs have cardinality \(n\), completing the two-point law. For a deleted matching of size \(k\), one candidate event occurs with conditional probability \(1/n\) for each matched first vertex, giving \(\Pr(C_n)=k/n^2\); its mixed output has cardinality two.

## Verification
The accompanying Python 3 standard-library program `verify.py` independently generates vertex permutations, simulates adsorption using the actual adjacency rule, and separately evaluates the arrival-order criterion for mixed occupancy. It checks both descriptions for every permutation of every missing-edge graph of maximum degree at most two on two parts of size three, plus five specified four-by-four missing-edge graphs. A total of \(392{,}400\) permutations across \(270\) graph instances passed. In particular the four-by-four deleted-cycle exact distribution is \(\Pr(X_4=3)=8/15\) and \(\Pr(X_4=4)=7/15\), and the deleted-matching law was verified at sizes three and four. Independent seeded checks of larger deleted matchings test the probabilities numerically. These finite tests corroborate, but are not used to prove, the all-size theorem.

## Relationship to prior work
The random-priority vertex adsorption process is classical; Pippenger (1989) studied it on regular graphs with few short cycles and related lattice families. Brightwell, Janson, and Luczak (2015 preprint) study greedy independent sets on random graphs with specified degree sequences; their key sparse graph assumptions do not cover nearly complete bipartite graphs of diverging degree. Krivelevich, Mészáros, Michaeli, and Shikhelman (2023 preprint/2024 journal) establish local-limit formulas and concentration under local growth assumptions, rather than the microscopic deletion-controlled, unnormalized variance law here. The published complete-multipartite exact variance result and published chain-graph exact output law address different graph classes: when \(H_n\) has a nonempty sparse matching or is a disjoint union of long even cycles, \(G_n\) has neither the full complete-multipartite structure nor nested bipartite neighborhoods. Their formulas therefore do not imply the present law.

The claimed contribution is limited to the bounded-deletion-degree universal rare-event asymptotics and the explicit two-regular exact two-point law. No novelty is asserted for the random-priority adsorption rule, the general maximal-independent-set interpretation, or the elementary count for an unmodified complete bipartite graph.

## Limitations
All results require a fixed bound on the degrees of the **deleted-edge graph**, not simply a sparse total number of deleted edges. No uniform conclusion is asserted when its maximum degree grows. The central moments are not a Gaussian central limit theorem; indeed, after square-root scaling the centered count converges in probability to zero in the illustrative positive-\(c\) regime despite nonvanishing normalized variance. The argument does not determine arrival-time kinetics or higher joint spatial occupancy distributions. Some older work on graph adsorption could not be inspected in full; the originality comparison remains best-knowledge rather than a proof that no equivalent theorem exists.

## References
1. G. Brightwell, S. Janson, M. Luczak, *The greedy independent set in a random graph with given degrees*, first arXiv version 19 October 2015, arXiv:1510.05560. https://arxiv.org/abs/1510.05560
2. N. Pippenger, *Random sequential adsorption on graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, DOI:10.1137/0402034. https://doi.org/10.1137/0402034
3. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015. https://doi.org/10.1002/rsa.21200
4. *Sharp variance of random greedy maximal independent sets on complete multipartite graphs*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-random-greedy-mis-variance-complete-multipartite--9cd73ef8690f
5. *Exact random-greedy maximal-independent-set law on chain graphs*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-random-greedy-maximal-independent-set-law-on-chain-graphs--36fe61ce32de
