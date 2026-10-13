# Sharp Gaussianity and fourth-moment boundaries for randomly stepped stochastic theta schemes

## Finding
For a one-dimensional Ornstein–Uhlenbeck equation, independently randomized positive step sizes in the stochastic theta discretization have an exact stationary Gaussianity criterion and an independent sharp fourth-moment criterion. Under the finite-support and mean-square stability conditions below, the stationary numerical law is Gaussian **if and only if** either the step is almost surely constant or \(\theta=1/2\). For **every real \(p>0\)**, the stationary absolute \(p\)-th moment is finite **if and only if** \(\mathbb E|R(H)|^p<1\). When \(\mathbb E[R(H)^4]<1\), its excess fourth cumulant equals a positive conditional-variance defect; otherwise its fourth moment is infinite.

A finite-step numerical consequence is that two distinct positive step-size laws with precisely the same first and second step moments can have the **same finite stationary variance** but opposite fourth-moment behavior. For explicit Euler–Maruyama applied to \(dX=-X\,dt+dW\), use
\[
\begin{array}{c|c|c}
&\text{step sizes}&\text{respective probabilities}\\ \hline
A&(1/2,3/2)&(1/2,1/2)\\
B&(11/12,4)&(36/37,1/37).
\end{array}
\]
Both laws satisfy \(\mathbb EH=1\), \(\mathbb EH^2=5/4\), and yield stationary variance \(4/3\). Law \(A\) yields stationary fourth moment \(92/15\), while law \(B\) yields infinite fourth moment despite the same contraction factor \(\mathbb E[R(H)^2]=1/4\). For law \(B\), the **entire finite-moment range** is \(0<p<\kappa\), where \(\kappa\in(3,4)\) uniquely solves \(36(1/12)^\kappa+3^\kappa=37\). In particular, \(\mathbb E[R(H)^4]=1261/576>1\).

## Assumptions and scope
Fix \(\lambda>0\), \(\sigma>0\), \(\theta\in[0,1]\), and the scalar SDE \(dX_t=-\lambda X_t\,dt+\sigma\,dW_t\). Let \((H_k,Z_k)_{k\ge0}\) be independent and identically distributed pairs, with \(Z_k\sim N(0,1)\) independent of \(H_k\). The common step law is any probability distribution with **finite, nonempty support contained in \((0,\infty)\)**. The randomized stochastic theta update is
\[
X_{k+1}=R(H_k)X_k+S(H_k)Z_k,\qquad
R(h)=\frac{1-(1-\theta)\lambda h}{1+\theta\lambda h},\quad
S(h)=\frac{\sigma\sqrt h}{1+\theta\lambda h}.
\]
It is the theta drift discretization with a conditionally Gaussian Brownian increment of variance \(H_k\), not a scheme that samples the physical SDE at iid deterministic times without numerical error. Assume \(m_2:=\mathbb E[R(H)^2]<1\). Define \(m_4:=\mathbb E[R(H)^4]\), \(b_2:=\mathbb E[S(H)^2]\), and \(v=b_2/(1-m_2)>0\). All expectations here involve only the fresh step law, except where the stationary state is explicitly named.

## Proof
**Existence, uniqueness, and variance.** On a bi-infinite independent extension of the driving pairs, form the causal series
\[
X_\infty=\sum_{j=0}^{\infty}\left(\prod_{i=1}^{j}R(H_{-i})\right)S(H_{-j-1})Z_{-j-1},
\]
with the empty product equal to \(1\). The \(L^2\) norms of successive summands are \(m_2^{j/2}\sqrt{b_2}\), hence the series converges in \(L^2\). Shifting its independent input sequence gives the stationarity equation. Synchronous coupling of any two initial states multiplies their difference after \(k\) steps by \(\prod_{i=0}^{k-1}R(H_i)\), which converges to zero in probability because its squared expectation equals \(m_2^k\). Coupling a stationary candidate with the constructed stationary series shows uniqueness of the invariant probability law, even without assuming the candidate has finite moments. Its mean is zero, and independence of the fresh pair from the past gives the variance identity \(v=m_2v+b_2\).

