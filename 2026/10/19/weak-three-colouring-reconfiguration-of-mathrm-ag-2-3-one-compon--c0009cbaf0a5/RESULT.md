# Weak three-colouring reconfiguration of \(\mathrm{AG}(2,3)\): one component of diameter ten

## Finding

Let \(\mathcal A=\mathrm{AG}(2,3)\) be the nine-point affine plane, equivalently the Hesse \((9_4,12_3)\) configuration or the unique Steiner triple system of order nine. Use three **distinguished** colours. A weak colouring assigns one of these colours to each point such that no affine line of three points is monochromatic. Join two weak colourings when they differ at **exactly one point**. The resulting undirected reconfiguration graph \(\mathcal R_3(\mathcal A)\) is connected, with
\[
 |V(\mathcal R_3)|=3762,\qquad |E(\mathcal R_3)|=16848,\qquad \operatorname{rad}(\mathcal R_3)=9,\quad \operatorname{diam}(\mathcal R_3)=10.
\]
Its degree distribution is \(162\) vertices of degree \(8\) and \(3600\) vertices of degree \(9\). The colour-class-size distributions (unordered sizes) are precisely \((1,4,4)\), \((2,3,4)\), and \((3,3,3)\), occurring respectively \(162\), \(2592\), and \(1008\) times. Every line uses exactly two colours in precisely the \(162\) colourings of type \((1,4,4)\), i.e. the strict bicolorings in the terminology of Colbourn–Dinitz–Rosa. Those \(162\) colourings are mutually nonadjacent and individually isolated **within their induced subgraph**, yet all connect through weak three-colourings using the same palette. In the full graph every one of them has eight legal exits, and has eccentricity ten.

The complete eccentricity profile, sorted by the unordered colour-class sizes, is: \((1,4,4)\): \(162\) with eccentricity ten; \((2,3,4)\): \(2592\) with eccentricity nine; \((3,3,3)\): \(864\) with eccentricity nine and \(144\) with eccentricity ten. No other eccentricities occur.

## Assumptions and scope

The points are the nine pairs \((x,y)\in\mathbb F_3^2\), ordered lexicographically as \((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)\) and indexed \(0,\ldots,8\). The twelve lines are the distinct sets \(\{(x,y)+t(u,v):t\in\mathbb F_3\}\), for \((u,v)\in\{(1,0),(0,1),(1,1),(1,2)\}\). Every two points lie on exactly one of the twelve lines, and each point lies on four lines. The three colour names are fixed, and a move recolours one point; no simultaneous recolourings or colour-name identifications are allowed.

All claims concern this **specific finite configuration** and this precise move. They make no assertion for general affine planes, higher orders, arbitrary Steiner triple systems, or other recolouring operations.

## Proof

**Elementary structural reductions.** A subset of points containing no complete line (an *arc*) has size at most four. For if an arc of size five existed, its ten point pairs, each on a unique line, would force ten lines to contain exactly two of its points. These ten lines already account for all \(5\cdot4=20\) point–line incidences contributed by the arc. Hence the remaining two lines would each miss all five points. Their union has at least five points, impossible because only four points lie outside the arc. Every weak colour class is an arc, so its size is at most four.

There is no weak two-colouring: if the red class has size \(r\), each line has one or two red points. Writing \(u\) for the number of lines with two red points, incidence counting gives \(4r=12+u\). Pair counting gives \(u=\binom r2\). Consequently \(r^2-9r+24=0\), whose discriminant is negative. Thus all valid three-colourings use all three colours, with unordered class sizes among \((1,4,4),(2,3,4),(3,3,3)\).

In any weak three-colouring, every two-coloured line contains exactly one equal-colour pair and every rainbow line contains none. Because every pair of points belongs to exactly one line, the number of rainbow lines equals \(12-\sum_{i=1}^3\binom{c_i}{2}\), where \(c_i\) are the class sizes. This number is respectively \(0,2,3\) for the three size types. In particular, the strict bicolorings are exactly the \((1,4,4)\) colourings.

Fixing point \(0\) as a singleton class, precisely six four-point arcs have four-point-arc complements among the remaining eight points: \(\{1,2,3,6\}\), \(\{1,2,4,8\}\), \(\{1,2,5,7\}\), \(\{3,4,6,8\}\), \(\{3,5,6,7\}\), and \(\{4,5,7,8\}\). These six possibilities can be checked against the twelve displayed affine lines; translation symmetry gives the same count for every singleton point. There are therefore \(9\cdot3\cdot6=162\) labelled bicolorings. Any of the eight points outside the singleton can legally change to the singleton's colour: the new two-point class cannot contain a line and its former four-point class remains an arc. All other single-point recolourings would create a five-point class, so every strict bicoloring has degree eight. A single recolouring changes its class sizes, so no two strict bicolorings are adjacent.

