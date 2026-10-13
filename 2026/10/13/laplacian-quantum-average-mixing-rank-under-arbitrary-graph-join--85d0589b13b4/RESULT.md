# Laplacian quantum average-mixing rank under arbitrary graph joins
## Finding
For every pair of nonempty finite simple undirected graphs \(X,Y\), the continuous-time Laplacian average-mixing matrix of their unweighted join has a universal block decomposition, with exact rank determined by the *reduced* average-mixing ranks of the factors. In particular, for **connected** \(X,Y\), each of order at least two,
\[
\operatorname{rank}\widehat M_L(X\vee Y)=\operatorname{rank}\widehat M_L(X)+\operatorname{rank}\widehat M_L(Y)+\mathbf1_{X\cong K_2}+\mathbf1_{Y\cong K_2}.
\]
Thus joining connected graphs of order at least three preserves the sum of their Laplacian average-mixing ranks (equivalently, adds their nullities), despite arbitrary coincidences among factor eigenvalues. The two-vertex complete graph is the **only** nontrivial connected factor that creates an extra rank-one correction.

The formula also holds for disconnected factors after replacing the usual rank by the reduced rank defined below. This yields one theorem for *all* nonempty finite simple graphs, including isolated vertices:
\[
\boxed{\operatorname{rank}\widehat M_L(X\vee Y)=\rho(X)+\rho(Y)+\mathbf1_{\min(|X|,|Y|)=1}+\mathbf1_{X\cong K_2}+\mathbf1_{Y\cong K_2}.}
\]
Here \(\rho(G)\) is defined via the spectral projectors orthogonal to the constant vector, not via an arbitrary choice of eigenbasis. For example, \(\widehat M_L(K_2)\) has rank one, but \(K_2\vee K_2=K_4\) has full average-mixing rank four; \(\overline{K_2}\vee\overline{K_2}=C_4\) has rank two; and \(P_3\vee P_3\) has rank four on six vertices.

## Assumptions and scope
All graphs are finite, simple, undirected, unweighted, and nonempty. Graphs need not be connected. Let \(L_G=D_G-A_G\) be the ordinary combinatorial Laplacian and
\[
\widehat M_L(G)=\lim_{T\to\infty}\frac1T\int_0^T e^{itL_G}\circ e^{-itL_G}\,dt=\sum_\lambda E_\lambda(G)\circ E_\lambda(G),
\]
where \(E_\lambda(G)\) are the distinct-eigenvalue orthogonal spectral projectors and \(\circ\) denotes entrywise multiplication. The limit always exists. Write \(n=|X|\), \(m=|Y|\), \(N=n+m\). For a graph \(G\) of order \(s\), set \(j_s=\mathbf1_s\), \(J_s=j_sj_s^{\mathsf T}\) and
\[
F_\lambda(G)=E_\lambda(G)-\mathbf1_{\lambda=0}J_s/s,
\quad Q_G=\sum_\lambda F_\lambda(G)\circ F_\lambda(G),\qquad \rho(G)=\operatorname{rank}Q_G.
\]
The subtraction removes only the distinguished constant direction, even when \(G\) is disconnected. For \(s=1\), \(Q_G=0\). For every connected \(G\) of order \(s\ge2\), \(\rho(G)=\operatorname{rank}\widehat M_L(G)\); this equality is **not** asserted for all disconnected factors. Define \(F_s(G)=0\) if \(s\) is absent from the Laplacian spectrum.

