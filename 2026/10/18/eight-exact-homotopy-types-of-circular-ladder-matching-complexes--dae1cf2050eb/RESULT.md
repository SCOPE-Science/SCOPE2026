# Eight exact homotopy types of circular-ladder matching complexes

## Finding

For every integer \(3\le n\le10\), let \(L_n=C_n\square K_2\) be the circular-ladder graph, and let \(\mathcal M(L_n)\) be its **ordinary matching complex**, with one vertex per graph edge and a simplex for each collection of pairwise vertex-disjoint graph edges. The complete homotopy classifications in this range are:

| \(n\) | Homotopy type of \(\mathcal M(L_n)\) |
|:---:|:---|
| \(3\) | \(\bigvee^{6}S^1\) |
| \(4\) | \(\bigvee^{4}S^2\) |
| \(5\) | \(\bigvee^{2}S^2\vee\bigvee^{2}S^3\) |
| \(6\) | \(\bigvee^{12}S^3\) |
| \(7\) | \(\bigvee^{14}S^4\) |
| \(8\) | \(\bigvee^{3}S^4\vee\bigvee^{7}S^5\) |
| \(9\) | \(\bigvee^{24}S^5\) |
| \(10\) | \(\bigvee^{40}S^6\) |

In particular, \(n=5\) and \(n=8\) give natural **mixed-dimensional** wedges. These are integral homotopy equivalences, not conclusions drawn solely from Betti numbers or experiments.

## Assumptions and scope

The graph \(L_n\) has vertex set \(\{(i,a):i\in\mathbb Z/n\mathbb Z,\ a\in\{0,1\}\}\). Its edges are the \(2n\) cycle edges \(\{(i,a),(i+1,a)\}\) and the \(n\) spokes \(\{(i,0),(i,1)\}\), where the first coordinate is taken modulo \(n\). This is a simple cubic graph for every \(n\ge3\). A matching is any, possibly nonperfect, pairwise disjoint edge set. The perfect-matching subcomplex is a different object and is not used here. All simplicial chains below use integral coefficients, with vertices indexed by the lexicographic order of these \(3n\) graph edges.

The theorem makes **exactly eight statements** for \(3\le n\le10\), and no assertion for \(n\ge11\). It does not give an equivariant action, a persistent filtration, or a recurrence for the entire infinite family.

## Proof

**1. Exhaustive face model.** Label the graph vertices \(0,\ldots,n-1,n,\ldots,2n-1\), build the cycle and spoke edges, and sort all edges lexicographically. A matching is represented by its \(3n\)-bit mask. Starting with the empty mask, add each graph edge precisely when the selected edges share no endpoint with it. Induction on the processed graph edges shows that every matching occurs **once**, so the face enumeration is exhaustive. Including the empty face, the successive numbers of faces for \(n=3,4,5,6,7,8,9,10\) are respectively \(32,108,342,1104,3544,11396,36626,117732\).

**2. Reproducible acyclic matching.** Process first the last \(n\) edges of the sorted list and then the first \(2n\) edges. For each processed edge, pair every currently unpaired face not containing that edge with the face obtained by inserting it, provided both belong to the current unpaired set. Every pair is a valid one-edge face inclusion, and pairs at each stage are disjoint. Remove the pair involving the empty face and regard its upper member as the unique unmatched zero-cell. For the remaining face poset, orient all cover edges downward except the paired edges, which are oriented upward. The verifier explicitly constructs all these directed incidences and topologically sorts their full directed Hasse graph. It visits **every** nonempty face for each of the eight inputs, proving acyclicity without assuming a heuristic ordering theorem.

The unmatched positive-dimensional cells are, by dimension:

| \(n\) | Critical cells above dimension zero |
|:---:|:---|
| \(3\) | six in dimension \(1\) |
| \(4\) | four in dimension \(2\) |
| \(5\) | two in dimension \(2\), two in dimension \(3\) |
| \(6\) | twelve in dimension \(3\) |
| \(7\) | fourteen in dimension \(4\) |
| \(8\) | four in dimension \(4\), eight in dimension \(5\) |
| \(9\) | twenty-six in dimension \(5\), two in dimension \(6\) |
| \(10\) | forty in dimension \(6\) |

**3. Exact integral Morse differential.** The boundary of an oriented simplex is the alternating sum obtained by removing each ordered graph-edge vertex. For a matched lower cell \(f\) and upper cell \(t\), the signed gradient-path recursion passes through every other codimension-one face of \(t\), using the negative ratio of its incidence sign to that of \(f\) in \(t\). Acyclicity makes this recursion finite. Summing these signed flows from each critical upper cell to critical lower cells computes the **integral** cellular Morse boundary, not just a mod-two matrix. The only parameters with critical cells in consecutive positive dimensions are \(n=5,8,9\):

