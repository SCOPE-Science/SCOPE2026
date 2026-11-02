# Cubic variance reversal at the fast-refresh boundary of a random-environment walk

## Finding

The limiting annealed diffusivity of a nearest-neighbour walk in an independently regenerating one-dimensional random environment has a universal third-order fast-refresh expansion. For the mean site drift \(m=2\mathbb E\omega_0-1\), site-disorder variance \(s=\operatorname{Var}(\omega_0)\), and failure-to-refresh probability \(q=1-p\),
\[
\sigma^2(1-q)=1-m^2+12sm^2q^2-8s^2q^3+O(q^4).
\]
The remainder is uniform over all site laws on \([0,1]\). Consequently, for any nonconstant environment with \(m=0\), complete refreshing is a **strict one-sided local maximum** of the effective variance, whereas the previously known fixed nonzero-drift case has a strict local minimum.

Moreover, consider any family of iid site laws indexed by \(q\downarrow0\), for which \(s(q)\to s_0>0\) and \(m(q)^2/q\to\tau\in[0,\infty)\). The crossover has the explicit limit
\[
\lim_{q\downarrow0}\frac{\sigma_q^2(1-q)-(1-m(q)^2)}{q^3}
=12s_0\tau-8s_0^2.
\]
The sign is negative for \(\tau<2s_0/3\) and positive for \(\tau>2s_0/3\); the equality case needs higher-order analysis. This extends the known second derivative calculation to the singular, nearly unbiased regime rather than claiming that quadratic result again.

## Assumptions and scope

On the integer line, choose iid random variables \(\omega_x\in[0,1]\), with \(\omega_x\) the conditional probability of a right step upon departing site \(x\). At each discrete time, a walk at \(x\) moves to \(x+1\) with probability \(\omega_x\), otherwise to \(x-1\); after the step, independently refresh the entire field by a fresh iid copy with probability \(p\in(0,1]\). This is the one-dimensional nearest-neighbour model of Martin--Nagel (2026). All laws are annealed over sites, steps and regeneration events. No ellipticity beyond \(0\le\omega_x\le1\) is necessary when \(p>0\). Define \(v(p)\) as the almost-sure speed and \(\sigma^2(p)\) by the annealed central-limit theorem for \((X_n-nv(p))/\sqrt n\). The claim concerns the one-sided limit \(p\uparrow1\), and does not assert monotonicity over the entire interval.

Write \(\mu=\mathbb E\omega_0\), \(m=2\mu-1\), \(s=\mathbb E(\omega_0-\mu)^2\), and \(q=1-p\). All constants appearing in the error bound can be chosen independently of the law of \(\omega_0\), because single-step displacement has absolute value one.

## Proof

**1. Exact regeneration formulas.** Let \(Z_n\) be the corresponding walk started at zero in a single unchanging iid field, let \(A_n=\mathbb E Z_n\), and let \(B_n=\mathbb E Z_n^2\). Complete-field regenerations produce iid space-time blocks \((T,Y)\), with \(\mathbb P(T=n)=p q^{n-1}\) and the conditional law of \(Y\) given \(T=n\) equal to the law of \(Z_n\). The renewal-reward strong law and central-limit theorem give, exactly,
\[
 v(p)=p^2\sum_{n\ge1}q^{n-1}A_n,
\qquad
 \sigma^2(p)=p^2\sum_{n\ge1}q^{n-1}
 [B_n-2n v(p)A_n+n^2v(p)^2].
\]
Indeed, \(\mathbb ET=1/p\), and the asymptotic variance per step is \(\mathbb E(Y-vT)^2/\mathbb ET\). The remainder of the last incomplete block is negligible under the geometric tail, so the formula applies to the original walk at deterministic times.

**2. Four static-block moments.** For any fixed path of \(n\) steps, let \(R_x\) and \(L_x\) count right and left departures from site \(x\). Annealing over iid site transition probabilities gives the exact path weight
\[
\mathbb P(\text{path})=
\prod_{x\in\mathbb Z}\mathbb E[\omega_0^{R_x}(1-\omega_0)^{L_x}].
\]
When \(n\le4\), no site is departed more than twice. Hence the weights depend only on \(\mu\) and \(s\), through
\[
\begin{aligned}
\mathbb E\omega_0^2&=\mu^2+s,\\
\mathbb E(1-\omega_0)^2&=(1-\mu)^2+s,\\
\mathbb E[\omega_0(1-\omega_0)]&=\mu(1-\mu)-s.
\end{aligned}
\]
Enumerating the \(2^n\) paths for the first four block lengths yields the following exact identities (not simulations):
\[
\begin{array}{c|cc}
n&A_n&B_n\\\hline
1&m&1\\
2&2m&2+2m^2\\
3&(3-2s)m&3+6m^2\\
4&4(1-s)m&4+12m^2-8sm^2-8s^2.
\end{array}
\]
For an explicit analytic check of the only new fourth-step algebra, write \(u=\mu\) and \(c=2u(1-u)-s\). The path enumeration gives \(\mathbb P(Z_4=4)=u^4\), \(\mathbb P(Z_4=-4)=(1-u)^4\), and
\[
\begin{aligned}
\mathbb P(Z_4=2)&=(2u^2+s)c,\\
\mathbb P(Z_4=-2)&=(2(1-u)^2+s)c.
\end{aligned}
\]
The remaining mass is at zero. It follows directly that \(A_4=4[\mathbb P(Z_4=4)-\mathbb P(Z_4=-4)]+2[\mathbb P(Z_4=2)-\mathbb P(Z_4=-2)]\) and \(B_4=16[\mathbb P(Z_4=4)+\mathbb P(Z_4=-4)]+4[\mathbb P(Z_4=2)+\mathbb P(Z_4=-2)]\), simplifying to the table. For the third step the nonextreme masses are \(\mathbb P(Z_3=1)=3u^2(1-u)+s(1-2u)\) and \(\mathbb P(Z_3=-1)=3u(1-u)^2+s(2u-1)\), with extreme masses \(u^3\) and \((1-u)^3\). These identities also give the third-step row, making the finite moments independently reconstructible without executing software. The exact-fraction checker corroborates them under eight rational site laws.

