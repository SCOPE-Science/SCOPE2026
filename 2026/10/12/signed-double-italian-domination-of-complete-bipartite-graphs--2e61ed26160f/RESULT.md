# Signed double Italian domination of complete bipartite graphs
## Finding
For integers
\[
2\le m\le n,
\]
the signed double Italian domination number of the complete bipartite graph \(K_{m,n}\) is
\[
\gamma_{sdI}(K_{m,n})=
\begin{cases}
4,&(m,n)=(2,2),\\
3,&2\le m\le3\text{ and }n\ge3,\\
4,&m\ge4.
\end{cases}
\]

The boundary \(K_{2,2}=C_4\) is already covered by the published cycle formula and is not part of the originality claim. The new content is the sharp complete-bipartite threshold outside that boundary: weight \(3\) is attainable exactly when the smaller part has size at most \(3\), while both parts of size at least \(4\) force weight \(4\).

## Assumptions and scope
A signed double Italian dominating function on a graph \(G\) is a map
\[
f:V(G)\to\{-1,1,2,3\}
\]
such that every vertex \(v\) satisfies
\[
\sum_{u\in N[v]}f(u)\ge1,
\]
and additionally a vertex with label \(-1\) has a subset of neighbors whose labels sum to at least \(3\), while a vertex with label \(1\) has a subset of neighbors whose labels sum to at least \(2\). Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_{sdI}(G)\) is the minimum weight.

Let \(X,Y\) be the bipartition of \(K_{m,n}\). Write
\[
S_X=\sum_{x\in X}f(x),\qquad S_Y=\sum_{y\in Y}f(y),
\]
and let \(P_X,P_Y\) be the corresponding sums over positive labels only. Because every vertex of one side sees every vertex of the other, the subset conditions reduce exactly to
\[
f(x)=-1\Longrightarrow P_Y\ge3,
\qquad
f(x)=1\Longrightarrow P_Y\ge2,
\]
with the symmetric conditions on \(Y\). The closed-neighborhood condition becomes
\[
f(x)+S_Y\ge1,
\qquad
f(y)+S_X\ge1.
\]

## Proof
We first prove the universal lower bound
\[
\gamma_{sdI}(K_{m,n})\ge3
\]
for \(m,n\ge2\).

Suppose a feasible function has weight at most \(2\). If \(S_X\le-1\), then feasibility forces \(S_X\in\{-2,-1\}\): when \(S_X=-2\), every vertex of \(Y\) must have label \(3\), and when \(S_X=-1\), every vertex of \(Y\) must have label at least \(2\). Hence the total weight is at least \(3\) in either case. The same holds with \(X,Y\) interchanged. Thus both side sums are nonnegative.

If \(S_X=0\), then, since \(|X|\ge2\) and zero is not an allowed label, some vertex of \(X\) has label \(-1\). Its closed-neighborhood inequality forces \(S_Y\ge2\). Weight at most \(2\) therefore gives \(S_Y=2\). No vertex of \(Y\) can then have label \(-1\), because such a vertex would require \(S_X\ge2\). Hence every label on \(Y\) is positive, so equality \(S_Y=2\) is possible only for \(n=2\) with both labels equal to \(1\). But then \(P_Y=2\), which cannot defend the label \(-1\) on \(X\), requiring positive neighbor sum at least \(3\). Thus neither side sum can be zero.

Both side sums are therefore positive. If one equals \(1\), that side necessarily contains a label \(-1\), because it has at least two vertices and all-positive labels would sum to at least \(2\). Such a label forces the opposite side sum to be at least \(2\), making the total weight at least \(3\). This proves the lower bound.

The published cycle formula gives
\[
\gamma_{sdI}(K_{2,2})=\gamma_{sdI}(C_4)=4.
\]

We now construct weight-\(3\) functions for every remaining graph with smaller part at most \(3\).

For \(m=2\) and odd \(n\ge3\), label the two vertices of \(X\) by \(2,2\). On \(Y\), assign \(1\) to \((n-1)/2\) vertices and \(-1\) to \((n+1)/2\) vertices. Then
\[
S_X=4,\qquad S_Y=-1,
\]
so the total weight is \(3\). Every vertex of \(X\) has closed-neighborhood sum \(1\); every vertex of \(Y\) has closed-neighborhood sum at least \(3\); and the positive sum on \(X\) is \(4\), enough for both neighbor-subset requirements on \(Y\).

