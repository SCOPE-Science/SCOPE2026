# Logarithmic Fisher information and pathwise local asymptotic normality for the discrete Poisson staircase

## Finding

Consider the discrete Poisson staircase of Yoshida [1], observed at every integer time from \(0\) through \(n\). Its transition law, with unknown parameter \(p\in(0,1)\), is
\[
 X_0=1,\qquad
 X_i=\begin{cases}
 X_{i-1}U_i,&\text{with probability }pX_{i-1},\\
 X_{i-1},&\text{otherwise},
 \end{cases}
\]
where the jump multipliers are independent uniform random variables on \((0,1)\). Set \(J_i=\mathbf1\{X_i<X_{i-1}\}\), \(N_n=\sum_{i=1}^nJ_i\), and let \(I_n^{\mathrm{path}}(p)\) be the Fisher information for \(p\) in the entire observed path \((X_0,\ldots,X_n)\). Let \(I_n^{\mathrm{end}}(p)\) denote the information in \(X_n\) alone.

**Theorem.** For every fixed \(p\in(0,1)\),
\[
 \lim_{n\to\infty}\frac{p^2 I_n^{\mathrm{path}}(p)}{\log n}=1,
 \qquad \lim_{n\to\infty}p^2 I_n^{\mathrm{end}}(p)=1.
\]
The path experiment is locally asymptotically normal with local parameterization \(p_{n,h}=p(1+h/\sqrt{\log n})\): for each fixed \(h\in\mathbb R\),
\[
 \log\frac{dP_{p_{n,h}}^{(n)}}{dP_p^{(n)}}
 =h\Delta_n-\tfrac12h^2+o_{P_p}(1),
 \qquad \Delta_n\Longrightarrow N(0,1).
\]
With probability tending to one, the unconstrained likelihood on \(0<p<1\) has a unique interior maximizer \(\widehat p_n\), and
\[
 \frac{\sqrt{\log n}}p(\widehat p_n-p)\Longrightarrow N(0,1).
\]
Thus the full trajectory has \(\log n\) times as much first-order information as its endpoint, and the maximum-likelihood estimator attains the LAN information bound.

## Assumptions and scope

The parameter \(p\) is deterministic, fixed strictly inside \((0,1)\); all states are observed without error and at unit time intervals, including repeated unchanged values. The support of the transition kernel does not depend on \(p\). The parameter \(p=1\), censored observation, and unknown starting states are not covered. Relative likelihoods use the natural mixed dominating transition measure: Lebesgue measure for a strict decrease and a point mass for an unchanged state.

## Proof

**1. Pathwise record coupling and jump counts.** Let \(V_1,V_2,\ldots\) be independent \(\operatorname{Uniform}(0,1)\) variables. Put \(Y_0=p\) and \(Y_i=\min\{p,V_1,\ldots,V_i\}\), and set \(X_i=Y_i/p\). Conditional on \(Y_{i-1}=y\), the next minimum decreases with probability \(y=pX_{i-1}\), and, given a decrease, the next value is uniform on \((0,y)\). This constructs exactly the stated transition kernel.

Let \(R_i=\mathbf1\{V_i=\min(V_1,\ldots,V_i)\}\) be ordinary lower-record indicators. Their insertion ranks are mutually independent and uniform on \(\{1,\ldots,i\}\), so the \(R_i\) are independent Bernoulli variables with means \(1/i\). The first \(T=\inf\{i:V_i<p\}\) is geometric with success probability \(p\), hence finite almost surely with all moments finite. For every \(i\ge T\), \(J_i=R_i\), and before \(T\), \(J_i=0\). Consequently \(|N_n-\sum_{i=1}^nR_i|\le T-1\) for all \(n\). Independence of the records proves \(N_n/\log n\to1\) almost surely and in \(L^2\).

For every \(i\ge0\), \(P(Y_i>y)=(1-y)^i\) for \(0\le y<p\). Thus
\[
 E_p Y_i=\frac{1-(1-p)^{i+1}}{i+1},\quad
 E_pY_i^2=2\int_0^p y(1-y)^i\,dy\le\frac{2}{(i+1)(i+2)}.
\]
In particular, \(\sum_iY_i^2<\infty\) almost surely and in expectation. The exact jump-count expectation is
\[
 E_pN_n=\sum_{j=1}^n\frac{1-(1-p)^j}{j}
 =H_n+\log p+o(1)=\log n+\gamma+\log p+o(1).
\]

**2. Likelihood and information.** Conditional on a preceding state \(x\), a strict jump to \(y\in(0,x)\) has density \(p\,dy\), whereas remaining at \(x\) has probability \(1-px\). Hence the log likelihood, up to a parameter-free term, is
\[
 \ell_n(p)=N_n\log p+\sum_{i:J_i=0}\log(1-pX_{i-1}).
\]
Its score is the martingale
\[
 S_n(p)=\sum_{i=1}^n\left(\frac{J_i}{p}
 -\frac{(1-J_i)X_{i-1}}{1-pX_{i-1}}\right),
\]
whose conditional increments have mean zero and conditional variance
\[
 \frac{X_{i-1}}{p(1-pX_{i-1})}
 =\frac{Y_{i-1}}{p^2(1-Y_{i-1})}.
\]
Therefore the exact full-path Fisher information is
\[
 I_n^{\mathrm{path}}(p)=\frac1{p^2}\sum_{i=0}^{n-1}
 E_p\left[\frac{Y_i}{1-Y_i}\right].
\]
The difference between the summand and \(E_pY_i\) is at most \(E_pY_i^2/(1-p)\), whose sum is bounded uniformly in \(n\). Hence
\[
 p^2 I_n^{\mathrm{path}}(p)=E_pN_n+O_p(1)=\log n+O_p(1).
\]
Here \(O_p(1)\) in this expectation identity means a deterministic constant depending on the fixed parameter \(p\), not the stochastic order notation.

