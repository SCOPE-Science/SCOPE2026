# When two-agent someone-knows becomes normal: a componentwise partition criterion and exact census

## Finding

**Theorem.** Let \(W\) be a nonempty finite set of \(n\) labelled worlds, and let \(E_1,E_2\) be two equivalence relations on \(W\). Interpret the bundled modality \(\mathbb S\varphi\) by \(K_1\varphi\lor K_2\varphi\), where \(K_i\) universally quantifies over the \(E_i\)-class of the current world. The following are equivalent, with validity interpreted over **every** propositional valuation on this fixed frame:

1. The distribution schema \(\mathbb S(p\to q)\to(\mathbb Sp\to\mathbb Sq)\) is valid.
2. At every \(w\in W\), the two cells \([w]_{E_1}\) and \([w]_{E_2}\) are comparable by inclusion.
3. Each intersecting block of \(E_1\) and block of \(E_2\) are comparable by inclusion.
4. Each equivalence class of the join \(E_1\vee E_2\) is a whole class of at least one of \(E_1,E_2\).

If these conditions hold, then for **every** modal formula and valuation the bundled operator agrees pointwise with the ordinary \(\mathsf{S5}\) operator for the meet relation \(E_1\cap E_2\):
\[
\mathbb S\varphi\ \equiv\ K_{E_1\cap E_2}\varphi.
\]
Thus the frame validates all normal \(\mathsf{S5}\) axioms for the bundled operator, including arbitrary modal nesting.

Write \(B_k\) for the \(k\)-th Bell number and \(L_n\) for the number of **ordered** pairs \((E_1,E_2)\) on \(n\) labelled worlds satisfying the equivalent conditions. Then \(L_0=1\) by the empty-set counting convention, and
\[
\sum_{n\ge0}L_n\frac{z^n}{n!}
=\exp\!\left(2\exp(e^z-1)-e^z-1\right).
\]
Equivalently, for each \(n\ge1\),
\[
L_n=\sum_{k=1}^{n}\binom{n-1}{k-1}(2B_k-1)L_{n-k}.
\]
The initial values \(L_1,\ldots,L_6\) are \(1,4,19,111,774,6229\). The first non-normal pair occurs on three worlds: there are \(B_3^2-L_3=6\) non-normal ordered pairs at that size, and none for smaller nonempty sets.

## Assumptions and scope

A frame is the ordered pair of equivalence relations, with no designated valuation. \(p,q\) in distribution are independently valued propositional variables. A pair counts separately from its reversal unless its entries coincide. The join \(E_1\vee E_2\) is the least equivalence relation containing both; its classes are the connected components of the undirected graph formed by their union. The meet is their set intersection. All sets of worlds are finite and labelled for enumeration. The empty-world case is used only as a neutral combinatorial base case; modal validity is not asserted there.

## Proof

**Step 1: distribution forces comparable cells.** Fix \(w\) and write \(A=[w]_{E_1}\), \(B=[w]_{E_2}\). If neither \(A\subseteq B\) nor \(B\subseteq A\), choose the valuation \(\llbracket p\rrbracket=A\) and \(\llbracket q\rrbracket=A\cap B\). Since \(p\) holds everywhere on \(A\), we have \(\mathbb Sp\) at \(w\). Since \(p\to q\) holds everywhere on \(B\), we have \(\mathbb S(p\to q)\) at \(w\). But \(q\) fails at some point of each of \(A\) and \(B\), hence \(\mathbb Sq\) fails at \(w\). Distribution fails. Consequently (1) implies (2).

Conversely, suppose (2) holds. For every \(X\subseteq W\), \(\mathbb S X\) holds at \(w\) precisely when either \(A\subseteq X\) or \(B\subseteq X\). Since the two cells are comparable, this is precisely when \(A\cap B\subseteq X\), equivalently \(K_{E_1\cap E_2}X\). The same identity applies to the truth set of any modal subformula, proving the claimed equivalence and (1). In particular (2) implies (3), because every intersecting pair of blocks contains some common \(w\), and (3) implies (2).

**Step 2: join-component structure.** Form the bipartite incidence graph whose left vertices are \(E_1\)-blocks, right vertices are \(E_2\)-blocks, with an edge for nonempty intersection. Under (3), if a left block \(A\) is adjacent to two distinct right blocks \(B,C\), then both \(B\subseteq A\) and \(C\subseteq A\): otherwise \(A\subseteq B\) would prevent \(A\) from meeting the disjoint block \(C\). Thus both neighbors of any degree-at-least-two left vertex have degree one; the same statement holds with sides reversed. Every connected incidence component is consequently a star (an isolated edge is allowed). The union of the worlds on the incident edges is the central block, belonging to one partition, and is a join-class. This proves (4). Conversely, if each join-class is a block of at least one partition, every block of the other partition contained within that join-class is comparable to it, giving (3).

