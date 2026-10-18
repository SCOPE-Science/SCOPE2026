# A parity transition for optimal maximal induced-matching reconfiguration in subdivided cliques

## Finding

Let \(H_n=S(K_n)\) be the graph obtained by subdividing every edge of the complete graph on \(n\ge3\) labeled original vertices exactly once. An *induced matching* is a set of edges whose endpoints induce a disjoint union of edges; it is *inclusion-maximal* when no further graph edge can be added without destroying this property.

Write \(I_n(z)\) for the polynomial counting all induced matchings by cardinality, including the empty matching, and \(M_n(z)\) for the analogous polynomial counting inclusion-maximal induced matchings. Then

\[
I_n(z)=\sum_{k=0}^{n-1}\binom{n}{k}(n-k)^k z^k,
\qquad
M_n(z)=\sum_{k=\lceil n/2\rceil}^{n-1}\binom{n}{k}(n-k)!\left\{\begin{matrix}k\\n-k\end{matrix}\right\}z^k.
\]

Here the bracketed coefficient is a Stirling number of the second kind. With the formal coefficient conventions \(I_0(z)=I_1(z)=1\), \(M_0(z)=1\) and \(M_1(z)=0\) (the last is a series convention, not the maximal-matching count of the edgeless one-vertex graph), the exponential generating functions are

\[
\sum_{n\ge0}I_n(z)\frac{t^n}{n!}=\exp\!\bigl(t e^{zt}\bigr),
\qquad
\sum_{n\ge0}M_n(z)\frac{t^n}{n!}=\exp\!\bigl(t(e^{zt}-1)\bigr).
\]

The minimum cardinality of an inclusion-maximal induced matching is \(\mu_n=\lceil n/2\rceil\). Every cardinality between \(\mu_n\) and \(n-1\) occurs. The number of minimum such matchings equals

\[
N_{2m}=\frac{(2m)!}{m!}\quad(m\ge2),
\qquad
N_{2m+1}=\frac{(2m+1)!}{2(m-1)!}\quad(m\ge1).
\]

Define the *optimal maximal-induced-matching reconfiguration graph* \(\mathcal R_n\): its vertices are inclusion-maximal induced matchings of cardinality \(\mu_n\), and two distinct vertices are adjacent when their edge sets differ by deleting one chosen edge and inserting one previously unchosen edge. The optimal cardinality and inclusion-maximal induced-matching property must hold at both endpoints of every move. Then:

\[
\boxed{
\begin{aligned}
\mathcal R_{2m}&\cong\bigsqcup^{(2m-1)!!}Q_m &&(m\ge2),\\
\mathcal R_{2m+1}&\text{ is connected and }3(m-1)\text{-regular} &&(m\ge2),\\
\mathcal R_3&\cong3K_1.&
\end{aligned}}
\]

Here \(Q_m\) is the hypercube of dimension \(m\), and \((2m-1)!!=(2m)!/(2^m m!)\). Thus reconfiguration of minimum inclusion-maximal induced matchings has an exact parity-controlled connectivity transition for all \(n\ge4\).

## Assumptions and scope

All graphs are finite, simple, undirected. Label the original vertices of \(H_n\) by \([n]=\{1,\ldots,n\}\). For distinct original labels \(u,v\), denote by \(u\to v\) the edge from original vertex \(u\) to the unique subdivision vertex on original pair \(\{u,v\}\). The arrow is a convenient notation for an undirected edge; it does not orient the host graph. Each original graph edge yields two possible arrows, corresponding to its two subdivision halves. Reconfiguration uses **single-edge replacement**, not sequential deletion/addition through nonmaximal intermediate configurations.

## Proof

**1. Complete structural encoding.** Suppose \(\mathcal M\) is an induced matching of \(H_n\). Each chosen edge is an arrow \(u\to v\). Two arrows \(u\to v\) and \(u'\to v'\) are mutually compatible exactly when their tails are distinct, and neither tail equals the other's head. Indeed, original vertices have adjacency only to subdivision vertices of incident original edges, and distinct subdivision vertices have no mutual adjacency. Consequently, the set \(U\) of tails has distinct labels, and every head lies in \([n]\setminus U\). Conversely, for any \(U\subsetneq[n]\) and any map \(f:U\to[n]\setminus U\), the arrows \(\{u\to f(u):u\in U\}\) form an induced matching. This representation is unique. For cardinality \(k\), choosing \(U\) in \(\binom nk\) ways and \(f\) in \((n-k)^k\) ways proves the formula for \(I_n(z)\).

