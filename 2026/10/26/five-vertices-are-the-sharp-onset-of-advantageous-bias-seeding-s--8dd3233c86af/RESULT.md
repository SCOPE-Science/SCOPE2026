# Five vertices are the sharp onset of advantageous-bias seeding switches

## Finding

Consider the death–birth biased voter process on a connected, finite, simple undirected graph with at least two vertices. In one step a uniformly random vertex copies a neighbor, chosen proportionally to fitness \(r>1\) for mutants and \(1\) for residents. A seed consists of exactly two initially mutant vertices, and its value is the probability of eventual all-mutant fixation.

**Sharp minimum order.** On every such graph with \(2\le |V|\le4\), a single two-vertex seed set maximizes fixation probability for **all** \(r>1\); hence no optimal-seed identity is forced to switch with positive advantage. This bound is sharp. On the five-vertex graph \(K_{2,3}\), write \(H,S,L\) for the three seed-orbit types, with mutant counts \((2,0)\), \((1,1)\), and \((0,2)\) in the parts of sizes \(2,3\). There is exactly one \(r_\star>1\) at which the optimum changes:

\[
\begin{array}{ll}
1<r<r_\star:&H\text{ is uniquely optimal up to automorphisms};\\
r=r_\star:&H\text{ and }S\text{ tie for the optimum};\\
r>r_\star:&S\text{ is uniquely optimal up to automorphisms}.
\end{array}
\]

The third orbit \(L\) is strictly inferior to both \(H\) and \(S\) for every \(r>0\). The threshold \(r_\star=2.05144026631733\ldots\) is the **unique positive root** of
\[
P(r)=48r^7+290r^6+365r^5-856r^4-2239r^3-1600r^2-460r-48.
\]

The minimality statement is for strictly advantageous bias \(r>1\) and two-seed optimization on connected undirected simple graphs. It does not claim that the same optimal pair persists when \(r<1\).

## Assumptions and scope

Let \(2\le |V|<\infty\). For a state \(X\subseteq V\), define \(f_X(v)=r\) if \(v\in X\), and \(f_X(v)=1\) otherwise. Select \(u\) uniformly from \(V\), select \(v\in N(u)\) with probability \(f_X(v)/\sum_{w\in N(u)}f_X(w)\), and replace the type at \(u\) by that at \(v\). The absorbing states are \(\varnothing\) and \(V\). For each fixed \(r>0\), there is a positive-probability path of at most \(|V|-1\) updates from every nonempty mixed state to \(V\): repeatedly copy a mutant across a cut edge. Finiteness gives a positive lower bound on the probability of absorption within that many steps, uniformly over mixed states, so absorption occurs almost surely. Its all-mutant fixation probability from \(X\) is \(F_X(r)\). The optimization domain is the family of all \(X\) with \(|X|=2\); a graph of order one has no feasible seed.

In \(K_{2,3}\), vertices within each part are symmetric; write \(F_{i,j}(r)\) for \(i\) mutants in the two-vertex part and \(j\) in the three-vertex part. The graph has five vertices and six edges.

## Proof

**1. Exact lumped equations.** For \((i,j)\) other than the two absorbing states, the non-self transition probabilities on \(K_{2,3}\) are
\[
\begin{aligned}
q_{i+}&=\frac{2-i}{5}\frac{rj}{rj+3-j},
&q_{i-}&=\frac{i}{5}\frac{3-j}{rj+3-j},\\
q_{j+}&=\frac{3-j}{5}\frac{ri}{ri+2-i},
&q_{j-}&=\frac{j}{5}\frac{2-i}{ri+2-i}.
\end{aligned}
\]
The fixation probabilities solve the finite first-step equations \(\sum_\delta q_\delta(F_{\mathrm{current}}-F_{\mathrm{next}})=0\), with \(F_{0,0}=0\) and \(F_{2,3}=1\). The transient linear system is nonsingular since absorption occurs almost surely. Exact elimination gives, with
\[
Q(r)=8r^6+53r^5+113r^4+102r^3+113r^2+53r+8,
\]
\[
F_{2,0}(r)=\frac{72r^7+535r^6+1340r^5+1341r^4+794r^3+330r^2+80r+8}{10(r+1)Q(r)},
\]
\[
F_{1,1}(r)=\frac{r(3r+2)(4r+1)(8r^4+51r^3+92r^2+27r+2)}{12(r+1)Q(r)},
\]
\[
F_{0,2}(r)=\frac{r^2(20r^5+143r^4+335r^3+278r^2+107r+17)}{3(r+1)Q(r)}.
\]
These expressions can be checked symbolically in the ten-transient-state lumped system and cross-checked in the full binary-state system at exact rational fitness values.

