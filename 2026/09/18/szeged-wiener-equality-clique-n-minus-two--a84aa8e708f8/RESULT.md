# Szeged–Wiener equality for graphs with an \((n-2)\)-clique

Let \(G\) be a finite simple connected graph. Write
\[
W(G)=\sum_{\{u,v\}\subseteq V(G)} d_G(u,v),
\qquad
Sz(G)=\sum_{uv\in E(G)} n_{uv}(u)n_{uv}(v),
\]
where \(n_{uv}(u)\) is the number of vertices strictly closer to \(u\) than to \(v\), and put
\[
\eta(G)=Sz(G)-W(G).
\]

Zhang and Li proved in arXiv:2609.20025 that every \(n\)-unexceptional 2-connected graph of order \(n\ge 10\) satisfies \(\eta(G)\ge 2n\). They constructed an equality graph for every \(n\ge 10\) and posed the problem of characterizing all equality cases.

## Theorem

Let \(G\) be a 2-connected graph of order \(n\ge 10\) containing a clique \(Q\) of order \(n-2\). Then
\[
\eta(G)=2n
\]
if and only if \(G\) is isomorphic to one of the following graphs.

1. **The Zhang–Li family \(G_n\).** Start with \(Q\cong K_{n-2}\), choose distinct \(p,q\in Q\), add adjacent vertices \(x,y\), and among the edges from \(\{x,y\}\) to \(Q\) add only \(xp\) and \(yq\). Equivalently,
   \[
   \overline{G_n}
   \]
   is obtained from \(K_{2,n-4}\) by attaching one pendant leaf to each vertex in the part of size \(2\).

2. **One additional graph at order \(10\).** Let \(J_{10}\) be the graph whose complement is obtained from \(K_{2,6}\) by attaching one pendant leaf to one vertex in the part of size \(2\) and adding one isolated vertex. Then
   \[
   \eta(J_{10})=20.
   \]

In particular, the equality problem of Zhang and Li is completely determined in the regime
\[
\omega(G)\ge n-2.
\]
Within this regime, their infinite family is the unique equality family for every \(n\ge 11\), while \(n=10\) has exactly one further isomorphism type.

## Exact four-parameter formulas

Fix a clique \(Q\) of order \(n-2\) and write \(V(G)\setminus Q=\{x,y\}\). Partition \(Q\) according to adjacency to \(x,y\):
\[
\begin{aligned}
A&=\{v\in Q: vy\in E(G),\ vx\notin E(G)\},\\
B&=\{v\in Q: vx\in E(G),\ vy\notin E(G)\},\\
C&=\{v\in Q: vx,vy\notin E(G)\},\\
D&=\{v\in Q: vx,vy\in E(G)\},
\end{aligned}
\]
and let
\[
a=|A|,\quad b=|B|,\quad c=|C|,\quad d=|D|.
\]
Thus
\[
n=2+a+b+c+d.
\]

### Adjacent outside vertices

If \(xy\in E(G)\), then
\[
\boxed{\eta(G)=8ab+3c(a+b)+2d(a+b)+4cd-4c.}
\tag{1}
\]

### Nonadjacent outside vertices

If \(xy\notin E(G)\) and \(d\ge 1\), then
\[
\boxed{\eta(G)=
5ab+2c(a+b)+2d(a+b)+4cd-2a-2b-4c+2d-2.}
\tag{2}
\]

If \(xy\notin E(G)\) and \(d=0\), 2-connectivity forces \(a,b\ge 2\), and
\[
\boxed{\eta(G)=5ab+2c(a+b)-a-b-4c-3.}
\tag{3}
\]

These formulas may be useful independently of the equality classification.

## Proof of the formulas

All vertices of \(Q\) are mutually adjacent. For an edge \(uv\) with \(u,v\in Q\), every other vertex of \(Q\) is equidistant from \(u,v\), so only \(x,y\) can change the Szeged contribution from the baseline value \(1\). The contribution \(n_{uv}(u)n_{uv}(v)\) depends only on the types of \(u,v\):

