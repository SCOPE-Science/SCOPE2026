# Sharp length of involution-avoiding cyclic two-window words

## Finding
Let \(\Sigma\) be a finite alphabet equipped with an involution \(\pi:\Sigma\to\Sigma\), meaning \(\pi^2\) is the identity. Suppose \(\pi\) has \(f\ge0\) fixed symbols and \(t\ge1\) two-element orbits, so \(q=|\Sigma|=f+2t\). A **two-window involution-avoiding cycle** is a nonempty cyclic word \(w\) over \(\Sigma\) in which all cyclic consecutive ordered pairs are distinct and no pair \((x,y)\) occurs together with \((\pi(x),\pi(y))\). In particular, no pair fixed by \(\pi\) may occur. A word of cyclic length one has its single pair \((x,x)\).

**Theorem.** For every such alphabet and involution, the greatest possible cyclic length is
\[
\boxed{L_{\max}(\pi)=\frac{q^2-f^2}{2}-\mathbf1_{\{f=0\text{ and }t\text{ odd}\}}.}
\]
An explicit balanced connected directed-edge selection described below attains the bound, and an Euler tour of that selection gives a maximum cycle. Thus the elementary orbit-counting bound is sharp **except** when there are no fixed symbols and the number of swapped symbol pairs is odd; in exactly that case the unavoidable deficiency is one pair orbit.

For example, when \((t,f)=(1,0),(2,0),(3,0),(1,1),(1,2),(1,3)\), the respective optimal lengths are \(1,8,17,4,6,8\). The formula includes every value of \(t\ge1\) and \(f\ge0\); it is not an asymptotic statement.

## Assumptions and scope
Two words count as the same consecutive pair only if their symbols agree *in order*. The alphabet symbols have no arithmetic structure: the involution may consist of any number of fixed points and disjoint transpositions. The cyclic boundary pair is included. Our result is limited to span two; it says nothing about longer windows or counts of optimal cycles. The vacuous case \(t=0\), where no nonempty valid cycle exists, is deliberately excluded.

For construction, relabel the moving symbols as \(a_i,b_i\) for \(0\le i<t\) with \(\pi(a_i)=b_i\), and fixed symbols as \(z_h\) for \(0\le h<f\). Write \(u\to v\) for the selected length-two word \((u,v)\). All operations below create a **set** of distinct directed edges.

## Proof
**1. Upper bounds.** Exactly \(f^2\) ordered pairs are fixed by the coordinatewise involution, namely those with both symbols fixed. They cannot occur. Every other ordered pair belongs to a two-element orbit \(\{(x,y),(\pi(x),\pi(y))\}\), at most one member of which can occur. Therefore any admissible cycle has length at most \((q^2-f^2)/2\).

When \(f=0\), set \(P=\{a_0,\ldots,a_{t-1}\}\) and \(N=\{b_0,\ldots,b_{t-1}\}\). There are exactly \(t^2\) involution-pair orbits of ordered edges crossing between \(P\) and \(N\): in each orbit one edge goes \(P\to N\), the other goes \(N\to P\). If the orbit bound were attained, one edge from every such orbit would occur. The difference between the numbers of \(P\to N\) and \(N\to P\) edges would then be a sum of \(t^2\) numbers, each equal to \(+1\) or \(-1\). In every directed closed walk this difference is zero. When \(t\) is odd, \(t^2\) is odd, an impossibility. Thus this case loses at least one edge.

**2. Explicit graph on moving symbols.** Select the loop \(a_i\to a_i\) for every \(i\). Select \(a_i\to b_i\) for every \(i\), except omit the edge for \(i=0\) if \(t\) is odd. Pair the block indices by
\[
\mathcal M=\begin{cases}
\{(0,1),(2,3),\ldots,(t-2,t-1)\},&t\text{ even},\\
\{(1,2),(3,4),\ldots,(t-2,t-1)\},&t\text{ odd}.
\end{cases}
\]
For each \(0\le i<j<t\), select **exactly four** additional edges by the following rule.

If \((i,j)\in\mathcal M\), select
\[
(a_i,a_j),\quad (b_i,a_j),\quad (a_j,a_i),\quad (b_j,a_i).
\]
If \(t\) is odd and \((i,j)=(0,1)\), select
\[
(a_0,a_1),\quad(b_0,a_1),\quad(a_1,a_0),\quad(a_1,b_0).
\]
For every other pair \((i,j)\), select
\[
(a_i,a_j),\quad(a_i,b_j),\quad(a_j,a_i),\quad(b_j,a_i).
\]
Each four-edge choice contains exactly one representative from each of the four two-element involution orbits on ordered edges between the two blocks \(\{a_i,b_i\}\) and \(\{a_j,b_j\}\). Each loop \((a_i,a_i)\) selects one from the paired loops, and each selected internal nonloop \((a_i,b_i)\) selects one from \(\{(a_i,b_i),(b_i,a_i)\}\). Thus the selected moving-symbol graph avoids complemented pairs and exhausts all their orbits, apart from the one deliberately omitted internal nonloop orbit when \(t\) is odd.

The last two four-edge configurations have zero in-degree minus out-degree at **each** of their four vertices. The first configuration contributes \(\operatorname{outdeg}-\operatorname{indeg}=-1\) at \(a_i,a_j\) and \(+1\) at \(b_i,b_j\); it exactly cancels the \(+1,-1\) contributions of the two selected internal edges \(a_i\to b_i\), \(a_j\to b_j\). Loops are balanced. The unmatched block \(i=0\) in the odd case has no internal nonloop edge and is balanced as well. Consequently all selected moving vertices are balanced.