- For \(n=5\), the exact \(2\times2\) boundary from dimension \(3\) to dimension \(2\) vanishes.
- For \(n=8\), the exact \(4\times8\) boundary has only rows two and four nonzero, both equal to \((1,0,-1,0,0,0,0,0)\). Its sole nonzero Smith factor is \(1\).
- For \(n=9\), the exact \(26\times2\) boundary has rank \(2\); rows three and fourteen give a \(2\times2\) identity minor. Integer unit-pivot elimination verifies that the residual matrix is zero. Both nonzero Smith factors are \(1\).

All other relevant positive-dimensional Morse differentials are zero because the critical dimensions do not occur consecutively.

**4. From Morse CW complexes to the homotopy types.** Acyclic discrete Morse theory yields a CW complex with one zero-cell and exactly the positive-dimensional critical cells just listed, with the displayed cellular boundary matrices. For \(n=3\), a connected CW complex with one vertex and six one-cells is a wedge of six circles. When all positive-dimensional cells lie in one dimension, their attaching maps land in a point; the result is a wedge in that dimension. In the mixed-dimensional cases, the lower positive-dimensional cell dimension is at least \(2\). The CW complex is then simply connected and has no cells below that dimension. Its relevant attaching maps to a wedge of spheres of dimension \(d\ge2\) are classified by their integer degrees because \(\pi_d(\bigvee S^d)\cong H_d(\bigvee S^d;\mathbb Z)\). Changing the cellular bases by unimodular operations corresponds to homotopy equivalences of the lower wedge and elementary transformations among higher cells; unit entries cancel sphere-cell pairs. Zero attaching degrees give nullhomotopic maps. Thus the exact matrices above leave the wedges stated in the table, with no torsion or hidden attaching maps.

## Verification

Run `python3 verify_prism.py` with Python 3 and standard library only. The supplied script independently enumerates all matching simplices, constructs and acyclicity-checks the complete face-poset matching, recomputes signed Morse differentials and verifies their unit-pivot reductions, computes Euler characteristics, and computes reduced simplicial homology over \(\mathbb F_2\) directly from the original face complex for **every** parameter \(3\le n\le10\). It prints `VERIFY_OK` only if all assertions pass.

The largest case has \(117732\) faces including the empty face and \(714010\) face-cover incidences. The Morse matching contains \(58845\) pairs and leaves one critical vertex and forty six-dimensional critical cells. Direct mod-two homology is a separate corroboration; the exact integral signed Morse differential is required for the integral and homotopy conclusions.

## Relationship to prior work

Donovan and Scoville [1] develop matching-complex methods and classify paths, cycles and Dutch windmill graphs, but do not provide the circular-ladder matching-complex table. Polygonal **line** tilings [2] involve chains of polygonal tiles, unlike the cyclic annulus here. Results for outerplanar graphs [3] do not apply: every finite simple outerplanar graph has a vertex of degree at most two, while each \(L_n\) is cubic. Categorical products of paths [4] are not Cartesian circular ladders.

Agarwal and Basak [5] determine independence complexes and **perfect** matching complexes for circular ladders. Their Problem 26 explicitly identifies the **ordinary** matching complex of circular ladders as a distinct future direction. Their results do not imply the eight homotopy types above: the ordinary matching complex includes nonperfect matchings absent from the perfect-matching subcomplex. Relevant prior small-grid matching-complex results concern open ladders rather than the cyclic closure. The exact finite classifications here are also distinct from Morse complexes of graph incidence matchings, which encode discrete gradient vector fields, not ordinary graph-edge matchings.

## Limitations

Only \(3\le n\le10\) is proved. No periodicity, universal recurrence or all-parameter formula is inferred from eight values. Although the verification is exhaustive for each of these eight finite graphs, it is not an infinite-family argument. The proof uses an exact enumerative discrete-Morse certificate rather than a compact symbolic classification. The literature comparison is substantial but cannot exclude an unindexed equivalent computation. Independent external validation has not been performed.

## References

1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1 (first public July 27, 2022); primary MSC 57Q70.
2. M. Bayer, M. M. Jelić Milutinović, and J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559v2.
3. M. Bayer, M. M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v2.
4. *On the matching complexes of categorical product of path graphs*, arXiv:2403.15298v2.
5. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, especially Problem 26 (September 2026).
6. B. Braun and W. K. Hough, *Matching and independence complexes related to small grids*, Electronic Journal of Combinatorics 24(4) (2017).
