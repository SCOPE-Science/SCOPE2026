# The five-leaf threshold for online identification of a cluster

## Finding

Let \(T\) be a finite rooted tree with unordered children and no unary internal vertices. On its leaf set, consider the concept class consisting of the descendant-leaf cluster of each vertex, together with the empty set. Then every such hierarchy with two to four leaves has VC and Littlestone dimensions both equal to two. Five leaves are necessary and sufficient for the Littlestone dimension to exceed the VC dimension. Among five-leaf hierarchies, the Littlestone dimension is three exactly for the fully binary ones, and two for all the others. This distinguishes three of the twelve unordered unlabeled five-leaf shapes.

## Assumptions and scope

Queries are individual leaves; hypotheses are individual clusters of one fixed tree, not candidate trees. Edge-depth counts from the root. A complete binary query tree is shattered if every answer history is realized by a hypothesis; its maximum depth is the Littlestone dimension. The VC dimension uses a single fixed query set. Suppressing unary vertices would not change the class.

## Proof

The empty set, two singletons and the root cluster shatter every leaf pair. No triple \(a,b,c\) is shattered: clusters with traces \(\{a,b\}\) and \(\{a,c\}\) would intersect and be incomparable, contrary to laminarity. Thus for at least two leaves the VC dimension is two. Fixed shattered queries can be used at every level of an adaptive tree, so the Littlestone dimension is at least two in those cases.

Consider the first query \(x\) of a depth-three tree. On its positive branch the hypotheses are the ancestor clusters of \(x\), including its singleton: there are \(1+d_x\), where \(d_x\) is the edge-depth of \(x\). They form a strict inclusion chain. Between any two consecutive clusters one can query a leaf in their difference to split the chain at that boundary. Thus the positive branch of \(x\) admits depth two exactly when \(d_x\ge3\): fewer than four hypotheses cannot fill four histories, and with four or more the consecutive chain can be split into two groups each with a further split available.

The negative branch admits depth two exactly when an internal cluster avoids \(x\). Such a cluster contains two leaves and, together with their singletons and the empty concept, shatters that pair. Without such a cluster, the negative branch has only singleton hypotheses and the empty one; any positive answer uniquely identifies the hypothesis. Consequently a hierarchy admits depth three if and only if some leaf \(x\) of depth at least three has an internal subtree off its root-to-leaf path.

At each strict ancestor of \(x\) there must be an off-path child subtree with at least one leaf, and one of these subtrees must supply at least two leaves. Counting \(x\) as well gives at least \(d_x+2\ge5\) leaves. At equality there are exactly three strict ancestors of \(x\), each with exactly one off-path child. Two off-path subtrees are single leaves and the third is a two-leaf cherry. This tree is fully binary. Conversely, placing the cherry at each of the three positions on the path gives a fully binary five-leaf tree admitting depth three. These yield the three distinct binary shapes: a root partition \(2+3\), or a root partition \(1+4\) with the four-leaf subtree split \(2+2\) or \(1+3\). A five-leaf tree has at most ten hypotheses (at most four internal vertices, five leaf vertices and one empty concept); depth four is therefore impossible. This proves the claimed dimensions.

For the total shape count, the root partitions of five leaves are \(4+1,3+2,3+1+1,2+2+1,2+1+1+1,1+1+1+1+1\). There are five possible four-leaf subtrees (root partitions \(3+1,2+2,2+1+1,1+1+1+1\), with two possibilities for the three-leaf part in \(3+1\)), and two three-leaf subtrees. The six root partitions of five thus contribute \(5,2,2,1,1,1\) shapes respectively, totaling twelve.

## Reproducibility

The two supplied standard-library scripts `CHECK_LAMINAR.py` and `CHECK_LABELED.py` check small hierarchy shapes using child multisets and labeled set partitions respectively. `CHECK_OUTPUT.txt` records both finite enumerations, including the five-leaf rank counts of nine at rank two and three at rank three. The proof above does not depend on these computations. Selected regular-tree checks in the scripts are background only.

## Relationship to prior work and limitations

The tree-shape counts are classical; see [OEIS A000669](https://oeis.org/A000669) for all unordered shapes without unary nodes and [A001190](https://oeis.org/A001190) for the fully binary ones. The conclusion concerns which shapes attain the online threshold, not a new enumeration of the shapes alone. The fixed-support shattering polynomial \(1+Nz+\binom N2z^2\) follows from laminarity and the empty, singleton and root clusters; it serves as background.

The earlier [height law for rooted tree descendant concepts](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-a-sharp-one-bit-height-law-for-online-learning-of-rooted-tree-de--b12283818b44/RESULT.md) used vertex queries and no empty concept, but already gave the positive-ancestor chain bound and the regular-tree sharpness construction. That construction adapts by extending side-branch queries to leaves; no regular-tree height law is claimed as a contribution here. Online rank of root-to-leaf paths as hypotheses, or of all trees as hypotheses queried by candidate clades, addresses different classes. The result concerns the first threshold, not subsequent minimum sizes for higher dimensions or an exact rank classification on arbitrary hierarchies. Priority is assessed against the compared statements, not guaranteed.