Every four-edge configuration includes both directions between \(a_i\) and \(a_j\), so all representatives \(a_i\) belong to one strongly connected subgraph (unless there is only one representative, when the assertion is immediate). Each \(b_i\) in a matched block lies on a directed four-cycle
\[
a_i\to b_i\to a_j\to b_j\to a_i
\]
with its matched partner. For odd \(t\ge3\), the special \((0,1)\) configuration connects the remaining \(b_0\) bidirectionally to \(a_1\). For \(t=1\), the moving-symbol graph contains only the loop at \(a_0\); its isolated, inactive symbol \(b_0\) causes no difficulty. Thus the graph on its active vertices is strongly connected and balanced.

**3. Adding fixed symbols.** If \(f\ge1\), first use the fixed symbol \(z_0\). For each \(i\), except \(i=0\) with odd \(t\), insert the two-edge circuit
\[
z_0\to a_i\to z_0.
\]
If \(t\) is odd, also insert the formerly missing internal edge \(a_0\to b_0\), together with
\[
z_0\to a_0,\qquad b_0\to z_0.
\]
These three edges form the circuit \(z_0\to a_0\to b_0\to z_0\). For every further fixed symbol \(z_h\), insert \(z_h\to a_i\) and \(a_i\to z_h\) for every \(i\). No fixed-to-fixed edges are allowed because these are fixed by the coordinatewise involution.

For each fixed symbol and each moving block, the construction selects precisely one of each of the two edge-orbits \(\{(z_h,a_i),(z_h,b_i)\}\) and \(\{(a_i,z_h),(b_i,z_h)\}\). The inserted two- and three-edge circuits preserve balance, and connect all added vertices to the original component. In the exceptional base case \(t=1\), the three-edge circuit also activates and connects \(b_0\). The result is therefore a connected balanced directed graph with one edge from **every** allowable orbit.

**4. Realization.** A finite directed graph whose active vertices are strongly connected and balanced has an Euler circuit. Read its vertices cyclically to obtain a word whose consecutive two-windows are exactly the graph's distinct edges. The constructed graph has
\[
\frac{(2t)^2}{2}-1=2t^2-1
\]
edges if \(f=0\) and \(t\) is odd, and \((q^2-f^2)/2\) edges otherwise. The upper bounds of Step 1 match these constructions. This proves the theorem. \(\square\)

## Verification
Run `python3 verify.py` using Python 3 standard library. The code reconstructs the graph, checks one-per-orbit selection and orbit omissions, computes every vertex's in-degree and out-degree, checks strong connectivity, constructs an Euler circuit by Hierholzer's algorithm, and independently compares the resulting cyclic word's two-window multiset with the edge set. These checks passed for all \(135\) parameter pairs \(1\le t\le15\), \(0\le f\le8\). Separate brute-force enumeration checked exact optima for \((t,f)=(1,0),(1,1),(2,0),(1,2)\). The accompanying `verification_output.txt` is the reproducible console output.

Finite computation is a cross-check, **not** an exhaustive verification of all parameter pairs. The general claim follows from the constructive proof and parity argument above.

## Relationship to prior work
Mitchell and Wild introduced negative-avoiding sequences for the coordinatewise map \(x\mapsto -x\) on \(\mathbb Z_q\), proved their elementary orbit bound, and constructed maximal sequences of all spans for \(q\ge3\). Their map has exactly one fixed symbol for odd \(q\) and exactly two for even \(q\); because involutions with the same orbit structure are conjugate by alphabet relabeling, their span-two theorems already cover **our cases \(f=1\) and \(f=2\)**. They explicitly ask about arbitrary involutions on the alphabet in their concluding section and note the exceptional binary complement case at span two. Our result provides the complete span-two answer in orbit-type parameters, including the new fixed-point-free odd-\(t\) parity obstruction and arbitrarily many fixed symbols. Those portions do not follow from the stated modular-negation constructions.

Earlier works on orientable and unoriented de Bruijn sequences pair a window with its **reversal**, rather than its image under an arbitrary coordinatewise alphabet involution. Their reversed-pair bounds and constructions do not imply this result. None of the inspected primary sources supplies the present all-involution span-two classification. Searches are not proof that unindexed equivalent work does not exist.

## Limitations
No classification or enumeration of all extremal cycles is claimed, and the theorem does not address spans greater than two. The case of an identity involution is excluded because it admits no nonempty cycle. Existing modular-negation instances \(f=1,2\) are acknowledged as previously covered. A differently formulated or unindexed theorem for general involutions remains an originality risk. No independent scientific audit has been performed.

## References
1. C. J. Mitchell and P. R. Wild, *Negative Avoiding Sequences*, arXiv:2603.25286, first public version 2026-03-26; especially Definitions 1.3 and 8.1, Theorems 3.2, 4.1, 6.2, 6.4, and Section 8. https://arxiv.org/html/2603.25286
2. A. Alhakim, C. J. Mitchell, J. Szmidt and P. R. Wild, *Orientable sequences over non-binary alphabets*, Cryptography and Communications 16 (2024), 1309–1326; especially Definition 3.3 and the period-bound discussion. https://doi.org/10.1007/s12095-024-00742-x
3. *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480; especially Sections 2–4 on reversal-orbit windows. https://arxiv.org/html/1608.08480v1