**3. Expansion and uniform control.** In the speed identity, expand \(p^2=(1-q)^2\), insert the first four \(A_n\), and use \(|A_n|\le n\). Termwise expansion gives
\[
 v(1-q)=m-2msq^2+O(q^4).
\]
In the variance identity, substitute this expression and the four \(A_n,B_n\). Collecting coefficients of \(q^0,q^1,q^2,q^3\) yields, respectively, \(1-m^2\), \(0\), \(12sm^2\), and \(-8s^2\). Therefore
\[
 \sigma^2(1-q)=1-m^2+12sm^2q^2-8s^2q^3+O(q^4).
\]
All remainders are uniform in the site law: \(|A_n|\le n\), \(0\le B_n\le n^2\) and \(|v(p)|\le1\), so the discarded \(n\ge5\) contributions are at most a universal constant times \(\sum_{n\ge5}n^2q^{n-1}=O(q^4)\) for \(0\le q\le1/2\). The nonlinear substitution of the speed has the same uniform order because the speed remainder is uniform and finite moments are bounded. These bounds also justify every power-series manipulation.

**4. Reversal and boundary scaling.** For any fixed law with \(s>0\) and \(m=0\), the cubic coefficient is strictly negative, establishing the local maximum at complete refresh. For a triangular family \(s(q)\to s_0>0\) and \(m(q)^2/q\to\tau\), subtract the complete-refresh variance \(1-m(q)^2\), divide by \(q^3\), and pass to the limit using the uniform \(O(q^4)\) remainder. The resulting coefficient is \(12s_0\tau-8s_0^2\). Its nonzero sign determines the strict inequality at sufficiently small \(q\).

## Verification

Run the standalone standard-library script `checker.py` using `python checker.py`. It independently enumerates all static-walk paths of lengths one through four under eight nontrivial rational site distributions; checks their first two moments and the derived coefficient identities with exact fractions; and makes an additional explicit finite-rate check through length twelve for a symmetric disordered field. The recorded `checker-output.txt` contains the actual results: 129 exact rational assertions passed, together with a conservative bound on truncating the geometric renewal series. No floating-point estimate is used to certify the coefficient identity or the infinite asymptotic statement.

## Relationship to prior work

Martin and Nagel, *Random walk in a regenerating random environment* (arXiv:2610.11919v1, first public October 8, 2026), define precisely this global-refresh model, prove the renewal formulas and show \((\sigma^2)'(1)=0\) and \((\sigma^2)''(1)=24sm^2\). Their Theorem 2.4 establishes a strict local **minimum** when \(s>0\) and \(m\ne0\). Thus the positive quadratic term here is existing work, not an original finding. The new statement identifies \((\sigma^2)'''(1)=48s^2\), the zero-drift **maximum**, and the sharp nearly-zero-drift crossover. The primary paper's proof through Lemma 3.3 computes the second derivative but not this third derivative or the crossover.

Avena and collaborators' cooling random-environment literature, including *Random walk in cooling random environment: ergodic limits and concentration inequalities* (arXiv:1803.03295) and *A cohesive account on ergodic behaviours and scaling limits of Random Walks in Cooling Random Environments* (arXiv:2603.22652), supplies related regeneration/limit frameworks, particularly for cooling intervals tending to infinity, rather than the small-failure finite-geometric calculation. A search for equivalent universal cubic coefficients, zero-mean maximum and near-unbiased scaling did not identify a matching statement in the inspected literature. This is a qualified best-knowledge priority assessment, not a historical uniqueness certificate.

## Limitations

The result requires independent complete refreshing and iid sites and gives only a one-sided local expansion near \(p=1\). The critical equality \(\tau=2s_0/3\) is unresolved at this order. At fixed nonzero \(m\), the leading positive quadratic correction is already in Martin--Nagel. Other renewal laws, correlated environments and higher-dimensional walks are not covered. Independent mathematical audit and exhaustive historical-priority certification have not been performed.

## References

Martin, R., and Nagel, J. (2026). *Random walk in a regenerating random environment*. arXiv:2610.11919v1, first public 2026-10-08. https://arxiv.org/abs/2610.11919

Avena, L., et al. (2018). *Random walk in cooling random environment: ergodic limits and concentration inequalities*. arXiv:1803.03295. https://arxiv.org/abs/1803.03295

Avena, L., and da Costa, C. (2026). *A cohesive account on ergodic behaviours and scaling limits of Random Walks in Cooling Random Environments*. arXiv:2603.22652. https://arxiv.org/abs/2603.22652
