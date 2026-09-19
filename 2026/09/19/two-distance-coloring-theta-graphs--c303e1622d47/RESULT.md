# Exact two-distance chromatic number of three-path theta graphs

## Result

Let \(\Theta(a,b,c)\) be the simple graph formed by three internally vertex-disjoint \(u\)-\(v\) paths of edge lengths
\[
1\le a\le b\le c,
\]
with \(b\ge2\) (so there is at most one direct \(uv\) edge). For a graph \(G\), a two-distance coloring is a proper coloring of \(G^2\), where vertices at graph distance at most two must receive different colors.

Then
\[
\chi\!\left(\Theta(a,b,c)^2\right)=
\begin{cases}
6,&(a,b,c)=(2,2,3),\\[1mm]
5,&(a,b,c)\in\mathcal F,\\[1mm]
4,&\text{otherwise},
\end{cases}
\]
where
\[
\mathcal F=
\{(2,2,2),(2,2,6),(1,2,3),(1,2,4),(1,3,4)\}
\cup\{(2,3,c):c\ge3\}
\cup\{(1,4,c):c\ge4\}.
\]

Thus the simplest 2-connected non-cactus series-parallel blocks already display all three values \(4,5,6\) in the subcubic regime. In particular, \(\Theta(2,2,3)^2=K_6\), so the sharp \(\Delta+3=6\) upper bound for squares of \(K_4\)-minor-free graphs of maximum degree three is attained inside the theta family.

## Four-color transfer lemma

A color word \(z_0z_1\dots z_L\) along a path is proper in the square of the path exactly when every three consecutive colors are distinct. With four colors \(\{0,1,2,3\}\), encode the last two colors by a state \((x,y)\), \(x\ne y\). The allowed transition is
\[
(x,y)\longrightarrow (y,z),\qquad z\notin\{x,y\}.
\]
By color symmetry it is enough to start at state \(01\). Let \(\alpha,\beta\) denote the two colors in \(\{2,3\}\). The terminal-state types reachable by a path of \(L\) edges are:

| \(L\) | reachable terminal-state types from \(01\) |
|---|---|
| 2 | \(1\alpha\) |
| 3 | \(\alpha0,\alpha\beta\) |
| 4 | \(01,0\alpha,\alpha0,\alpha1\) |
| 5 | \(01,10,0\alpha,1\alpha,\alpha1,\alpha\beta\) |
| 6 | \(10,0\alpha,\alpha0,1\alpha,\alpha1,\alpha\beta\) |
| \(\ge7\) | every ordered unequal state |

The table follows by the one-step recurrence above. At \(L=7\) all twelve ordered unequal states occur, and therefore all remain reachable at every larger length.

For vertices on different theta paths, distance at most two can only arise through the common endpoint neighborhoods. Hence a collection of path color words gives a coloring of the whole square exactly when it is valid on each path and the colors on each closed branch neighborhood are pairwise distinct.

## Classification of four-colorability

Every branch endpoint has degree three, so its closed neighborhood is a \(K_4\) in the square. Hence four colors are a universal lower bound.

### One direct path: \(a=1\)

Fix \(u=0\), \(v=1\). The first internal vertices of the other two paths must use colors \(2,3\), and the last internal vertices must also use \(2,3\) in some order.

For one of these paths, if its first and last internal vertices have the same color, the transfer table permits its length exactly when
\[
L\in S:=\{2\}\cup\{5,6,7,\dots\}.
\]
If the two endpoint-neighbor colors are swapped, the permitted lengths are exactly
\[
L\in T:=\{3\}\cup\{5,6,7,\dots\}.
\]
The two paths must simultaneously use the identity permutation or simultaneously use the swap. Therefore \(\Theta(1,b,c)\) is four-colorable iff either \(b,c\in S\) or \(b,c\in T\). The failures are precisely
\[
(1,2,3),\ (1,2,4),\ (1,3,4),\quad\text{and}\quad (1,4,c)\ (c\ge4).
\]

### No direct path and \(a=2\)

Fix \(u=0\) and let the three first-neighbor colors be \(1,2,3\).

