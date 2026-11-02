# A sharp vaccination switch on two-cycle contact networks

## Finding

Consider two disjoint simple cycles of the same length \(r\geq3\), with distinguished vertices \(a\) and \(b\), and one additional vertex \(h\) joined to \(a\) and \(b\), but no other cross-cycle edges. Thus the undirected contact network has \(2r+1\) vertices. Before an outbreak, permanently vaccinate exactly one vertex \(v\), deleting it and its incident edges. Choose one initially infected vertex uniformly from the remaining \(2r\) vertices. Run homogeneous Reed–Frost epidemic transmission: each newly infectious vertex independently infects each susceptible neighbor with probability \(q\in(0,1]\) once, then becomes recovered. Let \(E_r(v;q)\) be the expected total number ever infected, including the seed.

Define the connection-score difference
\[
D_r(q)=-q-\sum_{j=2}^{r-1}(j-1)q^j+\left(\binom r2+2\right)q^r-(r-1)q^{r+1}.
\]
There is exactly one \(q_r\in(0,1)\) satisfying \(D_r(q_r)=0\). The **complete optimal single-vertex vaccination classification** is:

- If \(0<q<q_r\), precisely the two cycle-to-bridge portals \(a,b\) minimize expected outbreak size.
- If \(q=q_r\), precisely \(a,b,h\) tie for the minimum.
- If \(q_r<q\leq1\), the degree-two intermediary \(h\) is the unique minimizer.

Every other vertex is strictly inferior to the portals at every \(q>0\). Moreover the switch has the sharp large-cycle scaling
\[
\boxed{\lim_{r\to\infty}r^3(1-q_r)=6.}
\]
At certain transmission, the sharp expected-size advantage of vaccinating the intermediary instead of a portal is \(1/r\):
\[
E_r(h;1)=r,\qquad E_r(a;1)=E_r(b;1)=r+1/r.
\]

## Assumptions and scope

The graph consists of two vertex-disjoint, unweighted, length-\(r\) cycles and the length-two connecting path \(a-h-b\). There is exactly one perfectly effective vaccination before seed selection; the seed is uniform among all unvaccinated vertices. Every edge transmission is independently sampled with the same probability \(q\), as in the Reed–Frost/independent-cascade model. The observable is the expected **number of ever-infected people**, not mortality, peak simultaneous prevalence, or outbreak probability above a different cutoff. All statements quantify over every integer \(r\geq3\) and all real \(0<q\leq1\). At the excluded degenerate value \(q=0\), every vaccination leaves only the seed infected, so all choices tie.

## Proof

**1. Epidemic-to-connectivity identity.** In the Reed–Frost process with one seed, its final infected set has the distribution of the seed's connected component when every residual edge is independently retained with probability \(q\). This is the standard deferred-decision coupling for the independent-cascade process. For any residual graph with exactly \(2r\) vertices, set
\[
S_v(q)=\sum_{\{x,y\}\subset V\setminus\{v\}}\Pr_q(x\leftrightarrow y\text{ after deleting }v).
\]
Counting ordered pairs in the component of a uniformly chosen seed yields, without an approximation,
\[
E_r(v;q)=1+\frac{S_v(q)}r.\tag{1}
\]

**2. Cycle and path connection sums.** On a simple \(r\)-cycle, the two edge-disjoint connecting arcs between two distinct vertices have lengths \(j\) and \(r-j\). Hence their probability of connection is exactly \(q^j+q^{r-j}-q^r\). Summing over unordered pairs gives
\[
C_r(q)=r\sum_{j=1}^{r-1}q^j-\binom r2q^r.\tag{2}
\]
For the path on \(r-1\) vertices, the corresponding score is
\[
P_{r-1}(q)=\sum_{j=1}^{r-2}(r-1-j)q^j.\tag{3}
\]
The total connection probability from a specified cycle vertex to all cycle vertices, including itself, is
\[
R_r(q)=1+2\sum_{j=1}^{r-1}q^j-(r-1)q^r.\tag{4}
\]
All these are exact finite polynomials valid at the endpoint \(q=1\).

**3. Scores of the only candidates.** Deleting the intermediary \(h\) leaves two disjoint cycles, so
\[
S_h(q)=2C_r(q).\tag{5}
\]
Deleting portal \(a\) leaves an isolated path of \(r-1\) vertices and the other cycle with a pendant vertex \(h\). The pendant edge is open with probability \(q\), independently of the other cycle edges, hence
\[
S_a(q)=S_b(q)=P_{r-1}(q)+C_r(q)+qR_r(q).\tag{6}
\]
Expanding (2)–(6) gives exactly \(S_a-S_h=D_r(q)\), the displayed polynomial. By (1), \(E_r(a;q)-E_r(h;q)=D_r(q)/r\).

