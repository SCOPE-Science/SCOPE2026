# Tree-topology invariance and sharp correlation rigidity for the four-cube Hypercube ratio

## Finding

Let \(E\) be **any** spanning tree on the labelled vertices \(\{1,2,3,4\}\), and assign a real edge parameter \(\rho_e\in(-1,1)\) to each of its three edges. For a four-cube vertex \(v\in\{0,1\}^4\), put \(s_i(v)=(-1)^{v_i}\) and
\[
x_v=\prod_{e=\{i,j\}\in E}\left(1+\rho_e s_i(v)s_j(v)\right)>0.
\]
The normalized weights \(x_v/16\) form the unbiased zero-field binary tree Ising distribution. For every five-vertex set \(U\subset\{0,1\}^4\), let \(d(U)=4!\operatorname{vol}_4(\operatorname{conv}U)\) and define
\[
P(x)=\sum_{|U|=5}d(U)\prod_{v\in U}x_v,\qquad T=\sum_v x_v,
\]
while \(S_F=\sum_{v\in F}x_v\) for each of the eight facets \(F\) of the four-cube. With \(t_e=\rho_e^2\), the following identity holds for **every one of the 16 labelled spanning trees**, independently of the tree topology:
\[
\boxed{P(x)=32\prod_{e\in E}(1-t_e)
\left(105+15\sum_e t_e-7\sum_{e<f}t_et_f-\prod_e t_e\right).}
\]
In particular, \(T=16\), all \(S_F=8\), and the exact Hypercube ratio is
\[
\boxed{\frac{P(x)T^3}{\prod_F S_F}=
\frac{\prod_{e\in E}(1-t_e)}{128}
\left(105+15\sum_e t_e-7\sum_{e<f}t_et_f-\prod_e t_e\right).}
\]
This ratio is **strictly decreasing in each \(t_e\in[0,1)\)** with the other two parameters fixed. Hence
\[
\boxed{\frac{P(x)T^3}{\prod_F S_F}\le\frac{105}{128},}
\]
with equality precisely at \(\rho_e=0\) for all three edges. The relative gap from the originally conjectured bound \(1\) is therefore at least \(23/128\), sharply for this entire connected three-correlation family.

## Assumptions and scope

The coordinates \(1,\ldots,4\) are labelled. A tree is a connected simple graph with exactly three edges on those coordinates. There are \(4^{4-2}=16\) such trees. The weights above are strictly positive for \(\rho_e\in(-1,1)\); the polynomial identities and non-strict bound extend to \(|\rho_e|\le1\) by continuity, including zero weights.

A convention for \(e<f\) simply chooses each unordered pair of distinct tree edges once. The polynomial does not depend on that convention, the labels, or whether the tree is a path or a star. Normalized simplex volume \(d(U)\) is the absolute determinant of the four edge vectors of the simplex, not its Euclidean volume.

The source's Hypercube conjecture in cube dimension four is \(P(x)T^3\le\prod_F S_F\) for arbitrary sixteen nonnegative vertex weights. The present theorem treats only zero-field binary **tree-product** weights and does not prove that unrestricted conjecture.

## Proof

**Uniform one-coordinate marginals.** Expand the product defining \(x_v\) as a sum of parity characters indexed by subsets of the tree's edges. The empty edge subset contributes \(1\). Every nonempty subset is a forest containing a nonempty edge component, whose odd-degree vertex set has at least two elements. Its parity character therefore has zero sum on the entire cube and zero correlation with every single coordinate sign. Thus \(\sum_v x_v=16\), and each fixed-coordinate halfcube receives precisely half that sum, so \(S_F=8\) for every facet.

**A finite exact polynomial identity, not interpolation from samples.** Fix a labelled tree and order its three edges. For \(\rho_e\in\mathbb R\), \(P(x)\) is a polynomial of degree at most five in each parameter because each vertex weight is linear in that parameter and each term in \(P\) contains five vertex weights. For any subset of tree edges, one may select coordinate signs \(\epsilon_i\in\{\pm1\}\) with \(\epsilon_i\epsilon_j=-1\) exactly on the chosen edges: assign a sign at a root and propagate along the unique tree paths. The induced reflections \(s_i\mapsto\epsilon_i s_i\) permute four-cube vertices and preserve the normalized absolute simplex determinants. Consequently \(P\) is unchanged by independently flipping the sign of any of the three \(\rho_e\). It is therefore **even** in each parameter and, in the variables \(t_e=\rho_e^2\), has degree at most two in each variable.

