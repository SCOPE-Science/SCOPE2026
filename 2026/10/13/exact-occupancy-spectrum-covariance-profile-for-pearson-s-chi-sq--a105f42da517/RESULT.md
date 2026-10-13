# Exact occupancy-spectrum covariance profile for Pearson's chi-square
## Finding
Let
\[
(N_1,\ldots,N_m)\sim\operatorname{Multinomial}
\left(n;\frac1m,\ldots,\frac1m\right),
\qquad m,n\ge2.
\]
For \(0\le r\le n\), define the frequency-of-frequencies coordinate
\[
K_r=\sum_{a=1}^m\mathbf 1\{N_a=r\},
\]
so \(K_r\) is the number of cells hit exactly \(r\) times. Let
\[
Q=\sum_{a=1}^m\frac{(N_a-n/m)^2}{n/m}
\]
be Pearson's chi-square statistic for the equal-cell null, and write
\[
p_r=\Pr(N_1=r)
=\binom nr m^{-r}\left(1-\frac1m\right)^{n-r}.
\]
Then
\[
\mathbb E K_r=mp_r
\]
and the exact finite-sample covariance is
\[
\boxed{
\operatorname{Cov}(K_r,Q)
=
\mathbb E K_r\,
\frac{\Delta_{n,m,r}}{n(m-1)},
}
\]
where
\[
\boxed{
\Delta_{n,m,r}
=
n(n-1)-2mr(n-1)+m^2r(r-1).
}
\]

For singleton cells this reduces to
\[
\boxed{
\operatorname{Cov}(K_1,Q)
=
\mathbb E K_1\,
\frac{(n-1)(n-2m)}{n(m-1)}.
}
\]
Hence singleton count and Pearson's statistic are negatively correlated in covariance sign when \(n<2m\), exactly uncorrelated when \(n=2m\), and positively correlated when \(n>2m\).

At the empty-cell end,
\[
\operatorname{Cov}(K_0,Q)
=
\mathbb E K_0\frac{n-1}{m-1}>0.
\]
Since the number of occupied cells is \(m-K_0\), this is consistent with the negative coupling between observed richness and collision intensity.

Pearson's variance also has the exact simple form
\[
\boxed{
\operatorname{Var}(Q)=\frac{2(m-1)(n-1)}{n}.
}
\]
For the variance of one occupancy count, put
\[
p_{rr}
=
\begin{cases}
\displaystyle
\frac{n!}{r!^2(n-2r)!}
\frac{(m-2)^{n-2r}}{m^n},&2r\le n,\\[8pt]
0,&2r>n.
\end{cases}
\]
Then
\[
\operatorname{Var}(K_r)
=
mp_r(1-p_r)+m(m-1)(p_{rr}-p_r^2).
\]
This gives an explicit finite correlation whenever \(\operatorname{Var}(K_r)>0\).

There is a clean fixed-load limit. If \(r\) is fixed and
\[
\frac nm\longrightarrow\lambda\in(0,\infty),
\]
write
\[
\pi_r(\lambda)=e^{-\lambda}\frac{\lambda^r}{r!}
\]
and
\[
v_r(\lambda)
=
\pi_r(1-\pi_r)
-
\pi_r^2\frac{(r-\lambda)^2}{\lambda}.
\]
Then
\[
\frac{\operatorname{Var}(K_r)}m\longrightarrow v_r(\lambda),
\]
\[
\frac{\operatorname{Cov}(K_r,Q)}m
\longrightarrow
\frac{\pi_r(\lambda)}{\lambda}
\left((\lambda-r)^2-r\right),
\]
and therefore
\[
\boxed{
\operatorname{Corr}(K_r,Q)
\longrightarrow
\frac{\pi_r(\lambda)((\lambda-r)^2-r)/\lambda}
{\sqrt{2v_r(\lambda)}}.
}
\]
For \(r\ge1\), the limiting covariance is negative exactly when
\[
r-\sqrt r<\lambda<r+\sqrt r,
\]
zero at the two boundaries, and positive outside. Thus the second-order polynomial
\[
(\lambda-r)^2-r
\]
organizes which occupancy-frequency layers move with or against Pearson's quadratic goodness-of-fit fluctuation.

## Assumptions and scope
The model is the finite equal-probability occupancy model, equivalently an equiprobable multinomial sample. The statistic \(K_r\) counts cells with exactly \(r\) observations; \(r=0\) is included.

The formulas are exact for every finite \(m,n\ge2\). The fixed-load correlation limit keeps \(r\) fixed while \(m,n\to\infty\) and \(n/m\to\lambda\in(0,\infty)\).

No independence claim is made. Zero covariance at a load boundary is only a second-moment orthogonality statement.

## Proof
Introduce the pair-collision count
\[
C=\sum_{a=1}^m\binom{N_a}{2}.
\]
Because
\[
\sum_aN_a=n,
\]
we have
\[
\sum_a N_a^2=n+2C.
\]
A direct expansion of Pearson's statistic gives
\[
Q
=
\frac mn\sum_aN_a^2-n
=
m-n+\frac{2m}{n}C.
\]
Thus it suffices to compute \(\operatorname{Cov}(K_r,C)\).

