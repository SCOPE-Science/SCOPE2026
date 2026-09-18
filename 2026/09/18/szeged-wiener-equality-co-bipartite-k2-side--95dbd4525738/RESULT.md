# Exact Szeged-Wiener equality in a co-bipartite class

## Statement

For a connected graph \(G\), write
\[
W(G)=\sum_{\{u,v\}\subseteq V(G)} d(u,v)
\]
for the Wiener index and
\[
Sz(G)=\sum_{uv\in E(G)} n_{uv}(u)n_{uv}(v)
\]
for the Szeged index, where \(n_{uv}(u)\) is the number of vertices strictly closer to \(u\) than to \(v\). Put
\[
\eta(G)=Sz(G)-W(G).
\]

Zhang and Li proved in 2026 that every \(n\)-unexceptional 2-connected graph of order \(n\ge 10\) satisfies
\[
\eta(G)\ge 2n,
\]
and posed the problem of determining all equality graphs. They also gave, for every \(n\ge10\), an equality graph obtained from a clique \(Q\cong K_{n-2}\) by adjoining adjacent vertices \(x,y\), with one edge from \(x\) to \(Q\) and one edge from \(y\) to a different vertex of \(Q\).

The following gives an exact formula and equality classification on a natural dense subclass.

**Theorem.** Let \(q\ge 8\), and let \(G\) be a 2-connected co-bipartite graph with a fixed clique partition
\[
V(G)=Q\mathbin{\dot\cup}\{x,y\},
\qquad
Q\cong K_q,
\qquad
xy\in E(G).
\]
Partition \(Q\) into
\[
\begin{aligned}
A&=N_Q(x)\setminus N_Q(y),\\
B&=N_Q(y)\setminus N_Q(x),\\
C&=N_Q(x)\cap N_Q(y),\\
D&=Q\setminus(N_Q(x)\cup N_Q(y)),
\end{aligned}
\]
and put \(a=|A|,b=|B|,c=|C|,d=|D|\). Then
\[
\boxed{\eta(G)=8ab+2c(a+b)+3d(a+b)+4cd-4d.}
\tag{1}
\]

Since \(n=q+2\), equality \(\eta(G)=2n\) holds if and only if one of the following occurs:

1. \(a=b=1,\ c=0,\ d=q-2\);
2. \(q=8\) and, up to interchanging \(x\) and \(y\),
   \[
   (a,b,c,d)=(1,0,1,6).
   \]

Consequently, for every \(n\ge11\), the Zhang--Li construction is the unique equality graph in this co-bipartite class. At \(n=10\), exactly one further isomorphism type occurs: take \(Q\cong K_8\), distinct \(u,v\in Q\), adjacent new vertices \(x,y\), and add cross-edges
\[
xu,\quad xv,\quad yv.
\]
This second graph has \(\eta(G)=20\). Zhang and Li already note that their displayed sufficient construction is not necessary in general; the theorem above identifies precisely what happens inside this subclass and does not assert that this ten-vertex graph was unknown to them.

## Proof

Because \(G\) is 2-connected, each of \(x,y\) has a neighbor in \(Q\), and their union of \(Q\)-neighbors has size at least two. Equivalently,
\[
a+c\ge1,\qquad b+c\ge1,\qquad a+b+c\ge2.
\tag{2}
\]
Conversely, when \(q\ge2\), these conditions are also sufficient for 2-connectivity: deleting \(x\) or \(y\) leaves the other attached to the clique \(Q\), while deleting one vertex of \(Q\) leaves at least one attachment from \(\{x,y\}\) to \(Q\).

Under (2), \(G\) has diameter at most two. Its nonedges are precisely the pairs from \(x\) to \(B\cup D\) and from \(y\) to \(A\cup D\). Hence
\[
W(G)=\binom{q+2}{2}+a+b+2d.
\tag{3}
\]

For an edge \(uv\) in any diameter-two graph,
\[
n_{uv}(u)=\deg(u)-|N(u)\cap N(v)|.
\tag{4}
\]
Indeed, apart from \(u\) itself, the vertices closer to \(u\) than to \(v\) are exactly the neighbors of \(u\) that are not neighbors of \(v\).

The degrees here are
\[
\deg(x)=1+a+c,\qquad \deg(y)=1+b+c,
\]
and vertices in \(A,B,C,D\) have degrees \(q,q,q+1,q-1\), respectively. Formula (4) gives the following edge contributions \(n_{uv}(u)n_{uv}(v)\):

- an edge inside \(Q\) contributes \(1\) when both endpoints have the same type;
- an \(A\)-\(B\) edge contributes \(4\);
- an \(A\)-\(C\), \(B\)-\(C\), \(A\)-\(D\), or \(B\)-\(D\) edge contributes \(2\);
- a \(C\)-\(D\) edge contributes \(3\);
- \(xy\) contributes \((a+1)(b+1)\);
- each \(xA\) edge contributes \(2(b+d+1)\), and each \(xC\) edge contributes \(b+d+1\);
- each \(yB\) edge contributes \(2(a+d+1)\), and each \(yC\) edge contributes \(a+d+1\).

Therefore
\[
\begin{aligned}
Sz(G)
={}&\binom q2
+3ab+c(a+b)+d(a+b)+2cd\\
&+(a+1)(b+1)
+2a(b+d+1)+c(b+d+1)\\
&+2b(a+d+1)+c(a+d+1).
\end{aligned}
\tag{5}
\]
Subtracting (3) from (5) proves (1).

