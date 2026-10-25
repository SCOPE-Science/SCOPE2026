# A sharp second-order three-Hermite ambiguity conditioning law

## Finding

Consider three separate normalized Hermite-window intensity measurements with precision shares \(w_0,w_1,w_2\geq0\) and \(w_0+w_1+w_2=1\). On an ambiguity-frequency disk with normalized squared radius \(R\), define the optimal **squared** lower singular multiplier bound
\[
M_3(R)=\max_{w_0+w_1+w_2=1\atop w_j\geq0}\ \min_{0\leq x\leq R}e^{-x}\bigl[w_0+w_1(1-x)^2+w_2(1-2x+x^2/2)^2\bigr].
\]
Set \(r_-=2-\sqrt2\), \(r_+=2+\sqrt2\), \(p=3-2\sqrt2\), \(q=3+2\sqrt2\), and
\[
\alpha_0=\frac{qe^{r_-}-pe^{r_+}}{q-p},\qquad
\alpha_1=\frac{e^{r_+}-e^{r_-}}{q-p},\qquad
C=\alpha_0+\alpha_1=5.984283368174\ldots .
\]
Both \(\alpha_0\) and \(\alpha_1\) are strictly positive. With
\[
F_R=e^{-R}(1-2R+R^2/2)^2,
\]
the exact sharp second-order asymptotic is
\[
\boxed{M_3(R)=F_R-CF_R^2+o(F_R^2)\qquad(R\to\infty).}
\]
For **every** maximizing allocation \(w(R)\), whether or not it is unique at finite \(R\),
\[
\boxed{\frac{w_0(R)}{F_R}\longrightarrow\alpha_0=0.929064805486\ldots,\qquad
\frac{w_1(R)}{F_R}\longrightarrow\alpha_1=5.055218562688\ldots,\qquad w_2(R)\longrightarrow1.}
\]
In particular, both lower-window shares are asymptotically necessary and the first-Hermite share is approximately \(5.441\) times the Gaussian share. The leading squared gain grows as \(e^{-R}R^4/4\); it is of order \(R^2\) larger than that attainable from the first two windows alone.

## Assumptions and scope

Let \(h_j\), \(j=0,1,2\), be the \(L^2(\mathbb R)\)-normalized Hermite functions and adopt the standard STFT convention \(V_gf(u,\omega)=\int_{\mathbb R}f(t)\overline{g(t-u)}e^{-2\pi i\omega t}\,dt\). The ambiguity transform of the unit-norm Hermite window has modulus
\[
|A_{h_j}(u,\omega)|=e^{-\pi(u^2+\omega^2)/2}|L_j(\pi(u^2+\omega^2))|,
\]
where \(L_0(x)=1\), \(L_1(x)=1-x\), and \(L_2(x)=1-2x+x^2/2\). Restrict the **unknown ambiguity-field input** to the disk \(D_R=\{(u,\omega):\pi(u^2+\omega^2)\leq R\}\). The three-channel linear Fourier-domain spectrogram response is the direct sum of the multipliers \(\sqrt{w_j}A_{h_j}\). Its squared least singular multiplier is precisely the minimum in the definition of \(M_3(R)\).

This statement concerns linear inversion of an unrestricted ambiguity field on \(D_R\). It does not assert a nonlinear phase-retrieval theorem, a global bound outside the disk, a characterization of all finite-\(R\) optimizers, or a claim about jointly combined rather than separately observed spectrogram channels. \(R\) tends to infinity; the Hermite orders remain fixed.

## Proof

**1. Radial Fourier reduction.** The standard Hermite ambiguity identity above reduces the squared norm of the vector-valued multiplier at normalized radius \(x\) to \(\sum_{j=0}^2w_j\phi_j(x)\), where \(\phi_j(x)=e^{-x}L_j(x)^2\). Continuity on the closed disk makes its minimum the lower squared singular multiplier bound. The compact simplex of \(w\)'s guarantees a maximizer for each positive \(R\).

