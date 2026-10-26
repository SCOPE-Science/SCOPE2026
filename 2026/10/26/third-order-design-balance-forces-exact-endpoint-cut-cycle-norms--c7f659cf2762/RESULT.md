# Third-order design balance forces exact endpoint cut–cycle norms

## Finding

Let \((V,\mathcal B)\) be any finite simple \(3\)-\((v,k,\tau)\) block design, with integers \(4\le k\le v-2\) and \(\tau\ge1\). Here \(|V|=v\), every block has cardinality \(k\), and every three distinct points belong to exactly \(\tau\) blocks. Write
\[
\lambda=\frac{\tau(v-2)}{k-2},\qquad r=\frac{\lambda(v-1)}{k-1}
\]
for the number of blocks through a pair and a single point, respectively. Form the unweighted bipartite incidence graph \(G\) whose vertices are the points and the blocks, with one edge \((i,S)\) precisely when \(i\in S\).

Orient edges from points to blocks, with the chosen signed vertex-edge incidence convention having \(+1\) at the point and \(-1\) at the block, and let \(Q\) be the real Euclidean-orthogonal projection from \(\mathbb R^{E(G)}\) onto the edge cut space. Let \(P=I-Q\) be the complementary orthogonal projection onto the cycle space. Then, on both real endpoint spaces \(\ell_1(E(G))\) and \(\ell_\infty(E(G))\), their exact operator norms are
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=1+
\frac{2(k-1)}{k\lambda v}
\bigl[\lambda(2v-k)-k-(v-k)\tau\bigr],}
\]
\[
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}
=\|Q\|_{1\to1}+\frac{k-2}{k}-\frac{2(k-1)}{\lambda v}.}
\]
Every edge column realizes each corresponding \(\ell_1\) norm. **No edge-transitivity hypothesis is needed**: the two answers depend only on design parameters, even for a design with a nontransitive automorphism group.

Equivalently, using \(\tau/\lambda=(k-2)/(v-2)\), define
\[
H(v,k)=1+\frac{2(k-1)}{kv}
\left[2v-k-\frac{(v-k)(k-2)}{v-2}\right].
\]
The norms obey the particularly simple inverse-pair-incidence laws
\[
\|Q\|=H(v,k)-\frac{2(k-1)}{v\lambda},\qquad
\|P\|=H(v,k)+\frac{k-2}{k}-\frac{4(k-1)}{v\lambda}.
\]
These are exact expressions, not bounds or numerical estimates.

## Assumptions and scope

The design is a set of distinct \(k\)-subsets of \(V\). All incidence edges have unit weight. The real cut space means \(\operatorname{im}D^\top\) for a signed edge-incidence matrix \(D\), and the real cycle space is \(\ker D\). The operators are the **canonical Euclidean-orthogonal** projections; no minimum over arbitrary nonorthogonal projections is asserted. The graph is connected because every pair of points lies in a common block and every block contains points.

The design identities follow by double counting blocks containing a fixed pair and a fixed point:
\[
\lambda(k-2)=\tau(v-2),\qquad r(k-1)=\lambda(v-1).
\]
The hypotheses imply \(\lambda\ge1\), \(v>k\), and \(1/(\lambda v)<1/k\), including at the allowed parameter endpoints.

## Proof

**1. Solve the incidence-graph Laplacian.** Let \(A\) be the unsigned point-versus-block incidence matrix. Every point occurs in \(r\) blocks, every block has \(k\) points, and the two-design identities imply
\[
AA^\top=(r-\lambda)I+\lambda J.
\]
The graph Laplacian in point/block order is
\[
L=\begin{pmatrix}rI&-A\\-A^\top&kI\end{pmatrix}.
\]
Fix an arbitrary incidence edge \(e=(i,S)\). Feed one unit of current from point \(i\) to block \(S\). If \(x\) and \(y\) denote point and block potentials, respectively, the equations are
\[
r x-Ay=\mathbf1_i,\qquad -A^\top x+ky=-\mathbf1_S.
\]
The block equation gives \(y=(A^\top x-\mathbf1_S)/k\); substituting produces
\[
\left(rI-\frac1k AA^\top\right)x
=\mathbf1_i-\frac1k\mathbf1_S^{(V)}.
\]
The right side has point-coordinate sum zero. On the mean-zero subspace the coefficient on the left is \(\bigl((k-1)r+\lambda\bigr)/k=\lambda v/k\). Taking the mean-zero gauge yields the exact point potentials
\[
\gamma=\frac1{\lambda v},\qquad
x_j=\begin{cases}
(k-1)\gamma,&j=i,\\
-\gamma,&j\in S\setminus\{i\},\\
0,&j\notin S.
\end{cases}
\]
Consequently
\[
y_T=\frac1k\left(\sum_{j\in T}x_j-\mathbf1_{T=S}\right),
\qquad Q_{(j,T),e}=x_j-y_T\quad(j\in T).
\]
The latter equality is exactly \(Q=D^\top L^+D\), which is a symmetric Euclidean-orthogonal projection and is independent of potential gauge.

**2. Take absolute values without approximation.** On the distinguished block \(S\), the edge currents are
\[
Q_{(i,S),e}=\frac1k+(k-1)\gamma,
\qquad Q_{(j,S),e}=\frac1k-\gamma\quad(j\in S\setminus\{i\}).
\]
All are strictly positive because \(\lambda v>k\), and their absolute values sum to one.

