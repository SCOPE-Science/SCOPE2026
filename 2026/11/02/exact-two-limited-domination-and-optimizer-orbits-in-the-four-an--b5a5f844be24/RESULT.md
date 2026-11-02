# Exact two-limited domination and optimizer orbits in the four- and five-cubes

## Finding

Let \(Q_d\) be the binary \(d\)-dimensional hypercube. A set \(D\subseteq V(Q_d)\) is *two-limited dominating* when every vertex outside \(D\) has a neighbor in \(D\), and every vertex in \(D\) has at most two neighbors outside \(D\). The minimum order is denoted by \(\gamma^{\mathrm L}_2(Q_d)\).

The two exact previously unlisted cells are
\[
\gamma^{\mathrm L}_2(Q_4)=8,\qquad \gamma^{\mathrm L}_2(Q_5)=16.
\]
There are respectively **428** and **1,830** distinct minimum sets on the labelled cubes. Under the full cube automorphism groups, these sets split into exactly six orbits in each dimension, of sizes
\[
Q_4:\quad 8,12,24,96,96,192;\qquad
Q_5:\quad 10,20,120,240,480,960.
\]
These are counts of subsets, not counts of orbit representatives or of ordered colorings. They apply precisely to \(d=4\) and \(d=5\); no general formula in \(d\) is asserted.

## Assumptions and scope

The vertices of \(Q_d\) are binary words of length \(d\), encoded by the integers \(0,\ldots,2^d-1\). Vertices are adjacent exactly when their encodings differ in one binary position. A subset is encoded by an unsigned bit mask in which bit \(u\) records whether vertex \(u\) belongs to the subset. This convention fixes the labelling for every count and certificate.

The 2-limited condition is the standard one imposing a bound on neighbors *outside* the chosen dominating set. In a \(d\)-regular graph, the same condition demands at least \(d-2\) neighbors *inside* the set at every selected vertex; every unselected vertex must have at least one selected neighbor. These are precisely \((1,d-2)\)-domination constraints in the alternative notation cited in the literature.

## Proof

