# Sharp endpoint projection constants and norm asymmetry for rectangular rook graphs

## Finding
Let \(3\le m<n\) be integers, and let \(G=K_m\square K_n\) be the unweighted rook graph on \(V=[m]\times[n]\). Give its edge space \(\mathbb R^E\) the usual real \(\ell_p\)-norm, and define the cycle space \(Z=\ker D\) and cut space \(B=\operatorname{ran}D^{\mathsf T}\), where \(D\) is an oriented vertex-edge incidence matrix. Write \(\lambda_p(Y)=\inf\{\|T\|_{\ell_p^E\to\ell_p^E}:T^2=T,\ \operatorname{ran}T=Y\}\).

Define, for \(0\le t\le1\),
\[
\begin{aligned}
C_A(t)&=\frac{2(m-1+(n-1)t)}m,&
C_B(t)&=\frac{2(n-1+(m-1)(1-t))}n,\\
R_A(t)&=\frac{2(m-1)}m+\frac{2(n-1)(1-t)}n,&
R_B(t)&=\frac{2(n-1)}n+\frac{2(m-1)t}m,\\
d_A(t)&=\frac{2(1+(n-1)t)}{mn},&
d_B(t)&=\frac{2(1+(m-1)(1-t))}{mn}.
\end{aligned}
\]
The four parameters are
\[
\begin{aligned}
t_{B,1}&=\frac{m^2-2m+n}{m^2-m+n^2-n},&
t_{B,\infty}&=\frac{n(m-1)}{2mn-m-n},\\
t_{Z,1}&=\frac{(m-1)(n+2)}{2mn+m+n-4},&
t_{Z,\infty}&=\frac{m^2-4m+n+2}{m^2-3m+n^2-3n+4}.
\end{aligned}
\]
All lie strictly between zero and one. The exact minimum projection norms are
\[
\boxed{\begin{aligned}
\lambda_1(B)&=C_A(t_{B,1}),&\lambda_\infty(B)&=R_A(t_{B,\infty}),\\
\lambda_1(Z)&=1+R_A(t_{Z,1})-2d_A(t_{Z,1}),&
\lambda_\infty(Z)&=1+C_A(t_{Z,\infty})-2d_A(t_{Z,\infty}).
\end{aligned}}
\]
Every minimum is attained by an explicit equivariant projection below, and is globally optimal among **all** real linear projections, not just equivariant ones. A distinctive effect of unequal axis sizes is strict endpoint asymmetry:
\[
\lambda_\infty(B)-\lambda_1(B)=
\frac{2(m-1)(n-1)(m-n)^2(mn-m-n)}{mn(2mn-m-n)(m^2-m+n^2-n)}>0,
\]
\[
\lambda_1(Z)-\lambda_\infty(Z)=
\frac{2(m-1)(n-1)(m-n)^2(mn-m-n-2)}{mn(2mn+m+n-4)(m^2-3m+n^2-3n+4)}>0.
\]
For example, when \((m,n)=(3,4)\), the four constants \((\lambda_1(B),\lambda_\infty(B),\lambda_1(Z),\lambda_\infty(Z))\) are \((19/9,217/102,43/18,19/8)\).

## Assumptions and scope
The graph has one edge between distinct vertices exactly when they share a row or a column. Its edge count is \(n\binom m2+m\binom n2\). Fix arbitrary orientations; changing orientations conjugates every relevant projection by a diagonal sign isometry, so the constants do not depend on these choices. Everything is finite-dimensional and over the real scalars. The restriction \(3\le m<n\) separates the genuinely rectangular case from the equal-axis Hamming case and the two-row prism case.

## Proof
**1. Symmetrization and classification.** The subgroup \(S_m\times S_n\) acts by signed edge-coordinate permutations, preserving both \(B\) and \(Z\) and acting isometrically on every \(\ell_p^E\). Averaging any projection onto either invariant subspace over this group yields an equivariant projection with no larger norm. Thus minimizing among equivariant projections is sufficient.

