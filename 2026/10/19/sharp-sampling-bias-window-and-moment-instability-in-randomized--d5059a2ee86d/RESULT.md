# Sharp sampling-bias window and moment instability in randomized absolute-value equations

## Finding
Consider the row-sampled generalized absolute-value equation (GAVE) iteration defined below. For every \(0<c<1\), every deterministic \(x_0\ne0\), and every row-one probability \(0<p<1\), the exact almost-sure logarithmic growth rate is
\[
\gamma_c(p)=\log(1+c)-2p(1-p)\log\frac{1+c}{1-c}.
\]
Set
\[
\delta_c=\sqrt{\frac{-\log(1-c^2)}{\log((1+c)/(1-c))}},\qquad p_\pm(c)=\frac{1\pm\delta_c}{2}.
\]
The iterates converge exponentially to the unique solution \(0\) almost surely **exactly when** \(p_-(c)<p<p_+(c)\). Outside the closed interval, their magnitudes diverge exponentially almost surely. At either boundary \(p=p_\pm(c)\), the iterates satisfy \(\liminf_k|x_k|=0\) and \(\limsup_k|x_k|=\infty\) almost surely.

For each real moment order \(s>0\), the exact exponential growth factor of \(\mathbb E|x_k|^s\) is
\[
\rho_s(p)=\frac{a_s+\sqrt{a_s^2(2p-1)^2+4p(1-p)b_s^2}}2,\quad a_s=(1+c)^s,\quad b_s=(1-c)^s.
\]
For all \(p\ne1/2\), the first absolute moment grows exponentially, and for **every** \(p\in(0,1)\), the second moment grows exponentially, even throughout the almost-sure convergence window. At fair sampling, \(\mathbb E|x_k|=|x_0|\) for all \(k\), but \(|x_k|\to0\) almost surely: the absolute error is a nonnegative, non-uniformly-integrable martingale. More generally, each probability in the strict almost-sure stability window has a unique critical moment order \(s_*(p)\in(0,1]\): moments below it decay, at it remain bounded away from both zero and infinity, and above it grow exponentially. The stable sampling-window width is \(p_+(c)-p_-(c)\sim\sqrt{c/2}\) as \(c\downarrow0\).

## Assumptions and scope
Let \(0<c<1\), \(\alpha=1-c\), and \(\beta=1/(1-c)\). Consider the consistent real nonsquare GAVE \(Ax-B|x|=0\), with
\[
A=\begin{pmatrix}1\\1\end{pmatrix},\qquad B=\begin{pmatrix}\beta\\-\beta\end{pmatrix},\qquad x\in\mathbb R.
\]
This equation has the unique solution \(x=0\), since for any \(x\ne0\) the two residuals cannot simultaneously vanish. Starting from any deterministic \(x_0\ne0\), apply independent row choices \(S_k=e_1\) with probability \(p\) and \(S_k=e_2\) with probability \(1-p\), using the GAVE randomized iteration
\[
x_{k+1}=x_k-\alpha\frac{A^\top S_k S_k^\top(Ax_k-B|x_k|)}{\|S_k^\top A\|_2^2}.
\]
Both row denominators equal one. Therefore \(x_{k+1}=c x_k+\varepsilon_{k+1}|x_k|\), with independent signs \(\Pr(\varepsilon_j=1)=p\). All probabilities and moments refer to these independent row choices; no finite-precision or additive-noise claim is made. The term *almost-sure logarithmic rate* means \(\lim_{k\to\infty}k^{-1}\log(|x_k|/|x_0|)\).

## Proof
**1. Sign-reset representation and exact Lyapunov exponent.** Since \(0<c<1\), the update never vanishes for nonzero input, and its sign is exactly \(\varepsilon_{k+1}\). Set \(a=1+c>1\), \(b=1-c\in(0,1)\). For \(j\ge2\), the absolute multiplier is \(a\) if \(\varepsilon_j=\varepsilon_{j-1}\), and \(b\) otherwise. The first multiplier is \(a\) or \(b\) according to whether \(\varepsilon_1\) matches the deterministic sign of \(x_0\). Hence
\[
\log\frac{|x_k|}{|x_0|}=O(1)+\sum_{j=2}^{k}\big[\mathbf1_{\varepsilon_j=\varepsilon_{j-1}}\log a+\mathbf1_{\varepsilon_j\ne\varepsilon_{j-1}}\log b\big].
\]
The indicator sequence is stationary and one-dependent; the subsequences at even and odd indices are individually iid. Applying the strong law to each gives same-label frequency \(p^2+(1-p)^2\) and switching frequency \(2p(1-p)\), proving the displayed \(\gamma_c(p)\). Solving \(\gamma_c(p)<0\) gives the stated open interval, since \(\gamma_c(p)=\log a-2p(1-p)\log(a/b)\), and \(0<\delta_c<1\). The strict-sign conclusions follow by exponentiating the almost-sure limit. As \(c\downarrow0\), elementary logarithmic expansions yield \(\delta_c^2\sim c/2\).

**2. Both critical boundaries oscillate without bound.** Fix \(p\in(0,1)\) with \(\gamma_c(p)=0\). Starting from the first appearance of a \(+\) sign, consider successive return times of the iid sign sequence to \(+\). Their lengths \(N_i\) are iid geometric with success parameter \(p\). The log-magnitude reward for a return cycle is \(Z_i=\log a\) when \(N_i=1\), and \(Z_i=2\log b+(N_i-2)\log a\) when \(N_i\ge2\). They are iid, have finite nonzero variance (the \(N_i=1\) and \(N_i=2\) rewards are distinct), and renewal reward counting yields \(\mathbb E Z_i=\gamma_c(p)\mathbb E N_i=0\). The centered, nondegenerate iid random walk \(\sum_{i\le n}Z_i\) has almost surely unbounded positive and negative limsups (for example by the law of the iterated logarithm). Since these sums are the exact log magnitudes at return times, the stated liminf and limsup follow for the full sequence.

