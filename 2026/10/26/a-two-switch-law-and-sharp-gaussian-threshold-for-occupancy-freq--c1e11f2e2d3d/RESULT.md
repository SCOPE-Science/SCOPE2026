# A two-switch law and sharp Gaussian threshold for occupancy-frequency covariances

## Finding

Allocate \(n\ge2\) independent, equiprobable balls to \(m\ge3\) labelled boxes. Let \(N_i\) be box \(i\)'s load and \(M_r=\sum_{i=1}^{m}\mathbf1\{N_i=r\}\), for integer \(0\le r\le n\). For \(r\ne s\) the cross-frequency covariance has a complete finite sign constraint: it may be negative, then positive, then negative as \(s\) increases, but it **cannot alternate more often**. Both reversals occur already at \((m,n,r)=(3,15,3)\). A second theorem gives the sharp fixed-\(m\), many-ball Gaussian threshold at which any positive off-diagonal covariance becomes possible.

Define \(p_r=\binom nr m^{-r}(1-1/m)^{n-r}\), and
\[
 p_{r,s}=\begin{cases}\dfrac{n!}{r!s!(n-r-s)!}m^{-r-s}(1-2/m)^{n-r-s},&r+s\le n,\\0,&r+s>n.\end{cases}
\]
Write \(Q_{r,s}=(m-1)p_{r,s}/(mp_rp_s)\) and \(B_{r,s}=m^2p_rp_s(Q_{r,s}-1)\). For distinct \(r,s\), \(B_{r,s}=\operatorname{Cov}(M_r,M_s)\). **For \(r=s\), \(B_{r,r}\) is an auxiliary off-diagonal box-pair contribution, not \(\operatorname{Var}(M_r)\).** For each fixed \(r\), the indices \(s\in\{0,\ldots,n\}\) with \(B_{r,s}>0\) form one (possibly empty) integer interval. Consequently the sequence \(B_{r,0},\ldots,B_{r,n}\) has at most two strict sign reversals after any zeros are ignored.

More sharply, fix \(m\ge3\), let \(\sigma_n=\sqrt{n(m-1)/m^2}\), and choose \(r_n\) with \((r_n-n/m)/\sigma_n\to x\). Set
\[
 \rho=-\frac1{m-1},\qquad a_m=\frac{m-1}{m\sqrt{1-\rho^2}}\in(0,1),\qquad c_m=\sqrt{-2\log a_m}.
\]
Then
\[
 \lim_{n\to\infty}\max_{0\le s\le n}Q_{r_n,s}=a_m e^{x^2/2}.
\]
If \(|x|<c_m\), every \(B_{r_n,s}<0\) for all sufficiently large \(n\), thus all true cross-frequency covariances with \(s\ne r_n\) are negative. If \(|x|>c_m\), the auxiliary sign profile has exactly two reversals for all sufficiently large \(n\), and the positive band contains true \(s\ne r_n\) covariances. No critical-point claim is made for \(|x|=c_m\).

## Assumptions and scope

All balls choose boxes independently with probability \(1/m\). Parameters \(m,n,r,s\) are integers with \(m\ge3\), \(n\ge2\), \(0\le r,s\le n\). The finite covariance identity is restricted to \(r\ne s\); the auxiliary kernel \(B\) is defined for all \(r,s\). Limits fix \(m\) and take \(n\to\infty\); they do not claim a simultaneous many-box limit. At the threshold \(|x|=c_m\), lower-order terms can matter.

## Proof

**1. Pairwise enumeration.** For a marked box, \(\mathbb P(N_1=r)=p_r\). For two different marked boxes, multinomial enumeration gives \(\mathbb P(N_1=r,N_2=s)=p_{r,s}\). Expanding \(M_rM_s\) for \(r\ne s\) leaves only ordered distinct box pairs, because no box has two unequal loads. Thus
\[
 \mathbb E M_r=mp_r,\qquad \mathbb E[M_rM_s]=m(m-1)p_{r,s},\qquad
 \operatorname{Cov}(M_r,M_s)=m^2p_rp_s(Q_{r,s}-1).
\]
All \(p_r\) are strictly positive, so the sign is exactly that of \(Q_{r,s}-1\).

**2. Exact one-band law.** For \(0\le s<n-r\), cancellation of consecutive binomial factors gives
\[
 \frac{Q_{r,s+1}}{Q_{r,s}}=
 \frac{n-r-s}{n-s}\frac{m-1}{m-2}.
\]
For \(r>0\) this ratio decreases strictly with \(s\): the factor \(1-r/(n-s)\) decreases. It crosses one, if at all, at \(s=n-(m-1)r\), possibly with a two-term plateau. Therefore \(Q_{r,s}\) is unimodal on \(0\le s\le n-r\). If \(s>n-r\), \(Q_{r,s}=0\), preserving unimodality. For \(r=0\) the displayed ratio is the constant \((m-1)/(m-2)>1\), followed by no forbidden-tail indices, so the sequence increases. A positive superlevel set of a positive unimodal sequence is an integer interval. The stated sign constraint follows. No assumption of nonzero covariance is needed; zeros may occur only on interval boundaries (or on a maximal plateau).