\[
\begin{array}{c|cccccc}
\text{types} & AB & AC & AD & BC & BD & CD\\ \hline
n_{uv}(u)n_{uv}(v) & 4&2&2&2&2&3.
\end{array}
\]

Pairs of the same type contribute \(1\). Hence the total contribution of the edges inside \(Q\) is
\[
\binom{n-2}{2}
+3ab+ac+ad+bc+bd+2cd.
\tag{4}
\]

Suppose first that \(xy\in E(G)\). Since \(G\) is 2-connected, any missing edge between \(\{x,y\}\) and \(Q\) has distance \(2\). Direct comparison of distances gives the following contributions:
\[
\begin{array}{c|ccccc}
\text{edge type} & xB & xD & yA & yD & xy\\ \hline
n_{uv}(u)n_{uv}(v)
&2(a+c+1)&a+c+1&2(b+c+1)&b+c+1&(a+1)(b+1).
\end{array}
\]
Moreover,
\[
W(G)=\binom n2+a+b+2c.
\]
Adding these terms to (4) and subtracting \(W(G)\) simplifies to (1).

Now suppose \(xy\notin E(G)\). If \(d\ge1\), a vertex of \(D\) gives a common neighbor of \(x,y\), so every nonedge has distance \(2\). The edge contributions incident with \(x\) or \(y\) are
\[
\begin{array}{c|cccc}
\text{edge type} & xB & xD & yA & yD\\ \hline
n_{uv}(u)n_{uv}(v)
&a+c+1&a+c+2&b+c+1&b+c+2.
\end{array}
\]
Here
\[
W(G)=\binom n2+a+b+2c+1.
\]
Together with (4), this gives (2).

Finally let \(xy\notin E(G)\) and \(d=0\). The degrees of \(x,y\) are \(b,a\), respectively, hence 2-connectivity gives \(a,b\ge2\). In this case \(d_G(x,y)=3\). The two incident edge types contribute
\[
xB:\ a+c+2,\qquad yA:\ b+c+2,
\]
and
\[
W(G)=\binom n2+a+b+2c+2.
\]
Equation (4) now reduces to the \(A,B,C\) types, and subtraction gives (3).

## Solving the equality equation

We now impose \(\eta(G)=2n\).

### Case 1: \(xy\in E(G)\)

From (1),
\[
\eta(G)-2n
=
8ab-2a-2b-4
+c(3a+3b+4d-6)
+2d(a+b-1).
\tag{5}
\]

If \(d=0\), 2-connectivity forces \(a,b\ge1\). For \(a=b=1\), the right-hand side of (5) is identically \(0\), while for every other pair \(a,b\ge1\) it is positive. Thus
\[
a=b=1,\qquad d=0,
\]
and \(c=n-4\). This is exactly \(G_n\).

If \(d=1\), (5) becomes
\[
8ab-6+c(3(a+b)-2).
\tag{6}
\]
If \(a+b=1\), equation (6) vanishes exactly when \(c=6\), giving \(n=10\) and \(J_{10}\). If \(a+b=0\), it is negative and never zero. If \(a+b\ge2\), then either \(ab\ge1\), in which case (6) is positive, or \(ab=0\), in which case \(3(a+b)-2\ge4\) and no nonnegative integer \(c\) solves (6).

Let \(d\ge2\). If \(ab\ge1\), the constant part of (5) is already positive. Hence an equality solution must have \(ab=0\); put \(s=a+b\). Then
\[
2s(d-1)-2d-4+c(3s+4d-6)=0.
\tag{7}
\]
If \(c=0\), equation (7) gives
\[
s(d-1)=d+2,
\]
whose nonnegative integer solutions with \(d\ge2\) are \((d,s)=(2,4),(4,2)\), both of order \(8\). If \(c\ge1\), (7) implies \(3s+2d\le10\); checking \(d=2,3,4,5\) gives only \((d,s,c)=(2,0,4)\) and \((5,0,1)\), again both of order \(8\). Thus no further solution exists for \(n\ge10\).

