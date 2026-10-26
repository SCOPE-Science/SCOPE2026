# First gapped anti-forcing spectrum in the hypercube sequence

## Finding

For the binary hypercube \(Q_d\), write \(\operatorname{af}(M)\) for the minimum number of edges *outside* a perfect matching \(M\) whose deletion leaves \(M\) as the unique perfect matching. The anti-forcing spectra in dimensions \(d=1,2,3,4\) are, respectively,
\[
\{0\},\qquad \{1\},\qquad \{3,4\},\qquad \{8,10,12\}.
\]
Thus \(Q_4\) is the first positive-dimensional hypercube whose anti-forcing spectrum is not an integer interval. Its complete anti-forcing polynomial is
\[
A_{Q_4}(z)=\sum_{M\text{ perfect}}z^{\operatorname{af}(M)}
=196z^{8}+72z^{10}+4z^{12}.
\]

All \(272\) perfect matchings of \(Q_4\) have ordinary forcing number \(4\). Under the full \(384\)-element graph automorphism group there are exactly eight orbits. For a perfect matching \(M\), let \(c(M)\) count the four-edge subsets of \(M\) which belong to no other perfect matching. The orbit census is:

| Orbit | Orbit size | \(\operatorname{af}(M)\) | \(c(M)\) | Direction multiplicities | Representative |
|---|---:|---:|---:|---|---|
| A | 4 | 12 | 2 | (8) | `01/23/45/67/89/AB/CD/EF` |
| B | 8 | 8 | 24 | (2,2,2,2) | `01/26/3B/4C/57/8A/9D/EF` |
| C | 12 | 8 | 12 | (4,4) | `01/23/46/57/8A/9B/CD/EF` |
| D | 24 | 10 | 4 | (4,4) | `01/23/45/67/8A/9B/CE/DF` |
| E | 32 | 8 | 18 | (2,2,2,2) | `01/23/46/5D/7F/8C/9B/AE` |
| F | 48 | 10 | 4 | (6,2) | `01/23/45/67/89/AB/CE/DF` |
| G | 48 | 8 | 8 | (4,2,2) | `01/23/45/67/8A/9D/BF/CE` |
| H | 96 | 8 | 10 | (4,2,2) | `01/23/45/6E/7F/8A/9B/CD` |

Representatives encode each vertex by a hexadecimal digit from `0` to `F` (its four-bit binary value). Each two-digit token encodes one edge. The direction multiplicities record the positive numbers of matching edges in the four coordinate directions, sorted decreasingly. In particular, direction counts alone do not determine the anti-forcing number: orbits C and D have the same counts \((4,4)\), but anti-forcing numbers \(8\) and \(10\).

## Assumptions and scope

Vertices of \(Q_d\) are the vectors of \(\mathbb F_2^d\); two vectors are adjacent exactly when they differ in one coordinate. All vertices, directions and matching edges are distinguished before graph automorphisms are applied. A forcing set of \(M\) means a subset of \(M\) contained in no other perfect matching, whereas an anti-forcing set is a subset of \(E(Q_d)\setminus M\) whose *deletion* leaves \(M\) unique. The complete census has been proved only for the explicitly stated dimensions \(1\le d\le4\); no spectrum statement for higher dimensions follows.

## Proof

**1. Exhaustive perfect-matching universe.** Given a set \(U\) of currently unmatched vertices, choose its numerically least vertex \(u\). For every available neighbour \(v\in U\), match \(u\) to \(v\) and recurse on \(U\setminus\{u,v\}\). These branches are disjoint, and every perfect matching follows exactly one branch at every step. The recursion gives \(272\) distinct perfect matchings of \(Q_4\). An independent bipartite permanent-by-subsets recurrence (even vertices as rows and odd vertices as columns) also gives \(272\).

**2. Ordinary forcing.** For each matching \(M\), enumerate its \(256\) edge subsets. A subset \(S\subseteq M\) forces \(M\) if and only if \(S\) is not included in any other enumerated perfect matching. This criterion is definitional, and the exhaustive universe established in step 1 makes the finite test exact. All \(272\) minima have cardinality four. The numbers of successful cardinality-four subsets are the values \(c(M)\) in the table.

**3. Anti-forcing reduces exactly to a directed feedback-arc set.** For each matching \(M\) of \(Q_4\), orient each nonmatching edge from its even-weight endpoint to its odd-weight endpoint. Contract every matching edge to one vertex, producing an eight-vertex directed multigraph \(D_M\) with \(24\) arcs. Directed cycles of \(D_M\) correspond to alternating cycles relative to \(M\); deleting nonmatching edges makes \(M\) unique if and only if the remaining contracted digraph is acyclic. In one direction an alternating cycle switches to a second perfect matching; conversely the symmetric difference of two distinct perfect matchings contains an alternating cycle. Thus \(\operatorname{af}(M)\) is the fewest arcs one must delete from \(D_M\) to make it acyclic.