**2. Exact maximality criterion.** An induced matching represented by \((U,f)\) is inclusion-maximal if and only if \(f\) is onto \([n]\setminus U\). If \(f\) misses a label \(a\) in the complement, choose any \(b\) in the nonempty image of \(f\); then adjoining the compatible arrow \(a\to b\) enlarges the matching. (For the empty matching on \(n\ge3\), any edge can be added.) Conversely, if every complement label occurs as a head, no new arrow can have an unused tail: each label is either an existing tail or is a head adjacent to a chosen subdivision vertex. The required number of surjections from a \(k\)-set to an \((n-k)\)-set is \((n-k)!\left\{\begin{smallmatrix}k\\n-k\end{smallmatrix}\right\}\), giving \(M_n(z)\). Such a surjection exists precisely when \(n-k\le k\le n-1\). This proves the support and \(\mu_n\). The two exponential generating functions follow by summing over the disjoint labeled root set and tail set: each root has an arbitrary, respectively nonempty, labeled fiber.

**3. Structure of optimum matchings.** For \(n=2m\), a minimum matching has \(m\) tails and \(m\) heads, and surjectivity forces a bijection. Thus it is precisely a perfect matching on \([2m]\) with one independent orientation choice for each of its \(m\) edges. There are \((2m-1)!!2^m=(2m)!/m!\) possibilities. For \(n=2m+1\), a minimum matching has \(m+1\) tails and \(m\) heads; surjectivity forces exactly one head to have two tails, and all other heads to have one. Hence the original labels are partitioned into one 3-element block equipped with a distinguished center and \(m-1\) 2-element blocks, each equipped with a head. Counting surjections gives \(\binom{2m+1}{m+1}m!\binom{m+1}{2}=(2m+1)!/[2(m-1)!]\).

**4. Even reconfiguration.** Fix \(n=2m\). Two optimum matchings sharing \(m-1\) arrows already fix \(m-1\) disjoint unoriented label pairs. Their remaining two labels must form the last pair in either matching. Thus a single-edge swap cannot change the underlying perfect matching. Conversely, flipping the orientation of any one pair changes exactly one selected edge and preserves maximality. The \(m\) choices are independent, giving a copy of \(Q_m\) for each of the \((2m-1)!!\) perfect matchings.

**5. Odd regularity.** Fix \(n=2m+1\). Write the unique 3-block as \(\{a,b,c\}\) with arrows \(a\to c,b\to c\), and write every 2-block as one arrow \(u\to v\). If a selected 2-block arrow is removed, restoring an onto map with the same minimum number of tails allows precisely its original arrow or the reverse \(v\to u\); the latter is the unique genuinely new adjacent configuration. If one of the two 3-block arrows is removed, its former tail must remain the new tail, and it may point to the head of any of the \(m-1\) 2-blocks. Each such change moves the 3-block to that pair while the remaining two labels of the former 3-block become a 2-block. These are all permitted replacements, and they are distinct. Thus the degree is \((m-1)+2(m-1)=3(m-1)\).

**6. Odd connectivity.** First consider \(n=5\). Using labels \(0,1,2,3,4\) for this paragraph, take \(X=\{1\to0,2\to0,3\to4\}\). We exhibit valid replacement paths from \(X\) to its image under every adjacent transposition of labels. Transposition \((0\ 1)\) is realized by

\[
\begin{split}
\{1\to0,2\to0,3\to4\}&\to\{1\to0,2\to4,3\to4\}\\
&\to\{0\to1,2\to4,3\to4\}\\
&\to\{0\to1,2\to1,3\to4\}.
\end{split}
\]

Transposition \((1\ 2)\) fixes \(X\). Transposition \((2\ 3)\) is realized by

\[
\{1\to0,2\to0,3\to4\}\to
\{1\to0,2\to4,3\to4\}\to
\{1\to0,2\to4,3\to0\}.
\]

