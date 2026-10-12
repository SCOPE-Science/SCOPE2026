# The weighted-cut law of noisy finite-difference baseline reuse

## Finding

**Theorem (exact covariance partition and hard optimal reuse).** Let \(n\ge2\), let \(H\in\mathbb R^{n\times n}\) be symmetric positive definite, and let \(\phi(x)=\frac12 x^\top Hx+b^\top x+c\) be a quadratic objective. Fix an iterate \(x\), differencing interval \(h>0\), step size \(\eta>0\), and noisy evaluation variance \(\sigma^2>0\). Suppose one independently obtains a noisy value at each point \(x+he_i\) and assigns each forward difference one of at most \(r\ge1\) independently evaluated baseline values at \(x\), reusing a baseline for all coordinates assigned the same label. Define \(d_i=H_{ii}\), \(\mu=Hx+b+hd/2\), and let \(C_1,\ldots,C_r\) denote the possibly empty groups.

For all such groupings, the mean is \(\mathbb E\widehat g=\mu\), and the **exact one-step expected objective** is

\[
\mathbb E\phi(x-\eta\widehat g)=\phi(x-\eta\mu)+\frac{\eta^2\sigma^2}{2h^2}\left[\operatorname{tr}H+\sum_{a=1}^{r}{\boldsymbol 1}_{C_a}^{\top}H{\boldsymbol 1}_{C_a}\right].
\]

Relative to reusing one baseline for all coordinates, the improvement is exactly

\[
\boxed{\mathbb E\phi(x-\eta\widehat g_{\mathrm{group}})-\mathbb E\phi(x-\eta\widehat g_{\mathrm{one}})=-\frac{\eta^2\sigma^2}{h^2}\sum_{i<j\, :\, c_i\ne c_j}H_{ij}.}
\]

Consequently, selecting at most \(r\) baselines optimally is **exactly maximum weighted \(r\)-cut**, with signed edge weights given by the off-diagonal Hessian entries. With two available baselines this optimization is NP-hard even for real rational positive-definite Hessians whose spectral condition number is smaller than \(1+\delta\), for any prescribed \(\delta>0\). This is a decision/optimization complexity statement under the standard NP-hardness of unweighted MAX-CUT; it is not an assertion that computing the expectation for a *specified* grouping is difficult.

In contrast, **every grouping has the same squared Euclidean gradient-estimation error**,

\[
\mathbb E\|\widehat g-\nabla\phi(x)\|_2^2=\frac{h^2}{4}\sum_{i=1}^n H_{ii}^2+\frac{2n\sigma^2}{h^2},
\]

and the same expected squared Euclidean distance after the one-step update. The curvature-weighted objective criterion can therefore discriminate between groupings that an ordinary Euclidean error criterion cannot.

## Assumptions and scope

An evaluation of the noisy function oracle at a fixed point returns its deterministic objective value plus an additive zero-mean random error. The \(n\) perturbed-point errors \(\xi_1,\dots,\xi_n\) and the \(r\) baseline errors \(\zeta_1,\dots,\zeta_r\) are mutually independent; every error has variance \(\sigma^2\). Identically distributed errors are sufficient but not necessary. All errors have finite second moments. **Reusing** one baseline means using the same realized random number in multiple coordinate differences, not making correlated independent draws. Each coordinate gets exactly one independently sampled perturbed-point value; assignments are fixed before observing those values, and one update is performed. Extra available baseline evaluations may be unused. For an actual prescribed \(r\)-group partition, use exactly the nonempty groups. All parameters are real except labels and finite cardinalities.

For coordinate \(i\), with assigned label \(c_i\in\{1,\dots,r\}\), the estimated derivative is

\[
\widehat g_i=\frac{\phi(x+he_i)+\xi_i-\phi(x)-\zeta_{c_i}}{h}.
\]

The optimization objective is the expectation of the **underlying noiseless quadratic value at the updated point**, not the noisy value used to estimate the gradient. Computational cost of additional baseline calls is not included in the risk; an evaluation budget is modeled only by the upper bound \(r\).

## Proof

**1. Mean and covariance.** Exact quadratic expansion gives \(\phi(x+he_i)-\phi(x)=h(Hx+b)_i+h^2H_{ii}/2\). Thus, with \(S_a={\boldsymbol 1}_{C_a}\),

