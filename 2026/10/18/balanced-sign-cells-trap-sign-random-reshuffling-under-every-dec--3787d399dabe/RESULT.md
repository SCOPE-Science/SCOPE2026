# Balanced-sign cells trap sign random reshuffling under every decreasing stepsize

## Finding

The following is a pathwise trapping theorem for plain sign-based random reshuffling (SignRR). It gives an explicit smooth, strongly convex finite-sum objective on which **every positive nonincreasing stepsize schedule tending to zero**, with a sufficiently small initial step, converges to a **nonstationary** point for **every** sequence of reshuffling permutations. This includes the classical nonsummable, square-summable Robbins–Monro schedules. Under independent uniformly random reshuffling the limit has an exact random-series law; with harmonic steps its variance is explicit and positive.

**Balanced-sign trapping theorem.** Let \(n\ge2\) be even and let \(f_1,\ldots,f_n:\mathbb R^d\to\mathbb R\) be differentiable. Suppose an open set \(U\subset\mathbb R^d\) exists such that each coordinatewise sign vector
\[
s_i=\operatorname{sign}(\nabla f_i(x))\in\{-1,0,1\}^d
\]
is independent of \(x\in U\), and \(\sum_{i=1}^n s_i=0\). Let \(p\) be the maximum, over coordinates, of the number of \(+1\) entries among the \(n\) corresponding signs; necessarily the number of \(-1\) entries is the same and \(p\le n/2\). Suppose the positive steps \(\gamma_k\) are nonincreasing and tend to zero. If the closed \(\ell_\infty\)-ball of radius \(2p\gamma_0\) about \(x_0\) is contained in \(U\), then for **every sequence** of complete-epoch permutations \(\pi_t\), the iteration
\[
x_{k+1}=x_k-\gamma_k s_{\pi_t(j)},\quad k=nt+j,\quad 0\le j<n
\]
stays inside \(U\), all iterates converge to \(x_\infty\), and
\[
\|x_\infty-x_0\|_\infty\le p\gamma_0.
\]
No independence assumption on the permutations is needed. All full-epoch displacements have absolutely summable norms.

**Strongly convex witness.** Let \(d=1\), \(n=2\), \(x_0=2\), and
\[
f_1(x)=\tfrac12(x-5)^2,\qquad f_2(x)=\tfrac12(x+5)^2,\qquad F(x)=\tfrac12\bigl(f_1(x)+f_2(x)\bigr)=\tfrac12x^2+\tfrac{25}{2}.
\]
The global minimizer is \(x_*=0\), and each component and their average are globally \(1\)-smooth and \(1\)-strongly convex. For *any* positive nonincreasing sequence with \(\gamma_0=1\) and \(\gamma_k\to0\), all SignRR iterates converge for every choice of permutations to \(X_\infty\in[1,3]\); hence
\[
|F'(X_\infty)|\ge1,\qquad F(X_\infty)-F(x_*)\ge\tfrac12.
\]
In particular this holds for \(\gamma_k=(k+1)^{-\alpha}\) for every \(1/2<\alpha\le1\), when \(\sum_k\gamma_k=\infty\) and \(\sum_k\gamma_k^2<\infty\).

When the two possible orders are independently sampled with probability \(1/2\) in each epoch, the limit is exactly
\[
X_\infty=2+\sum_{t=0}^\infty\varepsilon_t(\gamma_{2t}-\gamma_{2t+1}),
\quad \mathbb P\{\varepsilon_t=1\}=\mathbb P\{\varepsilon_t=-1\}=\tfrac12,
\]
with independent signs, so
\[
\mathbb E X_\infty=2,\qquad
\operatorname{Var}(X_\infty)=\sum_{t\ge0}(\gamma_{2t}-\gamma_{2t+1})^2.
\]
For harmonic steps \(\gamma_k=1/(k+1)\), the support is contained in \([2-\log 2,2+\log2]\) and
\[
\operatorname{Var}(X_\infty)=\frac{\pi^2}{6}-2\log2>0.
\]

