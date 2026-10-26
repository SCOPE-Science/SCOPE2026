# Exact strict edge anticorrelation for uniform forests of \(K_{3,n}\)

## Finding
For every integer \(n\ge 2\), choose uniformly among all acyclic edge subsets of the complete bipartite graph \(K_{3,n}\), including disconnected forests and isolated vertices. Write \(X_e\) for the indicator of a specified edge. Set
\[
z_n=3n^2+13n+16,\qquad a_n=3n^2+23n+38.
\]
Every edge has marginal inclusion probability \(p_n=a_n/(4z_n)\). For two distinct edges there are exactly three cases, and their covariances are:

* **One common right-side endpoint:**
  \[\operatorname{Cov}(X_e,X_f)=-\frac{(n-1)(9n^3+51n^2+104n+92)}{16z_n^2}.\]
* **One common left-side endpoint, with different right endpoints:**
  \[\operatorname{Cov}(X_e,X_f)=-\frac{41n^2+181n+194}{8z_n^2}.\]
* **Four distinct endpoints:**
  \[\operatorname{Cov}(X_e,X_f)=-\frac{17n^2+77n+66}{8z_n^2}.\]

All three are strictly negative for every admissible \(n\). The first covariance tends to \(-1/16\), whereas multiplying the second and third by \(n^2\) gives the respective limits \(-41/72\) and \(-17/72\). Thus the uniform-forest edge-negative-correlation inequality holds for the entire infinite graph family \(K_{3,n}\). For \(n\ge3\), these graphs contain \(K_{3,3}\) and are non-series-parallel.

## Assumptions and scope
The left bipartition has exactly three individually distinguishable vertices \(u_1,u_2,u_3\); the right bipartition has \(n\) vertices. There are \(3n\) possible edges. A spanning forest means an acyclic spanning subgraph, not necessarily connected; vertices with degree zero are retained. Every such forest receives equal probability. No variable edge weights or assertions about arbitrary graphs are involved. The three edge-pair categories are exhaustive because two distinct edges can meet on the left, meet on the right, or be disjoint.

## Proof
Process the right vertices in any fixed order. The current forest induces a partition of the three left vertices into connected components. Denote its state by \(s=0,1,2\), according as the number of terminal components is three, two, or one. A new right vertex may be joined to a set of left vertices **if and only if** that set contains no two vertices already in the same current component. Indeed, two such joins create a cycle; when every selected left vertex belongs to a different component, each added edge joins distinct components and no cycle appears.

For any state there are four nonmerging choices: the empty neighborhood and the three singleton neighborhoods. From state \(0\), three neighborhoods of size two lead to state \(1\), and the unique neighborhood of size three leads to state \(2\). From state \(1\), exactly two neighborhoods of size two lead to state \(2\). There are no other allowed transitions. Let \(Z_s(m)\) count valid completions by \(m\) as-yet-unprocessed right vertices when the left-side state is \(s\). By placing zero, one, or two strictly increasing merging transitions among the \(m\) columns,
\[
\begin{aligned}
Z_0(m)&=4^m+4m4^{m-1}+6\binom m2 4^{m-2},\\
Z_1(m)&=4^m+2m4^{m-1},\\
Z_2(m)&=4^m.
\end{aligned}
\]
The formulas also apply at \(m=0\) by the obvious empty-product interpretation of the displayed transition count. In particular the total number of forests is
\[
Z=Z_0(n)=4^{n-2}z_n.
\]

Fix an edge \(e=(u_1,v_1)\). Among the four subsets of neighbors of \(v_1\) that contain \(u_1\), one leaves state \(0\), two produce state \(1\), and one produces state \(2\). Process \(v_1\) first, to obtain the number of forests containing \(e\):
\[
A=Z_0(n-1)+2Z_1(n-1)+Z_2(n-1)=4^{n-3}a_n.
\]
For \(f=(u_2,v_1)\), sharing the right endpoint with \(e\), the marked column can have neighborhood \(\{u_1,u_2\}\) or \(\{u_1,u_2,u_3\}\). Hence
\[
B_R=Z_1(n-1)+Z_2(n-1)=4^{n-2}(2n+6).
\]
For distinct right vertices \(v_1,v_2\), process these two columns before the other \(n-2\) columns. Each marked column must contain its prescribed left endpoint. A cycle among these two columns occurs exactly when their chosen left-neighborhoods intersect in at least two vertices. Enumerating the at most sixteen ordered neighborhood pairs yields the following counts by final state:

| Marked edges | State \(0\) | State \(1\) | State \(2\) |
| --- | ---: | ---: | ---: |
| \((u_1,v_1),(u_1,v_2)\) | 1 | 4 | 4 |
| \((u_1,v_1),(u_2,v_2)\) | 1 | 4 | 5 |

Therefore their full completion counts are respectively
\[
\begin{aligned}
B_L&=Z_0(n-2)+4Z_1(n-2)+4Z_2(n-2)
 =4^{n-4}(3n^2+33n+66),\\
B_D&=Z_0(n-2)+4Z_1(n-2)+5Z_2(n-2)
 =4^{n-4}(3n^2+33n+82).
\end{aligned}
\]
For any pair type \(H\in\{R,L,D\}\), its joint inclusion probability is \(B_H/Z\), so
\[
\operatorname{Cov}(X_e,X_f)=\frac{ZB_H-A^2}{Z^2}.
\]
Substituting the four exact counts and cancelling powers of four gives the three claimed rational expressions. Explicitly, with \(r_n=2n+6\), \(\ell_n=3n^2+33n+66\), and \(d_n=3n^2+33n+82\), the required polynomial identities are
\[
\begin{aligned}
16z_nr_n-a_n^2&=-(n-1)(9n^3+51n^2+104n+92),\\
z_n\ell_n-a_n^2&=-2(41n^2+181n+194),\\
z_nd_n-a_n^2&=-2(17n^2+77n+66).
\end{aligned}
\]
All coefficients inside the three negative factors are positive for \(n\ge2\). The asymptotic statements follow by comparing leading polynomial coefficients, completing the proof.

## Verification
The standalone standard-library script `verify.py` enumerates every subset of the \(3n\) labeled edges for \(2\le n\le6\), tests acyclicity independently by union-find, and compares the five exact forest counts (total, one marked edge, and each of the three marked-pair types). It also checks the polynomial identities by integer coefficient arithmetic and the claimed rational covariance formulas for all integers \(2\le n\le2000\). Run `python3 verify.py`; the expected terminal marker is `VERIFICATION_OK`. The finite enumeration is corroboration, not the proof for arbitrary \(n\).

## Relationship to prior work
Grimmett and Winkler formulated edge-negative-correlation for uniform spanning forests as a general conjecture and verified all sufficiently small graphs computationally [1]. Semple and Welsh [2] proved a weighted form for graphs generated through series-parallel extensions of blocks from \(K_4\) and its minors. Erickson [3] proved a sum-of-squares theorem for series-parallel graphs. The graphs \(K_{3,n}\) for \(n\ge3\) are 3-connected non-series-parallel graphs, so those named graph-class theorems do not yield their edge correlations. More recent work [4] states that a general inequality remains unresolved, and proves other parameter ranges without giving the present uniform \(K_{3,n}\) orbit formulas. This result concerns the unweighted case only and does not claim a multivariate Rayleigh inequality or full negative association.

## Limitations
The theorem does not establish negative dependence for all increasing edge events, positive edge weights, arbitrary complete bipartite graphs \(K_{a,b}\), or arbitrary graph minors. The enumeration agrees with the all-size proof but cannot certify publication priority. Existing general results not identified in the cited literature may cover some of the present consequences. No independent mathematical audit has been performed.

## References
[1] G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185 (first submission 2003-02-17); Random Structures & Algorithms 24 (2004), 444–460.

[2] C. Semple and D. Welsh, *Negative correlation in graphs and matroids*, University of Canterbury report UCDMS2005/12 (November 2005); Combinatorics, Probability and Computing 17 (2008), 423–435. Open text: https://ir.canterbury.ac.nz/bitstreams/1cf68e98-580e-4f92-8ab6-371751ffd382/download

[3] A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, arXiv:1008.3660 (2010); Australasian Journal of Combinatorics 52 (2012), 75–87.

[4] R. Altar Çiçeksiz and M. Ravichandran, *Negative Correlations for Forests and the \(q<1\) Random Cluster Model*, arXiv:2610.00549 (2026).
