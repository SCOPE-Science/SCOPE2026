# A sharp first adaptive-shattering gap for acyclic graph orientations and connected subcubic amplifiers

## Finding

For a finite simple undirected graph \(G=(V,E)\), fix one reference direction on every edge. The **acyclic-orientation concept class** \(\mathcal A(G)\subseteq\{0,1\}^{E}\) consists of all Boolean edge-direction vectors that orient \(G\) without directed cycles. A query specifies an edge, and the answer gives the direction of that edge relative to its reference direction.

The following statements hold.

1. For every finite \(G\), with \(c(G)\) connected components (isolated vertices included),
   \[\operatorname{VCdim}(\mathcal A(G))=|V|-c(G).\]
   Every pseudoforest (each component has at most one cycle) has equal VC and Littlestone dimensions.
2. For the complete bipartite graph \(K_{2,3}\),
   \[|\mathcal A(K_{2,3})|=46,\qquad \operatorname{VCdim}(\mathcal A(K_{2,3}))=4,\qquad \operatorname{Ldim}(\mathcal A(K_{2,3}))=5.\]
   No bipartite graph on fewer than five vertices has this strict gap; among bipartite graphs on five vertices, \(K_{2,3}\) is the only one with a gap.
3. For every integer \(s\ge1\), a connected planar bipartite graph \(G_s\) with maximum degree three and \(5s\) vertices satisfies
   \[\operatorname{VCdim}(\mathcal A(G_s))=5s-1,\quad \operatorname{Ldim}(\mathcal A(G_s))=6s-1.\]
   Hence the VC–Littlestone gap is unbounded even on connected planar subcubic bipartite graphs.

The distinction concerns *realizable online mistake complexity*, characterized by complete binary Littlestone-shattered trees; it is not the adaptive query count required to identify an unknown orientation.

## Assumptions and scope

All graphs are finite, simple and undirected before orientation. Acyclicity forbids every directed cycle. Concepts have one Boolean coordinate per undirected edge. Changing any reference direction merely complements the corresponding coordinate, leaving both dimensions invariant. The empty edge set gives dimension zero.

A set of query coordinates is VC-shattered if every fixed binary labeling extends to a concept. A complete binary tree of depth \(d\) is Littlestone-shattered if every root-to-leaf labeled sequence has an extending concept; different internal nodes may query different coordinates. Distinct branches at the same internal node receive opposite answers.

In the explicit \(K_{2,3}\) certificate, the bipartition is \(\{a,b\}\cup\{u,v,w\}\), and the six coordinate indices are, in order, \((a,u),(a,v),(a,w),(b,u),(b,v),(b,w)\). Bit \(0\) orients from the listed first endpoint to the second, and bit \(1\) orients backward. The complete certificates and standalone checkers accompany this document.

## Proof

**The forest criterion.** Let \(F\subseteq E(G)\). If \(F\) contains a cycle, orient those cycle edges cyclically. This is an assignment on \(F\) with no acyclic extension, so \(F\) is not shattered. Conversely, if \(F\) is a forest, any assignment of directions to \(F\) is a directed acyclic graph. Take a topological ordering of its vertices and orient all remaining edges forward in this order. The resulting orientation of \(G\) is acyclic and extends the assignment. Therefore \(F\) is shattered if and only if it is a forest. Its maximum size is the graphic-matroid rank \(|V|-c(G)\), proving the VC formula.

**Trees, cycles, and pseudoforests.** A forest admits all \(2^{|E|}\) orientations, so both dimensions equal \(|E|\). A simple cycle on \(r\ge3\) edges admits exactly \(2^r-2\) acyclic orientations: only the two consistently directed cycles are excluded. Its VC dimension is \(r-1\), and the general inequality \(\operatorname{VCdim}\le\operatorname{Ldim}\), together with \(2^r-2<2^r\), forces its Littlestone dimension to equal \(r-1\). Every edge outside the unique cycle of a connected unicyclic graph is a bridge, hence has an unrestricted independent orientation. By the disjoint-coordinate additivity lemma below, its dimension is the sum of the cycle dimension and its number of bridges. The same holds componentwise for pseudoforests, giving equality of the two dimensions.

