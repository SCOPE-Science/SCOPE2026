# Two marked vertices recover Johnson-graph automorphism orbits

## Finding

Let \(n\) and \(k\) be integers with \(n\ge 2k\ge6\), and let \(J(n,k)\) be the graph whose vertices are the \(k\)-element subsets of an \(n\)-element set, with two vertices adjacent when they differ by one deletion and one insertion. Fix **any two distinct vertices** \(A,B\), assign them distinct individual vertex colours, and give every other vertex one common colour. Perform synchronous ordinary vertex colour refinement: in each round a vertex's new colour encodes its old colour and the multiset of its neighbours' old colours.

**Theorem.** After at most \(k+1\) refinement rounds, the colour classes are exactly the orbits of the automorphism group of \(J(n,k)\) fixing \(A\) and \(B\) separately. Let \(b=k-|A\cap B|\), \(a=k-b\), and \(c=n-k-b\). For a variable vertex \(S\), introduce its four *zone counts*
\[
(t,u,v,z)=\bigl(|S\cap A\cap B|,\ |S\cap(A\setminus B)|,\ |S\cap(B\setminus A)|,\ |S\setminus(A\cup B)|\bigr).
\]
These are precisely the integer quadruples satisfying
\[
0\le t\le a,\quad 0\le u,v\le b,\quad 0\le z\le c,\quad t+u+v+z=k.
\]
When \(n>2k\), each admissible quadruple gives one stable colour class. When \(n=2k\), the classes correspond instead to orbits of the involution
\[
\iota(t,u,v,z)=(a-z,\ b-v,\ b-u,\ a-t).
\]
This is an exact classification, including the cases \(A\cap B=\varnothing\) and \(b=1\).

Writing
\[
F_{n,k,b}=[x^k](1+x+\cdots+x^a)(1+x+\cdots+x^b)^2(1+x+\cdots+x^c),
\]
the exact number of stable colour classes is
\[
N_{n,k,b}=\begin{cases}
F_{n,k,b},&n>2k,\\[2mm]
\bigl(F_{n,k,b}+(a+1)(b+1)\bigr)/2,&n=2k.
\end{cases}
\]
The size of the class indexed by a quadruple is \(\binom a t\binom b u\binom b v\binom c z\). For a balanced-parameter class indexed by two distinct quadruples exchanged by \(\iota\), add the two corresponding sizes (which are equal). Each stable class is consequently definable, relative to the two distinguished unary colours, by a formula of two-variable first-order logic with counting of quantifier rank at most \(k+1\).

The balance transition is substantive. With \((n,k,b)=(8,4,2)\), the full four-zone partition has \(19\) nonempty cells, but the stable partition has just \(14\) because of complementation; for \((9,4,2)\), all \(22\) four-zone cells survive separately.

## Assumptions and scope

The graph is a finite, simple, undirected Johnson graph. The two distinguished vertices are **different** and individually named by different colours; nothing else is initially marked. This is a statement **about stable vertex colours and orbit partitions inside the specified graph**, not a claim that a marked Johnson graph is identified against every nonisomorphic graph by two-variable counting logic. The natural parameter range \(k\le n/2\) avoids duplicating graphs under the standard complement isomorphism \(J(n,k)\cong J(n,n-k)\). The assertion is new here only for \(k\ge3\); the stronger all-markings Tinhofer property of \(J(n,2)\) is already established in the cited literature.

## Proof

**1. Two anchor distances become visible.** The graph distance of \(S\) from \(A\) is \(p=k-|S\cap A|\), and similarly \(q=k-|S\cap B|\). The diameter of \(J(n,k)\) in the assumed range is \(k\). A uniquely coloured source allows iterative refinement to recognize distance layers by induction: after round \(r\), the colour of a vertex determines its distance to that source if at most \(r\), and distinguishes that case from distance greater than \(r\). Indeed, distance exactly \(r+1\) is recognized from a neighbour at distance \(r\) and from the absence of a shorter neighbour; the existing colour retains all earlier distinctions. Apply the argument simultaneously to the two different initially marked sources. After round \(k\), every refinement colour therefore determines the ordered pair \((p,q)\).

**2. Two local neighbour counts recover a zone statistic.** Write \(T=A\cap B\), \(U=A\setminus B\), \(V=B\setminus A\), and \(W=(A\cup B)^c\); their sizes are \(a,b,b,c\). For a vertex with zone counts \((t,u,v,z)\),
\[
p=k-t-u,\qquad q=k-t-v,\qquad z=p+q-k+t.
\]
Of the neighbours of \(S\), let \(M_{--}(S)\) count those whose ordered anchor-distance pair is \((p-1,q-1)\); let \(M_{++}(S)\) count those with pair \((p+1,q+1)\). A Johnson edge exchanges exactly one selected and one unselected underlying element. Both distances decrease precisely by removing a selected element of \(W\) and inserting an unselected element of \(T\). Both increase precisely by removing an element of \(T\) and inserting an unselected element of \(W\). Hence
\[
M_{--}=z(a-t),\qquad M_{++}=t(c-z),
\]
and
\[
M_{--}-M_{++}=a(p+q-k)+(2k-n)t.\tag{1}
\]
At round \(k+1\), the refined colour determines \((p,q,M_{--},M_{++})\): the distance pair is already determined by round-\(k\) colours, and the next neighbour-colour multiset gives the counts of their unions at the two specified pairs.

**3. Nonbalanced case.** If \(n>2k\), the coefficient \(2k-n\) in (1) is nonzero. It determines \(t\) uniquely, after which
\[
u=k-p-t,\qquad v=k-q-t,\qquad z=p+q-k+t
\]
determine all four zone counts. Thus different quadruples have different colours by round \(k+1\).

