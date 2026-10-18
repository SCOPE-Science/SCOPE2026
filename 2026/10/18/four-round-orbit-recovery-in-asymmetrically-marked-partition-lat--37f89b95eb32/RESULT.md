# Four-round orbit recovery in asymmetrically marked partition lattices

## Finding
Let \(a>b\ge1\) be integers, put \(n=a+b\), and let \(A=\{A_1,A_2\}\) partition \([n]\) into sets of sizes \(a\) and \(b\). In the full strict-refinement order on the lattice \(\Pi_n\) of all set partitions, give \(A\) a unique initial vertex colour and every other partition a common colour. Perform synchronous bidirectional counting colour refinement (in- and out-neighbour colour multiplicities and the previous colour retained at each round).

**Theorem.** After at most four refinement rounds, two partitions \(P,Q\) have equal colours exactly when their multisets
\[
\left\{\!\left\{\bigl(|C\cap A_1|,|C\cap A_2|\bigr):C\in P\right\}\!\right\}
\quad\hbox{and}\quad
\left\{\!\left\{\bigl(|D\cap A_1|,|D\cap A_2|\bigr):D\in Q\right\}\!\right\}
\]
are equal. These colour classes are exactly the orbits of the automorphisms of the marked partition lattice.

The exact number of stable classes is
\[
N(a,b)=[x^a y^b]\prod_{\substack{0\le u\le a,\;0\le v\le b\\u+v>0}}\frac{1}{1-x^u y^v}.
\]
If \(m_{uv}\) blocks have intersection profile \((u,v)\), that class contains
\[
\frac{a!\,b!}{\displaystyle\prod_{\substack{u,v\ge0\\u+v>0}}(u!v!)^{m_{uv}}m_{uv}!}
\]
partitions. In particular, \(N(4,3)=57\) and \(N(5,3)=97\). The four-round bound is an upper bound, not an asserted optimum.

## Assumptions and scope
The relation is the **full directed strict refinement relation**, not the undirected cover graph: \(P<Q\) means that every block of \(P\) is contained in a block of \(Q\), and \(P\ne Q\). Refinement counts strict predecessors and strict successors separately. There are no labels on underlying points in the logic; only the partition \(A\) is individualized. The unequal sizes \(a>b\) are essential to the orientation step in this proof; no theorem is asserted here for equal-size marked blocks, marks with more than two blocks, or identification among arbitrary finite structures.

## Proof
Write \(B_j\) for the number of partitions of a \(j\)-element set. In the first round a partition with \(k\) blocks has exactly \(B_k-1\) strict successors. Since \(B_k\) is strictly increasing for \(k\ge1\), the colour determines \(k\). If its blocks have sizes \(s_1,\ldots,s_k\), then it has \(\prod_i B_{s_i}-1\) strict predecessors.

For any \(p,q\ge2\), \(B_{p+q-1}>B_p B_q\). Indeed, partition two sets of sizes \(p\) and \(q\) sharing one chosen point, then identify the two blocks containing the common point; this embeds pairs of partitions into partitions of their union. A partition joining a noncommon point from each side while leaving the common point separate is not in the image. Consequently, among partitions with \(k<n\) blocks, the unique block-size type maximizing the number of strict predecessors is \((n-k+1,1,\ldots,1)\). Denote a partition of this type by \(E(S)\): its only nonsingleton block is the subset \(S\), with \(|S|\ge2\). The first colour round therefore isolates the family of \(E(S)\) at each size \(|S|\) from all other types. The same round detects whether \(E(S)<A\), which is equivalent to \(S\subseteq A_1\) or \(S\subseteq A_2\), except that a potential equality \(E(S)=A\) is already distinguished by the initial marked colour.

Consider pure \(E(S)\) with \(|S|=t\ge2\). If \(t>b\), its block lies necessarily in \(A_1\). If \(2\le t\le b\), count strict successors \(D\) of \(E(S)\) which have exactly \(n-t\) blocks and satisfy \(D<A\). All such \(D\) are detected as a union of first-round colour classes, since that round knows the block count and relation to \(A\). They are formed by merging one pair of blocks inside the appropriate block of \(A\). The count equals
\[
\binom{a-t+1}{2}+\binom b2\quad\text{when }S\subseteq A_1,
\qquad
\binom a2+\binom{b-t+1}{2}\quad\text{when }S\subseteq A_2.
\]
Their difference is \((t-1)(b-a)\ne0\). Thus by round two all pure \(E(S)\) are classified by \((|S\cap A_1|,|S\cap A_2|)\). Any marked equality case is already individually coloured.