**2. A two-node covering linear program.** The roots of \(L_2\) are precisely \(r_-\) and \(r_+\). For \(R>r_+\), let \(t=\min_{[0,R]}\sum_jw_j\phi_j\). At the two roots,
\[
\begin{pmatrix}e^{-r_-}&pe^{-r_-}\\e^{-r_+}&qe^{-r_+}\end{pmatrix}
\binom{w_0}{w_1}\geq t\binom11.
\]
The optimal nonnegative covering vector for unit right-hand side is \((\alpha_0,\alpha_1)\), with both rows active. Indeed its entries above solve the two equalities, and the strictly positive dual vector
\[
\binom{y_-}{y_+}=
\binom{e^{r_-}(q-1)/(q-p)}{e^{r_+}(1-p)/(q-p)}
\]
satisfies \(A^{\mathsf T}y=(1,1)^{\mathsf T}\) and \(y_-+y_+=C\). Thus every feasible \((w_0,w_1)\) obeys
\[
w_0+w_1\geq Ct.
\]
Strict positivity of \(\alpha_1\) is immediate. For \(\alpha_0\), the inequality \(qe^{r_-}>pe^{r_+}\) follows from \(e^{2\sqrt2}<q/p=q^2\), equivalently \(\sqrt2<\log q=2\operatorname{arsinh}(1)\); the last strict inequality follows by integrating \((1+t^2)^{-1/2}>1/\sqrt2\) over \(0\leq t<1\). Strict positivity of both dual entries is equivalent to \(p<1<q\). The dual is strictly positive and the node matrix invertible, so the unit covering minimizer is unique.

**3. Upper bound to second order.** Put \(F=F_R=\phi_2(R)\), \(s=w_0+w_1\), and
\[
\delta_R=\frac{\max\{\phi_0(R),\phi_1(R)\}}{F_R}
=\frac{\max\{1,(1-R)^2\}}{(1-2R+R^2/2)^2}=O(R^{-2}).
\]
For sufficiently large \(R\), \(\delta_R<1\). Evaluation at the disk boundary, combined with the covering inequality, gives
\[
t\leq F_R[1-(1-\delta_R)s]\leq F_R[1-(1-\delta_R)Ct],
\]
so
\[
M_3(R)\leq\frac{F_R}{1+(1-\delta_R)CF_R}
=F_R-CF_R^2+o(F_R^2).
\]
This is an upper bound on all nonnegative normalized allocations, not merely a test family.

