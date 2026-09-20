# Szeged–Wiener equality for graphs with an \((n-2)\)-clique

## Result

For a connected graph \(G\), write
\[
\eta(G)=\operatorname{Sz}(G)-W(G)
\]
for its Szeged–Wiener gap.

Zhang and Li (2026) proved that every 2-connected \(n\)-vertex graph with \(n\ge 10\), other than \(K_n,K_n^2,K_n^{n-2}\), satisfies \(\eta(G)\ge 2n\), and posed the problem of classifying equality. They also exhibited, for every \(n\ge10\), the graph \(G_n\) obtained from a clique \(Q\cong K_{n-2}\) by choosing distinct \(p,q\in Q\), adding adjacent vertices \(x,y\), and adding only the two further edges \(xp,yq\); this graph satisfies \(\eta(G_n)=2n\).

The equality problem can be solved completely in the high-clique regime.

**Theorem.** Let \(G\) be a 2-connected graph of order \(n\ge10\) containing a clique of order \(n-2\). Then \(\eta(G)=2n\) if and only if one of the following holds.

1. \(G\cong G_n\): a clique \(Q\cong K_{n-2}\), two adjacent vertices \(x,y\notin Q\), and distinct \(p,q\in Q\) with
   \[
   N_Q(x)=\{p\},\qquad N_Q(y)=\{q\}.
   \]
2. \(n=10\) and \(G\cong H_{10}\), where \(Q\cong K_8\), \(x,y\) are adjacent, and for distinct \(p,q\in Q\),
   \[
   N_Q(x)=\{p\},\qquad N_Q(y)=\{p,q\}.
   \]

Thus, for every \(n\ge11\), the Zhang–Li construction is the unique equality graph among all 2-connected graphs with clique number at least \(n-2\). At order \(10\), there is exactly one additional isomorphism type in this regime.

The proof yields an exact Szeged–Wiener-gap formula for every graph obtained by adjoining two vertices to a clique.

## Exact two-vertex extension formula

Let \(Q\cong K_q\), let \(x,y\notin Q\), and let
\[
A=N_Q(x),\qquad B=N_Q(y).
\]
Assume \(A,B\neq\varnothing\), so the resulting graph is connected. Partition \(Q\) according to the two neighborhood indicators and write
\[
a=|A\setminus B|,\quad b=|B\setminus A|,\quad c=|A\cap B|,\quad d=|Q\setminus(A\cup B)|,
\]
so \(q=a+b+c+d\).

If \(xy\in E(G)\), then
\[
\boxed{\eta(G)=8ab+2ac+3ad+2bc+3bd+4cd-4d.}
\tag{1}
\]

If \(xy\notin E(G)\) and \(c>0\), then
\[
\boxed{\eta(G)=5ab+2ac+2ad-2a+2bc+2bd-2b+4cd+2c-4d-2.}
\tag{2}
\]

If \(xy\notin E(G)\) and \(c=0\), then
\[
\boxed{\eta(G)=5ab+2ad-a+2bd-b-4d-3.}
\tag{3}
\]

These formulas distinguish only the four Venn cells of \(A,B\), as expected from the symmetry of the clique.

## Proof of the formulas

For an edge \(uv\) inside \(Q\), every clique vertex other than \(u,v\) is equidistant from the endpoints. The vertices \(x\) and \(y\) distinguish \(u,v\) exactly when their membership indicators in \(A\) and \(B\) differ. Summing over the six unordered pairs of the four Venn cells gives the total contribution of clique edges to the Szeged index:
\[
\binom q2 +(a+b)(c+d)+3ab+2cd.
\tag{4}
\]

Suppose first that \(xy\in E(G)\). For an edge \(xu\) with \(u\in A\), all vertices of \(Q\setminus A\) are closer to \(u\), while \(y\) is closer to \(x\) exactly when \(u\in A\setminus B\). Hence all \(xQ\)-edges together contribute
\[
(2a+c)(q-a-c+1).
\tag{5}
\]
Similarly, the \(yQ\)-edges contribute
\[
(2b+c)(q-b-c+1).
\tag{6}
\]
For the edge \(xy\), the two strict sides have sizes \(a+1\) and \(b+1\), so its contribution is
\[
(a+1)(b+1).
\tag{7}
\]
The Wiener index is
\[
W(G)=\binom q2+4q-(a+c)-(b+c)+1.
\tag{8}
\]
Subtracting (8) from the sum of (4)–(7) gives (1).

