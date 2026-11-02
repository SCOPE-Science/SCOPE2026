# A sharp Cauchy pole and logarithmic ridge cost for Gaussian-batch Polyak steps

## Finding

For a scalar Gaussian linear-regression batch of size \(k\ge 2\), an **uncapped** stochastic Polyak step that substitutes the valid zero lower bound for the batch minimum has a universal reciprocal-gradient tail, despite the use of a strongly convex quadratic batch loss. With notation below, at every deterministic starting point \(x\in\mathbb R\) and every \(0<\gamma\le 2\),

\[
\lim_{t\to\infty}t\,\mathbb P\{|T_0(x)|>t\}=C_{k,\gamma,\sigma}(x-\theta),
\]

where

\[
C_{k,\gamma,\sigma}(\delta)=\frac{\gamma\sigma}{\sqrt\pi}\frac{\Gamma((k+1)/2)}{\Gamma(k/2)}\left(1+\frac{\delta^2}{\sigma^2}\right)^{-(k-1)/2}>0.
\]

Consequently \(\mathbb E|T_0(x)|^q<\infty\) if and only if \(0<q<1\). At \(x=\theta\), the leading tail coefficient is asymptotic to \(\gamma\sigma\sqrt{k/(2\pi)}\) as the batch size increases. The singularity is not cured by increasing the finite minibatch size.

For the gradient-ridge update \(T_\varepsilon\) defined below, the first absolute displacement has the exact small-ridge logarithmic law

\[
\lim_{\varepsilon\downarrow0}\frac{\mathbb E|T_\varepsilon(x)-x|}{\log(1/\varepsilon)}=\frac12 C_{k,\gamma,\sigma}(x-\theta).
\]

Replacing zero by the **actual batch minimum** instead gives the linear contraction \(T_\star(x)=(1-\gamma/2)x+(\gamma/2)\widehat\theta\). Under fresh independent batches its unique stationary law has a finite absolute moment of order \(q>0\) if and only if \(q<k\); for \(k\ge3\) its variance is exactly

\[
\operatorname{Var}(U_\infty)=\frac{\gamma\sigma^2}{(4-\gamma)(k-2)}.
\]

At \(k=1\), the calibrated chain has exactly the Cauchy \((\theta,\sigma)\) stationary law, independently of \(\gamma\in(0,2]\). The two distinct moment boundaries reflect the positive residual left after fitting a noninterpolating batch, rather than stochasticity alone.

## Assumptions and scope

Fix any integer \(k\ge2\), any real true slope \(\theta\), deterministic initial point \(x\in\mathbb R\), independent random covariates \(X_i\sim N(0,1)\), and independent errors \(\xi_i\sim N(0,\sigma^2)\), where \(\sigma>0\). Let \(Y_i=\theta X_i+\xi_i\). Define the quadratic batch loss

\[
F_k(u)=\frac1{2k}\sum_{i=1}^k(X_iu-Y_i)^2,
\qquad G_k(u)=\frac{dF_k(u)}{du},
\]

and \(S=\sum X_i^2>0\), \(\widehat\theta=\sum X_iY_i/S\), and \(R=\sum (Y_i-X_i\widehat\theta)^2\). All formulas hold on the probability-one event on which denominators are nonzero. In particular \(G_k(x)\ne0\) almost surely for deterministic \(x\).

For a fixed dimensionless multiplier \(0<\gamma\le2\), compare the exact updates

\[
T_0(x)=x-\gamma\frac{F_k(x)}{G_k(x)},\qquad
T_\varepsilon(x)=x-\gamma\frac{F_k(x)G_k(x)}{G_k(x)^2+\varepsilon},\quad \varepsilon>0,
\]

and \(T_\star(x)=x-\gamma(F_k(x)-\min_uF_k(u))/G_k(x)\), with its continuous extension at zero gradient. The ridge uses a squared-gradient addition and is distinct from a hard cap on the stepsize. Fresh batch means that new independent observations are drawn at each iteration.

## Proof

**Batch projection and the residual gap.** Completing the square gives, identically,

\[
F_k(u)=\frac{S(u-\widehat\theta)^2+R}{2k},\qquad
G_k(u)=\frac S k(u-\widehat\theta),\qquad
\min_uF_k(u)=\frac R{2k}.
\]