**4. Matching feasible lower bound.** Write \(\varepsilon=F_R\to0\) and select
\[
w_0=(1+\sqrt\varepsilon)\alpha_0\varepsilon,\qquad
w_1=(1+\sqrt\varepsilon)\alpha_1\varepsilon,\qquad
w_2=1-C\varepsilon(1+\sqrt\varepsilon).
\]
These shares are nonnegative and sum to one for all sufficiently large \(R\). Let \(\phi=\phi_2\), and \(g=\alpha_0\phi_0+\alpha_1\phi_1\). The allocation's squared multiplier equals
\[
[1-C\varepsilon(1+\sqrt\varepsilon)]\phi(x)
+\varepsilon(1+\sqrt\varepsilon)g(x).
\]
On the fixed compact interval \([0,7]\), the only zeros of \(\phi\) are the two simple zeros of \(L_2\), hence quadratic zeros of \(\phi\). At each such root \(r\), \(g(r)=1\). Locally, \(\phi(x)\geq c_r(x-r)^2\) and \(g(x)\geq1-B_r|x-r|\). Completing the square gives a local minimum at least \(\varepsilon(1+\sqrt\varepsilon)-O(\varepsilon^2)>\varepsilon\). On the compact complement of small root neighborhoods \(\phi\) has a positive lower bound, so the same conclusion holds globally on \([0,7]\) for sufficiently small \(\varepsilon\). For \(x\geq7\), all three \(\phi_j\) are strictly decreasing: \(\phi_0'\!<0\), \(\phi_1'\!<0\) for \(x>3\), and \(\phi_2'\!<0\) for \(x>4+\sqrt6\). Hence on \([7,R]\) the candidate's minimum is at \(R\), where its value is
\[
\varepsilon[1-C\varepsilon(1+\sqrt\varepsilon)]
+\varepsilon(1+\sqrt\varepsilon)e^{-R}[\alpha_0+\alpha_1(1-R)^2]
=\varepsilon-C\varepsilon^2+o(\varepsilon^2).
\]
This endpoint is smaller than \(\varepsilon\) for all sufficiently large \(R\), proving a global matching lower bound. Together with Step 3 this proves the value asymptotic.

**5. All optimal allocations have the same asymptotic split.** For any maximizing \(w(R)\), write \(t=M_3(R)\), \(s=w_0+w_1\). Step 3's boundary inequality and the sharp value asymptotic imply
\[
s\leq\frac{F_R-t}{F_R(1-\delta_R)}=CF_R+o(F_R).
\]
The node inequalities imply \(A(w_0/F_R,w_1/F_R)^{\mathsf T}\geq(t/F_R)(1,1)^{\mathsf T}\), with \(t/F_R\to1\). Every subsequential limit of the bounded vectors \((w_0/F_R,w_1/F_R)\) therefore solves the unit covering program with cost at most \(C\). Step 2 gives its unique solution \((\alpha_0,\alpha_1)\). Thus the entire family converges to this pair, and \(w_2\to1\).

## Verification

The accompanying `verify.py` is a standalone Python 3 script using only the standard library. Running `python verify.py` checked the root identities, strict primal/dual positivity, normalized allocations, numerical global minima via stationary-point bracketing, and finite-radius endpoint inequalities; **844 numerical assertions passed**. Tests at \(R=12,14,16,18,20,22,24,27,30,34\) corroborated the asymptotic behavior. The proof above is analytical; numerical tests are not offered as a certificate of infinitely many radii or uniqueness at every finite radius.

## Relationship to prior work

Hermite-window STFT and Fock-space theory supply the classical ambiguity/Laguerre multiplier identity. Grohs–Liehr–Rathmair (2022) analyze phaseless lattice sampling with multiple Hermite-based windows, a distinct nonlinear injectivity problem rather than the present radius-dependent linear minimax conditioning problem. Fulsche–Hagger (2023) identify Laguerre zero circles and operator-quantization kernels; their zero-set results motivate the need to cover both zeros of the second Laguerre polynomial but do not prescribe optimal positive precision shares. Sandsten–Reinhold–Starkhammar (2017) optimize Hermite multitapers for approximate Wigner-distribution visualization and concentration, not the worst-case ambiguity multiplier on an expanding disk. Ydreskog (2023) optimizes multitaper spectrogram weights by other criteria, including least-squares approximation of a Wigner distribution; only its institutional abstract could be assessed, and the full thesis may contain further relevant material. A distinct two-Hermite radius optimization does not determine the simultaneous two-zero covering constant proved here.

## Limitations

The result is restricted to exactly three **separately observed** Hermite windows of orders \(0,1,2\), a normalized total precision budget, radial disk restriction, and the large-\(R\) regime. It is not an exact finite-radius phase diagram and does not assert phase retrieval for arbitrary signals from sampled spectrograms. Literature searches and inspected full texts did not identify the precise second-order law, but cannot establish global priority; the complete text of a closely related 2023 multitaper thesis was not accessible in this assessment.

## References

1. P. Grohs, L. Liehr, M. Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620, first submitted 2022-07-21. https://arxiv.org/abs/2207.10620
2. R. Fulsche, R. Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces*, arXiv:2308.11292, first submitted 2023-08-22, especially Section 3 and Theorem 3.4. https://arxiv.org/abs/2308.11292
3. M. Sandsten, I. Reinhold, J. Starkhammar, *Automatic Time-Frequency Analysis of Echolocation Signals Using the Matched Gaussian Multitaper Spectrogram*, Interspeech 2017, pp. 3048–3052, Section 2. https://www.isca-archive.org/interspeech_2017/sandsten17_interspeech.pdf
4. M. Ydreskog, *Optimal Multitaper Spectrograms*, Lund University Master's thesis, 2023, institutional record and abstract. https://lup.lub.lu.se/student-papers/record/9116759