**Step 3: connected pairs.** In a nonempty join-component \(C\) of cardinality \(k\), condition (4) means one of the two restricted partitions has only the indiscrete block \(C\); the other is arbitrary. There are \(B_k\) choices with the first indiscrete, and \(B_k\) with the second indiscrete, with the pair of two indiscrete partitions counted twice. Hence the number of connected permitted pairs is exactly \(c_k=2B_k-1\). Each global permitted pair has a **unique** set partition of worlds into its join-components and a permitted connected pair on every component. Conversely, assembling such decorated blocks produces an ordered pair of equivalence relations satisfying (4); there are no interactions between different blocks. The labelled exponential formula therefore gives \(L(z)=\exp(\sum_{k\ge1}c_kz^k/k!)\). Since \(\sum_{k\ge0}B_kz^k/k!=\exp(e^z-1)\) and \(\sum_{k\ge1}z^k/k!=e^z-1\), the displayed generating function follows. Distinguishing the component containing label \(1\) gives the stated recurrence.

**Step 4: minimum failure.** On one or two worlds, any two equivalence classes through one world are comparable. For three worlds, choose \(E_1\)-classes \(\{1,2\},\{3\}\) and \(E_2\)-classes \(\{1,3\},\{2\}\). At world \(1\), the cells are incomparable. Bell's number \(B_3=5\), so there are \(25-19=6\) failing ordered pairs by the recurrence. This is the sharp minimum non-normal frame size.

## Verification

The standalone Python 3 script `checker.py` enumerates every labelled partition and ordered pair of partitions for sizes \(1\) through \(6\), independently checks the cross-block inclusion criterion, and compares its counts with the Bell recurrence. For sizes \(1\) through \(3\), it further exhausts every pair of valuations for \(p,q\) and all worlds and confirms the exact equivalence with distribution validity. The script prints `ALL_CHECKS_PASSED` on success. These computations confirm finite cases but do not replace Steps 1–3 of the proof.

## Relationship to prior work

Ågotnes and Wang, *Somebody Knows* (2021), show that someone-knows is generally non-normal and give three-world counterexamples to the \(\mathsf K\) schema. Ding, Liu, and Wang, *Someone knows that local reasoning on hypergraphs is a weakly aggregative modal logic* (2023), study neighborhood/hypergraph semantics and weakly aggregative completeness. Ding and Yang, *A General Theory of Propositional Modal Bundled Modalities* (first publicly posted March 27, 2026), axiomatize the bundle over the class of \(\mathsf{S5}\) models. These results motivate seeking the **exceptional fixed finite frames** where normality holds. The stated theorem adds a framewise if-and-only-if, a complete join-component decomposition and an exact ordered-pair census; it does not assert that the general non-normal bundle is normal, nor does it claim the classical labelled exponential formula itself is new.

## Limitations

The classification concerns exactly two equivalence relations on a fixed finite labelled carrier. It does not enumerate isomorphism types, derive a general asymptotic for \(L_n\), or classify normality for three or more agents. Earlier work on weakly aggregative modalities or enriched/colored partition species might contain a more general theorem implying this result; the 2023 journal source could only be examined through public abstracts and bibliographic evidence in this investigation. The result has not received independent review.

## References

1. Yifeng Ding and Yuanzhe Yang. *A General Theory of Propositional Modal Bundled Modalities*. arXiv:2603.26268v1, first posted 2026-03-27; Section 5.1 and Theorem 5.6.
2. Thomas Ågotnes and Yì N. Wáng. *Somebody Knows*. Principles of Knowledge Representation and Reasoning (KR 2021), pp. 2–11, DOI:10.24963/kr.2021/1, especially Sections 1–2.
3. Yifeng Ding, Jixin Liu, and Yanjing Wang. *Someone knows that local reasoning on hypergraphs is a weakly aggregative modal logic*. Synthese 201, article 46 (2023), DOI:10.1007/s11229-022-04032-y.
4. Standard labelled exponential formula for set partitions: \(\sum_{k\ge0} B_kz^k/k!=\exp(e^z-1)\).
