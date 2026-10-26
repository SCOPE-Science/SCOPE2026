# Sharp noninterpolation fluctuations of AdaSPS on two quadratic clients

## Finding
For every fixed scale \(c\ge 1\), consider the original unprojected AdaSPS update of Jiang and Stich with independent equiprobable sampling from the two component losses
\[
f_{+}(x)=\tfrac12(x-1)^2,\qquad f_{-}(x)=\tfrac12(x+1)^2.
\]
Take the valid individual lower bounds \(\ell_{+}^{\star}=\ell_{-}^{\star}=0\), initial iterate \(x_0=0\), scale \(c_p=c\), and initial previous step \(\eta_{-1}=+\infty\). Let \(x_n\) be the iterate after \(n\) component gradients. Then, writing \(\gamma=1/(\sqrt2 c)\),
\[
 n^{1/4}x_n\ \xrightarrow{\mathrm d}\ \mathcal N(0,\gamma/2),\qquad
 \lim_{n\to\infty}\sqrt n\,\mathbb E[x_n^2]=\gamma/2=\frac1{2\sqrt2 c}.
\]
The averaged objective is \(f(x)=(x^2+1)/2\) with unique minimizer \(0\), so
\[
\lim_{n\to\infty}\sqrt n\,\mathbb E[f(x_n)-f(0)]
=\frac1{4\sqrt2 c}>0.
\]
In addition the accumulated loss \(S_n\) and adaptive step satisfy, almost surely,
\[
\frac{S_n}{n+1}\longrightarrow\frac12,\qquad
\sqrt{n+1}\,\eta_n\longrightarrow\gamma.
\]
Thus the noninterpolating last-iterate \(n^{-1/2}\) expected-objective rate is sharp for this algorithmic instance, with an explicit leading constant and limiting distribution; the stochastic step is not replaced by a deterministic schedule in the statement.

