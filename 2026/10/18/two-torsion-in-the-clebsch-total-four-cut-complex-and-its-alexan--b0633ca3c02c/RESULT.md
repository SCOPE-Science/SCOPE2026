# Two-torsion in the Clebsch total four-cut complex and its Alexander dual

## Finding

Let \(G\) be the sixteen-vertex, five-regular Clebsch graph defined below. Let \(K=\Delta^t_4(G)\) be its *total four-cut complex*: its facets are the complements of independent four-element vertex sets. Let \(B=K^{\vee}\) be its combinatorial Alexander dual. Then

\[
\widetilde H_j(K;\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&j=6,\\
\mathbb Z^{45},&j=8,\\
0,&\text{otherwise},
\end{cases}
\qquad
\widetilde H_j(B;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{45},&j=5,\\
\mathbb Z/2\mathbb Z,&j=6,\\
0,&\text{otherwise}.
\end{cases}
\]

Moreover, \(K\) is five-connected and \(B\) is four-connected. The complex \(K\) is pure of dimension eleven but is not shellable. Both complexes exhibit genuine integral two-torsion; their homotopy types are **not** asserted to split as wedges of Moore spaces and spheres.

## Assumptions and scope

The vertex set of \(G\) is \(V=\{0,1,\ldots,15\}\), with integers regarded as four-bit binary words. Distinct vertices \(x,y\) are adjacent exactly when their bitwise exclusive-or \(x\oplus y\) belongs to \(\{1,2,4,8,15\}\). This is the five-regular Clebsch graph (the folded five-cube). Every set here is finite, with simplicial homology over the integers and its usual orientation from the increasing vertex order.

A subset \(I\subseteq V\) is independent if no two distinct members are adjacent. Write
\[
K=\{F\subseteq V: \text{there exists an independent }I\subseteq V\setminus F\text{ with }|I|=4\},
\]
and
\[
B=\{F\subseteq V:\alpha(G[F])\le3\}.
\]
The equivalence \(B=K^{\vee}=\{F\subseteq V:V\setminus F\notin K\}\) follows directly from these definitions. The claim is specific to the given Clebsch graph and four-cut parameter; it makes no statement for all strongly regular graphs, all folded cubes, or all cut parameters.

## Proof

**1. Finite models.** The graph has exactly \(120\) independent four-element sets and \(16\) independent five-element sets. Thus \(K\) has \(120\) facets, each with \(12\) vertices, and is pure of dimension \(11\). Exhaustive down-closure of these facets gives the augmented face counts, listed in order from dimension \(-1\) through dimension \(11\),
\[
(1,16,120,560,1820,4368,8008,11440,12270,9040,4096,1056,120).
\]
The Alexander dual \(B\), formed independently by excluding all subsets containing an independent four-set, has augmented face counts in dimensions \(-1\) through \(7\):
\[
(1,16,120,560,1700,3312,3912,2400,600).
\]
All \(2^{16}\) possible vertex subsets are checked for the identity \(B=K^\vee\). The accompanying self-contained verifier reproduces these counts; an independent mod-two verifier uses a different face-generation algorithm.

**2. Complete acyclic matchings.** On each augmented face poset, perform element matching successively with vertices \(0,1,\ldots,15\): at vertex \(v\), pair every still-unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\) when both are available. Different pairs at a fixed vertex are disjoint. The full set of matched cover edges is reversed, and every other cover edge is directed from the larger face to the smaller. A complete directed acyclicity check by topological sorting visits every face, examining every cover incidence. The empty face is matched with a vertex in both complexes.

For \(K\), there are \(26{,}434\) pairs and exactly \(47\) unmatched faces: one in dimension \(6\), one in dimension \(7\), and \(45\) in dimension \(8\). All \(392{,}720\) cover incidences pass the acyclicity check. For \(B\), there are \(6{,}287\) pairs and exactly \(47\) unmatched faces: \(45\) in dimension \(5\), one in dimension \(6\), and one in dimension \(7\). All \(70{,}368\) cover incidences pass. Algebraic discrete Morse theory therefore gives reduced integral chain complexes with only those critical cells, together with the cellular homotopy models used in the connectivity assertions.

**3. Signed integral boundaries.** For an oriented face \(T=\{v_0<\cdots<v_q\}\), the coefficient of \(T\setminus\{v_j\}\) in its simplicial boundary is \((-1)^j\). To project a \(q\)-face to the critical \(q\)-chains, set the projection of critical faces to their basis vectors and of matched upper faces to zero. For a matched lower face \(F\) paired with \(U\), use the exact elimination identity
\[
P(F)=-\varepsilon(F,U)\sum_{\substack{H\subset U\\|H|=|F|\\ H\ne F}}\varepsilon(H,U)P(H),
\]
where \(\varepsilon(H,U)\in\{-1,1\}\) is the signed simplicial incidence. The acyclic directed incidence graph makes this recursion well-founded. Applying it to the ordinary boundaries of every critical cell yields, with ordered bases from the verifier,
\[
\partial^{K}_7=(2),\qquad \partial^{K}_8=(0,\ldots,0)\text{ (45 columns)},
\]
and independently
\[
\partial^{B}_6=(0,\ldots,0)^\mathsf{T}\text{ (45 rows)},\qquad \partial^{B}_7=(-2).
\]
There are no other possible nonzero reduced Morse boundary groups. The resulting integral homology is exactly as displayed in the Finding. In particular, the two-torsion is a genuine Smith factor \(2\), not an inference from computation over a finite field. The Euler characteristics independently agree: \(\widetilde\chi(K)=45\) and \(\widetilde\chi(B)=-45\).

**4. Connectivity and shellability.** The augmented acyclic matching pairs the empty face with a zero-simplex; standard discrete-Morse CW reduction leaves a basepoint and cells only in dimensions \(6,7,8\) for \(K\), and only in dimensions \(5,6,7\) for \(B\). Cellular approximation gives the asserted five- and four-connectivity, respectively. Since the pure eleven-dimensional \(K\) has nonzero homology below its top dimension (and has torsion), the homotopy conclusion required of a pure shellable complex is impossible. Therefore \(K\) is not shellable.

## Verification

Run `python3 verify.py` using Python's standard library. It rebuilds both complexes from the graph definition, checks every subset for combinatorial Alexander duality, checks every element-matching pair and every directed cover relation for acyclicity, and recomputes all signed Morse boundary coefficients from scratch. The expected final line is `VERIFY_OK`; `verify_output.txt` records an execution of this exact program. There are \(52{,}915\) augmented faces for \(K\) and \(12{,}621\) for \(B\). The dual-side calculation is an additional integer-chain check, not merely a repetition of the Betti-number formula. The separate `verify_mod2.py` constructs the dual again by independence-number recursion (rather than enumerating independent quadruples) and reduces the original simplicial boundaries over the two-element field, without any Morse matching. It independently returns degree-five, degree-six and degree-seven reduced Betti numbers of \(45,1,1\), corroborating the integral torsion calculation without replacing it.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduced total cut complexes and classified several graph families, including chordal, cyclic and multipartite examples. The Clebsch graph is not among their stated classified families, and the corresponding total four-cut integral homology is not given there. Their separate ordinary cut-complex construction permits disconnected four-vertex complements; it is different from the total four-cut condition used here.

Carnero Bravo's subsequent study of total cut complexes and Alexander duals gives important connectivity results and torsion-bearing examples built using disconnected graphs and isolated vertices. In particular, its explicit torsion example is not the connected, five-regular Clebsch graph and does not imply either calculation here. The presence of two-torsion among *all* total cut complexes is therefore not claimed to be a new phenomenon; the present contribution is the fully specified, connected, strongly regular Clebsch example and its paired dual integral calculation. Closest indexed same-graph results concern the ordinary independence complex, ordinary three-cut complex, dominance or forest complexes, not this total four-cut complex.

## Limitations

This is a finite, exact classification of **integral homology and connectivity**, not a determination of the complete homotopy types or attaching maps of the higher-dimensional cells. In particular, zero cellular differential from dimension eight does **not** prove that its forty-five cells split off as wedge summands. The computations are exhaustive for this sixteen-vertex graph but do not establish a family theorem. The literature comparison does not exclude unindexed equivalent results, and no independent mathematical audit has been performed.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first posted 2022-09-27, especially Definition 2.3 and the listed family classifications.
2. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first posted 2023-04-26; distinction between ordinary and total cut complexes.
3. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first posted 2026-02-24; connectivity results and Example 36 (torsion from a disconnected construction).
4. The accompanying `verify.py` and its recorded output `verify_output.txt` give the complete finite integer-chain verification for the graph specified here.
