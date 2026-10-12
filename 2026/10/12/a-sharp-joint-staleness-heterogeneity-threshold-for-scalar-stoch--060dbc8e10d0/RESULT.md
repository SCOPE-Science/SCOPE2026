# A sharp joint staleness–heterogeneity threshold for scalar stochastic gradient descent

## Finding
For independent one-step stale reads and independent positive random component curvatures, constant-step scalar stochastic gradient descent has a complete, distribution-free mean-square stability criterion. With normalized step \(s=\eta\mu>0\), stale-read probability \(p\in[0,1]\), and normalized curvature second moment \(\vartheta=\mathbb E[A^2]/\mu^2\ge1\), convergence in mean square from **every** deterministic two-state initialization holds exactly when
\[
\boxed{\vartheta(s+p s^2)<2.}
\]
Equivalently, its sharp stepsize ceiling is
\[
\boxed{s_*(p,\vartheta)=\frac{4}{\vartheta+\sqrt{\vartheta^2+8p\vartheta}},\qquad 0<s<s_*(p,\vartheta).}
\]
At equality the mean-square convergence property fails, not merely a particular sufficient estimate. The threshold depends on the entire law of positive sampled curvatures only through its first two moments.

The two independent noise mechanisms can be jointly destabilizing although each is individually harmless: with independent, equally likely curvatures \(A\in\{1/2,3/2\}\), delay probability \(p=1/2\), and step \(\eta=6/5\), the combined iteration is mean-square unstable from every nonzero deterministic two-state initialization. Suppressing only staleness, or suppressing only curvature variation, makes the same stepsize mean-square stable.

## Assumptions and scope
Let \((A_k)_{k\ge0}\) be i.i.d. **strictly positive** scalar curvatures with \(\mu=\mathbb E[A_k]\in(0,\infty)\) and \(\mathbb E[A_k^2]<\infty\). Let \((D_k)_{k\ge0}\) be independent i.i.d. Bernoulli stale-read indicators with \(\mathbb P(D_k=1)=p\in[0,1]\), independent of the entire curvature sequence and deterministic initial states. For fixed \(\eta>0\), consider the exact scalar recursion
\[
x_{k+1}=x_k-\eta A_k x_{k-D_k},\qquad k\ge0,
\]
from arbitrary deterministic \(x_{-1},x_0\in\mathbb R\). This is stochastic gradient descent for interpolating component quadratics \(f_{A}(x)=A x^2/2\), with a sampled gradient evaluated at either the current iterate or the immediately preceding iterate. Here "mean-square convergence" means \(\lim_{k\to\infty}\mathbb E[x_k^2]=0\), without requiring a uniform per-iteration contraction.

Normalize \(C_k=A_k/\mu\), so \(\mathbb E C_k=1\) and \(\mathbb E C_k^2=\vartheta\ge1\), and write \(s=\eta\mu\). No bounded-support condition, higher curvature moments, nonnegative-initial-state restriction, or finite component count is assumed.

## Proof
Condition on the past \(\mathcal F_k\), and put \(x=x_k\), \(y=x_{k-1}\), and \(z=x_{k+1}\). Independence and the normalized curvature moments give the exact conditional identities
\[
\begin{aligned}
\mathbb E[z^2\mid\mathcal F_k]
&=\bigl[1-2(1-p)s+(1-p)\vartheta s^2\bigr]x^2
       -2psxy+p\vartheta s^2 y^2,\\
\mathbb E[zx\mid\mathcal F_k]
&=\bigl[1-(1-p)s\bigr]x^2-psxy.
\end{aligned}
\]
These equalities require only the two stated moments.