**3. Moment transfer matrix.** Put \(v_k^+=(\mathbb E|x_k|^s\mathbf1_{x_k>0})\), \(v_k^-=(\mathbb E|x_k|^s\mathbf1_{x_k<0})\). Conditioning on the current sign and the independent next row gives the exact identity
\[
\begin{pmatrix}v_{k+1}^+\\v_{k+1}^-\end{pmatrix}=
\underbrace{\begin{pmatrix}p a^s&p b^s\\(1-p)b^s&(1-p)a^s\end{pmatrix}}_{M_s(p)}
\begin{pmatrix}v_k^+\\v_k^-\end{pmatrix}.
\]
For \(0<p<1\), \(M_s(p)\) is strictly positive. Its characteristic polynomial gives the displayed Perron root \(\rho_s(p)\); the other eigenvalue is strictly smaller in modulus. Perron–Frobenius theory then implies \(\mathbb E|x_k|^s=C_s\rho_s(p)^k(1+o(1))\) with \(C_s>0\) for every deterministic nonzero initialization. If \(s=1\), evaluating the characteristic polynomial at \(1\) gives \(c[4p(1-p)-1]\le0\), with equality exactly at \(p=1/2\). Thus \(\rho_1(p)\ge1\), strictly except at fair sampling. For \(s=2\), the displayed Perron root is minimized at \(p=1/2\), where \(\rho_2=(a^2+b^2)/2=1+c^2>1\).

**4. Complete moment frontier.** Define \(f(s)=\log\rho_s(p)\) for \(s\ge0\). For each integer \(k\), the function \(k^{-1}\log(\mathbb E|x_k|^s/|x_0|^s)\) is convex by Hölder; its pointwise limit \(f\) is therefore convex. Moreover \(f(0)=0\), and differentiating the simple Perron eigenvalue of \(M_0(p)\) gives \(f'(0)=\gamma_c(p)\). Finally \(\rho_s(p)\ge p(1+c)^s\to\infty\), so \(f(s)\to\infty\). Strict convexity for \(s>0\) follows from the nonzero asymptotic variance of the log multipliers (equivalently the positive variance of nondegenerate return-cycle rewards), or directly by differentiating the Perron root. In the stable window, \(f'(0)<0\), so the continuous strictly convex function has precisely one positive zero \(s_*(p)\). The preceding first-moment classification shows \(0<s_*(p)\le1\), with equality only when \(p=1/2\). The Perron asymptotic proves all three moment regimes. At fair sampling, direct conditional expectation gives \(\mathbb E(|x_{k+1}|\mid x_k)=|x_k|\); hence \(|x_k|\) is a nonnegative martingale. Its almost-sure limit is zero by Step 1, but its expectation stays \(|x_0|>0\), so it is not uniformly integrable. Also \(\mathbb E(x_{k+1}\mid x_k)=c x_k\) and \(\mathbb E(x_{k+1}^2\mid x_k)=(1+c^2)x_k^2\), proving the exact signed and quadratic formulas.

## Verification
Run `python3 verify.py` using Python standard library only. The included `verification.log` records 1,371 passed deterministic assertions: direct reproduction of the GAVE update, sign-reset paths, exact finite-string probabilities, matrix moment identities, phase roots, fair first and second moments, and the square-root small-step window. The numerical tests check the algebraic identities but are **not** offered as infinite-time proof; Steps 1–4 supply the infinite-time arguments. For \(c=1/2\), the stable probability interval is approximately \((0.244138950237,0.755861049763)\), and fair-sampling first and second absolute moment factors are \(1\) and \(5/4\), respectively.

## Relationship to prior work
Xie, Qi and Han (arXiv:2405.04091, first made public 2024-05-07) introduce the exact nonsquare GAVE randomized iteration studied here, with user-selected row probabilities, solvability bounds and general sufficient convergence theorems. Their Sections 4 and 5.3 are the relevant sources for the algorithm and randomized Kaczmarz specialization. Those theorems supply general sufficient hypotheses rather than the exact biased-row almost-sure phase diagram, critical boundary oscillation, Perron moment spectrum or a fair-sampling non-uniformly-integrable martingale for the present two-row sign-reset family. Classical scalar random-product and finite-state Markov-additive arguments provide proof mechanisms and do not by themselves identify the claimed GAVE parameter window. This is a method-specific example, not a new general random-product theorem.

## Limitations
The statement is exact for one scalar unknown, two specific GAVE residual rows, constant relaxation \(0<\alpha<1\), independent row sampling and exact arithmetic. It does not claim that the source paper's sufficient conditions are necessary, nor that the same phase diagram holds for arbitrary GAVE systems, dependent sampling or other algorithms. At \(p=0\) or \(p=1\), omitted from the main moment-matrix statement, repeated selection of one row gives deterministic exponential growth after a possible first transient. Nonlinear sign-reset systems have been studied in broader random dynamical systems; priority against an equivalent prior closed-form calculation cannot be established conclusively by finite literature searches.

## References
1. J. Xie, H.-D. Qi and D. Han, *Randomized iterative methods for generalized absolute value equations: Solvability and error bounds*, arXiv:2405.04091, first submitted 2024-05-07. https://arxiv.org/abs/2405.04091 ; full text https://arxiv.org/html/2405.04091v3 .
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM Journal on Matrix Analysis and Applications 36 (2015), 1660–1690, arXiv:1506.03296. This describes the linear \(B=0\) antecedent, not sign-dependent GAVE dynamics.
