# Two-chain grid posets are identified by depth-six counting logic

## Finding
For integers \(m,n\geq1\), let \(P_{m,n}\) be the finite poset \([m]\times[n]\) with coordinatewise order. In the signature consisting of **only** its strict order \(<\), the following hold.

1. Every \(P_{m,n}\) is uniquely determined **among finite strict partial orders** by its sentences of two-variable first-order logic with counting, \(C^2\). In fact, for each \(m,n\) there is a characteristic \(C^2\) sentence of quantifier rank at most six, with models among finite strict partial orders precisely the isomorphic copies of \(P_{m,n}\). Its counting constants may depend on \(m,n\); the quantifier-rank bound does not.
2. Starting from one colour, four rounds of relation-aware one-dimensional counting refinement on \(P_{m,n}\) yield exactly the automorphism orbits. If \(m\ne n\), every colour class is a singleton. If \(m=n\), the classes are \(\{(i,j),(j,i)\}\), including singleton diagonal classes.
3. **The ambient-class boundary is sharp:** among all finite structures with one binary relation, unrestricted \(C^2\)-identification holds for nonsquare products and for square products of side at most three, but **fails for every square product of side at least four**. The latter still are identified among finite strict partial orders.

This establishes a dimension-two rectangular family with a **uniform logical-depth bound**, even though square grids have nontrivial symmetry.

## Assumptions and scope
A finite strict partial order is an irreflexive, transitive binary relation; the reflexive relation is \(x\leq y\) when \(x=y\) or \(x<y\). For \(P_{m,n}\), \((i,j)\leq(k,l)\) exactly if \(i\leq k\) and \(j\leq l\). A counting quantifier \(\exists^{=r}y\) means exactly \(r\) witnesses; \(r\) may be any specified nonnegative integer. Quantifier rank counts quantifier nesting, not the magnitude of \(r\).

Relation-aware counting refinement begins with one colour. Each round replaces the colour of a vertex by its previous colour together with, for each previous colour, the numbers of vertices equal to it, strictly below it, strictly above it, and incomparable with it. Equivalently, counts use the four disjoint atomic pair-types (equal, strict-less, strict-greater, incomparable). A colour produced after \(t\) rounds has a defining unary \(C^2\) formula of quantifier rank at most \(t\).

## Proof
**Step 1: the two atoms and the axes.** Assume \(m,n\geq2\). The least point \((1,1)\) is unique. An element \((i,j)\) has exactly \(ij-1\) strict predecessors and \((m-i+1)(n-j+1)-1\) strict successors. Thus the two elements with exactly one strict predecessor are precisely the atoms \(a=(2,1)\) and \(b=(1,2)\). They are a colour class after the first round when \(m=n\). When \(m\ne n\), they are **different singleton colours**, since their numbers of strict successors differ by \(n-m\).

For the square case, let \(T\) be the set of elements incomparable with exactly one of \(a,b\). This is precisely the union of the two coordinate axes *without* the least point:
\[
T=\{(k,1):2\leq k\leq n\}\cup\{(1,k):2\leq k\leq n\}.
\]
Because the atoms form a first-round class, membership in \(T\) is decided in round two. Within \(T\), an axis point at distance \(k-1\) from the least point has exactly \(k-2\) strict predecessors in \(T\). Hence by round three the pair
\[
T_k=\{(k,1),(1,k)\},\qquad 2\leq k\leq n,
\]
has a distinct colour for every \(k\). For \(m\ne n\), one uses the two individually distinguished atoms instead: the two axes are distinguished in round two, each of their elements in round three by its predecessor count along that axis.

