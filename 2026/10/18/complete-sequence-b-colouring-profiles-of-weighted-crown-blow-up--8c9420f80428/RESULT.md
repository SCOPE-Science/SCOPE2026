# Complete sequence \(b\)-colouring profiles of weighted crown blow-ups

## Finding
Let \(r\ge3\). Partition two disjoint vertex sets into nonempty blocks \(A_1,\ldots,A_r\) and \(B_1,\ldots,B_r\), with \(|A_i|=a_i\ge1\) and \(|B_i|=b_i\ge1\). Form the simple graph \(G(\mathbf a,\mathbf b)\) by joining every vertex in \(A_i\) to every vertex in \(B_j\) exactly when \(i\ne j\), with no other edges. Equivalently, delete the disjoint biclique edge blocks \(A_i\times B_i\) from the complete bipartite graph on \(A=\bigcup_iA_i\) and \(B=\bigcup_iB_i\). This is a connected false-twin blow-up of the crown graph.

A color-dominating vertex (CDV) is a vertex whose closed neighbourhood meets every colour class in a proper colouring. A \(b\)-colouring is a proper colouring in which each colour class has at least one CDV. **Every \(b\)-colouring of \(G(\mathbf a,\mathbf b)\) is, up to permutation of colour names, exactly one of the following two colourings:**

1. The two-colour bipartition colouring with colour classes \(A\) and \(B\).
2. The \(r\)-colour paired-block colouring with colour classes \(A_i\cup B_i\) for \(1\le i\le r\).

**Every vertex is a CDV in either colouring.** Write \(A_*=\sum_i a_i\), \(B_*=\sum_i b_i\), and \(w_i=a_i+b_i\). Thus the two possible sorted **exact CDV-multiplicity profiles** are
\[
\bigl(\max\{A_*,B_*\},\min\{A_*,B_*\}\bigr)\quad\text{and}\quad(w_1,\ldots,w_r)^\downarrow.
\]
There are precisely two named \(b\)-colourings with two colours and precisely \(r!\) named \(b\)-colourings with \(r\) colours; there are none with any other number of colours.

For a nonincreasing positive finite sequence \(S=(s_1,\ldots,s_k)\), realization in the sense of Jakovac--Lang (each colour class requires at least the corresponding number of CDVs) holds **if and only if** precisely one of these tests is satisfied:
\[
\begin{aligned}
&k=2,\quad s_1\le\max\{A_*,B_*\},\quad s_2\le\min\{A_*,B_*\};\\
&\text{or}\\
&k=r,\quad s_j\le w_j^\downarrow\quad\text{for each }1\le j\le r.
\end{aligned}
\]
For any infinite positive nonincreasing sequence the complete \(S\)-spectrum is consequently a subset of \(\{2,r\}\), containing exactly those lengths that pass the corresponding tests.

Conversely, **every prescribed list of integers** \(w_1,\ldots,w_r\ge2\) occurs as the exact \(r\)-colour CDV profile within this connected graph family: set \(a_i=1\) and \(b_i=w_i-1\). In particular, for \(r\ge4\), every such graph realizes \((2,2,\ldots)\) with exactly two or \(r\) colours and with none of the intervening lengths. The unweighted crown-graph two-point phenomenon itself was previously reported; the present classification determines all block-weighted colourings and sequences.

## Assumptions and scope
All graphs are finite, simple, undirected; the two sides and their \(r\) block pairings are fixed. Every block is nonempty, \(r\ge3\), and every vertex must receive exactly one colour. The palette is named when counting colourings. The sorted notation \((w_i)^\downarrow\) means rearrangement into nonincreasing order. The distinction \(r\ge3\) is necessary: at \(r=2\) the graph is disconnected and the classification need not hold. For \(r=3\), the two admissible numbers of colours are consecutive, while for \(r\ge4\) the gap is nonempty.

## Proof
**Step 1: properly used mixed colours are confined to a block.** Call a colour *mixed* if it occurs on both bipartition sides, and *side-only* otherwise. Suppose a mixed colour occurs on \(A_i\) and \(B_j\). Properness forces \(i=j\), since every cross-block \(A_i B_j\) edge is present when \(i\ne j\). The presence of this colour on both \(A_i\) and \(B_i\) then excludes its occurrence on any other block, since all such vertices have an edge to at least one of these two classes. Hence a mixed colour is supported entirely inside one paired block \(A_i\cup B_i\).

**Step 2: the number of side-only colours is severely restricted.** Two distinct colours supported only on the \(A\)-side cannot simultaneously occur in a \(b\)-colouring: no vertex of either colour has a neighbour of the other, so neither colour has a CDV. The same holds on the \(B\)-side. Thus there is at most one \(A\)-only colour and at most one \(B\)-only colour. Moreover, if both are used, no mixed colour can have a CDV: any of its vertices on \(A\) misses the \(A\)-only colour, and any on \(B\) misses the \(B\)-only colour. Therefore, a \(b\)-colouring having a mixed colour has at most one side-only colour in total.

