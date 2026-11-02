# Fano flags and the unique mobile sector of Heawood \(3\)-colourings

## Finding
Let \(H\) be the point–line incidence graph of the Fano plane, and let \(\mathcal R_3(H)\) have one vertex for each proper colouring \(c:V(H)\to\{0,1,2\}\), with an edge when one vertex is recoloured. The colours are named, and colourings using fewer than three colours are included. Then
\[
|V(\mathcal R_3(H))|=2106,\qquad |E(\mathcal R_3(H))|=6804.
\]
There are exactly \(127\) connected components: \(126\) isolated colourings and one connected component \(\mathcal M\) with \(1980\) vertices and all \(6804\) edges. The connected component \(\mathcal M\) is self-centred:
\[
\operatorname{rad}(\mathcal M)=\operatorname{diam}(\mathcal M)=21.
\]
Every one of its \(1980\) vertices has eccentricity exactly \(21\).

The isolated colourings admit an exact **incidence-flag classification**. For each flag \((P,L)\) of the Fano plane, where point \(P\) lies on line \(L\), and each ordering \((A,B,C)\) of the three named colours, construct a colouring as follows:

- On point vertices, assign \(B\) to \(P\), \(C\) to the other two points of \(L\), and \(A\) to the four points outside \(L\).
- On line vertices, assign \(A\) to \(L\), \(C\) to the other two lines through \(P\), and \(B\) to the four lines not through \(P\).

These are precisely the frozen colourings, without repetitions. Hence their number is \(21\cdot6=126\); they form a single orbit under the Fano collineation group together with permutations of the named colours.

The mobile component has the exact degree enumerator
\[
D_{\mathcal M}(t)=126t^4+420t^5+504t^6+588t^8+252t^9+84t^{11}+6t^{14}.
\]
In particular, it has no frozen vertices. The extra \(126\) isolated vertices of \(\mathcal R_3(H)\) contribute \(126t^0\) to the degree enumerator of the full graph.

## Assumptions and scope
The Fano plane has seven points, seven lines, three points on each line, and exactly one line through any two distinct points. In a cyclic model, write the points as \(\mathbb Z/7\mathbb Z\) and the lines as
\[
L_j=\{j,j+1,j+3\}\pmod 7,\qquad 0\le j<7.
\]
The Heawood incidence graph has these seven points and seven lines as its vertices, adjacent exactly when a point belongs to a line. A valid recolouring changes exactly one of the fourteen vertex colours and must preserve propriety throughout. A colouring is *frozen* if no such move exists. The assertions are specific to this graph and the three named colours; no inference about arbitrary cubic bipartite graphs or other palettes is made.

## Proof
**1. Complete colour-count reduction.** Fix an assignment of colours to the seven point vertices. A line vertex can be coloured with precisely those named colours missing from its three incident points. If a Fano line contains all three point colours, that assignment admits no proper extension. If it contains two distinct point colours, the line colour is forced; if it is monochromatic, either of two colours is allowed, independently of the other line vertices. Thus an assignment with \(m\) monochromatic lines and no rainbow line has exactly \(2^m\) extensions. Exhausting the \(3^7=2187\) point assignments gives the following auditable finite table:

| Monochromatic lines \(m\) | Eligible point assignments | Full proper colourings | Has an integral height lift? |
|---:|---:|---:|---|
| 0 | 126 | 126 | No, all 126 |
| 1 | 210 | 420 | Yes, all 420 |
| 2 | 126 | 504 | Yes, all 504 |
| 4 | 42 | 672 | Yes, all 672 |
| 7 | 3 | 384 | Yes, all 384 |

The verification programs independently reconstruct this finite table or its equivalent counts from the explicit point–line incidence axioms. The weighted total is \(126+420+504+672+384=2106\).

