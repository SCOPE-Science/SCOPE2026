# Parity-refined comparison shattering of even permutations

## Finding

Let \(n\ge1\), and let \(\mathcal E_n\) be the Boolean concept class indexed by the even permutations of the labels \([n]=\{1,\dots,n\}\). On a query \(\{a,b\}\) with \(a<b\), the concept associated with a permutation word answers one if \(a\) appears before \(b\), and zero otherwise. A query support \(S\subseteq\binom{[n]}2\) is **shattered** if every assignment of its pair-comparison outcomes is realized by an even permutation.

**Parity-refined comparison-shattering theorem.** For every \(n\ge2\), a support \(S\) is shattered by \(\mathcal E_n\) if and only if the undirected graph \(([n],S)\) is a forest and either:

1. \(S\) is not the edge set of a spanning Hamiltonian path; or
2. \(S\) is a spanning Hamiltonian path and a traversal of that path lists the vertices in an even permutation in **both** directions.

In the second case both directions are even exactly when \(n\equiv0,1\pmod4\) and the permutation given by either traversal is even. In particular,
\[
\operatorname{VCdim}(\mathcal E_n)=
\begin{cases}
0,&n=1,2,\\
1,&n=3,\\
n-1,&n\ge4.
\end{cases}
\]
For \(n\ge4\), the exact number of maximum-size shattered supports is
\[
T_n=\begin{cases}
n^{n-2}-n!/4,& n\equiv0,1\pmod4,\\
n^{n-2}-n!/2,& n\equiv2,3\pmod4.
\end{cases}
\]

The exact adaptive (Littlestone) dimensions for \(1\le n\le7\) are, in increasing order of \(n\),
\[
\bigl(\operatorname{Ldim}(\mathcal E_n)\bigr)_{n=1}^{7}
=(0,0,1,3,5,8,10).
\]
The first failure of the cardinality upper bound is \(n=7\): there are \(7!/2=2520\) concepts, but \(\operatorname{Ldim}(\mathcal E_7)=10<11=\lfloor\log_2(2520)\rfloor\). This finite adaptive statement is established by the complete executable certificate and exact search described below, not by an extrapolation from a few examples.

## Assumptions and scope

All permutations here are linear-order words on labeled elements, not mappings evaluated on inputs. Evenness means an even inversion count of the word relative to the fixed natural label order. A binary query on \(\{a,b\}\), with \(a<b\), reports whether \(a\) precedes \(b\). The finite set of all such queries is the instance domain. Repeating a query in a decision tree is permitted by the definition but never useful along a branch.

A complete depth-\(d\) comparison tree is shattered when each of its \(2^d\) root-to-leaf answer strings is consistent with at least one concept. Its maximum depth is the Littlestone dimension. A support is VC-shattered when every static assignment to its distinct queries is consistent. The classification and count hold for every \(n\) in the stated ranges, whereas the adaptive table is only for \(n\le7\). The empty support is shattered by every nonempty concept class.

## Proof

**1. Forest obstruction.** If \(S\) contains a graph cycle, orient the comparison queries cyclically around it. No total order realizes that assignment. Thus a shattered support must be a forest. Conversely, every assignment on an undirected forest is an acyclic directed graph and therefore has at least one topological sorting.

**2. Parity of linear extensions.** If a finite partial order admits two different linear extensions, then it admits one extension of each parity. Indeed, the graph of linear extensions is connected under swapping adjacent incomparable elements: to transform an extension into a prescribed target extension, successively move its next required element left past only elements incomparable with it. A connected graph with more than one vertex has an edge; each such adjacent swap reverses permutation parity.

An orientation of an undirected forest has a unique topological ordering if and only if its directed edges include the successive pairs of a directed Hamiltonian path. For necessity, if the unique ordering is \(v_1,\dots,v_n\), then each consecutive pair \(v_i,v_{i+1}\) must be a directed edge: otherwise that pair is incomparable (an intervening directed path would require an intermediate element between consecutive vertices), and swapping the pair gives another ordering. These \(n-1\) edges use every vertex; because a forest has at most \(n-1\) edges, its entire edge set is this path. Sufficiency is immediate.

Hence, if \(S\) is a forest other than a spanning path, every assignment has at least two linear extensions and therefore an even one. If \(S\) is a spanning path, precisely the two consistently directed path orientations have unique linear extensions, namely the two path traversals. All other orientations have even extensions. Thus this path is shattered exactly when both traversal permutations are even. Reversal changes permutation parity by \((-1)^{\binom n2}\), giving the stated modulo-four condition. This establishes the complete support classification.

**3. Maximal supports and their count.** A forest contains at most \(n-1\) edges. If \(n\ge4\), a spanning star is not a path and so is shattered, proving \(\operatorname{VCdim}=n-1\). For \(n=1,2,3\), inspect the empty graph and the available single pairs: the unique even permutation at \(n=1,2\) shatters only the empty support; the three even permutations at \(n=3\) shatter every single pair but no spanning two-edge path.