## Assumptions and scope
The component index at time \(t\ge0\) is a fresh independent fair sign \(\xi_t\in\{-1,1\}\), with \(f_{\xi_t}(x)=(x-\xi_t)^2/2\). AdaSPS is precisely
\[
\eta_t=\min\left\{
\frac{f_{\xi_t}(x_t)-\ell_{\xi_t}^{\star}}{c\,|f'_{\xi_t}(x_t)|^2\sqrt{\sum_{s=0}^{t}(f_{\xi_s}(x_s)-\ell_{\xi_s}^{\star})}},\ \eta_{t-1}\right\},
\quad x_{t+1}=x_t-\eta_tf'_{\xi_t}(x_t).
\]
All variables are real; \(c\ge1\) is constant, sample choices are independent, no projection or momentum is used, and the arithmetic is exact. The algorithm is defined at every step: its iterates remain strictly between \(-1\) and \(1\), so no component gradient vanishes.

## Proof
**1. Exact reduction and invariance.** Set \(S_t=\frac12\sum_{s=0}^{t}(x_s-\xi_s)^2\). Since \(f_\xi(x)/|f'_\xi(x)|^2=1/2\) whenever \(x\ne\xi\), and \(S_t\) increases, induction in the original minimum gives
\[
\eta_t=\frac{1}{2c\sqrt{S_t}},\qquad x_{t+1}=(1-\eta_t)x_t+\eta_t\xi_t.
\tag{1}
\]
Here \(S_0=1/2\), hence \(0<\eta_t\le1/(\sqrt2 c)<1\). Starting at zero, every update is a strict convex combination of a point in \((-1,1)\) and one endpoint. Therefore \(|x_t|<1\) for every finite \(t\) on every sampling path, and (1) is legitimate for all \(t\).

**2. Concentration of accumulated loss.** Let \(\mathcal F_t=\sigma(\xi_0,\ldots,\xi_{t-1})\), so \(x_t\) is \(\mathcal F_t\)-measurable. The identity
\[
S_t=\frac{t+1}{2}+\frac12\sum_{s=0}^{t}x_s^2-\sum_{s=0}^{t}x_s\xi_s
\tag{2}
\]
separates a nonnegative predictable term from a martingale sum of differences bounded in absolute value by one. Azuma--Hoeffding implies
\[
\Pr\{S_{t-1}<t/4\}\le \exp(-t/32),\qquad t\ge1.
\tag{3}
\]
Also \(S_{t-1}\le2t\), directly from \(|x_s|<1\).

**3. Moment controls without treating the current adaptive step as predictable.** For \(t\ge1\), introduce the predictable comparison step \(\bar\eta_t=(2c\sqrt{S_{t-1}})^{-1}\). The one-step increment of \(S_t\) lies in \([0,2]\). The mean-value theorem, (3), and the boundedness of the iterates yield
\[
\mathbb E\left|\eta_t-\bar\eta_t\right|=O(t^{-3/2}).
\tag{4}
\]
The comparison update is \(y_{t+1}=(1-\bar\eta_t)x_t+\bar\eta_t\xi_t\); both it and the true update have magnitude at most one, and their difference is \((\eta_t-\bar\eta_t)(\xi_t-x_t)\). Conditional on \(\mathcal F_t\), the fair sign has zero mean and square one. Thus
\[
\mathbb E[y_{t+1}^2\mid\mathcal F_t]=(1-\bar\eta_t)^2x_t^2+\bar\eta_t^2,
\]
\[
\mathbb E[y_{t+1}^4\mid\mathcal F_t]=(1-\bar\eta_t)^4x_t^4+6(1-\bar\eta_t)^2\bar\eta_t^2x_t^2+\bar\eta_t^4.
\tag{5}
\]
There is a constant \(d=1/(2\sqrt2 c)>0\) such that \(\bar\eta_t\ge d/\sqrt t\) deterministically, and (3) gives \(\mathbb E[\bar\eta_t^{2j}\mathbf 1_{\{S_{t-1}\ge t/4\}}]=O(t^{-j})\), with exponentially small complementary probability. Equations (4)--(5), together with \(|a^j-b^j|\le j|a-b|\) on \([-1,1]\), give successive scalar inequalities
\[
\mathbb E x_{t+1}^2\le(1-d/\sqrt t)\mathbb E x_t^2+O(t^{-1}),
\]
\[
\mathbb E x_{t+1}^4\le(1-d/\sqrt t)\mathbb E x_t^4+O(t^{-3/2}).
\]
Elementary induction/comparison for these recurrences yields
\[
\mathbb E x_t^2=O((t+1)^{-1/2}),\qquad
\mathbb E x_t^4=O((t+1)^{-1}).
\tag{6}
\]
No independence between \(\eta_t\) and \(\xi_t\) was presumed.

**4. Self-normalization with quantitative remainder.** From (2), (6), and martingale orthogonality,
\[
\mathbb E\left|S_t-\frac{t+1}{2}\right|=O(\sqrt{t+1}),\quad
\mathbb E\left(S_t-\frac{t+1}{2}\right)^2=O((t+1)\log(t+2)).
\tag{7}
\]
For the second bound use \((\sum x_s^2)^2\le(t+1)\sum x_s^4\). Equation (6) also shows \(\mathbb E[(t+1)^{-1}\sum_{s\le t}x_s^2]=O(t^{-1/2})\). Markov's inequality along dyadic indices, Borel--Cantelli, and monotonicity of the numerator extend this Cesàro convergence to all integers almost surely. The bounded-increment martingale strong law applies to \(\sum x_s\xi_s\). Consequently (2) yields \(S_t/(t+1)\to1/2\) almost surely, and (1) gives the claimed adaptive-step limit.

Define \(a_t=\gamma/\sqrt{t+1}\). Applying the mean-value theorem to the inverse square root on \(S_t\ge(t+1)/4\), and using (3) and (7), proves
\[
\mathbb E|\eta_t-a_t|=O((t+1)^{-1}),\quad
\mathbb E(\eta_t-a_t)^2=O(\log(t+2)/(t+1)^2).
\tag{8}
\]
The rare complementary event contributes only an exponentially small term because both steps are uniformly bounded.

**5. Reduction to deterministic-gain stochastic approximation.** Couple the actual iterates with \(z_0=0\) and
\[
z_{t+1}=(1-a_t)z_t+a_t\xi_t.
\tag{9}
\]
Subtracting (9) from (1), and iterating the deterministic-coefficient error recursion, gives
\[
x_n-z_n=\sum_{s=0}^{n-1}(\eta_s-a_s)(\xi_s-x_s)
\prod_{j=s+1}^{n-1}(1-a_j).
\tag{10}
\]
By Minkowski and (8), using \(|\xi_s-x_s|\le2\),
\[
\|x_n-z_n\|_{L^2}\le C\sum_{s<n}\frac{\sqrt{\log(s+2)}}{s+1}
\exp\left(-\sum_{j=s+1}^{n-1}a_j\right)
=O\left(\frac{\sqrt{\log(n+2)}}{\sqrt n}\right).
\tag{11}
\]
For the last bound, split the sum at \(n/2\): older terms have \(e^{-\Omega(\sqrt n)}\) attenuation; for newer terms the exponential has an \(e^{-\Omega((n-s)/\sqrt n)}\) bound, leaving only \(O(\sqrt n)\) effective summands, each of order \(\sqrt{\log n}/n\). Hence \(n^{1/4}(x_n-z_n)\to0\) in \(L^2\).

**6. Limit of the comparison process.** Equation (9) expresses \(z_n\) as a weighted sum of independent symmetric signs, with variance
\[
V_n=\mathbb E z_n^2
=\sum_{s=0}^{n-1}a_s^2\prod_{j=s+1}^{n-1}(1-a_j)^2.
\tag{12}
\]
Only indices \(s=n+O(\sqrt n)\) contribute in the limit. Writing \(s=n-1-\lfloor y\sqrt n\rfloor\), one has \(\sqrt n\,a_s^2\to\gamma^2/\sqrt n\) per summand and the squared product tends to \(e^{-2\gamma y}\). Riemann-sum convergence with exponential tail domination yields
\[
\sqrt n\,V_n\longrightarrow\int_0^\infty\gamma^2e^{-2\gamma y}\,dy=\gamma/2.
\tag{13}
\]
The maximal coefficient of \(n^{1/4}z_n\) tends to zero, so the bounded independent-sign Lindeberg theorem gives \(n^{1/4}z_n\Rightarrow\mathcal N(0,\gamma/2)\). Equation (11) transfers the limit to \(x_n\). By Cauchy--Schwarz, (6), (11), and (13),
\[
\sqrt n\,|\mathbb E x_n^2-\mathbb E z_n^2|
\le\sqrt n\,\|x_n-z_n\|_2(\|x_n\|_2+\|z_n\|_2)\to0.
\]
This proves both asserted limits and the objective-gap constant.

## Verification
The companion standalone `verify_adasps.py` re-evaluates the original loss/gradient/minimum step against (1) on all \(2^{11}\) fair-sign paths for each of three allowed scales. It also runs seeded Monte Carlo comparisons of \(\sqrt n\mathbb E x_n^2\), \(S_{n-1}/n\), and the predicted limiting constants. The verification program uses ordinary Python and NumPy, and runs without external data. Finite-path checks are consistency tests only; the infinite limit follows from the proof above.

## Relationship to prior work
Jiang and Stich (arXiv:2308.06058v1, first public 2023-08-11) introduced the precise loss-accumulating, nonincreasing AdaSPS step rule used here; their Section 3 and appendix establish convergence-rate upper bounds and examine synthetic quadratics, but do not state the exact Gaussian fluctuation or strictly positive scaled last-iterate risk constant for this symmetric two-client case. Orvieto, Lacoste-Julien and Loizou (arXiv:2205.04583) introduced a different decreasing stochastic Polyak algorithm, DecSPS, and analyze bias and convergence; the present statement concerns AdaSPS and its exact cumulative-loss denominator. Lauand and Meyn (arXiv:2405.17834) analyze stochastic approximation with prescribed deterministic power-law gain and averaged-iterate asymptotics; the self-normalizing sample-dependent step here requires the separate equivalence estimates (4), (7), (8), and (11). Oikonomou and Loizou (arXiv:2406.04142) analyze momentum extensions; a comprehensive full-text comparison of that paper was not available, leaving a priority risk. Generic deterministic-gain stochastic approximation fluctuation theory is acknowledged and used in step 6, rather than claimed as new.

## Limitations
This theorem is specific to the equal-curvature, two-centered, scalar strongly convex noninterpolating instance, initial point zero, independent fair component draws, and \(c\ge1\). It is not an all-problems lower bound for AdaSPS, not a statement about Polyak--Ruppert averages, and not an assertion that all adaptive stochastic gradients have this limit. The only random normal limit is for unaveraged last iterates. The coefficient approaches zero as the **fixed** scale \(c\) tends to infinity; no uniform-in-\(c\) convergence is claimed. Numerical experiments cannot independently certify the infinite-horizon law or the novelty of the finding. Independent scientific audit and broader priority verification remain outstanding.

## References
1. X. Jiang and S. U. Stich, *Adaptive SGD with Polyak stepsize and Line-search: Robust Convergence and Variance Reduction*, arXiv:2308.06058v1 (2023-08-11), https://arxiv.org/abs/2308.06058.
2. A. Orvieto, S. Lacoste-Julien and N. Loizou, *Dynamics of SGD with Stochastic Polyak Stepsizes: Truly Adaptive Variants and Convergence to Exact Solution*, arXiv:2205.04583 (2022), https://arxiv.org/abs/2205.04583.
3. C. K. Lauand and S. Meyn, *Revisiting Step-Size Assumptions in Stochastic Approximation*, arXiv:2405.17834 (2024), https://arxiv.org/abs/2405.17834.
4. D. Oikonomou and N. Loizou, *Stochastic Polyak Step-sizes and Momentum: Convergence Guarantees and Practical Performance*, arXiv:2406.04142 (2024), https://arxiv.org/abs/2406.04142.