For \(m=2\) and even \(n\ge4\), label \(X\) by \(1,2\), and split \(Y\) equally between labels \(1\) and \(-1\). Then
\[
S_X=3,\qquad S_Y=0,
\]
and \(P_Y=n/2\ge2\). The label \(1\) on \(X\) is therefore defended, every label \(-1\) on \(Y\) sees positive sum \(3\), and all closed-neighborhood sums are at least \(1\). Again the weight is \(3\).

For \(m=3\), label all three vertices of \(X\) by \(1\), so
\[
S_X=P_X=3.
\]
If \(n\) is even, split \(Y\) equally between \(1\) and \(-1\). If \(n\) is odd, assign one label \(2\), assign \(1\) to \((n-3)/2\) vertices, and assign \(-1\) to \((n+1)/2\) vertices. In both cases
\[
S_Y=0,\qquad P_Y\ge2.
\]
All defining inequalities follow immediately, and the total weight is \(3\).

It remains to treat \(m,n\ge4\). A weight-\(4\) construction is obtained independently on each side with side sum \(2\). If a side has even size \(r\), assign \(1\) to \((r+2)/2\) vertices and \(-1\) to \((r-2)/2\) vertices. If \(r\) is odd, necessarily \(r\ge5\); assign one label \(2\), and split the remaining \(r-1\) vertices equally between \(1\) and \(-1\). Each side then has sum \(2\) and positive-label sum at least \(3\). Thus every label \(-1\) has closed-neighborhood sum \(1\) and sees positive neighbor sum at least \(3\), while every label \(1\) satisfies the weaker subset requirement. Hence
\[
\gamma_{sdI}(K_{m,n})\le4.
\]

Finally, weight \(3\) is impossible when \(m,n\ge4\). If a side sum is negative, it can only be \(-1\) or \(-2\); the closed-neighborhood inequalities then force every vertex of the other side to have label at least \(2\) or exactly \(3\), respectively, making total weight larger than \(3\). Thus both side sums are nonnegative. Since they sum to \(3\), each is at most \(3\). But each side has at least four vertices, so each side must contain a label \(-1\). A label \(-1\) on either side forces the opposite side sum to be at least \(2\). Hence
\[
S_X+S_Y\ge4,
\]
a contradiction. Therefore the minimum is \(4\).

## Verification
The included checker does not enumerate vertex labelings naively. For each side size it enumerates all count-vectors of labels \(-1,1,2,3\), retaining the side sum, positive-label sum, and multinomial multiplicity. It then tests the defining closed-neighborhood and neighbor-subset conditions exactly for every pair of side states.

For every ordered pair
\[
2\le m,n\le12,
\]
it computes the true minimum independently of the closed formula. Across \(121\) complete bipartite instances it checks \(3{,}294{,}225\) side-state pairs, and every minimum agrees with the displayed piecewise theorem.

## Relationship to prior work
The 2023 paper introducing signed double Italian domination defines the invariant, proves complexity results including NP-completeness on bipartite graphs, develops bounds, and determines exact values for cycles and the Petersen graph. Its exact cycle formula already covers the boundary \(K_{2,2}=C_4\); that boundary is therefore excluded from the originality claim. Targeted inspection of the primary article found no complete-bipartite specialization.

A 2024 survey of Roman \(\{2\}\)-type domination summarizes signed double Italian domination and the results known from the defining paper. Searches under “complete bipartite,” “complete multipartite,” and the notation \(K_{m,n}\) did not locate a theorem implying the threshold proved here.

The theorem therefore extends the exact-family theory to a canonical bipartite class and identifies a sharp transition at smaller-part size \(4\).

## Limitations
The theorem concerns complete bipartite graphs with both parts of size at least \(2\). Stars are not included.

The boundary \(K_{2,2}\) is known from the published cycle formula and is included only to give a complete piecewise statement.

The finite computation is corroborative only; the all-parameter result follows from the symbolic side-sum proof.

A differently phrased or non-indexed equivalent complete-bipartite result may exist.

## References
1. A. Almulhim, “Signed double Italian domination,” AIMS Mathematics 8(12) (2023), 30895–30909, DOI 10.3934/math.20231580; published 17 November 2023.
2. A. Almulhim, B. Al Subaiei, S. R. Mondal, “Survey on Roman \(\{2\}\)-Domination,” Mathematics 12(17) (2024), 2771, DOI 10.3390/math12172771.
