# The first distributivity transition in nearly complete random formal contexts

## Finding
Let \(\alpha>0\), let \(n\) be a positive integer, and let \(m_n=\lfloor\alpha n\rfloor\). Consider the formal context \(\mathcal K_n\) on \(n\) labelled objects and \(m_n\) labelled attributes in which all incidences are independent with probability \(1-q_n\). Let \(\mathcal B_n\) be its formal-concept lattice, and write \(D_n\) for the event that \(\mathcal B_n\) is distributive. As \(n\to\infty\):

1. If \(q_n=o(n^{-6/5})\), then \(\Pr(D_n)\to1\).
2. For fixed \(t>0\), if \(q_n=t n^{-6/5}\), then
   \[
     \Pr(D_n)=\exp(-\alpha^3t^5)+O_{\alpha,t}(n^{-1/5}).
   \]
   Moreover, the number of six-vertex path components in the missing-incidence graph converges in total variation to \(\operatorname{Pois}(\alpha^3t^5)\).
3. If \(n^{6/5}q_n\to\infty\) while \(nq_n\to0\), then \(\Pr(D_n)\to0\).

Thus \(n^{-6/5}\) is the sharp first loss-of-distributivity scale within the sparse missing-incidence regime \(q_n=o(1/n)\). The decisive component is a missing-incidence path on six vertices: its concept lattice is the nondistributive pentagon \(N_5\), whereas every tree with at most six vertices other than that path gives a distributive concept lattice. The assertion is about the first sparse transition, not monotonicity for all incidence densities.

## Assumptions and scope
A formal context is a finite triple \((G,M,I)\), with object set \(G\), attribute set \(M\), and incidence \(I\subseteq G\times M\). For \(A\subseteq G\), set \(A'=\{b\in M:\forall a\in A,\,(a,b)\in I\}\), and define \(B'\) dually for \(B\subseteq M\). A concept is a pair \((A,B)\) with \(A'=B\) and \(B'=A\). Concept order is inclusion of extents \(A\).

The missing-incidence graph \(H\) is the bipartite graph with vertex classes \(G,M\) and edges \(E(H)=(G\times M)\setminus I\). In the random model every possible missing edge occurs independently with probability \(q_n\). The graph is simple; isolated vertices are included. Distributivity has its standard two lattice identities; a single failed identity suffices to refute it. All asymptotic constants may depend on the displayed fixed parameters. No assertion is made for \(q_n\) bounded away from zero, for \(q_n\asymp1/n\), or for changes in \(m_n/n\) beyond the stated limit.

## Proof
**1. Graph representation and factorization.** A pair \((A,B)\) is a concept precisely when \(A\cup B\) is an inclusion-maximal independent set of \(H\). Indeed, independence says there are no missing edges between \(A\) and \(B\), and maximality says every excluded vertex has a missing edge to the opposite selected part; these are exactly the two closure equalities. The order between concepts is inclusion of their selected object sets. Every maximal independent set of a disjoint graph union is uniquely the union of maximal independent sets in its components. Hence the concept lattice of \(H\) is the direct product (under object-set inclusion) of the concept lattices of its connected components. Isolated vertices contribute singleton factors. A finite direct product is distributive exactly when all factors are distributive.

**2. The first obstructing tree.** Direct calculation of all unlabelled trees of orders \(1,2,3,4,5,6\) gives, respectively, \(1,1,1,2,3,6\) tree types. Among the six order-six trees, five give distributive concept lattices (with \(2,3,3,4,5\) concepts); the remaining type is the six-vertex path \(P_6\), giving \(N_5\). Every smaller tree gives a distributive lattice. Interchanging the two vertex colors dualizes the concept lattice, so the classification is independent of which bipartition is designated as objects. This finite classification can be checked without a graph-isomorphism oracle: Prüfer words enumerate every labelled tree of each order, two-coloring determines its object and attribute classes, and the displayed closure formulas enumerate its concept extents and the distributive identity. The supplied `verify.py` exhausts \(1+1+3+16+125+1296\) labelled trees and confirms that the only bad labelled ones are the \(360=6!/2\) paths on six vertices.

For a concrete witness, take objects \(o_1,o_2,o_3\), attributes \(a_1,a_2,a_3\), and missing edges \(o_1a_1,o_2a_1,o_2a_2,o_3a_2,o_3a_3\). These form \(P_6\). Its five closed extents are exactly
\[
\varnothing,\quad\{o_1\},\quad\{o_3\},\quad\{o_1,o_2\},\quad\{o_1,o_2,o_3\}.
\]
Taking \(x=\{o_1,o_2\}\), \(y=\{o_3\}\), and \(z=\{o_1\}\), one has \(x\wedge(y\vee z)=x\), but \((x\wedge y)\vee(x\wedge z)=z\ne x\). The pentagon obstruction itself is classical; its role as the unique first forest obstruction is what drives the probability law below.

**3. Graphs at the critical scale.** Set \(q_n=t n^{-6/5}\). Any connected bipartite graph on at least seven vertices contains a seven-vertex tree. The expected number of embeddings of such trees is \(O_{\alpha,t}(n^7q_n^6)=O(n^{-1/5})\). Any connected bipartite graph on at most six vertices that is not a tree contains a four-cycle or a six-cycle; their expected counts are \(O(n^4q_n^4+n^6q_n^6)=O(n^{-4/5})\). By Markov's inequality, with probability \(1-O(n^{-1/5})\), every component is a tree of at most six vertices. On this event, Step 2 and factorization show that \(D_n\) occurs exactly when there is no \(P_6\) component.