Let \(A_n=\sum_{i=0}^{n-1}Y_i\). Since \(N_n-A_n\) is a martingale of second moment at most \(E_pN_n=O(\log n)\), step 1 gives \(A_n/\log n\to1\) in probability. Because \(\sum_iY_i^2<\infty\), its score-bracket satisfies
\[
 \frac{p^2\langle S\rangle_n}{\log n}
 =\frac1{\log n}\sum_{i=0}^{n-1}\frac{Y_i}{1-Y_i}
 \longrightarrow1\quad\text{in probability}.
\]
For fixed \(p\in(0,1)\), score increments are uniformly bounded by \(\max\{1/p,1/(1-p)\}\). The bounded-increment martingale central limit theorem yields
\(\Delta_n:=pS_n(p)/\sqrt{\log n}\Longrightarrow N(0,1)\).

**3. LAN and efficient maximum likelihood.** Differentiating again gives
\[
 -\ell_n''(p)=\frac{N_n}{p^2}
 +\sum_{i:J_i=0}\frac{X_{i-1}^2}{(1-pX_{i-1})^2}.
\]
The second sum is almost surely bounded uniformly in \(n\), since \(\sum_iX_i^2<\infty\) and \(p<1\). This bound also holds uniformly for parameters in any compact neighborhood of the true \(p\). Thus \(-\ell_n''(q)/(\log n)\to1/p^2\) in probability whenever \(q\to p\). Taylor's theorem at \(q=p(1+h/\sqrt{\log n})\) proves the asserted LAN expansion. Strict concavity of \(\ell_n\) whenever a jump occurs, combined with scores of opposite signs at \(p\pm M/\sqrt{\log n}\) with high probability for sufficiently large fixed \(M\), gives existence and uniqueness of an interior maximizer with probability tending to one. Taylor expansion of the zero-score equation yields its stated limiting normal law. The variance equals the inverse LAN information.

**4. Endpoint information.** The marginal law already derived in [1] has mass \((1-p)^n\) at \(x=1\) and density \(np(1-px)^{n-1}\) on \(0<x<1\). Its density score is
\[
 \frac1p-\frac{(n-1)x}{1-px},
\]
while its atom score is \(-n/(1-p)\). Under \(z=nx\), the continuous density converges to \(pe^{-pz}\), and its score converges to \(1/p-z\). For fixed \(p<1\), domination by a constant times \(e^{-pz/2}(1+z^2)\) proves convergence of the continuous Fisher-information integral to \(E[(1/p-Z)^2]=1/p^2\), where \(Z\sim\operatorname{Exp}(p)\). The atomic contribution is \(n^2(1-p)^{n-2}\to0\). This establishes the endpoint information limit and finishes the proof.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic to check 111 finite identities: the record-minimum jump expectation, its harmonic-sum expression, the squared-minimum bound, and score conditional centering/variance for several rational parameters. Deterministically seeded finite simulations additionally inspect the score and predictable bracket at two observation horizons. These experiments are finite consistency tests, not a proof of LAN or infinite-time assertions; the proof above supplies those steps.

## Relationship to prior work

Yoshida [1] introduced this discrete-time staircase and derived its transition kernel, marginal distribution, joint survival function, jump-count generating function, and certain state-function martingales. The present likelihood experiment starts from that kernel but asks a different question: estimation of its parameter from the entire trajectory. The logarithmic information law, its LAN limit, the efficient estimator, and the endpoint-versus-path information separation are not statements of [1]. The original continuous-time Poisson hyperbolic staircase [2] is a different observation model and does not imply the discrete-time likelihood result without additional analysis. Standard record-rank independence [3] is used as known input, not claimed new.

## Limitations

This is a first-order asymptotic inference result for an interior scalar parameter with a continuously observed discrete-time trajectory; it does not establish uniform local asymptotic normality as \(p\) approaches either endpoint, finite-sample risk optimality, robustness to observation noise, or behavior when only jump times (without jump heights) are observed. The numerical experiment is not exhaustive. Possible related results in general record-process inference are a remaining literature risk.

## References

[1] Naohiro Yoshida, *Poisson Hyperbolic Staircase in Discrete Time*, arXiv:2604.22637v1, first submitted 2026-04-24, https://arxiv.org/abs/2604.22637 . MSC2020 primary 60J05.

[2] Benny Levikson, Tomasz Rolski, and Gideon Weiss, *On a Poisson Hyperbolic Staircase*, Probability in the Engineering and Informational Sciences **13** (1999), 11–31, DOI 10.1017/S0269964899131024.

[3] B. C. Arnold, N. Balakrishnan, and H. N. Nagaraja, *Records*, Wiley, 1998 (classical insertion-rank representation of continuous i.i.d. records).
