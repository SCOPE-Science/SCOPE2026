# A hidden logarithmic variance deficit under alternating elephant-walk memory

## Finding
Consider the full-memory elephant random walk with symmetric first step and deterministically alternating repetition probabilities. For every real \(\delta\in[-1,1]\), let \(X_1\) equal \(+1\) or \(-1\) with probability \(1/2\) each. At time \(n\ge1\), independently choose \(U_n\) uniformly from \(\{1,\ldots,n\}\), and a sign \(\varepsilon_n\in\{-1,+1\}\) with
\[
\Pr(\varepsilon_n=+1)=\frac{1+\delta(-1)^n}{2},\qquad
X_{n+1}=\varepsilon_nX_{U_n},\qquad S_n=\sum_{j=1}^nX_j.
\]
All random choices at each step are conditionally independent of the past, except through the selected previous increment.

**Theorem.** There is a finite real constant \(C_\delta\) for each \(\delta\in[-1,1]\), such that as integers \(m\to\infty\),
\[
\begin{aligned}
\operatorname{Var}(S_{2m})&=2m-2\delta^2\log m+C_\delta+O_\delta\!\left(\frac{\log m}{m}\right),\\
\operatorname{Var}(S_{2m+1})&=2m+1-2\delta^2\log m+C_\delta+2\delta+O_\delta\!\left(\frac{\log m}{m}\right).
\end{aligned}
\]
In particular, the logarithmic correction is always negative for \(\delta\ne0\), independent of which parity is positively reinforced, and
\[
\lim_{n\to\infty}\frac{n-\operatorname{Var}(S_n)}{\log n}=2\delta^2,
\qquad
\lim_{m\to\infty}\bigl[\operatorname{Var}(S_{2m+1})-\operatorname{Var}(S_{2m})\bigr]=1+2\delta.
\]
At \(\delta=0\) the walk is an ordinary simple symmetric random walk and \(\operatorname{Var}(S_n)=n\) exactly. Nevertheless, for every \(\delta\in[-1,1]\) and fixed \(T>0\), the entire rescaled path satisfies
\[
\bigl(N^{-1/2}S_{\lfloor Nt\rfloor}\bigr)_{0\le t\le T}
\ \Longrightarrow\ (B_t)_{0\le t\le T}
\quad\text{in }D([0,T])\text{ with the }J_1\text{ topology},
\]
where \(S_0=0\), \(B\) is standard Brownian motion, and \(N\to\infty\) through integers. Thus the alternating memory is invisible in the first-order functional diffusion limit but leaves an exact logarithmic and parity-resolved signature in the variance.

## Assumptions and scope
The memory index is uniform over the **complete** set of previous increments; no age bias, amnesia, delayed memory, random step size or spatially periodic lattice is allowed. The sign probabilities are deterministic and period two, alternating around \(1/2\), with the indexing shown above; both extreme values \(\delta=\pm1\) are included. The initial sign is fair. The conclusions are for the infinite sequence under a single fixed \(\delta\); the remainder does not assert uniformity in varying \(\delta\).