Now suppose \(xy\notin E(G)\). If \(c>0\), then \(d(x,y)=2\). For \(u\in A\), the vertex \(y\) is closer to \(u\) than to \(x\) precisely when \(u\in A\cap B\), giving total \(xQ\)-edge contribution
\[
(a+c)(q-a-c+1)+c.
\tag{9}
\]
The analogous \(yQ\) term is
\[
(b+c)(q-b-c+1)+c.
\tag{10}
\]
Here
\[
W(G)=\binom q2+4q-(a+c)-(b+c)+2,
\]
and (2) follows from (4), (9), and (10).

Finally, if \(xy\notin E(G)\) and \(c=0\), then \(d(x,y)=3\). For every \(u\in A\), the vertex \(y\) is closer to \(u\) than to \(x\), so the \(xQ\)-edge contribution is
\[
a(q-a+2),
\]
and similarly the \(yQ\)-edge contribution is \(b(q-b+2)\). Together with
\[
W(G)=\binom q2+4q-a-b+3,
\]
this yields (3).

## Equality classification

For the remainder set \(q=n-2\ge8\).

The graph is 2-connected exactly under the following elementary conditions:

- if \(xy\in E(G)\), then \(|A|,|B|\ge1\) and \(|A\cup B|\ge2\);
- if \(xy\notin E(G)\), then \(|A|,|B|\ge2\).

Indeed, the stated conditions are necessary by deleting \(x\), \(y\), or a unique clique attachment; conversely they ensure that deleting any single vertex leaves all remaining vertices connected through the clique (and, when present, the edge \(xy\)).

### Nonadjacent outside vertices

First let \(xy\notin E(G)\).

If \(c=0\), put \(s=a+b\). Two-connectivity gives \(a,b\ge2\), and (3) gives
\[
\eta(G)-2n
=5ab-3s-7+2d(s-3).
\tag{11}
\]
Since \(ab\ge2(s-2)\) for \(a,b\ge2\) and \(s\ge4\),
\[
5ab-3s-7\ge 10(s-2)-3s-7=7s-27>0.
\]
Thus equality is impossible.

If \(c>0\), formula (2) gives
\[
\eta(G)-2n
=5ab+2s(c-2)-6+d(2s+4c-6).
\tag{12}
\]
The coefficient of \(d\) is positive under the two-connectivity assumptions. Setting (12) equal to zero leaves only small possibilities:

- \(c=1\): then \(a,b\ge1\), and
  \[
  2d(s-1)=6+2s-5ab.
  \]
  Since \(ab\ge s-1\), the right side is nonnegative only for \(s\le3\); \(s=2,3\) give respectively \(d=5/2,1/2\).
- \(c=2\):
  \[
  d(2s+2)=6-5ab.
  \]
  Nonnegative right side forces \(ab\le1\). The only integral possibilities have \(q<8\).
- \(c\ge3\): nonnegativity of the right side forces \(ab=0\) and only finitely many values of \(s(c-2)\). If \(s=0\), equality reduces to \(d(4c-6)=6\), whose only integral solution is \(c=3,d=1\), giving \(q=4\). If \(s\ge1\), every positive right side is strictly smaller than the positive coefficient of \(d\), while the zero-right-side possibilities are \((s,c)=(3,3)\) and \((1,5)\), both with \(q=6\). Hence no solution has \(q\ge8\).

So no equality graph in the theorem has \(xy\notin E(G)\).

### Adjacent outside vertices

Now let \(xy\in E(G)\).

If \(c=0\), two-connectivity gives \(a,b\ge1\), and (1) becomes
\[
\eta(G)-2n
=2(4ab-a-b-2)+3d(a+b-2).
\tag{13}
\]
Both terms are nonnegative, and both vanish exactly when \(a=b=1\). This is precisely \(G_n\): the two outside vertices attach to distinct single clique vertices.

