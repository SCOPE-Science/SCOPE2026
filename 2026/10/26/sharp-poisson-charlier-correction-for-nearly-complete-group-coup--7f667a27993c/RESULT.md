# Sharp Poisson–Charlier correction for nearly complete group coupon drawings

## Finding

Consider \(n\) coupon types. Independently on each of \(t\ge2\) rounds, choose exactly \(n-r\) distinct types uniformly without replacement, where \(2\le r<n\). Let \(U\) be the number of types not seen in any round, and put
\[
\lambda=n(r/n)^t,\qquad
\delta=\frac{t}{r}-\frac{t-1}{n},\qquad
C_2(k;\lambda)=k(k-1)-2\lambda k+\lambda^2.
\]
For \(\pi_\lambda(k)=e^{-\lambda}\lambda^k/k!\) and \(K_t=4+5t+t^2/2\), the following **nonasymptotic signed approximation** holds:
\[
\boxed{\sum_{k=0}^{\infty}\left|\Pr\{U=k\}-\pi_\lambda(k)\left(1-\frac{\delta}{2}C_2(k;\lambda)\right)\right|
\le \frac{K_t}{r^2}\,e^{2\lambda}T_4(2\lambda),}
\]
where \(T_4(z)=z^4+6z^3+7z^2+z\). The corrected masses are a signed approximation, not necessarily a probability distribution.

For any fixed \(t\ge2\) and sequence \(r=r_n\) satisfying
\[
\lambda_n=n(r_n/n)^t\longrightarrow\lambda_*\in(0,\infty),
\]
the correction is sharp:
\[
\boxed{r_n\,d_{\mathrm{TV}}\big(\mathcal L(U_n),\operatorname{Poi}(\lambda_n)\big)
\longrightarrow \frac{t}{4}\mathbb E\left|C_2(Z;\lambda_*)\right|,\quad Z\sim\operatorname{Poi}(\lambda_*).}
\]
In addition, for the time \(T_n\) of complete collection,
\[
\Pr\{T_n\le t\}=e^{-\lambda_n}\left(1-\frac{\delta_n\lambda_n^2}{2}\right)+O_{t,\lambda_*}(r_n^{-2}).
\]
The two scales \(t/r_n\) and \((t-1)/n\) are both retained in the correction; the second can exceed the quadratic remainder for \(t>2\).

## Assumptions and scope

Drawings in distinct rounds are independent; within each round all \(\binom n{n-r}\) groups are equiprobable. The finite bound holds for every integer \(n>r\ge2\), \(t\ge2\), without assuming \(\lambda\) bounded. It is informative for bounded \(\lambda\). Total variation is \(\frac12\sum_k|p(k)-q(k)|\). In the stated asymptotic regime, \(r_n\to\infty\) and \(r_n/n\to0\) follow from the positive finite limit of \(\lambda_n\).

## Proof

**Exact factorial moments.** The missed types in one round form a uniformly random \(r\)-subset of \([n]\), so \(U\) is the size of the intersection of \(t\) independent such subsets. Write \((a)_j=a(a-1)\cdots(a-j+1)\), with \((a)_0=1\). For every nonnegative integer \(j\),
\[
\mu_j:=\mathbb E(U)_j=(n)_j\left(\frac{(r)_j}{(n)_j}\right)^t
=\lambda^j R_j,\qquad
R_j=\prod_{\ell=0}^{j-1}\frac{(1-\ell/r)^t}{(1-\ell/n)^{t-1}}
\]
when \(0\le j\le r\); set \(R_j=0\) when \(j>r\). Each product factor lies in \([0,1]\), so \(0\le R_j\le1\).

**Uniform fourth-degree remainder.** Put \(b_j=\delta j(j-1)/2\), so \(0\le b_j\le t j^2/(2r)\). We claim
\[
\left|R_j-1+b_j\right|\le \frac{K_t j^4}{r^2}\quad\text{for all integers }j\ge0.
\]
For \(j\le r/2\), let \(x_j=-\log R_j\ge0\). The elementary inequalities \(0\le-\log(1-u)-u\le2u^2\) for \(0\le u\le1/2\), together with \(\sum_{\ell<j}\ell^2\le j^3\), give
\[
|x_j-b_j|\le 4t j^3/r^2,\qquad
0\le x_j\le t j^2/r.
\]
Using \(0\le e^{-x}-1+x\le x^2/2\) for \(x\ge0\), we obtain
\[
|R_j-1+b_j|\le\frac{4t j^3+(t^2/2)j^4}{r^2}
\le\frac{(4t+t^2/2)j^4}{r^2}.
\]
For \(j>r/2\), including \(j>r\), use \(0\le R_j\le1\) and \(b_j\le t j^2/(2r)\). Because \(j^2/r>r/4\ge1/2\),
\[
|R_j-1+b_j|\le1+\frac{t j^2}{2r}
\le (4+t)\frac{j^4}{r^2}.
\]
The chosen \(K_t\) dominates both constants, proving the claim.

