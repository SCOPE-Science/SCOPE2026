# Higher Airy eigenvalue quantization and eigenvector limits for four-periodic geometric weighted shifts

## Finding

Fix real \(s,t>0\). On complex \(\ell^2(\mathbb N_0)\), let \(T_q e_j=\sigma_jq^j e_{j+1}\), where \(0<q<1\) and the strictly positive sequence \(\sigma\) has period four with \((\sigma_0,\sigma_1,\sigma_2,\sigma_3)=(1,s,1,t)\). Put \(J_q=(T_q+T_q^*)/2\), and order its strictly positive eigenvalues decreasingly, counting multiplicities, as \(\lambda_1(q)>\lambda_2(q)>\cdots>0\).

Define
\[
D_0=\sqrt{4+(s-t)^2},\quad L=\frac{s+t+D_0}{4},\quad
\kappa=\frac{2stL}{(s+t)D_0},\quad h=(-\log q)^{1/3}.
\]
Let \(a_k\) be the \(k\)-th positive solution of \(\operatorname{Ai}(-a)=0\), in increasing order. **For every fixed integer \(k\ge1\)**,
\[
\boxed{\lim_{q\uparrow1}\frac{L-\lambda_k(q)}{(-\log q)^{2/3}}=\kappa^{1/3}a_k.}
\]
Thus the entire fixed-rank upper-edge hierarchy is quantized by the Dirichlet Airy zeros. In particular, for every fixed \(k\ge1\),
\[
\lim_{q\uparrow1}\frac{\lambda_k(q)-\lambda_{k+1}(q)}{(-\log q)^{2/3}}
=\kappa^{1/3}(a_{k+1}-a_k)>0.
\]

The theorem also determines the eigenvector profiles. Put \(r=(s-t+D_0)/2\), extend \(\phi=(1,r,r,1)\) four-periodically, and write \(\bar m=(1+r^2)/2\). For any \(\ell^2\)-normalized real eigenvector \(u^{(k,q)}\) of \(J_q\) at \(\lambda_k(q)\), define its macroscopic envelope by linear interpolation of
\[
G_{k,q}(4jh)=\sqrt{\frac{\bar m}{h}}\,\frac{u^{(k,q)}_{4j}}{\phi_{4j}}
\qquad(j\ge0).
\]
The sign of each eigenvector can be chosen so that, as \(q\uparrow1\), \(G_{k,q}\) converges strongly in \(L^2(0,\infty)\) and locally uniformly to the normalized real function
\[
g_k(x)=C_k\operatorname{Ai}\!\left((L/\alpha)^{1/3}x-a_k\right),\quad
\alpha=\frac{2st}{L(s+t)D_0},\quad C_k>0,\quad\int_0^\infty g_k(x)^2\,dx=1.
\]
No convergence rate or uniformity in a growing rank \(k\) is claimed.

## Assumptions and scope

The operator acts on the half-line beginning with the edge of weight \(1\) between indices zero and one. Both modulation parameters are fixed and strictly positive. For each \(q<1\), \(T_q\), hence \(J_q\), is compact; positivity of all Jacobi off-diagonal entries gives simple nonzero point spectrum. There are infinitely many positive eigenvalues: disjoint supported adjacent-pair test vectors exhibit positive Rayleigh quotients on arbitrarily large-dimensional subspaces. The theorem concerns fixed \(k\) as \(q\uparrow1\), not an eigenvalue counting law for ranks varying with \(q\). The primary classification is spectral theory of bounded operators (MSC2020 47A10).

## Proof