\[
\widehat g=\mu+\frac1h\left(\xi-\sum_{a=1}^r\zeta_a S_a\right),\qquad
\operatorname{Cov}(\widehat g)=\frac{\sigma^2}{h^2}\left(I+\sum_{a=1}^rS_aS_a^\top\right).
\]

The independence assumptions eliminate every mixed covariance. At any two coordinates, the off-diagonal covariance is \(\sigma^2/h^2\) if they share a baseline and zero otherwise. The diagonal covariance is always \(2\sigma^2/h^2\), irrespective of group size. This proves the fixed Euclidean mean-squared gradient error (squared bias plus covariance trace). For the minimizer \(x_*=-H^{-1}b\), the identity \(\mathbb E\|x-\eta\widehat g-x_*\|_2^2=\|x-\eta\mu-x_*\|_2^2+2n\eta^2\sigma^2/h^2\) likewise holds for every grouping.

**2. Exact objective and cut law.** For any random vector \(Y\) with finite covariance \(\Sigma\), expansion of the quadratic gives \(\mathbb E\phi(Y)=\phi(\mathbb EY)+\frac12\operatorname{tr}(H\Sigma)\). Apply it to \(Y=x-\eta\widehat g\) using the covariance above. This yields the first displayed formula. The all-shared configuration has its group contribution \({\boldsymbol 1}^\top H{\boldsymbol 1}\). Subtracting removes all diagonal entries and all pairs within groups, leaving \(-2\sum_{i<j:\,c_i\ne c_j}H_{ij}\). Multiplication by \(\eta^2\sigma^2/(2h^2)\) yields exactly the boxed graph-cut identity for every number of labels and every sign pattern of the off-diagonal Hessian.

**3. Sharp complexity implication, even close to isotropy.** Given any unweighted simple graph \(G\) with \(n\ge2\) vertices, let \(A_G\) be its zero-diagonal symmetric adjacency matrix and put \(H=I+\epsilon A_G\). Choose rational \(\epsilon>0\) with \(t:=\epsilon(n-1)<\min\{1,\delta/(2+\delta)\}\). Since \(\|A_G\|_2\le n-1\), the spectrum of \(H\) belongs to \([1-t,1+t]\); hence \(H\) is positive definite and \(\kappa_2(H)\le(1+t)/(1-t)<1+\delta\). Such a rational \(\epsilon\) is efficiently computable for each fixed rational \(\delta>0\), for example by choosing a sufficiently small reciprocal of an integer multiple of \(n\). Fix rational \(x=0\), \(h=\eta=\sigma=1\), \(b=c=0\). For any two-label assignment, the cut objective in the boxed identity is \(\epsilon\) times the number of crossing graph edges. Thus an exact algorithm selecting a minimum-risk grouping using at most two baseline values also solves the (unweighted) MAX-CUT optimization problem, and an exact threshold comparison solves its NP-complete decision form. All numbers in the reduction have polynomial-size rational descriptions. Fixing any positive rational \(\delta\) gives NP-hardness inside the class \(\kappa_2(H)<1+\delta\); arbitrary real \(\delta>0\) follows by choosing a smaller rational tolerance.

**4. Signed-edge reversal.** Let

\[
H=\begin{pmatrix}1&-3/5\\-3/5&1\end{pmatrix},\qquad x=0,\quad b=0,\quad h=\eta=\sigma=1.
\]

This \(H\) is positive definite with eigenvalues \(2/5\) and \(8/5\). Both groupings have the identical deterministic mean update \((-1/2,-1/2)\), whose noiseless quadratic objective is \(1/10\). With one reused baseline, \(\operatorname{tr}H+{\boldsymbol1}^\top H{\boldsymbol1}=14/5\), so \(\mathbb E\phi(x^+)=3/2\). With distinct baselines, the corresponding trace bracket is \(4\), so \(\mathbb E\phi(x^+)=21/10\). The increase is exactly \(3/5\), although the gradient-estimation squared Euclidean error is \(9/2\) in both cases. This does not contradict budget monotonicity: *allowing* an additional baseline does not force its use, whereas *requiring* two nonempty groups does.

## Verification

