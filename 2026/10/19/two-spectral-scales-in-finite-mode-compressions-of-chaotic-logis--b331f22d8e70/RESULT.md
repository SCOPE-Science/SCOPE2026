# Two spectral scales in finite-mode compressions of chaotic logistic iterates

## Finding

Let \(f(x)=4x(1-x)\) on \([0,1]\), let \(f^{\circ n}\) denote its \(n\)-fold iterate, and put \(m=2^n\), \(n\ge1\). For \(g\in C^4([0,1])\), define the centered observable integral
\[
\Delta_n(g)=\int_0^1 g(x)\bigl(f^{\circ n}(x)-\tfrac12\bigr)\,dx.
\]
Then
\[
\Delta_n(g)=\frac{g(0)+g(1)}{4m^2}
+\frac{g(0)+g(1)+\tfrac32(g'(1)-g'(0))}{4m^4}
+o_g(m^{-4}). \tag{1}
\]
For \(g\in C^6\), the remainder in (1) is \(O_g(m^{-6})\). More generally, every prescribed finite asymptotic order is an explicit linear functional of endpoint derivatives of \(g\) (formula (4) below).

For an integer cutoff \(d\ge1\), write \(L_j(x)=\sqrt{2j+1}\,P_j(2x-1)\), \(0\le j\le d\), where \(P_j\) is the usual Legendre polynomial. Let \(H_{n,d}\) be the real symmetric \((d+1)\)-square matrix
\[
(H_{n,d})_{ij}=\int_0^1L_i(x)L_j(x)\bigl(f^{\circ n}(x)-\tfrac12\bigr)\,dx.
\]
Set \(u_j=(-1)^j\sqrt{2j+1}\), \(v_j=\sqrt{2j+1}\). In any finite-dimensional matrix norm,
\[
 m^2 H_{n,d}\longrightarrow \tfrac14(uu^{\mathsf T}+vv^{\mathsf T}). \tag{2}
\]
This limiting matrix has **exact rank two**. Its positive eigenvalues are \(S_e/2\) and \(S_o/2\), where
\[
S_e=\sum_{\substack{0\le j\le d\\j\text{ even}}}(2j+1),\qquad
S_o=\sum_{\substack{0\le j\le d\\j\text{ odd}}}(2j+1).
\]
Consequently two eigenvalues of \(H_{n,d}\) are positive and have asymptotics \(S_e/(2m^2)\) and \(S_o/(2m^2)\), as a multiset. Every mixed-parity matrix entry vanishes identically for all \(n\ge1\).

There is a second, strictly separated spectral scale. For \(d\ge2\), define the polynomial space \(\mathcal P_d\) with the \(L^2([0,1])\) inner product, its endpoint-null subspace
\[
K_d=\{p\in\mathcal P_d:p(0)=p(1)=0\},
\]
and the derivative evaluation \(J_d:K_d\to\mathbb R^2\), \(J_dp=(p'(0),p'(1))\). Apart from the two eigenvalues of order \(m^{-2}\), the \(d-1\) remaining eigenvalues, multiplied by \(m^6\), converge **as a multiset** to the eigenvalues of
\[
\boxed{\ \tfrac{21}{16}J_d^{*}J_d\ \text{ on }K_d.\ } \tag{3}
\]
Thus exactly \(\min(2,d-1)\) secondary eigenvalues are positive and of order \(64^{-n}\); all other eigenvalues are \(o(64^{-n})\). For \(d=2\), the sole secondary eigenvalue has the explicit sharp asymptotic \(\frac{315}{4}64^{-n}\). No claim is made when the cutoff grows with \(n\).

## Assumptions and scope

The map is the scalar \(r=4\) logistic map, the integration measure is Lebesgue measure on \([0,1]\), and the matrices are **finite compressions of multiplication operators**; they are not iterates of a separately projected nonlinear matrix recursion. The cutoff \(d\) is any fixed positive integer. The boundary expansions apply to all real or complex \(C^4\) test functions; eigenvalue statements concern the real polynomial basis and real symmetric compression. The displayed eigenvalue limits are taken as \(n\to\infty\) with \(d\) fixed. We use the standard Lagrange inner product and its induced adjoint on \(K_d\).

## Proof

