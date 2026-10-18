# Eight patches are sharp for survival-dependent shifts in optimal habitat protection

## Finding
Let \(T\) be a finite, undirected, unweighted tree of \(n\) equal habitat patches. Every patch independently remains usable with common probability \(p\in(0,1)\). After the random losses, write \(K_1,\ldots,K_s\) for the connected components of the surviving induced subgraph, and take \(C=\sum_{i=1}^s |K_i|^2\), the number of ordered mutually connected surviving patch pairs (including identical endpoints). An intervention makes one chosen vertex survive with certainty without changing other patches. The optimal intervention maximizes \(\mathbb E[C]\).

**Sharp minimum and complete first exceptional layer.** Every tree with at most seven vertices has at least one vertex that is an optimal intervention for *all* \(p\in(0,1)\). Among the 23 nonisomorphic unlabelled eight-vertex trees, exactly two lack such a universal optimal vertex. For the first exceptional tree with edge list `[(1,0),(1,2),(0,5),(2,3),(2,4),(5,6),(6,7)]`, vertex 2 alone is optimal for \(0<p<p_A\), vertex 1 alone for \(p_A<p<1\), and both at \(p_A\), where \(p_A\) is the unique root in \((0,1)\) of \(p_A^3+p_A^2=1\) (approximately \(0.7548776662\)). For the second exceptional tree with edge list `[(1,0),(1,2),(0,5),(2,3),(2,4),(5,6),(5,7)]`, precisely vertices 2 and 5 tie for optimum when \(0<p<1/\sqrt2\), and precisely vertices 0 and 1 tie when \(1/\sqrt2<p<1\); all four tie at \(p=1/\sqrt2\).

These are statements about *global* best protected patches, not merely reversals of arbitrary pairwise rankings. Thus eight is the smallest tree order at which the optimal protected site necessarily depends on the common patch survival probability.

## Assumptions and scope
The tree and its edges are fixed, and all patches have equal unit weight. Site failures are independent and identically distributed, and an intervention guarantees survival of exactly one chosen site. Connectivity uses surviving *vertices* and the fixed surviving-induced edge set; links do not fail independently. Each ordered pair of surviving sites contributes one to \(C\) if connected, and the pair with equal endpoints counts. No further survival, cost, or dispersal effects are assigned to the intervention. The result holds for every \(p\in(0,1)\), with endpoint values used only for algebraic certificates.

## Proof
**1. Exact protection gain.** Each connected ordered pair \((a,b)\) has a unique tree path \(P_{ab}\). Without protection, its probability of being connected is \(p^{d_T(a,b)+1}\), because every path vertex must survive. If vertex \(v\) is protected, the probability becomes \(p^{d_T(a,b)}\) when \(v\in P_{ab}\) and is unchanged otherwise. Define the nonnegative integer-coefficient path-through-vertex polynomial
\[
F_v(p)=\sum_{(a,b)\in V(T)^2:\,v\in P_{ab}}p^{d_T(a,b)}.
\]
The gain in expected connectivity, relative to protecting no site, is exactly
\[
\Delta_v(p)=(1-p)F_v(p).
\]
Since \(1-p>0\), every optimizer of the expected connectivity is exactly a maximizer of \(F_v(p)\). The diagonal term \((v,v)\) contributes one to \(F_v\), ensuring the normalization matches \(C\).

**2. Rigorous finite all-tree certificate.** The bundled executable enumerates all \(n^{n-2}\) Prüfer words for each \(2\le n\le8\), together with the one-vertex tree. Each labelled tree is converted into a canonical, unlabelled AHU code obtained by pruning leaves to its center(s), recursively sorting rooted branch codes, and taking the lexicographically smaller ordering of the two centered rooted halves when there are two centers. Consequently one representative from every isomorphism class is retained. The resulting class counts for orders \(1,\ldots,8\) are exactly \(1,1,1,2,3,6,11,23\).

For each representative, breadth-first search reconstructs the unique path for every ordered vertex pair and counts its contribution to every coefficient of every \(F_v\). To certify \(F_v(p)\ge F_w(p)\) for an entire interval rather than at sampled values, pad the integer-coefficient difference \(Q(p)=F_v(p)-F_w(p)\) to degree \(d=n-1\) and compute the integers
\[
b_j=\sum_{k=0}^j [p^k]Q(p)\binom{d-k}{j-k},\qquad 0\le j\le d.
\]
The exact identity
\[
(1+t)^dQ\!\left(\frac{t}{1+t}\right)=\sum_{j=0}^{d}b_jt^j
\]
proves \(Q(p)\ge0\) for all \(p\in[0,1]\) whenever every \(b_j\ge0\). No approximate sign sampling enters these dominance certificates. The verifier finds such a vertex simultaneously dominating every other vertex in all 25 shapes of order at most seven and in 21 of the 23 shapes of order eight. For the two exceptions, exact evaluation at \(p=1/2\) and \(p=9/10\) gives disjoint sets of maximizers; hence neither exceptional tree can have a universally optimal vertex. This exhausts all trees with at most eight vertices.

