# Five vertices are sharp for satisfaction loss under profitable Schelling swaps

## Finding
Consider a simple connected undirected graph with one agent at each vertex, at least two agents of each of two types, and no vacancies. An agent's *utility* is the fraction of her neighbors who share her type; agents of opposite types may exchange locations only when **each moving agent's own utility strictly increases**. Separately, call an agent *satisfied* when her utility is at least \(1/2\), and let \(H\) be the number of satisfied agents.

**Theorem.** A profitable exchange can strictly decrease \(H\) for the first time on a graph with **five vertices**. Among the \(21\) isomorphism classes of connected simple graphs on five vertices, precisely **two** admit such an exchange. They have, respectively, six and seven edges; hence the sparsest five-vertex witness is unique up to graph isomorphism.

A labeled six-edge witness has vertex set \(\{0,1,2,3,4\}\) and edge set
\[
\{\{0,1\},\{1,3\},\{1,4\},\{2,3\},\{2,4\},\{3,4\}\}.
\]
Initially agents at vertices \(0,3\) have type A and agents at \(1,2,4\) have type B. Exchange the agents at vertices \(0\) and \(4\). The two movers' utilities strictly rise, while the number of satisfied agents drops from \(2\) to \(1\). The sum of *all* agents' utilities actually rises from \(3/2\) to \(2\). For this witness, the satisfaction loss persists for every evaluation threshold \(\tau\in(1/3,1/2]\), even though moves are always governed by strict improvement of the untruncated utility fraction.

## Assumptions and scope
For every finite simple connected \(G=(V,E)\) with \(n=|V|\), let \(c:V\to\{\mathrm A,\mathrm B\}\) be a coloring with at least two vertices of each color. Every vertex has positive degree. Define
\[
u_c(v)=\frac{|\{w\in N(v):c(w)=c(v)\}|}{\deg(v)},\qquad
H_\tau(c)=|\{v\in V:u_c(v)\ge\tau\}|.
\]
A swap of the **agents** at distinct differently colored vertices \(i,j\), producing \(c'\), is profitable exactly when \(u_{c'}(j)>u_c(i)\) and \(u_{c'}(i)>u_c(j)\). The degree denominators on the two sides may be different. We study \(H_{1/2}(c')<H_{1/2}(c)\); the threshold is an external aggregate evaluation rule, **not** a truncated individual utility or a requirement that both movers be initially unhappy.

The five-vertex *topology classification* is among all connected simple graphs, without restrictions on degree other than positivity. Only existence and its sharp minimum are claimed, not a classification at larger orders.

## Proof
**Explicit witness.** In vertex order \(0,1,2,3,4\), exact utilities before the exchange are
\[
(0,\;1/3,\;1/2,\;0,\;2/3),
\]
and afterwards are
\[
(1,\;1/3,\;0,\;1/3,\;1/3).
\]
The A-agent moves from vertex \(0\) to vertex \(4\), changing utility from \(0\) to \(1/3\). The B-agent moves from vertex \(4\) to vertex \(0\), changing utility from \(2/3\) to \(1\). The positions meeting the threshold \(1/2\) change from \(\{2,4\}\) to \(\{0\}\). Summing those two utility vectors yields \(3/2\) and \(2\). The threshold robustness interval follows directly from the same vectors.

**Sharpness and classification certificate.** The attached self-contained `verify.py` performs a complete exact enumeration. For each order \(n\in\{2,3,4,5\}\), it visits every one of the \(2^{\binom n2}\) labeled simple graph edge masks, rejects disconnected masks by breadth/depth-first graph reachability, and assigns each connected graph an isomorphism-canonical edge mask by minimizing over all \(n!\) vertex permutations. For one representative of each graph class it visits every binary coloring with both color classes of size at least two, and every unordered pair of different-colored vertices. With integers \(a_v\) counting same-type neighbors and positive degrees \(d_v\), the exact profitability inequalities are
\[
a'_j d_i>a_i d_j,\qquad a'_i d_j>a_j d_i,
\]
and satisfaction at a vertex is checked exactly by \(2a_v\ge d_v\). Thus no floating-point comparisons or random sampling enter the classification.