**1. Exact conjugacy and endpoint expansion.** Put \(x(\theta)=(1-\cos\theta)/2\), \(0\le\theta\le\pi\). Elementary trigonometry gives \(f^{\circ n}(x(\theta))=(1-\cos(m\theta))/2\), and \(dx=(\sin\theta/2)\,d\theta\). With \(a(\theta)=g(x(\theta))\sin\theta\),
\[
\Delta_n(g)=-\frac14\int_0^\pi a(\theta)\cos(m\theta)\,d\theta.
\]
For every positive integer \(r\) and \(g\in C^{2r}([0,1])\), repeated ordinary integration by parts, using \(m=2^n\) even, gives
\[
\Delta_n(g)=\frac14\sum_{k=1}^r
\frac{(-1)^k\bigl(a^{(2k-1)}(\pi)-a^{(2k-1)}(0)\bigr)}{m^{2k}}
+o_g(m^{-2r}). \tag{4}
\]
The remainder is an \(m^{-2r}\) multiple of a Fourier cosine coefficient of \(a^{(2r)}\), which tends to zero by the Riemann–Lebesgue lemma. Two more continuous derivatives make the remainder \(O_g(m^{-2r-2})\). The coefficient of each \(m^{-2k}\) depends only on derivatives of \(g\) of order at most \(k-1\) at \(0,1\), because \(x(\theta)=O(\theta^2)\) near zero and \(1-x(\theta)=O((\pi-\theta)^2)\) near \(\pi\).

Direct endpoint differentiation gives
\[
a'(0)=g(0),\quad a'(\pi)=-g(1),\quad
a'''(0)=\tfrac32g'(0)-g(0),\quad
a'''(\pi)=\tfrac32g'(1)+g(1).
\]
Substitution into (4), with \(r=2\), proves (1). Reflection symmetry \(f^{\circ n}(1-x)=f^{\circ n}(x)\) also gives exact cancellation whenever \(g(1-x)=-g(x)\).

**2. Rank-two limit.** For any pair of basis polynomials \(L_i,L_j\), formula (1) gives
\[
(H_{n,d})_{ij}=\frac{L_i(0)L_j(0)+L_i(1)L_j(1)}{4m^2}+O_{i,j}(m^{-4}).
\]
Since \(L_j(0)=(-1)^j\sqrt{2j+1}\) and \(L_j(1)=\sqrt{2j+1}\), this proves (2). Even and odd coordinate subspaces are orthogonal; on each parity subspace the limiting matrix is respectively half the rank-one outer product of \((\sqrt{2j+1})\). Hence the two nonzero eigenvalues are \(S_e/2,S_o/2\). Exact mixed-parity cancellation follows from reflection symmetry. Both sums are nonzero for \(d\ge1\).

**3. The second scale.** Identify \(\mathcal P_d\) with its Legendre coefficient space. Split it orthogonally as \(E_d\oplus K_d\), where \(E_d=K_d^{\perp}\), and denote endpoint evaluation by \(T:E_d\to\mathbb R^2\), \(Tp=(p(0),p(1))\). Since \(d\ge2\), \(T\) is an isomorphism. Write the compression in this decomposition as
\[
H_{n,d}=\begin{pmatrix}A_m&C_m\\C_m^*&D_m\end{pmatrix}.
\]
Formula (4), used for products of polynomials, yields the following **operator-norm** expansions in these fixed spaces:
\[
 A_m=\frac{T^*T}{4m^2}+O_d(m^{-4}),\qquad
 C_m=\frac{3T^*R J_d}{8m^4}+O_d(m^{-6}),\qquad
 D_m=\frac{15J_d^*J_d}{8m^6}+O_d(m^{-8}), \tag{5}
\]
where \(R=\mathrm{diag}(-1,1)\). Indeed for \(p\in K_d\), \(q\in E_d\), the first nonzero term of \(\Delta_n(pq)\) is \(\frac{3}{8m^4}(p'(1)q(1)-p'(0)q(0))\). If \(p,q\in K_d\), their product vanishes to second order at both endpoints; expansion of \(a(\theta)\) to order \(\theta^5\) gives \(\Delta_n(pq)=\frac{15}{8m^6}(p'(0)q'(0)+p'(1)q'(1))+O_d(m^{-8})\). These facts prove (5).

