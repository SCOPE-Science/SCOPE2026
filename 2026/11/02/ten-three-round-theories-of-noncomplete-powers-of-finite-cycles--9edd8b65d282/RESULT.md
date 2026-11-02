# Ten three-round theories of noncomplete powers of finite cycles

## Finding
For integers \(r\ge1\) and \(n\ge2r+2\), let \(G(n,r)\) be the undirected simple graph with vertex set \(\mathbb Z/n\mathbb Z\); two distinct vertices are adjacent precisely when their cyclic distance is at most \(r\). We consider equality and adjacency, with no named vertices, orientation, or distance predicate. Write \(\equiv_3\) for agreement on every first-order sentence of quantifier rank at most three.

**Theorem.** Exactly **ten** \(\equiv_3\)-classes occur in the two-parameter family \(\{G(n,r):r\ge1,\ n\ge2r+2\}\). Four consist of ordinary cycles (\(r=1\)) with parameter conditions \(n=4\), \(n=5\), \(n=6\), \(n\ge7\). The remaining six (\(r\ge2\)) have parameter conditions

\[
 n=2r+2;\quad 2r+3\le n\le3r+1;\quad n=3r+2;\quad 3r+3\le n\le4r+1;\quad n=4r+2;\quad n\ge4r+3.
\]

Two members of the family are three-round equivalent if and only if they occupy the **same** one of these ten cases, even if their radii differ. In particular, all \(r\ge2\) graphs with \(n\ge4r+3\) share a common rank-three theory. For **each fixed** \(r\ge1\), the threshold \(4r+3\) for a common tail is sharp: \(G(4r+2,r)\not\equiv_3G(4r+3,r)\).

## Assumptions and scope
Cyclic distance means \(d_n(a,b)=\min\{(a-b)\bmod n,(b-a)\bmod n\}\). The inequality \(n\ge2r+2\) makes \(G(n,r)\) proper (noncomplete), of regular degree \(2r\). All first-order statements below are in the undirected equality-and-adjacency language. The theorem does not concern complete cycle powers, orientation, counting quantifiers, or ranks exceeding three.

## Proof
**Step 1: a three-round invariant for vertex-transitive graphs.** For distinct vertices \(a,b\) of a simple graph, define their *third-point spectrum* \(S(a,b)\subseteq\{00,01,10,11\}\): the word \(ij\) lies in \(S(a,b)\) if some \(z\notin\{a,b\}\) has adjacency values \((E(a,z),E(b,z))=(i,j)\). For a vertex-transitive graph of at least three vertices, form the collection \(\mathscr T(G)=\{(E(a,b),S(a,b)):a\ne b\}\). Two such graphs are three-round equivalent exactly when these collections agree. Indeed the first selected vertex is movable by an automorphism; in round two Duplicator must choose a pair of the same adjacency and spectrum type, and in round three only equality and the two prescribed adjacency bits remain. If a pair type is missing on the other side, Spoiler selects that pair in the first two rounds, then selects a third vertex realizing a spectrum bit absent on the other side. Conversely identical collections give a winning Duplicator strategy against moves in either structure. Repeated selections are answered by repetitions.

**Step 2: geometry of a cyclic pair.** By rotation and reflection, take the pair to be \(0,d\), where \(1\le d\le\lfloor n/2\rfloor\). Its pair adjacency is \(1\) exactly if \(d\le r\). The word \(00\) is *absent* from its third-point spectrum exactly if both circular arcs between the selected vertices have at most \(2r+1\) steps:
\[
00\notin S(0,d)\quad\Longleftrightarrow\quad d\le2r+1\ \text{and}\ n-d\le2r+1.
\]
This follows because each interior arc vertex must lie within \(r\) steps of at least one endpoint; a longer arc has a vertex at least \(r+1\) steps from both. For a nonadjacent pair (\(d>r\)), the word \(11\) occurs exactly when \(d\le2r\), by taking an interior common neighbor on a shortest arc, and conversely using the triangle inequality. For adjacent pairs \(11\) occurs for all \(r\ge2\): if \(d=1\), take the neighbor on the other side of an endpoint; if \(2\le d\le r\), take an interior vertex. For \(r=1\), adjacent pairs have no common neighbor because \(n\ge4\).

The two one-sided words \(10\) and \(01\) always occur together, because the graph is regular. They occur for every distinct pair **except** the diametrically opposite nonedge when \(n=2r+2\), where both are absent and every other vertex is adjacent to both endpoints. To see this rigorously, absence of both words for an adjacent pair would make its closed neighborhoods identical; distinct translates of the proper circular arc of \(2r+1\) vertices cannot coincide. For a nonadjacent pair, absence of both words means identical open neighborhoods. The numbers of common neighbors contributed by the two circular arcs of lengths \(d\) and \(n-d\) sum to \(c(d)=\max(0,2r-d+1)+\max(0,2r-(n-d)+1)\), since each arc has exactly that many interior vertices within \(r\) steps of both ends. Each term is at most \(r\). If \(n>2r+2\), one arc has length at least \(r+2\), and then \(c(d)<2r\), ruling out identical degree-\(2r\) neighborhoods. When \(n=2r+2\), both neighborhoods coincide exactly for the antipodal pair with \(d=n-d=r+1\). These arguments exhaust every possible third-point pattern.