## Proof
**1. Exact decomposition.** The join Laplacian is
\[
L_{X\vee Y}=\begin{pmatrix}L_X+mI_n&-J_{n,m}\\-J_{m,n}&L_Y+nI_m\end{pmatrix}.
\]
The constant projector is \(P_0=J_N/N\). The other projector on vectors constant on each factor is \(P_N=zz^{\mathsf T}\), where
\[
z=(m\mathbf1_n,-n\mathbf1_m)/\sqrt{nmN}.
\]
The remaining eigenvectors lie in the mean-zero factor subspaces, where the eigenvalues of \(L_X\) and \(L_Y\) are shifted by \(m\) and \(n\), respectively. Any collision between a shifted \(X\)-eigenvalue and a shifted \(Y\)-eigenvalue combines *disjointly supported* projectors, whose entrywise product vanishes. A collision with the eigenvalue \(N\) occurs precisely when an internal factor Laplacian has eigenvalue equal to its own order. Put
\[
p=\big(\underbrace{m/(nN),\ldots,m/(nN)}_{n},\underbrace{n/(mN),\ldots,n/(mN)}_{m}\big)^{\mathsf T},
\quad B_X=Q_X+\frac{2m}{nN}F_n(X),\quad B_Y=Q_Y+\frac{2n}{mN}F_m(Y).
\]
Using \(P_0\circ P_0=J_N/N^2\), \(P_N\circ P_N=pp^{\mathsf T}\), and \(F_n(X)\circ P_N|_X=mF_n(X)/(nN)\), one obtains **without a nonresonance assumption**
\[
\boxed{\widehat M_L(X\vee Y)=\operatorname{diag}(B_X,B_Y)+\frac{J_N}{N^2}+pp^{\mathsf T}.}\tag{1}
\]
All summands are positive semidefinite, since the Schur square of each orthogonal projector is positive semidefinite and both additional correction terms involve positive multiples of orthogonal projectors.

**2. The top-frequency correction can increase factor rank only for \(K_2\).** For each factor of order \(s\ge2\), projector row norms give
\[
Q_G\mathbf1_s=\left(1-\frac1s\right)\mathbf1_s,
\]
while \(F_s(G)\mathbf1_s=0\). We show that \(\ker Q_G\subseteq\ker F_s(G)\) whenever \(s\ge3\). The identity
\[
L_G=sI_s-J_s-L_{\overline G}
\]
reduces the assertion to the connected components \(C_1,\ldots,C_r\) of the complement, with sizes \(s_i\). Let \(W\) be the space of vectors constant on each \(C_i\), and let \(P_W=\sum_iJ_{C_i}/s_i\). Then \(F_s(G)=P_W-J_s/s\) when \(r\ge2\) (and is zero when \(r=1\)). All other reduced spectral projectors are block-supported in individual \(C_i\)'s, so if \(R=Q_G-F_s(G)\circ F_s(G)\), then \(R\) leaves \(W\) invariant and, on \(w=\sum_i c_i\mathbf1_{C_i}\),
\[
\langle w,Rw\rangle=\sum_i(s_i-1)c_i^2.
\]
If this vanishes, \(c_i=0\) on each component of size at least two. On the remaining singleton components, the principal matrix of \(F_s(G)\circ F_s(G)\) is
\[
\left(1-\frac2s\right)I+\frac1{s^2}J,
\]
which is positive definite for \(s\ge3\). Thus \(Q_G\) is strictly positive on \(W\), and \(\ker Q_G\perp W\supseteq\operatorname{im}F_s(G)\). Because both summands are positive semidefinite, adding a positive multiple of \(F_s(G)\) leaves the rank of \(Q_G\) unchanged. For \(s=2\), \(F_s(G)\ne0\) precisely for \(G\cong K_2\). In that case \(Q_G=J_2/4\), \(F_2(G)=\frac12\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\), and every positive correction raises rank from one to two. Therefore
\[
\operatorname{rank}B_G=\rho(G)+\mathbf1_{G\cong K_2}.
\tag{2}
\]

