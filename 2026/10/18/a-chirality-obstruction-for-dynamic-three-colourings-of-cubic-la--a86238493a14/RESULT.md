# A chirality obstruction for dynamic three-colourings of cubic ladders

## Finding
For every integer \(n\ge3\), let \(P_n=C_n\mathbin{\square}K_2\) be the circular prism, and let \(M_n\) be the \(n\)-rung Möbius ladder obtained by joining two rows of \(n\) vertices in parallel, with the final-to-first row edges crossed. Equivalently \(M_n=C_{2n}(1,n)\), using the circulant convention. Write \(\chi_2\) for the minimum number of colours in a proper vertex colouring in which each vertex sees at least two different neighbour colours.

Then
\[
\chi_2(P_n)=\begin{cases}3,&3\mid n,\\4,&3\nmid n,\end{cases}
\qquad\chi_2(M_n)=4\quad(n\ge3).
\]
More precisely, with a fixed palette of **three named colours**, the number of two-dynamic colourings of \(P_n\) is exactly \(12\) when \(3\mid n\) and zero otherwise; the number on \(M_n\) is always zero. Whenever a three-colour solution exists, its ordered rung colours follow one of two period-three orientations. The Möbius closing twist exchanges those orientations and rules out every solution.

## Assumptions and scope
All graphs are finite and simple, and \(n\ge3\). In column \(i\), write \(s_i=(a_i,b_i)\) for the colours of the two rung endpoints, indexed \(0\le i<n\). Rung colours differ; consecutive upper colours and consecutive lower colours differ. On \(P_n\), the boundary is periodic \(s_n=s_0\); on \(M_n\), it is twisted \(s_n=J(s_0)\), where \(J(a,b)=(b,a)\). The same boundary rule extends the sequence bi-infinitely, allowing all neighbour conditions to be read from adjacent triples. Every vertex has degree three. A named three-colour solution may use any colours from \(\{0,1,2\}\); in fact it must use all three.

## Proof
**Forced orientation lemma.** Suppose three colours suffice. Fix any column \(s_i=(x,y)\), where \(x\ne y\), and let \(z\) be the remaining colour. Properness leaves exactly three possibilities for the next column:
\[
 s_{i+1}\in\{(y,x),(y,z),(z,x)\}.
\]
The swapped possibility \((y,x)\) is impossible: at the next column, both the preceding upper neighbour and the rung neighbour of the upper vertex have colour \(x\), so its following upper neighbour must have colour \(z\). The corresponding lower vertex likewise forces its following lower neighbour to have colour \(z\). The following rung would have equal endpoint colours. If instead \(s_{i+1}=(y,z)\), the lower dynamic condition forces the following lower colour to be \(x\); properness then uniquely forces \(s_{i+2}=(z,x)\). Symmetrically, \(s_{i+1}=(z,x)\) forces \(s_{i+2}=(y,z)\). Hence every legal sequence has, for some ordering of the three colours, one of the two forms
\[
 (x,y),(y,z),(z,x),(x,y),\ldots
 \quad\text{or}\quad
 (x,y),(z,x),(y,z),(x,y),\ldots .
\]
These forms each have exact period three, and their cycles never contain the reversed pair \((y,x)\). A periodic closure requires \(3\mid n\). A twisted closure requires \(s_n=(y,x)\), which never occurs. This proves every stated lower bound, and proves the absence of named three-colour solutions on the Möbius ladder and on non-divisible prisms.

If \(3\mid n\), the first period-three orientation gives a valid three-colour prism colouring; so does the reverse orientation. There are precisely six choices for the initial ordered distinct pair and two choices for the orientation. The orientations are disjoint, giving exactly \(6\cdot2=12\) named solutions.

**Explicit four-colour constructions.** Set \(B_i=(i\bmod3,(i+1)\bmod3)\), using colours \(0,1,2,3\). A juxtaposition of columns is in increasing order of \(i\). The following formulae provide all remaining upper bounds:

| Graph / residue | Ordered columns |
| --- | --- |
| \(P_n\), \(n\equiv0\pmod3\) | \(B_0,\ldots,B_{n-1}\) (three colours) |
| \(P_n\) or \(M_n\), \(n\equiv1\pmod3\) | \(B_0,\ldots,B_{n-3},(0,3),(3,2)\) |
| \(P_n\) or \(M_n\), \(n\equiv2\pmod3\) | \(B_0,\ldots,B_{n-2},(2,3)\) |
| \(M_n\), \(n\equiv0\pmod3\) | \(B_0,\ldots,B_{n-2},(0,3)\) |

Within the period-three segment, all horizontal edges are proper and each vertex sees both alternative colours through its horizontal neighbours. For the at most three columns abutting a modified tail or the cyclic/twisted seam, substituting the displayed pairs gives different colours at each end of every edge and at least two colours among the three neighbours of each vertex. The verification only depends on the displayed residue case, not on the number of repeated period-three blocks. This may also be reproduced using the included standalone checker, which explicitly constructs every adjacency and performs the direct local tests. Together with the lower bounds, this proves both chromatic formulae.

## Verification
Run `python3 check.py` in a directory containing this file and the supplied `check.py`. The checker recomputes the complete three-colour state-pair transition relation: it has 18 admissible states and 12 transitions, each nonempty successor component is a directed three-cycle, and no state reaches its twisted boundary image. It tests the displayed explicit colouring recipes for both graph families for \(3\le n\le600\) (1196 graphs) and separately enumerates all named three-colour assignments by column-state backtracking for \(3\le n\le15\) (26 graph instances). Both routes agreed exactly with the theorem. These finite experiments are not used in lieu of the preceding general proof.

## Relationship to prior work
Gutierrez and Ugarte (2026) analyze the dynamic-colouring hierarchy for cubic and four-regular graphs and determine the hierarchy on the unrelated circulant family \(C_p(1,3)\); their general definitions are used here. Earlier general work on dynamic colouring already guarantees that any subcubic graph other than the five-cycle is two-dynamically four-colourable: the four-colour *upper bound by itself is not claimed as new*. The contribution here is the forced two-orientation classification, the twist obstruction, and the exact named three-colouring count and resulting sharp prism/Möbius dichotomy.

Lisitsyna (2013) studies perfect (equitable) three-colourings of prisms and Möbius ladders. A perfect colouring requires fixed neighbour-colour multiplicities throughout each colour class, a restriction not imposed by two-dynamic colouring. Thus its existence-parameter classification does not by itself settle the current local-surjectivity problem. The accessible record did not provide the complete article for a definitive comparison, so a possible stronger unobserved result remains a bibliographic limitation.

## Limitations
The result is confined to two-dynamic vertex colouring of these two cubic ladder closures, not to list, online, or three-dynamic colouring, and not to general twisted Cartesian products. Its novelty judgment is subject to the inaccessible full text of the 2013 perfect-colourings article and to potential unindexed equivalent work. The four-colour upper bound is previously known in much greater generality.

## References
1. J. Gutierrez and G. Ugarte, *Dynamic Coloring and Graph Squares of Regular Graphs*, arXiv:2610.09565v1 (first public 2026-10-07), https://arxiv.org/html/2610.09565v1.
2. M. A. Lisitsyna, *Perfect 3-colorings of prism and Möbius ladder graphs*, Journal of Applied and Industrial Mathematics 7 (2013), 215–220. DOI:10.1134/S1990478913020105.
3. *Upper Bounds of Dynamic Chromatic Number*, Ars Combinatoria 68 (2003), 193–201, https://combinatorialpress.com/ars-articles/volume-068-ars-articles/upper-bounds-of-dynamic-chromatic-number/.
4. Y. Chen, S. Fan, H.-J. Lai, H. Song and L. Sun, *On dynamic coloring for planar graphs and graphs of higher genus*, Discrete Applied Mathematics 160 (2012), 1064–1071, DOI:10.1016/j.dam.2012.01.012.