For each \(A\)-edge \(e=((i,j),(k,j))\) (the first coordinate changes), assign the mean-zero vertex potential
\[
\phi_e(a,b)=(\mathbf1_{a=i}-\mathbf1_{a=k})
\left(\frac{t}{m}\mathbf1_{b=j}+\frac{1-t}{mn}\right).
\]
For each \(B\)-edge \(e=((i,j),(i,k))\) (the second coordinate changes), assign
\[
\phi_e(a,b)=(\mathbf1_{b=j}-\mathbf1_{b=k})
\left(\frac{1-t}{n}\mathbf1_{a=i}+\frac{t}{mn}\right).
\]
Use the incidence convention \(De_e=\delta_{\mathrm{tail}(e)}-\delta_{\mathrm{head}(e)}\), so \((D^{\mathsf T}\phi)_e=\phi(\mathrm{tail}(e))-\phi(\mathrm{head}(e))\). Define \(P_t e=D^{\mathsf T}\phi_e\) and extend linearly. The action on vertex potentials decomposes into constants and the three tensor subspaces \(U_m\otimes\mathbf1\), \(\mathbf1\otimes U_n\), and \(U_m\otimes U_n\), where \(U_r=\{u:\sum_i u_i=0\}\). Directly summing complete-graph edge differences shows that \(P_t\) fixes all cut vectors: on these three nonconstant components the coefficients are respectively \(1,1,t+(1-t)=1\). Hence \(P_t^2=P_t\) and \(\operatorname{ran}P_t=B\).

Conversely, let \(P\) be an equivariant projection onto \(B\). Its column potentials, uniquely normalized by zero mean, are forced by permutations swapping an edge's two endpoints and fixing the other coordinate to have the forms \((\delta_i-\delta_k)\otimes(a\delta_j+b\mathbf1)\) and \((c\delta_i+d\mathbf1)\otimes(\delta_j-\delta_k)\). The identity \(P|_B=I|_B\), evaluated on the three nonconstant tensor components, imposes
\[
m(a+nb)=1,\qquad n(c+md)=1,\qquad ma+nc=1.
\]
Solving gives \(a=t/m\), \(b=(1-t)/(mn)\), \(c=(1-t)/n\), and \(d=t/(mn)\). Thus every equivariant cut projection equals \(P_t\) for exactly one real \(t\). Moreover, the map \(P\mapsto I-P^{\mathsf T}\) bijects cut projections with cycle projections: it produces \(Q_t=I-P_t^{\mathsf T}\), which satisfies \(Q_t^2=Q_t\) and \(\operatorname{ran}Q_t=\ker D=Z\). Conversely the adjoint of any cycle projection has kernel \(Z^\perp=B\), so this accounts for every equivariant cycle projection.

**2. Exact operator norms.** In the interval \(0\le t\le1\), the absolute column sums of \(P_t\) on the two edge orbits are exactly \(C_A(t),C_B(t)\), and its absolute row sums are exactly \(R_A(t),R_B(t)\). For an \(A\)-edge the sum of absolute complete-graph edge differences of \(\delta_i-\delta_k\) is \(2(m-1)\); the cross-axis part contributes \(2(n-1)t/m\) to its column and \(2(n-1)(1-t)/n\) to its row. Interchanging axes yields the remaining formulas. Its two diagonal coefficients are \(d_A(t),d_B(t)\), both strictly smaller than one. Since \(Q_t=I-P_t^{\mathsf T}\), its column sums are \(1+R_A(t)-2d_A(t)\), \(1+R_B(t)-2d_B(t)\), and its row sums are \(1+C_A(t)-2d_A(t)\), \(1+C_B(t)-2d_B(t)\). The operator norms are the maxima over the respective two edge orbits.