For an eight-vertex directed multigraph with multiplicities \(a_{ij}\), every acyclic retained arc set admits a topological ordering. Conversely, retaining all arcs pointing forward under any ordering is acyclic. Hence the largest possible retained arc set is determined by the recurrence
\[
F(\varnothing)=0,\qquad
F(S)=\max_{j\in S}\left(F(S\setminus\{j\})+
\sum_{i\in S\setminus\{j\}}a_{ij}\right).
\]
The exact value is \(\operatorname{af}(M)=24-F(\{1,\ldots,8\})\). Evaluating this integer recurrence on all \(256\) subsets for each of the \(272\) matchings yields multiplicities \(196,72,4\) for values \(8,10,12\), respectively. No optimization tolerance, search cutoff, or statistical inference enters this computation.

**4. Symmetry completeness.** Every automorphism of \(Q_4\) is a coordinate permutation followed by an independent bit translation, and all such maps are automorphisms. This is the full group since the image of the all-zero vertex has \(16\) choices, and images of its four neighbours have at most \(4!\) choices; the hypercube adjacency structure fixes every remaining vertex inductively. Enumerating all \(16\cdot4!=384\) maps partitions the matching universe into the eight orbits listed. Every forcing and anti-forcing statistic is invariant under automorphisms. The eight orbit sizes sum to \(272\), and their anti-forcing and minimum-forcing counts reproduce the complete distributions.

**5. Smaller dimensions and the first gap.** The same unmatched-vertex matching enumeration and directed-acyclicity recurrence applied directly to \(Q_1,Q_2,Q_3\) gives respectively \(1,2,9\) perfect matchings and anti-forcing multiplicities \((0:1)\), \((1:2)\), and \((3:6,4:3)\). Each of these spectra is an integer interval, whereas \(\{8,10,12\}\) is not. This proves the first-gap assertion in the stated sequence.

## Verification

`verify.py` independently checks the bipartite permanent count, enumerates all matchings and all candidate ordinary forcing subsets, evaluates the feedback-arc dynamic program, and generates all \(384\) cube automorphisms. On one representative from **each** of the eight orbits it independently enumerates all \(8!=40320\) vertex orders rather than using the recurrence, obtaining the same anti-forcing number. All of the assertions in the program pass; the final line printed is `VERIFY_OK`. The program also directly enumerates the smaller-dimensional anti-forcing spectra. The executable source is part of this package and requires Python 3 with no third-party dependencies.

## Relationship to prior work

The forcing-number problem on hypercubes was studied by Adams, Mahdian and Mahmoodian (2004) and by Riddle (2002). Lei, Yeh and Zhang (first posted 2014) formalized individual-matching anti-forcing numbers and their alternating-cycle characterization. Deng and Zhang (first posted 2016) studied extremal anti-forcing numbers and spectra, including even polygonal chains. Shi and Zhang (first posted 2017) proved that the maximum anti-forcing number of \(Q_d\) is \((d-1)2^{d-2}\) and that exactly \(d\) coordinate matchings attain it. Consequently the value \(12\) and its multiplicity \(4\) for \(Q_4\) are **previously known**, not asserted to be new. The additional information here is the precise submaximal multiplicities \(196\) and \(72\), the first spectrum gap, and the full eight-orbit forcing/anti-forcing refinement. The cited general maximum theorem by itself does not determine these data.

## Limitations

This is an exact finite classification, not a theorem about the anti-forcing spectrum in dimensions beyond four. The 2004 hypercube forcing paper was accessible at abstract level but not in full; a prior unindexed enumeration of the joint forcing and anti-forcing profile cannot be ruled out. The 2017 maximum anti-forcing theorem already accounts for the top degree and its four extremizers. Other published finite tables may cover part of the remaining spectrum. All counts and the recurrence are reproducible, but the work has not undergone independent external audit.

## References

1. P. Adams, M. Mahdian and E. S. Mahmoodian, *On the forced matching numbers of bipartite graphs*, Discrete Mathematics **281** (2004), 1–12, doi:10.1016/j.disc.2002.10.002.
2. M. E. Riddle, *The minimum forcing number for the torus and hypercube*, Discrete Mathematics **245** (2002), 283–292.
3. H. Lei, Y.-N. Yeh and H. Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796 (first posted 2014-06-15), doi:10.1016/j.dam.2015.08.024.
4. K. Deng and H. Zhang, *Extremal anti-forcing numbers of perfect matchings of graphs*, arXiv:1607.05392 (first posted 2016-07-19), doi:10.1016/j.dam.2017.02.024.
5. L. Shi and H. Zhang, *Tight upper bound on the maximum anti-forcing numbers of graphs*, arXiv:1704.04124 (first posted 2017-04-13), doi:10.23638/DMTCS-19-3-9.