There are \(n^{n-2}\) labeled spanning trees (Cayley's formula), of which \(n!/2\) are Hamiltonian paths. When \(n\equiv2,3\pmod4\), no spanning path is shattered. In the other two congruence classes, exactly half of the \(n!/2\) paths have even traversal parity: swapping any fixed pair of labels maps even-traversal paths bijectively to odd-traversal paths. Subtracting the unshattered paths gives the displayed formula for \(T_n\).

**4. Adaptive finite-range calculation.** For a nonempty subset \(H\subseteq\mathcal E_n\), and integer \(d\ge0\), define \(W(H,d)\) to mean that \(H\) shatters a complete depth-\(d\) tree. Then \(W(H,0)\) holds, and for \(d>0\)
\[
W(H,d)\iff \bigvee_{q\in\binom{[n]}2}
\bigl(W(H_{q,0},d-1)\wedge W(H_{q,1},d-1)\bigr),
\]
where \(H_{q,b}\) contains the concepts returning answer \(b\) at \(q\). A branch having fewer than \(2^{d-1}\) distinct concepts cannot shatter depth \(d-1\), so those branches can safely be skipped. This equivalence is an exact finite recursion, proved directly by taking the root query of a shattered tree and conversely grafting two shattered child trees.

The standalone program `verify_even_orders.py` enumerates all even permutation words, encodes each query's concept subset as an integer bit mask, memoizes the exact recurrence, and verifies that the depths \((0,0,1,3,5,8,10)\) are attainable while their successors are not. The supplied `trees.json` contains an explicit full binary query tree for each positive depth, with an even permutation witness at every leaf. Its paths are checked from the original permutation words, rather than accepted as an algorithm log. At \(n=7\), testing nonattainability of depth eleven evaluates 121,279 distinct memoized subset/depth states (including all lower-depth calls); the finite upper claim therefore depends on the stated exhaustive recurrence and executable computation. The witness trees contain 1,317 internal nodes and 1,322 leaves in total. For \(n\le6\), the attained dimension also equals the simple upper bound \(\lfloor\log_2(n!/2)\rfloor\) for \(n\ge2\).

## Verification

From the directory containing the files, run `python3 verify_even_orders.py trees.json`. It recomputes every adaptive value and immediate next-depth impossibility for \(1\le n\le7\), checks all decision-tree branches and leaf witnesses, and independently enumerates all supports of size at most \(n-1\) for \(2\le n\le6\). The latter finite check compares each support's actual set of comparison traces with the structural characterization, and reproduces \(T_4=10\), \(T_5=95\), \(T_6=936\). For deterministic regeneration of witnesses run `python3 generate_even_trees.py` in the same directory, then rerun the verifier. The included `even_order_check_output.txt` records one successful verification execution.

## Relationship to prior work

Maass and Turán established the forest criterion for VC shattering by **all** total orders, not by parity-constrained total orders. The present theorem distinguishes parity-sensitive Hamiltonian path supports, counts maximal supports, and studies the alternating-group subclass adaptively. Walker's general tree-dimension paper supplies the learning-theoretic context and the standard Littlestone definition but contains no permutation-parity characterization. Raz studied a different permutation VC-dimension based on realizing every relative order of selected labels, rather than independent binary query labels. Berendsohn, Kozma and Marx developed constraint-based permutation-pattern algorithms; their permutation object is related, but their results do not determine parity-constrained comparison shattering. Unrestricted total orders form a superfamily; consequently, their dimensions give upper bounds on this parity-restricted subclass, not the exact values or support classification.

## Limitations

No exact Littlestone dimension is asserted for \(n\ge8\). The finite upper calculation is not an infinite proof. External priority cannot be exhaustively ruled out by database searches and the inspected literature; a more closely focused treatment of alternating-group comparison queries may exist. No independent scientific audit has been performed. The maximum-support count applies to labeled query supports, not graph-isomorphism types. The ambient ordering of labels is necessary for the parity-sensitive path condition.

## References

1. W. Maass and G. Turán, *Lower Bound Methods and Separation Results for On-Line Learning Models*, Machine Learning **9** (1992), 107–145, DOI 10.1023/A:1022637031594; especially the comparison-query linear-order VC criterion on p. 139. Accessible author PDF: https://igi-web.tugraz.at/PDF/54.pdf.
2. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first posted March 23, 2022; specifically Sections 1.1 and its Littlestone definition.
3. R. Raz, *VC-Dimension of Sets of Permutations*, Combinatorica **20** (2000), 241–255, DOI 10.1007/s004930070023. The paper uses a different shattering definition.
4. B. A. Berendsohn, L. Kozma and D. Marx, *Finding and Counting Permutations via CSPs*, IPEC 2019, DOI 10.4230/LIPIcs.IPEC.2019.1.