**3. Global one-variable optimization.** For \(P_t\), the full absolute-sum formulas outside \([0,1]\) come from replacing each displayed signed coefficient by its absolute value. Clipping \(t\) to the nearest endpoint zero or one never increases either orbit's column sum or either orbit's row sum: the pure-axis absolute sum is minimized when its two coefficient groups have the same sign, while each cross-axis contribution is a positive multiple of \(|t|\) or \(|1-t|\). Hence each cut minimum lies in \([0,1]\). The two cut column branches are respectively increasing and decreasing, while the row branches are respectively decreasing and increasing; they cross once in the interior.

For cycle projections each orbit sum is convex in \(t\) on all of \(\mathbb R\), since it is a sum of absolute values of affine matrix entries. On \([0,1]\), the cycle column \(A\)-branch has slope \(-2(m+2)(n-1)/(mn)\) and the cycle column \(B\)-branch has slope \(2(m-1)(n+2)/(mn)\); at zero the \(A\)-branch is larger, and at one the \(B\)-branch is larger. Convexity implies that neither exterior half-line improves on the appropriate endpoint. Likewise the cycle row branches have slopes \(2(n-1)(n-2)/(mn)\) and \(-2(m-1)(m-2)/(mn)\); the \(B\)-branch dominates at zero and the \(A\)-branch at one, again excluding exterior minimizers. Each maximum is therefore minimized at the unique intersection of its two affine branches. Solving the four intersection equations yields exactly the four displayed parameters and constants. Elementary factorization gives both strictly positive endpoint differences; positivity follows from \(m,n\ge3\) and \(m\ne n\). Averaging proves the resulting minima are global.

## Verification
The independent standard-library script `verify.py` constructs the matrices from their vertex-potential definition with rational arithmetic. It checks projection idempotence, zero cycle divergence, every edge-orbit row and column norm formula, and all four balancing parameter identities on several unequal and equal-axis finite examples. Running `python verify.py` succeeded with 28,641 exact-rational assertions. These finite computations check implementation and boundary examples; the proof above establishes the result for every stated \(m,n\).

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (first public preprint 2023-05-21; arXiv:2305.12582), Section 2.6, treat uniform-alphabet Hamming graphs and prove uniqueness of their automorphism-invariant cycle projections. Their setting includes the square \(K_q\square K_q\), but its factor-interchange symmetry is absent for \(m<n\). The present unequal-axis case instead has a full nontrivial one-parameter equivariant projection family, and its four optimizing parameters are distinct from the Euclidean-orthogonal parameter \(m/(m+n)\). The earlier results neither state nor yield these four unequal-axis exact norms directly. The 2018 paper by the same authors treats general averaging and recursive diamond/Laakso graph families without supplying these rook-graph constants. Yan et al., *Cycle Invariant Positional Encoding for Graph Representation Learning* (arXiv:2311.14333), use orthogonal Hodge-cycle projectors including a square rook example for graph representation learning, not minimum Banach projection norms. The substantive new feature here is the strict distinction between the \(\ell_1\) and \(\ell_\infty\) endpoint invariants for both cut and cycle spaces.

## Limitations
The new theorem is limited to unequal axes of size at least three, real scalars, and the two endpoint norms. No exact norm is claimed for intermediate \(1<p<\infty\), and no uniqueness is claimed among all nonsymmetric minimizing projections. It does not assert that these formulas were previously conjectured. An unindexed equivalent source remains a bibliographic possibility, and no independent scientific review has been completed.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first public version 21 May 2023, especially Sections 2.1 and 2.6. https://arxiv.org/abs/2305.12582
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814, 10 July 2018, especially Sections 1 and 4–5. https://arxiv.org/abs/1807.03814
3. Z. Yan et al., *Cycle Invariant Positional Encoding for Graph Representation Learning*, arXiv:2311.14333, 2023, especially Section 4.2 and the rook/Shrikhande example. https://arxiv.org/abs/2311.14333