If \(a=b=2\), the first two length-two paths force the color of \(v\) to be \(3\) (after relabeling), their last-neighbor colors to be \(1,2\), and the third path to start and finish in the same state \((0,3)\). The transfer table shows that this same state is reachable, for \(c\ge2\), exactly when
\[
c\in\{4,5\}\cup\{7,8,9,\dots\}.
\]
Thus the failures are \((2,2,2),(2,2,3),(2,2,6)\).

If exactly one path has length two and the next path has length three, the length-two path forces a last-neighbor color that makes the length-three endpoint constraints impossible: if the color of \(v\) equals the first color on the length-three path, no length-three terminal state has that endpoint color; if it is the other available branch color, the length-three path is forced to reuse the already occupied last-neighbor color. Thus every \(\Theta(2,3,c)\), \(c\ge3\), fails to be four-colorable.

If \(b\ge4\), choose the color of \(v\) to be \(2\), and choose last-neighbor colors \((1,3,0)\) for the paths whose first-neighbor colors are \((1,2,3)\). The second path then uses terminal type \(\alpha1\) relative to its relabeled start, and the third uses type \(0\alpha\); both types are available for every length at least four. Hence all \(\Theta(2,b,c)\) with \(b\ge4\) are four-colorable.

### All path lengths at least three

Again fix \(u=0\), with first-neighbor colors \(1,2,3\), and first try \(v=0\). For a path starting with color \(p\in\{1,2,3\}\), the transfer table reduces the condition on its last-neighbor color \(q\) to
\[
\begin{array}{c|c}
L&\text{condition on }q\\ \hline
3,4&q\ne p,\\
5&q=p,\\
\ge6&q\text{ arbitrary in }\{1,2,3\}.
\end{array}
\]
The three last-neighbor colors must form a permutation of \(1,2,3\). Such a permutation exists except when exactly two paths have length five and the remaining path has length three or four. Indeed, with no forced fixed points a 3-cycle works; with one forced fixed point swap the other two; with three forced fixed points use the identity; and any unrestricted position causes no difficulty. The only two exceptional length multisets for this choice of endpoint color are therefore \((3,5,5)\) and \((4,5,5)\).

They are nevertheless four-colorable. With first-neighbor colors \((1,2,3)\), use respectively
\[
(3,5,5):\quad v=2,\quad(q_1,q_2,q_3)=(3,0,1),
\]
and
\[
(4,5,5):\quad v=1,\quad(q_1,q_2,q_3)=(0,2,3).
\]
Every required state is present in the transfer table. Hence all theta graphs with \(a\ge3\) are four-colorable.

Combining the three cases gives exactly the listed failures of four-colorability.

## Distinguishing five from six colors

The graph \(\Theta(2,2,3)\) has six vertices and diameter two, hence
\[
\Theta(2,2,3)^2=K_6,
\]
so its chromatic number is six.

Every other four-color obstruction above is five-colorable. One convenient verification uses the same state method with five colors: from any ordered unequal start state, every ordered unequal terminal state is reachable by a path of length at least five. The recurrence reaches all twenty ordered unequal states already at length five, and remains full thereafter.

For completeness, short witnesses can be fixed with colors \(0,1,2,3,4\):

- \(\Theta(2,2,2)\): its square is \(K_5\).
- \(\Theta(2,2,6)\): take \(u=0,v=4\), first-neighbor colors \(1,2,3\); the length-six path can end in state \((0,4)\).
- \(\Theta(2,3,3)\): use path words \(014\), \(0234\), \(0324\).
- \(\Theta(2,3,4)\): use \(014\), \(0234\), \(03104\).
- \(\Theta(2,3,c)\) for \(c\ge5\): use \(014\), \(0234\), and a length-\(c\) word from state \((0,3)\) to \((0,4)\), which exists by five-color state saturation.
- \(\Theta(1,2,3)\): use \(01\), \(021\), \(0341\).
- \(\Theta(1,2,4)\): use \(01\), \(021\), \(03241\).
- \(\Theta(1,3,4)\): use \(01\), \(0241\), \(03421\).
- \(\Theta(1,4,4)\): use \(01\), \(02341\), \(03421\).
- \(\Theta(1,4,c)\) for \(c\ge5\): use \(01\), \(02341\), and a length-\(c\) word from state \((0,3)\) to \((2,1)\).

