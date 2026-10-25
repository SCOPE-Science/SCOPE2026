# Spatial Cesàro classification and quenched Gaussian limits for Pascal-sign bootstrap walks

## Finding

**Theorem (complete deterministic scenery criterion and Pascal-sign application).** Let \(\xi_1,\xi_2,\ldots\) be independent random signs with equal probabilities, and let a **fixed deterministic** sign sequence \(f:\mathbb N_0\to\{-1,1\}\) be given. Put
\[
 S_0=X_0=Y_0=0,\qquad S_n=\sum_{j=1}^n\mathbf1_{\{\xi_j=-1\}},\qquad
 X_n=\sum_{j=1}^n\xi_j,\qquad Y_n=\sum_{j=1}^n f(S_{j-1})\xi_j.
\]
For each \(\rho\in[-1,1]\), the following are equivalent:

1. The spatial averages \(A_N(f)=N^{-1}\sum_{s=0}^{N-1} f(s)\) converge to \(\rho\).
2. The linearly interpolated, diffusively rescaled pair \(n^{-1/2}(X_{\lfloor nt\rfloor},Y_{\lfloor nt\rfloor})\) converges weakly on every finite interval in the usual path topology to a Brownian pair with marginal variances \(t\) and covariance \(\rho t\). Using the step functions instead gives the same assertion in the Skorokhod topology.

In fact, for every fixed deterministic \(f\),
\[
 \frac{1}{n}\sum_{j=0}^{n-1}f(S_j)-A_{\lfloor n/2\rfloor}(f)
 \longrightarrow 0\quad\text{almost surely}.\tag{1}
\]
The first coordinate and second coordinate are independent in the Brownian limit exactly when the spatial average is zero. The boundary correlations \(\rho=1\) and \(\rho=-1\) are allowed and give degenerate Gaussian pairs.

**Pascal-sign consequence.** Let \(\beta_0,\beta_1,\ldots\) be independent Bernoulli variables, independent of the walk, and assume that for some \(0<\varepsilon\le1/2\) every parameter belongs to \([\varepsilon,1-\varepsilon]\). Define the random scenery
\[
 f_\beta(s)=(-1)^{\sum_{k=0}^s e(s,k)\beta_k},\qquad
 e(s,k)=\binom{s}{k}\bmod 2\in\{0,1\}.
\]
Then almost surely with respect to the coefficient law, \(A_N(f_\beta)\to0\), and for almost every fixed coefficient sequence the conditional walk law satisfies the functional limit above with \(\rho=0\). Therefore the limiting Brownian coordinates are independent. Changing finitely many initial recycled increments to match alternative bootstrap conventions does not affect this conclusion.

## Assumptions and scope

The deterministic classification uses only independent fair input signs and a fixed, bounded, \(\{-1,1\}\)-valued scenery evaluated at the **number of negative input steps so far**. No independence or stationarity assumption on the scenery is imposed. The random Pascal application adds independent coefficient bits with uniform nondegeneracy, but their success probabilities need not be equal. Every probability-one statement for the walk is with its coefficient scenery held fixed; it is not merely an averaged (annealed) assertion.

## Proof