**2. Exact optimization.** Subtraction yields
\[
F_{2,0}(r)-F_{1,1}(r)=\frac{-P(r)}{60(r+1)Q(r)}.
\]
Further,
\[
F_{1,1}(r)-F_{0,2}(r)=\frac{r(16r^6+128r^5+341r^4+326r^3+77r^2+8r+4)}{12(r+1)Q(r)}>0
\]
and
\[
F_{2,0}(r)-F_{0,2}(r)=\frac{16r^7+175r^6+670r^5+1243r^4+1312r^3+820r^2+240r+24}{30(r+1)Q(r)}>0.
\]
Every displayed denominator is positive for \(r>0\). In descending powers, \(P\) has one sign change; Descartes' rule implies at most one positive root, counted with multiplicity. Because \(P(1)=-4500<0\) and \(P(3)=259464>0\), the root exists and lies strictly between \(1\) and \(3\). These inequalities and absence of other positive roots imply the sign of \(-P\) on each side of the root. Together with the two strict dominances this proves the phase diagram.

**3. Sharp minimality.** Up to isomorphism, the connected graphs with three vertices are the three-vertex path and triangle. The six connected graphs with four vertices are the star, four-vertex path, paw, four-cycle, diamond (complete graph minus one edge), and complete graph. For every graph in this list an explicit seed pair maximizes fixation for all \(r>1\), as follows. Vertices are numbered from zero, and the edge lists and seed pairs are encoded in `verify.py`. For the three-vertex path, choose the center and a leaf; for the triangle, any pair; for the four-vertex star, its center and a leaf; for the four-vertex path, its two internal vertices; for the paw, the triangle's degree-three vertex and a degree-two vertex; for the four-cycle, an edge; for the diamond, its two degree-three vertices; and for the complete graph, any pair.

To verify the last finite assertion, enumerate all binary configurations for each representative graph; write its exact absorbing-chain linear system and solve over \(\mathbb Q(r)\). For each asserted maximizing pair, subtract the fixation rational function of every competing pair. Either the gap is identically zero or the reduced rational numerator and denominator, after substituting \(r=1+z\), have nonnegative coefficients and at least one positive coefficient each. Thus each nonzero gap is strictly positive for every \(z>0\). The accompanying program performs and asserts each exact symbolic computation for all eight classes of orders three and four; \(K_2\) has only one two-vertex seed set, already fully mutant. This exhausts the connected simple graphs of orders two through four and proves sharpness.

## Verification

The unchanged companion program `verify.py` can be run with Python 3 and SymPy. It checks the exact \(K_{2,3}\) rational identities and denominator positivity, counts roots of \(P\) above one, and proves all optimization comparisons for orders three and four by coefficient certificates over \(\mathbb Q\). An unlumped 32-configuration chain on \(K_{2,3}\) is solved at the exact rational biases \(r=2\) and \(r=3\) to cross-check the lumped values. Numerical root approximation is informational; the polynomial and Descartes argument are the exact result.

## Relationship to prior work

Durocher, Karras, Pavlogiannis and Tkadlec (2022), *Invasion Dynamics in the Biased Voter Process*, define this death–birth biased-voter rule and study fixation-maximizing initial seed sets. They establish general monotonicity/submodularity for advantageous bias and give a seven-node illustration of bias-dependent seed performance. Their neutral-bias formula and strong-bias adjacency criterion imply existence of some crossover on \(K_{2,3}\) by continuity; this weaker existence claim is not asserted as new. Those principles do not give the exact threshold, three-orbit ranking, or sharp minimum order. A later indexed record [4] gives the same \(K_{2,3}\) formulas and ranking, but does not give the exclusion of all smaller graphs.

Zhang, Wu, Liu and Yang (2012), *Fixation Probabilities on Complete Star and Bipartite Digraphs*, is relevant literature on bipartite populations. Comparing any fixation formula requires matching the update rule as well as the graph: selecting a parent first by fitness and then choosing a replacement is generally a different chain from the death-first rule used here.

## Limitations

This theorem is about the first possible **change of an optimal pair as advantageous fitness varies**, not all fitness regimes, directed or weighted networks, more than two initial mutants, or an enumeration of higher-order graphs. The comparisons do not establish publication priority against other specialized work.

## References

1. L. Durocher, P. Karras, A. Pavlogiannis, J. Tkadlec, *Invasion Dynamics in the Biased Voter Process*, arXiv:2201.08207v2; IJCAI 2022, DOI: 10.24963/ijcai.2022/38. https://arxiv.org/html/2201.08207v2
2. C. Zhang, Y. Wu, W. Liu, X. Yang, *Fixation Probabilities on Complete Star and Bipartite Digraphs*, Discrete Dynamics in Nature and Society (2012), Article 940465. DOI: 10.1155/2012/940465. https://onlinelibrary.wiley.com/doi/10.1155/2012/940465
3. J. Tkadlec, A. Pavlogiannis and collaborators, *Limits on amplifiers of natural selection under death-Birth updating*, 2020, https://pmc.ncbi.nlm.nih.gov/articles/PMC6968837/ (background comparison of update conventions).
4. *A sharp fitness crossover in two-seed invasion on a five-vertex graph*, Resultary 2026/11/8. https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-a-sharp-fitness-crossover-in-two-seed-invasion-on-a-five-vertex--b10b122c6ac9/RESULT.md