## Proof
**1. Exact one- and two-step moment recurrences.** Let \(\mathcal F_n=\sigma(X_1,\ldots,X_n)\) and write \(a_n=\delta(-1)^n\). Since the selected increment is uniform over the full past,
\[
\mathbb E[X_{n+1}\mid\mathcal F_n]=\frac{a_n}{n}S_n,
\qquad
\mathbb E[S_{n+1}\mid\mathcal F_n]=\left(1+\frac{a_n}{n}\right)S_n.
\]
The fair first sign and the recursion give \(\mathbb E S_n=0\) for every \(n\). As \(X_{n+1}^2=1\), writing \(v_n=\operatorname{Var}(S_n)=\mathbb E S_n^2\) yields the *exact* identity
\[
v_1=1,\qquad v_{n+1}=\left(1+\frac{2a_n}{n}\right)v_n+1.\tag{1}
\]
In particular \(v_2=2-2\delta\). Pair the updates at even time \(2m\) and odd time \(2m+1\). With \(y_m=v_{2m}\), direct multiplication in (1) gives
\[
y_{m+1}=\left(1+\frac{\delta(1-2\delta)}{m(2m+1)}\right)y_m+2-\frac{2\delta}{2m+1}.\tag{2}
\]
Set \(z_m=y_m-2m\), \(\kappa=\delta(1-2\delta)\). Equation (2) simplifies exactly to
\[
z_1=-2\delta,\qquad
z_{m+1}=\left(1+\frac{\kappa}{m(2m+1)}\right)z_m-\frac{4\delta^2}{2m+1}.\tag{3}
\]
The factor in parentheses is nonnegative: it equals \(1+\delta/m)(1-2\delta/(2m+1)\), vanishing only at \(m=1,\delta=-1\). Strict positivity is not needed: the absolute-product bound below also covers this endpoint.

**2. Exact logarithmic coefficient, constants, and remainder.** By (3), \(|\kappa/[m(2m+1)]|=O_\delta(m^{-2})\) and the forcing is \(O_\delta(m^{-1})\). Iteration with the bounded product \(\prod_{j\ge1}(1+|\kappa|/[j(2j+1)])\) proves \(z_m=O_\delta(1+\log m)\). Define
\[
w_m=z_m+2\delta^2\log m.
\]
Subtracting adjacent terms using (3),
\[
w_{m+1}-w_m=
\frac{\kappa z_m}{m(2m+1)}
+2\delta^2\left(\log(1+1/m)-\frac{2}{2m+1}\right)
=O_\delta\!\left(\frac{1+\log m}{m^2}\right).\tag{4}
\]
The expression in parentheses is \(O(m^{-2})\) by the Taylor expansion of the logarithm. The series of absolute differences in (4) converges, so \(w_m\to C_\delta\in\mathbb R\). Its tail is bounded by \(O_\delta((1+\log m)/m)\). This proves the even-time assertion. The first update after even time is
\[
v_{2m+1}=\left(1+\frac{\delta}{m}\right)v_{2m}+1
=2m+1+2\delta+z_m+\frac{\delta z_m}{m},
\]
which yields the odd-time assertion. The limits and the \(\delta=0\) identity follow immediately.

**3. Full Brownian functional limit.** Start normalization at time two to include the extreme parameter \(\delta=1\), at which the first multiplier would vanish. Put \(g_2=1\) and
\[
g_{n+1}=g_n\left(1+\frac{a_n}{n}\right),\qquad n\ge2.
\]
All factors are strictly positive. Since \(\sum_{n\ge2}a_n/n=\delta\sum_{n\ge2}(-1)^n/n\) converges and \(\sum_n n^{-2}<\infty\), the logarithmic product converges: \(g_n\to g_\infty\in(0,\infty)\). It follows that \(g_n\) and \(g_n^{-1}\) are uniformly bounded for \(n\ge2\). The process \(M_n=S_n/g_n\), \(n\ge2\), is a square-integrable martingale with increments
\[
M_{n+1}-M_n=\frac{X_{n+1}-a_nS_n/n}{g_{n+1}},\qquad
\mathbb E[(M_{n+1}-M_n)^2\mid\mathcal F_n]
=\frac{1-\delta^2 S_n^2/n^2}{g_{n+1}^2}.\tag{5}
\]
The increments in (5) are uniformly bounded. Part 2 gives \(\mathbb E S_n^2=n+O_\delta(\log n)\), so for every fixed \(T>0\),
\[
\frac1N\sum_{n=2}^{\lfloor NT\rfloor}\mathbb E\frac{S_n^2}{n^2}
=O_\delta\!\left(\frac{\log N}{N}\right)\longrightarrow0.
\]
Consequently the predictable quadratic variation of \(N^{-1/2}M_{\lfloor Nt\rfloor}\) converges uniformly in probability on \([0,T]\) to \(t/g_\infty^2\). The bounded increments give conditional Lindeberg automatically, and the martingale functional central limit theorem gives \(N^{-1/2}M_{\lfloor Nt\rfloor}\Rightarrow g_\infty^{-1}B_t\). The deterministic factors \(g_{\lfloor Nt\rfloor}\) converge uniformly to \(g_\infty\) on every interval \([\epsilon,T]\). At the origin, Doob's inequality and bounded martingale differences imply
\[
\limsup_{N\to\infty}\mathbb E\left[\max_{2\le k\le\lfloor N\epsilon\rfloor}\frac{|S_k|^2}{N}\right]\le C_\delta\epsilon,
\]
with the finitely many initial indices negligible. Letting \(\epsilon\downarrow0\) extends the convergence to \([0,T]\), proving the functional limit and finishing the theorem.

