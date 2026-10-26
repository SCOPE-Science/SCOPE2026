# Six rank-four theories of finite hypercube graphs and a sharp 64-vertex kernel

## Finding

Write \(Q_d\) for the simple graph on \(\{0,1\}^d\), joining two binary words precisely when their Hamming distance is one. In the first-order adjacency-and-equality language, for **all integers** \(d,e\ge1\),

\[
Q_d\equiv_4 Q_e\quad\Longleftrightarrow\quad \min(d,6)=\min(e,6).
\]

Here \(\equiv_4\) denotes agreement on *every* first-order graph sentence of quantifier rank at most four (without counting quantifiers or named vertices). Consequently, there are exactly six such theories among all positive-dimensional finite hypercubes. Every one has a hypercube representative of at most \(2^6=64\) vertices, and that bound is sharp: the sixth class has no hypercube representative on fewer than 64 vertices.

## Assumptions and scope

The structures are finite, nonempty, undirected, loopless graphs; the only nonlogical relation is adjacency. Dimension \(d\) is a positive integer. Vertices are not named, coordinates are not part of the signature, and quantified variables range over vertices. The bound is for representatives **within the hypercube family**, not for arbitrary graphs realizing the same rank-four theory.

For \(j\ge0\), let \(\Delta_j(u,v)\) express graph distance at most \(j\). Define \(\Delta_1(u,v)\) as \(u=v\lor E(u,v)\), define \(\Delta_2(u,v)\) as \(\exists w\,[\Delta_1(u,w)\land\Delta_1(w,v)]\), and define \(\Delta_4(u,v)\) as \(\exists w\,[\Delta_2(u,w)\land\Delta_2(w,v)]\). Their respective quantifier ranks are zero, one, and two.

## Proof

**1. Five explicit separation boundaries.** For \(k=2,3\), the sentence asserting that some vertex has \(k\) pairwise distinct neighbors has rank \(k+1\) and holds in \(Q_d\) iff \(d\ge k\). Thus rank at most four separates dimension one from two, and two from three.

The rank-three sentence
\[
\exists x\exists y\forall z\,[z=x\lor z=y\lor E(x,z)\lor E(y,z)]
\]
expresses that two closed neighborhoods cover all vertices. It holds in \(Q_3\) (choose antipodes) and all lower dimensions. It fails in each \(Q_d\) for \(d\ge4\), since the union of two closed neighborhoods has at most \(2(d+1)<2^d\) vertices.

The rank-four sentence \(\forall x\forall y\,\Delta_4(x,y)\) says that the diameter is at most four; because \(\operatorname{diam}(Q_d)=d\), it separates dimensions at most four from dimensions at least five.

Finally, the rank-four sentence
\[
\exists x\exists y\forall z\,[\Delta_2(x,z)\lor\Delta_2(y,z)]
\]
asserts that two radius-two balls cover the vertices. In \(Q_5\), antipodal centers cover the cube, since each word lies at distance at most two from one of them. For each \(d\ge6\), two radius-two balls cover at most \(2(1+d+\binom d2)<2^d\) vertices; the strict inequality holds at six and thereafter by elementary induction. This separates dimension five from every larger dimension. The five boundaries establish at least six theories, including the sharpness of the 64-vertex representative.

**2. Coordinate-orbit description of all four-round types.** Consider an ordered \(t\)-tuple \(\bar a=(a_1,\ldots,a_t)\), \(t\ge1\). Each coordinate is classified by its \((t-1)\)-bit pattern \(\eta\) of differences between \(a_j\) and \(a_1\) for \(2\le j\le t\). Let \(c_\eta\) be the number of coordinates with pattern \(\eta\). Translating all vertices and permuting coordinates preserves adjacency; conversely these operations take any two ordered tuples with the same vector \(c=(c_\eta)\) to one another. Thus \(c\) is a complete orbit invariant for ordered tuples.

Let \(A_t(c)\) record, for each ordered pair of tuple positions, whether their vertices coincide, are adjacent, or are distinct and nonadjacent. Hamming distances are sums of coordinate-class counts, so \(A_t(c)\) is determined exactly by \(c\). Put \(H_{t,0}(c)=A_t(c)\). For \(r\ge1\), put
\[
H_{t,r}(c)=\bigl(A_t(c),\{H_{t+1,r-1}(s):s\in\operatorname{Split}(c)\}\bigr),
\]
where \(\operatorname{Split}(c)\) ranges over *all* ways of splitting every integer \(c_\eta\) into nonnegative parts \(c_{\eta,0}+c_{\eta,1}=c_\eta\). These are precisely the possible coordinate patterns obtained by adjoining a further vertex. A straightforward induction on \(r\) (the Hintikka-type or Ehrenfeucht–Fraïssé induction) shows that two tuples have the same \(H_{t,r}\) if and only if they agree on all formulas of quantifier rank at most \(r\) with those tuple positions as the available parameters. The set of child types, rather than a multiset, is essential: ordinary first-order logic quantifies existentially over a possible next vertex; subsequent equality tests are already encoded at the next stage.

