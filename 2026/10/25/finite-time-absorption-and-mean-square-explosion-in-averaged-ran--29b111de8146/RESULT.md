# Finite-time absorption and mean-square explosion in averaged randomized Kaczmarz

## Finding

For the consistent two-equation system with row matrix \(A=I_2\), consider *parallel averaged randomized Kaczmarz*: at each iteration sample \(q\ge 2\) rows independently and uniformly with replacement, compute their individual Kaczmarz corrections from the **same** current iterate, average those corrections, and multiply the average by a fixed relaxation \(\alpha>0\). Let \(x_*\) be the exact solution, and assume both coordinates of \(e_0=x_0-x_*\) are nonzero.

**Theorem (batch-resonant absorption and a separation of convergence modes).** The iteration reaches \(x_*\) at a finite random iteration almost surely if and only if
\[
\alpha=\frac{q}{j}\quad\text{for some integer }1\le j\le q.
\]
At such a resonance put \(p_j=\binom qj 2^{-q}\), and let \(\tau\) be the first iteration at which the entire error is zero. If \(2j\ne q\), then for every integer \(n\ge0\),
\[
\Pr(\tau>n)=2(1-p_j)^n-(1-2p_j)^n,
\qquad \mathbb E\tau=\frac{3}{2p_j}.
\]
If \(2j=q\), instead \(\Pr(\tau>n)=(1-p_j)^n\) and \(\mathbb E\tau=1/p_j\).

For **every** \(q\ge2\), \(\alpha>0\), and initial error, the squared Euclidean error has the *exact* expectation
\[
\mathbb E\|e_n\|_2^2
=\left(1-\alpha+\frac{q+1}{4q}\alpha^2\right)^n\|e_0\|_2^2.
\]
In particular, for \(q=4\) and \(\alpha=4\), \(\tau<\infty\) almost surely with \(\mathbb E\tau=6\) and
\[
\Pr(\tau>n)=2(3/4)^n-(1/2)^n,
\qquad \mathbb E\|e_n\|_2^2=2^n\|e_0\|_2^2.
\]
Thus exact finite termination almost surely coexists with exponentially *growing* mean-square error.

The separation does **not** require exact resonance. At \(q=4\) and \(\alpha=19/5\), the error never becomes exactly zero when both initial coordinates are nonzero, but
\[
\lim_{n\to\infty}\frac1n\log\|e_n\|_2
=\frac1{16}\log\left(\frac{6972041972007}{64000000000000000}\right)<0
\quad\text{almost surely},
\]
whereas
\[
\mathbb E\|e_n\|_2^2=\left(\frac{137}{80}\right)^n\|e_0\|_2^2.
\]
Both strict inequalities persist for all relaxation parameters in some open neighborhood of \(19/5\), so the almost-sure-versus-mean-square separation is robust.

## Assumptions and scope

All operations are in exact real arithmetic. The system is \(Ax=b\) with \(A=I_2\), so \(x_*=b\). At each integer iteration \(n\ge0\), draw \(q\) independent indices \(I_{n,1},\ldots,I_{n,q}\), each uniform on \(\{1,2\}\); all draws are independent across iterations. The update is
\[
x_{n+1}=x_n-\frac\alpha q\sum_{s=1}^q
\bigl(x_{n,I_{n,s}}-b_{I_{n,s}}\bigr)\mathbf e_{I_{n,s}}.
\]
Here \(\mathbf e_1,\mathbf e_2\) are coordinate unit vectors, and the sum uses a shared pre-update iterate \(x_n\). This is not sequential randomized Kaczmarz and is not sampling without replacement. The stopping time \(\tau\) is the *first positive* integer with \(x_\tau=x_*\). If either initial error coordinate is already zero, only the remaining coordinate's geometric waiting time is needed; the two-coordinate stopping law above is stated for both initially nonzero.

## Proof

