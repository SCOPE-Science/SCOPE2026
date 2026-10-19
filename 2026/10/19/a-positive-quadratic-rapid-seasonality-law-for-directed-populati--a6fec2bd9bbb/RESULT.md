# A positive quadratic rapid-seasonality law for directed population networks

## Finding

Let a finite strongly connected population network have a fixed, possibly directed migration generator and bounded periodic local growth rates. The population's principal Floquet exponent has an **explicit, nonnegative quadratic correction** to the rapidly oscillating environmental average. Precisely, under the assumptions below, as the physical environmental period \(T\downarrow0\),

\[
\Lambda(T)=\lambda_0+\mathcal C T^2+O(T^3),\qquad
\mathcal C=\frac12\sum_{i\ne j}q_iL_{ij}p_j\int_0^1\bigl(H_i(s)-H_j(s)\bigr)^2\,ds.
\]

The coefficient \(\mathcal C\) is strictly positive unless **all locations share exactly the same centered seasonal fluctuation**, in which case \(\Lambda(T)=\lambda_0\) for every \(T>0\). Therefore, whenever the fluctuations differ between patches, \(\Lambda(T)\) is strictly increasing for all sufficiently small positive periods. No migration reversibility or symmetry, equal seasonal durations, or restriction to two environmental states is required.

This is a local-in-period assertion. It does not assert monotonicity at arbitrary environmental periods; known directed-network examples can be nonmonotone away from the rapid-switching limit.

## Assumptions and scope

Fix an integer \(n\ge2\). Let \(L\in\mathbb R^{n\times n}\) have nonnegative off-diagonal entries, zero column sums, and a strongly connected directed graph with an edge \(j\to i\) when \(L_{ij}>0\). We do not assume \(L=L^{\mathsf T}\), detailed balance, or a particular normalization of its positive edge weights. Let each \(r_i:\mathbb R\to\mathbb R\) be bounded, piecewise continuous and one-periodic. Define

\[
\bar r_i=\int_0^1r_i(s)\,ds,\qquad
A_0=L+\operatorname{diag}(\bar r_1,\ldots,\bar r_n).
\]

Its spectral abscissa \(\lambda_0\) is a simple real eigenvalue. Choose positive left and right eigenvectors \(q,p\gg0\), normalized by \(q^{\mathsf T}p=1\), so \(A_0p=\lambda_0p\) and \(q^{\mathsf T}A_0=\lambda_0q^{\mathsf T}\). For each patch define the unique absolutely continuous, one-periodic, zero-mean primitive \(H_i\) by

\[
H_i'(s)=r_i(s)-\bar r_i\quad\text{for a.e. }s,\qquad
\int_0^1H_i(s)\,ds=0.
\]

For every \(T>0\), consider the cooperative population system

\[
\dot x(t)=\left[L+\operatorname{diag}\bigl(r_1(t/T),\ldots,r_n(t/T)\bigr)\right]x(t).
\]

Let \(\Phi_T(T)\) denote its positive monodromy matrix over a physical period \(T\) and let \(\Lambda(T)=T^{-1}\log\rho(\Phi_T(T))\). The asymptotic constant in \(O(T^3)\) is for the fixed network and fixed bounded seasonal profile as \(T\to0^+\); it is not asserted uniformly over unbounded families of profiles or matrices.

## Proof

