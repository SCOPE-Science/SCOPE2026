# Two-switch covariance geometry of multinomial occupancy frequencies

## Finding

Let \(m\ge3\) and allocate \(n\) independent balls uniformly to \(m\) boxes. Let \(X_r\) be the number of boxes containing exactly \(r\) balls. For two distinct integers \(0\le j<k\), put \(s=j+k\), require \(n\ge s\), and define
\[
R_{m,j,k}(n)=\frac{(n)_{s}(m-2)^{n-s}m^{n-1}}{(n)_j(n)_k(m-1)^{2n-s-1}},
\]
where \((n)_r=n(n-1)\cdots(n-r+1)\) and \((n)_0=1\). Then \(\operatorname{Cov}(X_j,X_k)\) has exactly the sign of \(R_{m,j,k}(n)-1\). For \(j=0\), this ratio strictly decreases in \(n\). For \(j\ge1\), its consecutive quotient is greater than, equal to, or less than one exactly as
\[
(n+1)(n+1-s)\quad\text{is less than, equal to, or greater than}\quad m(m-2)jk.
\]
In particular it is strictly increasing then strictly decreasing (allowing a two-point plateau), with its maximum at \(n=\lfloor z\rfloor\) when \(z\notin\mathbb Z\), and at both \(z-1,z\) when \(z\in\mathbb Z\), where
\[
z=\frac{s+\sqrt{s^2+4m(m-2)jk}}2.
\]
Consequently positive covariance occurs on a possibly empty *contiguous interval of sample sizes*: as \(n\) grows, covariance has at most two strict sign reversals, and a positive phase can only be enclosed by negative phases. The exact integer positivity criterion is the explicit inequality \(R_{m,j,k}(n)>1\), without numerical root estimation.

A sharp exceptional scale arises for fixed consecutive positive squares \(j=a^2\), \(k=(a+1)^2\), \(a\ge1\), and \(q=a(a+1)\). For every fixed real \(y\), with \(n_m=qm+\lfloor y\sqrt m\rfloor\),
\[
\lim_{m\to\infty}m^2\log R_{m,j,k}(n_m)=1-\frac{y^2}{q}.
\]
Thus the positive-covariance interval near \(qm\) has asymptotic width \(2\sqrt{qm}\); more precisely its endpoints differ from \(qm\) by \(\pm\sqrt{qm}+o(\sqrt m)\). This thin positive phase is invisible at the scale \(n/m\). Its boundary is intrinsic: for heterogeneous allocations a three-switch pattern already occurs with three box probabilities \((1,15,16)/32\), for \((j,k)=(1,2)\), at sample sizes \(3,4,9,10\) with signs \(+,-,+,-\), respectively.

## Assumptions and scope

All draws are independent. The pair \(j,k\) is fixed within a finite-sample statement and distinct, with \(0\le j<k\); the ratio and covariance assertions are for \(m\ge3\) and \(n\ge j+k\). An integer threshold where covariance is exactly zero is permitted and is not counted as a strict sign reversal. The critical-window limit fixes \(a\) and \(y\) while \(m\to\infty\). The final heterogeneous example concerns unequal probabilities and is a counterexample to extension of the uniform two-switch bound, not to the uniform theorem.

## Proof

Write \(p_r=\binom nr m^{-r}(1-1/m)^{n-r}\) for the occupancy probability of one designated box. For two distinct boxes, the joint probability of occupancies \(j,k\) is
\[
p_{j,k}=\frac{(n)_{j+k}}{j!k!m^{j+k}}(1-2/m)^{n-j-k}.
\]
Therefore \(\mathbb EX_r=mp_r\), \(\mathbb E(X_jX_k)=m(m-1)p_{j,k}\) for \(j\ne k\), and
\[
\operatorname{Cov}(X_j,X_k)=m^2p_jp_k\big(R_{m,j,k}(n)-1\big).
\]
Substitution gives the displayed exact ratio. Its adjacent quotient simplifies to
\[
\frac{R_{m,j,k}(n+1)}{R_{m,j,k}(n)}=
\frac{m(m-2)}{(m-1)^2}\frac{(n+1-j)(n+1-k)}{(n+1)(n+1-j-k)}.
\]
Since \((m-1)^2-m(m-2)=1\), comparison with one is equivalent to comparing \((n+1)(n+1-j-k)\) with \(m(m-2)jk\). The former is strictly increasing in integer \(n\ge j+k\). For \(j=0\), it is strictly positive, making the ratio decreasing. For \(j,k\ge1\), it crosses the positive constant at most once, proving the unimodality and the exact maximizer. Moreover, \(R_{m,j,k}(n)\to0\) exponentially as \(n\to\infty\), because its adjacent quotient tends to \(m(m-2)/(m-1)^2<1\). This proves the sign classification.

