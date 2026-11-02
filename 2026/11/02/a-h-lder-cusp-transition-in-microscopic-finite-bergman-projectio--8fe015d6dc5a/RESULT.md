# A Hölder-cusp transition in microscopic finite Bergman projection kernels

## Finding

The second finite-size correction of the microscopic Bergman polynomial projection kernel on the unit disk undergoes a sharp change of order at radial Hölder exponent \(\alpha=1/2\). The boundary cusp dominates a smooth slope when \(0<\alpha<1/2\); both effects coexist at \(\alpha=1/2\); and the smooth slope together with the universal discretization correction dominates when \(1/2<\alpha<1\). The result gives exact two-point coefficient functions and uniform errors, rather than only a leading boundary-universality limit.

Fix \(0<\alpha<1\), \(c>0\), and \(d>-1-c\), and put
\[
W(r)=1+c(1-r)^\alpha+d(1-r),\qquad 0\le r\le1.
\]
Equip the complex polynomial space \(\mathcal P_{N-1}=\operatorname{span}\{1,z,\ldots,z^{N-1}\}\) with the inner product induced by \(W(|z|)\,dA(z)/\pi\) on the unit disk. Its reproducing kernel is denoted \(K_N(z,w)\). For \(\operatorname{Re}u,\operatorname{Re}v\ge0\), write \(s=u+\overline v\), and define
\[
F_\gamma(s)=\int_0^1t^\gamma e^{-st}\,dt\quad(\gamma>-1),\qquad
C_\alpha=c2^{-\alpha}\Gamma(1+\alpha),\qquad D=d/2,
\]
\[
G(s)=sF_1(s)+\tfrac12e^{-s}.
\]
Then, as the positive integer \(N\to\infty\),
\[
\begin{aligned}
&\frac{K_N(e^{-u/N},e^{-v/N})}{N^2}
=F_1(s)-\frac{C_\alpha F_{1-\alpha}(s)}{N^\alpha}\\[2pt]
&\quad+\begin{cases}
\displaystyle\frac{C_\alpha^2F_{1-2\alpha}(s)}{N^{2\alpha}}
+O(N^{-\min\{3\alpha,1\}}),&0<\alpha<\frac12,\\[5pt]
\displaystyle\frac{G(s)+(C_\alpha^2-D)F_0(s)}N
+O(N^{-3/2}),&\alpha=\frac12,\\[5pt]
\displaystyle\frac{G(s)-DF_0(s)}N
+O(N^{-2\alpha}),&\frac12<\alpha<1.
\end{cases}
\end{aligned}
\]
All remainders are uniform when \((u,v)\) ranges over any fixed compact subset of the product of the closed right half-planes; their constants can depend on that compact set and on the fixed weight parameters.

On the boundary diagonal \(u=v=0\), the two-point statement specializes to
\[
\frac{K_N(1,1)}{N^2}=\frac12-\frac{C_\alpha}{2-\alpha}N^{-\alpha}
+\begin{cases}
\displaystyle\frac{C_\alpha^2}{2-2\alpha}N^{-2\alpha}+O(N^{-\min\{3\alpha,1\}}),&\alpha<\frac12,\\[5pt]
\displaystyle(\frac12+C_\alpha^2-D)N^{-1}+O(N^{-3/2}),&\alpha=\frac12,\\[5pt]
\displaystyle(\frac12-D)N^{-1}+O(N^{-2\alpha}),&\alpha>\frac12.
\end{cases}
\]
The first cusp coefficient is nonzero for every \(c>0\). On \(0<\alpha<1/2\), the next coefficient is also strictly positive on the diagonal, so the \(N^{-2\alpha}\) scale is genuine. At and above the transition, the displayed two-point \(N^{-1}\) profile is nonzero as a function of \(s\), although its value may vanish at selected points for special parameters.

## Assumptions and scope

The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(dA\) is ordinary Euclidean area. Since \(x^\alpha\ge x\) for \(x\in[0,1]\), the restrictions \(c>0\) and \(d>-1-c\) ensure \(W(r)\ge1+(c+d)(1-r)>0\) on the closed disk. The kernel has exactly \(N\) polynomial terms, degrees \(0,\ldots,N-1\), and is normalized with \(dA/\pi\), not with unnormalized area. The exponent \(\alpha\) and other parameters are held fixed as \(N\to\infty\). The points \(e^{-u/N}\) are in the closed disk for \(\operatorname{Re}u\ge0\); on-boundary evaluation is legitimate for polynomials. Only the stated cusp-plus-linear radial weights are considered; the result makes no assertion about arbitrary nonsmooth weights or nonradial domains.