Gaussian orthogonal projection, conditional on the covariate vector, yields mutually independent \(S\sim\chi_k^2\), \(Z\sim N(0,1)\), and \(V\sim\chi_{k-1}^2\), with

\[
\widehat\theta=\theta+\frac{\sigma Z}{\sqrt S},\qquad R=\sigma^2V.
\]

In particular, \(R>0\) almost surely when \(k\ge2\): the zero target is a strict (though valid) lower bound.

**Uncapped pole.** Put \(d=(x-\theta)/\sigma\). Direct substitution gives

\[
T_0(x)=x-\frac\gamma2(x-\theta)+\frac{\gamma\sigma}{2\sqrt S}\left[Z+\frac{V}{Z-d\sqrt S}\right].
\]

Let \(P=\gamma\sigma V/[2\sqrt S(Z-d\sqrt S)]\). Conditional on \(S,V\), the event \(|P|>t\) is an interval of radius \(\gamma\sigma V/(2\sqrt S\,t)\) around \(d\sqrt S\) for a standard normal variable. Therefore

\[
\lim_{t\to\infty}t\,\mathbb P(|P|>t\mid S,V)=\frac{\gamma\sigma V}{\sqrt S}\,\varphi(d\sqrt S),
\]

where \(\varphi(z)=e^{-z^2/2}/\sqrt{2\pi}\). The conditional expression is dominated by \(\gamma\sigma V/(\sqrt{2\pi S})\), which is integrable for \(k>1\). Independence and the chi-square integral give

\[
\begin{aligned}
\lim_{t\to\infty}t\,\mathbb P(|P|>t)
&=\gamma\sigma(k-1)\mathbb E[S^{-1/2}\varphi(d\sqrt S)]\\
&=\frac{\gamma\sigma}{\sqrt\pi}
\frac{\Gamma((k+1)/2)}{\Gamma(k/2)}(1+d^2)^{-(k-1)/2}.
\end{aligned}
\]

The remaining random term \(\gamma\sigma Z/(2\sqrt S)\) has Student-type tail order \(t^{-k}\), which is \(o(t^{-1})\). For any fixed \(0<\eta<1\), the triangle-inequality upper/lower tail squeezes at \((1\pm\eta)t\) transfer the same coefficient to the full update. The tail integral identity proves divergence for every \(q\ge1\). For \(0<q<1\), the inverse-normal moment \(\sup_a\mathbb E|Z-a|^{-q}\) is finite, as is \(\mathbb E S^{-q/2}\), so the update has finite \(q\)-moment. Stirling's ratio formula proves the coefficient's stated large-\(k\) behavior at the true slope.

**Gradient ridge.** With \(t_0=x-\widehat\theta\), the regularized update satisfies the exact identity

\[
T_\varepsilon(x)-x=-\frac\gamma2\frac{t_0^3+(R/S)t_0}{t_0^2+(k\sqrt\varepsilon/S)^2}.
\]

The first term in the numerator has expected absolute size bounded by \(\gamma\mathbb E|t_0|/2<\infty\), uniformly in \(\varepsilon\). For the residual term, condition on \(S,V\) and write \(u=Z-d\sqrt S\), \(a_\varepsilon=k\sqrt\varepsilon/(\sigma\sqrt S)\). Its conditional absolute mean is

\[
\frac{\gamma\sigma V}{2\sqrt S}
\int_{\mathbb R}\frac{|u|}{u^2+a_\varepsilon^2}\,\varphi(u+d\sqrt S)\,du.
\]

For fixed \(S>0\), its integral is \(2\varphi(d\sqrt S)\log(1/a_\varepsilon)+O_{S,d}(1)\); hence after dividing by \(\log(1/\varepsilon)\) it tends to \(\varphi(d\sqrt S)\). An elementary split at \(|u|=1\) bounds the normalized integral by a constant multiple of \(1+\log_+S\) for all sufficiently small \(\varepsilon\). Since \(\mathbb E[V S^{-1/2}(1+\log_+S)]<\infty\) for \(k>1\), dominated convergence gives \(\gamma\sigma\mathbb E[V S^{-1/2}\varphi(d\sqrt S)]/2=C_{k,\gamma,\sigma}/2\).

**Batch-exact target and stationary moments.** Subtracting \(\min F_k=R/(2k)\) cancels the reciprocal term and yields

\[
T_\star(x)=\left(1-\frac\gamma2\right)x+\frac\gamma2\widehat\theta.
\]