**Analytic Floquet expansion.** Set \(s=t/T\), \(D(s)=\operatorname{diag}(r_i(s)-\bar r_i)\), and \(Q=A_0-\lambda_0I\). In seasonal time the equation reads \(x'=T(A_0+D(s))x\). Its monodromy has an entire convergent expansion in \(T\), and \((\Phi_T(T)-I)/T\to A_0\). The simple Perron eigenvalue of \(A_0\), and the associated positive monodromy eigenvector, therefore admit analytic continuations at \(T=0\). This yields a one-periodic positive Floquet profile \(y(s,T)\), analytic in \(T\), satisfying

\[
\partial_sy=T\bigl(Q+D(s)-(\Lambda(T)-\lambda_0)I\bigr)y,
\qquad \int_0^1q^{\mathsf T}y(s,T)\,ds=1.
\]

Expand \(y=p+Ty_1+T^2y_2+\cdots\) and \(\Lambda=\lambda_0+T\lambda_1+T^2\lambda_2+\cdots\). Let \(H(s)=\operatorname{diag}(H_i(s))\) and let \(K(s)\) be a zero-mean, one-periodic diagonal primitive of \(H\), i.e. \(K'=H\).

**First order and vanishing linear drift.** At order \(T\), \(y_1'=D p\), hence \(y_1=Hp+c\), with constant vector \(c\). The order-\(T^2\) periodic solvability condition, using \(\int_0^1H=\int_0^1D=0\) and \(\int_0^1 D H\,ds=\frac12[H^2]_0^1=0\), gives

\[
0=Qc-\lambda_1p.
\]

Multiplication by \(q^{\mathsf T}\) yields \(\lambda_1=0\), so \(Qc=0\). Because \(\ker Q=\operatorname{span}\{p\}\) and the profile normalization gives \(q^{\mathsf T}c=0\), necessarily \(c=0\). Thus \(y_1=Hp\): there is **no linear correction in physical period**, regardless of directed migration.

**Second order and exact coefficient.** The equation at the next order is

\[
y_2'=QHp+DHp,
\qquad y_2=QKp+\tfrac12H^2p+c_2
\]

for some constant vector \(c_2\). At order \(T^3\), average the profile equation against \(q^{\mathsf T}\). Since \(q^{\mathsf T}Q=0\), \(\int D=0\), and \(\int D_iH_i^2=\tfrac13[H_i^3]_0^1=0\), this gives

\[
\lambda_2=\int_0^1q^{\mathsf T}D(s)QK(s)p\,ds
=-\sum_{i,j}q_iQ_{ij}p_j\int_0^1H_i(s)H_j(s)\,ds.
\]

The last equality follows from integration by parts \(\int H_i'K_j=-\int H_iH_j\) using periodic endpoints.

Set \(W_{ij}=q_iQ_{ij}p_j\). Both \(\sum_jW_{ij}=q_i(Qp)_i=0\) and \(\sum_iW_{ij}=(q^{\mathsf T}Q)_jp_j=0\). Consequently, at each \(s\),

\[
-\sum_{i,j}W_{ij}H_iH_j
=\frac12\sum_{i\ne j}W_{ij}(H_i-H_j)^2
=\frac12\sum_{i\ne j}q_iL_{ij}p_j(H_i-H_j)^2.
\]

This establishes the displayed quadratic coefficient. Every term is nonnegative. If the coefficient is zero, then \(H_i=H_j\) almost everywhere along each directed positive migration edge; continuity and strong connectivity force \(H_1=\cdots=H_n\) throughout the period. Conversely common \(H_i\)'s make the coefficient zero.

**Strictness and the equality case.** Analyticity implies \(\Lambda'(T)=2\mathcal CT+O(T^2)\), hence \(\Lambda'(T)>0\) for sufficiently small \(T>0\) whenever \(\mathcal C>0\). When all centered fluctuations are the same, write \(r_i(s)=\bar r_i+g(s)\) with \(\int_0^1g=0\). The instantaneous matrix is \(A_0+g(s)I\), so the scalar temporal factor commutes with \(A_0\), and \(\Phi_T(T)=e^{TA_0}\) exactly. Thus \(\Lambda(T)=\lambda_0\) for every positive period. This completes the strict dichotomy.

## Verification

A nonreversible three-site cycle makes the coefficient exact. Set

\[
L=\begin{pmatrix}-1&0&1\\1&-1&0\\0&1&-1\end{pmatrix},
\qquad
r(s)=\begin{cases}(2,-1,-1),&0\le s<1/3,\\(-1,2,-1),&1/3\le s<2/3,\\(-1,-1,2),&2/3\le s<1.\end{cases}
\]

All averaged patch growth rates vanish; \(\lambda_0=0\), \(p=(1/3,1/3,1/3)^{\mathsf T}\), \(q=(1,1,1)^{\mathsf T}\). Exact rational integration of the centered primitives yields

\[
\left(\int_0^1H_i(s)H_j(s)\,ds\right)_{i,j}
=\begin{pmatrix}
1/27&-1/54&-1/54\\-1/54&1/27&-1/54\\-1/54&-1/54&1/27
\end{pmatrix}.
\]

Each of the three directed positive edges contributes \(1/54\), hence

\[
\boxed{\Lambda(T)=\tfrac1{18}T^2+O(T^3).}
\]

The standalone program `verify.py` checks all displayed exact rational identities and independently assembles the actual season-by-season monodromy. It also checks the energy identity and the rapid-period expansion on a nonsymmetric, six-directed-edge network with four unequal seasons, plus the exactly flat common-forcing case. It passed 36 assertions when executed with Python 3, NumPy, SciPy and SymPy. Numerical checks illustrate rather than prove the theorem; the analytic argument above covers every finite strongly connected network and bounded piecewise-continuous seasonal profile.

## Relationship to prior work

Benaïm, Lobry, Sari and Strickler [1], Sections 3.2–3.7 and Appendix S1, identify the rapid-period averaged eigenvalue, prove general growth comparisons and pose a conjecture of global period monotonicity for fixed migration. Their arguments do not give the explicit all-profile directed quadratic coefficient or the strict **local** period derivative. Later work [2], Section 3.2, Proposition 1, does derive a second-order fast-period term for **two** environmental states with general matrices; therefore the special two-state reduction is not asserted as a new expansion in isolation. Its Section 4.2, Proposition 6, proves the disappearance of the first-order coefficient for fixed migration and any number of environmental states but does not state the strictly positive second-order formula for arbitrary multi-season or piecewise-continuous profiles. That paper also demonstrates global nonmonotonicity without migration symmetry, so global period monotonicity is not claimed here.

Katriel [3] and Liu, Lou and Song [4] obtain broader monotonicity results for symmetric migration. Those results cannot imply a general directed-edge positivity law without an additional nonsymmetric argument. The present edge-weighted coefficient is compatible with their symmetric special cases. A related theory of time-periodic cooperative nonlocal dispersal systems [5] includes frequency-monotonicity results in a different operator setting; full theorem hypotheses were not accessible during this comparison, and equivalence under particular discretizations remains a publication-priority risk.

## Limitations

This result concerns deterministic linear population growth and a **constant** irreducible migration generator. It does not extend by assertion to a time-dependent migration matrix, nonlinear density dependence, stochastic switching, disconnected networks, or uniform estimates over varying network families. It yields an asymptotic local period theorem, not global period monotonicity. Although the mathematics is analytically proved, equivalent consequences of more general spectral theorems not inspected in full text remain a priority risk.

## References

[1] M. Benaïm, C. Lobry, T. Sari and E. Strickler, *When can a population spreading across sink habitats persist?*, arXiv:2311.04706, first posted 2023-11-08, https://arxiv.org/abs/2311.04706.

[2] P. Monmarché, S. J. Schreiber and E. Strickler, *Impacts of Tempo and Mode of Environmental Fluctuations on Population Growth*, arXiv:2408.11179, first posted 2024-08-20, https://arxiv.org/abs/2408.11179.

[3] G. Katriel, *Dispersal-induced growth in a time-periodic environment*, arXiv:2104.01589, https://arxiv.org/abs/2104.01589.

[4] S. Liu, Y. Lou and P. Song, *A New Monotonicity for Principal Eigenvalues with Applications to Time-Periodic Patch Models*, SIAM J. Appl. Math. 82 (2022), 576–601, https://doi.org/10.1137/20M1320973.

[5] Y.-X. Feng, W.-T. Li, S. Ruan and M.-Z. Xin, *Principal Spectral Theory of Time-Periodic Nonlocal Dispersal Cooperative Systems and Applications*, SIAM J. Math. Anal. 56 (2024), 4040–4083, https://doi.org/10.1137/22M1543902.