**1. Periodic ground state and exact quadratic form.** Let \(\epsilon=-\log q=h^3\). The four-periodic vector \(\phi=(1,r,r,1)\) obeys
\[
\frac{\sigma_{j-1}\phi_{j-1}+\sigma_j\phi_{j+1}}2=L\phi_j\qquad(j\in\mathbb Z).
\]
Set \(m_j=\phi_j^2\), \(c_j=\sigma_j\phi_j\phi_{j+1}\); then \(2Lm_j=c_{j-1}+c_j\), \(c_{-1}=t\), and \((c_0,c_1,c_2,c_3)=(r,sr^2,r,t)\). For a real finite-support sequence \(v\), with \(u_j=\phi_jv_j\), direct square completion gives
\[
\begin{aligned}
L\sum_{j\ge0}m_jv_j^2-\langle J_{e^{-h^3}}u,u\rangle
={}&\frac12\sum_{j\ge0}c_je^{-h^3j}(v_{j+1}-v_j)^2
+\frac t2v_0^2\\
&+\frac12\sum_{j\ge1}\{c_j(1-e^{-h^3j})+c_{j-1}(1-e^{-h^3(j-1)})\}v_j^2.
\end{aligned}
\tag{1}
\]
This identity, by density, is valid on the weighted sequence Hilbert space \(\ell^2(m)\). Denote its nonnegative right-hand side by \(Q_h(v)\), and its mass by \(M(v)=\sum m_j|v_j|^2\). The \(k\)-th smallest eigenvalue of the positive form \(Q_h\), below its essential level \(L\), is precisely \(L-\lambda_k(e^{-h^3})\) by the min–max principle.

**2. Cell resistance and effective continuum form.** Define
\[
S=\frac2r+\frac1{sr^2}+\frac1t,\qquad \bar m=\frac{1+r^2}{2}.
\]
For each complete four-edge cell, weighted Cauchy–Schwarz gives the *sharp* inequality
\[
\sum_{j=4n}^{4n+3}c_j|v_{j+1}-v_j|^2
\ge \frac{|v_{4n+4}-v_{4n}|^2}{S},
\tag{2}
\]
with equality exactly for cell increments proportional to \(1/c_j\). The effective diffusivity per unit mass is
\[
\alpha=\frac{2}{S\bar m}=\frac{4}{(1+r^2)S}
=\frac{2st}{L(s+t)D_0}.
\tag{3}
\]
The last identity follows from \(r^2-(s-t)r=1\) and \(D_0=r+r^{-1}\). Define the Dirichlet Airy form on \(L^2(0,\infty)\):
\[
\mathfrak a(g)=\alpha\int_0^\infty|g'(x)|^2dx+L\int_0^\infty x|g(x)|^2dx,
\quad\mathcal D(\mathfrak a)=H_0^1(0,\infty)\cap L^2(xdx).
\tag{4}
\]
Its form domain embeds compactly in \(L^2\): local compactness comes from the one-dimensional Rellich theorem, and the moment term bounds the mass outside a large interval by \(O(R^{-1})\).

**3. Compactness for every bounded-energy family.** Suppose \(M(v_h)=1\) and \(Q_h(v_h)\le Ch^2\). Formula (1) forces \(|v_{h,0}|=O(h)\). On any fixed macroscopic interval \(j\le R/h\), \(e^{-h^3j}=1+O_R(h^2)\), so \(\sum_{j\le R/h}|v_{h,j+1}-v_{h,j}|^2=O_R(h^2)\). The potential in (1) is bounded below, for \(j\ge2\), by \(c\min(h^3(j-1),1)m_j\) with \(c>0\) depending on \(s,t\). It follows that
\[
\limsup_{h\downarrow0}\sum_{j\ge R/h}m_j|v_{h,j}|^2\le C_1/R\qquad(R\ge2),
\tag{5}
\]
where \(C_1\) depends only on the energy bound and parameters. This is the needed tightness.

