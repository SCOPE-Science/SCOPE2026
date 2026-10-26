# Five vertices are the sharp onset of advantageous-bias seeding switches

## Finding

Consider the death–birth biased voter process on a connected, finite, simple undirected graph. In one step a uniformly random vertex copies a neighbor, chosen proportionally to fitness \(r>1\) for mutants and \(1\) for residents. A seed consists of exactly two initially mutant vertices, and its value is the probability of eventual all-mutant fixation.

**Sharp minimum order.** On every connected graph with at most four vertices, some single two-vertex seed set maximizes fixation probability for **all** \(r>1\); hence no optimal-seed identity is forced to switch with positive advantage. This bound is sharp. On the five-vertex graph \(K_{2,3}\), write \(H,S,L\) for the three seed-orbit types, with mutant counts \((2,0)\), \((1,1)\), and \((0,2)\) in the parts of sizes \(2,3\). There is exactly one \(r_\star>1\) at which the optimum changes:

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

The minimality statement is for strictly advantageous bias \(r>1\), connected undirected simple graphs, and two-seed optimization. It does not claim that the same optimal pair persists when \(r<1\).

## Assumptions and scope

For a state \(X\subseteq V\), define \(f_X(v)=r\) if \(v\in X\), and \(f_X(v)=1\) otherwise. Select \(u\) uniformly from \(V\), select \(v\in N(u)\) with probability \(f_X(v)/\sum_{w\in N(u)}f_X(w)\), and replace the type at \(u\) by that at \(v\). The process has absorbing states \(\varnothing\) and \(V\), reached almost surely on connected graphs for every \(r>0\). Its all-mutant fixation probability from \(X\) is \(F_X(r)\). The optimization domain is the family of all \(X\) with \(|X|=2\).

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
These expressions are verified symbolically in the ten-state lumped system, and cross-checked in the full binary-state system at two exact rational fitness values by the accompanying program.

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
Every displayed denominator is positive for \(r>0\). In descending powers, \(P\) has one sign change; Descartes' rule implies at most one positive root, counted with multiplicity. Because \(P(1)=-4500<0\) and \(P(3)=259464>0\), the root exists and lies strictly between \(1\) and \(3\). These inequalities, together with the two strict dominances, prove the complete phase diagram.

**3. Sharp minimality.** Up to isomorphism, the connected graphs with three vertices are the three-vertex path and triangle. The six connected graphs with four vertices are the star, four-vertex path, paw, four-cycle, diamond (complete graph minus one edge), and complete graph. For every graph in this list an explicit seed pair maximizes fixation for all \(r>1\), as follows. Vertices are numbered from zero, and the edge lists and seed pairs are encoded in `verify.py`. For the three-vertex path, choose the center and a leaf; for the triangle, any pair; for the four-vertex star, its center and a leaf; for the four-vertex path, its two internal vertices; for the paw, the triangle's degree-three vertex and a degree-two vertex; for the four-cycle, an edge; for the diamond, its two degree-three vertices; and for the complete graph, any pair.

To verify the last finite assertion rigorously, enumerate all binary configurations for each representative graph; write its exact absorbing-chain linear system and solve over \(\mathbb Q(r)\). For each asserted maximizing pair, subtract the fixation rational function of every competing pair. Either the gap is identically zero or the reduced rational numerator and denominator, after substituting \(r=1+z\), have nonnegative coefficients and at least one positive coefficient. Thus each nonzero gap is strictly positive for every \(z>0\). The accompanying standalone program performs and asserts each exact symbolic computation for all eight nontrivial isomorphism classes; \(K_2\) has only one two-vertex seed set, already fully mutant. This exhausts all connected simple graphs of order at most four and proves sharpness.

## Verification

Run `python verify.py` with Python 3 and SymPy. The script checks the exact \(K_{2,3}\) rational identities and denominator positivity, counts the positive roots of \(P\), and proves all four-or-fewer-vertex optimality comparisons by coefficient certificates over \(\mathbb Q\). An independent 32-configuration (unlumped) transition system on \(K_{2,3}\) is solved at the exact rational biases \(r=2\) and \(r=3\) to cross-check the three lumped values. The verification completed successfully. Numerical root approximation is informational; the polynomial and Descartes argument are the exact result.

## Relationship to prior work

Durocher, Karras, Pavlogiannis and Tkadlec (2022), *Invasion Dynamics in the Biased Voter Process*, define precisely this death–birth biased-voter rule and study fixation-maximizing initial seed sets. They establish general monotonicity/submodularity for advantageous bias and provide a seven-node illustration of bias-dependent seed performance. Their general neutral-bias formula and strong-bias adjacency criterion help motivate the present question, but neither gives the exact \(K_{2,3}\) threshold, complete three-orbit ranking for all \(r>1\), or the sharp minimum vertex count. General existence of some crossover on \(K_{2,3}\) can already be inferred from those endpoint principles; that weaker existence claim is **not** asserted as new.

Zhang, Wu, Liu and Yang (2012), *Fixation Probabilities on Complete Star and Bipartite Digraphs*, investigate complete bipartite populations (including \(K_{2,3}\)) using a **birth-first, death-second** fitness-proportional reproduction mechanism and study averaged seed-placement probabilities. Their recursion is not the death-first, neighbor-fitness-weighted rule used here, and their results therefore do not imply the displayed rational functions or threshold. Both sources were inspected in accessible full HTML, including definitions, methods, results and relevant appendices/sections.

## Limitations

This theorem is about the first possible **change of an optimal pair as advantageous fitness varies**, not all fitness regimes, directed/weighted networks, more than two initial mutants, or higher-order graphs. The eight small isomorphism classes are exhaustive only through order four. An alternative presentation of the same five-vertex calculation in specialized earlier death–birth literature cannot be excluded by a finite literature search; priority should be independently checked before publication.

## References

1. L. Durocher, P. Karras, A. Pavlogiannis, J. Tkadlec, *Invasion Dynamics in the Biased Voter Process*, arXiv:2201.08207v1 (first posted 2022-01-20), revised 2022-05-02; IJCAI 2022, DOI: 10.24963/ijcai.2022/38. https://arxiv.org/html/2201.08207v2
2. C. Zhang, Y. Wu, W. Liu, X. Yang, *Fixation Probabilities on Complete Star and Bipartite Digraphs*, Discrete Dynamics in Nature and Society (2012), Article 940465. DOI: 10.1155/2012/940465. https://onlinelibrary.wiley.com/doi/10.1155/2012/940465
3. J. Tkadlec, A. Pavlogiannis and collaborators, *Limits on amplifiers of natural selection under death-Birth updating*, 2020, https://pmc.ncbi.nlm.nih.gov/articles/PMC6968837/ (background comparison of update conventions).
