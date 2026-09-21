# Sharp minimum order of k-stepwise irregular trees at fixed maximum degree

## Statement

Fix an integer \(k\ge 1\). A graph is \(k\)-stepwise irregular (\(k\)-SI) if
\[
|d(u)-d(v)|=k
\]
for every edge \(uv\).

Every nontrivial \(k\)-SI tree has maximum degree
\[
\Delta=1+hk
\]
for a unique integer \(h\ge1\). Define
\[
F_0=1,\qquad F_i=1+ikF_{i-1}\quad(i\ge1).
\]
Equivalently,
\[
F_i=\sum_{j=0}^{i}\frac{i!}{j!}k^{i-j}.
\]

Then every \(k\)-SI tree \(T\) with \(\Delta(T)=1+hk\) satisfies
\[
\boxed{|V(T)|\ge N_{k,h}:=1+(1+hk)F_{h-1}}
\]
or, explicitly,
\[
\boxed{|V(T)|\ge
1+(1+hk)\sum_{j=0}^{h-1}\frac{(h-1)!}{j!}k^{h-1-j}.}
\]

Equality holds for exactly one tree up to isomorphism. Its unique maximum-degree vertex is a root of degree \(1+hk\); each nonroot vertex of degree \(1+ik\), \(1\le i\le h-1\), has exactly \(ik\) children of degree \(1+(i-1)k\); and the vertices at level \(0\) are leaves. The extremal tree has radius \(h\) and diameter \(2h\).

For \(k=1\), writing \(\Delta=h+1\), this becomes
\[
N_{1,h}=1+\Delta\sum_{j=0}^{\Delta-2}\frac{(\Delta-2)!}{j!},
\]
which is the known minimum-order sequence for ordinary stepwise-irregular trees recorded as OEIS A392965. Thus the theorem extends that minimum-order phenomenon from SI trees to arbitrary \(k\)-SI trees and gives the unique extremizer uniformly.

## Proof

A nontrivial tree has a leaf. In a \(k\)-SI tree, degrees change by exactly \(k\) along every edge, so every vertex degree is congruent to \(1\pmod{k}\). Hence
\[
\Delta(T)=1+hk
\]
for some \(h\ge1\). Moreover, a path from a maximum-degree vertex to a leaf must pass through every degree
\[
1,\ 1+k,\ldots,\ 1+hk.
\]

Root \(T\) at a maximum-degree vertex. Call a vertex of degree \(1+ik\) a class-\(i\) vertex. Consider any nonroot class-\(i\) vertex \(v\) together with the component below it after the edge to its parent is deleted; call this rooted component a branch at class \(i\).

We claim that every branch at class \(i\) has at least \(F_i\) vertices. Prove this by strong induction on the order of the branch. If \(i=0\), then \(v\) has degree \(1\), so the branch consists only of \(v\), and its order is \(F_0=1\).

Now let \(i\ge1\). Since \(v\) has one parent and total degree \(1+ik\), it has exactly \(ik\) children. Every child is in class \(i-1\) or class \(i+1\). Each child branch is smaller than the branch at \(v\), so the induction hypothesis applies to it. The sequence \((F_i)\) is strictly increasing, because
\[
F_i-F_{i-1}=1+(ik-1)F_{i-1}>0.
\]
Consequently every child branch contains at least \(F_{i-1}\) vertices: a class-\(i-1\) child gives at least \(F_{i-1}\), while a class-\(i+1\) child gives at least \(F_{i+1}>F_{i-1}\). Therefore
\[
|B_v|\ge1+ikF_{i-1}=F_i.
\]
This proves the branch bound.

The root has degree \(1+hk\). Since there is no class \(h+1\), all of its \(1+hk\) children are class \(h-1\). Their branches are pairwise disjoint, hence
\[
|V(T)|\ge1+(1+hk)F_{h-1}=N_{k,h}.
\]

For equality, every root-child branch must attain \(F_{h-1}\), and equality must hold recursively in the branch argument. At any class-\(i\) vertex, a child in class \(i+1\) would contribute at least \(F_{i+1}>F_{i-1}\), making the bound strict. Thus every child must be in class \(i-1\), and every child branch must itself be extremal. This forces the recursive rooted tree described in the statement, so the equality case is unique up to isomorphism.

Conversely, that recursively defined tree has the required degrees: the root has \(1+hk\) children; every nonroot class-\(i\) vertex has one parent and \(ik\) children, hence degree \(1+ik\); and class-\(0\) vertices are leaves. Every edge joins consecutive classes, so every edge has degree difference \(k\). Its order obeys the same recurrence with equality, hence is \(N_{k,h}\).

Finally, every root-to-leaf path has length \(h\). Since the root has at least two child branches, two leaves in different root branches are at distance \(2h\), proving radius \(h\) and diameter \(2h\).

