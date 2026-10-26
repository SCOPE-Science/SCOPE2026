# Strong odd colorings of ladder graphs are exactly square colorings

## Finding

**Theorem.** Let \(n\ge 2\), and let \(L_n=P_2\square P_n\) be the two-row, \(n\)-rung ladder. A coloring of \(L_n\) is strong odd if and only if it is a proper coloring of the square graph \(L_n^2\). For every nonnegative integer \(k\), the number of strong odd colorings using a labeled palette of \(k\) available colors (with unused colors permitted) is

\[
P_n(k)=k(k-1)(k-2)(k-3)(k^2-7k+13)^{n-2}.
\]

In particular, \(\chi_{\mathrm{so}}(L_n)=4\) for all \(n\ge 2\). With a fixed four-color palette there are exactly \(24\) strong odd colorings, and these constitute a single color-permutation orbit. The forced four-color pattern repeats after four rungs. The one-rung graph \(L_1=K_2\) is excluded from the formula and has \(k(k-1)\) strong odd colorings.

## Assumptions and scope

Graphs are finite, simple, undirected. The vertices of \(L_n\) are \(a_i,b_i\) for \(1\le i\le n\); the edges are rungs \(a_ib_i\) and rails \(a_ia_{i+1}\), \(b_ib_{i+1}\) for \(1\le i<n\). The square \(L_n^2\) joins pairs at distance one or two in \(L_n\).

For an integer \(k\ge0\), a \(k\)-palette strong odd coloring is a proper map \(c:V(L_n)\to\{1,\dots,k\}\) such that, for every vertex \(v\), every color appearing in the open neighborhood \(N(v)\) occurs there an odd number of times. The palette need not be used surjectively. A proper coloring of \(L_n^2\) is equivalently a proper coloring of \(L_n\) in which the neighbors of each vertex have pairwise distinct colors.

## Proof

**First-rung rigidity.** Each vertex in the first rung has degree two when \(n\ge2\). At \(a_1\), the two neighbors \(b_1\) and \(a_2\) have different colors: two equal occurrences would violate the strong odd condition. Likewise \(a_1\) and \(b_2\) have different colors because they are neighbors of \(b_1\). Properness supplies the remaining edges of the four-cycle \(a_1b_1b_2a_2a_1\). Thus the four vertices on the first two rungs have four pairwise distinct colors.

**Propagation.** Suppose successive rungs \(i-1\) and \(i\), where \(2\le i<n\), use four distinct colors. The three neighbors of \(a_i\) are \(a_{i-1},b_i,a_{i+1}\). Their first two colors are distinct by the induction hypothesis. For a multiset of three colors, the condition that every positive color multiplicity be odd permits either three distinct colors or three copies of the same color, but forbids a multiplicity profile \(2+1\). Since the first two colors differ, the third color must differ from both. Therefore \(c(a_{i+1})\) differs from \(c(a_{i-1})\) and \(c(b_i)\). Similarly, applying the condition at \(b_i\), the color \(c(b_{i+1})\) differs from \(c(b_{i-1})\) and \(c(a_i)\). Properness on rails and the new rung supplies \(c(a_{i+1})\ne c(a_i)\), \(c(b_{i+1})\ne c(b_i)\), and \(c(a_{i+1})\ne c(b_{i+1})\). Consequently the four vertices on rungs \(i,i+1\) are pairwise differently colored, completing the induction.

**Equivalence.** The edges of \(L_n^2\) are exactly the original edges together with pairs of vertices with a common neighbor. Every such pair is assigned distinct colors: this follows from the initial degree-two condition and, for all interior degree-three vertices, the propagation step just proved. Thus every strong odd coloring is a proper square coloring. Conversely, in a proper square coloring the neighbors of each vertex have distinct colors, and each color that appears there occurs exactly once; hence the coloring is strong odd.

**Enumeration.** The first two rungs form a four-clique in \(L_n^2\), and therefore may be colored in exactly \(k(k-1)(k-2)(k-3)\) ways. Given two successive rungs whose colors are \((A,B)\) and \((C,D)\), where these four are distinct, write the next rung as \((E,F)\). The established square constraints say

\[
E\notin\{A,C,D\},\qquad F\notin\{B,C,D\},\qquad E\ne F.
\]

There are \(k-3\) choices for each of \(E,F\) before the last inequality. Their allowed color sets have intersection of size \(k-4\), so the number of next rungs is

\[
(k-3)^2-(k-4)=k^2-7k+13.
\]

It is independent of the history and maintains the four-distinct-color induction hypothesis for the last two rungs. Multiplication over the remaining \(n-2\) rungs proves the formula whenever \(k\ge4\); for \(k<4\), the mandatory four-clique makes the count zero and the displayed polynomial also vanishes. Setting \(k=4\) gives exactly four colors and a single continuation from each initial four-color assignment: \(E=B\) and \(F=A\). The rungs are therefore successively \((A,B),(C,D),(B,A),(D,C),(A,B),\dots\), establishing the four-rung periodicity, the exact count \(4!=24\), and the strong odd chromatic number \(4\). \(\square\)

## Verification

A standalone program, `verify.py`, independently constructs ladder adjacency and directly tests the original strong odd condition against the square-coloring condition for nineteen ladder/palette cases, inspecting \(1{,}647{,}568\) complete color assignments. It also uses a separate neighborhood-parity transfer recurrence for all \(2\le n\le16\) and \(2\le k\le8\), yielding \(105\) independent counts agreeing with the formula. The recorded command is `python verify.py`; its captured output is `verification_output.txt`. These finite checks are corroborative; the unrestricted theorem follows from the proof above.

## Relationship to prior work

Kwon and Park introduced strong odd coloring and observed that square colorings are strong odd. They proved equality of the respective chromatic *numbers* for claw-free graphs and obtained sparse-graph bounds. The ladder \(L_n\) contains an induced claw for \(n\ge3\), so that claw-free theorem does not establish the present equivalence, let alone equality of *every palette's coloring sets* or the exact polynomial. Caro, Petruševski, Škrekovski, and Tuza proved a general submultiplicative bound for strong odd coloring of Cartesian products and studied trees and unicyclic graphs; that bound neither forces four colors for all ladders nor counts colorings. The ordinary chromatic polynomial of a ladder is different: it enumerates proper colorings of \(L_n\), not strong odd colorings or proper colorings of \(L_n^2\). The present contribution is the explicit rigidity and complete labeled-palette enumeration for a natural clawed subcubic family.

## Limitations

The theorem applies to two-row, open-ended ladders only; it does not assert the same equivalence for wider rectangular grids or cyclic ladders. Arithmetic counts labeled palette assignments, not isomorphism classes of colors. A related 2025 study on odd and strong odd colorings was located bibliographically, but its complete text was not inspected, leaving a residual priority risk. Novelty is assessed against inspected accessible literature and research records, not independently certified. No independent mathematical audit has been performed.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653v1 (first public version 22 January 2024). https://arxiv.org/html/2401.11653v1
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336v1 (3 October 2024). https://arxiv.org/html/2410.02336v1
3. H. S. M. Weerabaddana and A. A. I. Perera, *Chromatic polynomial of ladder graph*, RESCON 2022, University of Peradeniya, 28 October 2022. https://ir.lib.pdn.ac.lk/items/20301f6c-6c73-4218-af2b-7a17c41d202b