Suppose \(c\ge1\), and again write \(s=a+b\). Then
\[
\eta(G)-2n
=8ab+2s(c-1)-2c-4+d(3s+4c-6).
\tag{14}
\]
If \(s=0\), two-connectivity forces \(c\ge2\), and equality would imply
\[
d(2c-3)=c+2,
\]
which has no solution with \(q\ge8\). If \(s=1\), then \(ab=0\), and equality in (14) is
\[
d(4c-3)=6.
\]
The unique solution with \(q\ge8\) is \(c=1,d=6\), hence \(q=8\), which is exactly \(H_{10}\) (up to exchanging \(x,y\)).

Finally let \(s\ge2\). If \(ab>0\), the right side of (14) is already strictly positive at \(d=0\). If \(ab=0\), equality can occur only when
\[
(s-1)(c-1)\le3.
\]
Checking the resulting possibilities \(c=1\), \(c=2\) with \(s\le4\), \(c=3\) with \(s=2\), and \(c=4\) with \(s=2\) gives either a nonintegral \(d\) or \(q=6\). Hence there are no further solutions for \(q\ge8\).

This proves the theorem.

## Verification

A standalone verifier in `artifacts/verify_near_complete.py` computes graph distances, the Wiener index, and the Szeged index directly from the definitions. It checks the closed formulas and the 2-connectivity criterion for every Venn-cell parameter type with \(2\le q\le10\) and nonempty \(A,B\), and separately checks the equality classification over all parameter types with \(8\le q\le40\). The saved output is in `artifacts/verification.txt`. These finite checks support but do not replace the proof.

## Literature context and originality

The current full text of Zhang and Li, *Improved Bounds on the Szeged–Wiener Gap and the BKLPS Conjecture*, arXiv:2609.20025v1 (17 September 2026), proves the lower bound \(\eta(G)\ge2n\), explicitly poses classification of the equality cases as Problem 7, and gives the family \(G_n\) above as a sufficient construction. Its searchable full text contains no clique-number or \((n-2)\)-clique equality classification. The result here proves that their construction is the only equality type in the entire \((n-2)\)-clique regime once \(n\ge11\), and identifies the unique order-10 exception in that regime.

The earlier primary source of Bonamy, Knor, Lužar, Pinlou, and Škrekovski, *On the difference between the Szeged and Wiener index* (Applied Mathematics and Computation 312 (2017), 202–213; arXiv:1602.05184), proves the sharp \(2n-6\) bound and classifies that older equality case as \(K_n^2\) and \(K_n^{n-2}\). It proposed the stronger \(2n\) conjecture but does not contain the equality classification proved here.

Targeted searches for the Szeged–Wiener gap together with clique number, \((n-2)\)-cliques, near-complete graphs, two-vertex extensions of a clique, and the equation \(\eta(G)=2n\) did not locate an equivalent theorem or the three-case formula (1)–(3). To the best of our knowledge, the result is new. No specific inaccessible paper was identified as a likely source of prior coverage; the residual originality risk is unindexed parallel work or older work using substantially different terminology for near-complete graphs.

## Limitations

The classification addresses the high-clique slice \(\omega(G)\ge n-2\) of the equality problem, not all 2-connected graphs with \(\eta(G)=2n\). The recent source explicitly states that its displayed construction is not a necessary condition in general, so equality types with smaller clique number remain outside this result. The computational checks are finite supporting evidence only.

## References

1. L. Zhang and E. Li, *Improved Bounds on the Szeged–Wiener Gap and the BKLPS Conjecture*, arXiv:2609.20025v1, 2026. https://arxiv.org/abs/2609.20025
2. M. Bonamy, M. Knor, B. Lužar, A. Pinlou, and R. Škrekovski, *On the difference between the Szeged and Wiener index*, Applied Mathematics and Computation 312 (2017), 202–213. https://arxiv.org/abs/1602.05184

Same-model review: passed. Independent audit: not yet performed.