Interpolate the cell values \(\sqrt{\bar m/h}\,v_{h,4n}\) linearly at the positions \(4nh\), obtaining \(G_h\). Estimate (2), with the preceding local coefficient estimate, bounds \(G_h\) in \(H^1(0,R)\) for every fixed \(R\); the boundary penalty implies \(G_h(0)\to0\). Passing to a subsequence gives local uniform and strong local \(L^2\) convergence to some \(g\in H_0^1\). The mass in a cell differs from \(4\bar m|v_{h,4n}|^2\) by a summable \(o(1)\) error: use the four-site Cauchy inequality and the local \(O_R(h^2)\) gradient bound. Combined with (5) and four-periodic averaging this yields \(\|g\|_2=1\) and global strong \(L^2\) convergence of \(G_h\).

**4. Liminf inequality for all vectors.** On \(j\le R/h\), estimate (2), the coefficient limit \(e^{-h^3j}\to1\), and weak lower semicontinuity of the interpolated derivatives give
\[
\liminf_{h\downarrow0}\frac{Q_h^{\rm kinetic}(v_h)}{h^2}
\ge \alpha\int_0^\infty|g'(x)|^2dx.
\tag{6}
\]
For fixed \(R\), Taylor expansion of the potential weights, uniformly at \(j\le R/h\), gives
\[
\frac{c_j(1-e^{-h^3j})+c_{j-1}(1-e^{-h^3(j-1)})}{2h^2}
=Lm_j(hj)+O_R(h),
\tag{7}
\]
using \(c_{j-1}+c_j=2Lm_j\). The local mass convergence and periodic averaging therefore imply a potential liminf of \(L\int x|g|^2\), after \(R\uparrow\infty\). Consequently
\[
\liminf_{h\downarrow0}h^{-2}Q_h(v_h)\ge \mathfrak a(g).
\tag{8}
\]
The argument applies to arbitrary signed and complex vectors by real and imaginary parts and polarization, not merely to the ground state.

**5. Recovery for an arbitrary finite-dimensional test space.** For a smooth compactly supported Dirichlet function \(g\), take \(v_{4n}=\sqrt{h/\bar m}\,g(4nh)\). On each cell define the intermediate four values by the resistance-minimizing rule
\[
 v_{4n+j+1}-v_{4n+j}
 =\frac{v_{4n+4}-v_{4n}}{S c_j},\quad j=0,1,2,3.
\tag{9}
\]
Then Riemann sums and equality in (2) show
\[
M(v_h)\to\|g\|_2^2,\qquad h^{-2}Q_h(v_h)\to\mathfrak a(g).
\tag{10}
\]
Since the construction is linear in \(g\), the norm and energy convergence are uniform on the unit sphere of *every fixed finite-dimensional* span of such test functions (polarize the convergent quadratic forms). Smooth compactly supported Dirichlet functions form a core of \(\mathfrak a\). Thus (10) supplies simultaneous recovery for a basis of the first \(k\) Airy eigenfunctions, after form approximation. By the \(k\)-dimensional min–max principle,
\[
\limsup_{h\downarrow0}h^{-2}(L-\lambda_k(e^{-h^3}))\le\mu_k,
\tag{11}
\]
where \(\mu_k\) is the \(k\)-th eigenvalue of the operator associated with (4).

**6. Matching lower bound for every rank.** Fix \(k\) and choose an orthonormal family of the first \(k\) eigenvectors of \(J_{e^{-h^3}}\), transported to \(\ell^2(m)\). Their energy quotients are each at most \(h^2(\mu_k+o(1))\), by (11). For any linear combination the same bound follows by diagonalization. Apply Step 3 along one subsequence to the entire finite family, and Step 4 to every rational linear combination; then use continuity to extend to all coefficients. The limiting envelopes form an orthonormal \(k\)-tuple in \(L^2\), and every nonzero vector in their span has Airy Rayleigh quotient at most \(\liminf h^{-2}(L-\lambda_k)\). The continuum min–max principle gives
\[
\mu_k\le \liminf_{h\downarrow0}h^{-2}(L-\lambda_k(e^{-h^3})).
\tag{12}
\]
Equations (11)–(12) establish convergence for all fixed \(k\).