For fresh batches write \(a=1-\gamma/2\in[0,1)\) and \(b=\gamma/2\). Iterations relative to the true slope are \(U_{j+1}-\theta=a(U_j-\theta)+bW_j\), with iid \(W_j=\sigma Z_j/\sqrt{S_j}\), a scaled Student variable of \(k\) degrees of freedom. The absolutely convergent stationary series \(U_\infty-\theta=b\sum_{i\ge0}a^iW_i\) exists uniquely and has finite \(q\)-moment exactly for \(q<k\). Finite moments follow from Minkowski/subadditivity; infinite moments follow by conditioning on all innovations except one and using the Student tail \(\mathbb P(|W_0|>t)\asymp t^{-k}\). If \(k\ge3\), \(\mathbb E W_j^2=\sigma^2/(k-2)\), hence \(\operatorname{Var}(U_\infty)=b^2\sigma^2/[(1-a^2)(k-2)]\), as claimed. At \(k=1\), \(W_j\) is Cauchy with scale \(\sigma\); stability of Cauchy sums gives the invariant scale \(b\sigma/(1-a)=\sigma\), centered at \(\theta\).

## Verification

The supplied `verify.py` uses only the Python standard library. Run `python3 verify.py`. It checks exact rational batch identities and the three update formulas, independent chi-square integral evaluations for the tail coefficient, exact stationary variance algebra, and random-sampling diagnostics for three batch sizes. A successful run reports 690 exact rational tests, 12 gamma-constant quadratures, 16 exact variance identities, and 570,000 Monte Carlo samples. Random simulations and quadratures illustrate formulas; the preceding analytic argument supplies the infinite-dimensional quantifiers, sharp tails, moment conclusions, and asymptotics.

## Relationship to prior work

Gower, Blondel, Gazagnadou and Pedregosa (2022) develop slack-variable variants of stochastic Polyak steps and explain difficulties outside interpolation. Orvieto, Lacoste-Julien and Loizou (2022) establish convergence theory for **capped** SPS with loose batch-optimum lower bounds and introduce decaying safeguards. Schaipp, Gower and Ulbrich (2023) analyze proximal SPS variants. Their results motivate comparing lower-bound and exact-batch targets but do not imply the quantitative **uncapped** Gaussian one-step tail, its exact ridge logarithmic coefficient, or the calibrated invariant moment threshold. The Student-ratio and Gaussian projection ingredients are standard and not claimed as new; the claimed mathematical contribution is their precise joint classification for this particular stochastic optimization update. Published mathematical-record searches found no directly covering implication. Publication priority should still be checked independently against specialized statistical-ratio and normalized-learning literature.

## Limitations

Only scalar Gaussian random-design regression, finite batches, squared loss, independent homoscedastic Gaussian errors, fixed deterministic start, uncapped zero-target Polyak steps, the specified gradient-ridge rule, and independently refreshed batches for invariant-law statements are considered. The singularity does **not** apply to the capped SPS or DecSPS variants of the cited work. No almost-sure divergence, multi-dimensional theorem, non-Gaussian universality, bounded-data statement, or end-to-end optimizer risk guarantee is claimed. An infinite expectation is not a claim that every realization is large. The ridge coefficient describes an asymptotic in the stated dimensional normalization.

## References

1. R. M. Gower, M. Blondel, N. Gazagnadou, and F. Pedregosa, *Cutting Some Slack for SGD with Adaptive Polyak Stepsizes* (first public version 2022-02-24), https://arxiv.org/abs/2202.12328.
2. A. Orvieto, S. Lacoste-Julien, and N. Loizou, *Dynamics of SGD with Stochastic Polyak Stepsizes: Truly Adaptive Variants and Convergence to Exact Solution* (first public version 2022-05-09), https://arxiv.org/abs/2205.04583.
3. F. Schaipp, R. M. Gower, and M. Ulbrich, *A Stochastic Proximal Polyak Step Size* (first public version 2023-01-12), https://arxiv.org/abs/2301.04935.
4. S.-C. Chan and Y. Zhou, *On the Performance Analysis of the Least Mean M-Estimate and Normalized Least Mean M-Estimate Algorithms with Gaussian Inputs and Additive Gaussian and Contaminated Gaussian Noises* (2009), https://link.springer.com/article/10.1007/s11265-009-0405-9.