It remains to solve the equality condition. Let
\[
s=a+b.
\]
Using \(q=a+b+c+d\), equation \(\eta(G)=2(q+2)\) is equivalent to
\[
0=
8ab+2c(s-1)+d(3s+4c-6)-2s-4.
\tag{6}
\]

### Case 1: \(c=0\)

By (2), \(a,b\ge1\), hence \(s\ge2\). If \(s=2\), then \(a=b=1\), and (6) vanishes for every \(d\). This is exactly family 1.

If \(s\ge3\), then \(ab\ge s-1\) and \(3s-6\ge0\), so the right side of (6) is at least
\[
8(s-1)-2s-4=6s-12>0.
\]
Thus there are no other equality cases with \(c=0\).

### Case 2: \(c\ge1\)

The coefficient
\[
\delta=3s+4c-6
\]
of \(d\) in (6) is positive under (2).

If \(a,b\ge1\), then \(s\ge2\) and \(ab\ge s-1\). Rearranging (6) gives
\[
d\delta
=
2s+4-8ab-2c(s-1)
\le 14-8s<0,
\]
a contradiction. Hence \(ab=0\). By symmetry assume \(b=0\), so \(s=a\).

If \(s=0\), then \(c\ge2\), and (6) becomes
\[
d(4c-6)=2c+4.
\]
Its nonnegative integer solutions are \((c,d)=(2,4)\) and \((5,1)\), both with \(q=6\), outside \(q\ge8\).

Now let \(s\ge1\). If \(c=1\), equation (6) reduces to
\[
d(3s-2)=6.
\]
The only solution is \(s=1,d=6\), giving \(q=8\), which is family 2.

Finally suppose \(c\ge2\). If \(s=1\), then \(d(4c-3)=6\), which has no integer solution. If \(s=2\), the only nonnegative possibilities for the numerator in
\[
d(3s+4c-6)=2s+4-2c(s-1)
\]
are \(c=2,3,4\); direct substitution gives no solution with \(q\ge8\). If \(s=3\), only \(c=2\) leaves a positive right side, but it is smaller than the positive coefficient of \(d\). If \(s\ge4\), the right side is at most \(8-2s\le0\); equality at zero forces \(d=0\) and
\[
c=\frac{s+2}{s-1}=1+\frac3{s-1},
\]
whose only possibility with \(s\ge4,c\ge2\) is \(s=4,c=2\), again giving \(q=6\). Thus no further solution occurs for \(q\ge8\).

This completes the classification.

## Relation to the open equality problem

Bonamy--Knor--Lužar--Pinlou--Škrekovski proved the earlier universal lower bound
\[
\eta(G)\ge2n-6
\]
for 2-connected noncomplete graphs and conjectured the strengthened \(2n\) lower bound outside the three exceptional families for \(n\ge10\). Zhang and Li proved that conjecture and then explicitly posed the equality classification problem. Their Lemma 8 supplies family 1 above and explicitly remarks that this sufficient condition is not necessary.

The theorem here does not solve the global equality problem. It gives a complete answer on the co-bipartite subclass having a two-vertex clique side, including an exact closed formula for every graph in the class and a rigidity statement for all \(n\ge11\).

## Computational verification

The accompanying standard-library Python script constructs every parameter quadruple \((a,b,c,d)\) satisfying the 2-connectivity conditions for \(2\le q\le20\), computes all-pairs graph distances directly, evaluates \(W\) and \(Sz\) from their definitions, and checks formula (1). It also checks the stated equality classification for \(8\le q\le20\). The computation is supplementary evidence; the proof above is general and does not rely on enumeration.

## Limitations and originality

The result classifies only co-bipartite graphs admitting a clique partition with one side of size two. It does not characterize all equality graphs in Zhang--Li Problem 7.

Originality is to the best of our knowledge. Exact and synonymous searches were made for the Szeged--Wiener gap on co-bipartite graphs, two-clique graphs, and the equality value \(2n\). The full accessible 2017 Bonamy--Knor--Lužar--Pinlou--Škrekovski paper and the accessible 2026 Zhang--Li preprint were checked at the directly relevant theorem/problem statements; neither gives formula (1) or this subclass classification. Klavžar--Nadjafi-Arani (2014) was also checked for co-bipartite/two-clique terminology and its abstract/structural focus concerns other lower-bound regimes. No inaccessible paper was identified as specifically likely to contain this exact classification. Because the equality problem has only just been posed in the cited 2026 preprint, very recent or unindexed parallel work remains the principal residual originality risk.

## References

1. L. Zhang and E. Li, *Improved Bounds on the Szeged-Wiener Gap and the BKLPS Conjecture*, arXiv:2609.20025 (2026). https://arxiv.org/abs/2609.20025
2. M. Bonamy, M. Knor, B. Lužar, A. Pinlou, and R. Škrekovski, *On the difference between the Szeged and the Wiener index*, Applied Mathematics and Computation 312 (2017), 202--213. https://doi.org/10.1016/j.amc.2017.05.047
3. S. Klavžar and M. J. Nadjafi-Arani, *Improved bounds on the difference between the Szeged index and Wiener index of graphs*, European Journal of Combinatorics 39 (2014), 148--156. https://doi.org/10.1016/j.ejc.2014.01.001
