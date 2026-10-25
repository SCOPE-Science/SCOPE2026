# The first negative covariance between complementary phylogenetic diversities occurs at fourteen leaves

## Finding
Let \(T\) be an unrooted binary tree with \(n\) distinctly labeled leaves and unit edge lengths. Choose a subset \(A\) of exactly \(k\) leaves uniformly, and let \(B=L(T)\setminus A\). Write \(D_T(U)\) for the number of edges in the minimal connected subtree spanning a leaf set \(U\).

**Sharp finite classification.** For every \(4\le n\le13\), every such tree, and every \(2\le k\le n-2\),
\[
\operatorname{Cov}\bigl(D_T(A),D_T(B)\bigr)>0.
\]
At \(n=14\), for \(k=6\), precisely one unlabelled unrooted binary tree shape among the \(135\) shapes gives negative covariance: the fourteen-leaf caterpillar. On this tree,
\[
\operatorname{Cov}\bigl(D_T(A),D_T(B)\bigr)=-\frac{122}{7007}.
\]
Consequently fourteen leaves is the smallest size at which complementary uniform samples can have negatively covarying unrooted phylogenetic diversities under unit edge lengths. This does **not** classify arbitrary larger trees or edge weights.

## Assumptions and scope
All edges have length exactly one. Internal vertices have degree three, all leaves degree one, there is no root, and each leaf is counted once. Both subsamples must have at least two leaves. For the fourteen-leaf witness, the smaller sample has six leaves and its complement eight. Randomness is only the uniform choice of a leaf subset; the tree is fixed. The sign is a population covariance of two random variables on the same complementary partition, not the covariance of independent draws.

A caterpillar here is an unrooted binary tree whose \(n-2\) internal vertices induce a path. Number those internal vertices consecutively \(v_0,\ldots,v_{n-3}\). Attach two leaves at each endpoint and one leaf at each interior vertex. This uniquely defines its unlabelled shape.

## Proof
**1. Exact edge formula.** For each internal edge \(e\), deleting it partitions the leaf set into two nonempty blocks \(S_e\) and \(S_e^c\). Define \(I_e(U)=1\) exactly when \(U\) intersects both blocks. If \(2\le|U|\le n-2\), every pendant edge incident to a member of \(U\) belongs to its spanning subtree and no other pendant edge does. Hence
\[
D_T(U)=|U|+\sum_{e\text{ internal}}I_e(U).
\]
There are exactly \(n-3\) internal edges. For fixed sample sizes the first term is deterministic. The covariance is therefore computed exactly by enumerating the \(\binom nk\) possible subsets and their complementary split indicators.

**2. Exhaustion of all tree shapes.** The unique unrooted binary tree with three leaves is the starting shape. Given a tree with \(n-1\) leaves, subdivide each edge once in turn and attach a new leaf to the inserted vertex. Every \(n\)-leaf unrooted binary tree arises this way: delete any leaf, suppress its resulting degree-two parent, and reverse this operation. Two constructed trees are identified exactly by recursive unordered rooted-tree encoding at their center vertex or center edge, with leaf and internal-vertex types distinguished. Recursion from leaves shows that these encodings agree exactly for isomorphic typed trees. Thus generating all edge insertions and retaining one of each canonical encoding exhausts the unlabelled shapes, rather than sampling them.

The attached `verify.py` realizes this construction using only integer operations. The counts of distinct shapes at \(n=4,5,\ldots,14\) are respectively \(1,1,2,2,4,6,11,18,37,66,135\). For each shape through thirteen leaves and every \(2\le k\le\lfloor n/2\rfloor\), it computes the exact covariance via the formula above and checks strict positivity. Complement symmetry gives the same result for \(n-k\). The smallest covariance over all shapes and sample sizes for \(n=4,5,\ldots,13\), respectively, is
\[
\frac29,\ \frac6{25},\ \frac29,\ \frac{88}{441},\ \frac5{28},\ \frac{82}{567},\ \frac{13}{126},\ \frac{25}{363},\ \frac{107}{3234},\ \frac{53}{11154}.
\]
All are strictly positive. At fourteen leaves with \(k=6\), exact enumeration of all \(135\) shapes finds precisely one negative case. The canonical encoding identifies it with the caterpillar.

**3. Explicit independent witness calculation.** In the fourteen-leaf caterpillar the attachment coordinates of the leaves along its internal path are
\[
0,0,1,2,3,4,5,6,7,8,9,10,11,11.
\]
For any sample \(U\) containing at least two leaves, with \(r(U)\) the difference between its largest and smallest attachment coordinates, its edge count is exactly \(D_T(U)=|U|+r(U)\). Directly enumerate the \(\binom{14}{6}=3003\) six-subsets. Writing \(X=D_T(A)\), \(Y=D_T(B)\), the resulting integer sums are
\[
\sum X=47619,\qquad \sum Y=55627,\qquad \sum XY=882033.
\]
Consequently
\[
\operatorname{Cov}(X,Y)
=\frac{3003(882033)-(47619)(55627)}{3003^2}
=-\frac{122}{7007}.
\]
A second computation in `verify.py` removes all unselected leaves iteratively and counts edges of the remaining spanning subtree, independently confirming all three sums for the witness. Steps 1–3 prove the stated sharp finite result.

## Verification
Run `python3 verify.py` in the directory containing the supplied files. It requires only the Python standard library. The expected output is saved as `verification_output.txt`. The program checks exact tree-shape counts, validates vertex degrees, independently obtains each internal split by traversing the tree after removing an edge, computes rational covariances from integer moment sums, exhausts every required shape and sample size, and repeats the fourteen-leaf witness with a separate subtree-pruning implementation. It reports `EXACT_VERIFICATION_OK` on success. No random or numerical-tolerance operations enter these checks.

## Relationship to prior work
Hardy and Senterre (2007) developed a community-level partitioning of phylogenetic distinctness; their statistic is based on between-species divergence and spatial assemblages rather than the covariance of two complementary uniform leaf-sample **subtree lengths**. Nipperess and Matsen (2013) gave exact mean and variance formulas for phylogenetic diversity of a **single** rarefied sample. Their edge-snip framework supports computing marginal moments, but the article does not give the joint complementary-sample sign classification or its first negative tree size. The present finite classification uses their ecological motivation and standard edge-based view without claiming these foundational formulas as new.

## Limitations
The classification is finite and exact through fourteen leaves; it is not a universal sign theorem for larger leaf sets. The unique-negative-shape statement is restricted to fourteen leaves with a six-versus-eight partition. Unrestricted branch lengths and rooted phylogenetic diversity are not covered. The finite check is fully enumerated, not a proof of any untested infinite extension. The ecological interpretation presumes a known exact tree and simple uniform partitioning; it does not quantify estimation uncertainty under phylogenetic reconstruction or field sampling.

## References
- Hardy, O. J., and Senterre, B. (2007). *Characterizing the phylogenetic structure of communities by an additive partitioning of phylogenetic diversity*. Journal of Ecology 95, 493–506. First publicly available 12 April 2007. DOI: 10.1111/j.1365-2745.2007.01222.x.
- Nipperess, D. A., and Matsen, F. A. IV (2013). *The mean and variance of phylogenetic diversity under rarefaction*. Methods in Ecology and Evolution 4, 566–572. First publicly available 9 February 2013. DOI: 10.1111/2041-210X.12042.
