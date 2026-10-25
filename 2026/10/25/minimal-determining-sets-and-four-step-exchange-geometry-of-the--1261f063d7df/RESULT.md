# Minimal determining sets and four-step exchange geometry of the five-regular Clebsch graph

## Finding
Let \(G\) be the five-regular Clebsch (Greenwood–Gleason, folded five-cube) graph with vertices \(\mathbb F_2^4\), where distinct vertices \(x,y\) are adjacent exactly when \(x+y\in\{e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}\). A *determining set* is a vertex set with trivial pointwise stabilizer in \(\operatorname{Aut}(G)\); *inclusion-minimal* means no proper subset is determining.

The determining number is \(\operatorname{Det}(G)=4\). Its full family of inclusion-minimal determining sets consists of exactly \(560\) four-sets and \(192\) five-sets, with no other cardinalities:

- All \(480\) four-sets inducing exactly one graph edge.
- All \(80\) independent four-sets whose four vertex labels have nonzero vector sum in \(\mathbb F_2^4\).
- All \(192\) five-sets inducing a five-cycle.

Each of these three families is one automorphism orbit. Define the *minimum-set exchange graph* \(X\) on the \(560\) determining four-sets, where two sets are adjacent if their intersection has size three. Then \(X\) has \(5920\) edges, is connected, and every vertex has eccentricity four. In particular,
\[\operatorname{rad}(X)=\operatorname{diam}(X)=4.\]
The \(480\) one-edge bases have exchange degree \(20\), and the \(80\) independent bases have exchange degree \(28\). Their breadth-first-search distance layer profiles, respectively, are
\[(1,20,126,244,169)\quad\text{and}\quad(1,28,126,220,185).\]
Since the inclusion-minimal determining sets have two different sizes, the determining-set family does not satisfy the matroid basis-exchange axiom, despite connectedness of its minimum-set exchange graph.

## Assumptions and scope
The graph has exactly sixteen vertices and forty edges. In some conventions, *Clebsch graph* denotes the complementary ten-regular graph; this theorem concerns only the explicitly defined **five-regular** graph. The determining-set stabilizer fixes each selected vertex individually, not merely setwise. A legal exchange may replace a selected vertex by **any** unselected vertex; adjacency between the removed and added graph vertices is not required. No assertions are made about other dimensions of folded hypercubes.

## Proof
Write \(d_1=e_1,\ldots,d_4=e_4\) and \(d_5=e_1+e_2+e_3+e_4\). They are five distinct nonzero vectors with sum zero, and every nonzero vector in \(\mathbb F_2^4\) has a **unique** expression as a sum of one or two of these five vectors. Thus the five neighbors of vertex zero are \(d_1,\ldots,d_5\), and each other nonzero vertex corresponds to a unique pair of these neighbors. Every vertex-fixing automorphism is determined by its permutation of these five neighbors. Conversely, any permutation of the five \(d_i\) extends linearly to a graph automorphism, because the only dependency is their sum; translations also preserve the graph. Consequently
\[\operatorname{Aut}(G)\cong\mathbb F_2^4\rtimes S_5,\qquad |\operatorname{Aut}(G)|=16\cdot120=1920.\]

For a nonempty candidate determining set \(S\), choose \(x\in S\). Represent each difference \(y+x\), for \(y\in S\setminus\{x\}\), uniquely by a subset of one or two of the directions \(d_1,\ldots,d_5\). Form the zero-one incidence matrix with one row per such \(y\) and one column per direction. An automorphism that fixes \(x\) and all other selected vertices corresponds exactly to a coordinate permutation preserving every row. Therefore its stabilizer is trivial **if and only if** all five columns of this matrix are distinct. This is a necessary and sufficient elementary certificate, not an assumption about graph automorphisms.

The independent script `verify_profiles.py` checks this exact criterion for all \(2^{16}=65536\) subsets, tests inclusion-minimality by deletion of each selected point, and compares each resulting family with the claimed geometric descriptions. It finds precisely \(560\) inclusion-minimal four-sets and \(192\) inclusion-minimal five-sets and no other sizes. It explicitly checks **both directions** of each description for every possible four- and five-set, so the classification does not follow merely from examples or a partial search. In particular, no set of size below four determines the graph.

For the exchange assertion, form every unordered pair of distinct determining four-sets that share exactly three vertices; there are \(5920\) such pairs. Breadth-first search from **all 560** vertices determines every eccentricity, yielding eccentricity four throughout and the stated degrees and layer profiles. The separate program `verify_action.py` reaches the same results by enumerating all \(1920\) automorphisms and explicitly generating one-for-one replacements, rather than using the incidence-column test and pairwise-intersection adjacency. It additionally verifies the indicated orbit decompositions. All exhaustive loops have explicitly finite bounds and executable sources.

Finally, an inclusion-minimal determining five-set cannot be a matroid basis together with a four-set, because bases of a matroid have equal cardinality. This last contrast uses the standard basis notion; it is not an assertion that the entire reconfiguration graph is a matroid basis graph.

## Verification
From a Python 3 interpreter, run `python3 verify_action.py` and `python3 verify_profiles.py` separately. Their expected UTF-8 JSON outputs are `verify_action.out` and `verify_profiles.out`. The first verifies all explicitly constructed automorphisms against all \(16^2\) ordered vertex pairs; the second verifies the five-direction incidence criterion directly and tests all \(65536\) vertex subsets. The exchange graph is exhaustively searched from every optimal set using two different edge-generation procedures. Recorded outputs and code are included with this result. These are finite exact certificates, not probabilistic sampling or numerical approximations.

## Relationship to prior work
Boutin introduced determining sets and stabilizer-based methods, and also investigated the exchange property for other graph families. Bailey and Cameron survey equivalent permutation-group base terminology. Brouwer's graph tables give the relevant five-regular/ten-regular nomenclature and automorphism-group context. The inspected primary works do not state this complete Clebsch determining-set classification or its minimum-set exchange geometry. The earlier group and graph facts are background, not claimed as new.

## Limitations
The originality comparison is a best-knowledge literature comparison, not a proof that no unpublished, unindexed, or differently named finite table contains an equivalent census. The proof is exhaustive for this sixteen-vertex graph only. The computation does not establish analogous formulas for other folded-cube dimensions, any reconfiguration mixing time, or an external independent scientific validation.

## References
1. D. L. Boutin, *Identifying Graph Automorphisms Using Determining Sets*, Electronic Journal of Combinatorics **13** (2006), #R78, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r78/pdf.
2. D. L. Boutin, *Determining sets, resolving sets, and the exchange property*, arXiv:0808.1427, https://arxiv.org/abs/0808.1427.
3. R. F. Bailey and P. J. Cameron, *Base size, metric dimension and other invariants of groups and graphs*, https://www.math.mun.ca/rbailey00/papers/basesize_metdim.pdf.
4. A. E. Brouwer, *Clebsch graph*, https://jaanos.github.io/tables/graphs/Clebsch.html.
