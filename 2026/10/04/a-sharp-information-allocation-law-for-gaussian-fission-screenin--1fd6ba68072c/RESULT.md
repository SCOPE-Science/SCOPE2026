# A sharp information-allocation law for Gaussian fission screening and confirmation
## Finding
Let \(X\sim N(\mu,1)\) and \(Z\sim N(0,1)\) be independent, with \(\mu>0\), and form the Gaussian fission split \(U=X+\tau Z\), \(V=X-Z/\tau\) for \(\tau>0\). Select the positive direction when \(U>0\), then, using only the independent inference component \(V\), reject \(H_0:\mu\le 0\) at one-sided level \(0<\alpha<1/2\) when \(V/\sqrt{1+\tau^{-2}}>z_{1-\alpha}\). The probability of both selection and rejection is \[D_{\mu,\alpha}(\tau)=\Phi\!\left(\frac{\mu}{\sqrt{1+\tau^2}}\right)\Phi\!\left(\frac{\mu}{\sqrt{1+\tau^{-2}}}-z_{1-\alpha}\right).\] It has a unique maximizer \(\tau_*(\mu,\alpha)>1\). Writing \(h(x)=\phi(x)/\Phi(x)\) and \(\theta_*=\arctan\tau_*\), the maximizer is the unique solution of \[\cos\theta_*\,h(\mu\sin\theta_*-z_{1-\alpha})=\sin\theta_*\,h(\mu\cos\theta_*).\] Moreover, as \(\mu\downarrow0\), \[\tau_*(\mu,\alpha)\longrightarrow \frac{e^{-z_{1-\alpha}^2/2}}{2\alpha}.\] Thus the power-optimal fission is strictly inference-heavy for every positive signal at conventional one-sided levels; at \(\alpha=0.05\), the weak-signal optimum allocates only \(0.1301507268\) of Fisher information to selection. At the null boundary \(\mu=0\), the joint selection-and-rejection probability is exactly \(\alpha/2\) for every \(\tau\), so this tuning changes alternative discovery probability without changing that boundary-null probability.

At \(\alpha=0.05\) and \(\mu=1\), the optimizer is \(\tau_*=2.32247756096945\), so the selection component receives Fisher-information fraction \(1/(1+\tau_*^2)=0.1563990184\). The optimized joint discovery probability is \(0.1528501778\), compared with \(0.1324258550\) for the equal-information choice \(\tau=1\).

## Assumptions and scope
The observation is scalar with known unit variance. The artificial noise is independent standard Gaussian noise. The screening rule is the canonical one-sided sign screen \(U>0\), and confirmation is the ordinary one-sided level-\(\alpha\) z-test based only on the independent inference component. The objective is the unconditional probability that a true positive direction is both screened in and subsequently rejected. This is not a claim about conditional selective power, arbitrary selection rules, unknown variance, multivariate regression, or optimality among all possible post-selection procedures.

For the split above,
\[
U\sim N(\mu,1+\tau^2),\qquad V\sim N(\mu,1+\tau^{-2}),\qquad \operatorname{Cov}(U,V)=0.
\]
Joint Gaussianity therefore makes \(U\) and \(V\) independent. Their Fisher-information fractions about \(\mu\) are respectively \(1/(1+\tau^2)\) and \(\tau^2/(1+\tau^2)\), which sum to one.

