# Sharp eight-vertex onset of transmissibility-dependent optimal vaccination on contact trees

## Finding

**Theorem (sharp tree threshold and exact first switch).** Let \(T\) be any finite tree on \(n\ge2\) vertices. Vaccinate one vertex \(v\) by deleting it before infection; choose the initial infected individual uniformly from the remaining \(n-1\) vertices. Independently declare every remaining contact edge transmissible with probability \(p\in(0,1)\), and define the outbreak as the entire connected component of the chosen seed in the resulting open-edge forest. Write \(M_v(p)\) for its expected number of infected vertices. A *parameter-independent optimal vaccinee* is one vertex minimizing \(M_v(p)\) simultaneously for every \(p\in(0,1)\).

1. Every tree on \(2\le n\le7\) vertices has a parameter-independent optimal vaccinee. This is an exact finite theorem, certified for every labeled tree by the exhaustive program supplied here.
2. A tree on eight vertices need not have one. Specifically, the three-arm spider with arm lengths \((1,1,5)\) has center \(0\), pendant leaves \(1,2\), and the long arm \(0-3-4-5-6-7\). There is a unique \(\alpha\in(0,1)\) with \(\alpha^3+\alpha^2=1\) (approximately \(0.7548776662\)). The unique optimum is vertex \(0\) when \(0<p<\alpha\), vertex \(3\) when \(\alpha<p<1\), and precisely \(\{0,3\}\) tie at \(p=\alpha\).
3. For **every** \(n\ge8\), the spider with arms \((1,1,n-3)\) changes its set of optimal vaccination vertices as \(p\) increases: its center is uniquely optimal for all sufficiently small positive \(p\), but is not optimal for all sufficiently large \(p<1\). Consequently the bound of seven is sharp for all orders.

No corresponding assertion is made for contact graphs with cycles, more than one vaccinated vertex, heterogeneous transmission, or continuous-time infection/recovery dynamics.

## Assumptions and scope

All graphs are finite, simple, undirected trees. A successful edge transmits with probability \(p\), independently of all other edges. The vertex deleted as vaccinee cannot be selected as seed or infected. The initial seed is uniform **after** deletion, and its probability law does not depend on the vaccinee. Outbreak size counts the seed. This is an independent-bond (Reed–Frost-type) epidemic model; it is not an assertion about a generic continuous-time SIR model with correlated outgoing transmissions.

For each vaccinee \(v\), define the *residual susceptibility polynomial*
\[
 S_v(p)=\sum_{\substack{\{a,b\}\subseteq V(T)\setminus\{v\}\\ a\leftrightarrow b\text{ in }T-v}}p^{d_T(a,b)},
\]
where the sum is over unordered distinct residual vertices connected in \(T-v\), and \(d_T(a,b)\) is their unique original tree-path length. Isolated vertices contribute nothing. The integer coefficients count connected pairs by distance.

## Proof

**1. Exact objective.** Condition on the uniform seed \(s\). A residual vertex \(t\ne s\) is in its outbreak exactly if every edge along the unique \(s\)-to-\(t\) path is open. The connection probability is \(p^{d_T(s,t)}\) when \(s,t\) lie in the same component of \(T-v\), and zero otherwise. Summing first over vertices and then over seeds yields
\[
 M_v(p)=\frac1{n-1}\sum_{s\ne v}\left(1+\sum_{t\ne s,v}\Pr(s\leftrightarrow t)\right)
 =1+\frac{2}{n-1}S_v(p).
\]
Thus the vaccinees minimizing expected outbreak size are exactly those minimizing \(S_v\).

**2. Exhaustive finite lower bound, all parameters.** For each integer \(n\in\{2,3,4,5,6,7\}\), the program `verify_vaccination.py` ranges over **all** \(n^{n-2}\) Prüfer words, hence bijectively over every labeled tree on \(\{0,\ldots,n-1\}\). Its independent breadth-first search counts the integer distance coefficients of every \(S_v\). For any such tree, it finds a vertex \(w\) for which every difference \(S_u(p)-S_w(p)\), for all \(u\), has nonnegative Bernstein coefficients of degree five.