## Verification
Run `python3 verify.py` from the directory containing this file and the standalone verifier. It requires only the Python standard library. Recorded output: `PASS: 322 exact-rational/numerical assertions`. The checker independently constructs exact finite-step laws for seven rational parameters, verifies the one- and two-step identities, compares variance log-slopes over separated large index ranges, and tests Brownian-scale covariance. Exact finite enumeration and numerical convergence diagnostics do **not** prove infinite-time limits; steps 2 and 3 supply those proofs.

## Relationship to prior work
Fan and Qi (2026, arXiv:2610.16065v1) introduce complete-memory elephant walks with arbitrary time-varying repetition probabilities and prove broad scalar central limit, law-of-the-iterated-logarithm, and martingale normalization theorems. Their framework contains this alternating model. The specific period-two variance recurrence (3), universal negative \(-2\delta^2\log m\) correction, finite parity constant gap, and their coexistence with the path-level Brownian limit are the results addressed here; no claim is made that the conditional expectation or martingale normalization is new.

Schütz and Trimper's constant-probability elephant model and classical functional limit results (including Coletti, Gava and Schütz) cover the nonalternating case. Gut and Stadtmüller's restricted-memory variations concern which past increments are sampled, not the alternating repetition law with complete memory. Shibata's periodic-structure functional limits vary the underlying spatial lattice, not the temporal repetition probability. These distinctions do not constitute a proof of worldwide priority, and a more general unpublished or unlocated second-order theorem remains possible.

## Limitations
The exact logarithmic coefficient assumes period-two complementary repetition probabilities and fair initial sign; generic periodic patterns, random environments, and nonuniform memory selection are not analyzed. The bounded remainder constant \(C_\delta\) is characterized by a convergent limit, not evaluated in elementary closed form. The Brownian functional limit by itself would not identify the logarithmic term; the result is not a quantitative distributional approximation or a local limit theorem. No independent mathematical audit has been performed.

## References
- X. Fan and Y. Qi, *A Generalized Elephant Random Walk with Time-Dependent Memory*, arXiv:2610.16065v1, first submitted 2026-10-12, https://arxiv.org/abs/2610.16065.
- G. M. Schütz and S. Trimper, *Elephants can always remember: Exact long-range memory effects in a non-Markovian random walk*, Physical Review E 70 (2004), 045101, https://doi.org/10.1103/PhysRevE.70.045101.
- C. F. Coletti, R. Gava and G. M. Schütz, *A strong invariance principle for the elephant random walk*, arXiv:1707.06905, https://arxiv.org/abs/1707.06905.
- A. Gut and U. Stadtmüller, *Variations of the elephant random walk*, Journal of Applied Probability 58 (2021), 805–829, arXiv:1812.01915, https://arxiv.org/html/1812.01915v1.
- S. Shibata, *Functional limit theorems for elephant random walks on general periodic structures*, arXiv:2511.10347, https://arxiv.org/abs/2511.10347.
- P. Hall and C. C. Heyde, *Martingale Limit Theory and Its Application*, Academic Press, 1980 (standard martingale limit theory).