By symmetry,
\[
\mathbb E K_r=mp_r.
\]
Condition on the event \(N_1=r\). The remaining \(n-r\) balls are independently and uniformly allocated among the other \(m-1\) cells. Hence the expected number of colliding pairs is
\[
\mathbb E[C\mid N_1=r]
=
\binom r2+\frac1{m-1}\binom{n-r}{2}.
\]
Unconditionally, each of the \(\binom n2\) pairs collides with probability \(1/m\), so
\[
\mathbb EC=\frac1m\binom n2.
\]
Using \(K_r=\sum_a\mathbf1\{N_a=r\}\), symmetry now yields
\[
\operatorname{Cov}(K_r,C)
=
mp_r
\left(
\binom r2+\frac1{m-1}\binom{n-r}{2}
-\frac1m\binom n2
\right).
\]
Multiplication by \(2m/n\) and elementary simplification give
\[
\operatorname{Cov}(K_r,Q)
=
mp_r\frac{n(n-1)-2mr(n-1)+m^2r(r-1)}{n(m-1)}.
\]
This proves the finite covariance formula and the singleton and empty-cell specializations.

For the variance of \(Q\), write
\[
C=\sum_{1\le i<j\le n}J_{ij},
\qquad
J_{ij}=\mathbf1\{X_i=X_j\}.
\]
Every \(J_{ij}\) has success probability \(1/m\). Any two distinct pair indicators are pairwise independent: disjoint pairs are independent by the sampling model, while for overlapping pairs
\[
\Pr(X_i=X_j=X_k)=\frac1{m^2}
=
\Pr(X_i=X_j)\Pr(X_i=X_k).
\]
Therefore
\[
\operatorname{Var}(C)
=
\binom n2\frac1m\left(1-\frac1m\right),
\]
and the affine relation between \(Q\) and \(C\) gives
\[
\operatorname{Var}(Q)=\frac{2(m-1)(n-1)}n.
\]

For \(K_r\), two distinct specified cells both have occupancy \(r\) with probability \(p_{rr}\). The indicator-sum variance formula gives
\[
\operatorname{Var}(K_r)
=mp_r(1-p_r)+m(m-1)(p_{rr}-p_r^2).
\]

Finally, when \(n/m\to\lambda\) with fixed \(r\), routine factorial expansions give
\[
p_r\to\pi_r(\lambda),
\]
\[
\frac{\operatorname{Var}(K_r)}m
\to
\pi_r(1-\pi_r)-\pi_r^2\frac{(r-\lambda)^2}{\lambda},
\]
and
\[
\frac{\Delta_{n,m,r}}{m^2}
\to
(\lambda-r)^2-r.
\]
Together with \(\operatorname{Var}(Q)/m\to2\), these limits prove the correlation formula and its sign classification.

## Verification
The accompanying `checker.py` uses exact rational arithmetic to enumerate every allocation for a grid of small \((m,n)\), recompute \(K_r\), collisions, and Pearson's statistic, and compare the empirical finite probability law with the displayed covariance formula for every \(r\).

A second exact loop checks the closed variance formulas, the two conservation identities
\[
\sum_{r=0}^n\operatorname{Cov}(K_r,Q)=0
\]
and
\[
\sum_{r=0}^n r\operatorname{Cov}(K_r,Q)=0,
\]
which follow from \(\sum_rK_r=m\) and \(\sum_rrK_r=n\), and the singleton orthogonality at \(n=2m\).

The finite replay is supplementary. The proof establishes the theorem for all allowed parameters.

## Relationship to prior work
Barbour and Gnedin study occupancy counts \(X_{n,r}\), the numbers of boxes hit exactly \(r\) times, and develop joint normal approximation and covariance structures for these frequency counts. Their full article includes explicit moment formulas in a Poissonized occupancy model. The inspected text does not introduce Pearson's statistic or derive the mixed covariance above.

Nakata studies collision counts in occupancy problems, including exact distributions, factorial moments, negative association, and limit theorems. That work supplies a close collision-based probabilistic context but concerns a different collision statistic and does not state the frequency-count versus Pearson covariance profile.

The present result identifies an exact finite bridge between the frequency-of-frequencies spectrum and Pearson's classical quadratic statistic. The load-dependent sign changes are not visible from marginal occupancy-count moments alone.

## Limitations
Equal cell probabilities are essential to the one-polynomial formula. Under unequal multinomial probabilities, conditioning on one cell occupancy changes the collision expectation through the full remaining probability vector.

The fixed-load result keeps \(r\) fixed. It does not describe regimes where \(r\) itself grows with \(m\) or \(n\).

The finite covariance is elementary enough that an equivalent expression may occur in older occupancy or goodness-of-fit literature under different notation; targeted searches and the closest inspected primary sources did not locate it.

## References
1. A. D. Barbour and A. V. Gnedin, “Small counts in the infinite occupancy scheme,” arXiv:0809.4387, first submitted 25 September 2008.
2. T. Nakata, “The Number of Collisions for the Occupancy Problem with Unequal Probabilities,” *Advances in Applied Probability* 46 (2014), 168–185. DOI: 10.1239/aap/1396360108.
