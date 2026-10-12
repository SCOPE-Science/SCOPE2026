# Matching deletion preserves the \(p\)-strong Roman value of bicliques with both shores at least three
## Finding
Let \(3\le r\le s\), \(0\le t\le r\), and \(p\ge3\) be integers. Let \(G_{r,s,t}=K_{r,s}-M_t\), where \(M_t\) is any matching of size \(t\). Then
\[
\gamma^{p}_{\mathrm{StR}}(G_{r,s,t})
=2+\left\lceil\frac{r-1}{p}\right\rceil+\left\lceil\frac{s-1}{p}\right\rceil.
\]
Hence deleting any matching preserves the complete-bipartite value in this range. In particular, for the crown graph \(\operatorname{Cr}_n=K_{n,n}-M_n\), \(n\ge3\),
\[
\gamma^{p}_{\mathrm{StR}}(\operatorname{Cr}_n)=2+2\left\lceil\frac{n-1}{p}\right\rceil.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The bipartition of \(G_{r,s,t}\) is denoted by \(A\cup B\), where \(|A|=r\) and \(|B|=s\). The deleted edges form a matching, so each vertex loses at most one cross-edge.

For a positive integer \(p\), a \(p\)-strong Roman dominating function is a map
\[
f:V(G)\to\left\{0,1,\ldots,\left\lceil\frac{\Delta(G)+p}{p}\right\rceil\right\}
\]
such that every vertex \(v\) with \(f(v)=0\) has a neighbor \(u\) satisfying
\[
f(u)\ge 1+\left\lceil\frac{|N(u)\cap B_0|}{p}\right\rceil,
\qquad B_0=\{x:f(x)=0\}.
\]
The quantity \(\gamma^p_{\mathrm{StR}}(G)\) is the minimum weight \(\sum_v f(v)\). The result is proved for every \(p\ge3\), including values beyond the parameter range in the published complete-bipartite proposition.

## Proof
Write \(z_A=|A\cap B_0|\), \(z_B=|B\cap B_0|\), and let \(W_A\) and \(W_B\) be the total labels on the two shores. Define
\[
\phi_p(0)=0,
\qquad
\phi_p(z)=\min\left\{\left\lceil\frac z p\right\rceil,
2\left\lceil\frac{z-1}{p}\right\rceil\right\}
\quad(z\ge1).
\]

Assume first that \(z_B>0\). Every zero in \(B\) must have an adjacent defender in \(A\). If exactly one vertex of \(A\) is capable of defending zeros in \(B\), then its unique possible deleted cross-neighbor cannot itself be a zero in \(B\); otherwise that zero has no adjacent capable defender. Consequently that defender sees all \(z_B\) zeros and contributes at least \(\lceil z_B/p\rceil\) above its baseline positive label \(1\). If at least two vertices of \(A\) are capable defenders, then each loses at most one neighbor and therefore sees at least \(z_B-1\) zeros; together their excess above baseline is at least \(2\lceil(z_B-1)/p\rceil\). Counting every positive vertex of \(A\) once at baseline gives
\[
W_A\ge r-z_A+\phi_p(z_B).
\]
The same inequality is trivial when \(z_B=0\), because then \(\phi_p(z_B)=0\). By symmetry,
\[
W_B\ge s-z_B+\phi_p(z_A).
\]
Thus
\[
w(f)\ge H_r(z_A)+H_s(z_B),
\qquad
H_m(z)=m-z+\phi_p(z).
\]

We need one elementary estimate. If \(m\ge3\), \(p\ge3\), and \(0\le z\le m-1\), then
\[
H_m(z)\ge1+\left\lceil\frac{m-1}{p}\right\rceil.
\]
For \(z=0\) this is immediate. For \(z\ge1\), each of the two terms defining \(\phi_p(z)\) separately gives the bound. Indeed,
\[
m-z+\left\lceil\frac z p\right\rceil
\ge m-z+\frac z p
\ge 1+\frac{m-1}{p},
\]
and the left side is integral. Also
\[
m-z+2\left\lceil\frac{z-1}{p}\right\rceil
\ge m-z+\frac{2(z-1)}p
\ge 1+\frac{2(m-2)}p
\ge 1+\frac{m-1}{p},
\]
where the middle inequality uses that \(p\ge3\), so the displayed affine function is nonincreasing in \(z\), and the last inequality uses \(m\ge3\). Again integrality gives the required ceiling.

If neither shore is entirely zero, applying this estimate to both shores yields
\[
w(f)\ge2+\left\lceil\frac{r-1}{p}\right\rceil+
\left\lceil\frac{s-1}{p}\right\rceil.
\]
If, say, all of \(A\) is zero, feasibility forces \(z_B=0\). The bound above becomes
\[
w(f)\ge s+\phi_p(r)
\ge s+\left\lceil\frac{r-1}{p}\right\rceil.
\]
Since \(s\ge3\) and \(p\ge3\),
\[
\left\lceil\frac{s-1}{p}\right\rceil\le s-2,
\]
so the same target lower bound follows. The case in which all of \(B\) is zero is symmetric.

For the matching upper bound, if \(t=0\), choose any edge \(ab\) with \(a\in A\), \(b\in B\). If \(t>0\), choose the two endpoints \(a,b\) of one deleted matching edge. Put
\[
f(a)=1+\left\lceil\frac{s-1}{p}\right\rceil,
\qquad
f(b)=1+\left\lceil\frac{r-1}{p}\right\rceil,
\]
and label every other vertex \(0\). In the first case each defender sees every opposite-shore zero; in the second case the only missing cross-neighbor is the other positive defender. Hence each defender has exactly the required capacity for all opposite-shore zeros. The labels also lie in the permitted codomain: when \(t<r\), \(\Delta=s\), while for \(t=r\), \(\Delta=s-1\). This proves the formula.

## Verification
A standalone checker in `verify.py` independently evaluates the definition by exhaustive labeling for all graphs \(G_{3,3,t}\) and \(G_{3,4,t}\), every admissible \(t\), and \(p\in\{3,4,5\}\). It also checks the proof inequalities and the explicit construction on a wider deterministic parameter grid. The exhaustive computation is a finite stress test only; the theorem for arbitrary parameters is established by the proof above.

## Relationship to prior work
Valenzuela-Tripodoro, Mateos-Camacho, Cera López, Casablanca, and Álvarez-Ruiz introduced \(p\)-strong Roman domination and proved the complete-bipartite formula for \(K_{r,s}\) in the range \(3\le p\le\Delta-1\); their exact-value section treats complete bipartite graphs and bi-stars, and their future-work section explicitly calls for exact values on further graph families. The same full text contains no occurrence of “crown” or “matching.”

A later 2026 paper by Valenzuela-Tripodoro, Mateos-Camacho, Cera López, and Álvarez-Ruiz has primary MSC 05C78 and determines ordinary strong Roman domination, including crown graphs. That is the \(p=2\) model, not the \(p\)-strong model for \(p\ge3\). Neither that crown result nor the earlier complete-bipartite \(p\)-strong result implies the present matching-deletion theorem: deleting edges simultaneously removes possible defenders and reduces a defender’s zero-neighborhood load, so monotonicity in either direction is unavailable in general.

## Limitations
The theorem requires both shores to have at least three vertices and \(p\ge3\). The small-shore case \(r=2\) has a different complete-bipartite formula and is not claimed here. No claim is made about deleting a nonmatching set of edges: the proof uses essentially that each vertex loses at most one cross-edge. The literature search cannot exclude an unindexed equivalent result under alternate notation for \(p\)-strong Roman domination; this remains the principal originality risk.

## References
1. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera, R. M. Casablanca, and M. P. Álvarez-Ruiz, “p-Strong Roman Domination in Graphs,” WSEAS Transactions on Mathematics 23 (2024), 1005–1017, DOI 10.37394/23206.2024.23.104; arXiv:2501.10140.
2. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera López, and M. P. Álvarez-Ruiz, “Complexity and Exact Values for [k]-Roman and Strong Roman Domination for Specific Graph Families,” Mathematics 14 (2026), 1535, DOI 10.3390/math14091535.