To prove the displayed identity rigorously it now suffices, by repeated univariate degree-two interpolation, to verify it for every ordered triple \(\rho_e\in\{0,1,2\}\): the squared nodes \(\{0,1,4\}\) are distinct. This sufficiency is an algebraic consequence of the proved degree bounds; no numerical extrapolation from finite experiments is involved. The bundled checker exhaustively lists all \(\binom{16}{5}=4368\) five-vertex subsets, constructs each \(4\times4\) integer difference determinant, and checks every one of the \(16\times3^3=432\) tree-and-grid cases against
\[
32(1-a)(1-b)(1-c)[105+15(a+b+c)-7(ab+ac+bc)-abc],
\]
where \(a,b,c\) stand for the three squared edge parameters. All arithmetic is in exact integers; the 432 checks pass. By the interpolation argument the polynomial identity is established for all real parameters, with no dependency on a numerical tolerance.

**Strict monotonicity and equality.** In the open physical parameter cube, write \(a,b,c\) for the squared correlations. The bracketed symmetric polynomial is
\[
Q(a,b,c)=105+15(a+b+c)-7(ab+ac+bc)-abc.
\]
Fix \(b,c\in[0,1)\), and define \(Q_0=105+15(b+c)-7bc\) and \(Q_1=15-7(b+c)-bc\). Then \(Q=Q_0+aQ_1\), and \(Q_1\ge0\) because \(b,c\le1\). Moreover,
\[
\begin{aligned}
Q-(1-a)\partial_a Q
&=Q_0-Q_1+2aQ_1\\
&=90+22(b+c)-6bc+2a[15-7(b+c)-bc]>0.
\end{aligned}
\]
Thus \(\partial_a[(1-a)Q]=-[Q-(1-a)\partial_a Q]<0\). Multiplication by the positive other factors \((1-b)(1-c)\) proves strict decrease with \(a\), and symmetry proves it with \(b,c\). The unique maximum is at \(a=b=c=0\), where the ratio equals \(105/128\). This also proves the exact equality and sharpness assertions.

## Verification

Run the bundled standard-library-only Python program `tree_hypercube_checker.py` with Python 3. It reconstructs the determinant table and checks all 432 interpolation-grid identities on all 16 trees using integer arithmetic. It separately tests that the sum of normalized determinant volumes is \(3360\), establishing the uniform-weight ratio. The expected terminal output is:

```text
TREE_HYPERCUBE_OK trees=16 grid_per_tree=27 subsets=4368 nonzero=3008
```

The determinant histogram is: zero on 1360 five-sets, one on 2672, two on 320, three on 16. These are exhaustive counts for this finite polynomial, not heuristic evidence about arbitrary point sets. The reduction from 432 evaluations to a universal parameter identity is justified by the even-degree-two interpolation proof above. The monotonicity step is analytic, not based on the grid.

## Relationship to prior work

Averkov, von Dichter and Soprunov introduced the Hypercube inequality and proved its three-cube case, leaving the unrestricted four-cube case open. Their 2026 preprint does not give a tree-Ising or correlation-polynomial specialization.

The published theorem *Sharp symmetric gap for the first open hypercube inequality* proves the same optimal bound \(105/128\) on a **different** weight cone: weights constant on coordinate-permutation and complement orbits, hence constant on Hamming weight classes paired by complementation. It does not imply the present result. For example, on the three-edge star with all correlations \(1/2\), the weight of the Hamming-one vertex whose negative sign is at the star center is \(1/8\), while the weight of a Hamming-one vertex whose negative sign is at a leaf is \(9/8\). The two weights are not equal, so those tree weights lie outside that published cone. The present theorem additionally proves a topology-independent three-edge profile, not merely the shared uniform-weight upper bound.

A previously determined exact two-correlation law concerns **two disjoint correlated pairs** with independent remaining pair blocks. It is recovered here only as a degenerate edge-zero specialization, after which the interaction graph is no longer connected. It does not cover any genuinely three-edge connected tree distribution, nor prove topology independence for paths and stars.

The tree weights may also be described as positive zero-field Ising graphical-model distributions, or as unbiased binary Markov tree laws. This equivalence is a reparameterization of the same claim, not a separate novelty assertion.

## Limitations

This theorem does not settle the conjecture for arbitrary four-cube vertex weights. It does not cover cyclic Ising interaction graphs, nonzero external fields, arbitrary binary Markov networks, or arbitrary higher-dimensional cubes. An older equivalent formula in stochastic geometry, graphical models or unindexed mathematical literature remains a possible priority risk; the checked sources do not establish independence or priority certification.

The determinant enumerator is exact but specific to sixteen cube vertices. The analytic interpolation and monotonicity steps are indispensable for conclusions about all real correlations. Independent external review has not been performed.

## References

1. Gennadiy Averkov, Katherina von Dichter and Ivan Soprunov, *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909v1, first publicly posted 14 August 2026. https://arxiv.org/abs/2608.14909
2. *Sharp symmetric gap for the first open hypercube inequality*, published research record, 11 October 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-symmetric-gap-for-the-first-open-hypercube-inequality--4f3e013d18c9/RESULT.md