For the fixed positive step \(s\), define the quadratic energy
\[
V_s(x,y)=(1+ps)x^2-2psxy+p\vartheta s^2(1+ps)y^2.
\]
For \(p>0\), its matrix has positive leading diagonal \(1+ps\) and determinant
\[
\det G_s=p s^2\bigl[\vartheta(1+ps)^2-p\bigr]>0.
\]
The strict inequality follows from \(\vartheta\ge1\), \(0<p\le1\), and \(s>0\), including the endpoint \(p=\vartheta=1\). Therefore \(V_s\) is positive definite for every \(p>0\). For \(p=0\), it reduces to \(V_s(x,y)=x^2\); the unused lag state then has no effect on the update.

Inserting the two exact conditional moments into \(V_s(z,x)\), the cross and past-state terms cancel identically, leaving
\[
\boxed{
\mathbb E[V_s(x_{k+1},x_k)\mid\mathcal F_k]
     -V_s(x_k,x_{k-1})
=s\bigl[\vartheta(s+ps^2)-2\bigr]x_k^2.
}
\]
For \(\vartheta(s+ps^2)<2\), set \(\delta=s[2-\vartheta(s+ps^2)]>0\). Taking expectations and telescoping for any \(N\ge1\) gives
\[
\delta\sum_{k=0}^{N-1}\mathbb E[x_k^2]
=V_s(x_0,x_{-1})-\mathbb E[V_s(x_N,x_{N-1})]
\le V_s(x_0,x_{-1}).
\]
Thus the nonnegative series \(\sum_{k\ge0}\mathbb E[x_k^2]\) is summable and its terms tend to zero. This proves sufficiency for every initial pair, including \(p=0\).

If \(\vartheta(s+ps^2)\ge2\), the same exact identity makes \(\mathbb E[V_s(x_k,x_{k-1})]\) nondecreasing. For \(p>0\), every nonzero deterministic initial pair has strictly positive initial energy. If mean-square convergence nevertheless held, Cauchy–Schwarz would force the expectation of this fixed quadratic form to tend to zero, a contradiction. For \(p=0\), choose any \(x_0\ne0\): the scalar identity makes \(\mathbb E[x_k^2]\) nondecreasing, so convergence fails. Necessity, including equality, follows.

For \(s>0\) the function \(s\mapsto\vartheta(s+ps^2)\) is strictly increasing, vanishes at zero, and tends to infinity. Its unique positive equality root is the displayed \(s_*\); the rationalized expression is valid also at \(p=0\). It decreases strictly with curvature heterogeneity \(\vartheta\) and with \(p\) whenever \(p\) is increased from a smaller nonnegative value.

For the promised interaction example, \(\mu=1\) and \(\vartheta=5/4\). At \(p=1/2\) and \(s=6/5\),
\[
\vartheta(s+ps^2)=\frac54\left(\frac65+\frac{18}{25}\right)=\frac{12}{5}>2.
\]
With the identical curvature law but \(p=0\) the left side is \(3/2<2\); with \(p=1/2\) but constant curvature \(A\equiv1\), it is \(48/25<2\). This proves genuine joint, rather than separate, destabilization.

## Verification
The standalone file `checks/verify_exact.py` checks the general conditional-drift polynomial identity, the independent three-coordinate second-moment transfer determinant, and positivity of the energy determinant symbolically using SymPy. It also checks the conditional-drift identity against all four outcomes of independent two-point curvatures and Bernoulli lag in 2,800 exact-rational test cases. Its execution produced `VERIFY_OK symbolic_drift=1 symbolic_moment_matrix=1 exact_cases=2800`. The symbolic identity and positivity argument, not the finite tests, establish the infinite-parameter theorem.

An independent moment-system cross-check uses the state \((\mathbb E[x_k^2],\mathbb E[x_kx_{k-1}],\mathbb E[x_{k-1}^2])^\top\) and the matrix
\[
T=\begin{pmatrix}
1-2(1-p)s+(1-p)\vartheta s^2&-2ps&p\vartheta s^2\\
1-(1-p)s&-ps&0\\
1&0&0
\end{pmatrix},
\qquad \det(I-T)=s[2-\vartheta(s+ps^2)].
\]
This determinant is an algebraic consistency check, not a standalone spectral proof; the explicit energy provides both directions of convergence.

