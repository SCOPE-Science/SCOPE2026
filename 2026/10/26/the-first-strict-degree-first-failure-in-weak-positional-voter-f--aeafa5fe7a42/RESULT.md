# The first strict degree-first failure in weak positional voter fixation on trees has nine vertices

## Finding
For the single-site positional voter model on an unweighted, connected, loopless tree, let \(F_T(u,\delta)\) be the probability of eventual all-mutant fixation when the initial mutant is placed uniformly among all vertices, only vertex \(u\) is receptive to the invasion advantage \(\delta\ge0\), and all other sites update neutrally. Define the weak-benefit score \(b_T(u)=\partial_\delta F_T(u,0)\).

**Sharp theorem.** For every tree \(T\) on \(2\le |V(T)|\le8\) vertices, at least one vertex of maximum degree maximizes \(b_T\). There exists a nine-vertex tree whose *unique* maximum-degree vertex does not maximize \(b_T\). Consequently, nine is the smallest tree order admitting a strict failure of every degree-maximizing one-site choice. This is a weak-selection claim, not a claim that every degree-maximizing choice is optimal after arbitrary tie-breaking.

For the tree on labeled vertices \(0,1,\ldots,8\) with edges

\[
\{(0,5),(0,7),(1,0),(1,2),(1,3),(1,4),(5,6),(7,8)\},
\]

vertex \(1\) is the unique maximum-degree vertex, with degree \(4\), whereas vertex \(0\) has degree \(3\) and is the unique optimum of the weak-benefit score. Exactly,

\[
 b_T(0)=\frac{256096}{2909163},\qquad
 b_T(1)=\frac{481465}{5818326},\qquad
 b_T(0)-b_T(1)=\frac{30727}{5818326}>0.
\]

All other vertices have strictly smaller scores than vertex \(0\). Since the fixation probabilities depend analytically on \(\delta\) near zero, there exists \(\delta_0>0\) such that vertex \(0\) is also the unique fixation-maximizing one-site placement for every \(0<\delta<\delta_0\).

## Assumptions and scope
The graph is a finite, simple, unweighted, undirected, connected tree with at least two vertices and no self-loops. One vertex, uniformly random among all vertices, initially has opinion or mutant type \(A\); all others have type \(B\). At each discrete step one uniformly random vertex updates by copying a neighbor. At the designated receptive site \(u\), neighbors of type \(A\) have sampling weight \(1+\delta\) and neighbors of type \(B\) have weight \(1\); all other update sites use uniform neighbor sampling. Both monochromatic states absorb. Selection is *weak* in the precise derivative sense stated above; finite positive advantage is asserted only in an unspecified sufficiently small interval for the nine-vertex witness.

A strict degree-first failure means that some vertex of lower degree has strictly larger weak-benefit score than **every** vertex of maximum degree; it does not mean that every possible maximum-degree tie-breaking rule fails on smaller trees.

## Proof
Let \(n=|V(T)|\), let \(m=n-1\) be its edge count, and let \(d_i\) denote the degree of vertex \(i\). For distinct vertices \(i,j\), define \(\psi_{ij}=\psi_{ji}\) by \(\psi_{ii}=0\) and the finite rational linear system

\[
 2\psi_{ij}=1+\frac1{d_i}\sum_{z\sim i}\psi_{zj}
                  +\frac1{d_j}\sum_{z\sim j}\psi_{iz}.
\]

The unique solution is positive off the diagonal: it is the expected meeting time of two independent neighbor-copying random walks whose individual jump rates are one. Uniqueness follows because the embedded pair walk on a finite connected graph eventually coalesces almost surely.

The weak-selection coefficient is

\[
 \boxed{\displaystyle b_T(u)=\frac{1}{n m d_u}
 \sum_{\{i,j\}\subseteq N(u)}\psi_{ij}.}
\]