**7. Eigenvector convergence and constants.** The Dirichlet Airy operator \(-\alpha g''+Lxg\) has compact resolvent and simple eigenvalues
\[
\mu_k=\alpha^{1/3}L^{2/3}a_k=\kappa^{1/3}a_k.
\tag{13}
\]
Its real normalized eigenfunctions are the displayed translated Airy functions. Step 3 makes every low-energy sequence precompact. Induct on \(k\): any limit of the first normalized eigenvector has unit norm and Rayleigh quotient \(\mu_1\), and so is \(\pm g_1\); a limit of the \(k\)-th eigenvector is orthogonal to earlier limiting eigenvectors and has Rayleigh quotient at most \(\mu_k\), forcing membership in the one-dimensional \(k\)-th Airy eigenspace. Fixing its sign gives the asserted full-sequence strong \(L^2\) and local uniform convergence. Subtract the eigenvalue limits at adjacent ranks for the spectral-gap formula. Finally, \((-\log q)/(1-q)\to1\), allowing either boundary parameter.

## Verification

The standalone `VERIFY.py` checks the exactly algebraic ground-state identity and four-edge resistance formula with rational coefficients for two nontrivial parameter pairs; it also computes the first three upper-edge eigenvalues for several small values of \(-\log q\) using symmetric tridiagonal eigensolvers and compares their scaled gaps with the first three Airy zeros. Run `python VERIFY.py` (Python 3, NumPy and SciPy). Exact finite algebraic checks corroborate the identities used in Steps 1–2; the infinite-dimensional quantization and eigenvector convergence are established by Steps 3–7, not inferred from finite eigenvalues.

## Relationship to prior work

Ghosh, Birbonshi and Ojha (2026) introduced this period-four geometrically damped shift and analyzed its numerical radius through bounds and entire determinants. Chien and Nakazato (2009) treated the unmodulated geometric shift, with determinantal and numerical-radius results. A published 11 October 2026 note, *A sharp Airy-edge law for four-periodic geometric weighted shifts*, proved precisely the **first** Airy level, \(\lambda_1\), with its explicit cell resistance and scalar variational limit. Those formulas and the rank-one Airy limit are recognized here as prior work. The additional assertion established above is **simultaneous fixed-rank Airy quantization, sharp adjacent gaps, and convergence of the individual higher eigenvectors**. The first-level result by itself contains no information about higher eigenvalues; the multi-dimensional min–max and spectral-compactness argument in Steps 5–7 is essential. General periodic-Jacobi turning-point methods provide conceptual background but do not by themselves identify a covering result with this weighted half-line operator, normalization, and all fixed spectral levels.

## Limitations

The claims are pointwise in every fixed rank and fixed positive pair \(s,t\), not uniform in rank or in degenerating modulation parameters. The error is \(o((-\log q)^{2/3})\), with no explicit uniform rate. The initiating 2026 preprint's complete primary text was inaccessible during this comparison, although its public abstract and a detailed third-party synopsis were examined; potential uninspected coverage is an originality risk. The related 2026 first-level research note was read in full. Independent assessment of originality and proof has not been performed.

## References

1. A. Ghosh, R. Birbonshi, S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486, first publicly posted 2026-08-18. https://arxiv.org/abs/2608.17486
2. *A sharp Airy-edge law for four-periodic geometric weighted shifts*, published mathematical note, 2026-10-11. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-a-sharp-airy-edge-law-for-four-periodic-geometric-weighted-shift--cffc9a187d0d/RESULT.md
3. M.-T. Chien, H. Nakazato, *The numerical radius of a weighted shift operator with geometric weights*, Electronic Journal of Linear Algebra 18 (2009), 58–63. https://doi.org/10.13001/1081-3810.1293
4. G. Świderski, B. Trojan, *Orthogonal polynomials with periodically modulated recurrence coefficients in the Jordan block case*, Annales de l'Institut Fourier 74 (2024), 1521–1601. https://doi.org/10.5802/aif.3624