**1. Exact exhaustive criterion in four dimensions.** For a mask \(X\) of vertices in \(Q_4\), and for each vertex \(u\), put
\[
s_X(u)=\bigl|\{v\in X:v\sim u\}\bigr|.
\]
The following equivalence is immediate from degree four and the definition:
\[
X\text{ is two-limited dominating in }Q_4
\iff
\left\{\begin{array}{ll}
s_X(u)\ge2,&u\in X,\\
s_X(u)\ge1,&u\notin X.
\end{array}\right.
\]
The standalone `verify.cpp` applies this exact test to all \(2^{16}=65,536\) bit masks, in increasing unsigned order. It computes the minimum popcount over feasible masks and stores *every* attaining mask. The computation returns minimum \(8\) and exactly \(428\) attaining masks. This enumeration is exhaustive by construction, rather than a sampled search.

**2. Exhaustive dimension-five reduction to two sixteen-vertex layers.** Identify \(Q_5\) with two \(Q_4\) layers and write a candidate subset as \(D=A\cup B'\), where \(A,B\subseteq V(Q_4)\), and the prime indicates the upper layer. Write \(s_A(u)\) for the number of selected neighbors of vertex \(u\) *inside* the first \(Q_4\) layer. Define the admissibility predicate
\[
P(A):\quad s_A(u)\ge2\quad\text{for every }u\in A,
\]
and the compulsory opposite-layer set
\[
R(A)=\{u\in A:s_A(u)=2\}\ \cup\ \{u\notin A:s_A(u)=0\}.
\]
For selected \(u\in A\), the 2-limited condition in degree five requires at least three selected neighbors. Since exactly one neighbor is vertical, this is equivalent to \(s_A(u)\ge2\), together with selecting its vertical neighbor when \(s_A(u)=2\). For unselected \(u\notin A\), domination requires its vertical neighbor to be selected precisely when \(s_A(u)=0\). The argument is identical in the other layer. Therefore the exact equivalence is
\[
D\text{ is two-limited dominating in }Q_5
\iff P(A)\land P(B)\land R(A)\subseteq B\land R(B)\subseteq A.
\]
The code iterates all \(65,536\) lower-layer masks to construct every admissible \(A\), with no discarded feasible layer. Exactly \(8,122\) masks satisfy \(P\). It then checks all \(8,122^2=65,966,884\) *ordered* admissible pairs against the two required-set containments, including every pair whose size is below the incumbent optimum. This gives minimum cardinality \(16\) and exactly \(1,830\) optimum pairs. Each optimum is independently checked against the original 32-vertex closed condition by iterating all five hypercube neighbors; therefore the reduced representation and direct graph predicate agree on the complete minimum layer. The proof of the equivalence above ensures no feasible pair was skipped, including all potential smaller sizes.

**3. Exact full automorphism orbits.** Every automorphism of a binary hypercube is a coordinate permutation followed by an independent choice of coordinate-bit flips. A generating set consists of flips in each coordinate and swaps of each pair of adjacent coordinate indices. Acting on a selected-set mask, these transformations permute all its vertex bits. The code starts from the complete lists of minimum masks from steps 1 and 2, floods every generated orbit, and deletes its members from the remaining list. It rejects duplicate minima, any transformed mask not already among the feasible minima, any unswept mask, and any wrong orbit sum. The resulting orbit representatives are given below as the **decimal selected-vertex bit masks**; orbit sizes are counts of labelled minimizers:

| Cube | Orbit sizes and canonical least-mask representatives |
| --- | --- |
| \(Q_4\) | \(8:255\); \(12:4080\); \(24:7128\); \(96:975\); \(96:2022\); \(192:987\) |
| \(Q_5\) | \(10:65535\); \(20:16776960\); \(120:63960000\); \(240:1044735\); \(480:4193340\); \(960:1045455\) |

Because the generators generate the full automorphism group, these are orbits under all cube automorphisms, not just under a sampled subgroup. Their sizes add to \(428\) and \(1,830\), respectively. These finite exact tests constitute a reproducible exhaustive computation establishing the stated theorem, not a proof by extrapolation to larger dimensions.

## Verification

The source file `verify.cpp` is a standalone, standard C++17 checker. It uses only integer masks, exact population counts, bit operations, equality tests, and breadth-first exploration of the automorphism generators. For reproducibility, compile and run:

```sh
c++ -O2 -std=c++17 verify.cpp -o verify
./verify
```

The recorded output from the actual source file is:

```text
Q4_EXHAUSTIVE 8 428 SUBSETS_CHECKED 65536
Q5_EXHAUSTIVE 16 1830 ADMISSIBLE_LAYERS 8122 ORDERED_PAIRS 65966884
Q4_SIX_AUTOMORPHISM_ORBITS 8:255 12:4080 24:7128 96:975 96:2022 192:987
Q5_SIX_AUTOMORPHISM_ORBITS 10:65535 20:16776960 120:63960000 240:1044735 480:4193340 960:1045455
VERIFY_OK
```

The public program is the complete finite certificate and has no external files or library dependencies beyond a C++17 compiler. The checker does not claim an infinite-dimensional theorem or independent human validation.

## Relationship to prior work

Aleksandra Tepeh's manuscript *On \(k\)-limited domination: complexity and Cartesian products*, originally publicly posted on 2026-06-21, provides the definitions, relates limited domination in regular graphs to \((1,t)\)-domination, and displays a table of known hypercube values (Table 3). Its accessible first-version full text leaves the \(k=2\), \(d=4,5\) entries unfilled. The present result fills precisely those two cells and additionally enumerates the labelled minimizers and their full symmetry orbits; none of the resulting counts follows solely from the earlier stated bounds.

Božović's subsequent *On \(k\)-limited domination: complexity and Sierpiński graphs* determines different graph families. The earlier foundational article *On \(k\)-limited domination in graphs* gives the general theory but not these explicit optimizer censuses. Existing exact hypercube total-domination statements apply to the distinct regime \(k=d-1\), so they do not give either present \(k=2\) result. The earlier hypercube perfect-domination literature concerns a different neighbor-condition. A full historical uniqueness claim is not made.

## Limitations

The values and orbit counts were proved by complete finite enumeration for the two indicated cubes; they have no claimed extension to larger dimensions. Their correctness is conditional on the auditable, standalone program and the stated layer-equivalence proof. Historical priority is provisional, particularly because not every version or inaccessible appendix of every potentially related paper could be examined. The computation has been reviewed together with the proof, but no independent audit or external validation has been performed.

## References

1. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (first public version 2026-06-21), https://arxiv.org/abs/2606.22428 .
2. D. Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs*, arXiv:2610.01584 (2026-10-01), https://arxiv.org/abs/2610.01584 .
3. *On \(k\)-limited domination in graphs*, *Computational and Applied Mathematics* (2026), https://doi.org/10.1007/s40314-026-03902-2 .
4. P. M. Weichsel, *Dominating sets in n-cubes*, *Journal of Graph Theory* 18 (1994), 479–488, https://doi.org/10.1002/jgt.3190180506 .