## Assumptions and scope

The theorem concerns unscaled, coordinatewise sign updates using each component once per epoch, not a majority-vote compressor or a variance-reduced or error-feedback variant. The global schedule is deterministic, positive, nonincreasing and vanishing; the permutation sequence may be arbitrary or random. For \(p=0\), all component signs vanish on \(U\) and the trajectory is constant. With \(p>0\), the stated ball containment prevents leaving the sign-constant cell. There is no general claim that the region \(U\) is globally invariant for larger starting steps, that arbitrary nonmonotone schedules trap the iterates, or that every finite sum has a balanced-sign cell.

The witness uses no nonsmooth losses or pathological curvature: the component gradients are \(x-5\) and \(x+5\), and the constant-sign region is \(U=(-5,5)\), which contains the closed interval \([0,4]\) used in the bound. It demonstrates genuine nonstationarity for the *average* objective despite convergent iterates.

## Proof

**1. Prefix-count bound.** Fix a permutation \(\pi\) and any coordinate \(r\). Because the \(r\)-th component signs have the same number, at most \(p\), of positive and negative occurrences, every unweighted prefix sum \(S_j^{(r)}=\sum_{i=0}^j s_{\pi(i)}^{(r)}\) satisfies \(|S_j^{(r)}|\le p\), and \(S_{n-1}^{(r)}=0\). More generally, any weighted prefix of these signs with nonnegative nonincreasing weights no larger than \(\gamma_{nt}\) has magnitude at most \(p\gamma_{nt}\): the positive and negative contributions each have at most \(p\) terms, and neither can exceed \(p\gamma_{nt}\).

**2. Summation by parts.** Write \(X_t=x_{nt}\) for the beginning of epoch \(t\), and \(a_j=s_{\pi_t(j)}\). Within \(U\) the actual signs are \(a_j\). Since \(\sum_j a_j=0\), discrete summation by parts gives the exact identity
\[
X_{t+1}-X_t=-\sum_{j=0}^{n-2}(\gamma_{nt+j}-\gamma_{nt+j+1})\sum_{i=0}^j a_i.
\]
By the prefix-count bound and step monotonicity,
\[
\|X_{t+1}-X_t\|_\infty\le p(\gamma_{nt}-\gamma_{nt+n-1})\le p(\gamma_{nt}-\gamma_{n(t+1)}).
\]
This is a deterministic bound uniform over all epoch orders.

**3. Global trapping and convergence.** A bootstrap gives the sign-constant hypothesis at every iteration. Assuming all earlier epochs lie within \(U\), summing the last bound yields \(\|X_t-x_0\|_\infty\le p\gamma_0\). Every intermediate iterate differs from \(X_t\) by at most \(p\gamma_{nt}\) in sup norm, by step 1, so its distance from \(x_0\) is at most \(2p\gamma_0\). The closed ball is in \(U\), completing induction. The total variation of epoch starts satisfies
\[
\sum_{t=0}^\infty\|X_{t+1}-X_t\|_\infty
\le p\sum_{t=0}^\infty(\gamma_{nt}-\gamma_{n(t+1)})=p\gamma_0,
\]
where the last identity uses \(\gamma_k\to0\). Thus \((X_t)\) is Cauchy and converges. The intermediate distances to \(X_t\) are at most \(p\gamma_{nt}\to0\), proving full-iterate convergence and the endpoint bound.