## Relationship to prior work
Niu, Recht, Ré and Wright's *Hogwild!* (public June 28, 2011) motivates asynchronous stochastic-gradient updates. Duchi, Chaturapruek and Ré (2015) rigorously analyze broad asynchronous stochastic optimization with changing stepsizes, rather than the present exact constant-step scalar stability frontier. Gomez, Orosz and Murray (2013) and Gomez, Qin, Orosz and Murray (2014) develop second-moment stability methods for **fixed-coefficient** stochastic-delay recurrences; their inspected scalar and vector models do not contain an independently resampled curvature coefficient and do not state the displayed joint \((p,\vartheta)\) frontier. The later full SGD stability analysis of Mulayoff and Michaeli (2023) concerns current-iterate sampled gradients and thereby covers the no-lag limit, not the independent-lag interaction.

The generic practice of lifting random linear recurrences to second moments and the no-lag threshold \(s<2/\vartheta\) are not new. Nor is the fixed-coefficient stochastic-delay specialization claimed independently. The contribution is the complete sharp joint two-moment/one-step-lag classification for sampled positive quadratic curvatures, with an explicit energy and an exact synergy witness. Its implication is strictly stronger than placing separate no-delay and deterministic-curvature sufficient conditions side by side.

## Limitations
The update is a simplified, single-scalar iid stale-read model. It does not include delayed writes, update collisions, state-dependent delay, correlated sampling, higher or random unbounded lags, asynchronous wall-clock throughput, additive gradient noise at the optimizer, or coupled multidimensional Hessians. The theorem classifies **mean-square convergence**, not optimal convergence speed, finite-time accuracy, almost-sure behavior, or the general applicability of asynchronous SGD. The separate boundary cases \(p=0\) and \(\vartheta=1\) are traditional topics; novelty is claimed only for the joint characterization and its sharp interaction. Older asynchronous linear-recursion and random-feedback literature could contain an equivalent formula under different terminology; in particular the full 1993 Beidas–Papavassilopoulos article was not obtained for a decisive complete-text comparison.

## References
1. F. Niu, B. Recht, C. Ré, S. J. Wright, *Hogwild!: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent*, public 2011-06-28, https://optimization-online.org/2011/06/3080/ ; arXiv:1106.5730, https://arxiv.org/abs/1106.5730.
2. J. Duchi, S. Chaturapruek, C. Ré, *Asynchronous Stochastic Convex Optimization*, arXiv:1508.00882v1 (2015-08-04), https://arxiv.org/abs/1508.00882.
3. M. Gomez, G. Orosz, R. M. Murray, *Stability of Discrete-Time Systems with Stochastically Delayed Feedback*, European Control Conference (2013), DOI:10.23919/ECC.2013.6669802, accessible PDF https://scispace.com/pdf/stability-of-discrete-time-systems-with-stochastically-w8py0ve66h.pdf.
4. M. M. Gomez, W. B. Qin, G. Orosz, R. M. Murray, *Exact Stability Analysis of Discrete-Time Linear Systems with Stochastic Delays*, American Control Conference (2014), DOI:10.1109/ACC.2014.6859470, author PDF https://websites.umich.edu/~orosz/articles/ACC_2014_paper2.pdf.
5. R. Mulayoff, T. Michaeli, *Exact Mean Square Linear Stability Analysis for SGD*, arXiv:2306.07850 (2023), https://arxiv.org/abs/2306.07850.
6. B. F. Beidas, G. P. Papavassilopoulos, *Convergence Analysis of Asynchronous Linear Iterations with Stochastic Delays*, Parallel Computing 19 (1993), 281–302, DOI:10.1016/0167-8191(93)90038-M (abstract inspected; full text not verified).
