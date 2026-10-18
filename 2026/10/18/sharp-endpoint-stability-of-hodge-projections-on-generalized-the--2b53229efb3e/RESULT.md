# Sharp endpoint stability of Hodge projections on generalized theta networks

## Finding
Let \(r\ge2\), and let \(G\) be a finite simple graph formed by \(r\) internally vertex-disjoint paths between the same two poles, with positive integral edge lengths \(\ell_1,\ldots,\ell_r\). At most one length is \(1\). Orient every path from the first pole to the second. Equip real edge flows with counting-measure \(\ell^2(E)\), and let \(P\) be its orthogonal projection onto the space of vertex gradients, while \(Q=I-P\) projects onto divergence-free flows. Define
\[
s=\min_j\ell_j,\qquad S=\sum_{j=1}^r\frac1{\ell_j}.
\]
Then their **sharp bounded-data endpoint norms** are exactly
\[
\boxed{\|P\|_{\ell^\infty(E)\to\ell^\infty(E)}
=2-\frac2s+\frac{(r-2)s+2}{s^2 S},\qquad
\|Q\|_{\ell^\infty(E)\to\ell^\infty(E)}
=1+\frac{r-2}{sS}.}
\]
Both maxima are attained by a suitable sign pattern of input flows. For \(r\ge3\), a shortest branch always contains an output edge realizing either norm; for \(r=2\), the norms simplify to \(2-2/(\ell_1+\ell_2)\) and \(1\), with every output edge equivalent.

In particular, for every fixed \(r\ge3\) and fixed integer \(s\ge2\), taking lengths \(s,M,\ldots,M\) and sending \(M\to\infty\) gives
\[
\boxed{\|P\|\longrightarrow r,\qquad\|Q\|\longrightarrow r-1.}
\]
These are strict, optimal upper bounds on all finite simple generalized-theta graphs with \(r\) branches. In contrast, for equal lengths \(\ell_j=m\ge2\),
\[
\boxed{\|P\|=3-\frac2r-\frac{2(r-1)}{rm},\qquad
\|Q\|=2-\frac2r.}
\]
For the elementary high-contrast family with lengths \(2,M,\ldots,M\), both constants simplify further to
\[
\boxed{\|P\|=1+\frac{r-1}{1+2(r-1)/M},\qquad
\|Q\|=1+\frac{r-2}{1+2(r-1)/M}.}
\]
In particular, in a joint limit \(r,M\to\infty\) with \(M/r\to\tau\in[0,\infty]\), one has \(\|P\|/r\to\tau/(\tau+2)\), interpreting the value at \(\tau=\infty\) as \(1\). Thus even a family of simple graphs with only two vertices of high degree can exhibit order-\(r\) bounded-error amplification under a Hilbert-orthogonal projection, despite its \(\ell^2\)-norm being exactly \(1\).

## Assumptions and scope
The path length is its number of edges. Distinct paths share only their poles, and no other edges exist. The requirement of a *simple* graph forbids two length-one branches. All edges have unit least-squares weight; no vertex weighting or probabilistic normalization is used. Reversing an edge orientation changes basis signs and leaves both stated induced norms invariant. The \(\ell^\infty\) norm is the maximum absolute edge value, not the norm of recovered vertex potentials. The result is a sharp **fixed-graph** operator norm, and does not optimize over alternate projections onto the same range.

Writing \(D\) for the edge-by-vertex signed incidence matrix, \(P=D(D^TD)^\dagger D^T\). The kernel of \(D^T\) is the circulation space, so \(Q\) is the orthogonal projection onto that kernel. The matrices are symmetric and idempotent in \(\ell^2\) but need not be contractions in \(\ell^\infty\). The finite operator norm equals the largest absolute row sum.

## Proof
**1. Reduce the circulation projection to branch means.** Number the edges of branch \(i\) consecutively, and for an arbitrary edge vector \(x\) set
\[
\bar x_i=\frac1{\ell_i}\sum_{e\in E_i}x_e.
\]
At every internal degree-two vertex a divergence-free vector must have equal consecutive oriented edge values. Thus it has a constant value \(c_i\) along branch \(i\). Kirchhoff balance at the first pole is \(\sum_i c_i=0\), and this also ensures balance at the other pole. Conversely, every such choice is a circulation. Orthogonal projection therefore minimizes
\[
\sum_{i=1}^r\ell_i(c_i-\bar x_i)^2
\quad\text{subject to}\quad\sum_i c_i=0.
\]
Lagrange multipliers give uniquely
\[
\boxed{(Qx)_e=\bar x_i-\frac1{\ell_i S}\sum_{k=1}^r\bar x_k,
\qquad e\in E_i.}
\]
This formula also follows directly from the Hodge orthogonality \(\operatorname{im}D=\ker(D^T)^\perp\), without any choice of gauge for vertex potentials.

**2. Compute every exact absolute row sum.** For a fixed output edge in branch \(i\), every coefficient of its \(Q\)-row on the same branch equals
\[
\frac1{\ell_i}-\frac1{\ell_i^2 S}\ge0,
\]
while every coefficient on branch \(k\ne i\) equals \(-1/(\ell_i\ell_kS)\). Their absolute sum is
\[
B_i=1+\frac{r-2}{\ell_i S}.
\]
Since \(r\ge2\), this is greatest for a shortest branch. Replacing \(Q\) by \(P=I-Q\), the diagonal coefficient is positive, the other same-branch coefficients are nonpositive, and all cross-branch coefficients are positive: explicitly they are
\[
1-\frac1{\ell_i}+\frac1{\ell_i^2S},\qquad
-\frac1{\ell_i}+\frac1{\ell_i^2S},\qquad
\frac1{\ell_i\ell_k S}.
\]
The exact absolute sum becomes
\[
A_i=2-\frac2{\ell_i}
+\frac{(r-2)\ell_i+2}{\ell_i^2 S}.
\]
Every absolute row sum is attained by setting each input coordinate to the sign of its coefficient. No relaxation is used.