Let \(K_n=\#\{s:I_{n,s}=1\}\). The variables \(K_n\) are independent with \(K_n\sim\operatorname{Bin}(q,1/2)\). Subtracting the exact solution from the update gives
\[
e_{n+1,1}=\left(1-\frac{\alpha K_n}{q}\right)e_{n,1},\qquad
e_{n+1,2}=\left(1-\frac{\alpha(q-K_n)}q\right)e_{n,2}.
\tag{1}
\]

**Exact absorption.** A currently nonzero first coordinate is annihilated in an iteration exactly when \(K_n=q/\alpha\). The second coordinate is annihilated exactly when \(K_n=q-q/\alpha\). For either event to be possible, \(q/\alpha\) must be an integer \(j\in\{1,\ldots,q\}\). If it is not, (1) multiplies each initially nonzero coordinate only by nonzero factors at all finite times; consequently finite termination is impossible. If it is, each coordinate's annihilation event has probability \(p_j=\binom qj/2^q>0\) independently on successive iterations. Both events therefore occur in finite time almost surely, after which the respective coordinates remain zero. If \(j\ne q-j\) these are two disjoint types of events per iteration. Inclusion-exclusion for the event that at least one type has not appeared in the first \(n\) iterations gives \(2(1-p_j)^n-(1-2p_j)^n\). If \(j=q-j\), one event kills both coordinates and the survival probability is \((1-p_j)^n\). Summation of the survival probabilities over \(n\ge0\) yields the stated expectations.

**Second moment.** Binomial moments give \(\mathbb EK_n=q/2\) and \(\mathbb EK_n^2=q(q+1)/4\). Hence
\[
\mathbb E\left(1-\frac{\alpha K_n}{q}\right)^2
=1-\alpha+\frac{q+1}{4q}\alpha^2=:m_q(\alpha).
\]
The other coordinate has the same multiplier distribution. Conditional on the past, (1) thus implies \(\mathbb E(\|e_{n+1}\|_2^2\mid e_n)=m_q(\alpha)\|e_n\|_2^2\). Iteration proves the expectation formula without assuming independence between the two coordinates. At \((q,\alpha)=(4,4)\), \(m_4(4)=2\), \(j=1\), and \(p_1=4/16=1/4\); substitution establishes the announced law and \(\mathbb E\tau=6\).

**Nonresonant, robust separation.** Put \(q=4\) and \(\alpha=19/5\). The five possible first-coordinate multipliers, corresponding to \(K_n=0,1,2,3,4\), are
\[
1,\quad 1/20,\quad -9/10,\quad -37/20,\quad -14/5.
\]
They are nonzero and occur with respective probabilities \((1,4,6,4,1)/16\). Therefore the strong law of large numbers applied to their logarithmic absolute values yields the Lyapunov exponent
\[
\gamma=\frac1{16}\log\!\left[
(1/20)^4(9/10)^6(37/20)^4(14/5)
\right]
=\frac1{16}\log\!\left(\frac{6972041972007}{64000000000000000}\right)<0.
\]
The second-coordinate multiplier has exactly the same distribution. Applying the strong law to both coordinate products, and using that both initial coordinates are nonzero, gives \(\lim n^{-1}\log\|e_n\|_2=\gamma\) almost surely. The second-moment multiplier is \(m_4(19/5)=137/80>1\). The two strict inequalities \(\gamma<0\) and \(m_4(\alpha)>1\) are continuous in \(\alpha\) near \(19/5\), because all five possible multipliers remain nonzero there. Their simultaneous validity therefore holds on an open interval. This completes the proof.

## Verification

Run the accompanying standalone exact-arithmetic checker with `python3 check.py`. It checks the binomial extinction events over multiple batch sizes, exact survival identities, direct finite-horizon state-distribution enumeration for both highlighted relaxation parameters, and the rational Lyapunov-product and second-moment constants. No simulation or finite enumeration is used to infer the universal or almost-sure statements: the proof above supplies those steps.

## Relationship to prior work

Moorman, Tu, Molitor, and Needell (2020) analyze a parallel averaged randomized Kaczmarz update with independent row samples. Their uniform-weight analysis gives mean-square bounds and overrelaxation guidance, including the general quadratic multiplier that specializes to the present second-moment formula. The present claim does **not** regard that moment identity alone as new; it concerns the exact finite-absorption classification and the contrast with almost-sure stability outside the mean-square stability region.

Tondji and Lorenz (2022) analyze randomized sparse Kaczmarz by averaging. Their update reduces to the present rule when the shrinkage threshold is zero and the system has two orthogonal unit rows. Their stated conclusions address expected/Bregman convergence under relaxation restrictions, not the above almost-sure finite hitting law or the nonresonant pathwise-versus-mean-square separation. The classical orthogonal-row coupon-collection behavior of the unrelaxed Kaczmarz method is a familiar boundary case, not itself claimed as new.

## Limitations

The exact absorption classification depends on orthogonal coordinate rows, independent draws with replacement, shared-iterate averaging, and exact arithmetic. It does not classify nonorthogonal matrices, noisy/inconsistent systems, or soft-thresholded sparse Kaczmarz with a positive threshold. Exact finite hitting at \(\alpha=q/j\) is sensitive to perturbing the relaxation parameter; the exhibited *asymptotic* separation, by contrast, persists on an open interval around \(19/5\). The result does not imply that typical large finite-precision trajectories exhibit growing errors: rare events can dominate the mathematical expectation, and floating-point behavior requires its own analysis.

## References

1. J. D. Moorman, T. K. Tu, D. Molitor, and D. Needell, *Randomized Kaczmarz with Averaging*, arXiv:2002.04126 (first posted 2020-02-10). In particular, the uniform-weight update and its mean-square bound.
2. L. Tondji and D. A. Lorenz, *Faster Randomized Block Sparse Kaczmarz by Averaging*, arXiv:2203.10838 (first posted 2022-03-21), later *Numerical Algorithms* 93 (2023), DOI: 10.1007/s11075-022-01473-x. In particular, Equation (1.8) and the overrelaxation discussion.