## Proof
Put \(z=z_{1-\alpha}\) and parameterize \(\tau=\tan\theta\) with \(0<\theta<\pi/2\). Independence gives
\[
D_{\mu,\alpha}(\theta)=\Phi(\mu\cos\theta)\,\Phi(\mu\sin\theta-z).
\]
Let \(g(x)=\log\Phi(x)\) and \(h(x)=g'(x)=\phi(x)/\Phi(x)\). The inverse Mills ratio satisfies
\[
g''(x)=h'(x)=-h(x)\{x+h(x)\}<0.
\]
Indeed, \(x+h(x)>0\): it is immediate for \(x\ge0\), while for \(x<0\) the standard Mills inequality \(\Phi(x)<\phi(x)/(-x)\) gives \(h(x)>-x\). Thus \(g\) is strictly increasing and strictly concave.

For
\[
F(\theta)=\log D_{\mu,\alpha}(\theta)=g(\mu\cos\theta)+g(\mu\sin\theta-z),
\]
each summand has strictly negative second derivative on \(0<\theta<\pi/2\): for an inner function \(a\), the second derivative is \(g''(a)(a')^2+g'(a)a''\), and both \(\mu\cos\theta\) and \(\mu\sin\theta-z\) have negative second derivative there. Hence \(F\) is strictly concave. Its derivative is
\[
F'(\theta)=\mu\{-\sin\theta\,h(\mu\cos\theta)+\cos\theta\,h(\mu\sin\theta-z)\}.
\]
As \(\theta\downarrow0\), this tends to \(\mu h(-z)>0\); as \(\theta\uparrow\pi/2\), it tends to \(-\mu h(0)<0\). Strict concavity therefore gives exactly one zero, proving existence and uniqueness and yielding the displayed first-order equation.

Because \(0<\alpha<1/2\), we have \(z>0\). At \(\theta=\pi/4\),
\[
F'(\pi/4)=\frac{\mu}{\sqrt2}\{h(\mu/\sqrt2-z)-h(\mu/\sqrt2)\}>0,
\]
since \(h\) is strictly decreasing. The unique root therefore satisfies \(\theta_*>\pi/4\), equivalently \(\tau_*>1\).

At the root,
\[
\tan\theta_*=\frac{h(\mu\sin\theta_*-z)}{h(\mu\cos\theta_*)}.
\]
Letting \(\mu\downarrow0\) makes the right-hand side converge uniformly in \(\theta\) to \(h(-z)/h(0)\). Since \(\Phi(-z)=\alpha\), \(h(-z)=\phi(z)/\alpha\), and \(h(0)=2\phi(0)\), the limit is
\[
\frac{h(-z)}{h(0)}=\frac{e^{-z^2/2}}{2\alpha}.
\]
Finally, at \(\mu=0\), independence gives \(D_{0,\alpha}(\tau)=\Phi(0)\Phi(-z)=\alpha/2\) for every \(\tau\).

## Verification
The bundled `verify.py` recomputes the Gaussian split covariance, solves the strictly concave first-order condition by bisection for several signals and levels, checks the reported \(\alpha=0.05,\mu=1\) numbers, verifies numerically that all tested optima satisfy \(\tau_*>1\), checks the weak-signal limit, and confirms null-boundary invariance over multiple \(\tau\) values. These computations corroborate the analytic proof; the proof itself, not the finite grid, establishes the quantifiers over all \(\mu>0\), \(0<\alpha<1/2\), and \(\tau>0\).

## Relationship to prior work
García Rasines and Young introduce the independent Gaussian decomposition used here, state that the randomization variance controls how much information is reserved for selection versus inference, and explicitly note that their information-averaging representation offers a possible way to choose that variance. Their theoretical comparison and simulations use broader regression/selection settings and do not state the scalar joint-discovery objective, the strict inference-heavy optimum, or the inverse-Mills weak-signal limit proved here. Leiner, Duan, Wasserman and Ramdas develop the broader data-fission framework and likewise emphasize the continuous Fisher-information tradeoff.

Tian and Taylor study randomized-response selective inference and establish power advantages of randomization, but their selective conditional procedures are different from the independent confirmation rule analyzed here. Cox's 1975 paper is an important older comparison: its accessible abstract says that it derives recommendations for how to divide an ordinary data split in a many-normal-means significance-testing problem. The full article was not available in accessible full text during this review, so an older equivalent formula under that distinct many-hypothesis setup remains a residual literature risk. The present claim is restricted to the Gaussian fission/sign-screen/z-confirmation workflow and does not assert a general novelty theorem about all data-splitting allocation problems.

## Limitations
The result assumes known variance, a single Gaussian mean, one-sided sign screening, and independent confirmation. It optimizes joint screening-and-rejection probability for a fixed positive \(\mu\); a practitioner does not know \(\mu\) in advance, so the formula is a design benchmark rather than a universal plug-in tuning rule. The weak-signal limit supplies a signal-free local benchmark, but robustness to variance estimation, two-sided screening, multiple candidate parameters, or misspecification is unproved. The originality assessment also retains risk from Cox (1975), whose full text could not be inspected.

## References
1. D. García Rasines and G. A. Young, “Splitting strategies for post-selection inference,” *Biometrika* 110(3), 597–614 (2023). arXiv:2102.02159; DOI: 10.1093/biomet/asac070.
2. J. Leiner, B. Duan, L. Wasserman and A. Ramdas, “Data Fission: Splitting a Single Data Point,” *Journal of the American Statistical Association* 120, 135–146 (2025). arXiv:2112.11079; DOI: 10.1080/01621459.2023.2270748.
3. X. Tian and J. E. Taylor, “Selective inference with a randomized response,” *Annals of Statistics* 46(2), 679–710 (2018). arXiv:1507.06739; DOI: 10.1214/17-AOS1564.
4. D. R. Cox, “A note on data-splitting for the evaluation of significance levels,” *Biometrika* 62(2), 441–444 (1975). DOI: 10.1093/biomet/62.2.441.