Transposition \((3\ 4)\) is the single move replacing \(3\to4\) by \(4\to3\). Every intermediate state is a surjective arrow system. Relabeling acts by automorphisms, so these paths together with the fact that adjacent transpositions generate the symmetric group prove connectivity of \(\mathcal R_5\).

For arbitrary odd \(n=2m+1\ge5\), a configuration consists of one 3-block and \(m-1\) 2-blocks. Reconfiguration restricted to the five labels of the 3-block and any chosen 2-block is a relabeled instance of \(\mathcal R_5\); keeping every other block fixed preserves feasibility and minimal cardinality. Therefore any transposition of labels lying together in the 3-block, together in a 2-block, or in the 3-block and one 2-block can be realized by a path. For labels \(p,q\) in distinct 2-blocks, select a label \(c\) from the 3-block and perform the transpositions \((p\ c)\), \((p\ q)\), \((q\ c)\) in order. At each step the transposed pair lies in the current 3-block and one 2-block; the composition exchanges \(p,q\) and restores \(c\). Hence **every** transposition of the original labels is realizable. Since the symmetric group acts transitively on all configurations of one centered 3-block and oriented 2-blocks, \(\mathcal R_n\) is connected. Finally, for \(n=3\), the three choices of the unique head each give two arrows to that head, and no one-edge replacement is feasible, yielding \(3K_1\).

## Verification

The standalone Python file `verify_induced.py` constructs every host graph from original and subdivision vertices. It uses the original graph's edge adjacency to enumerate induced matchings directly, then tests maximality by the absence of an addable host-graph edge; no structural surjection criterion is used in these decisions. It compares every coefficient with the formulas above. For every \(n=2,\ldots,9\), the same program builds the exact reconfiguration graph on minimum inclusion-maximal induced matchings and verifies the component counts, sizes, and degrees. Its recorded output in `verification_output.txt` ends with `VERIFICATION_OK n=2..9 induced_matchings_checked=342630 reconfiguration_orders=2..9`. These finite tests are supplementary; the infinite-family proof is given above.

## Relationship to prior work

Kurita, Wasa, Uno, and Arimura establish efficient general enumeration of induced matchings in graphs without four-cycles, a class containing these clique subdivisions. Their result does not specify the induced-matching counting polynomial, surjective-map characterization of *inclusion-maximal* matchings, or optimum one-edge-swap reconfiguration for this family. Basavaraju and coauthors bound the number of maximal induced matchings in arbitrary triangle-free graphs; this broad upper bound does not determine the exact family polynomial or reconfiguration components. Cao studies algorithms for maximal *induced vertex subgraphs*, a different maximality setting. Yuan and coauthors study extremal numbers of maximal induced matchings across all connected graphs, which likewise does not give the stated graph-family exact classification. The precise parity transition above requires additional structural analysis not implied by these general enumeration or extremal results.

## Limitations

The result concerns the **one-subdivision** of a complete graph and **single-edge replacement among minimum-cardinality inclusion-maximal induced matchings**. It makes no connectivity claim about reconfiguration at nonminimum cardinalities, nor about token-slide adjacency or ordinary (not induced) matchings. Search coverage cannot establish global bibliographic priority; alternative terminology such as induced edge domination or maximal independent sets of a squared line graph may conceal an equivalent published classification. Independent scientific validation has not been performed.

## References

1. K. Kurita, K. Wasa, T. Uno, H. Arimura, *Efficient Enumeration of Induced Matchings in a Graph without Cycles with Length Four*, arXiv:1707.02740 (first public version, 10 July 2017). https://arxiv.org/abs/1707.02740
2. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei, Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180 (2013). https://arxiv.org/abs/1312.5180
3. Y. Cao, *Enumerating Maximal Induced Subgraphs*, arXiv:2004.09885 (2020). https://arxiv.org/abs/2004.09885
4. B.-J. Yuan, Z.-Y. Yang, L. Zheng, S.-C. Gong, *Maximal and maximum induced matchings in connected graphs*, arXiv:2410.11288 (first public version 15 October 2024). https://arxiv.org/abs/2410.11288
