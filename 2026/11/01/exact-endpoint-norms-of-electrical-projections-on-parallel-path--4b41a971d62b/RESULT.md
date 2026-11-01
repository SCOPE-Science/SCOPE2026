# Exact endpoint norms of electrical projections on parallel-path networks

## Finding
Let \(G\) be a finite, unweighted, simple, undirected network made from \(r\ge2\) internally vertex-disjoint paths between the same two distinct terminals. The paths have positive integer edge lengths \(\ell_1,\ldots,\ell_r\). Simplicity means that at most one of these lengths is \(1\). Write \(N=\sum_i\ell_i\), and orient every path from the first terminal to the second. Let \(B:\mathbb R^{V(G)}\to\mathbb R^{E(G)}\) be the edge-gradient operator and \(P\) the orthogonal projection in the unweighted edge Hilbert space onto \(\operatorname{im}B\). Define \(G_*=\sum_{j=1}^r1/\ell_j\). Then the exact, attained endpoint norm is
\[
\boxed{\|P\|_{\ell^\infty(E)\to\ell^\infty(E)}=
\max_{1\le i\le r}\left(2-\frac2{\ell_i}+\frac{2+(r-2)\ell_i}{\ell_i^2G_*}\right).}
\]
In particular, every value is rational and an input with edge values in \(\{-1,1\}\) attains the norm.

For any fixed integer \(s\ge1\), let \(\mathcal T_s(N)\) be the collection of these networks having \(N\) edges and every path length at least \(s\). For all sufficiently large \(N\), this collection is nonempty. The **sharp minimum-path-length hierarchy** is
\[
\boxed{\lim_{N\to\infty}\frac{1}{\sqrt N}
\max_{G\in\mathcal T_s(N)}\|P_G\|_{\ell^\infty\to\ell^\infty}
=\frac1{2\sqrt s}.}
\]
Thus a direct terminal edge permits sharp normalized amplification \(1/2\), while excluding such an edge lowers the sharp coefficient to \(1/(2\sqrt2)\). For the explicit family consisting of one path of length \(s\) and \(q\) further paths of length \(sq\), the short-edge row has absolute sum exactly \(q/2+3/2-1/s\), with \(N=s(1+q^2)\). The norm is at least this value.

## Assumptions and scope
All vertex and edge sets are finite. Edges are unweighted, and the edge Hilbert inner product is \(\langle x,y\rangle=\sum_{e\in E}x_ey_e\). The endpoint norm is the *unweighted edge maximum norm*, not an electrical-energy-weighted endpoint norm. The edge orientation is arbitrary: reversing an edge changes the matrix by signed conjugation and leaves its induced endpoint norm unchanged. The network has two distinct terminals and internally disjoint paths; for a simple graph, no more than one path is a single edge. The maximum over \(\mathcal T_s(N)\) concerns the specified graph family, not all connected graphs on \(N\) edges.

## Proof
**Step 1 — gradient subspace and orthogonal minimization.** For any edge vector \(x\), write \(s_i(x)=\sum_{e\in\text{path }i}x_e\). An edge vector is a gradient if and only if all its path sums have the same value \(\delta\): necessity is telescoping between the terminals, and sufficiency follows by integrating along the internally disjoint paths to construct compatible vertex potentials. Thus the orthogonal projection \(z=Px\) uniquely minimizes \(\sum_e(z_e-x_e)^2\) subject to the common-path-sum constraints. Given a fixed \(\delta\), the least-squares correction is uniform within each path,
\[
z_e=x_e+\frac{\delta-s_i(x)}{\ell_i}
\quad(e\text{ in path }i).
\]
Minimizing \(\sum_i(\delta-s_i(x))^2/\ell_i\) yields
\[
\delta=\frac{\sum_i s_i(x)/\ell_i}{G_*}.
\]
This identifies the unique orthogonal projector without an appeal to a pseudoinverse formula.

**Step 2 — its rows.** Fix an edge \(e\) in path \(i\). The matrix coefficient in the column corresponding to edge \(f\) is
\[
P_{ef}=
\begin{cases}
1-1/\ell_i+1/(\ell_i^2G_*),&f=e,\\
-1/\ell_i+1/(\ell_i^2G_*),& f\ne e\text{ in path }i,\\
1/(\ell_i\ell_jG_*),&f\text{ in path }j\ne i.
\end{cases}
\]
Because \(r\ge2\), one has \(G_*>1/\ell_i\); hence the diagonal term is nonnegative, same-path off-diagonal terms are strictly negative when present, and other-path entries are strictly positive. The absolute row sum is therefore
\[
\begin{aligned}
\sum_f|P_{ef}|
&=1-\frac1{\ell_i}+\frac1{\ell_i^2G_*}
 +(\ell_i-1)\left(\frac1{\ell_i}-\frac1{\ell_i^2G_*}\right)
 +\sum_{j\ne i}\frac1{\ell_iG_*}\\
&=2-\frac2{\ell_i}+\frac{2+(r-2)\ell_i}{\ell_i^2G_*}.
\end{aligned}
\]
The induced \(\ell^\infty\) norm of any finite real matrix is its largest absolute row sum. Selecting the input \(x_f=\operatorname{sgn}(P_{ef})\), with either sign at zero entries, attains the sum for the maximizing row. This proves the exact norm statement and the asserted extremizer.