**Absolutely summable inversion.** The exact factorial-moment inversion is
\[
\Pr\{U=k\}=\sum_{j=k}^{\infty}(-1)^{j-k}\binom jk\frac{\mu_j}{j!},
\]
where the sum is actually finite. The same identity with \(\mu_j=\lambda^j\) produces \(\pi_\lambda(k)\). Differentiation of the Poisson generating function, or direct coefficient extraction, gives
\[
\sum_{j=k}^{\infty}(-1)^{j-k}\binom jk\frac{\lambda^j j(j-1)}{j!}
=\pi_\lambda(k)C_2(k;\lambda).
\]
Inverting the remainder term and summing first over \(k\), using \(\sum_{k=0}^j\binom jk=2^j\), yields
\[
\sum_k|\Pr\{U=k\}-\pi_\lambda(k)(1-\delta C_2(k;\lambda)/2)|
\le\frac{K_t}{r^2}\sum_{j\ge0}\frac{(2\lambda)^j j^4}{j!}
=\frac{K_t}{r^2}e^{2\lambda}T_4(2\lambda).
\]
All interchanges are justified by the displayed absolutely convergent exponential series, even when \(j>r\). This proves the finite bound.

**Sharpness and full collection.** Since \(\delta_n=t/r_n-(t-1)/n>0\), the reverse triangle inequality gives
\[
\left|d_{\mathrm{TV}}\big(\mathcal L(U_n),\operatorname{Poi}(\lambda_n)\big)
-\frac{\delta_n}{4}\mathbb E|C_2(Z_n;\lambda_n)|\right|
\le\frac{K_t}{2r_n^2}e^{2\lambda_n}T_4(2\lambda_n),
\]
for \(Z_n\sim\operatorname{Poi}(\lambda_n)\). In the specified regime, \(r_n\to\infty\), \(r_n/n\to0\), hence \(r_n\delta_n\to t\). Poisson fourth moments are locally uniformly bounded in the mean, so their Charlier absolute moments converge. Taking limits proves the sharp constant. Finally \(T_n\le t\) exactly when \(U_n=0\), and \(C_2(0;\lambda)=\lambda^2\), giving the completion-probability formula.

## Verification

A reproducible exact-rational enumeration and factorial-moment inversion are supplied in `verify.py`. Small examples check the complete probability mass function against explicit independent group selection. Larger examples compare scaled total variation with the limiting constant and test the signed remainder against the proved finite bound. These computations are checks, not a substitute for the infinite-parameter proof above.

## Relationship to prior work

Betken and Thäle (2023) study coupon group drawings and prove quantitative normal and Poisson approximations for the \(\Theta(n\log n)\)-drawing regime with fixed package size. Here the number of rounds is fixed and each package contains \(n-r_n\) types, with \(r_n\asymp n^{1-1/t}\); those theorem hypotheses do not cover the present critical window. Goldstein and Reinert (2006) study **the identical random-subset intersection object** for arbitrary fixed subset sizes and derive an explicit total-variation upper bound and the Poisson limit. Their theorem does not provide the present signed second-Charlier expansion, the uniform quadratic-order remainder, or the sharp variation constant. The Charlier correction itself is a standard approximation mechanism; the added mathematical content is the explicit sharp dependent-subset coefficient with a global summable error estimate and the resulting coupon-completion calibration.

## Limitations

The result concerns independent uniformly chosen equal-sized groups and fixed \(t\), not growing numbers of rounds, unequal group sizes, arbitrary coupon probabilities, or higher-order corrections. The signed approximation may have negative values in extremely remote tails. The bound scales as \(e^{2\lambda}T_4(2\lambda)/r^2\) and need not be useful when \(\lambda\) grows. Historic priority cannot be guaranteed from the inspected literature; general Poisson–Charlier expansion techniques might contain a covering specialization that was not identified. The 2026 study of group packages very close to \(n\) concerns expected completion times; its full text was not accessible for comparison.

## References

1. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, Journal of Applied Probability 60 (2023), 1352–1366; preprint first publicly posted 15 February 2022 (arXiv:2202.07485); journal version published online 25 April 2023, DOI: 10.1017/jpr.2023.6.
2. L. Goldstein and G. Reinert, *Total Variation Distance for Poisson Subset Numbers*, Annals of Combinatorics 10 (2006), 333–341; publicly available author manuscript dated 23 February 2005, https://www.stats.ox.ac.uk/~reinert/papers/poissonsubset.pdf.
3. H.-K. Hwang and V. Zacharovas, *Uniform Asymptotics of Poisson Approximation to the Poisson-Binomial Distribution*, Theory of Probability and Its Applications 55 (2011), 198–224; DOI: 10.1137/S0040585X97984784. Its central independent-indicator setting differs from dependent subset intersections; full-text coverage remains a priority risk.