## Proof

**Step 1 (exact radial moments).** Radial symmetry makes distinct monomials orthogonal. Put \(j=k+1\). The squared norm of \(z^k\) is
\[
\mu_{j-1}=2\int_0^1 r^{2j-1}W(r)\,dr
=\frac1j+2c\,B(2j,1+\alpha)+\frac d{j(2j+1)},
\]
where \(B\) is the Euler beta function. Therefore
\[
K_N(z,w)=\sum_{j=1}^N\frac{(z\overline w)^{j-1}}{\mu_{j-1}}.
\]
The beta expression is exact, not an approximation.

**Step 2 (uniform moment inversion).** The gamma-ratio asymptotic
\[
\frac{\Gamma(2j)}{\Gamma(2j+1+\alpha)}
=(2j)^{-1-\alpha}(1+O_\alpha(j^{-1}))
\]
gives
\[
j\mu_{j-1}=1+C_\alpha j^{-\alpha}+Dj^{-1}
+O_{\alpha,c,d}(j^{-\alpha-1}+j^{-2}).
\]
For all sufficiently large \(j\), apply the convergent reciprocal identity \(1/(1+x)=1-x+x^2+O(x^3)\), with \(x=O(j^{-\alpha})\). Retaining precisely the terms needed across the three regimes yields
\[
\frac1{\mu_{j-1}}
=j-C_\alpha j^{1-\alpha}+C_\alpha^2j^{1-2\alpha}-D
+O_{\alpha,c,d}\!\left(j^{1-3\alpha}+j^{-\alpha}+j^{-1}\right).
\]
Indeed, the mixed product of \(j^{-\alpha}\) and \(j^{-1}\) gives \(O(j^{-\alpha})\) after multiplication by \(j\); the square of \(j^{-1}\) and the error in the gamma ratio give \(O(j^{-1})\). Replacing a finite number of initial terms by this expansion changes the kernel divided by \(N^2\) only by \(O(N^{-2})\).

**Step 3 (uniform microscopic summation).** On any compact set of complex \(s\), the following Riemann-sum formulas hold uniformly:
\[
\frac1{N^2}\sum_{j=1}^N je^{-s(j-1)/N}
=F_1(s)+\frac{G(s)}N+O(N^{-2}),
\]
\[
\frac1{N^2}\sum_{j=1}^N j^{1-\alpha}e^{-s(j-1)/N}
=N^{-\alpha}F_{1-\alpha}(s)+O(N^{-\alpha-1}),
\]
\[
\frac1{N^2}\sum_{j=1}^N j^{1-2\alpha}e^{-s(j-1)/N}
=\begin{cases}
N^{-2\alpha}F_{1-2\alpha}(s)+O(N^{-2\alpha-1}),&0<\alpha\le\frac12,\\
O(N^{-2\alpha}),&\frac12<\alpha<1,
\end{cases}
\]
\[
\frac1{N^2}\sum_{j=1}^N e^{-s(j-1)/N}
=N^{-1}F_0(s)+O(N^{-2}).
\]
To verify the first formula, set \(t_j=j/N\) and note that the summand is \(e^{s/N}t_j e^{-st_j}/N\). The right-endpoint Euler--Maclaurin formula gives a correction \(e^{-s}/(2N)\); multiplying by \(e^{s/N}=1+s/N+O(N^{-2})\) gives \(G(s)\). For the other precise summation formulas, \(t^{1-\alpha}e^{-st}\) has bounded variation for every \(0<\alpha<1\), and \(t^{1-2\alpha}e^{-st}\) has bounded variation only when \(\alpha\le1/2\). Their right Riemann sums have error \(O(N^{-1})\) before the indicated scaling. When \(\alpha>1/2\), the exponent \(1-2\alpha\in(-1,0)\) is integrably singular at zero, and direct power-sum comparison, rather than a bounded-variation estimate, gives the asserted \(O(N^{-2\alpha})\) bound. The exponential shift contributes an error of the same or smaller order.

