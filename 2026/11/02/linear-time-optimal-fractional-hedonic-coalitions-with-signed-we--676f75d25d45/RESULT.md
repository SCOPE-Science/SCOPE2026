# Linear-time optimal fractional-hedonic coalitions with signed weights on paths and cycles

## Finding

**Theorem.** Let \(G=(V,E)\) be any finite simple undirected graph of maximum degree at most two, with an arbitrary symmetric edge valuation \(w:E\to\mathbb R\), including negative, zero, and irrational values. Each participant \(v\in C\) obtains fractional-hedonic utility
\[
u_v(C)=\frac{1}{|C|}\sum_{z\in C\setminus\{v\}}w_{vz},
\]
where missing edges have value zero. The utilitarian welfare of a partition \(\Pi\) is
\[
\operatorname{SW}(\Pi)=\sum_{C\in\Pi}\frac{2}{|C|}\sum_{e\in E(C)}w_e.
\]
There exists a welfare-maximizing partition in which **every coalition induces a connected subgraph on at most three vertices**. The optimal welfare and such a maximizing partition can be computed in \(O(|V|+|E|)\) arithmetic and comparison operations, regardless of the magnitudes and signs of the valuations.

On a weighted path, the only necessary coalition tiles are a singleton (contribution zero), an edge pair (contribution equal to its edge weight), or a three-consecutive-vertex path (contribution two-thirds of the sum of its two edge weights). On a cycle of length at least four, conditioning on the tile containing one fixed vertex leaves a path and requires only six such dynamic programs. A triangle is a constant-size special case.

The bound of three is tight already on the unweighted three-vertex path: the single triple has welfare \(4/3\), whereas every partition into pairs and singletons has welfare at most \(1\). The maximum-degree restriction is sharp: on the unweighted claw \(K_{1,3}\), the grand coalition has welfare \(3/2\), while every partition with coalition sizes at most three has welfare at most \(4/3\).

## Assumptions and scope

The graph is finite, simple, and undirected, with no edge between distinct connected components. Its maximum degree is at most two. Edge valuations are symmetric and real; no positivity, integrality, or bounded-magnitude assumption is made. Utilities use **coalition size** \(|C|\) as denominator, not \(|C|-1\). All set partitions are allowed; coalitions need not be connected by definition. Complexity is stated in the real-arithmetic/comparison model. A bit-complexity bound for arbitrary encoded reals is neither defined nor asserted.

The theorem guarantees the existence of one optimizer of the specified small-connected-coalition form. It does **not** claim that all welfare-maximizing partitions have this form: for example, all-zero valuations make every partition optimal.

## Proof

**1. Reduction to connected positive components.** Write \(W(C)=\sum_{e\in E(C)}w_e\). A coalition with \(W(C)\le0\) can be split into singletons without reducing welfare, because its contribution \(2W(C)/|C|\) is nonpositive. For a coalition with \(W(C)>0\), let \(C_1,\ldots,C_r\) be the vertex sets of the connected components induced by \(C\). Replacing every component having positive total edge weight by its own coalition, and splitting all other components into singletons, produces welfare
\[
\sum_{j:W(C_j)>0}\frac{2W(C_j)}{|C_j|}
\ \ge\ \frac{2\sum_j\max\{W(C_j),0\}}{|C|}
\ \ge\ \frac{2W(C)}{|C|}.
\]
Thus some optimum uses only positive-weight connected nonsingleton coalitions.

**2. The matching replacement lemma.** Let \(C\) be such a connected coalition with \(q=|C|\ge4\). Its induced graph is a path or an entire cycle, because \(\Delta(G)\le2\). Put \(W=W(C)>0\) and \(P=\sum_{e\in E(C)}\max\{w_e,0\}\ge W\). We construct a matching of positive edges whose total weight is at least \(2W/q\). Replacing \(C\) with its matching-edge pairs and any remaining singleton vertices then preserves or increases welfare, because each pair contributes exactly its edge weight.

For a path, partition the edges into two alternating matchings. Their positive-edge weights total \(P\), so one weighs at least \(P/2\ge W/2\ge2W/q\). For an even cycle, its two alternating perfect matchings give the same inequality, again since \(q\ge4\).

For an odd cycle with \(q\ge5\), take the \(q\) cyclic rotations of one matching of cardinality \((q-1)/2\). Each edge occurs in exactly \((q-1)/2\) of these matchings. After discarding negative edges, the mean matching weight is \((q-1)P/(2q)\). At least one matching has weight no smaller than this mean; since \(q-1\ge4\),
\[
\frac{(q-1)P}{2q}\ge\frac{2W}{q}.
\]
Therefore every connected coalition of size at least four is replaceable by edge pairs and singletons without loss. Applying these replacements to an optimal partition, together with Step 1, proves the three-vertex structural theorem. A connected triple induces a path, except that the full triangle is also possible.