Here is the precise exact certificate. For a polynomial \(Q(p)=\sum_{r=0}^5c_rp^r\), the coefficient \(\beta_j\) in the Bernstein expansion
\[
 Q(p)=\sum_{j=0}^5\beta_j\binom5j p^j(1-p)^{5-j}
\]
satisfies
\[
 5!\,\beta_j=\sum_{r=0}^{j}c_r\binom jr r!(5-r)!,\qquad j=0,1,\ldots,5.
\]
The right side is an integer, and the program checks it is nonnegative for every vertex comparison. Because all Bernstein basis functions are nonnegative on \([0,1]\), the inequalities hold for the **whole continuum** \(0\le p\le1\), not merely sampled parameters. The tested Prüfer-word counts are respectively \(1,3,16,125,1296,16807\), summing to \(18248\), with no failed tree. Since deletion leaves at most \(n-1\) vertices, every pair distance in the residual forest is at most \(n-2\le5\), so degree-five Bernstein conversion is exact. Prüfer's bijection and the supplied program make this a complete, reproducible finite proof of assertion 1.

**3. Eight-vertex exact optimizer.** For the spider in assertion 2, direct connected-pair distance counting gives the following polynomials (the notation on the left denotes the vertex vaccinated):
\[
\begin{array}{ll}
 S_0=4p+3p^2+2p^3+p^4,&S_3=5p+3p^2+p^3,\\
 S_1=S_2=6p+5p^2+4p^3+3p^4+2p^5+p^6,&S_4=5p+4p^2,\\
 S_5=5p+4p^2+2p^3,&S_6=5p+5p^2+3p^3+2p^4,\\
 S_7=6p+6p^2+4p^3+3p^4+2p^5.&
\end{array}
\]
For every \(p\in(0,1)\), each \(S_v-S_3\) for \(v\in\{1,2,4,5,6,7\}\) is strictly positive: all are polynomials with nonnegative power coefficients except \(S_4-S_3=p^2(1-p)>0\); and each of the other differences has strictly positive power coefficients. Therefore only vaccinees \(0\) and \(3\) can minimize. Their difference is
\[
 S_3(p)-S_0(p)=p(1-p^2-p^3).
\]
The polynomial \(p^2+p^3\) is strictly increasing from zero to two on \([0,1]\), so its level-one equation has exactly one solution \(\alpha\) there. The sign of the displayed difference proves all claimed optimality intervals and the unique tie.

**4. Reversal for all larger orders.** Let \(n\ge8\) and take the three-arm spider \(T_n\) with center \(c\), two single-edge arms and a long arm of length \(n-3\). For any tree, the coefficient of \(p\) in \(S_v(p)\) is precisely the number of edges remaining after deleting \(v\), namely \(n-1-\deg_T(v)\). The center has degree three and every other vertex degree at most two; thus \(S_v(p)-S_c(p)\) has a strictly positive linear coefficient for every \(v\ne c\). Since there are finitely many competitors, continuity of these finitely many polynomials gives a common neighborhood to the right of zero in which \(c\) is **uniquely** optimal.

At \(p=1\), the susceptibility polynomial counts all unordered pairs connected after the deletion. Deleting \(c\) leaves components of sizes \(1,1,n-3\), whereas deleting \(b\), the long-arm vertex adjacent to \(c\), leaves components of sizes \(3,n-4\). Consequently
\[
 S_c(1)=\binom{n-3}{2},\quad
 S_b(1)=\binom32+\binom{n-4}{2},\quad
 S_c(1)-S_b(1)=n-7>0.
\]
Continuity therefore makes \(b\) strictly preferable to \(c\) on a neighborhood to the left of one. The center cannot remain optimal throughout \((0,1)\). This proves assertion 3 and sharpness.