**Step 3 — uniform upper bound at fixed minimum path length.** Fix \(s\ge1\), a network in \(\mathcal T_s(N)\), and one row from a path of length \(t\ge s\). Put \(k=r-1\), \(M=N-t\), and \(S=\sum_{j\ne i}1/\ell_j\). Cauchy–Schwarz gives
\[
S\ge\frac{k^2}{M}.
\]
The row sum in Step 2 is
\[
2-\frac2t+\frac{k-1+2/t}{1+tS}
\le 2+\frac{k+1}{1+tk^2/M}.
\]
Using \(k/(1+ak^2)\le1/(2\sqrt a)\) for \(a>0\), together with \(1/(1+ak^2)\le1\), shows that every row sum is at most
\[
3+\frac12\sqrt{\frac{N-t}{t}}
\le3+\frac12\sqrt{\frac Ns}.
\]
Consequently the limit superior in the asserted hierarchy is at most \(1/(2\sqrt s)\).

**Step 4 — matching lower bound for every sufficiently large edge count.** For fixed \(s\), take one path of length \(s\) and set \(M=N-s\) and \(k=\lfloor\sqrt{M/s}\rfloor\). Distribute the remaining \(M\) edges among \(k\) paths whose lengths differ by at most one. For all sufficiently large \(N\), every such length is at least \(s\), and this is a simple graph even when \(s=1\) because the other paths then have lengths at least two. For the short-path row, \(S\), the sum of reciprocals of these \(k\) lengths, satisfies \(S\to1/s\), while \(k/\sqrt N\to1/\sqrt s\). The exact row formula gives
\[
\frac1{\sqrt N}\left(2-\frac2s+\frac{k-1+2/s}{1+sS}\right)
\longrightarrow\frac1{2\sqrt s}.
\]
This establishes the limit inferior over *all* sufficiently large integers \(N\), and hence the claimed limit. In the exactly commensurate family \((s,sq,\ldots,sq)\) with \(q\) long paths, one has \(G_*=2/s\) and the short row is \(q/2+3/2-1/s\), as stated.

## Verification
A standalone Python 3 program, `verify_theta.py`, uses exact rational arithmetic. It independently constructs the incidence matrix of each test network, removes one terminal column, inverts the reduced incidence Gram matrix, and compares the resulting orthogonal projection to the closed-form matrix in Step 2. It also checks the largest absolute row sum, symmetry, idempotence on small instances, and the explicit minimum-length hierarchy witnesses. Execute `python3 verify_theta.py` in the directory containing this document and the program. In the checked run it passed 21,580 exact-rational comparisons over 127 small network profiles and 344 scaling witnesses. Finite testing confirms representative formulas but does not establish the universal statements; those follow from Steps 1–4.

## Relationship to prior work
Kelner and Maymounkov, *Electric routing and concurrent flow cutting* (arXiv:0909.2859, publicly posted 15 September 2009), derive a general square-root edge-count upper bound for electrical routing and use a short edge accompanied by many long parallel paths to exhibit matching order of growth (Theorem 1.2 and Appendix A). That order-of-growth construction is **previously known** and is not claimed as a new example here. Schild, Rao, and Srivastava, *Localization of Electrical Flows* (arXiv:1708.01632, Section 1.1, Example 1.1), calculate the unit electrical flow length for a similarly balanced shortcut configuration and identify the relationship between the transfer-current column norm and electrical routing congestion. Those observations supply context and the natural invariant; they do not give the all-profile formula above or the sharp upper constant for the family with an arbitrary fixed minimum path length.

Gurel-Gurevich, Nachmias, and Sachdeva, *A Tight Bound on Localization of Electrical Flows* (arXiv:2605.24130, Theorems 1.1–1.3), prove average-edge and absolute-matrix spectral bounds. Their averages are distinct from the worst-edge maximum evaluated here. The claimed contribution is the **profile-by-profile exact maximum norm and complete sharp hierarchy** inside the parallel-path family, not the electrical-projection representation or the existence of square-root growth.

## Limitations
No claim is made about weighted conductances, overlapping internal vertices, arbitrary series-parallel networks, or all connected graphs. For general graphs, the normalization \(1/(2\sqrt s)\) does not apply because there is no specified common-terminal path decomposition. The independent verification code tests finite examples only. Related prior work already supplies the square-root growth order and the shortcut lower-bound construction; an unknown equivalent exact profile theorem in the broader transfer-current literature remains a residual originality risk. Independent external scientific validation has not been performed.

## References
1. Jonathan Kelner and Petar Maymounkov, *Electric routing and concurrent flow cutting*, arXiv:0909.2859v1 (15 September 2009), especially Theorem 1.2 and Appendix A. https://arxiv.org/abs/0909.2859
2. Aaron Schild, Satish Rao, and Nikhil Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632v1 (4 August 2017), especially Example 1.1 and Section 1.3. https://arxiv.org/abs/1708.01632
3. Ori Gurel-Gurevich, Asaf Nachmias, and Sushant Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130v1 (22 May 2026), especially Theorems 1.1–1.3. https://arxiv.org/abs/2605.24130
