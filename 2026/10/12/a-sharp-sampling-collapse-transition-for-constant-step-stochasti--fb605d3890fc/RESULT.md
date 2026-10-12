# A sharp sampling-collapse transition for constant-step stochastic proximal quadratics

## Finding
Consider the two strongly convex scalar functions
\[
f_1(x)=\frac{\kappa}{2}x^2,\qquad f_2(x)=\frac12(x-1)^2,\qquad \kappa\ge1,
\]
and evaluate performance against their **fixed equally weighted objective** \(F=(f_1+f_2)/2\), with minimizer \(x_\star=1/(\kappa+1)\). Let independent sampling select the first proximal operator with probability \(p\in[0,1]\), and the second with probability \(1-p\). The proximal step parameter is one; no inverse-probability correction is used. Define the limiting squared error
\[
R_\kappa(p)=\lim_{n\to\infty}\mathbb E[(X_n-x_\star)^2].
\]
This limit exists for every deterministic finite start. Put
\[
\begin{aligned}
A_\kappa&=(\kappa-1)(\kappa+3)(\kappa^2+4\kappa+5),\\
B_\kappa&=6(\kappa+1)^2(\kappa+3),\\
P_\kappa(p)&=A_\kappa p^2+B_\kappa p-3(\kappa+1)^4.
\end{aligned}
\]
**Sharp transition.** If \(1\le\kappa<1+2\sqrt2\), the unique global minimizer of \(R_\kappa\) on \([0,1]\) is the unique root \(p_\star\in(0,1)\) of \(P_\kappa(p)=0\). If \(\kappa\ge1+2\sqrt2\), the unique minimizer is \(p_\star=1\): the optimal stationary-risk sampler entirely selects the high-curvature first component. At \(\kappa=1\), \(p_\star=1/2\).

The unique choice that makes the stationary mean unbiased for \(x_\star\) is \(p_{\rm ub}=(\kappa+1)/(\kappa+3)\). For every \(\kappa>1\), the stationary-risk optimum satisfies \(p_\star>p_{\rm ub}\). In particular, for \(\kappa\ge1+2\sqrt2\), the unbiased sampler incurs
\[
\frac{R_\kappa(p_{\rm ub})}{R_\kappa(1)}=\frac{\kappa^2}{2\kappa+1}\longrightarrow\infty.
\]
The **absolute** expected objective excess at the unbiased sampler tends to \(1/8\), whereas at the stationary-risk-optimal deterministic sampler it tends to zero. These statements concern terminal stationary error, not objective fidelity under changing sampling distributions.

## Assumptions and scope
For each \(\kappa\ge1\), take any deterministic real \(X_0\). Let \(I_0,I_1,\ldots\) be iid with \(\Pr(I_n=1)=p\) and \(\Pr(I_n=2)=1-p\), including endpoints. Set \(X_{n+1}=\operatorname{prox}_{f_{I_n}}(X_n)\) with \(\operatorname{prox}_f(x)=\arg\min_y\{f(y)+(y-x)^2/2\}\). Hence
\[
X_{n+1}=\begin{cases}X_n/(\kappa+1)&I_n=1,\\(X_n+1)/2&I_n=2.\end{cases}
\]
Both maps are strict contractions. The original benchmark \(F=(f_1+f_2)/2\) is held fixed while the uncorrected sampling probability varies. The stationary expected objective gap is \(\frac{\kappa+1}{4}R_\kappa(p)\).

## Proof
Write \(w_1=\kappa/(\kappa+1)\), \(w_2=1/2\), and \(W=pw_1+(1-p)w_2\). The step is \(X_{n+1}=(1-w_{I_n})X_n+w_{I_n}m_{I_n}\) with component minimizers \(m_1=0\), \(m_2=1\). Because both multipliers are at most \(1/2\) in absolute value, synchronous coupling of trajectories gives geometric contraction in every finite moment and a unique invariant law. Its mean is
\[
\mu=\frac{(1-p)w_2}{W}.
\]
Taking centered second moments and using independence of \(I_n\) and \(X_n\), the invariant variance is
\[
V=\frac{p(1-p)w_1^2w_2^2}{W^2S},\qquad
S=p(2w_1-w_1^2)+(1-p)(2w_2-w_2^2)>0.
\]
Indeed, the centered random affine forcing takes values \(w_i(m_i-\mu)\), its mean vanishes, and its variance equals \(p(1-p)w_1^2w_2^2/W^2\); the contraction factor for centered variance is \(1-S\). Therefore
\[
R_\kappa(p)=V+\left(\mu-\frac1{\kappa+1}\right)^2.
\]
With \(D_1=\kappa+1+(\kappa-1)p\) and \(D_2=3(\kappa+1)^2+(\kappa^2+2\kappa-3)p\), exact simplification yields
\[
\frac{dR_\kappa}{dp}=\frac{8\kappa^2P_\kappa(p)}{D_1^2D_2^2}.
\]
For \(\kappa\ge1\), \(D_1,D_2>0\), \(P_\kappa(0)=-3(\kappa+1)^4<0\), and
\[
\frac{dP_\kappa}{dp}=2A_\kappa p+B_\kappa>0\quad(0\le p\le1).
\]
At the other endpoint,
\[
P_\kappa(1)=-2\kappa(\kappa+2)(\kappa^2-2\kappa-7).
\]
Consequently the derivative changes from negative to positive at a unique interior root exactly for \(1\le\kappa<1+2\sqrt2\), while it is negative on \([0,1)\) for \(\kappa\ge1+2\sqrt2\). This proves global uniqueness, including the equality threshold. At \(\kappa=1\), the derivative polynomial is linear and its root is \(1/2\).