The exhaustive output is: \(1,2,6,21\) connected graph isomorphism classes at orders \(2,3,4,5\), with respectively \(0,0,0,2\) classes exhibiting satisfaction loss. The two positive classes at order five have six and seven edges; the code verifies their canonical masks against two explicit edge sets, rather than inferring the class count from a graph-database lookup. A second way of counting verifies \(1,4,38,728\) labeled connected graphs at the four orders. For \(n<4\), the two-types/two-per-type constraint is empty. Exhaustion of the six classes at \(n=4\), followed by the explicit witness at \(n=5\), proves the sharp minimum. Exhaustion of the \(21\) classes at \(n=5\) proves the claimed two-topology classification.

## Verification
Place this document alongside `verify.py` and execute `python3 verify.py` using standard Python 3. The program uses only `itertools` and `fractions`; it asserts the exact utilities, both agents' improvement inequalities, the two aggregate outcomes, the labeled and unlabeled connected-graph counts, and the complete five-vertex classification. On successful execution it ends with `PASS: all checks exact and exhaustive for connected graphs of order at most five.` An independent enumeration against a separate graph-atlas library was also used to cross-check the count and degrees of the two five-vertex topology classes; the package's primary certificate does not depend on that library.

## Relationship to prior work
Zhang's 2011 paper (first online February 7, 2011) studies tipping in a Schelling-type spatial game with a different preference function. Chauhan, Lenzner, and Molitor (2018) study tolerance-truncated individual incentives and social costs expressed via discontent, for which a mover already above the tolerance threshold may have no incentive to improve her fraction further. The present **fraction-maximizing** incentives instead agree with the 2019 swap-game formulation of Agarwal, Elkind, Gan, and Voudouris, who study equilibrium existence, total utility, and integration rather than the precise one-exchange five-vertex threshold for the half-satisfied headcount. Echzell and collaborators (2019) prove convergence claims under a threshold-truncated objective; convergence of a potential does not imply that a thresholded satisfaction headcount improves after *every* move. Bilò and collaborators (2022) investigate graph topology, potential changes, and equilibrium welfare, including counts of zero-utility agents, but their cited statements do not supply this exact half-threshold headcount classification. The full-text comparisons covered definitions, principal relevant results, and related-work sections; they do not constitute a guarantee against an equivalent result in unexamined literature.

## Limitations
The theorem is about exactly two types, full occupancy, connected undirected simple graphs, binary threshold evaluation at \(1/2\), and individually profitable **untruncated** fraction-maximizing swaps. It does not establish nonmonotonicity of a particular stochastic trajectory or long-run welfare, nor does it claim that the same threshold holds for other tolerance conventions or any different mobility rule. It does not classify orders above five. Because the result is a complete finite enumeration rather than a closed-form infinite classification, correctness depends on inspectable exhaustive enumeration and its exact finite coverage. Novelty remains subject to independent bibliographic assessment; independent scientific audit has not been performed.

## References
1. J. Zhang, “Tipping and residential segregation: A unified Schelling model,” *Journal of Regional Science* **51** (2011), 167–193, first online 2011-02-07. DOI: 10.1111/j.1467-9787.2010.00671.x.
2. A. Chauhan, P. Lenzner, L. Molitor, “Schelling Segregation with Strategic Agents” (2018), arXiv:1806.08713. https://arxiv.org/pdf/1806.08713
3. A. Agarwal, E. Elkind, J. Gan, A. A. Voudouris, “Swap Stability in Schelling Games on Graphs” (2019), arXiv:1909.02421. https://arxiv.org/pdf/1909.02421
4. H. Echzell, T. Friedrich, P. Lenzner, L. Molitor, M. Pappik, F. Schöne, F. Sommer, D. Stangl, “Convergence and Hardness of Strategic Schelling Segregation” (2019), arXiv:1907.07513. https://arxiv.org/pdf/1907.07513
5. D. Bilò, V. Bilò, P. Lenzner, L. Molitor, “Topological Influence and Locality in Swap Schelling Games” (2022), DOI: 10.1007/s10458-022-09573-7.