**4. Quadratic nonstationary witness.** On \(U=(-5,5)\), the sign of \(f_1'\) equals \(-1\), and that of \(f_2'\) equals \(+1\). Here \(p=1\), \(x_0=2\), \(\gamma_0=1\), and \([x_0-2,x_0+2]=[0,4]\subset U\). By step 3, all epoch limits lie in \([1,3]\). The full gradient is \(F'(x)=x\), proving the gradient and objective-gap lower bounds. Because the step sizes vanish, these are limits of *all individual iterates*, not merely an epoch-subsampled sequence.

**5. Exact random limit law.** For two rows, each completed epoch increments the iterate by \(+\delta_t\) if the order is \((1,2)\) and by \(-\delta_t\) if the order is \((2,1)\), where \(\delta_t=\gamma_{2t}-\gamma_{2t+1}\ge0\). Since \(\sum_t\delta_t\le\gamma_0\), the Rademacher series converges absolutely for every sign realization. Independence and symmetry give the stated mean and variance by finite-sum moment identities and \(L^2\) convergence. For harmonic steps,
\[
\sum_{t\ge0}\delta_t=\sum_{t\ge0}\left(\frac1{2t+1}-\frac1{2t+2}\right)=\log2,
\]
and
\[
\sum_{t\ge0}\delta_t^2
=\sum_{m\ge1}\frac1{m^2}-2\sum_{t\ge0}\left(\frac1{2t+1}-\frac1{2t+2}\right)
=\frac{\pi^2}{6}-2\log2.
\]
The strict positivity follows already from the first variance summand \(\delta_0^2=1/4\).

## Verification

Run \(\texttt{python3 verify.py}\) (Python standard library only). It checks all permutations of a collection of balanced sign patterns, exact rational summation-by-parts identities and stepwise bounds on finite nonincreasing rational schedules, deterministic trapping of the two quadratic components under prescribed orders, the explicit two-row Rademacher increments, and convergence of partial harmonic alternating and squared sums to the claimed constants. The script is a reproducibility and algebra check, not a substitute for the infinite-horizon telescoping argument.

## Relationship to prior work

Qin, Liu and Xu (2023), arXiv:2310.15976, Algorithm 1 and Proposition 3.3, introduce exactly the unscaled sign-reshuffling update studied here and prove a stationarity upper bound containing a potentially nonvanishing conditional-gradient-deviation term. Their statement does **not imply** the present all-permutation, every-decreasing-stepsize pathwise trapping mechanism, its smooth strongly convex nonstationary witness, or the harmonic-limit variance identity. The result makes that paper's nonvanishing-error warning concrete; it does not contradict their upper bound.

Chzhen and Schechtman (2023), arXiv:2305.13187, explicitly note that vanilla signSGD need not converge for finite sums, and study a distinct, randomly sampled variance-reduced/noise-corrected algorithm. A general qualitative observation of possible failure is not the quantified, full-reshuffling, step-schedule-universal theorem proved here. Bernstein et al. (2018), arXiv:1802.04434, analyze signSGD with minibatch sampling and different noise/sign agreement hypotheses, not this pathwise exact finite-sum mechanism.

## Limitations

Originality cannot be guaranteed from finite database and literature searches, and older sign stochastic-approximation literature may contain an equivalent balanced-sign cancellation lemma. The broad qualitative claim that vanilla signSGD can fail is already known; the contribution claimed here is only the **quantified SignRR trapping criterion, schedule-uniform smooth strongly convex witness, and exact harmonic random-limit law**. The proof does not cover adaptive/nonmonotone steps, momentum, error feedback, variance reduction, or escape once the fixed-sign cell condition fails. Independent validation has not been performed.

## References

1. Z. Qin, Z. Liu and P. Xu, *Convergence of Sign-based Random Reshuffling Algorithms for Nonconvex Optimization* (2023), arXiv:2310.15976. https://arxiv.org/abs/2310.15976. First public posting: 2023-10-24.
2. E. Chzhen and S. Schechtman, *SignSVRG: fixing SignSGD via variance reduction* (2023), arXiv:2305.13187. https://arxiv.org/abs/2305.13187.
3. J. Bernstein, Y.-X. Wang, K. Azizzadenesheli and A. Anandkumar, *signSGD: Compressed Optimisation for Non-Convex Problems* (2018), arXiv:1802.04434. https://arxiv.org/abs/1802.04434.