### Case 2: \(xy\notin E(G)\)

First let \(d=0\). Using (3),
\[
\eta(G)-2n
=
5ab-3a-3b-7+2c(a+b-3).
\tag{8}
\]
Since \(a,b\ge2\), the first four terms are at least \(1\), and \(a+b-3\ge1\). Hence (8) is positive.

Now let \(d\ge1\), and put \(s=a+b\). Formula (2) gives
\[
\eta(G)-2n
=
5ab+2s(c+d-2)+c(4d-6)-6.
\tag{9}
\]

For \(d=1\), 2-connectivity forces \(a,b\ge1\). Equality in (9) would require
\[
2c(s-1)=2s+6-5ab.
\]
If \(\min\{a,b\}\ge2\), the right-hand side is negative. Otherwise, say \(a=1\le b\); nonnegativity forces \(b\in\{1,2\}\), which would require respectively \(c=5/2\) or \(c=1/2\). Thus there is no integer solution.

For \(d=2\), equality becomes
\[
5ab+c(2s+2)=6.
\]
If \(ab\ge1\), this has no nonnegative integer solution. If \(ab=0\), it reduces to \(c(s+1)=3\), and every solution has order \(7\).

For \(d\ge3\), if \(ab\ge1\) then the right-hand side of (9) is positive. Hence \(ab=0\), and equality becomes
\[
2s(d-2)-6+c(2s+4d-6)=0.
\]
If \(c=0\), then \(s(d-2)=3\), giving only order \(8\). If \(c\ge1\), the coefficient comparison forces a finite set of smaller possibilities; the only equality possibility is \(d=3,s=0,c=1\), of order \(6\). Consequently no nonadjacent-\(x,y\) equality graph occurs for \(n\ge10\).

This proves the theorem. ∎

## Relation to the current literature

Zhang and Li, *Improved Bounds on the Szeged–Wiener Gap and the BKLPS Conjecture* (arXiv:2609.20025, submitted 17 September 2026), prove the lower bound
\[
\eta(G)\ge2n
\]
for every \(n\)-unexceptional 2-connected graph of order \(n\ge10\). Their Problem 7 asks for all equality graphs. Their Lemma 8 gives the family called \(G_n\) above and explicitly notes that this sufficient construction is not necessary.

The theorem here determines every equality graph having a clique of order at least \(n-2\). It recovers their entire equality construction, proves its uniqueness in that regime for all \(n\ge11\), and exhibits the unique additional high-clique equality graph \(J_{10}\).

The earlier paper of Bonamy, Knor, Lužar, Pinlou, and Škrekovski, *On the difference between the Szeged and the Wiener index* (arXiv:1602.05184; Applied Mathematics and Computation 312 (2017), 202–213), proves the sharp \(2n-6\) bound and characterizes those equality cases, but does not contain the \(2n\)-equality classification above.

## Limitations

This is a partial solution of Zhang–Li Problem 7, not a full solution. It classifies equality only under the structural hypothesis
\[
\omega(G)\ge n-2.
\]
Graphs with \(\omega(G)\le n-3\) remain outside the theorem. No independent validation or journal peer review is asserted.

## References

1. L. Zhang and E. Li, *Improved Bounds on the Szeged–Wiener Gap and the BKLPS Conjecture*, arXiv:2609.20025 (2026), https://arxiv.org/abs/2609.20025.
2. M. Bonamy, M. Knor, B. Lužar, A. Pinlou, and R. Škrekovski, *On the difference between the Szeged and the Wiener index*, Applied Mathematics and Computation 312 (2017), 202–213; arXiv:1602.05184, https://arxiv.org/abs/1602.05184.