**3. Identify the maximizing branch for a simple graph.** For fixed \(S\) write \(u_i=1/\ell_i\). The expression \(A_i\) is the value at \(u_i\) of the strictly convex quadratic
\[
F(u)=2-2u+\frac{r-2}{S}u+\frac2S u^2.
\]
Thus the maximum among all branches must occur at one of the two extreme lengths. Choose a shortest branch \(s\) and a longest branch \(L\), and put \(u=1/s\), \(v=1/L\). Direct factorization gives
\[
F(u)-F(v)=\frac{u-v}{S}
\left[(r-2)-2\sum_{k\text{ on the other }r-2\text{ branches}}\frac1{\ell_k}\right].
\]
If \(r\ge3\), every branch strictly between the chosen extreme branches has length at least \(2\): a simple graph permits at most one length-one branch, which must be a chosen shortest branch. The bracket is nonnegative, so **a shortest branch always maximizes**. When the shortest and longest lengths differ, a longest branch ties precisely if each of the other \(r-2\) branch lengths equals \(2\); strict convexity excludes any intermediate reciprocal length from maximization. If all lengths agree, all branches are equivalent. When \(r=2\), the bracket is zero; direct substitution yields \(A_i=2-2/(\ell_1+\ell_2)\) on either branch. Substituting \(s\) in \(A_i,B_i\) proves both boxed formulas.

**4. Sharp global bounds and the balanced comparison.** Since \(r\ge2\), \(S>1/s\). Therefore
\[
A_s<2-\frac2s+\frac{(r-2)s+2}{s}=r.
\]
For \(r\ge3\), also \(B_s<1+(r-2)=r-1\); when \(r=2\), \(B_s=1\) exactly. For lengths \((s,M,\ldots,M)\) with \(s\) fixed and \(M\) tending to infinity, \(S=1/s+(r-1)/M\to1/s\), and direct substitution gives \(A_s\to r\), \(B_s\to r-1\). Taking \(s=2\) makes every graph simple. For all lengths equal to \(m\ge2\), substitute \(S=r/m\) into the exact formulas to obtain the asserted equal-arm values. This proves both the strict universal bounds and their optimality.

## Verification
The included standalone `verify_theta.py` reconstructs the incidence matrix of each tested graph independently, forms the exact anchored normal-equation orthogonal projector, and checks the absolute row sums against the formulas. It passes 64 exact symbolic rational graph instances, 150 further numerical instances, 1,064 equal-arm rational identities, and 84 asymptotic-bound consistency checks. It also tests sign-pattern attainment, idempotence, and the extreme-branch difference identity. Execute with `python verify_theta.py` (requires NumPy and SymPy). These finite checks are corroboration; Steps 1–4 above prove the statements for **every** permitted integer length and branch count.

## Relationship to prior work
Jiang, Lim, Yao, and Ye introduce the \(\ell^2\)-optimal HodgeRank gradient-flow projection and its divergence-free residual on comparison graphs. Kassel and Wu give the associated transfer-current/Green-kernel formula and investigate its stochastic-geometric scaling. These general descriptions provide the projection framework, but their stated theorems do not evaluate the sharp \(\ell^\infty\) amplification, identify the shortest-branch worst row on every simple generalized-theta graph, or determine the optimal \(r\)-branch growth.

A published cactus-graph coordinate-projection formula concerns projections in Lipschitz-free transportation spaces, not the Hilbert-orthogonal edge projector here; a generalized-theta graph with at least three paths is typically not a cactus. Published theta-graph algebraic-gnarledness formulas concern cointegral homology bases and their \(\ell^1\)-norms, not the operator in this theorem. A published minimum-enclosing-ball result concerns directed edge-root polytopes on the **same path-network class**, but determines a geometric radius rather than an edge-flow Hodge-projection norm. The known transfer-current identity is used openly as background; the sharp row-sum classification and high-contrast law are the added conclusions.

## Limitations
Only unweighted finite *simple* generalized-theta graphs are covered. The formulas should not be applied unchanged to multiple direct parallel edges, weighted least squares, arbitrary series-parallel networks, or vertex-potential errors. The universal \(r\)-bounds are suprema over graph sizes, not attained by a finite graph when \(r\ge3\). The general transfer-current representation predates this work; an equivalent earlier specialized \(\ell^\infty\)-norm computation might exist under electrical-flow or inverse-incidence terminology and remains a priority risk. No independent audit has been performed.

## References
1. X. Jiang, L.-H. Lim, Y. Yao, Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067 (first version 2008-11-07); *Mathematical Programming* 127 (2011), 203–244, especially the HodgeRank orthogonal decomposition and projection discussion.
2. A. Kassel, W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946 (first version 2013-12-10), particularly Section 2 and the transfer-current/orthogonal-projection identity.
3. *Sharp coordinate-projection norms for edge bases of cactus transportation spaces*, publicly archived mathematical finding, 2026, identifier `b98930fbc1cd`.
4. *Exact algebraic gnarledness of three-path theta graphs*, publicly archived mathematical finding, 2026, identifier `cceb12dd2a0d`.
5. *Parallel-path screening and the exact minimum sphere of directed edge polytopes*, publicly archived mathematical finding, 2026, identifier `fb9309fc855d`.