For completeness, the formula can be obtained without assuming the desired rankings. In the neutral voter process, the degree-weighted mutant mass divided by \(2m\) is the fixation-probability martingale. At a biased update at \(u\), when the mutant-neighbor fraction is \(p\), the probability of copying \(A\) changes from \(p\) to \((1+\delta)p/(1+\delta p)\); its derivative at zero is \(p(1-p)\). First-order perturbation of the finite absorbing Markov chain sums this expected drift along the neutral process. In the dual coalescing-walk representation, for distinct starting sites \(i,j\), the probability of different current types averaged over one uniformly random initial mutant is \(2/n\) times the probability their dual lineages have not yet coalesced. The sum of these probabilities over original discrete steps equals \(n\psi_{ij}\), since an outstanding pair makes a move with probability \(2/n\) per step. Writing \(p(1-p)\) as the sum of neighboring unordered type disagreements divided by \(d_u^2\) yields the boxed formula. This is a specialization of the earlier general weak-selection coalescence method, not a new method.

To prove the lower bound on tree order, enumerate every Prüfer word of length \(n-2\) over the alphabet \(\{0,\ldots,n-1\}\), for each \(2\le n\le8\). The Prüfer bijection supplies *all* labeled trees. Collapse duplicate isomorphism classes using the canonical balanced-parenthesis string obtained by recursively sorting rooted children at the tree center(s). The resulting class counts for \(n=2,3,4,5,6,7,8\) are respectively \(1,1,2,3,6,11,23\). For each canonical representative, solve the preceding rational coalescence system exactly and compare all \(b_T(u)\). In every class some maximum-degree vertex attains the maximum score. This is an exhaustive finite certificate, not a sample; the complete standard-library verifier is supplied as `verify.py`.

For the displayed nine-vertex tree, the same exact linear solve gives the fractions in the Finding section. Its leaf vertices have score zero, vertices \(5\) and \(7\) have score \(1196615/34909956\), vertex \(1\) has the score shown above, and vertex \(0\) exceeds all of them. Thus the nine-vertex upper bound and the eight-vertex lower bound match. Analyticity of the finite absorption-probability linear system near \(\delta=0\) turns the strict derivative inequalities into strict small-positive-\(\delta\) inequalities for this fixed tree.

## Verification
Run `python verify.py` with Python 3 and no third-party packages. The program enumerates all \(n^{n-2}\) Prüfer words for each tree order \(2\) through \(8\), canonicalizes every resulting tree, checks the unlabeled counts, builds the rational pair-meeting system, verifies its solution by substitution, and tests the degree-optimality inequality exactly. It then computes the nine-vertex witness scores and checks strict optimality of vertex \(0\). Successful completion prints `ALL EXACT CHECKS PASSED`. No Monte Carlo simulations or floating-point comparisons are used for the proof certificate.

## Relationship to prior work
Petsinis, Pavlogiannis, and Karras (first preprint November 26, 2022; AAAI 2023) introduced the positional voter model, derived the general weak-selection coefficient using coalescence quantities (Lemma 6 and Theorem 5), and evaluated degree-based choices empirically. Their general computational theorem is a premise here and is not claimed as new. The separately determined sharp **minimum tree order** and its fully exhaustive small-tree certificate are not stated by that work. Allen and coauthors (2021) developed coalescent weak-selection methods in a different graph-update setting; Brendborg and coauthors (2022) study site-dependent advantage for the distinct positional Moran process. Neither inspected work reports this particular positional-voter tree-order boundary.

## Limitations
The result gives a sharp finite obstruction to a degree-first *weak-bias* heuristic, not a guarantee about substantial bias, multiple receptive vertices, weighted or directed graphs, graphs with loops, or other updating rules. It does not establish optimality of all degree-tied vertices on smaller trees. A published general weak-selection formula already enables evaluation of any fixed graph, so mathematical novelty here is the exhaustive sharp structural cutoff and concrete exact obstruction, not the coalescence formula itself. Numerical impact on large real networks is not asserted. Independent scientific review remains outstanding.

## References
1. P. Petsinis, A. Pavlogiannis, and P. Karras, *Maximizing the Probability of Fixation in the Positional Voter Model*, arXiv:2211.14676 (first submitted 2022-11-26), AAAI 2023, DOI:10.1609/aaai.v37i10.26446. Full text: https://arxiv.org/abs/2211.14676.
2. B. Allen et al., *Fixation probabilities in graph-structured populations under weak selection*, PLOS Computational Biology 17 (2021), e1008695, DOI:10.1371/journal.pcbi.1008695. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC7880501/.
3. J. Brendborg et al., *Fixation Maximization in the Positional Moran Process*, arXiv:2201.02248 (2022). Full text: https://arxiv.org/abs/2201.02248.