**Step 3: the complete type table.** Abbreviate the following spectra of distinct third vertices:
\[
 T=\{11\},\qquad E=\{01,10\},\qquad B=\{01,10,11\},\qquad N=\{00,01,10\},\qquad F=\{00,01,10,11\}.
\]
The table records the **set of spectra** available for adjacent pairs and nonadjacent pairs, respectively. Braces around multiple spectra indicate that different pairs exhibit different spectra.

| Radius and length | Adjacent-pair spectra | Nonadjacent-pair spectra |
| --- | --- | --- |
| \(r=1,\ n=4\) | \(\{E\}\) | \(\{T\}\) |
| \(r=1,\ n=5\) | \(\{N\}\) | \(\{B\}\) |
| \(r=1,\ n=6\) | \(\{N\}\) | \(\{F,E\}\) |
| \(r=1,\ n\ge7\) | \(\{N\}\) | \(\{F,N\}\) |
| \(r\ge2,\ n=2r+2\) | \(\{B\}\) | \(\{T\}\) |
| \(r\ge2,\ 2r+3\le n\le3r+1\) | \(\{B,F\}\) | \(\{B\}\) |
| \(r\ge2,\ n=3r+2\) | \(\{F\}\) | \(\{B\}\) |
| \(r\ge2,\ 3r+3\le n\le4r+1\) | \(\{F\}\) | \(\{B,F\}\) |
| \(r\ge2,\ n=4r+2\) | \(\{F\}\) | \(\{F,E\}\) |
| \(r\ge2,\ n\ge4r+3\) | \(\{F\}\) | \(\{F,N\}\) |

For completeness, the transitions follow directly from Step 2. At \(n=2r+2\), every distinct pair covers the remaining vertices; the nonadjacent antipodes are false twins. At \(2r+3\), adjacent distance-one pairs first admit \(00\), while adjacent distance-\(r\) pairs fail to admit \(00\) until \(n=3r+2\). Nonadjacent distance-\(r+1\) pairs first admit \(00\) at \(n=3r+3\), while a covering nonadjacent pair persists through \(n=4r+2\). Nonadjacent pairs lacking \(11\) first appear at \(n=4r+2\), precisely at cyclic distance \(2r+1\); at this boundary they also lack \(00\), and from \(n=4r+3\) onward they have \(00\). The \(r=1\) rows follow from the same arc tests together with the absence of triangles. Each displayed interval is nonempty for its stated radius; the examples \(r=2\) give all six latter cases. The ten row fingerprints are pairwise distinct. By Step 1, they are the ten and only ten three-round theories.

**Step 4: sharpness as an explicit sentence.** The rank-three sentence
\[
 \exists x\,\exists y\,\bigl(x\ne y\ \wedge\ \forall z\,[z=x\ \lor\ z=y\ \lor\ E(z,x)\ \lor\ E(z,y)]\bigr)
\]
asserts that two vertices dominate all other vertices. It is true in \(G(4r+2,r)\), witnessed by diametrically opposite vertices, and false in every \(G(n,r)\) with \(n\ge4r+3\) since two open neighborhoods cover at most \(4r\) other vertices, fewer than \(n-2\). Thus the tail cutoff cannot be reduced for any \(r\).

## Verification
The standalone Python program `verify/cycle_rank3.py` enumerates all pair spectra directly, checks the ten-class tail fingerprint for radii \(1\) through \(15\) and lengths up to forty-nine beyond each threshold, and checks sharpness via exhaustive two-vertex domination. Its output is `verify/cycle_rank3.out`. The independent program `verify/ef3_independent.py` implements the **full two-sided three-round Ehrenfeucht–Fraïssé game** without assuming transitivity or using pair spectra. It distinguishes all \(45\) pairs of ten class representatives and directly checks several cross-parameter stable-tail equivalences. Its output is `verify/ef3_independent.out`. Both were executed successfully. The proof of the infinite statements and of exactly ten classes is analytic; the computations are finite corroboration only. Reproduce with `python3 verify/cycle_rank3.py` and `python3 verify/ef3_independent.py` from the package root.

## Relationship to prior work
Brown and Hoshino (2007), Theorem 4.1 and 4.8, give a complete Ehrenfeucht–Fraïssé classification for **ordinary cycles** at every rank; their rank-three cutoff \(7\) accounts for the first four rows above. Their paper does not state a classification for varying positive powers of cycles. Verbitsky (2004) studies first-order definability bounds for cycles and wider graph classes, not the exact cross-radius three-round phase diagram. Thus the present claim concerns the six additional radius-at-least-two regimes and their collapse across different degrees. Searches did not identify an exact earlier equivalent, but negative search evidence does not establish priority.

## Limitations
The analysis requires \(n\ge2r+2\), assumes a pure undirected adjacency vocabulary, and concerns quantifier rank at most three. It says nothing about arbitrary circulants, higher ranks, counting logics, or ordered/colored structures. Exact historical priority has not been independently certified; an equivalent result might exist outside searched sources.

## References
1. Oleg Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361v1, publicly posted January 26, 2004; especially Introduction and preliminaries. https://arxiv.org/abs/math/0401361
2. Jason Brown and Richard Hoshino, *The Ehrenfeucht-Fraïssé Game for Paths and Cycles*, Ars Combinatoria 83 (2007), 193–212, especially Theorems 4.1 and 4.8. https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/
