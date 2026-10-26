# Sharp pair-exceedance prefactor and singular tail dependence under batch resetting

## Finding

For a stationary one-dimensional Brownian gas with uniform random **batch resetting**, the probability that **two tagged particles simultaneously make large positive excursions** has an exact asymptotic coefficient, not only an exponential rate. For \(N\ge3\), \(2\le m<N\), \(r,D>0\), define
\[
\lambda=\frac{rm}{N},\quad c=\frac{rm(m-1)}{N(N-1)},\quad \alpha=\lambda-c,\quad \delta=2\lambda-c,
\]
\[
k_1=\sqrt{\lambda/D},\qquad k_2=\sqrt{2\delta/D}.
\]
Then, with \(X_1,X_2\) two distinct stationary particle positions,
\[
\boxed{\mathbb P(X_1>x,X_2>x)\sim
\frac{c+4\alpha\lambda/c}{\delta\sqrt{2\pi k_2x}}\,e^{-k_2x}}
\qquad(x\to\infty).
\]
Since \(\mathbb P(X_1>x)=e^{-k_1x}/2\) exactly for positive \(x\),
\[
\boxed{\mathbb P(X_2>x\mid X_1>x)\sim
\frac{2(c+4\alpha\lambda/c)}{\delta\sqrt{2\pi k_2x}}
 e^{-(k_2-k_1)x}}.
\]
Each of the four joint sign quadrants has the same probability. The same-threshold absolute excursion probability is therefore four times the positive-quadrant expression. The conditional extreme probability vanishes exponentially even though positive correlations between squared coordinates persist.

There is a singular distinction at independent resetting \(m=1\): then \(c=0\) and \(\mathbb P(X_1>x,X_2>x)=e^{-2k_1x}/4\) exactly, with no algebraic prefactor. The displayed mixed-batch result assumes fixed \(c>0\) and does not claim uniform convergence as \(c\downarrow0\).

## Assumptions and scope

There are fixed integers \(N\ge3\) and \(2\le m<N\). Between rate-\(r\) reset events, all coordinates follow independent Brownian motions with generator \(D\partial_{xx}\). At each event an independent uniformly chosen subset of exactly \(m\) labels is set to zero. Brownian increments, event times and choices are independent. The stationary regime exists because each tagged particle is reset at positive rate \(\lambda\). All asymptotics hold with \(N,m,r,D\) fixed as the positive threshold \(x\) tends to infinity. The boundary cases \(m=1\) and \(m=N\) are discussed separately and are not included in the new mixed-batch assertion.

## Proof

**1. Reset types and an exact renewal decomposition.** For two fixed labels, reset events affecting exactly the first, exactly the second, or both occur at independent Poisson rates \(\alpha,\alpha,c\), respectively. Their union rate is \(\delta=2\alpha+c=2\lambda-c\). Read the stationary process backward to the last event affecting either label. Its age \(T\) has density \(\delta e^{-\delta t}\), and its mark is independent of \(T\), with probabilities \(\alpha/\delta,\alpha/\delta,c/\delta\). A singly reset coordinate starts from zero while the unreset coordinate has its stationary one-point law, independent of the new Brownian motions. At a joint reset, both start from zero. The one-point stationary law is Laplace with density \(k_1e^{-k_1|y|}/2\), by mixing a \(N(0,2Dt)\) displacement against an exponential age of rate \(\lambda\). Let \(Y\) have this Laplace law and set \(Q_t(x)=\mathbb P(N(0,2Dt)>x)\). Consequently the following is an **exact identity**, for every \(x>0\):
\[
\mathbb P(X_1>x,X_2>x)
=\int_0^\infty e^{-\delta t}
\left\{cQ_t(x)^2+2\alpha Q_t(x)\mathbb E[Q_t(x-Y)]\right\}\,dt.
\tag{1}
\]
The identity counts no previous unsuccessful resets incorrectly: the pre-reset state of the unreset coordinate has its stationary marginal, and the fresh increments after the last tagged reset are independent.

**2. Common-reset contribution.** Write \(J(x)=\int_0^\infty e^{-\delta t}Q_t(x)^2\,dt\). Mills' ratio, uniformly in the saddle window, gives
\[
Q_t(x)^2\sim\frac{Dt}{\pi x^2}e^{-x^2/(2Dt)}.
\]
The exponent \(\delta t+x^2/(2Dt)\) has a unique nondegenerate minimizer \(t_*=x/\sqrt{2D\delta}\), with minimum \(k_2x\). The integral outside any fixed relative neighborhood of \(t_*\) is exponentially negligible. The standard positive Bessel integral identity then yields
\[
J(x)\sim\frac{D}{\pi x^2}\int_0^\infty t e^{-\delta t-x^2/(2Dt)}dt
=\frac{K_2(k_2x)}{\pi\delta}
\sim\frac{e^{-k_2x}}{\delta\sqrt{2\pi k_2x}}.
\tag{2}
\]
Here \(K_2\) denotes the modified Bessel function. The middle equality applies to the asymptotic proxy; it does **not** assert that the original Gaussian survival integral equals the Bessel expression at finite \(x\).