For completeness, when \(j=0\), \(R_{m,0,k}(k)=(1-1/m)^{1-k}\), so it starts strictly above one for \(k\ge2\), equals one for \(k=1\), then decreases. For positive \(j,k\), the pair moments are positive at every admissible \(n\), so no exceptional denominator occurs.

For fixed positive \(j,k\) and \(n/m\to\lambda\in(0,\infty)\), expansion of the logarithm gives
\[
\log R_{m,j,k}(n)=\frac{j+k-1-\lambda-jk/\lambda}{m}+O(m^{-2})
\]
when \(n=\lambda m\) exactly; uniformity holds on compact positive \(\lambda\)-intervals, and replacing \(\lambda\) by \(n/m\) handles integer sequences. The quadratic \(\lambda^2-(j+k-1)\lambda+jk\) has a repeated positive root precisely when \((\sqrt k-\sqrt j)^2=1\), which for positive integers is equivalent to consecutive squares. At that root \(\lambda=q=a(a+1)\), expansion one order further yields
\[
\log R_{m,j,k}(n)=\frac{j+k-1-\lambda-jk/\lambda}{m}
 +\frac{3(j+k)/2-2\lambda-1/2-jk(j+k-1)/(2\lambda^2)}{m^2}
 +O(m^{-3})
\]
for \(n=\lambda m\), with locally uniform remainder. Insert \(\lambda=q+\lfloor y\sqrt m\rfloor/m\): the coefficient of the first term becomes \(-y^2/(qm^2)+o(m^{-2})\), and the second term becomes \(1/m^2+o(m^{-2})\), proving the stated limit. Strict unimodality and the limit's opposite signs at \(y=\pm(\sqrt q\pm\epsilon)\) establish the endpoint asymptotics.

For unequal probabilities \(p_1,p_2,p_3\), write \(\mu_r(n)=\sum_i\binom nr p_i^r(1-p_i)^{n-r}\). For \(j\ne k\),
\[
\operatorname{Cov}(X_j,X_k)=\frac{n!}{j!k!(n-j-k)!}\sum_{i\ne l}p_i^jp_l^k(1-p_i-p_l)^{n-j-k}-\mu_j(n)\mu_k(n).
\]
With \((p_1,p_2,p_3)=(1,15,16)/32\), \((j,k)=(1,2)\), substitution gives, at \(n=3,4,9,10\), respectively, covariance signs \(+,-,+,-\). The accompanying exact-rational script checks the corresponding numerators and denominators; hence this heterogeneous model has at least three strict sign reversals and does not obey the two-switch classification.

## Verification

Run `python3 verify.py` with the Python standard library. It exhaustively enumerates 48 small equiprobable models and compares the covariance with the exact formula; checks the sign ordering in 15,351 parameter points; and computes exact rational covariances at all four heterogeneous checkpoints. This is finite corroboration only; the proof above supplies the all-parameter conclusions. The asymptotic expansion is algebraic and does not rely on numerical extrapolation.

## Relationship to prior work

Classical random-allocation theory gives occupancy-profile moment formulas. Barbour and Gnedin (2008), *Small counts in the infinite occupancy scheme*, studies infinite unequal-frequency systems, normal approximations and limiting correlation structures, especially in the Poissonized model. Its inspected introduction and covariance sections do not state the finite fixed-box two-switch classification or the consecutive-square square-root window. Kolchin, Sevastyanov and Chistyakov's book *Random Allocations* (1978) is a close general reference but was not fully accessible for comparison. The novelty asserted here is not the underlying pair-moment formula: it is the exact global finite-sample sign-variation bound, critical arithmetic window, and sharp heterogeneous boundary.

## Limitations

These results concern cross-covariances of distinct occupancy frequencies, not all dependence orders, joint distribution shape, or statistical test power. The asymptotic window fixes the occupancy indices. The unequal-probability example proves only at least three switches; it does not classify all heterogeneous profiles. Older comprehensive allocation literature could contain an equivalent finite-sample consequence implicitly. All review is same-model; independent audit has not been performed.

## References

1. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387, first public preprint 2008-09-25, https://arxiv.org/abs/0809.4387.
2. V. F. Kolchin, B. A. Sevastyanov and V. P. Chistyakov, *Random Allocations*, V. H. Winston & Sons, 1978.