**2. Classification of all frozen colourings.** At a frozen line vertex, both colours other than its own must appear among the three neighbouring point vertices. Consequently, every Fano line meets exactly two point-colour classes. Conversely, a point assignment with that property must have point-class sizes \(1,2,4\): each Fano line contributes exactly one pair of same-coloured points, and every pair of points belongs to exactly one line, so
\[
\sum_{i=0}^{2}\binom{n_i}{2}=7,\qquad \sum_i n_i=7,
\]
which has only the unordered nonnegative integer solution \(\{n_0,n_1,n_2\}=\{1,2,4\}\). Let \(P\) be the singleton-colour point, and \(Q,R\) the two points of the size-two class. If \(P,Q,R\) were not collinear, the line through \(P\) and \(Q\) would have one point from each of the three classes, a contradiction. Hence they lie on one line \(L\), which determines the point assignment from a flag \((P,L)\) and an ordering of colours. Propriety forces the line colours in the pattern stated above. Direct incidence checks show that every vertex then sees both other colours, so every resulting colouring is indeed frozen. Each flag and colour ordering gives a distinct colouring; there are \(7\cdot3\cdot3!=126\).

**3. Height-lift dichotomy and the single mobile component.** For a proper three-colouring \(c\), assign to each oriented incidence edge \(u\to v\) the unique increment \(\delta_c(u,v)\in\{-1,+1\}\) congruent to \(c(v)-c(u)\pmod 3\). A *height lift* is an integer function \(h\) with \(h(v)-h(u)=\delta_c(u,v)\), even heights at point vertices, odd heights at line vertices, and \(h(v)\equiv c(v)\pmod 3\). Such a lift exists exactly when all signed cycle sums vanish. Fixing the first point's height to be its unique representative in \(\{0,2,4\}\) makes a lift unique whenever one exists.

There is also a direct geometric dichotomy, independent of the finite height checks. If all three colours appear on the seven points, no Fano line can be monochromatic: if line \(L\) consisted entirely of colour \(A\), choose outside points of the other two colours \(B,C\); the line joining them meets \(L\) at an \(A\)-point and would be rainbow, making its line vertex impossible to colour. Consequently every line has exactly two point colours. By Step 2, such colourings are precisely the \(126\) frozen flag colourings. Their inability to admit an integral lift is also visible around a six-cycle: choosing a singleton-colour point, a size-two-class point on its distinguished line, and a point outside that line gives a cycle whose successive vertex colours are \(B,C,A,B,C,A\), so the signed increments total \(\pm6\), not zero.

If at most two colours \(A,B\) appear on the seven point vertices, construct an integral lift explicitly. Choose even integer heights \(a,b\) for those two colours, satisfying \(a\equiv A\), \(b\equiv B\pmod3\) and \(|a-b|=2\). Give each point its colour's corresponding height. Every line meeting both point colours has the missing third colour, so assign its line vertex the odd midpoint \((a+b)/2\). Every monochromatic line, with its points at height \(a\) or \(b\), receives the unique one of the adjacent odd heights \(a\pm1\) or \(b\pm1\) congruent to its chosen line colour modulo three. Every incidence edge then has height difference \(\pm1\), and all heights have the prescribed residues. If only one point colour is used, apply the same construction without the unused class. Thus **exactly** the \(1980\) non-frozen colourings have lifts. The independent finite programs additionally verify this implication for all states by checking edge consistency after spanning-tree propagation.

The height-function recolouring lemma of Cereceda, van den Heuvel and Johnson implies that all proper three-colourings of a connected bipartite graph admitting such lifts belong to one recolouring component. More explicitly, given two lifts with the same parity convention, a local maximum or minimum at a vertex where their heights disagree can be changed by \(2\) toward the other lift; repeating decreases the \(L^1\) discrepancy by exactly \(2\) each step. Therefore all \(1980\) colourings with height lifts lie in one component. The remaining \(126\) are frozen, yielding exactly \(127\) components.

**4. Sharp metric.** Any two integer lifts of the same colouring and parity convention differ by a global multiple of \(6\). The same height-transformation argument, together with the fact that each recolouring changes one height by \(2\), gives the *exact* distance for height-admitting colourings:
\[
d(c,d)=\min_{k\in\mathbb Z}\frac12\sum_{v\in V(H)}|h_c(v)-h_d(v)-6k|.
\]
For the lower bound, lift an arbitrary recolouring path starting at \(h_c\); its final height differs from \(h_d\) by \(6k\). For the upper bound, apply the monotone-height argument to the chosen pair \(h_c,h_d+6k\). The minimum exists and can be found from the median of the fourteen coordinate differences.