**Step 3: a mixed colour excludes even one side-only colour.** Suppose an \(A\)-only colour and at least one mixed colour occur, with no \(B\)-only colour. Every vertex on the \(B\)-side must be coloured by a mixed colour, and a mixed colour used at \(B_i\) necessarily belongs entirely to block \(i\). Thus, for each \(i\), a mixed colour exists inside \(A_i\cup B_i\). An \(A\)-only vertex \(v\in A_i\) cannot see that block's mixed colour: \(v\) has no neighbour in \(A_i\cup B_i\), and \(v\) does not itself carry the mixed colour. Therefore no \(A\)-only vertex can be a CDV, contradiction. The situation with one \(B\)-only colour is symmetric. Hence a \(b\)-colouring uses either **only side-only colours** or **only mixed colours**.

**Step 4: classify both cases.** With only side-only colours, Step 2 permits at most one colour on each side. Since both sides are nonempty and colours cannot be shared across sides without being mixed, each side is monochromatic and the two colours differ. With only mixed colours, each \(A_i\) and \(B_i\) must be coloured by the (necessarily present) mixed colour supported in block \(i\). Two different mixed colours supported in the same block cannot both have a CDV: there are no edges inside \(A_i\cup B_i\), so vertices of either would miss the other colour. Therefore exactly one mixed colour occurs per block, giving the stated \(r\)-colouring.

**Step 5: verify the CDVs and derive all sequence claims.** In the bipartition colouring every vertex has a neighbour on the opposite side because \(r\ge3\) and all blocks are nonempty. In the paired-block colouring every vertex in block \(i\) has neighbours of each other block's colour, since \(A_i\) is complete to \(B_j\) and \(B_i\) is complete to \(A_j\) for all \(j\ne i\). Thus every vertex is a CDV. The unique two possible profiles are therefore exactly the sizes of the displayed colour classes. Assigning the most stringent sequence requirement to the largest class is necessary and sufficient, yielding the coordinatewise inequalities. The named-colour enumeration follows by permuting \(2\) or \(r\) colours among distinct nonempty classes. Finally, choosing \(a_i=1\) and \(b_i=w_i-1\) realizes any \(r\)-profile with \(w_i\ge2\); both side sizes are at least \(r\), so \((2,2,\ldots)\) also passes the two-colour test. No other colour number is possible by Step 4. \(\square\)

## Verification
The accompanying `verification.py` constructs the graph independently from the block sizes, examines every named colouring for the listed ten small parameter cases and palette sizes two through one more than the block count, tests properness edge by edge, determines CDVs from closed neighbourhoods, and compares complete count-by-number-of-colours and exact CDV-multiplicity profiles to the theorem. Run from this directory: `python3 verification.py`. The recorded outcome was: `PASS 10 graph profiles; every named assignment for palette sizes 2 through r+1 checked`. This finite computation is only a check of the general proof, not a replacement for it.

## Relationship to prior work
Jakovac and Lang's *Sequence b-colorings in graphs* (September 8, 2026, arXiv:2609.08484v1), especially Definitions 2.1--2.2, introduces the CDV multiplicity requirements and investigates general realizability, cycles, girth-constrained regular graphs, and additional-CDV phenomena. The primary accessible PDF and its pertinent statements were inspected; it does not formulate the weighted crown-blow-up classification.

A published 2026 result titled *Two-point sequence \(b\)-spectrum of crown graphs* establishes the spectrum \(\{2,r\}\) for the unweighted crown graph and the constant sequence \((2,2,\ldots)\). This previously known special case is **not** claimed as new. The present theorem gives the entire \(b\)-colouring classification, arbitrary positive biclique block weights, the exact CDV profiles, and every realizable sequence for each weighted graph. Those stronger assertions are not a logical consequence of the unweighted special-case statement alone.

Gawel's 2024 work *Increasing the b-Chromatic Number of Complete Bipartites by Deleting Edges* treats an edge-deletion optimization of the classical \(b\)-chromatic number. The accessible abstract and opening portion do not supply the full sequence profile theorem. Its complete text was not inspected, so potential unrecognized stronger coverage remains a bibliographic risk.

## Limitations
This is a classification only for the stated positive block sizes and \(r\ge3\), not for arbitrary bipartite graphs or arbitrary edge deletions. The closed-form class rules prove mathematical correctness independently of the finite tests. A published unweighted crown special case already contains one of the corollaries, and the current bibliographic review cannot rule out equivalent results under different terminology or in inaccessible/unindexed full texts. Independent mathematical audit and definitive publication-priority verification have not been performed.

## References
1. M. Jakovac and M. S. Lang, *Sequence b-colorings in graphs*, arXiv:2609.08484v1 (first public September 8, 2026), https://arxiv.org/abs/2609.08484 .
2. *Two-point sequence b-spectrum of crown graphs*, published research record (2026); previously reports the unweighted constant-sequence two-point spectrum.
3. D. Gawel, *Increasing the b-Chromatic Number of Complete Bipartites by Deleting Edges*, DePaul Discoveries, 13(1), article 7 (2024), https://via.library.depaul.edu/depaul-disc/vol13/iss1/7/ .
