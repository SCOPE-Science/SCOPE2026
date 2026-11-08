# A four-dimensional edge-fault threshold for sharp hypercube Lipschitz spread

## Finding
For an integer \(d\ge2\), let \(Q_d\) be the binary \(d\)-cube with unit edges, delete **one** edge \(e\), and let \(G_d=Q_d-e\). Under the uniform probability measure on its \(2^d\) vertices, let
\[
\operatorname{spr}(G)=\max_{\lvert f(u)-f(v)\rvert\le1\ (uv\in E(G))}\operatorname{Var}(f(X)).
\]
Then
\[
\boxed{\operatorname{spr}(G_d)=\begin{cases}
5/4,&d=2,\\
15/16,&d=3,\\
d/4,&d\ge4.
\end{cases}}
\]
Thus deletion strictly increases sharp Lipschitz variance in dimensions two and three, but leaves it **exactly unchanged in every dimension at least four**. The respective increases over \(\operatorname{spr}(Q_d)=d/4\) are \(3/4\), \(3/16\), and zero.

Every maximizer is classified. Use an automorphism of \(Q_d\) to put the deleted edge between the binary vertices indexed \(0\) and \(1\); identify \(x\in\{0,1\}^d\) with its binary integer \(\sum_{i=1}^d 2^{i-1}x_i\), and normalize \(f(0)=0\). For \(d=2\), the maximizers are the two signed vectors \(\pm(0,3,1,2)\), with entries indexed \(0,1,2,3\). For \(d=3\), they are the four vectors \(\pm(0,3,1,2,1,2,0,1)\) and \(\pm(0,3,1,2,1,2,2,3)\). For every \(d\ge4\), all maximizers, and only those, are the \(2^d\) signed coordinate sums
\[
f(x)=\sum_{i=1}^d\varepsilon_i x_i,\qquad\varepsilon_i\in\{-1,1\}.
\]
Arbitrary additive constants restore all maximizers without normalization.

## Assumptions and scope
The graph is simple and undirected, has **exactly one** removed unit edge, retains all \(2^d\) vertices, and is connected for \(d\ge2\). The distances are shortest-path distances in the altered graph, and the target is the real-valued uniform-measure *quadratic* variance, not an energy norm or a higher moment. Graph automorphisms carry any deleted edge to \(\{0,1\}\), so the chosen coordinates lose no generality. At \(d=1\) deleting the only edge disconnects the graph and the unconstrained spread is infinite; this is outside the theorem.

## Proof
**1. Reduction to all-tight integer heights.** Fix \(f(0)=0\). The edge constraints define a bounded polytope, because \(G_d\) is connected. Variance is strictly convex on this normalized affine space: for distinct normalized functions \(f,g\), the centered difference is nonzero and the strict convexity identity has positive quadratic defect. Consequently every maximizer is a vertex of the Lipschitz polytope.

For a candidate \(f\), call an edge *tight* when \(\lvert f(u)-f(v)\rvert=1\). If its tight-edge subgraph is disconnected, shift a tight component not containing vertex zero by \(\pm t\) for sufficiently small \(t>0\). Both shifts remain feasible, and \(f\) is their midpoint; hence \(f\) is not a vertex. Therefore a maximizer has a connected spanning tight-edge subgraph. Along a tight spanning tree, \(f\) is integer-valued and has parity equal to the bipartition parity \(\sum_i x_i\pmod2\). Because every surviving cube edge crosses this bipartition, its integer value difference must be odd. The difference is also bounded in magnitude by one, so **every surviving edge is tight**. Conversely every normalized assignment with \(\lvert f(u)-f(v)\rvert=1\) on all surviving edges is a vertex: fixing values along a spanning tree of tight edges removes all infinitesimal freedom. Thus it suffices, and is exact, to enumerate *height functions* with \(f(0)=0\) and difference exactly \(\pm1\) on every surviving edge. The first reduction is related to the original integer-extremizer principle; the bipartite all-tight strengthening is used here to make a finite computation exhaustive.

**2. Exact finite base and all equality cases.** Use the standalone `verify_one_edge_cube.py`. For each \(d\in\{2,3,4\}\), construct the graph explicitly by integer bit flips, omitting only \(\{0,1\}\). Traverse a breadth-first spanning tree rooted at zero. At each vertex \(v\ne0\), the value must be either \(f(\operatorname{parent}(v))-1\) or \(f(\operatorname{parent}(v))+1\); discard a choice if any already-assigned neighbor would have absolute difference other than one. A complete recursion visits every normalized height exactly once. For each complete vector \(f\), compare the integer
\[
H_d(f)=2^d\sum_{v} f(v)^2-\left(\sum_v f(v)\right)^2
       =2^{2d}\operatorname{Var}(f).
\]
The exhaustive height counts are \(8,44,1080\), the maximal numerators are \(20,60,256\), and their maximizer counts are \(2,4,16\), respectively. The verifier checks the explicit exceptional vectors in dimensions two and three and proves that, in dimension four, the entire equality set is precisely the signed coordinate sums. As a separate check, it enumerates **all** feasible normalized integer Lipschitz assignments (not just all-tight heights): the counts are \(27,597,221637\), and the same exact numerator maxima and equality sets result. All comparisons use integers, not floating-point tolerances. The checker's complete source is part of this result; these are finite exhaustive proofs of the base cases, not extrapolations from samples.