**The six-edge obstruction.** A directed cycle in \(K_{2,3}\) must use two vertices from each bipartition class, so must be a directed four-cycle. For each \(z\in\{u,v,w\}\), let \((p_z,q_z)\in\{0,1\}^2\) encode the two edges incident to \(z\). A directed four-cycle exists if and only if some \(z\) has \((p_z,q_z)=(0,1)\) and a different \(z'\) has \((p_{z'},q_{z'})=(1,0)\). Thus the allowed words are the union of the ternary products with symbols \(\{00,01,11\}\) or \(\{00,10,11\}\). Their intersection consists of \(\{00,11\}^3\), yielding
\[|\mathcal A(K_{2,3})|=3^3+3^3-2^3=46.\]
A depth-six shattered tree needs \(64\) distinct concepts, so \(\operatorname{Ldim}\le5\). The array of \(31\) internal edge queries and the \(32\) distinct leaf witness words in `certificate.json` give a complete depth-five shattered tree. The verifier checks every one of the \(160\) leaf-to-node answer constraints, the acyclicity of all witness words, and the count of distinct witnesses; it therefore proves \(\operatorname{Ldim}\ge5\). The forest criterion gives \(\operatorname{VCdim}=2+3-1=4\). This proves the strict gap exactly, without extrapolation from an enumeration.

**Small bipartite graphs.** A bipartite graph with at most four vertices is a forest or has its only cycle equal to a four-cycle, so is a pseudoforest. A bipartite graph on five vertices with two independent cycles must have at least six edges and bipartition sizes \(2\) and \(3\), with six edges available in total: it must be \(K_{2,3}\). All other bipartite graphs on five vertices are pseudoforests. This proves the claimed first occurrence and uniqueness.

**Additivity lemma.** If \(\mathcal C\) and \(\mathcal D\) are nonempty Boolean concept classes on disjoint query domains, their Cartesian product satisfies
\[\operatorname{VCdim}(\mathcal C\times\mathcal D)=\operatorname{VCdim}(\mathcal C)+\operatorname{VCdim}(\mathcal D),\qquad \operatorname{Ldim}(\mathcal C\times\mathcal D)=\operatorname{Ldim}(\mathcal C)+\operatorname{Ldim}(\mathcal D).\]
For VC dimension, the trace on any query set factors into the traces on its intersections with the two domains; it is full precisely if both factors are full. For Littlestone dimension, first place a shattered tree for \(\mathcal C\), and under each of its leaves place an independent shattered tree for \(\mathcal D\), proving the lower bound. For the upper bound, run the optimal realizable Littlestone mistake-bound algorithm separately on each coordinate domain. Every example belongs to exactly one domain, so the total number of mistakes is bounded by the sum of the two optimal mistake bounds. The standard equivalence between optimal realizable mistake bound and Littlestone dimension proves the upper bound. The same reasoning extends to any finite number of factors.

**Connected degree-three amplifiers.** Take \(s\) vertex-disjoint copies of \(K_{2,3}\), labeling the degree-two side of copy \(j\) by \(u_j,v_j,w_j\). Add exactly the bridge \(w_j u_{j+1}\) for each \(1\le j<s\). Call the resulting graph \(G_s\). Its \(5s\) vertices form a connected graph; no vertex has degree more than three, because different bridge ends in an interior copy are the distinct degree-two vertices \(u_j,w_j\). Every block is planar, bridges preserve planarity, and the bipartitions of alternating blocks can be reversed to make the bridges bipartite.

No directed cycle can use a bridge. Consequently acyclic orientations of \(G_s\) are exactly independent acyclic orientations of its \(s\) five-vertex blocks together with arbitrary choices of its \(s-1\) bridge directions. By additivity,
\[\operatorname{Ldim}(\mathcal A(G_s))=5s+(s-1)=6s-1.\]
By the forest criterion and connectedness, \(\operatorname{VCdim}(\mathcal A(G_s))=5s-1\). Their difference is \(s\) for every positive integer \(s\), completing the proof.

## Verification

`certificate.json` uses breadth-first heap order for the \(31\) internal-node edge labels. A length-five branch word selects a leaf witness from `leaf_orientation_words` in lexicographic branch order. The query at depth \(t\), after the \(t\)-bit branch prefix interpreted as an integer \(j\), is at array index \(2^t-1+j\).

Run `python3 verify.py` alongside `certificate.json` to independently enumerate all \(64\) edge orientations by a topological-sort acyclicity test, calculate the two dimensions by exact finite recurrences and traces, and replay the complete certificate. Run `g++ -std=c++17 -O2 independent.cpp -o check && ./check` for a separately implemented four-cycle characterization and complete certificate replay. Their recorded outputs are `verify_output.txt` and `cpp_output.txt`. Neither program requires network access or external packages.

The mathematical proof, rather than a finite computer search over general graphs, establishes the theorem for every \(s\ge1\). Computer checking is confined to the explicit five-vertex obstruction and its fully specified finite certificate.

## Relationship to prior work

Walker, *Tree Dimension and the Sauer–Shelah Dichotomy* (arXiv:2203.12211, first public March 23, 2022), develops general shattering/tree-dimension bounds, including VC and Littlestone versions. Its statements do not determine the acyclic-orientation values of \(K_{2,3}\) or the connected bounded-degree family here.

Pradeep, Nachum and Gastpar, *Finite Littlestone Dimension Implies Finite Information Complexity* (arXiv:2206.13257, first public June 27, 2022), treats general optimal online-mistake complexity and associated information complexity, not graph-specific acyclic-orientation classes.

Pikhurko, *Finding an Unknown Acyclic Orientation of a Given Graph* (arXiv:0904.1229, April 7, 2009; subsequently published in *Combinatorics, Probability and Computing*), studies worst-case **active identification query counts** \(c(G)\). That is a different adversarial objective from realizable **mistake bound**/Littlestone dimension; general active-identification bounds do not imply a complete depth-five shattered decision tree. The inspected paper's statements concern \(c(G)\), not the graph-specific VC and Littlestone formulas above.

Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique* (ITCS 2023; arXiv preprint 2022), proves generic dimension-computation hardness; it does not supply these explicit graph classes in the material inspected. A related public research record studies non-separating out-branchings in acyclic orientations of \(K_{3,n}\), a different invariant. Publication priority beyond inspected sources is not certified.

## Limitations

No exact formula for the Littlestone dimension of every graph or every \(K_{2,n}\) is asserted. The first-gap statement is specific to bipartite graphs; unrestricted graphs can exhibit other behavior. The connected constructions contain bridges and are not claimed to be two-edge-connected. The dimension of their orientation classes does not by itself determine the active identification cost \(c(G)\), information complexity, or agnostic-learning rates. The source comparison is bounded and does not establish absolute historical novelty. Formal machine-checked proof and independent scientific audit have not been performed.

## References

1. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211 (2022), https://arxiv.org/abs/2203.12211.
2. A. Pradeep, I. Nachum and M. Gastpar, *Finite Littlestone Dimension Implies Finite Information Complexity*, arXiv:2206.13257 (2022), https://arxiv.org/abs/2206.13257.
3. O. Pikhurko, *Finding an Unknown Acyclic Orientation of a Given Graph*, arXiv:0904.1229 (2009), https://pikhurko.github.io/E/Pikhurko10cpc.pdf.
4. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, ITCS 2023, DOI 10.4230/LIPIcs.ITCS.2023.85.