**3. Exact structure of the two exceptional cases.** For the first explicit tree, direct path counting yields
\[
F_2(p)-F_1(p)=2p(1-p^2-p^3).
\]
The remaining vertices are dominated throughout \(0<p<1\) by vertex 2 or vertex 1 (the certificate compares 2 against vertices 3–7 and 1 against vertex 0). The strictly decreasing expression \(1-p^2-p^3\) has exactly one zero on \((0,1)\). Neither candidate ties another vertex in that open interval except that the two candidates tie at their crossover; therefore the stated optimal choices follow.

For the second explicit tree, path counts give
\[
F_2(p)=F_5(p),\qquad F_0(p)=F_1(p),\qquad
F_2(p)-F_0(p)=2p(1-2p^2).
\]
The other four vertices are strictly below one of those candidate pairs throughout the open interval, as certified by the same coefficient test. The difference changes sign exactly at \(p=1/\sqrt2\), proving the complete optimality regimes.

## Verification
Run `python vertex_criticality_verify.py` with Python 3.9 or later and no third-party dependencies. The program computes all labelled Prüfer trees, canonically reduces to nonisomorphic shapes, constructs the path polynomials from actual edge lists, produces exact integer coefficient dominance checks, verifies the two explicit polynomial identities and exact rational winner sets, and independently enumerates all \(2^7\) survival configurations conditional on each protected vertex at two rational probabilities. Expected terminal summary:

`VERIFY_OK unlabeled_counts=1,1,1,2,3,6,11,23 exceptions=2 exact_bernstein=PASS witness_polynomials=PASS direct_state_count=PASS`

This finite enumeration is complete for \(n\le8\), and says nothing about a universal larger-order classification. Integer and rational certificates, rather than floating-point optimization or a search timeout, supply the finite exhaustive proof.

## Relationship to prior work
The connected-pair objective \(C\), and its equivalence to landscape coincidence/connected-component metrics on undirected graphs, are *existing* ecological network indices: Matisziw and Murray (2009) introduced a connectivity-change index and Saura (2010) established its equivalence to the earlier landscape coincidence probability. Minor and Urban (2008) motivated habitat-patch criticality and resistance to network disturbance. Saura and Rubio (2010) explained patch and link contributions under graph connectivity metrics. This result does **not** introduce a new deterministic connectivity measure, a new path-enumeration identity, or new conservation criteria in general. Its subject is instead the sharp smallest order and complete exceptional-shape classification for **independent stochastic site failure with one certain-protection intervention** and the exact probability-dependent globally optimal vertices. Existing edge-failure reinforcement questions change the reliability of a corridor, and do not imply this site-protection classification.

The full Minor–Urban (2008) text and the available full-text treatment of Saura (2010) were examined for mathematical coverage. The Matisziw–Murray paper is particularly relevant but only its abstract and the detailed analysis of its connectivity index in Saura (2010) could be inspected; equivalent stronger statements elsewhere cannot be excluded solely by unsuccessful literature searches.

## Limitations
The theorem is a finite tree-structure result, not a claim about arbitrary graphs, unequal patch qualities, nonidentical or correlated survival, interventions that alter edges, multiple simultaneous protections, or an empirically optimal conservation decision. The component-square metric gives equal weight to all ordered patch pairs and includes diagonal pairs; changing the metric can change the conclusion. The two thresholds belong to the explicit eight-vertex shapes, not to every landscape. The earlier literature comparison cannot constitute a proof that no equivalent unpublished or otherwise inaccessible theorem exists.

## References
1. Minor, E. S., and Urban, D. L. (2008). *A Graph-Theory Framework for Evaluating Landscape Connectivity and Conservation Planning*. Conservation Biology 22, 297–307. DOI: `10.1111/j.1523-1739.2007.00871.x` (first publicly available 31 January 2008).
2. Matisziw, T. C., and Murray, A. T. (2009). *Connectivity Change in Habitat Networks*. Landscape Ecology 24, 89–100. DOI: `10.1007/s10980-008-9282-z`.
3. Saura, S. (2010). *Measuring Connectivity in Habitat Mosaics: The Equivalence of Two Existing Network Indices and Progress Beyond Them*. Community Ecology 11, 217–222. DOI: `10.1556/ComEc.11.2010.2.10`.
4. Saura, S., and Rubio, L. (2010). *A Common Currency for the Different Ways in Which Patches and Links Can Contribute to Habitat Availability and Connectivity in the Landscape*. Ecography 33, 523–537. DOI: `10.1111/j.1600-0587.2009.05760.x`.
