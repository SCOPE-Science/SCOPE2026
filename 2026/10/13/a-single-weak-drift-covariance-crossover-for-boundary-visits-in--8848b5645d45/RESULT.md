# A single weak-drift covariance crossover for boundary visits in gambler's ruin

## Finding

Let the nearest-neighbour walk on the integers \(\{0,1,\ldots,m\}\) be absorbed upon reaching either endpoint, and start at a fixed positive integer \(i<m\). Its upward-step probability depends on the upper barrier through \(p_m=(1+e^{-b/m})^{-1}\), for a fixed drift parameter \(b\geq0\). Define the absorption time \(T_m\) and the number \(N_{1,m}\) of visits to state \(1\) before absorption (including time zero when applicable). Then, for each fixed \(i\geq1\) and \(b\geq0\),

\[
\lim_{m\to\infty}\frac{\operatorname{Cov}_i(T_m,N_{1,m})}{m}=F_i(b).
\]

For \(b>0\), writing \(R=e^{-b}\), the limit is

\[
F_i(b)=\frac{4\bigl[((2i-1)+R)(1-R)-b((i-1)+(i+1)R)\bigr]}{b(1-R)^2},
\]

and at the symmetric endpoint \(F_i(0)=2-2i/3\).

The complete sign diagram for this limiting covariance is as follows. For \(i=1\), it is strictly positive for every \(b\geq0\). For \(i=2\), it is positive up to one critical drift \(b_*\), zero there, and negative above it, where \(b_*\approx1.49888421886734\) is the unique positive root of

\[
(3+e^{-b_*})(1-e^{-b_*})=b_*(1+3e^{-b_*}).
\]

For \(i=3\), it is zero at \(b=0\) and strictly negative at every \(b>0\). For every fixed \(i\geq4\), it is strictly negative for all \(b\geq0\). Thus a genuine drift-induced sign reversal in this near-fair regime occurs only for a walk started two lattice sites from the lower absorbing boundary.

## Assumptions and scope

For every integer \(m\geq i+1\), the walk \((X_t)_{t\geq0}\) starts from \(X_0=i\) and, at each nonabsorbing site, moves up with probability \(p_m\) and down with probability \(q_m=1-p_m\). Both endpoints are absorbing. Explicitly,

\[
T_m=\inf\{t\geq0:X_t\in\{0,m\}\},\qquad N_{1,m}=\sum_{t=0}^{T_m-1}\mathbf 1_{\{X_t=1\}}.
\]

The start \(i\) and the parameter \(b\) remain fixed as \(m\to\infty\). The covariance is taken with respect to the law starting at \(i\). The limits are not claimed to hold uniformly when either \(i\) or \(b\) grows with \(m\). The result concerns unconditioned absorption at either boundary, not absorption conditioned on one endpoint.

## Proof

**1. Exact mixed-moment identity.** Let \(Q\) denote the substochastic transition matrix on \(\{1,\ldots,m-1\}\), let \(G=(I-Q)^{-1}=\sum_{t\geq0}Q^t\), and let \(t_a=\mathbb E_a T_m=\sum_k G_{ak}\). The Green entry \(G_{a1}\) is \(\mathbb E_aN_{1,m}\). Expanding the product of the two occupation sums, conditioning after a visit to state \(1\), and using

\[
\sum_{t\geq0}tQ^t=G^2-G,
\]

gives the exact identity

\[
\operatorname{Cov}_i(T_m,N_{1,m})
=G_{i1}(t_1-t_i)+(G^2)_{i1}-G_{i1}.
\tag{1}
\]

For example, the first two terms in the mixed expectation are \(\mathbb E_i[T_mN_{1,m}]=G_{i1}t_1+(G^2-G)_{i1}\). Because the finite chain is absorbed almost surely, the Green matrix and all displayed moments are finite.

**2. Explicit potential kernel.** If \(b>0\), put \(r=q_m/p_m=e^{-b/m}\), \(d=p_m-q_m=(1-r)/(1+r)\). Solving the difference equation for the expected occupation of site \(k\), subject to zero values at both absorbing boundaries, gives

\[
G_{ak}=\begin{cases}
\displaystyle\frac{(1-r^a)(1-r^{m-k})}{d(1-r^m)},&a\leq k,\\[5pt]
\displaystyle\frac{(1-r^k)(r^{a-k}-r^{m-k})}{d(1-r^m)},&a\geq k.
\end{cases}
\tag{2}
\]

The same elementary boundary-value calculation for the mean duration yields

\[
t_a=\frac{m(1-r^a)/(1-r^m)-a}{d},\qquad
G_{a1}=\frac{r^{a-1}-r^{m-1}}{p_m(1-r^m)}.
\tag{3}
\]

Both formulas can also be checked by substitution in \((I-Q)G=I\) and \((I-Q)t=\mathbf{1}\).

**3. Weak-drift limit.** Write \(R=e^{-b}\). For fixed \(i\) and \(b>0\), expansion of (3) gives

\[
G_{i1}\longrightarrow2,\qquad
\frac{t_1-t_i}{m}\longrightarrow2(i-1)\left(\frac1b-\frac1{1-R}\right).
\tag{4}
\]

For a sequence of bulk indices satisfying \(k/m\to x\in(0,1)\) and \(k>i\), formula (2) gives