The closed form for \(F_i\) follows immediately by unrolling \(F_i=1+ikF_{i-1}\).

## A degree-complexity-three consequence

The case \(h=2\) gives the unique smallest non-star \(k\)-SI tree:
\[
N_{k,2}=2k^2+3k+2.
\]
More generally, all \(k\)-SI trees having exactly three distinct degrees \(\{1,k+1,2k+1\}\) admit a simple core description. Delete all leaves. The remaining graph \(H\) is a bipartite tree with parts \(A\) (the degree-\(k+1\) vertices) and \(B\) (the degree-\(2k+1\) vertices), every \(b\in B\) has \(d_H(b)=2k+1\), and every \(a\in A\) has \(1\le d_H(a)\le k+1\). Conversely, every such core becomes a \(k\)-SI tree after attaching \(k+1-d_H(a)\) leaves to each \(a\in A\).

If \(b=|B|\ge1\), then the tree identity gives
\[
|A|=2kb+1,
\]
and the number of leaves is
\[
(2k^2-1)b+k+1.
\]
Hence the exact order spectrum for degree complexity three is
\[
\boxed{n=2k(k+1)b+k+2\qquad(b\ge1).}
\]
Every \(b\ge1\) occurs: arrange the \(B\)-vertices in a chain separated by \(A\)-vertices, add pendant \(A\)-vertices until every \(B\)-vertex has core degree \(2k+1\), and then attach leaves to raise every \(A\)-vertex to degree \(k+1\).

## Context and originality

Gutman's 2018 paper introduced stepwise-irregular graphs and considered minimum-order SI trees with prescribed maximum degree. The currently recorded general \(k=1\) minimum-order formula is OEIS A392965. The formula above specializes exactly to A392965 when \(k=1\).

Das, Mishra and Rai introduced and studied 2-stepwise irregular graphs and generalized several properties to \(k\)-SI graphs. Alizadeh, Klavžar and Langari subsequently studied general \(k\)-SI graphs. Their full arXiv text proves bipartiteness, existence results by diameter, a sharp upper bound on maximum degree in terms of order, size bounds, and the fact that \(k\)-SI trees have even diameter. It does not state the minimum-order theorem above or its recursive unique extremizer. A 2026 paper by Adiyanyam et al. studies upper bounds on maximum degree and size and characterizes certain extremal 2-SI graphs according to its available abstract.

To the best of our knowledge, searches for minimum-order \(k\)-SI trees, prescribed maximum degree, 2-SI tree order, degree-complexity-three trees, and equivalent formulations did not locate the general formula, uniqueness theorem, or the exact three-degree order spectrum above.

## Scientific limitations

The full theorem text of Das--Mishra--Rai (2023) was not inspected; its accessible abstract and indexed snippets were checked. The full text of Adiyanyam et al. (2026) was also not inspected; its abstract was checked and emphasizes maximum-degree/size extremality rather than minimum-order trees. These sources therefore remain the most relevant residual originality risks. Unindexed results or equivalent statements under different terminology remain possible.

No finite enumeration is used in the proof; the result is established symbolically by the rooted-branch lower bound and its equality conditions.

## References

1. I. Gutman, *Stepwise irregular graphs*, Applied Mathematics and Computation 325 (2018), 234--238. https://doi.org/10.1016/j.amc.2017.12.045
2. OEIS Foundation Inc., *A392965: Least number of vertices in a stepwise-irregular tree with at least one vertex of degree n*. https://oeis.org/A392965
3. S. Bera, P. Paul, *Properties of stepwise irregular graphs*, arXiv:1809.03297 (2018). https://arxiv.org/abs/1809.03297
4. S. Das, U. Mishra, S. Rai, *On two-stepwise irregular graphs*, Scientia Iranica 30(3) (2023), 1049--1057. https://doi.org/10.24200/sci.2022.57725.5388
5. Y. Alizadeh, S. Klavžar, J. Langari, *Extremal results on k-stepwise irregular graphs*, Applied Mathematics and Computation 514 (2026), 129818. https://doi.org/10.1016/j.amc.2025.129818 ; preprint: https://arxiv.org/abs/2411.15765
6. D. Adiyanyam, A. Enkhbayar, L. Buyantogtokh, S. Dorjsembe et al., *On k-stepwise irregular graphs*, Discrete Applied Mathematics 393 (2026), 268--279. https://doi.org/10.1016/j.dam.2026.06.027
7. S. Bera, P. Paul, K. G. Subramanian, *Some properties of stepwise irregular graphs*, Electronic Journal of Graph Theory and Applications 14(1) (2026). https://doi.org/10.5614/ejgta.2026.14.1.14