**1. An occupation-time identity.** In an infinite input-sign sequence, define the holding time \(G_s\) at counting level \(s\) as the number of consecutive input steps for which the pre-increment count \(S_{j-1}=s\). It consists of a possibly empty string of positive steps followed by a negative step. The \(G_s\) are independent and identically distributed with
\[
 \Pr(G_s=k)=2^{-k},\quad k=1,2,\ldots,\qquad
 \mathbb E G_s=2,\quad\operatorname{Var}(G_s)=2.
\]
Set \(T_J=\sum_{s=0}^{J-1}G_s\), the time at which the count reaches level \(J\). The independent, centered, uniformly square-integrable variables
\(f(s)(G_s-2)\) satisfy
\(\sum_{s=1}^{\infty}\operatorname{Var}(f(s)(G_s-2))/s^2<\infty\). Kolmogorov's convergence criterion and Kronecker's lemma therefore yield
\[
 \frac1J\sum_{s=0}^{J-1} f(s)(G_s-2)\longrightarrow0
 \quad\text{almost surely}.\tag{2}
\]
The renewal strong law gives \(T_J/J\to2\), and the usual strong law for the input signs gives \(S_n/n\to1/2\). At time \(n\) the contributions of completed levels are exactly \(\sum_{s<S_n}G_s f(s)\), while the final level contributes between zero and \(G_{S_n}\) units in absolute value. Exponential tails for the geometric law and Borel–Cantelli imply \(G_J/J\to0\) almost surely; hence \(G_{S_n}/n\to0\). Combining these facts with (2) gives
\[
 \sum_{j=0}^{n-1} f(S_j)
 =2\sum_{s=0}^{S_n-1}f(s)+o(n)
 =2\sum_{s=0}^{\lfloor n/2\rfloor-1}f(s)+o(n)
 \quad\text{almost surely},
\]
because the absolute difference of the two partial sums is at most \(\lvert S_n-\lfloor n/2\rfloor\rvert=o(n)\). This proves (1), **for each fixed scenery**, regardless of whether its spatial averages converge.

**2. Gaussian sufficiency and necessity.** Each increment of \((X,Y)\) is \((\xi_j,f(S_{j-1})\xi_j)\), a bounded martingale difference for the input filtration, with predictable conditional covariance
\[
 \begin{pmatrix}1&f(S_{j-1})\\f(S_{j-1})&1\end{pmatrix}.
\]
If \(A_N(f)\to\rho\), equation (1), applied at each integer time \(\lfloor nt\rfloor\), gives predictable quadratic covariations converging to
\(t\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\). Their paths are uniformly Lipschitz after rescaling, so convergence is uniform over compact time intervals. The bounded jumps satisfy the martingale Lindeberg condition, and the martingale functional central limit theorem proves Gaussian convergence (including the singular cases \(\rho=\pm1\)).

Conversely, if the rescaled pair converges to a Brownian pair with covariance \(\rho t\), the necessary-and-sufficient bootstrap-walk Brownian-limit criterion of Collevecchio, Hamza, Shi and Williams, as restated in Theorem 1 of Hamza–Tournier, forces
\(n^{-1}\sum_{j=0}^{n-1}f(S_j)\to\rho\) in probability. Equation (1) says that this differs by a quantity tending to zero almost surely from the **deterministic** number \(A_{\lfloor n/2\rfloor}(f)\). Therefore this deterministic number converges to \(\rho\). As \(n\) ranges over even integers, \(\lfloor n/2\rfloor\) ranges over all positive integers, proving the required spatial Cesàro limit. This concludes the equivalence.

**3. Pascal-sign spatial strong law.** Fix \(0<\varepsilon\le1/2\), and write \(q=1-2\varepsilon\in[0,1)\). If \(0\le s<t\), choose the most significant binary digit on which \(s\) and \(t\) differ. Since \(t>s\), that digit is present in \(t\) and absent in \(s\). Lucas' parity theorem implies that the binomial parity vectors
\((e(s,k))_{k\le t}\) and \((e(t,k))_{k\le t}\) differ on at least \(2^{w(t)-1}\) coefficient positions, where \(w(t)\) is the number of ones in the binary expansion of \(t\). Indeed, all submasks of \(t\) containing that distinguished digit contribute, and there are exactly that many. Independence of the bits then implies
\[
 \left|\mathbb E_\beta[f_\beta(s)f_\beta(t)]\right|
 \le q^{2^{w(t)-1}}.\tag{3}
\]
Also \(f_\beta(s)^2=1\). Thus for \(N\ge2\),
\[
 \mathbb E_\beta[A_N(f_\beta)^2]
 \le\frac1N+\frac2N\sum_{t=1}^{N-1}q^{2^{w(t)-1}}.\tag{4}
\]
Let \(m=\lceil\log_2N\rceil\). The number of nonnegative integers below \(2^m\) with binary weight at most \(\lfloor m/4\rfloor\) is at most \(2^{mH_2(1/4)}\), where \(H_2(u)=-u\log_2u-(1-u)\log_2(1-u)\), by the elementary binomial-tail entropy bound. For the remaining indices the summand in (4) is at most \(q^{2^{m/4-1}}\), interpreted as zero when \(q=0\). As \(H_2(1/4)<7/8\), (4) therefore yields
\[
 \mathbb E_\beta[A_N(f_\beta)^2]=O_\varepsilon(N^{-1/8}).\tag{5}
\]
Take the deterministic subsequence \(N_j=\lfloor j^{10}\rfloor\). Chebyshev's inequality, (5), and \(\sum_jj^{-10/8}<\infty\) imply by Borel–Cantelli that \(A_{N_j}(f_\beta)\to0\) almost surely. Since \(\lvert f_\beta(s)\rvert=1\) and \(N_{j+1}/N_j\to1\), interpolation between successive subsequence lengths gives \(A_N(f_\beta)\to0\) for every integer \(N\). For almost every fixed \(\beta\), apply the deterministic equivalence with \(\rho=0\) under the **conditional input-walk law**, completing the quenched assertion.