**3. Finite stabilization lemma.** For an integer \(K\ge0\), write \(\operatorname{cap}_K(c)\) for componentwise truncation \(\min(c_\eta,K)\). For every \(r\ge0\),
\[
\operatorname{cap}_{2^{r+1}}(c)=\operatorname{cap}_{2^{r+1}}(c')
\quad\Longrightarrow\quad H_{t,r}(c)=H_{t,r}(c').
\]
For \(r=0\), componentwise truncation at two preserves whether each pair distance is zero, one or at least two. For the induction, write \(h=2^r\). If two nonnegative integers agree when capped at \(2h\), then their entire sets of feasible ordered splits agree after each resulting part is capped at \(h\): for a parent value at least \(2h\), any split either has a part below \(h\), which is copied exactly while the other part stays at least \(h\), or has both parts at least \(h\), which is realizable in both parents. Small parent values match exactly. Apply this independently to every coordinate class and then induct on \(r\).

For a single marked vertex there is only one coordinate class with count \(d\). Thus all \(H_{1,3}((d))\) agree when \(d\ge16\). Hypercube vertex transitivity means that the rank-four sentence type of \(Q_d\) is exactly determined by the rank-three profile of any marked vertex: every first move is equivalent, and the root atomic type is constant. Therefore **every \(Q_d\) with \(d\ge16\) is rank-four equivalent**.

**4. Exact finite calculation covering the remainder.** The standalone `verification.py` implements the preceding recurrence for \(t=3,r=1\), \(t=2,r=2\), and \(t=1,r=3\), using exact integers and canonical sorted sets. It computes all dimensions \(1\le d\le17\). The resulting root profiles are different at each \(d=1,2,3,4,5,6\) and coincide for every \(6\le d\le17\). The stabilization lemma covers all larger dimensions, establishing the theorem. The program also verifies that for \(d\ge6\) the six distinct two-pebble rank-two types correspond exactly to Hamming distances \(0,1,2,3,4,\ge5\). This is supplementary structural evidence, not an extra assumption in the proof.

## Verification

Run `python3 verification.py` beside this file. The accompanying `verification_output.txt` records distinct canonical SHA-256 fingerprints at dimensions one through six, an identical fingerprint from six through seventeen, the final `FINITE_PROFILE_CLASSIFICATION_OK` check, and `VERIFY_OK`. In a separate graph-level cross-check, the program directly enumerates all \(8,64,512,4096,32768,262144\) ordered triples, respectively, for dimensions one through six and their possible fourth-vertex adjacencies, along with all ordered pairs and third-vertex extensions. Both calculations agree exactly on every tested tuple. The mathematical truncation lemma—not extrapolation from these finite computations—handles every dimension beyond sixteen.

## Relationship to prior work

Pikhurko and Verbitsky, *Logical complexity of graphs: a survey* (arXiv:1003.4865, first public 2010-03-25), develops logical depth, Ehrenfeucht games and balanced distance formulas for finite graphs, but does not state this six-class hypercube theorem. Clemente and Tyszkiewicz, *Problems in logic for computer science students* (May 2020), Problem 2.12.11 and its solution, explicitly give a rank-three separation of \(Q_3\) and \(Q_4\), covering one special comparison made above; it neither states the \(Q_5\)/\(Q_6\) boundary nor establishes the uniform high-dimensional equivalence. These comparisons concern conclusions and their implications, not merely matched terminology. Related research on logical profiles of Johnson/rook graphs and on marked-hypercube color refinement concerns distinct graph families or logical invariants and does not imply the present theorem.

## Limitations

The theorem concerns ordinary adjacency/equality first-order logic at rank four, not counting logic, other ranks, named coordinates, or arbitrary finite products. The bound 64 is sharp only among hypercube representatives. The finite computation was subjected to additional direct tests but not independent external audit. Exhaustive discovery of all historic literature is not claimed: a specialized treatment under different terminology or an unindexed prior solution remains possible.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first posted 2010-03-25; revised 2013), https://arxiv.org/abs/1003.4865 .
2. L. Clemente and J. Tyszkiewicz, *Problems in logic for computer science students*, May 2020, Problem 2.12.11 and solution, https://lclem.github.io/logic_course/book/logic_book_2020-05-24.pdf .