Let \(Y_n\) count all (not necessarily isolated) alternating six-vertex paths, with the orientation fixed by starting at their unique object-side endpoint. Each path uses three distinct object vertices, three distinct attribute vertices, and five missing edges. Thus
\[
\mu_n:=\mathbb E Y_n=(n)_3(m_n)_3q_n^5=\alpha^3t^5+O_{\alpha,t}(n^{-1}).
\]
Here \((r)_3=r(r-1)(r-2)\). Two path indicators are independent if they share no missing-edge variables. For two different paths sharing \(h\) edges, \(1\le h\le4\), their common-edge graph is a forest on at least \(h+1\) vertices. The number of ordered pairs of embeddings of this overlap type is therefore \(O_{\alpha}(n^{11-h})\); the probability that both paths occur is at most \(q_n^{10-h}\). The standard dependency-graph Stein–Chen inequality bounds the total-variation distance from \(\operatorname{Pois}(\mu_n)\) by a constant times the sums of products of indicator probabilities and joint probabilities over dependent pairs. The latter is bounded by
\[
\sum_{h=1}^{4}O_\alpha(n^{11-h}q_n^{10-h})=O_{\alpha,t}(n^{-1/5}),
\]
while the former is of smaller order. Consequently \(Y_n\) is within \(O(n^{-1/5})\) in total variation of \(\operatorname{Pois}(\alpha^3t^5)\). Outside the exceptional graph event above, every six-vertex path is exactly one \(P_6\) component. Therefore \(\Pr(D_n)=\Pr(Y_n=0)+O(n^{-1/5})\), proving the critical assertion, including total-variation convergence for the count of \(P_6\) components.

**4. Either side of the transition.** If \(q_n=o(n^{-6/5})\), the expected number of six-vertex paths is \(O(n^6q_n^5)=o(1)\). The expected numbers of seven-vertex trees and four- and six-cycles also vanish. The component classification then implies \(\Pr(D_n)\to1\).

Suppose instead that \(n^{6/5}q_n\to\infty\) and \(nq_n\to0\). The path count has \(\mu_n\asymp n^6q_n^5\to\infty\). Using the same overlap classification, its variance satisfies
\[
\frac{\operatorname{Var}Y_n}{\mu_n^2}
\le O_\alpha\!\left(\frac1{\mu_n}+\sum_{h=1}^4\frac1{n^{h+1}q_n^h}\right)=o(1).
\]
Hence \(Y_n/\mu_n\to1\) in probability. Each counted path has at most \(O_\alpha(n)\) possible extra missing edges touching one of its six vertices, so the expected number of counted paths that are not isolated components is \(O_\alpha(\mu_n n q_n)=o(\mu_n)\). Markov's inequality shows that at least one counted path is an isolated \(P_6\) component with probability tending to one. Its nondistributive concept-lattice factor forces \(D_n\) to fail. This proves the supercritical assertion.

## Verification
Execute `python3 verify.py` in a directory containing this document and the standalone program. The program enumerates every labelled tree with at most six vertices via Prüfer words, checks closure extents and the lattice identity directly, checks all \(512\) possible three-object/three-attribute missing-incidence matrices, and verifies the direct-product phenomenon on a nontrivial example. Its expected final line is `VERIFY_OK`. Among the \(512\) matrices, exactly \(36\) with five missing edges and exactly \(6\) with six missing edges yield nondistributive concept lattices; the former \(36\) are precisely the six-vertex paths.

These are exhaustive checks of the stated finite classification and examples, not computations proving the probabilistic limits. The infinite asymptotic claims follow from the explicit combinatorial bounds and the standard Stein–Chen inequality used above.

## Relationship to prior work
The Bernoulli coin-toss model for formal contexts is discussed by Felde, Hanika, and Stumme (2020), and Sakurai (2021) studies expectations of concept counts in random formal contexts. Neither cited source claims this first distributivity threshold. The six-vertex \(N_5\) reduced-context example is already displayed in Abdulla, Hille, Dürrschnabel, and Stumme (2025, Figure 1(b)); no priority is claimed for the pentagon construction itself or for Birkhoff's forbidden-sublattice criterion. The classical small-subgraph Poisson mechanism is also standard; the claimed new element is its sharp application to concept-lattice distributivity using the complete first-obstruction classification and graph-product reduction. Accessible published research records were additionally searched for equivalent formulations, without discovering a dominating theorem; a previously published equivalent reformulation remains possible.

## Limitations
The result concerns the first extremely sparse non-incidence transition. It does not say that nondistributivity persists at every larger missing-edge probability: adding non-incidences can change a concept lattice nonmonotonically. The proof assumes independent incidence choices and fixed positive asymptotic aspect ratio. The supplied checks exhaust only finite graph sizes needed for the stated first-obstruction classification. Originality is based on the cited accessible literature and research-record comparisons, not an exhaustive theorem database or independent publication-priority certification. Independent external validation has not been performed.

## References
1. M. Felde, T. Hanika, G. Stumme, *Null Models for Formal Contexts*, Information 11 (2020), article 135, published 2020-02-28, DOI: https://doi.org/10.3390/info11030135.
2. T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023 (initial public version 2021-01-26), https://arxiv.org/pdf/2101.11023.
3. M. Abdulla, T. Hille, D. Dürrschnabel, G. Stumme, *Rises for Measuring Local Distributivity in Lattices*, arXiv:2506.23168 (2025-06-29), especially Figure 1(b) and Section 6, https://arxiv.org/pdf/2506.23168.
4. G. Birkhoff, *Lattice Theory*, third edition, American Mathematical Society, 1967 (the forbidden-\(M_3,N_5\) characterization).
5. R. Arratia, L. Goldstein, L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability 17 (1989), 9–25.
6. S. Janson, T. Łuczak, A. Ruciński, *Random Graphs*, Wiley (2000), standard sparse subgraph-count methodology.