For a mixed \(E(S)\), write \(u=|S\cap A_1|\ge1\) and \(v=|S\cap A_2|\ge1\). Among its strict predecessors of the type \(E(T)\), the number with \(T\) a two-element subset of \(A_1\) is \(\binom u2\), and analogously the count with \(T\subseteq A_2\) is \(\binom v2\). Each of these two predecessor families is a union of round-two colour classes. Because \(r\mapsto\binom r2\) is strictly increasing on positive integers \(r\), round three recovers both \(u\) and \(v\). Together with the pure cases, the third-round colours of the \(E(S)\) recover their exact ordered intersection profiles.

Now take a partition \(P\) that is not itself of type \(E(S)\). For every \((i,j)\) with \(i+j\ge2\), the number of strict predecessors \(E(S)<P\) with \((|S\cap A_1|,|S\cap A_2|)=(i,j)\) is
\[
\beta_{ij}(P)=\sum_{C\in P}\binom{|C\cap A_1|}{i}\binom{|C\cap A_2|}{j}.
\]
Round four reads these numbers using the recovered third-round classes. The missing values \(\beta_{00}\), \(\beta_{10}\), \(\beta_{01}\) equal respectively the number of blocks of \(P\) (known in round one), \(a\), and \(b\). Thus all coefficients of
\[
F_P(X,Y)=\sum_{C\in P}(1+X)^{|C\cap A_1|}(1+Y)^{|C\cap A_2|}
\]
are known. Setting \(U=1+X\), \(V=1+Y\) uniquely recovers the multiplicity of every monomial \(U^uV^v\), hence the block intersection multiset. The exceptional partitions \(E(S)\) have already been classified in round three. Therefore every pair of different intersection multisets is separated by round four.

The group of permutations of \(A_1\) independently of \(A_2\) acts as automorphisms fixing \(A\). It is transitive on exactly the partitions with each prescribed multiset of intersection pairs: match blocks having the same pair, and biject their points separately on the two sides. Thus these orbits are invariant colour cells, and the round-four cells coincide with them; this also excludes any larger orbit fusion by other automorphisms.

Finally, to enumerate profiles, choose a nonnegative multiplicity \(m_{uv}\) for each nonzero pair \((u,v)\), with \(\sum u m_{uv}=a\) and \(\sum v m_{uv}=b\). The generating function above counts these vector partitions. Distributing separately the \(a\) and \(b\) labeled points among the blocks, then dividing by factorials for within-block order and repeated identical block profiles, yields the class-size formula.

## Verification
Run `python3 verify_refinement.py` and `python3 verify_orbit_formula.py` using Python 3 and the standard library. The first independently constructs the strict order and computes all bidirectional refinement rounds for all \(a>b\ge1\) with \(a+b\le7\), checking stable colours against separately enumerated point-stabilizer orbit keys. Nine parameter cases cover 3,161 vertex instances and reach stability by round three. The second independently compares the multivariate coefficient count, orbit cardinalities, Bell totals, and binomial-moment uniqueness across twelve parameter cases with \(a+b\le8\), totaling 15,581 vertex instances; it also computes additional exact coefficients. Both print explicit `VERIFY_..._OK` markers on success. Finite verification is corroboration only; the proof above establishes all indicated parameters.

## Relationship to prior work
Gill (2000) studies the permutation-group action and Möbius/homology representations of partition (semi)lattices, not iteration-bounded refinement of a partition lattice with one distinguished partition. Kiefer, Schweitzer and Selman (arXiv 2015) establish general connections of colour refinement to two-variable counting logic and classify structures identifiable by that logic; their results do not explicitly classify the point-stabilizer orbits of a partition lattice with one unequal two-block landmark. Classical vector-partition generating functions and multinomial counts are standard and are used here as tools, not asserted as independently new. The proposed contribution is the exact four-round anchored reconstruction and its orbit consequence, beyond the unmarked block-size classification.

## Limitations
The upper bound is not claimed sharp. The result is for the full strict directed order, not Hasse edges; unequal two-block anchors are required. It does not show identification of the entire marked lattice among unrelated structures. Priority remains contingent on a specialist literature review: a less-visible prior treatment of individualization in partition lattices or of analogous moment inversion may overlap.

## References
1. R. Gill, *The Action of the Symmetric Group on a Generalized Partition Semilattice*, Electronic Journal of Combinatorics **7** (2000), R23, DOI 10.37236/1501, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v7i1r23/pdf/ .
2. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1 (30 March 2015), https://arxiv.org/pdf/1503.08792 .
3. G. Birkhoff, *Lattice Theory*, third edition, American Mathematical Society (1973), standard account of finite partition lattices.
