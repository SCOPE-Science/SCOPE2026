# A sharp rooted colour-refinement dichotomy for Cartesian products of strongly regular graphs

## Finding

Let \(d\ge1\). Let \(X_1,\ldots,X_d\) be connected noncomplete strongly regular simple graphs with **the same** parameters \((v,k,\lambda,\mu)\). Thus every vertex has \(k\) neighbours, two adjacent vertices have \(\lambda\) common neighbours, and two nonadjacent vertices have \(\mu\) common neighbours. In particular, \(\mu>0\), \(0<k<v-1\), and every factor has diameter two. Let \(G=X_1\square\cdots\square X_d\) and choose any root \(o=(o_1,\ldots,o_d)\). At round zero colour \(o\) uniquely, and give all other vertices the same colour. Apply synchronous one-dimensional counting colour refinement, preserving previous colours in each refinement signature.

For any vertex \(x\), let \((a,b,c)\) record the numbers of coordinates at respective distances \(0,1,2\) from the corresponding root coordinate; thus \(a+b+c=d\). Set \(s=b+2c\), the distance from \(o\) in \(G\). Then the **least stable refinement round** (the least \(t\) for which rounds \(t\) and \(t+1\) induce the same partition) is exactly

\[
\boxed{t=2d-1}.
\]

There is an exact dichotomy.

**Hamming-parameter regime:** If \(\mu=2\) and \(k=2\lambda+2\), the stable colours are precisely the \(2d+1\) sets specified by \(s=0,1,\ldots,2d\). Writing \(q=1+k/2\), the class at distance \(s\) contains exactly \(\binom{2d}{s}(q-1)^s\) vertices.

**Other parameters:** If \(\mu\ne2\) or \(k\ne2\lambda+2\), the stable colours are precisely the \(\binom{d+2}{2}\) classes indexed by \((a,b,c)\) with \(a+b+c=d\). The class indexed by \((a,b,c)\) contains exactly

\[
\boxed{\frac{d!}{a!b!c!}\,k^b(v-k-1)^c}
\]

vertices. In both regimes the entire refinement trace, including colour-class multiplicities at each round (up to canonical relabelling), is determined solely by the common strongly regular parameters and \(d\); it does not depend on the factor isomorphism types or the choice of roots.

## Assumptions and scope

The theorem concerns finite, undirected, loopless, connected, **noncomplete** strongly regular factors sharing an identical quadruple \((v,k,\lambda,\mu)\). It includes factors that are nonisomorphic to each other, and does not require vertex transitivity. The Cartesian product changes exactly one coordinate along an edge. The root has its own round-zero colour, whereas every nonroot vertex shares one colour. The stated refinement round counts transitions from this round-zero partition. The theorem makes no claim that its classes are automorphism orbits, nor does it assert graph identification by colour refinement.

## Proof

**1. The equitable coordinate-profile quotient.** Fix \(x\) of profile \((a,b,c)\). The local distance partition about any root of a strongly regular factor has the following neighbour counts: distance-zero vertices send \(k\) edges to distance one; distance-one vertices send \(1,\lambda,k-\lambda-1\) edges to distance zero, one, two; and distance-two vertices send \(0,\mu,k-\mu\) edges to distance zero, one, two. These values are root-independent by strong regularity. In \(G\), the profile-transition multiplicities are therefore

\[
\begin{array}{c|c}
\text{new profile}&\text{number of neighbours}\\ \hline
(a-1,b+1,c)&ka\\
(a+1,b-1,c)&b\\
(a,b-1,c+1)&(k-\lambda-1)b\\
(a,b+1,c-1)&\mu c\\
(a,b,c)&\lambda b+(k-\mu)c.
\end{array}
\]

Terms with impossible target profiles are omitted. The last row counts neighbours that keep the profile, not loops. Thus each profile is an equitable cell, so refinement can never split a fixed profile. This same transition system and each profile's size \(\frac{d!}{a!b!c!}k^b(v-k-1)^c\) depend only on \((v,k,\lambda,\mu,d)\), proving parameter-independence of the entire refinement trace.

**2. Propagation from a single root.** The Cartesian distance is \(s=b+2c\). For a profile in distance shell \(L_s\), the numbers of neighbours in shells \(L_{s-1},L_s,L_{s+1}\), respectively, are

\[
B_s=b+\mu c,\qquad A_s=\lambda b+(k-\mu)c,\qquad F_s=ka+(k-\lambda-1)b.
\]

Every shell \(L_s\), \(0\le s\le2d\), is nonempty: each coordinate can have distance zero, one or two. By induction on the refinement round \(t\), vertices at distance \(>t\) all have the same colour (their rooted radius-\(t\) neighbourhoods cannot see the root, and the ambient graph is \(dk\)-regular). Also, by round \(t\) distinct shells \(L_0,\ldots,L_t\) have disjoint colour sets, and their colours differ from the common far-region colour: at the next round a vertex in \(L_{t+1}\) has at least one neighbour in the already distinguished \(L_t\), while vertices farther out have none. This proves the shell separation used below. In particular, at round \(2d-2\) shells \(L_{2d-1}\) and \(L_{2d}\) still share a colour, so stabilization is impossible earlier than \(2d-1\).

**3. The Hamming-parameter regime.** Suppose \(\mu=2\) and \(k=2\lambda+2\). Then

\[
B_s=s,\qquad A_s=\lambda s,\qquad F_s=\frac{k}{2}(2d-s),
\]

which depend only on \(s\). Consequently the distance partition is equitable and cannot be split by refinement, while Step 2 separates all the distance shells by round \(2d-1\). This establishes exactly \(2d+1\) stable classes and the sharp round bound. The standard strongly regular parameter identity \((v-k-1)\mu=k(k-\lambda-1)\) gives \(v-k-1=k^2/4\). Hence each factor's distance enumerator is