**Gaussianity necessity.** Suppose this stationary state is centered Gaussian with variance \(v\). Conditional on the fresh step \(H=h\), the next state is centered Gaussian of variance
\[
Q(h):=R(h)^2v+S(h)^2.
\]
The mixture has fourth moment \(3\mathbb E[Q(H)^2]\), whereas a centered Gaussian with variance \(v=\mathbb E Q(H)\) has fourth moment \(3v^2\). Thus Gaussianity requires \(\operatorname{Var}(Q(H))=0\), that is, \(Q(h)=v\) at every positive-probability step. Rearranging \(S(h)^2=v(1-R(h)^2)\) gives
\[
v=\frac{\sigma^2}{\lambda[2+(2\theta-1)\lambda h]}.
\]
Because \(\sigma,\lambda,v>0\), this equation at two distinct supported steps implies \(2\theta-1=0\). The same argument works even if some supported step expands deterministically; such a step cannot satisfy the positive variance equation.

**Gaussianity sufficiency.** For a singleton step law, stationarity is an ordinary stable Gaussian autoregression. For \(\theta=1/2\), the identity \(S(h)^2=[\sigma^2/(2\lambda)](1-R(h)^2)\) holds at *every* \(h>0\). Every conditional transition therefore preserves \(N(0,\sigma^2/(2\lambda))\), and uniqueness proves this is the stationary law. This also proves that the randomized midpoint scheme preserves the exact scalar OU equilibrium for any finite-support positive step law.

**Complete moment spectrum.** Conditional on all step sizes in the stationary causal series, the innovations are independent centered Gaussians. Thus the stationary state is a Gaussian scale mixture \(X_\infty\mid(H_j)\sim N(0,V)\), where
\[
V=\sum_{j=0}^\infty\left(\prod_{i=1}^jR(H_{-i})^2\right)S(H_{-j-1})^2
\]
and \(V\stackrel d=S(H)^2+R(H)^2V'\), with \(V'\) an independent copy of \(V\). The sum is finite almost surely because its expectation is \(v\). For every real \(p>0\), let \(q=p/2\). If \(\mathbb E|R(H)|^p<1\), then \(\mathbb EV^q<\infty\): for \(q\ge1\) apply Minkowski's inequality to the nonnegative variance-series summands, whose \(L^q\) norms decay geometrically as \((\mathbb E|R|^p)^{j/q}\); for \(0<q\le1\), use \((\sum_jt_j)^q\le\sum_jt_j^q\) and the same geometric bound. Conversely, if \(\mathbb EV^q<\infty\) and \(\mathbb E|R|^p\ge1\), the almost-sure strict inequality
\[
(S(H)^2+R(H)^2V')^q>(R(H)^2V')^q
\]
because \(S(H)^2>0\), would imply \(\mathbb EV^q>\mathbb E|R|^p\,\mathbb EV^q\ge\mathbb EV^q\), impossible. Finally, for a standard normal \(G\), conditional Gaussianity gives \(\mathbb E|X_\infty|^p=\mathbb E|G|^p\,\mathbb EV^{p/2}\). This proves the asserted if-and-only-if criterion for **all positive real moment orders**, including the fourth-order boundary below. It does not prove a precise tail asymptotic.

**Fourth moment and cumulant.** The fourth power of the stationary identity, using the centered Gaussian fresh noise, gives, provided the fourth moment is finite,
\[
(1-m_4)\mathbb E[X_\infty^4]
=6v\mathbb E[R(H)^2S(H)^2]+3\mathbb E[S(H)^4]>0.
\]
Consequently, finite fourth moment is impossible if \(m_4\ge1\). Conversely, if \(m_4<1\), the \(L^4\) norms of successive causal-series summands decay geometrically as \(m_4^{j/4}\), so \(\mathbb E[X_\infty^4]<\infty\). Subtracting \(3v^2\) from the displayed recurrence and using \(\mathbb E Q(H)=v\), we obtain the **exact** fourth-cumulant identity
\[
\mathbb E[X_\infty^4]-3v^2
=\frac{3\operatorname{Var}(Q(H))}{1-m_4}.
\]
Thus the fourth moment exists exactly when \(m_4<1\); in this region it is strictly super-Gaussian for any nonconstant step distribution and \(\theta\ne1/2\), while it is Gaussian when the criterion above holds. The second moment remains finite in both regimes by hypothesis. No assertion of a particular power-law tail exponent is required or proved.