**4. No other vaccination can be optimal.** Delete any nonportal vertex of the left cycle. The residual left-cycle vertices form a path on \(r-1\) vertices; this path is joined to \(h\) by the surviving edge from portal \(a\). After a relabeling of just the left path, this residual graph is the graph obtained by deleting \(a\), with *one additional edge* joining that path to \(h\). The same argument applies symmetrically to a nonportal right-cycle vertex. Couple independent edge states in the common subgraph and sample the additional edge independently. Connectivity of each pair can only increase, and it increases strictly for some cross-component pair with positive probability for every \(q>0\) (at \(q=1\), surely). Thus \(S_v(q)>S_a(q)\) for every nonportal \(v\); by (1) these vaccinations are strictly worse.

**5. Exactly one crossover in the physical interval.** The polynomial \(D_r(q)/q\) has coefficients with the sign pattern: a nonempty consecutive negative block, one positive coefficient \(\binom r2+2\), then the negative coefficient \(-(r-1)\). It therefore has at most two positive real roots, counted with multiplicity, by Descartes' rule. Direct substitution gives \(D_r(q)/q\to-1\) as \(q\downarrow0\), \(D_r(1)=1\), and \(D_r(q)\to-\infty\) as \(q\to+\infty\). Consequently there is a positive root strictly between zero and one and another strictly above one. Descartes' rule excludes any further positive roots, proving uniqueness and the strict signs claimed in the classification.

**6. Sharp cubic crossover scale.** Differentiating the displayed polynomial and summing the powers at \(q=1\) gives
\[
D_r'(1)=\frac{r(r^2-3r+8)}6.
\]
The explicit coefficients also give \(\sup_{0\leq q\leq1}|D_r''(q)|=O(r^4)\): the sum of second-derivative magnitudes is bounded by a constant times \(\sum_{j\leq r}j^3+r^4\). For every fixed \(c>0\), Taylor's theorem therefore gives
\[
D_r(1-c/r^3)=1-\frac c6+O_c(1/r).
\]
For every fixed \(\eta\in(0,6)\), the right side is positive at \(c=6-\eta\) and negative at \(c=6+\eta\) for all sufficiently large \(r\). Since the physical root is unique, it is trapped between these two points; letting \(\eta\downarrow0\) proves the stated limit.

## Verification

The standalone program `verification/check.py` independently enumerates all open/closed edge patterns of each post-vaccination graph for \(r=3,4,5\) and the exact rational probabilities \(q=1/3,1/2,3/4,1\). It computes the connected-component pair count directly from graph edges, independently of the polynomial derivation; compares all portals and the intermediary to (2)–(6); and verifies strict inferiority of every nonportal. It also checks signs across numerically determined crossover roots and the approach to the cubic scaling. Run with `python3 verification/check.py` from the package root; only Python's standard library is required. These finite checks are corroboration; the proof above, not enumeration, establishes the assertion for all \(r\) and real \(q\).

## Relationship to prior work

Li, Zhao, and Zhang (2022) study SIR vaccination through a site–bond percolation model and average epidemic size under random-network vaccination; their accessible abstract establishes the broader epidemiological motivation but does not certify absence of an exact finite-graph targeted result, as their complete article was not accessible for comparison. Becchetti et al. (2022) rigorously state and explain the standard Reed–Frost/bond-percolation correspondence and study long-range random small-world graphs, rather than the exact optimal single-vertex vaccination on this deterministic two-cycle family. Chatterjee and Zehmakan (2023) compare centrality-based vaccination heuristics under a *different*, degree-normalized network SIR transition law; their results cannot be transferred to the present probability law. The contribution assessed here is the explicit optimal-vertex switch polynomial, uniqueness in the physical interval, and the \(r^{-3}\) crossover boundary, not the classical percolation correspondence.

## Limitations

No statement is made for heterogeneous edge transmissibilities, imperfect vaccines, multiple vaccinations or seeds, nonuniform seeding, other connector lengths, non-Reed–Frost infectious-period distributions, or mortality-weighted objectives. In particular, for a general SIR process with correlated outgoing transmission events, simple undirected independent bond percolation can be inapplicable. Priority remains subject to the unavailable full text of Li–Zhao–Zhang (2022) and any unidentified specialized finite-network vaccination treatment. No independent external mathematical audit is claimed.

## References

1. S. Li, X. Zhao, and R. Zhang, *Site-bond percolation model of epidemic spreading with vaccination in complex networks*, Journal of Mathematical Biology 85, 49 (2022), first public version verified 2022-10-12, https://doi.org/10.1007/s00285-022-01816-1.
2. L. Becchetti, A. Clementi, F. Pasquale, L. Trevisan, and I. Ziccardi, *Bond Percolation in Small-World Graphs with Power-Law Distribution*, arXiv:2205.08774 (first public version 2022-05-18), https://arxiv.org/abs/2205.08774, especially Section 1 and Appendix A.
3. S. Chatterjee and A. N. Zehmakan, *Effective Vaccination Strategies in Network-based SIR Model*, arXiv:2305.16458 (first public version 2023-05-25), https://arxiv.org/abs/2305.16458, especially Sections III, IV, VI and VII.
4. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, Physical Review E 76, 036113 (2007), https://doi.org/10.1103/PhysRevE.76.036113, distinguishing independent-bond and correlated-infectious-period processes.