## Verification

The self-contained Python program `verification.py` uses exact binomial parities and rational probabilities. It checks triangular Pascal invertibility through eight coefficients; all binary pairs \(0\le s<t<193\) against the Lucas differing-mask bound; independent enumeration of the random-coefficient pair-correlation product for seven coefficients; and a seeded family of finite renewal-occupation identities. It reports 19,109 checks passed. These finite checks provide reproducible error detection; (1)–(5) and the functional limit are proved for every relevant size analytically, not inferred from enumeration. Execute `python verification.py` with Python 3.10 or later.

## Relationship to prior work

Hamza and Tournier (arXiv:2610.01658v1, sections 1 and 4.3) state **annealed** convergence for the coefficient-static, cardinality-grouped inclusion-induced bootstrap walk in Proposition 11 and Corollary 12; they explicitly leave the corresponding quenched question open. Their argument already contains a Lucas-parity correlation estimate under **walk-time averaging**. The result here is not a new claim about the annealed theorem: it establishes the exact *deterministic spatial-Cesàro if-and-only-if criterion* for all fixed count-dependent bootstrap signs, and independently establishes an almost-sure spatial sign law for the particular nonidentically distributed Pascal coefficient model, which gives the conditional (quenched) conclusion.

Collevecchio, Hamza, Shi and Williams (arXiv:2010.16000; subsequently published in 2022) established the general predictable-quadratic-covariation criterion for two-dimensional bootstrap walks. That criterion supplies the necessity step in the proof but does not itself identify which **count-dependent** deterministic sign sequences meet it; the weighted geometric occupation decomposition supplies that classification here. A significant originality caveat is that quantitative estimates in Hamza–Tournier could plausibly be strengthened using subsequence Borel–Cantelli to recover the quenched corollary by a different argument; novelty should be evaluated on the combined explicit deterministic criterion and spatial almost-sure law, not on the word 'quenched' alone.

## Limitations

The deterministic if-and-only-if theorem is for fair input signs and the nondecreasing **negative-step count** state, not for arbitrary random-walk position sceneries or general Markov environments. The Pascal application requires independent, uniformly nondegenerate Bernoulli coefficients; no statement is made for parameters approaching zero or one without control, or for dependence among the coefficients. The proof gives an existence result and a nonoptimal moment-decay exponent, not a sharp quenched convergence rate. An equivalent formulation hidden in general renewal-reward or bootstrap-walk literature remains a search risk. Independent validation has not been performed.

## References

1. Kais Hamza and Laurent Tournier, *Are random random walks normal?*, arXiv:2610.01658v1, first posted 1 October 2026, especially Theorem 1, Proposition 11, Corollary 12 and proof of Proposition 11. https://arxiv.org/html/2610.01658v1
2. Andrea Collevecchio, Kais Hamza, Mao Shi and Roger J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000, available preprint, later published 2022, particularly its two-dimensional Brownian-limit characterization. https://arxiv.org/pdf/2010.16000
3. Lucas' theorem on binomial coefficients modulo two; Kolmogorov's convergence criterion; Kronecker's lemma; the martingale functional central limit theorem (standard results used in the proof).
