# A Boolean cell stratification and exact face polynomial for cyclic-tournament Hom complexes

## Finding
Let \(m\ge2\) be an integer, \(n=2m+1\), and let \(R_n\) be the cyclic tournament on \(\mathbb Z/n\mathbb Z\) with \(u\to v\) if and only if \(1\le (v-u)\bmod n\le m\). Let \(X_n=\operatorname{Hom}(\overrightarrow C_3,R_n)\) be the regular CW complex of directed multihomomorphisms from the oriented triangle. A cell is a triple \((A,B,C)\) of nonempty subsets with every arc in \(A\times B\), \(B\times C\), and \(C\times A\); its dimension is \(|A|+|B|+|C|-3\).

**Cell stratification theorem.** Every cell admits a **unique** anchor triple \((a,b,c)\), itself a directed cyclic triangle, and a unique subset of exactly \(m-1\) available augmentation positions. For each fixed anchor triple, its cells are therefore indexed by a Boolean lattice on \(m-1\) generators. This is a *set-theoretic partition of the face poset into Boolean intervals*; it is not asserted that each interval is a CW subcomplex or that the partition is a discrete-Morse matching.

In particular, the complete regular-CW face polynomial is
\[
\boxed{F_{X_n}(t)=\sum_{d\ge0}f_d t^d=n\binom{m+1}{2}(1+t)^{m-1}.}
\]
Thus \(X_n\) is a pure \((m-1)\)-dimensional regular CW complex, with
\[
f_d=n\binom{m+1}{2}\binom{m-1}{d}\quad(0\le d\le m-1),
\]
and no cells in other dimensions. The cyclic target-rotation group \(C_n\) acts freely on cells, and the quotient CW complex has exactly \(\binom{m+1}{2}\binom{m-1}{d}\) dimension-\(d\) cells. The ordinary Euler characteristic vanishes for \(m\ge2\).

## Assumptions and scope
All statements concern the **regular polyhedral CW cell structure** of directed Hom, rather than the simplices of its barycentric subdivision. An anchor is an ordered triple of the first occupied elements in the three cyclic consecutive blocks \(A,B,C\), read clockwise in that order; this depends on the cell but not on a choice of integer representatives. For \(n=3\) the Hom complex consists of three isolated points and the zero-Euler statement does not apply. No new homotopy equivalence, homology classification, or shellability claim is made here.

## Proof
**Circular-order lemma.** A directed triangle \(a\to b\to c\to a\) in \(R_n\) is encountered in cyclic order \(a,b,c\). Indeed rotate so \(a=0\), then \(b=x\) with \(1\le x\le m\); write \(c=x+y\) because \(b\to c\), where \(1\le y\le m\). Since \(c\to0\), we have \(n-(x+y)\in[1,m]\), hence \(0<x<x+y<n\). Therefore any triple \((a,b,c)\in A\times B\times C\) appears in this cyclic order. The elementary circular-separation observation now shows that all occupied \(A\)-labels form one cyclic block, followed by all occupied \(B\)-labels and then all occupied \(C\)-labels. For completeness: if one color were split by another color, pick one point of each split segment, one intervening point of the other color and a point of the third color; one of the two transversal triples would have the reverse cyclic order. Thus the three color classes cannot interleave, and their first occupied elements are uniquely defined.

