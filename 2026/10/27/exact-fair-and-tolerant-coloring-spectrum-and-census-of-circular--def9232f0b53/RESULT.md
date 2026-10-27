# Exact fair-and-tolerant coloring spectrum and census of circular ladders

## Finding
For each integer \(n\ge 3\), let the circular ladder \(P_n=C_n\square K_2\) have vertices \((i,s)\), where \(i\in\mathbb Z/n\mathbb Z\) and \(s\in\{0,1\}\), and edges connecting successive indices within each layer and matching indices across layers. A FAT coloring uses all its named colors and gives every vertex the same number of neighbors in each color other than its own, as well as a fixed number of neighbors in its own color (see [1]). Let \(N_k(n)\) count all FAT colorings with a fixed palette of exactly \(k\) named colors.

The complete spectrum at three and four colors is
\[
N_3(n)=\begin{cases}36,&6\mid n,\\6,&n\equiv3\pmod 6,\\0,&3\nmid n,\end{cases}
\qquad
N_4(n)=\begin{cases}24,&4\mid n,\\0,&4\nmid n.\end{cases}
\]
Consequently the FAT chromatic number is
\[
\chi^{\mathrm{FAT}}(P_n)=\begin{cases}
4,&4\mid n,\\
3,&4\nmid n\text{ and }3\mid n,\\
2,&3\nmid n\text{ and }4\nmid n.
\end{cases}
\]
The count of unnamed color partitions is respectively \(N_3(n)/6\) at three colors and \(N_4(n)/24\) at four colors. In particular, there is exactly one unnamed four-color FAT partition whenever it exists; three-color partitions number six for multiples of six and one for odd multiples of three.

## Assumptions and scope
All graphs are finite, undirected, simple, and connected. Fix \(n\ge3\); every circular-ladder vertex has degree three. For \(k\ge 2\), a FAT \(k\)-coloring is a surjection from vertices onto \(\{0,\ldots,k-1\}\) for which there are nonnegative \(\alpha,\beta\) with \(\beta+(k-1)\alpha=1\): each vertex has \(3\alpha\) neighbors of any *different* color and \(3\beta\) neighbors of its own color. The FAT chromatic number maximizes \(k\), not minimizes it. Color palettes and the layer/index labels are fixed for \(N_k(n)\); no rotations or graph automorphisms are divided out.

## Proof
**Degree restriction and baseline.** For connected graphs with at least two nonempty color classes, \(\alpha>0\); otherwise no edges would join different classes. Since \(3\alpha\) is a positive integer, \((k-1)3\alpha\le3\) forces \(k\le4\). Coloring every vertex of layer zero by color zero and every vertex of layer one by color one is a FAT two-coloring for every \(n\): every vertex has two same-color neighbors and one other-color neighbor, so \(\alpha=1/3,\beta=2/3\).

**Four colors.** Necessarily \(3\alpha=1\) and \(3\beta=0\). Thus each vertex has exactly one neighbor of each other color and no same-color neighbor. Write \(a_i,b_i\) for the colors in the upper/lower vertices of column \(i\). Both colors in a column differ. The two distinct colors in column \(i+1\) must be precisely the two colors not in \(\{a_i,b_i\}\): both are adjacent to their counterpart in column \(i\), and each is forced to avoid the entire preceding pair because all three neighbors at either vertex of column \(i\) have distinct colors. It follows that the column pairs alternate complementary unordered color pairs. The color at \((i+2,0)\) must differ from \(a_i\) and belong to \(\{a_i,b_i\}\), so \(a_{i+2}=b_i\); similarly \(b_{i+2}=a_i\). These identities imply \(a_{i+4}=a_i,b_{i+4}=b_i\) and no smaller period for the ordered columns, since \(a_i\neq b_i\). Therefore cyclic closure holds exactly if \(4\mid n\). Conversely, take any ordered pair of distinct colors for column zero, then any ordered pair of the two complementary colors for column one; the forced four-periodic continuation meets every FAT condition. The number of choices is \(4\cdot3\cdot2=24\), so the four-color count follows.

**Three colors.** Necessarily \(3\alpha=1\) and \(3\beta=1\) (the other possible positive integral value for \(3\alpha\) would violate \(\beta\ge0\)). Every vertex sees exactly one neighbor in each of the three colors, including its own. Encode colors as \(\mathbb F_3\) and let the column vector be \(u_i=(a_i,b_i)\) and the coordinate-swap map be \(J(a,b)=(b,a)\). The missing third color of two distinct elements \(p,q\in\mathbb F_3\) is \(-p-q\). The neighborhood conditions therefore impose
\[
u_{i+1}=-u_{i-1}-Ju_i.
\]
Applying the recurrence again gives \(u_{i+2}=Ju_{i-1}\), hence
\[
u_{i+3}=Ju_i,\qquad u_{i+6}=u_i.
\]
Here \(Ju_i\) denotes swapping upper and lower colors, not an exchange of named palette colors.