**3. Attainment of two reversals.** Exact rational substitution into the displayed probabilities for \((m,n,r)=(3,15,3)\) gives \(Q_{3,6}<1<Q_{3,7}\) and \(Q_{3,11}>1>Q_{3,12}\). By unimodality, indices \(0\) through \(6\) have negative \(B\), \(7\) through \(11\) positive \(B\), and \(12\) through \(15\) negative \(B\). The \(s=3\) entry is only auxiliary; removing it yields the asserted signs of true \(\operatorname{Cov}(M_3,M_s)\).

**4. Local central window.** For fixed \(m\) the first two loads are the first two coordinates of a multinomial vector. Their means are \(n/m\), variances are \(\sigma_n^2\), and their correlation is \(\rho=-1/(m-1)\). Using Stirling's factorial expansion in the exact one- and two-box mass functions uniformly when both standardized deviations remain in compact sets gives the bivariate lattice local limit
\[
 Q_{r_n,s_n}\longrightarrow
 a_m\exp\!\left(\frac{\rho xy-\rho^2(x^2+y^2)/2}{1-\rho^2}\right)
 =a_m e^{x^2/2}\exp\!\left[-\frac{\rho^2}{2(1-\rho^2)}\left(y-\frac{x}{\rho}\right)^2\right],
\]
whenever \((r_n-n/m)/\sigma_n\to x\) and \((s_n-n/m)/\sigma_n\to y\). The constant \(a_m<1\) follows by squaring: \(m^3(m-2)-(m-1)^4=2m(m-1)(m-2)-1>0\) for every \(m\ge3\).

**5. Sharp global maximum and threshold.** The adjacent-ratio formula locates every maximizer of \(Q_{r_n,s}\) at one of the integers adjacent to \(n-(m-1)r_n\), which equals \(n/m-(m-1)x\sigma_n+o(\sigma_n)\). This is an admissible interior load for all large \(n\). Its standardized displacement tends to \(x/\rho\). The local limit applied at that actual maximizer yields the global maximum limit \(a_m e^{x^2/2}\). If \(|x|<c_m\), this limit is less than one, hence every finite-\(n\) ratio is below one eventually. If \(|x|>c_m\), the limiting maximum exceeds one; the Gaussian expression is below one at two suitably chosen, fixed standardized values of \(y\) on opposite sides of \(x/\rho\). Taking integer loads at these values forces negative-positive-negative signs, and unimodality rules out any further reversals. Since \(x\ne0\), positive loads close to the maximizing position have \(s_n\ne r_n\) for all large \(n\), establishing actual positive cross-frequency covariance.

## Verification

Run `python3 check.py` using only the Python standard library. The checker enumerates all allocation strings for \(3\)–\(5\) boxes at small sample sizes, independently compares exact-rational off-diagonal covariances with the formula, verifies thousands of adjacent-ratio identities as exact fractions, checks the full two-reversal witness, and checks numerical convergence toward the Gaussian maximum. The analytic arguments above, not the finite computations, prove the all-parameter and asymptotic statements.

## Relationship to prior work

Exact occupancy probability laws and covariance matrix asymptotics are classical. The off-diagonal multinomial mass formula is not claimed to be new. A published 2011 discussion explicitly records the standard many-box Poisson-regime covariance matrix for occupancy frequency counts. Barbour and Gnedin (2008) study joint normal approximations and correlation structure for infinitely many boxes with unequal probabilities. O'Neill's 2019 publicly posted occupancy study develops computation and moments of the number of occupied boxes, and his 2022 follow-up treats an extended occupancy Markov chain. These prior frameworks are distinct from the finite two-reversal classification and the *fixed number of boxes* standardized positive-covariance threshold established here. A related published occupancy-richness analysis determines the sign of \(\operatorname{Cov}(K,M_r)\), where \(K=\sum_{s\ge1}M_s\); a single sum over frequencies cannot determine the individual cross-covariance signs classified here.

## Limitations

The diagonal \(r=s\) is intentionally excluded from the covariance-sign claim, as it is a variance and has an additional same-box contribution. The Gaussian threshold is for fixed \(m\), not for \(m\to\infty\), and there is no boundary assertion when \(|x|=c_m\). The finite no-more-than-two-reversals statement allows exact zero covariances. No joint CLT for frequency-count statistics is claimed. Historical priority remains uncertain because not all older occupancy literature was accessible in full.

## References

1. B. O'Neill, *The Classical Occupancy Distribution: Computation and Approximation*, accepted author version posted 2019-12-19, DOI: 10.1080/00031305.2019.1699445.
2. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387 (2008), especially §§1–3, 5.
3. B. O'Neill, *Three Distributions in the Extended Occupancy Problem*, arXiv:2209.02220 (2022).
4. *Covariance of counts of bins having specified counts of balls*, Mathematics Stack Exchange, question 87779 (2011), for the previously known many-box asymptotic covariance matrix.
5. *A one-switch covariance law for occupancy richness and frequency counts*, public mathematical research record (2026), identifier `2026/10/4/93dddb2be813`.