Write the anchors in circular order as \(a,b,c\), and let \(x=(b-a)\bmod n\), \(y=(c-b)\bmod n\), and \(z=(a-c)\bmod n\). These are positive, sum to \(n=2m+1\), and each is at most \(m\), because the anchors form a directed triangle. Define the following disjoint sets of **available additional vertices**, with every residue interpreted modulo \(n\):
\[
P_A=\{a+j:1\le j\le m-z\},\qquad
P_B=\{b+j:1\le j\le m-x\},\qquad
P_C=\{c+j:1\le j\le m-y\}.
\]
The bounds put these vertices strictly before the next anchor: for example \(m-z=x+y-m-1\le x-1\), using \(y\le m\). The other two cases are cyclic permutations. A cell with anchors \((a,b,c)\) is **exactly** one of the triples
\[
A=\{a\}\cup S_A,\quad B=\{b\}\cup S_B,\quad C=\{c\}\cup S_C,
\qquad S_A\subseteq P_A,\ S_B\subseteq P_B,\ S_C\subseteq P_C.
\]
To see necessity and sufficiency, let \(r_A,r_B,r_C\) denote the largest respective chosen clockwise offsets after each anchor, with zero for empty augmentation. Because the occupied color classes are cyclic consecutive blocks, the longest required positive directed distances across the three arc families are exactly \(x+r_B\) (from first \(A\) to last \(B\)), \(y+r_C\) (from first \(B\) to last \(C\)), and \(z+r_A\) (from first \(C\) to last \(A\)). All required arcs exist if and only if
\[
r_A\le m-z,\qquad r_B\le m-x,\qquad r_C\le m-y.
\]
This proves the claimed independent Boolean augmentation description. The number of available positions is
\[
(m-z)+(m-x)+(m-y)=3m-(2m+1)=m-1.
\]
For a fixed anchor, choosing exactly \(d\) positions produces exactly \(\binom{m-1}{d}\) dimension-\(d\) cells.

Finally, anchor triples are counted by choosing \(a\) in \(n\) ways, and \((x,y)\in[1,m]^2\) with \(z=n-x-y\in[1,m]\). This is equivalent to \(x+y\ge m+1\), giving \(\sum_{x=1}^{m}x=\binom{m+1}{2}\) pairs. Multiplying gives the face polynomial. Every cell extends within its anchor Boolean interval to a top cell (choose all available positions), proving purity and dimension. A nonidentity target translation sends the unique anchor \(a\) to a different residue and hence fixes no cell, giving the quotient cell counts. Finally \(\chi(X_n)=F_{X_n}(-1)=0\) because \(m-1\ge1\).

## Verification
The standalone, dependency-free `verify.py` builds the cells directly from the tournament arc predicate, without using the anchor theorem; a second generator builds them from the anchor subsets. For \(n=5,7,9,11,13,15\), the complete sets agree exactly and their dimension counts are respectively \((15,15)\), \((42,84,42)\), \((90,270,270,90)\), \((165,660,990,660,165)\), \((273,1365,2730,2730,1365,273)\), and \((420,2520,6300,8400,6300,2520,420)\). Run `python3 verify.py` from the extracted package. This is a finite stress test only; the preceding proof establishes all parameters.

## Relationship to prior work
Dochtermann and Singh (2021/2023) introduce regular-polyhedral directed Hom complexes and study several tournament examples, emphasizing transitive targets. The previously published calculation for the regular cyclic nine-vertex tournament gives the special face vector \((90,270,270,90)\) and an exact circle homotopy type. An existing all-odd-order equivariant circle classification provides the underlying homotopy information, but neither a circle homotopy type nor its equivariant version determines a CW face vector, purity, or the unique Boolean anchor stratification. The present statement is deliberately enumerative and structural, not a new circle theorem.

## Limitations
The Boolean pieces are poset intervals **only as an indexed set partition**; the face incidence between different anchors is not determined by the polynomial. The theorem does not establish a homology basis, explicit boundary matrices, perfect Morse matching or new homotopy type. The formula is for the canonical tournament with steps \(1,\ldots,m\), not arbitrary regular or circulant tournaments. Equivalent unindexed enumeration remains a bibliographic risk.

## References
1. Anton Dochtermann and Anurag Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, first public arXiv:2108.10948v1, 24 August 2021; European Journal of Combinatorics 110 (2023), 103704, DOI 10.1016/j.ejc.2023.103704.
2. *The directed Hom complex \(\operatorname{Hom}(\overrightarrow C_3,R_9)\) has the homotopy type of a circle*, public published-finding corpus record dated 4 October 2026 (RESULT.md, sha `70f5b26512e1f4a5f0884113734de446edd0aa7b`).