**4. Balanced case.** If \(n=2k\), then \(c=a\). Put \(s=p+q-k\), so that \(z=s+t\) and
\[
M_{--}=(s+t)(a-t).\tag{2}
\]
For fixed \(p,q\), equality of the quadratic in (2) at feasible \(t\) and \(t'\) implies either \(t=t'\) or \(t+t'=a-s\). In the second case the formulas above give exactly
\[
(t',u',v',z')=(a-z,b-v,b-u,a-t)=\iota(t,u,v,z).
\]
Hence round \(k+1\) separates any two quadruples not connected by \(\iota\).

**5. No further distinctions are possible.** Every permutation of the underlying \(n\)-element set preserving each of the four zones separately fixes \(A\) and \(B\) individually, induces an automorphism of the Johnson graph, and is transitive on vertices with each particular quadruple. This proves that no colour-refinement round can split such a cell. In the balanced case, choose a permutation of the underlying set exchanging \(T\leftrightarrow W\) and \(U\leftrightarrow V\), possible because the paired zone sizes match. Follow its action on \(k\)-subsets by complementation. This is a graph automorphism fixing \(A\) and \(B\) individually and it acts on quadruples by \(\iota\). It follows that no round can distinguish the two halves of a two-quadruple class. Together with Steps 3–4, this proves the claimed exact stable partition and equality with the full pointwise automorphism-stabilizer orbit partition. No classification of the whole automorphism group is needed in this step: the displayed automorphisms are transitive on every stable class, and every automorphism fixes that class setwise because it preserves the initial colours and all refinement colours.

**6. Enumeration and logic.** The polynomial coefficient counts admissible zone-count quadruples. If \(n=2k\), the fixed quadruples of \(\iota\) satisfy \(t+z=a\), \(u+v=b\), giving exactly \((a+1)(b+1)\) fixed quadruples, all admissible since \(a+b=k\). Burnside's two-element orbit count yields the displayed class formula. A quadruple class has the stated product-binomial cardinality by independent selection within zones; the two-quadruple union has the sum. Finally, each vertex colour after \(r\) rounds has a standard inductive definition by a unary formula in \(C^2\) of rank \(r\), using counting quantifiers for neighbour-colour multiplicities. Taking \(r=k+1\) gives the definability assertion.

## Verification

The mathematical proof above covers **all** allowed integers \(n,k,b\) and does not depend on finite search. Two standalone scripts provide independent finite stress tests:

- `direct_refinement.py` constructs Johnson graphs and their adjacency lists, performs synchronous refinement from exactly two individual colours, and compares the full stable partition with the explicitly predicted quadruple/involution partition. It passed \(62\) distinct \((n,k,b)\) cases, covering \(20{,}098\) vertex occurrences in total, with \(6\le n\le12\).
- `arithmetic_profiles.py` independently enumerates admissible quadruples, checks the neighbour-count identities and injectivity modulo the involution, and checks both orbit-count and class-size mass formulas. It passed \(2{,}008\) parameter configurations with \(268{,}128\) admissible quadruple occurrences, for \(6\le n\le36\).

Run both with Python 3 from this directory using `python direct_refinement.py` and `python arithmetic_profiles.py`. Their exact recorded standard outputs are included as `direct_output.txt` and `arithmetic_output.txt`. The finite tests are checks, not substitutes for the proof or exhaustive searches over all parameter values.

## Relationship to prior work

Gavrilyuk and Goryainov (2012) classify two-part equitable colourings of \(J(v,3)\); an arbitrary two-part equitable partition is a different object from the stabilized multicolour refinement under two uniquely marked vertices, and their classification does not imply the present orbit reconstruction. Ganesan's 2014 study establishes the automorphism group of balanced Johnson graphs and isolates the extra complementation symmetry; its group determination does **not** give an algorithmic or logical statement about the stable partition after two individualizations. Arvind–Köbler–Rattan–Verbitsky's 2015 work proves the **stronger all-markings** Tinhofer property specifically for \(J(n,2)\), including a proof in its appendix. The present theorem intentionally assumes \(k\ge3\); it does not re-present their \(k=2\) consequence as new. Arvind and collaborators' 2016 work studies the parameterized complexity of individualization and refinement in general graphs, rather than the pair-specific Johnson-graph partition formula. The exact local statistic (1), the balanced involution, the class-size spectrum and the uniform depth bound together refine the relation between high symmetry and counting logic in the larger Johnson family.

## Limitations

The theorem does not assert the full Tinhofer property for \(J(n,k)\) when \(k\ge3\), does not treat three or more marks, and does not assert that the colour partition determines the whole marked graph against unrestricted competitors. The \(k+1\) upper bound need not be tight for particular parameters. The priority comparison has residual risk of specialized earlier literature on pointed Johnson schemes or equitable partitions that uses different terminology; no independent priority or correctness audit has been performed.

## References

1. Alexander L. Gavrilyuk and Sergey V. Goryainov, *On Perfect 2-Colorings of Johnson Graphs J(v, 3)*, Journal of Combinatorial Designs 21 (published online 2012-07-30), https://doi.org/10.1002/jcd.21327 .
2. Ashwin Ganesan, *On the automorphism group of a Johnson graph*, arXiv:1412.5055 (initial public version 2014-12-09), https://arxiv.org/abs/1412.5055 .
3. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (initial public version 2015-02-04), https://arxiv.org/abs/1502.01255 . See the appendix on \(J(n,2)\) and the definitions of the Tinhofer hierarchy.
4. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert, and G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, MFCS 2016, LIPIcs 58, Article 13 (published 2016-08-19), https://doi.org/10.4230/LIPIcs.MFCS.2016.13 .
