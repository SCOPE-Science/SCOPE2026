# Strict fixed-order balancing for Mahler products of complete-bipartite symmetric edge polytopes

## Finding
Fix an integer \(N\ge6\). Among the complete-bipartite graphs \(K_{p,q}\) with \(p+q=N\), let \(P_{p,q}\) be the symmetric edge polytope and \(P_{p,q}^{\circ}\) its polar in the zero-sum hyperplane. Then
\[
\operatorname{vol}(P_{p+1,q-1})\operatorname{vol}(P_{p+1,q-1}^{\circ})>
\operatorname{vol}(P_{p,q})\operatorname{vol}(P_{p,q}^{\circ})
\quad\text{if }2\le p\le q-2.
\]
Consequently the unique maximizing unordered split is \(\{\lfloor N/2\rfloor,\lceil N/2\rceil\}\). The minimizing unordered splits are exactly those whose smaller part is one or two. For \(N\le5\) all splits tie. The comparison transfers one vertex while keeping dimension fixed; it does not follow from monotonicity when only one part grows.

## Assumptions and scope
All part sizes are positive integers. The space is \(H=\{x\in\mathbb R^{p+q}:\sum_i x_i=0\}\), with \(d=p+q-1\), and
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_j):i\in A,\ j\in B\}\quad(|A|=p,\ |B|=q).
\]
Volumes and polarity can be taken in intrinsic Euclidean coordinates. Equivalently, one may choose any basis on the primal and its dual basis on the polar, since their volume factors cancel. The same body is the unit ball of the real Lipschitz-free space of the unit-edge shortest-path metric on \(K_{p,q}\). No comparison with other graph families is asserted.

## Proof
### Input: the known normalized product
Let \(w_k=4^{-k}\binom{2k}{k}\). By the complete-bipartite product formula in [2],
\[
R(p,q):=\frac{d!}{4^d}\operatorname{vol}(P_{p,q})\operatorname{vol}(P_{p,q}^{\circ})
=\frac{N}{\binom Np}\sum_{k\ge0}w_k\binom{p-1}{k}\binom{q-1}{k}.
\]
All out-of-range binomial coefficients are zero. The formula combines the primal volume from the bipartite \(h^*\)-polynomial [1] with the exact polar volume [2]. In intrinsic Euclidean coordinates their factors of \(\sqrt N\) and \(1/\sqrt N\) cancel. The normalization \(d!/4^d\) is common to all splits considered.

### Beta-binomial baseline
Vandermonde's identity gives
\[
\sum_{k\ge0}\frac{\binom{p-1}{k}\binom{q-1}{k}}{k+1}
=\frac1p\sum_{k\ge0}\binom p{p-1-k}\binom{q-1}k
=\frac1p\binom{N-1}{p-1}=\frac{\binom Np}{N}.
\]
With \(s_k=(k+1)w_k\), we have \(s_0=s_1=1\) and
\[
\frac{s_{k+1}}{s_k}=1+\frac{k}{2(k+1)^2}.
\]
In particular all splits with a part of size at most two have \(R(p,q)=1\); their product sum has no nonzero term beyond \(k=1\).

### Single crossing at fixed \(N\)
Take \(2\le p\le q-2\). For \(0\le k\le p\) put
\[
D_k=(p+1)\binom pk\binom{q-2}k-q\binom{p-1}k\binom{q-1}k.
\]
The adjacent difference is
\[
R(p+1,q-1)-R(p,q)=\frac{N}{q\binom Np}\sum_{k=0}^p w_kD_k.
\]
The baseline identity shows \(\sum_{k=0}^p D_k/(k+1)=0\). For \(k<p\), canceling the shared binomial factors gives
\[
D_k=\binom{p-1}k\binom{q-2}k
\frac{(q-p-1)[kN-p(q-1)]}{(p-k)(q-1-k)}.
\]
The sign for \(k<p\) is thus that of the increasing affine function \(kN-p(q-1)\). Also \(D_0=p+1-q<0\) and \(D_p=(p+1)\binom{q-2}p>0\). Every positive coefficient lies after every negative coefficient. Since the positive and negative masses of \(D_k/(k+1)\) agree, their weighted mean comparison with the nondecreasing weights \(s_k\) yields
\[
\sum_{k=0}^p w_kD_k=\sum_{k=0}^p s_k\frac{D_k}{k+1}>0.
\]
Indeed, divide the positive and the absolute negative coefficients by their common mass and compare the two means by pairing the indices; all differences of weights are nonnegative and the pair \((p,0)\) has positive mass and strictly positive difference because \(p\ge2\). This proves the strict transfer inequality. By symmetry and repeated transfers for \(p\le q\), it gives the stated maximizer and shows every split with a smaller part at least three is strictly above the tied thin splits. When \(N\le5\) there are only thin splits.

## Verification
The accompanying `verify.py` checks finite instances of the product normalization and single-crossing certificate in exact rational arithmetic. For example, at \(N=8\) the normalized values in order of increasing smaller part are \(1,1,29/28,21/20\). The single-crossing proof, not the finite test, establishes strictness for all claimed sizes.

## Relationship to prior work
The primal and polar volume evaluations, normalized product formula, benchmark equality classification, and one-part-fixed limit appear in [1,2]; these are not claimed as new. The monotonicity in [2] holds when one part alone grows, so goes in opposite directions for the two changes of a fixed-order transfer and does not give the comparison here. The fixed-order directional-width theorem in [3] is for the same bodies but a different invariant. Its width ordering orders the polar volumes in the opposite direction (by the radial integral of the polar); it does not compare their products with primal volume. The new statement here is the strict comparison at fixed order and the resulting exact maximizer at each dimension.

## References
1. A. Higashitani, K. Jochemko, and M. Michałek, *Arithmetic Aspects of Symmetric Edge Polytopes*, Theorem 4.1, https://arxiv.org/abs/1807.07678.
2. *A sharp Mahler-product hierarchy for complete-bipartite symmetric edge polytopes*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-a-sharp-mahler-product-hierarchy-for-complete-bipartite-symmetri--f86fbac7ea01.
3. *Balanced bipartitions stochastically enlarge Euclidean widths of symmetric edge polytopes*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-balanced-bipartitions-stochastically-enlarge-euclidean-widths-of--189623e8986a.