Any first two columns \(u_0=(a,b)\), \(u_1=(c,d)\) are allowed exactly when \(a\neq d\) and \(b\neq c\); these conditions ensure that the two preassigned neighbors of each vertex of column one have different colors. Once they hold, the recurrence selects the unique third neighbor color. The inequalities propagate to every subsequent column: \(u_2\) consists of the missing colors of the unequal pairs \((a,d)\) and \((b,c)\), so it differs in the required way from \(u_1\), and induction continues. The recurrence yields a valid infinite six-periodic coloring, and the two initial columns uniquely determine it. There are \(3^2\cdot 2^2=36\) initial choices, all giving valid colorings when \(6\mid n\).

If \(n\equiv3\pmod6\), cyclic closure of \(u_{i+3}=Ju_i\) forces \(u_i=Ju_i\) for every column. Then \(a_i=b_i\) for every \(i\), and the column colors run through the three colors cyclically. There are exactly \(3\cdot2=6\) named colorings. For all other \(n\) not divisible by three, cyclic closure is impossible: alternatively, [1, Theorem 2.12] shows that connected regular graphs have equal FAT color-class sizes, so \(3\mid 2n\), equivalently \(3\mid n\), is necessary. Both cases counted above provide colorings whenever \(3\mid n\). All three-color FAT partitions have all three colors nonempty by their local neighborhood condition.

The resulting chromatic-number cases follow from the upper bound four, exact existence for three/four colors, and universal two-color construction. Quotienting named colorings by permutation of color names divides by \(3!\) or \(4!\), because every palette color occurs.

## Verification
The self-contained program `fat_prism_verifier.py` checks FAT neighbor distributions directly, with no implementation of the algebraic recurrence. It enumerates allowed ordered column assignments by backtracking for \(3\le n\le20\), independently computes \(N_3(n)\), \(N_4(n)\), and compares each to the formulas (36 cases). All complete colorings at small orders are also checked against the stated period identities. It verifies the two-color construction for all \(3\le n\le100\) (98 additional checks). Run `python3 fat_prism_verifier.py`; the expected output is `VERIFY_OK local_census_cases=36 prism_orders=3..20 two_color_constructions=98`. These finite tests are not the proof of the infinite-family theorem.

## Relationship to prior work
Beers and Mulas [1] defined FAT colorings, established the connected regular equal-class-size lemma, and gave general degree bounds. Their follow-up [2, Section 7, especially Theorem 7.6 and Figure 9] *already constructs* three-color FAT colorings of a six-cycle Cartesian product with \(K_2\) by lifting base-cycle colorings. Thus the mere existence of a three-color FAT coloring of \(P_6\), and the general Cartesian lifting principle, are prior work and are not claimed here. The new result is the precise divisibility trichotomy across all circular ladders together with the exact named and unnamed census and rigidity of the four- and three-color partitions. Other FAT-coloring investigations [3–5] focus on the comparison with conventional chromatic numbers, realizable parameter pairs, and irreducible-coloring counts on other host graphs, without a matching circular-ladder classification located. General perfect-coloring and covering-map terminology supplies equivalent language for the local constraints but does not by itself establish the exact prism spectrum or census.

## Limitations
Only simple circular ladders \(C_n\square K_2\) with \(n\ge3\) are classified; open ladders, twisted/Möbius ladders, and general Cartesian graph products are not addressed. The enumeration counts named vertex colorings, not equivalence classes under graph automorphisms. Direct finite checks stop at the documented parameters; the infinite claim uses the displayed recurrence/rigidity proof. A historical-priority search cannot rule out prior classification under perfect-coloring, graph-cover, or equitable-partition terminology. Independent mathematical audit has not been performed.

## References
[1] L. Beers and R. Mulas, *Fair and Tolerant (FAT) Graph Colorings*, arXiv:2510.18494 (first version 2025-10-21), https://arxiv.org/abs/2510.18494 .
[2] L. Beers and R. Mulas, *Spectral Perspectives on FAT Graph Colorings*, arXiv:2604.21665 (2026-04-23), https://arxiv.org/abs/2604.21665 .
[3] S. Shaebani, *On Fair and Tolerant Colorings of Graphs*, arXiv:2511.14871 (2025), https://arxiv.org/abs/2511.14871 .
[4] S. Shaebani, *Concerning FAT Colorings of Graphs*, arXiv:2512.11153 (2025), https://arxiv.org/abs/2512.11153 .
[5] S. Shaebani, *On The Number of Irreducible FAT Colorings*, arXiv:2606.22374 (2026), https://arxiv.org/abs/2606.22374 .