**Exact moment-matched witness.** Set \(\lambda=\sigma=1\), \(\theta=0\). Then \(R(h)=1-h\), \(S(h)^2=h\), and \(m_2=1-2\mathbb EH+\mathbb EH^2\). For the two displayed rational laws, direct exact evaluation gives
\[
\mathbb EH_A=\mathbb EH_B=1,\quad
\mathbb EH_A^2=\mathbb EH_B^2=5/4,\quad
m_2=1/4,\quad v=4/3.
\]
For law \(A\), \(m_4=1/16\), \(\operatorname{Var}(Q(H))=1/4\), and therefore
\[
\mathbb E[X_{\infty,A}^4]
=3(4/3)^2+\frac{3(1/4)}{1-1/16}=92/15.
\]
For law \(B\), \(m_4=1261/576>1\), so its unique finite-variance stationary law has infinite fourth moment. More precisely, its positive-order moment function is controlled by
\[
M(p)=\frac{36}{37}\left(\frac1{12}\right)^p+\frac1{37}3^p.
\]
We have \(M(0)=1\), \(M'(0)=[36\log(1/12)+\log3]/37<0\), \(M''(p)>0\) for every real \(p\), \(M(3)=1297/1776<1\), and \(M(4)=1261/576>1\). Strict convexity and divergence as \(p\to\infty\) show that \(M(p)=1\) has exactly one positive solution \(\kappa\in(3,4)\), and \(M(p)<1\) holds precisely for \(0<p<\kappa\). Hence \(\mathbb E|X_{\infty,B}|^p<\infty\) **if and only if** \(0<p<\kappa\), whereas law \(A\) has finite moments at all positive orders because \(|R(H)|=1/2\) for both of its steps. This completes the classification and witness.

## Verification
Run `python3 verify.py` from the directory containing this document and the standalone verifier. It uses only Python standard-library rational arithmetic and checks the exact step moments, \(m_2\), \(m_4\), the rational bounds \(M(3)<1<M(4)\), both stationary variance identities, the finite-fourth-moment identity, and 210 rational-parameter consistency cases. Its `VERIFY_OK` result confirms the listed finite algebraic identities; the universal statements and the infinite fourth moment follow from the proof above, not enumeration or simulation.

## Relationship to prior work
Jiang, Liu, and Weng (arXiv:1801.09047v1, §2 equation (2.6), §4 Example 4.1) introduce the fixed-step stochastic theta scheme and calculate its scalar OU Gaussian stationary variance. We use their normalization, and make **no novelty claim** for that fixed-step result. The result above concerns a genuinely random and independent step at every update and identifies exact Gaussianity, kurtosis, and fourth-moment boundaries.

Wen and Li (2022) investigate almost-sure stability for random-variable-step stochastic theta schemes. Only its publisher metadata and abstract were accessible for the present comparison; the full text was not available. It is therefore a material residual literature-comparison risk, especially for unstated special examples. Their stated target is almost-sure stability, not stationary fourth moments.

Jiang, Hu, and Lu (2020) study fixed-step stochastic theta methods for SDEs with Markovian switching; their transition kernel is different from independent random timestep resampling of one OU equation. Nakao (1998) analyzes general multiplicative-noise heavy-tail effects; those **general mechanisms are prior work**. The specific numerical-method Gaussianity classification and the rational equal-step-moment witness are the statements assessed here, not the underlying random-affine moment principle.

## Limitations
The result is scalar, linear, additive-Gaussian-noise, exact-arithmetic, iid-step, and finite-support. It assumes \(m_2<1\); it does not classify unstable second moments or general adaptive/path-dependent steps, nonlinear drifts, multidimensional SDEs, or wall-clock accuracy. A finite fourth moment is not equivalent to a Gaussian tail. The exact positive moment-cutoff \(\kappa\) for law \(B\) does not establish a precise asymptotic power-law form or divergence of sample paths. Priority is not independently certified, and an inaccessible directly relevant 2022 publication remains a specified risk. Independent audit has not been performed.

## References
1. Y. Jiang, W. Liu, L. Weng, *Stationary distribution of the stochastic theta method for nonlinear stochastic differential equations*, arXiv:1801.09047v1 (first posted 2018-01-27), https://arxiv.org/abs/1801.09047; Numerical Algorithms 83 (2020), 1531–1553. See §2 and §4 Example 4.1.
2. X. Wen, Z. Li, *Almost sure stability of stochastic theta methods with random variable stepsize for stochastic differential equations*, International Journal of Control 96 (2023), 1551–1567, first available accepted version 2022-03-22; DOI:10.1080/00207179.2022.2056516 (abstract only inspected).
3. Y. Jiang, L. Hu, J. Lu, *The stochastic theta method for stationary distribution of stochastic differential equations with Markovian switching*, Advances in Difference Equations 2020, 667, DOI:10.1186/s13662-020-03129-3 (open-access full text inspected).
4. H. Nakao, *Asymptotic power law of moments in a random multiplicative process with weak additive noise*, arXiv:cond-mat/9802030v1 (1998), https://arxiv.org/abs/cond-mat/9802030 (full text inspected).