**3. Constructive optimization.** For a path whose vertices are indexed \(0,\ldots,n-1\), let \(a_i=w_{\{i,i+1\}}\). Let \(F_j\) be the maximum welfare of a tiled prefix on \(j\) vertices, with \(F_0=0\). For \(j\ge1\), omitting choices whose tile does not fit, the recurrence is
\[
F_j=\max\left\{F_{j-1},\ F_{j-2}+a_{j-2},\ F_{j-3}+\frac23(a_{j-3}+a_{j-2})\right\}.
\]
The three terms correspond exactly to the last coalition having one, two, or three consecutive vertices. The structural theorem makes this recurrence globally optimal. Backpointers recover a partition. For a cycle of length \(n\ge4\), fix vertex zero. Its tile is exactly one of \(\{0\}\), \(\{0,1\}\), \(\{n-1,0\}\), \(\{0,1,2\}\), \(\{n-1,0,1\}\), or \(\{n-2,n-1,0\}\). For each choice the unoccupied vertices form a single linear interval, so apply the path recurrence and add the fixed tile's welfare. Evaluate all six choices and select the largest. For \(n=3\), enumerate the five set partitions of the triangle directly. Distinct connected components contribute independently. All graph traversals and all constant-many path dynamic programs use \(O(|V|+|E|)\) arithmetic/comparison operations.

**4. Sharpness.** On \(P_3\) with both edge weights one, the triple contributes \(2(1+1)/3=4/3\), versus at most one from any pair/singleton tiling. On \(K_{1,3}\) with unit weights, a grand coalition contributes \(2\cdot3/4=3/2\), versus at most \(2\cdot2/3=4/3\) from a coalition of size at most three and the remaining singleton. This verifies both boundaries.

## Verification

The embedded standalone `verify.py` performs unrestricted set-partition enumeration, independently of the structural argument, for small graphs. It compared the constructive optimum and actual witness welfare with the unrestricted exact-rational optimum on 2,209 path/cycle weight instances and 580 disconnected degree-two instances, including exhaustive ternary edge weights on every path/cycle with up to six edges. All comparisons passed. It separately confirms both sharpness examples. A 10,000-vertex cycle was processed in a separate linear-program implementation test; such finite execution is a computational check, not a proof of asymptotic complexity. The matching lemma and recurrence above provide the infinite mathematical proof.

To reproduce from the embedded source, run `python verify.py` with Python 3 and the standard library; the program prints the successful case counts and raises an exception if any value or witness differs.

## Relationship to prior work

Hanaka, Ikeyama and Ono (2023, arXiv:2310.05139v1, Theorem 5.1) give a general \((nW)^{O(\omega)}\)-time algorithm for weighted fractional-hedonic utilitarian welfare on treewidth \(\omega\), where \(W\) bounds absolute edge weight; for their unweighted block-graph theorem, coalitions have special star/clique structure. Their general weighted bounded-treewidth result includes paths and cycles as objects but does not establish the present magnitude-independent linear bound or the signed degree-two three-vertex structural lemma.

Bilò, Fanelli, Flammini, Monaco and Moscardelli (2018, Lemma 13) prove a diameter-at-most-two coalition property for **unweighted trees**, not arbitrary signed weighted cycles. Aziz, Gaspers, Gudmundsson, Mestre and Täubig (2015) give an exact welfare objective formula and a weighted symmetric general-graph approximation, but not the exact degree-two algorithm. Bazgan, Casel and Cazals (2021/2022) study **unweighted** dense graph partitions, including a remark that maximum-degree-two instances are easy, and establish hardness at cubic degree. Those special cases and prior general algorithms are acknowledged rather than claimed as new.

## Limitations

Only utilitarian welfare is optimized. Nash, egalitarian welfare, and equilibrium stability are not classified. On graphs of maximum degree three, a universal three-vertex optimum need not exist; no hardness claim for signed weighted cubic graphs is made here. The real-arithmetic time bound does not quantify bit growth for rational encodings, nor does it provide oracle access to arbitrary noncomputable real valuations. The structural lemma gives existence, not uniqueness or a count of *all* optimal set partitions. Novelty is assessed against the specifically inspected literature and searchable records; unlocated equivalent weighted-special-case results remain possible. External independent audit has not been conducted.

## References

1. T. Hanaka, A. Ikeyama and H. Ono, *Maximizing Utilitarian and Egalitarian Welfare of Fractional Hedonic Games on Tree-like Graphs*, arXiv:2310.05139v1 (public 2023-10-08), https://arxiv.org/abs/2310.05139.
2. V. Bilò, A. Fanelli, M. Flammini, G. Monaco and L. Moscardelli, *Nash Stable Outcomes in Fractional Hedonic Games: Existence, Efficiency and Computation*, JAIR 62 (2018), doi:10.1613/jair.1.11211, https://www.jair.org/index.php/jair/article/download/11211/26422/20780.
3. H. Aziz, S. Gaspers, J. Gudmundsson, J. Mestre and H. Täubig, *Welfare Maximization in Fractional Hedonic Games*, IJCAI 2015, https://ijcai.org/proceedings/2015/71.
4. C. Bazgan, K. Casel and P. Cazals, *Dense Graph Partitioning on Sparse and Dense Graphs*, arXiv:2107.13282 (2021), SWAT 2022, doi:10.4230/LIPIcs.SWAT.2022.13, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SWAT.2022.13.