**Finite exhaustive lemma.** For the remaining exact counts, connectivity and distances, the following fully specified finite enumeration supplies a proof. Enumerate each of the \(3^9=19683\) nine-digit ternary words. Retain a word if and only if no one of the twelve explicitly generated lines has three equal digits. For each retained word and each of the nine positions, try both other digits, retaining precisely those changes whose resulting word also passes the line test. This constructs the entire undirected simple graph, not a sample. Breadth-first search from **each** retained word visits every word and records its greatest distance. The attached standalone implementation `verify_coordinates.py` executes exactly these loops and asserts the reported cardinalities, degrees and eccentricities; therefore each computation has a finite, transparent exhaustive domain.

As a logically separate reconstruction, `verify_arcs.py` lists all \(2^9\) subsets as bit masks, retains exactly the subsets containing no listed line, and enumerates all ordered triples of disjoint arcs partitioning the nine points. It constructs edges by transferring one point from one colour-class bit mask to another while preserving the arc condition. It repeats all breadth-first searches, using a differently represented state space and a separately entered incidence list. The two programs give identical sorted vertex and edge SHA-256 fingerprints and identical full numerical summaries (see below). The set-partition method exhausts precisely the same weak-colouring domain because a colouring is exactly an ordered partition into three line-free classes. Both methods establish the lemma without sampling, random trials, or any unproved large-order inference.

The exact degrees sum to \(162\cdot8+3600\cdot9=33696\), proving the edge total \(16848\) by the handshaking identity. All \(3762\) graph-search runs reach all \(3762\) states; the greatest recorded distance is ten and the least eccentricity is nine. For an explicit extremal pair, the row-major ternary words `001001112` and `112112220` have distance ten. A legal ten-move path is

`001001112 -> 201001112 -> 202001112 -> 202101112 -> 202101212 -> 212101212 -> 212101210 -> 212102210 -> 112102210 -> 112102220 -> 112112220`.

The exhaustive breadth-first search from the first endpoint confirms there is no shorter path.

## Verification

Run from the folder containing the included files:

```
python3 verify_coordinates.py
python3 verify_arcs.py
```

Each program prints a canonical JSON summary followed by `VERIFY_OK`; its complete recorded output is included in `verification_coordinates.txt` or `verification_arcs.txt`. The two output files agree byte-for-byte. Canonically sorted vertices hash to `931e08d1d6167e59e0246e3747fbe8e4527e217a5aae4c5d898c742425bb1234`; sorted undirected edge-index pairs hash to `fda7d2573c23bb1a48c821fb4228c254fbd6fa5575728e8b1d5c7b33128d1ff9`. These are reproducibility fingerprints, not substitutes for inspecting the programs and their exhaustive domains.

The exact distance distribution among the \(\binom{162}{2}=13041\) unordered pairs of distinct strict bicolorings has counts \(2592,1782,1296,6480,648,81,162\) at distances \(4,5,6,7,8,9,10\), respectively. In particular every pair of distinct strict bicolorings requires at least four moves through weak colourings with rainbow lines.

## Relationship to prior work

Colbourn, Dinitz and Rosa (1999) study strict bicolorings of Steiner triple systems, explicitly give the \((4,4,1)\) size split for the Steiner triple system of order nine, and define weak colourings. That paper does not give the present single-point-recolouring graph or its distances. The existence of a strict bicoloring and the underlying chromatic minimum are **not** claimed as new here.

The later work on arc-proper colourings of finite affine planes (arXiv:2601.19043) treats no-three-collinear colour classes, proves the minimal palette for odd orders, and enumerates minimum colourings in the **different** order-four affine plane. The inspected material has no single-point recolouring theorem for the nine-point plane. Cardinal–Demaine–Eppstein–Hearn–Winslow (arXiv:1805.04055) study reconfiguration of Boolean not-all-equal constraints, principally with two colours and hardness for varying instances, not this fixed three-colour Hesse graph. No inspected source implies the exact connectivity or diameter asserted here.

## Limitations

This is a finite, computer-assisted exact result: the numerical connectivity and metric assertions depend on the complete, bounded enumerations in the included readable programs, not on a symbolic closed-form distance formula or a theorem for all affine orders. Search cannot establish universal publication priority; equivalent work not indexed under the searched terminology remains possible. The provided checks are reproducibility aids and are not external mathematical certification. The bicolouring counts concern **labelled** point assignments and distinguished colours, not isomorphism classes.

## References

1. C. J. Colbourn, J. H. Dinitz and A. Rosa, *Bicoloring Steiner Triple Systems*, Electronic Journal of Combinatorics **6** (1999), #R25, DOI: `10.37236/1457`, publicly dated 1999-05-24. Open full text: `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v6i1r25/pdf/`.
2. G. Araujo-Pardo and L. Martínez-Sandoval, *The arc chromatic number for Galois projective planes, affine planes and Euclidean grids*, arXiv:2601.19043, `https://arxiv.org/pdf/2601.19043` (inspected sections 2, 4 and 6).
3. J. Cardinal, E. D. Demaine, D. Eppstein, R. A. Hearn and A. Winslow, *Reconfiguration of Satisfying Assignments and Subset Sums: Easy to Find, Hard to Connect*, arXiv:1805.04055, `https://arxiv.org/html/1805.04055v1` (inspected sections 1–2).