For any other block \(T\), write \(b_T=|T\cap(S\setminus\{i\})|\). If \(i\in T\), the current leaving point \(i\) is positive and every other current on that block is nonpositive; its total absolute current is
\[
\frac{2\gamma}{k}\bigl((k-1)^2+b_T\bigr).
\]
If \(i\notin T\), currents on \(S\setminus\{i\}\) are nonpositive and those outside \(S\) are nonnegative, giving total absolute current
\[
\frac{2\gamma}{k}\,b_T(k-b_T).
\]
The expressions include zero-current boundary cases. No hidden sign assumption is used.

**3. Count the signed regions using precisely three-design balance.** There are \(r-1\) blocks other than \(S\) containing \(i\), and
\[
\sum_{T\ni i,\ T\ne S} b_T=(k-1)(\lambda-1).
\]
For blocks not containing \(i\), count ordered pairs \((j,\ell)\) with \(j\in S\setminus\{i\}\), \(\ell\notin S\), both in \(T\). Every such pair belongs to \(\lambda\) blocks, of which exactly \(\tau\) also contain \(i\). Therefore
\[
\sum_{T\not\ni i}b_T(k-b_T)=(k-1)(v-k)(\lambda-\tau).
\]
Summing the absolute currents gives
\[
\begin{aligned}
\sum_{f\in E(G)}|Q_{f,e}|
&=1+\frac{2\gamma}{k}\Big[(r-1)(k-1)^2
 +(k-1)(\lambda-1)\\
&\hspace{56pt} +(k-1)(v-k)(\lambda-\tau)\Big]\\
&=1+\frac{2(k-1)}{k\lambda v}
\bigl[\lambda(2v-k)-k-(v-k)\tau\bigr].
\end{aligned}
\]
This does not depend on the chosen incidence edge. Taking the maximum column sum proves the \(\ell_1\) formula for \(Q\).

**4. The complementary projection.** Outside the distinguished block, the column of \(P=I-Q\) is the negative of the corresponding column of \(Q\). On \(S\), only the chosen edge receives the added diagonal unit. Since \(0<Q_{e,e}<1\), the total absolute contribution on that block becomes
\[
1-Q_{e,e}+\sum_{j\in S\setminus\{i\}}Q_{(j,S),e}
=\frac{2(k-1)}{k}-2(k-1)\gamma.
\]
Subtract the original contribution one and add the new contribution to obtain the displayed \(\ell_1\) formula for \(P\). Both projections are symmetric, so their \(\ell_\infty\) operator norms equal their \(\ell_1\) norms. Every incidence-edge column has these sums, proving all assertions.

## Verification

A standalone standard-library exact-rational checker is included as `verification_checker.py`. It enumerates all triples to check the design axioms, builds every edge-current column, checks Kirchhoff divergences at every point and block, and compares both absolute column sums against the formulas. For two smaller instances it separately solves the **full grounded graph Laplacian** using exact rational Gauss–Jordan elimination, rather than relying on the incidence Schur complement.

The completed checks covered five designs, including complete block designs and binary affine Steiner quadruple systems: **1,096 complete exact-current columns**, of which **116 were independently reconstructed by grounded Laplacian inversion**. The exact results included:
\[
\begin{array}{c|c|c}
\text{design}&\|Q\|&\|P\|\\\hline
\text{complete }(v,k)=(8,4)&59/20&17/5\\
\text{affine }3\text{-}(8,4,1)&11/4&3\\
\text{affine }3\text{-}(16,4,1)&191/56&27/7
\end{array}
\]
The two eight-point designs have the same point and block sizes but different replication parameters, demonstrating the nontrivial inverse-incidence dependence. Finite checks corroborate the all-parameter proof, not vice versa.

For a Steiner quadruple system \(3\)-\((v,4,1)\) (whenever such a system exists), the formulas specialize to
\[
\|Q\|=1+\frac{3(v-1)(v-4)}{v(v-2)},\qquad
\|P\|=\|Q\|+\frac12-\frac{12}{v(v-2)}.
\]
They approach \(4\) and \(9/2\), respectively, along the family of affine systems on \(2^m\) points for integers \(m\ge3\).

## Relationship to prior work

The problem is motivated by the study of cut/cycle projections and transportation-cost spaces, in particular Dilworth–Kutzarova–Ostrovskii (2018, 2023). Their inspected graph-family calculations concern diamond or Laakso graphs, discrete tori, and Hamming graphs, not the incidence graphs of arbitrary three-designs. The orthogonal cut-projection matrix is also the electrical transfer-current matrix studied by Schild–Rao–Srivastava (2017) and Gurel-Gurevich–Nachmias–Sachdeva (2026). Those papers obtain universal localization bounds, not exact per-column constants expressed in three-design parameters.

The incidence matrix spectrum alone does not immediately give these endpoint norms: absolute-value signs and the third-order block-overlap counts are decisive. The result is for canonical orthogonal projections, not for minimum-norm projections within all algebraic complements. Unsearched older or less-indexed incidence-network calculations might contain equivalent formulas.

## Limitations

Only finite simple block designs of strength at least three, with unit incidence edges and \(4\le k\le v-2\), are covered. The formulas do not automatically extend to arbitrary two-designs, weighted incidence edges, minimum norms of nonorthogonal projections, other \(\ell_p\) exponents, or arbitrary hypergraphs. A strength-three design need not be edge-transitive; its endpoint norm nevertheless depends only on the standard design parameters. No classification of which feasible parameter sets actually have simple designs is asserted.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (first public 2023-05-21), especially Sections 1.1 and 2.4–2.7.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz-free spaces on finite metric spaces*, arXiv:1807.03814v1 (first public 2018-07-10).
3. A. Schild, S. Rao, N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632v1 (first public 2017-08-04), especially Theorems 1.4–1.5.
4. O. Gurel-Gurevich, A. Nachmias, S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130v1 (first public 2026-05-22), especially Theorems 1.1–1.3.
