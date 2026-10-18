# Directed Young-diagram cover graphs are counting-refinement rigid up to conjugation

## Finding

Let \(\lambda=(\lambda_0,\ldots,\lambda_{h-1})\) be any nonempty integer partition in weakly decreasing positive order. Its Young-diagram cell poset has vertex set
\[
D_\lambda=\{(i,j):0\le i<h,\ 0\le j<\lambda_i\}
\]
with coordinatewise order. Give its Hasse graph the **upward direction**: \((i,j)\to(i+1,j)\) and \((i,j)\to(i,j+1)\) whenever both cells are present. Start every vertex with one common colour, and in each round replace a colour by the ordered triple of its previous colour, the multiset of colours of immediate in-neighbours, and the multiset of colours of immediate out-neighbours. Write \(\lambda'\) for the conjugate partition obtained by transposing the diagram.

**Theorem (two-part classification).** For every nonempty partition \(\lambda\):

1. If \(\lambda\ne\lambda'\), the stable colour classes in its oriented Hasse graph are all singletons. If \(\lambda=\lambda'\), the stable colour classes are exactly the sets \(\{(i,j),(j,i)\}\), with the obvious singleton interpretation on the diagonal. In both cases these are precisely the automorphism orbits.
2. If two such graphs have identical global vertex-colour multisets under simultaneous counting refinement, their Young diagrams are isomorphic as directed cell posets, equivalently their partitions differ at most by conjugation. Thus the directed-cover counting fingerprint is a complete isomorphism invariant **relative to this family**.

In particular, writing \(n=|D_\lambda|\) and letting \(d\) be the number of diagonal cells, the number of stable classes is \(n\) for non-self-conjugate \(\lambda\), and \((n+d)/2\) for self-conjugate \(\lambda\). Every class has size one or two. The two eight-cell shapes \(\lambda=(4,3,1)\) and \(\mu=(4,2,2)\) have *identical* distributions of rank and root-to-cell binomial path counts, yet their directed counting-refinement fingerprints differ. Thus the full local neighbour refinement carries information beyond that initial path statistic.

## Assumptions and scope

The poset consists of all cells of a northwest-closed, unskewed Young/Ferrers diagram: if \((i,j)\) belongs, every \((a,b)\) with \(0\le a\le i\) and \(0\le b\le j\) belongs. Both arc directions are counted **separately** by the refinement procedure. The graph is not the undirected grid and does not include all transitive comparabilities. No external marking is present. No upper bound is imposed on the number of rows, columns, or cells. The comparison assertion concerns other graphs *of the same Young-diagram cover form*, not arbitrary digraphs.

## Proof

**1. The rooted path invariant.** The cell \(o=(0,0)\) is the unique vertex of indegree zero. It is therefore a singleton class after one refinement round. In a stable colour partition, the incoming and outgoing numbers of neighbours in any particular colour class are constant across that class. Consequently the number of directed walks of every length from \(o\) is constant on each stable class: start with the indicator of the distinguished singleton \(o\), then multiply repeatedly by the incoming adjacency operator. Since each coordinate step increases the sum of the coordinates by one, walks from \(o\) to \((i,j)\) exist only at length \(s=i+j\). Northwest closure ensures that every sequence of \(i\) downward and \(j\) rightward unit steps stays in \(D_\lambda\). Therefore their number is
\[
W_s(i,j)=\binom{i+j}{i}.
\]
If two cells have the same stable colour, they have the same \(s\) and the same binomial coefficient. For fixed \(s\), \(\binom{s}{k}\) is strictly increasing for \(0\le k\le\lfloor s/2\rfloor\), with only the familiar symmetry \(k\leftrightarrow s-k\). Hence the only two *different* cells potentially sharing a stable colour are transposes \((i,j)\) and \((j,i)\).

**2. Propagation of a hypothetical transpose-colour equality.** Suppose \(i<j\), both \((i,j)\) and \((j,i)\) exist, and their stable colours agree. When \(i\ne j\), the two possible immediate predecessors have distinct pairs \(\{a,b\}\) of unordered coordinates; the same is true for the two possible immediate successors. The rooted path invariant already distinguishes these two types whenever both occur. Equitability therefore forces the following property for every possible unit predecessor or successor \(q\) of \((i,j)\): its transpose \(q^T\) is a corresponding neighbour of \((j,i)\), and the stable colours of \(q,q^T\) agree. The converse follows symmetrically. The rule is applied only to off-diagonal pairs; a diagonal neighbour matches itself.

Apply the predecessor rule along a path that first reduces the smaller coordinate to zero and then reduces the larger coordinate to one. This path stays strictly off the diagonal and remains inside the northwest-closed diagram, so equality propagates to \((0,1)\) and \((1,0)\).

For any present cell \((a,b)\) strictly above the diagonal, with \(a<b\), there is a path from \((0,1)\) to \((a,b)\) that first moves right to \((0,b)\) and then moves down to \((a,b)\). It stays strictly above the diagonal and in the northwest-closed diagram. Repeated application of the successor rule forces the transposed cell \((b,a)\) to exist, with the same stable colour. Applying the same argument below the diagonal yields the reverse inclusion. Every diagonal cell is already its own transpose. Thus the entire shape is transpose-invariant: \(\lambda=\lambda'\).

Therefore **any** nontrivial stable colour class forces self-conjugacy. When \(\lambda\) is self-conjugate, coordinate transpose is an actual directed graph automorphism, so every transpose pair does have one common stable colour. Step 1 rules out larger classes. This proves the exact stable classes. Since automorphisms always preserve the colour refinement, the same argument identifies their orbits and supplies the stated class counts.

**3. Comparison across two shapes.** Perform the refinement with one common colour vocabulary on the disjoint union of two Young-diagram cover graphs. The restrictions of this refinement to each component have the same internal equality classes as refinement on that component alone. Suppose that the two final component colour histograms agree. If one shape is self-conjugate and has more than one cell, some colour occurs twice there, whereas in any non-self-conjugate shape every colour occurs once; therefore both shapes must be self-conjugate or both non-self-conjugate (the one-cell case is unique).

If both are non-self-conjugate, every colour occurs at most once per component. Matching vertices of equal colours gives a bijection, and the stable incoming/outgoing neighbour-colour multisets force that bijection to preserve every directed arc. Thus the two graphs are isomorphic.

If both are self-conjugate, the class of all indegree-zero roots in the disjoint union is itself colour-definable, so the same walk-count invariant applies componentwise and identifies, for every colour, its rank \(s\) and binomial path count, hence its unordered coordinate pair \(\{i,j\}\). As each shape is transpose-invariant, the resulting multiplicity (one for a diagonal cell, two for an off-diagonal pair) specifies exactly which coordinates belong to the shape. The two shapes are identical as cell sets. This proves the global fingerprint claim. Conjugation always gives a directed graph isomorphism; conversely an isomorphism preserves the same rooted path invariant, and the singleton-pair argument above shows that only the two conjugate forms can occur.

## Verification

Two standalone standard-library Python programs implement the oriented cover edges directly. `verify_global.py` generates every partition of each size \(1\le n\le18\), simultaneously runs counting refinement on all such graphs of a fixed size, checks the exact internal stable classes and checks that global fingerprints coincide exactly on conjugate pairs. It verifies 1,596 partitions. `verify_cellwise.py` independently builds and refines 1,806 test shapes (six fixed shapes and 1,800 fixed-seed random partitions), comprising 124,300 cells, also checking that the number of root-to-cell directed paths is the indicated binomial coefficient. The included logs record successful execution. These tests corroborate but do not establish the infinite theorem.

Run from the package root with `python3 verify_global.py` and `python3 verify_cellwise.py`. No external Python dependencies are required.

## Relationship to prior work

Classical partition conjugation and northwest-closed Ferrers/Young diagrams are standard; Callan (2005) provides a day-verifiable early source for the conjugation background. Arvind, Köbler, Rattan, and Verbitsky (2015) establish the general colour-refinement framework and the undirected-graph notion of amenability/refinability. Kiefer, Schweitzer, and Selman (2015) establish general \(C^2\) classification methods for finite relational structures and clarify that orbit-exactness and absolute identification are different concepts for relational structures. These works are background, not claimed as new.

The present claim concerns **oriented cell-poset cover graphs for every Young-diagram shape**. The inspected primary texts do not state this explicit all-shape orbit partition or the complete relative Young-diagram fingerprint, and the general undirected-graph results are not themselves an identical statement. Other work on colour refinement of directed Ferrers diagrams may exist, especially under the aliases staircase grid poset, partition-cell order, and directed Ferrers graph; full publication priority is not established.

## Limitations

The conclusion does not assert identification among all finite digraphs, a sharp number of refinement rounds, results for skew Young diagrams, or results for undirected covers. The proof uses northwest closure and the root-to-cell binomial path count critically. Search incompleteness and possible specialized earlier coverage are originality risks. The scientific assessment here is not independent validation.

## References

- D. Callan, *On conjugates for set partitions and integer compositions*, first arXiv submission 2005-08-02, arXiv:math/0508052. https://arxiv.org/abs/math/0508052
- V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, first arXiv submission 2015-02-04, arXiv:1502.01255. https://arxiv.org/abs/1502.01255
- S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, first arXiv submission 2015-03-30, arXiv:1503.08792. https://arxiv.org/abs/1503.08792