The standalone Python 3 checker `verify.py` uses only standard-library exact rational arithmetic (`fractions.Fraction`). It independently enumerates all \(2^{n+r}\) Rademacher noise configurations for several two- and three-coordinate positive-definite quadratics, comparing direct averages to the covariance formula, checks the cut identity for alternative assignments, verifies the signed-edge risk witness and Euclidean-error invariance, and enumerates every unweighted simple graph on \(2\) through \(5\) vertices to test the reduction. The checker returns `PASS 18107 exact rational checks` when run as `python verify.py`. Those finite checks are consistency tests; the proof for arbitrary dimensions is the algebraic covariance calculation and polynomial reduction above.

## Relationship to prior work

Brekelmans, Driessen, Hamers, and den Hertog (2003 working paper; 2005 journal paper), Section 2.1, **already compute the nonzero cross-coordinate covariance caused by a single shared base-point observation** and its Euclidean gradient-error contribution. That covariance endpoint and elementary error propagation are prior work, not separately claimed as new. Their Sections 2–4 compare predetermined finite-difference and designed-experiment estimators and interval choices; the inspected statements do not optimize assigning independent baseline realizations to coordinate groups under the next-iterate quadratic objective. Berahas, Cao, Choromanski, and Scheinberg (arXiv:1905.01332, first publicly posted 2019-05-03), Section 2.1, study the standard forward finite-difference gradient with a single common evaluation at the base point and derive norm-error bounds for noisy objectives. Their stated results do not optimize the partition of multiple independently evaluated baselines according to the off-diagonal quadratic Hessian. Shi, Xie, Xuan, and Nocedal (arXiv:2110.06380) study choosing finite-difference *intervals* in the presence of measurement noise, rather than cross-coordinate baseline grouping. The 1999 analysis by Kleinman, Spall, and Naiman studies common random numbers in stochastic approximation to reduce gradient-estimation variance by correlating paired simulation inputs, not the present independent-additive-noise reference-reuse partition. These are substantive differences in sampling object and optimization criterion; no priority claim is made solely from different terminology. The general quadratic covariance identity and known MAX-CUT hardness are standard ingredients; the specific optimization equivalence and its consequences concern the designated derivative-free sampling design.

## Limitations

The claim is exact for **one step**, **quadratic objectives**, independent equal-variance additive oracle noise, and the specified shared-baseline reuse mechanism. It does not assert convergence of repeated noisy updates, a faster algorithm for finding an optimal grouping, a monotone benefit from forcing more baseline calls, or a practical wall-clock advantage. Approximate Hessians, correlated oracle errors beyond literal reuse, unbalanced baseline variance, adaptive grouping based on observed noise, and nonsmooth or nonquadratic objectives are outside the theorem. The NP-hardness statement is worst-case exact optimization; it does not preclude effective heuristics or special cases. Priority remains subject to potentially unindexed specialized common-random-number design results.

## References

1. A. S. Berahas, L. Cao, K. Choromanski, K. Scheinberg, *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization*. arXiv:1905.01332 (v1 dated 2019-05-03), especially Section 2.1. https://arxiv.org/abs/1905.01332 ; lawful 2019 working version: https://optimization-online.org/2019/05/7189/
2. H.-J. M. Shi, Y. Xie, M. Q. Xuan, J. Nocedal, *Adaptive Finite-Difference Interval Estimation for Noisy Derivative-Free Optimization*. arXiv:2110.06380 (v1 dated 2021-10-12). https://arxiv.org/abs/2110.06380
3. E. Kleinman, J. C. Spall, D. Q. Naiman, *Simulation-Based Optimization with Stochastic Approximation Using Common Random Numbers*. Management Science 45 (1999), 1570–1578, Section 2.2. https://www.jhuapl.edu/spsa/PDF-SPSA/Kleinman_Simulation-Based.PDF
4. R. C. M. Brekelmans, L. Driessen, H. J. M. Hamers, D. den Hertog, *Gradient Estimation Schemes for Noisy Functions*. CentER Discussion Paper 2003-12 (2003), Journal of Optimization Theory and Applications 126 (2005), 529–551, Section 2.1. Author-uploaded manuscript: https://www.researchgate.net/publication/4866402_Gradient_Estimation_Schemes_for_Noisy_Functions ; university manuscript record: https://research.tilburguniversity.edu/en/publications/gradient-estimation-schemes-for-noisy-functions
5. M. R. Garey, D. S. Johnson, L. Stockmeyer, *Some Simplified NP-Complete Graph Problems*. Theoretical Computer Science 1 (1976), 237–267. Establishes NP-completeness of unweighted simple MAX-CUT. https://doi.org/10.1016/0304-3975(76)90059-1