**3. Add the factor ranks.** For \(s\ge2\), \(Q_G\mathbf1_s=(1-1/s)\mathbf1_s\) and \(F_s(G)\mathbf1_s=0\), hence \(\mathbf1_s\in\operatorname{im}B_G\). If \(n,m\ge2\), both vectors in the rank-two correction \(J_N/N^2+pp^{\mathsf T}\) lie in \(\operatorname{im}\operatorname{diag}(B_X,B_Y)\); the correction cannot alter rank. If exactly one factor is a singleton, its \(B\)-block vanishes, and \(J_N/N^2\) supplies exactly one new direction, while the other factor already contains its constant direction. If both factors are singletons, the join is \(K_2\) and the mixing matrix is \(J_2/2\) of rank one. In every case, (1) and (2) yield the boxed rank formula. Finally, for connected \(G\) of order at least two, \(\widehat M_L(G)=Q_G+J_s/s^2\), and its two summands already have the same positive constant-vector direction; their kernels, and hence their ranks, coincide. This proves the connected-factor formula.

## Verification
The standalone exact-arithmetic checker `verify_laplacian_join.py` constructs exact rational spectral projectors from the actual Laplacian matrices of ten basic graphs (orders one through four), verifies their idempotency and completeness, and checks (1) and the rank theorem for all 100 ordered graph pairs, totaling 3,800 exact matrix entries. The observed output is `VERIFY_OK exact_pairs=100 exact_entries=3800 singular_cases=52 K4_rank=4 C4_join_O3_rank=5`. The checker uses SymPy, no floating-point tolerances, and is included as a standalone file. These examples test singleton factors, disconnected factors, cross-factor resonance, top-frequency resonance, and ordinary nonresonance, but the unrestricted result is proved analytically above.

## Relationship to prior work
The general Cesàro-projector identity is classical in quantum average-mixing work and is explicitly available in Coutinho--Godsil--Guo--Zhan (2018). Coutinho--Baptista--Godsil--Spier--Werner (2022, primary MSC 81P68, first public 2022-08-18) supply exact quantum-walk averaging methods, not the rank law for Laplacian joins. Kirkland--Monterde (2023) provide exact Laplacian join transition-amplitude formulas and analyze periodicity, cospectrality and state transfer; those formulas supply a route to the block spectral decomposition, but the searched full text does not state (1), the complement-component positivity lemma, or the general rank-additivity/exceptions theorem. Lo--Rajaram--Schepens--Sullivan--Tamon--Ward (2005) discuss adjacency-based *circulant* joins and approximate average uniformity, not this Laplacian rank invariant. The present proof is a new deduction from established spectral machinery, rather than an assertion that all constituent tools are new.

## Limitations
The proof has not undergone independent mathematical validation. The theorem is limited to ordinary combinatorial Laplacians, unweighted simple finite graphs and uniform-in-time Cesàro averages; it does not assert the same rank formula for adjacency Hamiltonians, weighted joins or other sampling measures. The exact block formula depends on the factors' spectral projectors, so it does not by itself furnish a numerical rank in terms of vertex counts alone for an arbitrary pair. Prior-work coverage could exist in a more general association-scheme or spectral-commutant theorem not located in the searches; the general projector and Laplacian join-evolution formulas substantially reduce the amount of new derivation, and independent literature review is appropriate.

## References
1. Coutinho, G., Godsil, C., Guo, K., Zhan, H. *A New Perspective on the Average Mixing Matrix*. Electronic Journal of Combinatorics 25(4), P4.14 (2018). arXiv:1709.03591, https://arxiv.org/pdf/1709.03591.
2. Coutinho, G., Baptista, P. F., Godsil, C., Spier, T. J., Werner, R. *Irrational quantum walks*. arXiv:2208.08971v1 (first public 2022-08-18), https://arxiv.org/pdf/2208.08971.
3. Kirkland, S., Monterde, H. *Quantum walks on join graphs*. arXiv:2312.06906v1 (first public 2023-12-12), https://arxiv.org/pdf/2312.06906.
4. Lo, P., Rajaram, S., Schepens, D., Sullivan, D., Tamon, C., Ward, J. *Mixing of Quantum Walk on Circulant Bunkbeds*. arXiv:quant-ph/0509059v1 (2005), https://arxiv.org/pdf/quant-ph/0509059.
