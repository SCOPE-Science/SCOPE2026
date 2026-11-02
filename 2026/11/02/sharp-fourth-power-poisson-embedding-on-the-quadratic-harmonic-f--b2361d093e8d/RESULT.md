# Sharp fourth-power Poisson embedding on the quadratic harmonic Fourier band

## Finding

Let \(\mathcal P_2\) be the complex vector space of harmonic polynomials on the unit disk with angular frequencies \(-2,-1,0,1,2\). The normalized boundary and area norms are
\[
\|f\|_{h^2}^2=\frac1{2\pi}\int_0^{2\pi}|f(e^{i\theta})|^2\,d\theta,
\qquad
\|f\|_{b^4}^4=\frac1\pi\int_{|z|<1}|f(z)|^4\,dx\,dy.
\]
Define
\[
P(s)=18s^4+121s^3+180s^2-100s-80.
\]
It has exactly one positive root \(s_*\), and \(0.7425<s_*<0.7426\). Put
\[
K_*=
\frac{33s_*^4+240s_*^3+520s_*^2+960s_*+560}
{8(7s_*^4+40s_*^3+30s_*^2+80s_*+60)}
=1.349833287676307\ldots.
\]
**The sharp quadratic-bandlimited inequality** is
\[
\boxed{\ \|f\|_{b^4}^4\le K_*\|f\|_{h^2}^4\quad (f\in\mathcal P_2).\ }
\]
Define
\[
t_*=
\frac{9s_*^4+40s_*^3+10s_*^2+80s_*+40}
{10(s_*^2+8s_*+8)},
\qquad
x_*=(1+t_*+s_*^2/2)^{-1/2}.
\]
Every nonzero equality case, and no other, is
\[
\boxed{\
f(z)=\gamma x_*\left[1+\sqrt{t_*/2}\left(e^{i\vartheta}z+e^{-i\vartheta}\overline z\right)
+\frac{s_*}{2}\left(e^{2i\vartheta}z^2+e^{-2i\vartheta}\overline z^2\right)\right],
\ }
\]
where \(\gamma\in\mathbb C\setminus\{0\}\) and \(\vartheta\in\mathbb R\). In particular, every nonzero extremizer has constant complex phase times a real harmonic polynomial after rotation, with a uniquely determined ratio of constant, linear and quadratic amplitudes. The norm ratio is \(K_*^{1/4}=1.077879056335061\ldots\).

## Assumptions and scope

Every \(f\in\mathcal P_2\) has the unique representation
\[
f(re^{i\theta})=\sum_{k=-2}^2c_k r^{|k|}e^{ik\theta},
\qquad c_k\in\mathbb C,\quad 0\le r<1.
\]
The boundary Hilbert norm is \(\sum_{k=-2}^2|c_k|^2\). No real-valuedness or relation between positive and negative frequency coefficients is imposed. All integrals use normalized angular measure \(d\theta/(2\pi)\) and normalized area measure \(dx\,dy/\pi\). This is an exact **five-dimensional Fourier cutoff**, not an assertion about arbitrary elements of harmonic \(h^2\).

## Proof

**1. The exact quartic form.** Angular orthogonality and the radial integral \(\int_0^1 2r^{M+1}\,dr=2/(M+2)\) give, with \(M=|i|+|j|+|k|+|l|\),
\[
\|f\|_{b^4}^4
=\sum_{\substack{i,j,k,l\in\{-2,-1,0,1,2\}\\i+j=k+l}}
\frac{2c_ic_j\overline{c_kc_l}}{2+|i|+|j|+|k|+|l|}.
\tag{1}
\]
Every coefficient in this four-index expansion is positive. Thus replacing all \(c_k\) by \(|c_k|\) cannot decrease the value and does not alter \(\|f\|_{h^2}\).

Put \(x=|c_0|\), \(a=|c_1|\), \(d=|c_{-1}|\), \(b=|c_2|\), \(e=|c_{-2}|\), and write \(A=a^2+d^2\), \(B=b^2+e^2\), \(p=ad\), \(q=be\). Expanding (1) for these five nonnegative numbers gives exactly
\[
\begin{aligned}
F={}&x^4+2x^2A+2x^2p+\tfrac43x^2B+\tfrac43x^2q\\
&+\tfrac43x\,[a^2b+d^2e+2ad(b+e)]\\
&+\tfrac13A^2+\tfrac23p^2+\tfrac15B^2+\tfrac25q^2+AB+2pq.
\end{aligned}
\tag{2}
\]