Together with the four-color obstruction proof, these witnesses give chromatic number five in exactly the claimed cases.

## Context and originality

Suvagiya (2026) determines two-distance and list-two-distance coloring exactly for cacti. In the subcubic case, cacti have square chromatic number four except for a \(C_5\) block, which forces five. The paper explicitly identifies extension from cacti toward broader outerplanar or \(K_4\)-minor-free classes as a natural next direction. A three-path theta graph is a minimal 2-connected series-parallel obstruction to being a cactus: it has a \(K_{2,3}\) subdivision but remains \(K_4\)-minor-free.

Lih, Wang and Zhu (2003) proved the sharp general bound \(\chi(G^2)\le \Delta+3\) for \(K_4\)-minor-free graphs when \(\Delta\in\{2,3\}\), so the value six at \(\Theta(2,2,3)\) is compatible with, and may well be among, their sharp examples. No originality is claimed for that isolated sharp witness. The new claim is the complete three-parameter classification above, including the infinite five-color families and the transfer characterization of every four-colorable theta.

Searches for `theta graph`, `generalized theta graph`, `square coloring`, `2-distance coloring`, `distance-two coloring`, `subdivision of K_{2,3}`, and equivalent combinations did not locate a prior exact classification of \(\chi(\Theta(a,b,c)^2)\). A 2016 paper classifies packing colorings of generalized theta graphs, a different invariant. A 2022 paper whose title mentions generalized theta graphs studies ordinary proper coloring of the theta family; its abstract separately mentions the square of a comb graph and does not state a square-coloring result for theta graphs.

The full text of Lih--Wang--Zhu (2003) was not inspected; its abstract and bibliographic record were inspected. Because it states that sharpness examples are given, it is the source most capable of containing an isolated theta example, but no evidence was found that it contains the full classification. The full text of Hetherington--Woodall (2008), which proves the corresponding list bounds, was likewise not inspected; its abstract was inspected. These are the principal residual originality risks. The originality assessment is therefore only to the best of our knowledge.

## Verification

`artifacts/verify_theta_square.py` constructs the theta graph and its square directly, computes exact chromatic numbers by backtracking, and compares them with the theorem for every \(1\le a\le b\le c\le10\) with \(b\ge2\). It checks 210 parameter triples. It also reconstructs the four-color state recurrence through the saturation length and confirms that \(\Theta(2,2,3)^2=K_6\). The recorded output is in `artifacts/verification.txt`.

The finite computation supports the proof but is not used as a substitute for the general argument.

## References

1. V. Suvagiya, *Two-distance and list-two-distance coloring of cacti: the subcubic case and the C5 obstruction*, arXiv:2609.20204 (2026). https://arxiv.org/abs/2609.20204
2. K.-W. Lih, W.-F. Wang, X. Zhu, *Coloring the square of a K4-minor free graph*, Discrete Mathematics 269 (2003), 303--309. https://doi.org/10.1016/S0012-365X(03)00059-1
3. T. J. Hetherington, D. R. Woodall, *List-colouring the square of a K4-minor-free graph*, Discrete Mathematics 308 (2008), 4037--4043. https://doi.org/10.1016/j.disc.2007.07.102
4. D. Laïche, I. Bouchemakh, É. Sopena, *Packing Coloring of Undirected and Oriented Generalized Theta Graphs*, Australasian Journal of Combinatorics 66 (2016), 310--329. https://arxiv.org/abs/1606.01107
5. D. V. Shankar, T. Muthulakshmi, *On proper coloring of Durer graph, square graph of comb graph, generalized theta graph and tadpole graph*, International Journal of Food and Nutritional Sciences 11(8) (2022), 275--282. https://ijfans.org/index.php/Journal/article/view/8313