**Step 4 (compare decay exponents).** Insert Step 2 into the exact kernel series of Step 1, with \(z\overline w=e^{-s/N}\), and use Step 3. The cumulative \(j^{1-3\alpha}\) remainder, divided by \(N^2\), is \(O(N^{-3\alpha})\) when \(3\alpha<2\) (and smaller than needed when \(3\alpha\ge2\)); the other remainders are \(O(N^{-1-\alpha})\) or smaller. For \(0<\alpha<1/2\), \(N^{-2\alpha}\) dominates \(N^{-1}\), and the omitted terms are \(O(N^{-\min\{3\alpha,1\}})\). At \(\alpha=1/2\), the square-cusp term and the smooth/discretization terms all have order \(N^{-1}\); all discarded terms are \(O(N^{-3/2})\). For \(1/2<\alpha<1\), the square-cusp term is \(O(N^{-2\alpha})\) and the displayed \(N^{-1}\) terms dominate. This proves the three cases with the stated uniformity.

Finally \(F_\gamma(0)=1/(\gamma+1)\) and \(G(0)=1/2\) give the diagonal statements. Since \(C_\alpha>0\), the cusp coefficient never vanishes. The endpoint function \(G(s)-DF_0(s)\) cannot vanish identically because \(F_0\) and \(e^{-s}\) are linearly independent, and the critical profile adds a constant multiple of \(F_0\). This verifies a genuine two-point \(N^{-1}\) correction in both latter regimes.

## Verification

The standalone `check.py` recomputes the exact beta-function moments and independently integrates the radial moments by Simpson quadrature. It also checks the unweighted finite-kernel normalization, conjugation symmetry and the three rescaled second-order profiles for real and complex boundary separation parameters. The script requires only the Python standard library; run it with `python3 check.py` from the same directory. On the accompanying execution it passed 210 finite assertions. These computations are supplementary and **do not** prove any asymptotic statement; Steps 1--4 supply the infinite-\(N\) proof.

## Relationship to prior work

Hübner's 2026 study (arXiv:2610.24693, first public October 17, 2026) establishes strong weighted Bergman polynomial asymptotics at finite regularity and motivates distinguishing cusp effects from smooth corrections. It concerns individual orthogonal polynomials on Jordan domains and does not state the three-regime, microscopic, **finite projection-kernel** expansion for the present explicit positive radial family. Lubinsky's 2009 universality theorem gives the leading boundary microscopic kernel for general positive continuous weights, but does not give these two exact subleading coefficient functions or the \(\alpha=1/2\) transition. Hedenmalm--Wennman's analytic-weight hard-edge expansion addresses a more regular category and does not directly provide the Hölder-cusp competition. Pennanen--Rättyä--Wang--Wu's 2026 radial weighted Bergman reproducing-kernel bounds concern the **untruncated infinite kernel**, giving estimates rather than finite-\(N\) coefficients. Zeytuncu's radial-kernel study also concerns full kernels and zeros, not this truncation asymptotic. These comparisons distinguish mathematical implications, not merely paper titles.

## Limitations

The proof exploits exact beta moments of a fixed model family and does not yield an arbitrary-weight second-order universality theorem. Only fixed \(\alpha,c,d\) and bounded microscopic coordinates are covered. For \(\alpha>1/2\) the \(N^{-1}\) coefficient may vanish at particular coordinate pairs or for certain diagonal choices; the assertion of sharp order concerns the full two-point profile, not each point. For \(\alpha=1/2\) and \(\alpha<1/2\), the indicated remainder can contain further nonzero terms, so no higher-order cancellation is claimed. Independent validation has not been performed. Equivalent coverage in older, difficult-to-index asymptotic literature cannot be categorically excluded.

## References

1. Lennart Aljoscha Hübner, *Asymptotics of Weighted Bergman Polynomials under Finite Regularity*, arXiv:2610.24693 (first publicly submitted 2026-10-17), https://arxiv.org/abs/2610.24693.
2. Doron S. Lubinsky, *Universality Type Limits for Bergman Orthogonal Polynomials*, 2009 preprint, https://lubinsky.math.gatech.edu/Research%20papers/UniversBergmanOct09.pdf.
3. Håkan Hedenmalm and Aron Wennman, *Riemann-Hilbert Hierarchies for Hard Edge Planar Orthogonal Polynomials*, arXiv:2008.02682, https://arxiv.org/abs/2008.02682.
4. Atte Pennanen, Jouni Rättyä, Siyu Wang and Fanglei Wu, *Optimal Off-Diagonal Upper Estimates for Bergman Reproducing Kernels*, arXiv:2607.19959 (first submitted 2026-07-22), https://arxiv.org/abs/2607.19959.
5. Yunus Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806, https://arxiv.org/abs/1009.2806.