**Step 2: recovering all orbit classes.** In a square grid, for \(x=(i,j)\) and each \(2\leq k\leq n\), the number of elements of \(T_k\) weakly below \(x\) equals
\[
\mathbf 1_{\{k\leq i\}}+\mathbf 1_{\{k\leq j\}}.
\]
These numbers, read over all \(k\), determine the unordered pair \(\{i,j\}\). Thus by round four precisely the sets \(\{(i,j),(j,i)\}\) can remain together. The coordinate-swap automorphism prevents any further separation. In a nonsquare grid the two ordered sequences of axis points are individually coloured by round three; the weak comparison profile against those singleton colours determines both coordinates, making round four discrete. A one-factor product is a chain, whose distinct predecessor counts make refinement discrete in one round.

**Step 3: reconstructing any equivalent square poset.** Let \(Q\) be a finite strict partial order having the same fourth-round colour-class sizes and comparison counts between those classes as \(P_{n,n}\). Write \(T_k^Q\) for the class corresponding to \(T_k\). Each \(T_k^Q\) has two elements. For every \(k<l\), the strict comparisons from \(T_k^Q\) into \(T_l^Q\) form a perfect matching, just as in the grid. Choose names \(A_2,B_2\) for the two atoms. For \(k>2\), name \(A_k\) the unique point of \(T_k^Q\) above \(A_2\), and \(B_k\) the other point. **Transitivity** forces all \(A_2<A_3<\cdots<A_n\) and \(B_2<B_3<\cdots<B_n\), with no cross-axis comparisons. Indeed, a crossed comparison \(A_k<B_l\), for \(2\leq k<l\), would imply \(A_2<B_l\), contradicting the prescribed matching from \(T_2^Q\) to \(T_l^Q\).

For each \(x\in Q\), define \(i(x)\) to be the largest \(k\) for which \(A_k\leq x\), or \(1\) if no such \(k\) exists. Define \(j(x)\) similarly using the \(B\)-axis. Transitivity makes each axis intersection an initial segment. The comparison counts of the colour classes \(T_k^Q\) below \(x\) are the formula in Step 2, so if \(x\) belongs to the class indexed by \(\{r,s\}\), then \(\{i(x),j(x)\}=\{r,s\}\). For \(r<s\), the two members acquire the **opposite** coordinate assignments: each point of \(T_s^Q\) is below exactly one member of that two-element class, so they cannot both choose the same axis. (For the class \(T_s^Q\) itself this matching is the equality relation.) Thus every ordered pair in \([n]^2\) labels exactly one vertex of \(Q\).

If \(x\leq y\) in \(Q\), transitivity makes the axis points below \(x\) a subset of those below \(y\); hence \(i(x)\leq i(y)\) and \(j(x)\leq j(y)\). Conversely, for fixed \(x\) and any fourth-round colour class \(D\), the number of vertices of \(D\) with both coordinates greater than or equal to those of \(x\) is **exactly** the number of elements of \(D\) above \(x\) in the reference grid. The colour-class comparison counts in \(Q\) agree with those in the grid. Since no other members of \(D\) can be above \(x\), all coordinatewise allowed comparisons must occur. The coordinate labelling therefore is an order isomorphism \(Q\cong P_{n,n}\).

If \(m\ne n\), Step 2 already produces singleton classes. Equality of fourth-round class sizes and strict comparison counts then directly forces every entry of the binary relation, **even without assuming** the competitor satisfies the axioms of a partial order.

**Step 3a: sharp boundary without a poset assumption.** When \(n=2\), the square grid has only one doubleton orbit class, so its comparison profiles uniquely force the relation among arbitrary binary structures. When \(n=3\), the three doubleton classes are \(T_2,T_3,\{(2,3),(3,2)\}\). Their only non-forced relation blocks are the two one-regular matchings \(T_2\to T_3\) and \(T_3\to\{(2,3),(3,2)\}\). The two choices for each block give four combinations; starting with arbitrary labels of \(T_2\), one can propagate the matching labels along this three-class path, making **every** combination isomorphic to the original grid. Other blocks are forced by their zero-or-all edge degrees and the singleton classes. For \(n=1\) the structure is a singleton.