**3. Tensorization and rigidity of intact cubes.** On \(Q_m=Q_{m-1}\square K_2\), for any feasible \(F\), write its restrictions to the two layers as \(F_0,F_1\) and their means as \(\mu_0,\mu_1\). The law of total variance gives
\[
\operatorname{Var}(F)=\tfrac12\operatorname{Var}(F_0)
+\tfrac12\operatorname{Var}(F_1)
+\tfrac14(\mu_1-\mu_0)^2.
\]
Every vertical edge enforces \(\lvert F_1(x)-F_0(x)\rvert\le1\), hence \(\lvert\mu_1-\mu_0\rvert\le1\). Starting from \(Q_1=K_2\), induction shows \(\operatorname{spr}(Q_m)=m/4\). Equality requires both layers optimal and \(F_1-F_0\equiv\pm1\), since the mean of numbers in \([-1,1]\) has absolute value one only if they all equal the same endpoint. Inductively, all equality functions are exactly affine signed coordinate sums.

**4. Tensorization of the damaged cube.** For \(d\ge5\), split \(G_d\) by its last coordinate. The layer with last coordinate zero is \(G_{d-1}\); the other is an intact \(Q_{d-1}\). All vertical edges survive. The same variance identity and vertical-edge bound yield
\[
\operatorname{spr}(G_d)
\le\tfrac12\operatorname{spr}(G_{d-1})
 +\tfrac12\operatorname{spr}(Q_{d-1})+\tfrac14.
\]
The checked \(d=4\) base gives \(\operatorname{spr}(G_4)=1=4/4\); induction therefore gives \(\operatorname{spr}(G_d)\le d/4\). Every signed coordinate sum is feasible and has variance \(d/4\), giving the reverse inequality. At equality the two layers must each maximize variance, and every vertical difference equals one fixed sign. By the base classification and the preceding intact-cube rigidity, the layers are matching signed coordinate sums, and the full function is a signed coordinate sum. This proves the asserted exact values and complete equality description for all dimensions.

## Verification
Run `python3 verify_one_edge_cube.py` in the directory containing this file and the script; it uses only the Python standard library. Its terminal marker is `ALL_ONE_EDGE_DELETED_CUBE_BASE_CASES_EXACT_OK`. The program independently computes the graph and the objective twice, once over 1,132 all-tight height candidates across dimensions two, three and four and once over 222,261 general integer candidates. It asserts all counts, exact maxima, and equality sets. The analytical product induction proves the infinitely many higher dimensions from the finite \(d=4\) base. No numerical optimization, unverified solver status, or finite-to-infinite extrapolation is invoked.

## Relationship to prior work
Alon, Boppana and Spencer introduced graph spread, and their Theorem 2.1 established integer optimal potentials for graph metrics. Addario-Berry, Janson and McDiarmid explicitly record the intact cube identity \(\operatorname{spr}(Q_d)=d/4\) and Cartesian-product additivity. Yancey investigates the structure of extremal Lipschitz functions and products. These are essential background, not new discoveries here. The present statement concerns the **non-Cartesian graph obtained by deleting one edge**, its sharp dimension-four invariance threshold, and its equality set; neither the intact product identity nor general integrality alone determines that threshold. A distinct calculation on edge-data gradient projections after the same graph perturbation concerns a different operator norm and cannot imply the claimed variance formula.

## Limitations
The result is limited to deleting exactly one edge of an unweighted binary cube and uniform vertex measure. It gives no formula for multiple failures, weighted edges or measures, \(q\)-ary Hamming graphs, or sub-Gaussian concentration constants. A finite base case is verified by fully enumerated integer configurations rather than by a short closed-form combinatorial inequality. Originality comparisons cannot exclude unpublished or unindexed equivalent work. This proof is not an independent formal verification.

## References
- N. Alon, R. Boppana, and J. Spencer, *An Asymptotic Isoperimetric Inequality*, Geometric and Functional Analysis 8 (1998), 411–436, doi:10.1007/s000390050062; author-hosted full text: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf (especially §2.1).
- L. Addario-Berry, S. Janson, and C. McDiarmid, *On the spread of random graphs*, initial public arXiv version dated 2009-02-06, arXiv:0902.1156; https://arxiv.org/pdf/0902.1156 (especially §1.1).
- M. P. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, arXiv:1705.09725, initial version 2017-05-26; https://arxiv.org/pdf/1705.09725 (especially §§1–2).