**3. A finite exponential tilt from the unreset coordinate.** In the saddle window, for every fixed real \(y\),
\[
\frac{Q_t(x-y)}{Q_t(x)}\longrightarrow
\exp\!\left(\frac{k_2y}{2}\right).
\]
Crucially \(k_2/2<k_1\), because \(k_1^2-k_2^2/4=c/(2D)>0\). The stationary Laplace marginal therefore has the finite tilted moment
\[
\mathbb E e^{k_2Y/2}=\frac{k_1^2}{k_1^2-k_2^2/4}
=\frac{2\lambda}{c}.
\tag{3}
\]
To pass this limit under the integral, restrict first to \(|Y|\le M\) in a shrinking relative saddle window. For the complement, Gaussian Mills bounds and the exponential Laplace density bound the tilted integrand by an integrable exponential with rate strictly between \(k_2/2\) and \(k_1\). Taking \(M\to\infty\) after the \(x\to\infty\) limit gives
\[
\int_0^\infty e^{-\delta t}Q_t(x)\mathbb E[Q_t(x-Y)]dt
\sim\frac{2\lambda}{c}J(x).
\tag{4}
\]
Equivalently, in a two-age description, the exponent for unequal ages is bounded below by \(k_2x+(c/2)|t_1-t_2|\), an explicit transverse localization bound proving no remote-age sector contributes at the same order. Indeed, for \(u,v>0\), convexity of the reciprocal implies \(1/u+1/v\ge4/(u+v)\), giving this lower bound for the Gaussian exponential proxy.

**4. Finish.** Substitute (2) and (4) into exact identity (1). Since \(c>0\), both contributions are positive and their sum has coefficient \(c+4\alpha\lambda/c\). Dividing by the exact one-coordinate exceedance proves the conditional statement. Independent symmetric Brownian increments, conditional on reset ages, make each joint sign quadrant equiprobable. For \(m=1\), no reset marks affect two labels together; independent Poisson thinning yields independent stationary coordinates, giving the stated exact product formula.

## Verification

The companion `verify.py` evaluates the **exact** last-event integral numerically using the normal–Laplace convolution and compares it with the derived leading coefficient for several finite mixed-batch parameter sets and increasing thresholds. It also checks the reset-rate identities, the strict moment-generating-function gap and the separate independence boundary. Finite numerical comparisons are corroboration, not proof of the infinite-threshold statement; the saddle calculation and integrable-tilt justification above establish the limit. Reproduce with Python 3 and SciPy using `python verify.py`.

## Relationship to prior work

De Mauro, Majumdar and Schehr, arXiv:2601.20077 (first posted 2026-01-27), introduce this **same** batch-reset Brownian gas and derive an exact stationary pair-density formula using a modified Bessel kernel and convolution (Supplementary Material §S3, equations S33–S36). Those equations are acknowledged as substantially stronger **finite-position information**; the model and exact pair law are **not** claimed as new. The finding here is the explicitly evaluated **far-quadrant exceedance probability**, including its nontrivial \(x^{-1/2}\) coefficient, the conditional rare-event normalization, and the discontinuity in prefactor type at zero common-reset intensity. A prior sharp logarithmic joint-excursion law already gives the exponential rate but does not determine the asymptotic coefficient. Biroli, Larralde, Majumdar and Schehr (arXiv:2211.00563, first posted 2022-11-01) study global synchronous resetting and extremes; that regime \(m=N\) is excluded from the new mixed-batch theorem. An exact full pair density logically determines any marginal integral, so originality specifically rests on the **nontrivial sharp asymptotic extraction**, not on a previously unknown underlying pair distribution.

## Limitations

The result is not uniform as \(m/N\) changes or as \(c\downarrow0\), does not provide a joint large-\(N\) limit, and concerns stationary fixed-label positive exceedances rather than first-passage maxima or the largest particle over a growing population. The exact pair density of the source implicitly contains this tail information; independent assessment of how substantial the asymptotic extraction is remains outstanding. No claim is made about new finite-position pair laws or entropy production.

## References

1. G. de Mauro, S. N. Majumdar and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077, first posted 2026-01-27; especially Supplementary Material §S3 (exact pair law), https://arxiv.org/html/2601.20077v3 .
2. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563, 2022; https://arxiv.org/pdf/2211.00563 .