\[
1+kz+(v-k-1)z^2=\bigl(1+(k/2)z\bigr)^2,
\]

and the Cartesian product's distance enumerator is its \(d\)-th power. Taking the coefficient of \(z^s\) gives \(\binom{2d}{s}(k/2)^s\).

**4. The other parameter regime when \(\mu\ne2\).** At round \(s\), vertices in shell \(L_s\) can be distinguished by the total number of neighbours in \(L_{s-1}\), because \(L_{s-1}\) is already separated from all other shells at round \(s-1\). That total is

\[
B_s=b+\mu c=s+(\mu-2)c.
\]

For fixed \(s\), this distinguishes all feasible values of \(c\), and then \(b=s-2c\) and \(a=d-b-c\) are forced. Every profile in \(L_s\) is consequently a distinct class no later than round \(s\), for \(1\le s\le2d-1\). The last shell \(L_{2d}\) has the unique profile \((0,0,d)\). Therefore all profiles are separated by round \(2d-1\).

**5. The other parameter regime when \(\mu=2\) but \(k\ne2\lambda+2\).** We first show by induction that every shell \(L_s\) is monochromatic at round \(s\) (for \(1\le s\le2d\)). It is monochromatic together with all more distant vertices at round \(s-1\); its neighbours in \(L_{s-1}\) all carry a common colour at that round by the induction hypothesis, and its number of such neighbours is \(B_s=s\). All remaining neighbours are still in the common far region. Thus it is monochromatic at round \(s\), but its colour differs from colours in other shells.

At round \(s+1\), a vertex of \(L_s\) counts neighbours of the dedicated round-\(s\) colour of \(L_s\). Their number is

\[
A_s=\lambda s+(k-2\lambda-2)c.
\]

The coefficient of \(c\) is nonzero, so all feasible profiles within \(L_s\) are separated by round \(s+1\). Shells \(L_{2d-1}\) and \(L_{2d}\) each have only one profile, and all shells with possibly multiple profiles have \(s\le2d-2\). Hence every profile is distinguished by round \(2d-1\).

In all cases Step 1 prevents over-refinement, Steps 3–5 establish the stated final partitions, and Step 2 gives sharpness. This completes the proof.

## Verification

A standalone Python 3 program, `verify.py`, constructs actual strongly regular graphs, checks their parameters, forms their Cartesian products, and performs uncompressed synchronous counting colour refinement on every vertex. It compares the actual stable partition with the theorem's distance/profile classification, its predicted class sizes, and the exact least stable round. It uses no external packages. Running `python3 verify.py` on the supplied code produced `CASES 20 ALL_TESTS_PASS`; the sample spans C4, rook graphs of sizes \(3\times3\) and \(4\times4\), the Shrikhande graph, Petersen graph, triangular graph, Clebsch graph, and mixed nonisomorphic Shrikhande/rook factors. These are finite checks independent of the symbolic proof; they do not prove the universal quantifiers.

## Relationship to prior work

The colour-refinement algorithm and equitable partitions are standard (Kersting–Mladenov–Garnett–Grohe, 2014). Strongly regular graphs, Hamming products and Doob graphs have long-standing descriptions; in particular, the fact that Shrikhande products can share intersection arrays with Hamming graphs is not asserted as new (Bespalov–Krotov, 2015, and older references). Kiefer–McKay (2020) investigate extremal iteration numbers on general graphs, not the exact one-rooted rounds of every strongly regular Cartesian product. Cai–Guo–Gavrilyuk–Ponomarenko (2024) investigate **higher-dimensional** Weisfeiler–Leman coherent configurations and Cartesian prime decomposition, rather than the ordinary rooted one-dimensional refinement trace and its exceptional intersection-parameter threshold. The assertion here is the sharp classification and trace-invariance for all common-parameter strongly regular factors, including the two qualitatively different stable partitions; it is not a claim to have discovered the underlying graph products, their distance arrays, or the colour-refinement algorithm.

## Limitations

No new result on graph-isomorphism recognition, automorphism-orbit exactness, general products with unequal strongly regular parameters, directed graphs, disconnected or complete factors, or higher-dimensional Weisfeiler–Leman is claimed. Different strongly regular graphs sharing parameters may have different automorphism orbits inside the same stable class. The literature comparison cannot exclude an equivalent unindexed statement; current work on Cartesian coherent configurations is a particularly relevant area for further expert scrutiny. Computed tests cover finite examples only. Independent scientific audit has not been performed.

## References

1. S. Klavžar, *Characterizing subgraphs of Hamming graphs*, Journal of Graph Theory 49 (2005), 302–312. First available online 8 April 2005. https://doi.org/10.1002/jgt.20084
2. K. Kersting, M. Mladenov, R. Garnett, M. Grohe, *Power Iterated Color Refinement*, AAAI (2014), 1904–1910. Published 21 June 2014. https://doi.org/10.1609/aaai.v28i1.8992
3. E. Bespalov, D. Krotov, *MDS codes in the Doob graphs*, arXiv:1512.03361, 10 December 2015. https://arxiv.org/abs/1512.03361
4. S. Kiefer, B. D. McKay, *The Iteration Number of Colour Refinement*, ICALP (2020). https://arxiv.org/abs/2005.10182
5. J. Cai, J. Guo, A. L. Gavrilyuk, I. Ponomarenko, *Cartesian products of graphs and their coherent configurations*, arXiv:2411.02689 (2024). https://arxiv.org/abs/2411.02689
