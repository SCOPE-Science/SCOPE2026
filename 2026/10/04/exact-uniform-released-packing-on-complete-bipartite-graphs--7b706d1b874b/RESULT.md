# Exact uniform released packing on complete bipartite graphs
## Finding
Let \(G=K_{a,b}\) have bipartition \(A\cup B\), with \(a=|A|\ge 1\) and \(b=|B|\ge 1\). Fix integers \(u\ge 1\) and \(k\ge 0\). Write \(L^R_{k,u}(G)\) for the maximum weight of a Released \((k\mathbf 1,\mathbf 0,u\mathbf 1)\)-packing function.

Set
\[
T_0=(a+b)(u-1).
\]
If \(k\ge u\), set
\[
T_A=au+\min\{b(u-1),k-u\},\qquad
T_B=bu+\min\{a(u-1),k-u\}.
\]
If \(k\ge 2u\), set
\[
T_{AB}=\min\{au,k-u\}+\min\{bu,k-u\}.
\]
Then
\[
L^R_{k,u}(K_{a,b})=\max T,
\]
where the maximum is taken over \(T_0\) and the other displayed terms only when their stated hypotheses hold.

Equivalently, the four terms are the exact optima in the four possible saturation patterns: neither side contains a vertex assigned \(u\), only \(A\) does, only \(B\) does, or both do.

A useful boundary case is
\[
L^R_{u,u}(K_{a,b})=\max\bigl\{(a+b)(u-1),au,bu\bigr\}.
\]
For instance, \(L^R_{2,2}(K_{3,1})=6\), attained by assigning value \(2\) to all three vertices on the size-three side and \(0\) to the remaining vertex.

## Assumptions and scope
Graphs are finite, simple, and undirected. A Released \((k\mathbf 1,\mathbf 0,u\mathbf 1)\)-packing function is a map \(f:V(G)\to\{0,1,\ldots,u\}\) such that, whenever \(f(v)=u\), the closed-neighborhood sum satisfies \(f(N[v])\le k\). No restriction is imposed at vertices with value below \(u\).

The theorem covers all positive upper bounds \(u\) and all nonnegative uniform capacities \(k\), without assuming the normalization \(u\le k\le u|N[v]|\).

## Proof
Let
\[
X=\sum_{x\in A}f(x),\qquad Y=\sum_{y\in B}f(y).
\]
There are four exhaustive cases according to whether each side contains a saturated vertex, meaning a vertex with value \(u\).

If neither side is saturated, every vertex has value at most \(u-1\), so \(X+Y\le(a+b)(u-1)=T_0\). Equality is attained by assigning \(u-1\) everywhere.

Suppose \(A\) is saturated and \(B\) is not. For any saturated \(x\in A\), its closed neighborhood is \(\{x\}\cup B\), hence
\[
u+Y=f(N[x])\le k.
\]
Thus this case is possible only when \(k\ge u\), and then \(Y\le k-u\). Because \(B\) is not saturated, also \(Y\le b(u-1)\). There is no capacity condition restricting the values of other vertices of \(A\), so \(X\le au\). Therefore
\[
X+Y\le au+\min\{b(u-1),k-u\}=T_A.
\]
This bound is attained by assigning \(u\) to every vertex of \(A\) and distributing \(\min\{b(u-1),k-u\}\) units arbitrarily over \(B\), with no vertex of \(B\) exceeding \(u-1\). The case in which only \(B\) is saturated is symmetric and gives \(T_B\).

Finally suppose both sides are saturated. A saturated vertex of \(A\) forces \(Y\le k-u\), while a saturated vertex of \(B\) forces \(X\le k-u\). Since each saturated side has total at least \(u\), this case is possible only when \(k\ge2u\). Together with the trivial bounds \(X\le au\) and \(Y\le bu\),
\[
X+Y\le\min\{au,k-u\}+\min\{bu,k-u\}=T_{AB}.
\]
When \(k\ge2u\), each of the two target side-sums lies between \(u\) and the corresponding total capacity. Hence it can be realized by an integer assignment with at least one vertex equal to \(u\) on that side. The resulting function satisfies every active closed-neighborhood constraint, so \(T_{AB}\) is attained.

Taking the maximum over the four exhaustive saturation patterns proves the formula.

## Verification
The accompanying verifier enumerates every assignment \(f:V(K_{a,b})\to\{0,1,\ldots,u\}\) for \(1\le a,b\le3\), \(1\le u\le3\), and a range of capacities \(0\le k\le u(a+b+1)\). It checks the released-packing condition directly from the definition and compares the brute-force optimum with the closed formula. It also checks the explicit \(K_{3,1}\), \(u=k=2\) witness. This is a finite stress test only; the universal statement is proved by the four-case argument above.

## Relationship to prior work
Fekete, Hinrichsen, Leoni, and Lopez Pujato introduced released packing functions in arXiv:2608.11169v1 (11 August 2026). Their definition imposes the neighborhood-capacity condition only at vertices attaining the upper bound, and their paper develops complexity and polyhedral results. It gives small exact examples for paths, cycles, and wheels but does not state an exact complete-bipartite formula for arbitrary uniform \(k\) and \(u\).

A contemporary public review of that preprint independently notes that the paper's Observation 2.2(iii), asserting optimality of the all-\((u-1)\) assignment when \(k=u\) on connected graphs, is false and gives a \(P_3\) counterexample. The present result does not claim novelty for that falsity. Its contribution is the full exact biclique phase diagram for every \(a,b,k,u\), from which a large family of further counterexamples and sharp values follows.

Targeted searches for released packing, conditional-capacity packing, bicliques, and complete bipartite graphs found no prior statement implying the displayed formula.

## Limitations
The theorem treats uniform capacity and upper-bound vectors and zero lower bounds on complete bipartite graphs. It does not classify arbitrary vertex-dependent vectors, arbitrary lower bounds, or general multipartite graphs. The literature search cannot exclude an older equivalent result under terminology unrelated to released packing functions, although this risk is reduced because the invariant itself was introduced in 2026.

## References
1. P. Fekete, E. Hinrichsen, V. Leoni, M. I. Lopez Pujato, "Released packing functions in graphs," arXiv:2608.11169v1, 11 August 2026.
2. Pith, "Pith review of Released packing functions in graphs," pith:6OPKYP2C, 12 August 2026.