\[
G_{ik}\longrightarrow\frac{2i(1-e^{-b(1-x)})}{1-R},\qquad
G_{k1}\longrightarrow\frac{2(e^{-bx}-R)}{1-R}.
\tag{5}
\]

These products are uniformly bounded in \(k\) as \(m\to\infty\) with \(i,b\) fixed; the finitely many indices \(k\leq i\) contribute only \(O(1)\). The Riemann-sum limit therefore gives

\[
\lim_{m\to\infty}\frac{(G^2)_{i1}}m
=\frac{4i}{(1-R)^2}\int_0^1(1-Re^{bx})(e^{-bx}-R)\,dx
=4i\left(\frac{1+R}{b(1-R)}-\frac{2R}{(1-R)^2}\right).
\tag{6}
\]

Combining (1), (4), and (6) yields the displayed \(F_i(b)\). At \(b=0\), use the symmetric kernel and durations

\[
G_{ak}=\frac{2\min(a,k)(m-\max(a,k))}{m},\qquad t_a=a(m-a).
\]

Inserting these into (1) and taking the corresponding Riemann sum gives \(F_i(0)=2-2i/3\). This agrees with the continuous limit of the expression at positive \(b\).

**4. Strict sign classification.** For \(b>0\), the denominator of \(F_i(b)\) is positive. Write its numerator divided by four as

\[
H_i(b)=((2i-1)+e^{-b})(1-e^{-b})-b((i-1)+(i+1)e^{-b}).
\]

Direct differentiation shows

\[
H_i(0)=H_i'(0)=0,\qquad H_i''(b)=e^{-b}\bigl[4(1-e^{-b})-(i+1)b\bigr].
\tag{7}
\]

For \(i\geq3\), the strict bound \(1-e^{-b}<b\) implies \(H_i''(b)<0\), hence \(H_i(b)<0\) whenever \(b>0\). For \(i=1\),

\[
H_1(b)=2e^{-b}(\sinh b-b)>0.
\]

For \(i=2\), the function \((1-e^{-b})/b\) is strictly decreasing from \(1\) to \(0\), so (7) changes from positive to negative at exactly one positive argument. Consequently \(H_2'\), which starts at zero and tends to \(-1\), has exactly one positive zero. The function \(H_2\) therefore first increases above zero, then decreases to \(-\infty\); it has precisely one strictly positive root \(b_*\), with the stated sign change. Finally, the endpoint values \(F_i(0)=2-2i/3\) settle the symmetric cases. This proves the theorem.

## Verification

Run the bundled standard-library Python program `python verify_walk_cov.py`. It solves independent exact-rational finite-chain recurrences for the first and mixed moments, checks the potential kernel and identity (1) over multiple sizes, biases and initial sites, evaluates the large-barrier limit numerically, and checks the analytic sign diagram and root bracket. Its reported success line is

`VERIFY_OK exact_finite_independent_conditions=600 asymptotic_sign_root=1.49888421886734`

The universal limiting and uniqueness statements are proved above; finite checks cannot substitute for their proofs.

## Relationship to prior work

The classical gambler's ruin solution supplies the absorbing-walk potential kernel. Van Uem's analysis of stopping strategies and gambler's ruin includes mean absorption-time formulas; no claimed novelty attaches to those marginal expressions. Bénichou and Desbois study joint occupation-time transforms for Brownian motion on graphs with drift, which provide an important continuum comparison but not this discrete starting-site-specific weak-drift sign diagram.

A particularly close predecessor is de Vos and Vervaat's work on joint generating functions of Bernoulli-walk local times at stopping times. Its scope potentially includes mixed occupation moments, and those moment identities are not themselves claimed novel. The contribution assessed here is the explicit fixed-start, near-fair large-barrier scaling and the complete, uniquely located covariance-sign transition. Only the available abstract of that predecessor could be examined, so possible implicit coverage is an acknowledged priority risk.

## Limitations

The theorem does not provide an exact sign classification at each finite \(m\), or for leftward drift, growing starting locations, varying drift scales, conditional exit laws, or general birth-death chains. The comparison with one historically relevant Bernoulli-walk generating-function article is limited by unavailable full text. The numerical checks are supporting evidence and do not establish the asymptotic formulas or uniqueness. Exhaustive historical priority is not established.

## References

1. Olivier Bénichou and Jean Desbois, *Exit and Occupation times for Brownian Motion on Graphs with General Drift and Diffusion Constant*, arXiv:0810.4636v1, first posted 25 October 2008. https://arxiv.org/abs/0810.4636
2. T. J. van Uem, *Stopping strategies and gambler's ruin problem*, arXiv:1302.7247v1, first posted 28 February 2013. https://arxiv.org/abs/1302.7247
3. J. C. de Vos and W. Vervaat, *Local Times of Bernoulli Walk*, Statistica Neerlandica 42 (1988), 1--16. doi:10.1111/j.1467-9574.1988.tb01516.x; earlier Tilburg Research Memorandum FEW 244 (1987).
4. T. L. Hill, *Number of visits to a state in a random walk, before absorption, and related topics*, Proceedings of the National Academy of Sciences 85 (1988), 4577--4579. doi:10.1073/pnas.85.13.4577.
