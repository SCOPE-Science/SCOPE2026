# Distances between strict bicolorings in the weak recolouring graph of AG(2,3)

## Finding

Let the points be \(\mathbb F_3^2\), with three distinguished colours. A weak colouring forbids monochromatic affine lines, and a move changes the colour of exactly one point while staying weak. Call a colouring *strict* if every line uses exactly two colours. No move takes one strict colouring directly to another, but all pairs of strict colourings are joined by weak recolourings. In the graph on **all** weak colourings, the 162 strict colourings have the following pair-distance distribution:

| Distance | Other strict colourings at this distance from any fixed strict colouring | Unordered strict pairs |
|---:|---:|---:|
| 4 | 32 | 2592 |
| 5 | 22 | 1782 |
| 6 | 16 | 1296 |
| 7 | 80 | 6480 |
| 8 | 8 | 648 |
| 9 | 1 | 81 |
| 10 | 2 | 162 |

No other positive distance occurs between strict colourings. For any strict colouring, its two strict partners at distance ten are precisely the two nontrivial cyclic permutations of its three colour names. Thus even the best change between distinct strict assignments takes at least four moves; the distance counts distinguish how hard it is to move between such assignments once rainbow lines are allowed.

## Assumptions and scope

Take all twelve affine lines and label the nine points lexicographically by \((x,y)\in\{0,1,2\}^2\). All colours are distinguished; colour permutations and affine point maps are used as symmetries of the graph, not taken as quotients. Distances are measured allowing any weak intermediate state; there is no prohibition on intermediate strict states and no claim about other affine planes.

## Proof

A class of any weak colouring is a line-free set. If five points formed a line-free set, their ten pairs would give ten lines carrying two points each, accounting for all twenty point-line incidences of the five points. The remaining two lines would both be disjoint from the five points, impossible since two distinct lines cover at least five points and the complement has just four. Thus each colour class has size at most four, all three colours occur, and the unordered sizes are \((1,4,4),(2,3,4)\) or \((3,3,3)\). In a weak colouring with sizes \(c_0,c_1,c_2\) the number of two-coloured lines is \(\sum_i\binom{c_i}{2}\): each such line yields exactly one same-colour pair and each pair belongs to a unique line. This number is twelve precisely for \((1,4,4)\).

Translate the singleton of a strict colouring to the origin. On every line through it the two remaining points must have the same colour to avoid a rainbow line. The other two colour classes must therefore each receive two of the four directions through the origin. Every such choice works: a class consisting of the nonzero points of two distinct directions is of the form \(\{a,-a,b,-b\}\). Any triple within it contains an opposite pair and has nonzero sum, so is not a line. Conversely, in \(\mathbb F_3^2\) three distinct points form a line if and only if they sum to zero. There are \(9\cdot3\cdot\binom42=162\) strict colourings. A move from a strict colouring must change one of the eight non-singleton points to the singleton colour because all other moves create a class of size five. It therefore produces a nonstrict state.

Affine maps and colour permutations act transitively on strict colourings. After matching the singleton point and its colour, an invertible linear map can send representative vectors of the two chosen directions of one four-point colour class to representative vectors of the two corresponding directions of the target. It sends the two complementary directions to the two complementary directions as well. These operations preserve the weak graph, so it suffices to compute distances from one strict root, the lexicographic word `001001112`.

The finite check uses all \(3^9\) distinguished colour assignments. Construct the line list as the distinct point triples with zero vector sum; retain exactly those words having no monochromatic listed triple. At coordinate \(i\), bucket retained words by their other eight coordinates and join each pair in each bucket. This builds the full graph because adjacency means agreeing everywhere except one coordinate. Breadth-first search from the root gives the minimum move count on every reached state. Restrict the endpoints to words that use exactly two colours on each line. The included program prints the complete root counts of the table and verifies that all strict endpoints are reached; its two strict endpoints at distance ten are `112112220` and `220220001`, the two cyclic colour renamings. Transitivity transfers the histogram to every strict root and transfers the two endpoints (conjugating a three-cycle by a palette permutation leaves it a three-cycle). Counting each strict pair from both ends multiplies each root count by \(162/2\), giving the third column.

## Verification

Run `python3 verify_strict_distances.py` with a standard Python 3 interpreter. It reconstructs the full weak state space, uses one rooted breadth-first search justified by transitivity on strict states, and checks the histogram and antipode identities. This is a bounded finite proof, with no conclusions about other planes, other palettes, or the induced strict subgraph beyond the absence of edges.

## Relationship to prior work

Colbourn, Dinitz and Rosa, *Bicoloring Steiner Triple Systems*, EJC **6** (1999), #R25, DOI [10.37236/1457](https://doi.org/10.37236/1457), distinguish weak colourings from bicolorings (exactly two colours on every line) and give the \((4,4,1)\) size split for order nine. The [ambient weak-graph classification](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-two-peripheral-affine-types-in-optimal-weak-three-colourings-of--01f5dae5fbed/RESULT.md) gives orbits, degrees, eccentricities, antipode counts, and an all-pairs distance histogram for the full weak graph. The table here instead conditions *both* endpoints to be strict; the all-pairs histogram and eccentricities do not give these restricted counts. Only the strict-endpoint metric is claimed here, not the ambient classification or historical priority.