**2. Strict reflection symmetrization.** The arithmetic–geometric mean inequality yields \(p\le A/2\) and \(q\le B/2\). Cauchy–Schwarz and \(p\le A/2\) yield
\[
\begin{aligned}
a^2b+d^2e+2ad(b+e)
&\le\sqrt B\sqrt{(a^2+2p)^2+(d^2+2p)^2}\\
&=\sqrt B\sqrt{A^2+4Ap+6p^2}\\
&\le \tfrac3{\sqrt2}A\sqrt B.
\end{aligned}
\]
Consequently, with \(y=\sqrt A\), \(z=\sqrt B\),
\[
F\le G(x,y,z)
=x^4+3x^2y^2+2x^2z^2+2\sqrt2\,xy^2z
+\tfrac12y^4+\tfrac32y^2z^2+\tfrac3{10}z^4.
\tag{3}
\]
The constraint is \(x^2+y^2+z^2=\|f\|_{h^2}^2\). Equality in (3) holds when \(a=d=y/\sqrt2\) and \(b=e=z/\sqrt2\). If \(x,y,z>0\), all equality conditions force precisely these two within-pair equalities. Thus (3) is a sharp reduction of the full five-variable magnitude problem to three nonnegative variables, rather than a bound with an uncertain gap.

**3. Exact global maximum.** By homogeneity set \(x^2+y^2+z^2=1\). If \(x=0\), write \(v=z^2\); then \(G=\frac12+\frac12v-\frac7{10}v^2\le33/56\). If \(z=0\), write \(v=y^2\); then \(G=1+v-\frac32v^2\le7/6\). Both are strictly below the final constant. For \(x>0\) set
\[
s=\frac{\sqrt2 z}{x},\qquad t=\frac{y^2}{x^2},\qquad
Q(t,s)=\frac{\frac12t^2+(3+2s+\frac34s^2)t+1+s^2+\frac3{40}s^4}
{(1+t+s^2/2)^2}.
\]
The parameters satisfy \(s,t\ge0\), and \(G=Q(t,s)\). Let \(C=1+s^2/2\), \(B_0=3+2s+3s^2/4\), \(A_0=1+s^2+3s^4/40\). Direct differentiation yields
\[
\frac{\partial Q}{\partial t}
=\frac{(C-B_0)t+B_0C-2A_0}{(t+C)^3}.
\]
Since \(B_0-C=(s^2+8s+8)/4>0\) and \(B_0C-2A_0=(9s^4+40s^3+10s^2+80s+40)/40>0\), for each fixed \(s\ge0\) the unique maximum occurs at
\[
t=T(s)=\frac{9s^4+40s^3+10s^2+80s+40}{10(s^2+8s+8)}.
\]
Substituting gives the univariate profile
\[
R(s)=Q(T(s),s)
=\frac{33s^4+240s^3+520s^2+960s+560}
{8(7s^4+40s^3+30s^2+80s+60)}.
\]
Its derivative factors **exactly** as
\[
R'(s)=-\frac{5(s^2+8s+8)P(s)}
{2(7s^4+40s^3+30s^2+80s+60)^2}.
\tag{4}
\]
The coefficient sign pattern of \(P\) has exactly one change. Descartes' sign rule, together with \(P(0)=-80\) and positive leading coefficient, shows that \(P\) has exactly one positive zero; the derivative in (4) changes from positive to negative there. Hence \(R\) has a unique global maximum at \(s_*\), and \(t=T(s_*)\). This maximum exceeds \(7/6\), so it includes no boundary maximizer. Evaluating \(R(s_*)\) proves the sharp constant and the unique optimal magnitude vector.