The second verification program exhaustively evaluates this exact metric for **every pair** of the \(1980\) mobile states and finds eccentricity \(21\) for every state. Independently, the first verification program runs breadth-first search from every state in the same component and obtains the same eccentricity. This establishes the radius and diameter claims without extrapolation.

For an explicit sharpness witness, take \(c\) assigning colour \(0\) to all seven points and \(1\) to all seven lines, and take \(d\) with those colours exchanged. In the normalized lifts, the height differences are \(-4\) at the seven points and \(-2\) at the seven lines; the optimal global shift is \(0\) or \(-1\). Thus \(d(c,d)=(7\cdot4+7\cdot2)/2=21\).

**5. Symmetry and degrees.** The Fano collineation group is flag-transitive; together with permutations of the three colour names it is transitive on the flag-parametrized frozen states. The two independent programs enumerate all single-site recolourings and obtain the stated degree polynomial and \(6804\) undirected edges. The first additionally constructs the full \(336\)-element incidence automorphism group and verifies transitivity on the frozen states.

## Verification
The two required standalone programs are `check_singer.py` and `check_vector_height.py`; both use Python 3 and its standard library only. Run them in a directory containing the files:

```sh
python3 check_singer.py
python3 check_vector_height.py
```

The first uses the cyclic difference set \(\{0,1,3\}\) in \(\mathbb Z/7\mathbb Z\), recursively generates all named proper colourings, constructs all legal moves, performs all-root graph searches, and checks the full incidence automorphism group. The second uses the seven nonzero vectors of \(\mathbb F_2^3\), constructs Fano lines by vector addition, independently counts extensions from point assignments, checks the incidence-flag classification and the height dichotomy, and evaluates the exact height metric for every ordered pair of mobile states. Each contains executable assertions; a failed assertion is not evidence of success.

## Relationship to prior work
Cereceda, van den Heuvel and Johnson developed the three-colouring recolouring graph, its signed-cycle weights, the height-function connectivity lemma, and general criteria for non-mixing of bipartite graphs. Their work supplies the general structural lemma used here; its application alone does **not** enumerate the Heawood states, identify which colourings lack heights, classify frozen configurations as Fano flags, or give the sharp diameter \(21\). These are the specific finite-geometry claims established here.

A separate known result about homomorphisms from the Heawood graph to the five-cycle concerns the different target graph \(C_5\), not proper three-colourings (homomorphisms to \(K_3\)). A homomorphism to a triangle cannot be composed with a graph homomorphism from \(K_3\) to \(C_5\), because the latter is triangle-free. Counts or connectivity in the five-cycle target therefore do not imply the present theorem. Other known recolouring and exchange calculations on Heawood structures concern different configurations and moves.

## Limitations
This is a complete exact result only for the fourteen-vertex Heawood graph and exactly three named vertex colours. It does not classify other incidence graphs or claim a general bounded-diameter theorem. The exhaustive conclusions rely on the two supplied, independently organized finite computations, and the height argument relies on a previously published general lemma. Historical priority is qualified: some older work may describe an equivalent finite instance under different terminology. An independent scholarly audit has not been performed.

## References
1. L. Cereceda, J. van den Heuvel and M. Johnson, *Mixing 3-colourings in bipartite graphs*, European Journal of Combinatorics **30** (2009), 1593–1606, DOI: `10.1016/j.ejc.2009.03.011`. Author manuscript (dated February 2007): `https://matthewjohnsondurham.github.io/papers/cdam-2007-06.pdf`.
2. L. Cereceda, J. van den Heuvel and M. Johnson, *Finding paths between 3-colorings*, Journal of Graph Theory **67** (2011), 69–82, DOI: `10.1002/jgt.20514` (first online 2010-12-16).
3. J. C. Baez, *Heawood Graph*, Visual Insight / American Mathematical Society, 2015-08-01, `https://blogs.ams.org/visualinsight/2015/08/01/heawood-graph/` (standard Fano-incidence description and symmetries).