For every \(n\ge4\), by contrast, keep the strict-order relation of \(P_{n,n}\) except for the comparison block between \(T_2\) and \(T_4\): replace the two edges \( (2,1)<(4,1)\) and \( (1,2)<(1,4)\) by \( (2,1)<(1,4)\) and \( (1,2)<(4,1)\). Each element retains the same comparison counts into every fourth-round orbit class, as a perfect matching was simply crossed. Because the grid orbit partition is equitable, joint counting refinement cannot distinguish the resulting binary structure from the grid. But the unchanged chain \( (2,1)<(3,1)<(4,1)\) has lost its first-to-last comparison, so the new relation is not transitive, hence not isomorphic to the original poset. This proves both failure of unrestricted \(C^2\) identification and the necessity of the **poset-class restriction** from side four onward.

**Step 4: the uniform bound.** Each fourth-round colour class of the reference poset has a unary defining \(C^2\) formula of quantifier rank at most four. Conjoin assertions giving (i) that the classes cover the domain, (ii) their exact sizes, and (iii) the numbers of strict successors and predecessors of each class from each point of every other class. Counting quantifiers make the latter assertions expressible with one additional counting-quantifier layer and one outer universal quantifier. The resulting characteristic sentence has quantifier rank at most six. Steps 2–3 prove its required model uniqueness among finite posets.

## Verification
The included `grid_refinement_check.py` constructs the strict order directly, independently recomputes the relation-type count signatures through four refinement rounds, and compares the resulting partition with the predicted orbit partition for 113 rectangles (all \(2\leq m\leq n\leq15\) plus eight larger or uneven instances). It reports success.

The separate `square_competitor_check.py` enumerates every alternative one-regular comparison block compatible with the prescribed colour-class degrees in the square grids of side \(2,3,4\). For side four there are nine independently switchable matching blocks, hence 512 equitable block choices; exactly 32 yield transitive orders, and all 32 are isomorphic to the target grid. The corresponding counts at sides two and three are 1/1 and 4/4. A third, separately implemented program, `sharp_boundary_check.py`, constructs the crossed-matching nontransitive companion and confirms counting-refinement indistinguishability through stabilization for square sides four through eight. These finite checks are **corroboration, not the all-size proof**; the proof is in the preceding section. Exact commands and outputs appear in `CHECKS.txt`.

## Relationship to prior work
Immerman and Lander (1990) developed the connection between counting logic and colour-refinement descriptions and established identification results including trees. Arvind, Köbler, Rattan, and Verbitsky (first preprint 2015) study which **undirected graphs** are distinguished by colour refinement and related fractional invariants. Grädel, Otto, and Rosen (1997) establish decidability of \(C^2\). None of the inspected results supplies the present relative identification theorem for **partially ordered products of two chains**, the explicit orbit-partition proof, or the uniform rank-six bound. The proof above uses its own reconstruction argument, not an identification theorem asserted by these sources.

## Limitations
Square grids of side at least four are **not** identified among arbitrary binary-relational structures: the explicit crossed-matching competitor is nontransitive and has the same \(C^2\) theory. Partial-order transitivity itself requires three variables to state directly. No assertion is made for general products of three or more chains, or for all finite distributive lattices. The quantifier-rank bound is sufficient but is not claimed optimal. Prior publication priority has not been independently certified; a specialized treatment of finite posets may contain a related result.

## References
1. N. Immerman and E. Lander, *Describing Graphs: A First-Order Approach to Graph Canonization*, in *Complexity Theory Retrospective*, 1990, pp. 59–81. https://people.cs.umass.edu/~immerman/pub/canon.pdf
2. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, first posted 2015-02-04, arXiv:1502.01255. https://arxiv.org/abs/1502.01255
3. E. Grädel, M. Otto, and E. Rosen, *Two-Variable Logic with Counting Is Decidable*, LICS 1997, pp. 306–317. https://www.lfcs.inf.ed.ac.uk/events/lics/1997/GraedelOttoRosen-Twovariablelogicwit.html