**4. Complex equality.** At the maximizing magnitudes all five \(|c_k|\) are positive. Equality in the first triangle inequality requires the phases of every four-index term in (1) to agree with those of its positive diagonal terms. In particular, the resonances \(1+(-1)=0+0\), \(1+1=0+2\), and \((-1)+(-1)=0+(-2)\) require
\[
\arg(c_1)+\arg(c_{-1})=2\arg(c_0),\quad
2\arg(c_1)=\arg(c_0)+\arg(c_2),\quad
2\arg(c_{-1})=\arg(c_0)+\arg(c_{-2})
\pmod{2\pi}.
\]
These give \(\arg c_k=\phi+k\vartheta\) for every \(-2\le k\le2\). Conversely, affine frequency phases align every term of (1), attaining equality. Together with the unique optimal magnitudes from steps 2–3, this proves the displayed complete extremizer family.

## Verification

The accompanying executable `CHECK.py` reconstructs the 22-term quartic by independently summing all admissible four-index Fourier resonances using exact rational arithmetic. It tests (2) and (3), the normalized profile, the stationary formula \(T\), the rational maximum profile \(R\), derivative factorization (4), exact root bracketing, and boundary formulas using symbolic algebra. It then directly checks the equality witness and tests 768 additional randomly generated complex coefficient vectors. Its final status is `CHECK_OK exact-symbolic=12 random-complex=768`.

The symbolic identities establish the algebraic reductions. The universal inequality, uniqueness, and exhaustiveness of all equality cases follow from the **analytic** Cauchy–Schwarz, derivative-sign and phase-resonance arguments above, not from finite random tests or root approximations. The rational signs \(P(7425/10000)<0<P(7426/10000)\) verify the decimal bracket.

## Relationship to prior work

Das, Rasila, and Zhu (2026) study full harmonic Hardy-to-Bergman inclusions and explicitly leave the optimal unrestricted constant open, already in the planar case. Their estimate applies to this subspace but does not give its sharp fourth-power value or its equality shapes. The present five-frequency value is **not** claimed as an improved bound for the unrestricted class. Its purpose is an exact finite-bandwidth benchmark and a reflection-rigidity classification in the same nonlinear norm problem.

Kalaj–Bajrami (2018) address harmonic Riesz and Carleman inequalities for whole function classes; their available abstract and first-page preview do not state the five-frequency cutoff classification. A separate published result on weighted harmonic Bergman **circle traces** is a diagonal Hilbert-space \(L^2\)-to-\(L^2\) comparison, not the nonlinear disk-area fourth moment. A sharp quartic result for degree-two **spherical harmonics** concerns homogeneous modes on spheres, not planar harmonic Poisson sums across degrees zero, one, and two. A separate four-consecutive-character Fourier fourth-moment result has a circle integral without degree-dependent radial weights; its constant does not imply (3)–(4).

## Limitations

No sharp constant for the unrestricted harmonic \(h^2\to b^4\) embedding is asserted. The result is exact only for the complete five-frequency cutoff \(\mathcal P_2\), with unweighted planar disk area and Hilbert boundary norm. It does not directly imply optimal rates of convergence of higher spectral cutoffs. The full text of Kalaj–Bajrami (2018) was not inspected, and an unindexed equivalent finite-bandwidth calculation remains a residual originality risk. No independent mathematical audit has been performed.

## References

1. S. Das, A. Rasila and J.-F. Zhu, *Isoperimetric-type inequalities for pluriharmonic functions on the polydisc*, arXiv:2606.31024v1, submitted 2026-06-30, especially Section 7. https://arxiv.org/abs/2606.31024.
2. D. Kalaj and E. Bajrami, *On Some Riesz and Carleman Type Inequalities for Harmonic Functions in the Unit Disk*, Comput. Methods Funct. Theory 18 (2018), 295–305, DOI:10.1007/s40315-017-0226-y.
3. *Exact frequency staircase for weighted harmonic Bergman circle traces*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-frequency-staircase-for-weighted-harmonic-bergman-circle-t--e5356e299a36/RESULT.md.
4. *Sharp L4/L2 norm and extremizers for degree-two spherical harmonics*, published mathematical research record, 2026-09-20, https://github.com/Resultary/2026/blob/main/2026/9/20/SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f/RESULT.md.
5. *Exact fourth moment and all extremizers for four consecutive Fourier characters*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-fourth-moment-and-all-extremizers-for-four-consecutive-fou--77a4e780524e/RESULT.md.