For large \(m\), \(A_m\) is positive definite. Its Schur complement is
\[
\begin{aligned}
D_m-C_m^*A_m^{-1}C_m
&=\frac1{m^6}\left(\frac{15}{8}J_d^*J_d
-\frac9{16}J_d^*R\,T(T^*T)^{-1}T^*R J_d\right)+O_d(m^{-8})\\
&=\frac{21}{16m^6}J_d^*J_d+O_d(m^{-8}), \tag{6}
\end{aligned}
\]
because \(T:E_d\to\mathbb R^2\) is invertible and \(R^2=I\). For eigenvalues \(\lambda=m^{-6}\zeta\) with bounded \(\zeta\), the exact characteristic determinant factorization through \(A_m-\lambda I\) shows that the small eigenvalues scaled by \(m^6\) converge to those of (6), while (2) supplies the two large eigenvalues. The determinant argument also rules out additional scales between \(m^{-2}\) and \(m^{-6}\): the two largest eigenvalues are \(\asymp m^{-2}\), and the other eigenvalues satisfy \(O_d(m^{-6})\) by the Schur block factorization.

Finally every \(p\in K_d\) has the form \(p(x)=x(1-x)s(x)\), \(\deg s\le d-2\), and \(J_dp=(s(0),-s(1))\). Therefore \(\mathrm{rank}(J_d)=\min(2,d-1)\). For \(d=2\), \(K_d\) is spanned by \(p=x(1-x)\), whose squared \(L^2\) norm is \(1/30\) and whose endpoint derivative squares sum to \(2\). The sole eigenvalue of \(\frac{21}{16}J_d^*J_d\) is \((21/16)(2)/(1/30)=315/4\), completing (3).

## Verification

The included `verify.py` uses only Python 3 standard-library rational arithmetic. Running `python3 verify.py` prints `VERIFY_OK: independent exact integrations and finite asymptotic checks: 115`. Two separate methods integrate the test polynomial: (i) elementary cosine-product moments and (ii) the Chebyshev three-term recurrence followed by exact polynomial integration. Checks include several degrees, \(m=2^n\) for \(1\le n\le6\), exact identities for \(g=1,x,x(1-x)\), reflection cancellation, the \(m^{-6}\) test on \(g=x^2(1-x)^2\), and the scaled determinant of the \(d=2\) block. The observed determinant tends to \(2835/8\) after multiplication by \(m^{10}\), as forced by the three predicted leading eigenvalues. These tests do not establish the infinite limits; the endpoint expansion and Schur-complement proof do.

## Relationship to prior work

Janowicz and Orłowski, *Quantum logistic map considered as discrete-time Heisenberg equation* (arXiv:2607.19159v1, first posted 2026-07-21), Theorem 2 and its proof in Section 4.2, give an **exact finite Chebyshev-moment formula** for every fixed Legendre matrix element and a uniform-in-time-for-fixed-indices \(O(4^{-n})\) estimate. These results, including the exact matrix entries, are prior art and not claimed here. The result above adds the explicit endpoint-jet distributional asymptotics, a rank-two leading Galerkin profile, and a strictly separated \(64^{-n}\) eigenvalue tier whose coefficient involves a nontrivial Schur correction \(21/16\). The inspected source does not state these eigenvalue multiplicities or the two-scale spectral limit. Its exact entries are compatible with, and allow independent cross-checking of, the present theorem. The angle-doubling conjugacy itself is classical; see MathWorld's *Logistic Map--r=4*.

## Limitations

All estimates and eigenvalue limits hold for a **fixed** polynomial cutoff. No growing-cutoff uniformity, no operator-norm convergence, and no statements about the dynamics of an iterated projected nonlinear matrix map follow. The infinite-dimensional multiplication operators do not converge in norm: \(\|M_{f^{\circ n}}-\tfrac12I\|=\tfrac12\) for every \(n\), since each iterate ranges over \([0,1]\). The asymptotic result is derived from classical trigonometric conjugacy and integration by parts; it is not a novel conjugacy principle. An equivalent asymptotic spectral extraction from the known exact Chebyshev formula could appear in other literature; no independent priority determination has been performed.

## References

1. M. Janowicz and A. Orłowski, *Quantum logistic map considered as discrete-time Heisenberg equation*, arXiv:2607.19159v1 (2026-07-21), https://arxiv.org/abs/2607.19159 . Full publicly accessible text: https://www.researchgate.net/publication/410698105_Quantum_logistic_map_considered_as_discrete-time_Heisenberg_equation , especially Section 4.2, Theorem 2, equations (23)–(31).
2. E. W. Weisstein, *Logistic Map--r=4*, Wolfram MathWorld, https://mathworld.wolfram.com/LogisticMapR=4.html . Classical conjugacy and invariant density.
3. Ł. Pawela and K. Życzkowski, *Matrix logistic map: Fractal spectral distributions and transfer of chaos*, *Chaos* 36 (2026), 033139, https://doi.org/10.1063/5.0298024 . Distinct matrix-valued logistic-map model; not a source of the two-scale compression theorem.