Solving \(\mu=x_\star\) gives \(p_{\rm ub}=(\kappa+1)/(\kappa+3)\). Algebra gives
\[
P_\kappa(p_{\rm ub})=-\frac{2(\kappa-1)(\kappa+1)^2(\kappa^2+4\kappa+2)}{\kappa+3},
\]
strictly negative for \(\kappa>1\); thus the optimal probability is larger than \(p_{\rm ub}\). The risk at that unbiased probability is \(\kappa^2/((\kappa+1)^2(2\kappa+1))\); at \(p=1\) it is \(1/(\kappa+1)^2\). Multiplication by \((\kappa+1)/4\) proves the objective comparison and limits.

## Verification
The self-contained program `verify.py` (with `requirements.txt`) checks the exact rational derivative, endpoint and unbiased identities symbolically using SymPy. It enumerates all affine-update paths for nine successive steps for five curvatures and five rational sampling probabilities, merging identical states, and verifies 450 exact finite-time first- and second-moment equalities against separate recurrences. A further six curvature grids check the predicted optimizer against 101 candidate probabilities. These are diagnostics: the preceding sign analysis, not enumeration or numerical tests, proves the infinite-horizon and uniqueness statements.

## Relationship to prior work
Asi and Duchi's stochastic approximate proximal point framework (arXiv:1810.05633) supplies the proximal iteration model and studies convergence, optimality, and adaptivity; it does not in the inspected material state this probability-optimized, fixed-step stationary-risk classification. Bianchi, Hachem, and Salim (arXiv:1702.04144) treat invariant behavior for constant-step stochastic forward-backward/resolvent iterations at greater generality but do not in the inspected material identify the displayed sharp two-component switching polynomial. Patrăşcu and Necoara (arXiv:1706.06297) develop nonasymptotic stochastic proximal convergence guarantees. Défossez and Bach (arXiv:1412.0156) study optimal sampling for averaged explicit LMS/SGD, typically using importance weighting to preserve a fixed original objective; the present experiment uses uncorrected proximal component updates and measures terminal stationary error. Exact equivalent derivations in other specialized literature cannot be ruled out.

## Limitations
This is a scalar, two-component, equal-objective-weight benchmark with a fixed proximal step of one and iid selection. Sampling without reweighting changes the stationary bias and implicit target; the deterministic optimal sampler at high curvature therefore **does not** solve the equally weighted objective exactly. The result does not imply that dropping one component is a generally suitable learning procedure, nor does it compare compute budgets, finite-time optima, importance-corrected algorithms, nonlinear objectives, or higher-dimensional problems. The stationary error at \(p=1\) remains positive for every finite \(\kappa\). Independent validation has not been performed.

## References
1. H. Asi and J. C. Duchi, *Stochastic (Approximate) Proximal Point Methods: Convergence, Optimality, and Adaptivity*, arXiv:1810.05633 (first publicly submitted 2018-10-12).
2. P. Bianchi, W. Hachem, and A. Salim, *A Constant Step Forward-Backward Algorithm Involving Random Maximal Monotone Operators*, arXiv:1702.04144 (2017).
3. A. Patrăşcu and I. Necoara, *Nonasymptotic Convergence of Stochastic Proximal Point Algorithms for Constrained Convex Optimization*, arXiv:1706.06297 (2017).
4. A. Défossez and F. Bach, *Constant Step Size Least-Mean-Square: Bias-Variance Trade-offs and Optimal Sampling Distributions*, arXiv:1412.0156 (2014), comparison reference only.