## Verification

Run `python3 verify_vaccination.py` using the accompanying standalone Python 3 file. It requires only the Python standard library. The actual execution returned:

`VERIFY_OK labeled_trees=18248 all_p_Bernstein_certificates=YES eight_vertex_profiles=8 exact_outbreak_enumerations=32 spider_endpoint_identity=YES`

The program enumerates all Prüfer words up to order seven; uses only exact integer arithmetic for the Bernstein certificates; verifies all eight distance-profile polynomials; and independently enumerates surviving-edge configurations at four rational \(p\)-values for all eight possible vaccinees (32 distinct exact expectation comparisons). It also checks the spider endpoint-count identity for lengths five through 49. The unlimited-order spider assertion is proved in section 4, **not** inferred from this bounded final loop or from numeric sampling.

## Relationship to prior work

Newman's 2002 preprint gives foundational epidemic/percolation connections; pair connectivity and susceptibility are established tools, and this proof does not claim novelty for that starting identity. Chen and colleagues (2006) study fragmentation and pair-connectivity quantities after node removal, principally in random and scale-free networks. Holme (2004) investigates practical local vaccination strategies; its complete preprint was not accessible for inspection. Holme (2017) explicitly compares influence, vaccination, and sentinel objectives with exact small-graph results. In particular, it discusses why high-degree nodes matter at low infection rates and fragmentation matters at high rates. Those **qualitative ideas are prior work**.

The contribution asserted here is narrower and specific: for the **independent-edge model on all finite trees**, the sharp seven-versus-eight threshold for the existence of a single universally optimal vaccinee, together with an explicit eight-vertex optimizer transition and a construction for all higher orders. Holme's inspected exact results instead use a continuous-time infection/recovery SIR process and classify differences among three epidemiological objectives; its statements do not imply the present tree-only all-parameter cutoff. Chen and colleagues' fragmentation functional determines an endpoint but not the all-parameter optimum. Searches for equivalent distance-polynomial, pair-connectivity, and node-deletion formulations found no directly covering result, but the possibility of an unindexed stronger theorem remains.

## Limitations

The theorem treats one deleted contact vertex, independent identically distributed edge transmission, a fixed tree, and one uniformly selected susceptible seed after intervention. Real contact networks often contain cycles, heterogeneous infectiousness, transmission correlations and multiple introductions. The result is a structural statement about expected final outbreak size, not about epidemic timing, stochastic extinction of reinfecting epidemics, or risk-adjusted clinical decisions. The finite cutoff uses a reproducible exhaustive integer certificate rather than a short case-free classification. Originality rests on literature searches and comparison with accessible full texts; no independently audited priority claim is made. An inaccessible potentially relevant 2004 paper is specifically acknowledged above.

## References

1. M. E. J. Newman, “The spread of epidemic disease on networks,” arXiv:cond-mat/0205009v1 (first posted 2002-04-30), https://arxiv.org/pdf/cond-mat/0205009.
2. Y. Chen, G. Paul, R. Cohen, S. Havlin, S. P. Borgatti, F. Liljeros and H. E. Stanley, “Percolation theory applied to measures of fragmentation in social networks,” arXiv:cond-mat/0610625v1 (2006), https://arxiv.org/pdf/cond-mat/0610625.
3. P. Holme, “Efficient local strategies for vaccination and network attack,” arXiv:q-bio/0403021 (2004); abstract available, complete preprint unavailable, https://arxiv.org/abs/q-bio/0403021.
4. P. Holme, “Three faces of node importance in network epidemiology: Exact results for small graphs,” arXiv:1708.06456 (2017), https://arxiv.org/pdf/1708.06456.
5. A. Bucur and P. Holme, “Beyond ranking nodes: Predicting epidemic outbreak sizes by network centralities,” arXiv:1909.10021 (2019), https://arxiv.org/pdf/1909.10021.
