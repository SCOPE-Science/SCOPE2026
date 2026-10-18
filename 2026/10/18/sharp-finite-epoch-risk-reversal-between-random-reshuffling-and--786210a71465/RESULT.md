# Sharp finite-epoch risk reversal between random reshuffling and stochastic gradient descent

## Finding

For equal-Hessian strongly convex quadratic components, fresh random reshuffling (RR) can have a **larger expected last-epoch objective gap** than with-replacement stochastic gradient descent (SGD), even though both are stable. The exact comparison has a sharp spectral threshold at the normalized component step \(\eta\lambda=1\). This is an *instancewise last-iterate risk comparison*, not a comparison of convergence-rate upper bounds for averaged iterates.

**Theorem (exact finite-epoch risk difference and sharp reversal).** Fix integers \(n\ge2\), \(K\ge1\), \(d\ge1\), a real symmetric positive-definite matrix \(H\in\mathbb R^{d\times d}\), deterministic starting point \(x_0\), arbitrary vectors \(c_1,\ldots,c_n\in\mathbb R^d\), and a constant component step \(0<\eta<2/\lambda_{\max}(H)\). For component objectives
\[
f_i(x)=\tfrac12\langle x,Hx\rangle+\langle c_i,x\rangle+d_i,
\qquad f(x)=n^{-1}\sum_{i=1}^n f_i(x),
\]
run either (i) SGD with an independent uniformly sampled component index at every step or (ii) RR with a fresh independent uniformly random permutation of all \(n\) components for every epoch. Both use \(x\leftarrow x-\eta\nabla f_i(x)\) and exactly \(nK\) component updates. For an orthonormal eigenbasis \((v_j)_{j=1}^d\) of \(H\), with eigenvalues \(\lambda_j>0\), write
\[
\bar c=n^{-1}\sum_{i=1}^nc_i,\quad \delta_i=c_i-\bar c,\quad
r_j=1-\eta\lambda_j,\quad
s_j^2=n^{-1}\sum_{i=1}^n\langle v_j,\delta_i\rangle^2,
\]
\[
Q_n(r)=\sum_{a=0}^{n-1}r^{2a},\qquad W_n(r)=\sum_{a=0}^{n-1}r^a,
\qquad S_{n,K}(r)=\sum_{h=0}^{K-1}r^{2nh}.
\]
Then, writing \(x_\star=-H^{-1}\bar c\),
\[
\begin{aligned}
\Delta_{n,K}&:=\mathbb E[f(x_{nK}^{\rm RR})-f(x_\star)]
-\mathbb E[f(x_{nK}^{\rm SGD})-f(x_\star)]\\
&=\frac{\eta^2}{2(n-1)}\sum_{j=1}^d\lambda_j s_j^2\bigl(Q_n(r_j)-W_n(r_j)^2\bigr)S_{n,K}(r_j).
\end{aligned}
\]
For \(-1<r<1\), \(Q_n(r)-W_n(r)^2\) is positive if \(r<0\), zero if \(r=0\), and negative if \(r>0\). Consequently, **RR has no greater last-epoch expected objective gap for every component-offset instance when \(\eta\lambda_{\max}(H)\le1\)**, and **RR has no smaller gap for every instance when \(\eta\lambda_{\min}(H)\ge1\)**. Each inequality is strict when a corresponding strictly signed eigendirection has \(s_j^2>0\), unless contributions of opposite signs are present. In the mixed spectral regime, the sign can be either direction, even with the same \(H,\eta,n,K\), by varying only the offset vectors. In the scalar case, the exact universal reversal is at \(\eta\lambda=1\), independently of \(n,K,x_0\).

Moreover, throughout the specified stable-step domain,
\[
0\le\mathbb E[f(x_{nK}^{\rm RR})-f(x_\star)]
\le 2\,\mathbb E[f(x_{nK}^{\rm SGD})-f(x_\star)],
\]
and the constant \(2\) is the best possible *universal* factor: for \(n=2\), \(d=1\), \(c_1=-c_2\ne0\), \(x_0=x_\star=0\), and \(\eta\lambda\uparrow2\), the ratio of the two expected objective gaps tends to \(2\) for any fixed \(K\ge1\).

## Assumptions and scope

All expectations are over the sampling schemes only; the data, initial point, Hessian, and step are deterministic. Different RR permutations are independent across epochs; all with-replacement draws are independent. The same deterministic initialization, component functions, gradient counts, and constant \(\eta\) are used in both runs. Distinct components may have different linear and constant terms but **share precisely the same Hessian**. The restriction \(0<\eta<2/\lambda_{\max}(H)\) ensures every scalar propagation factor lies strictly between \(-1\) and \(1\). The result is about the **final iterate after complete epochs**, not internal epoch iterates, within-epoch averages, arbitrary noncommuting component Hessians, or general nonlinear smooth objectives.

## Proof

Write \(e_t=x_t-x_\star\). Since \(\nabla f_i(x)=H(x-x_\star)+\delta_i\), one step is \(e_{t+1}=(I-\eta H)e_t-\eta\delta_{i_t}\). Let \(\delta_{i,j}=\langle v_j,\delta_i\rangle\), so \(\sum_i\delta_{i,j}=0\). In the \(j\)-th eigenmode, the net noise introduced in one epoch is a weighted sum
\[
Z_j=-\eta\sum_{a=0}^{n-1}r_j^a\delta_{I_{n-a},j}.
\]
Each epoch has mean-zero \(Z_j\), independent of the previous epoch state; the deterministic multiplier of the previous state is \(r_j^n\) in **both** sampling schemes.

For with-replacement indices, the sampled \(\delta_{I,j}\) have variance \(s_j^2\) and are independent, giving \(\mathbb E Z_j^2=\eta^2s_j^2Q_n(r_j)\). For a uniform random permutation, diagonal covariances equal \(s_j^2\), while for two distinct positions
\[
\mathbb E[\delta_{I_a,j}\delta_{I_b,j}]
=\frac{1}{n(n-1)}\sum_{i\ne k}\delta_{i,j}\delta_{k,j}
=-\frac{s_j^2}{n-1}.
\]
Thus the reshuffled epoch-noise variance is
\[
\mathbb E Z_j^2=\frac{\eta^2s_j^2}{n-1}\bigl(nQ_n(r_j)-W_n(r_j)^2\bigr).
\]
Independent fresh epochs eliminate cross-terms. Iterating the scalar epoch recurrence for \(K\) epochs gives, with \(e_{0,j}=\langle v_j,x_0-x_\star\rangle\),
\[
\begin{aligned}
\mathbb E[e_{nK,j}^{\rm SGD}{}^2]&=r_j^{2nK}e_{0,j}^2
+\eta^2s_j^2Q_n(r_j)S_{n,K}(r_j),\\
\mathbb E[e_{nK,j}^{\rm RR}{}^2]&=r_j^{2nK}e_{0,j}^2
+\frac{\eta^2s_j^2}{n-1}\bigl(nQ_n(r_j)-W_n(r_j)^2\bigr)S_{n,K}(r_j).
\end{aligned}
\]
Because \(f(x)-f(x_\star)=\tfrac12\sum_j\lambda_je_j^2\), multiplying by \(\lambda_j/2\) and summing proves the exact difference formula. This calculation is unaffected by cross-eigenmode correlations, since the objective contains no cross-eigenmode terms.

The geometric-sum identity, valid for \(-1<r<1\),
\[
Q_n(r)-W_n(r)^2
=\frac{2(1-r^n)(r^n-r)}{(1-r)^2(1+r)},
\]
has a strictly positive denominator and \(1-r^n>0\). Since \(r^n-r=r(r^{n-1}-1)\), and \(r^{n-1}-1<0\) for \(0<|r|<1\) and \(n\ge2\), its sign is \(-\operatorname{sign}(r)\); at \(r=0\) it vanishes. All other factors in the difference are nonnegative. For either strict direction, choose \(\delta_1=u,\delta_2=-u\), all other offsets zero, with \(u\) an eigenvector in that spectral region. This also proves the two-sided mixed-spectrum examples by choosing \(u\) in either of the two regions.

Finally, Cauchy–Schwarz gives \(W_n(r)^2\le nQ_n(r)\), whence the reshuffled epoch-noise variance is at most \(n/(n-1)\) times the with-replacement variance and hence at most twice it. The deterministic part of each expected objective gap is identical and nonnegative, so adding this common part retains the factor-two bound. To show sharpness, in dimension one with \(n=2\), \(c_1=-c_2\ne0\), and \(x_0=x_\star=0\), the entire objective gap is noise. Its exact RR/SGD ratio is
\[
\frac{2Q_2(r)-W_2(r)^2}{Q_2(r)}
=\frac{(1-r)^2}{1+r^2}\longrightarrow2
\quad\text{as }r\downarrow-1
\quad(\eta\lambda\uparrow2).
\]
The factor \(S_{2,K}\) cancels for every \(K\ge1\). This completes the proof.

## Verification

An independent exact-arithmetic enumeration in `check.py` compares **every** sampled path for small instances against the closed formulas, using rational numbers rather than Monte Carlo. The cases include \(n=3,K=2\) at \(r=1/2,0,-1/2\), \(n=4,K=1\) at \(r=-1/2\), and two mixed-spectrum two-dimensional configurations at fixed eigenvalues \(1,3\) and step \(1/2\), showing opposite comparison signs. For the scalar \(n=3,K=2,r=1/2\) case, exact gaps are \(3649/32768\) (RR) and \(10929/32768\) (SGD); for \(r=-1/2\) they are \(126369/32768\) (RR) and \(98289/32768\) (SGD). Running `python check.py` prints each comparison and asserts exact equality with the symbolic formula. Enumeration independently checks finite cases only; the universal theorem follows from the analytic covariance and geometric-sum argument, not from enumeration.

## Relationship to prior work

Zijian Liu's 2026 theorem compares **optimized upper-rate guarantees for averaged iterates** under random reshuffling and SGD. It does not assert samplewise or instancewise dominance of the **last iterate's expected objective gap** at the same fixed step. The present result specifies a domain where that stronger interpretation would be false. Safran–Shamir (2020, 2021) derive tight rate bounds for reshuffling on quadratics, including commuting curvature, but not this all-finite-epoch exact RR-minus-SGD loss sign threshold and sharp two-factor ceiling. De Sa (2020) shows random reshuffling need not dominate under differing component Hessians, whereas this theorem has exactly matching Hessians and isolates a pure finite-population noise effect. Domingo-Enrich (2022) analyzes stationary and small-step spectral variance of shuffled stochastic methods; stationary variance can be related to the infinite-epoch limit of our formulas, but those results are not the stated **finite-epoch exact spectral comparison**. Li (2026) obtains last-epoch rates with controlled steps, not an exact instancewise sign classification over the whole stable-step interval. We make no claim to having originated stationary shuffled-noise covariance formulas, or to a superior general convergence rate.

## Limitations

A high-level 2026 preprint on metric-aware shuffling could not be inspected in full, leaving residual literature-coverage risk; the accessible scientific description emphasizes noncommuting multiplicative update matrices rather than this common-Hessian additive-noise model. Cross-mode error covariances may be nonzero, so the objective result must not be interpreted as a Loewner covariance ordering. Extensions to component-dependent Hessians, nonlinear losses, partial epochs, unequal step sizes, and adaptive sampling remain unproved. The factor-two upper bound is a worst-case supremum approached at the stability boundary, not necessarily attained by a strictly stable step. Independent validation has not been performed.

## References

1. Z. Liu, *Random Reshuffling Dominates Stochastic Gradient Descent*, Proceedings of COLT (2026), arXiv:2606.32005, first submitted 2026-06-30; https://arxiv.org/abs/2606.32005; https://proceedings.mlr.press/v336/liu26d.html.
2. I. Safran and O. Shamir, *How Good is SGD with Random Shuffling?*, COLT/PMLR 125 (2020); https://proceedings.mlr.press/v125/safran20a.html.
3. I. Safran and O. Shamir, *Random Shuffling Beats SGD Only After Many Epochs on Ill-Conditioned Problems*, arXiv:2106.06880 (2021); https://arxiv.org/abs/2106.06880.
4. C. M. De Sa, *Random Reshuffling is Not Always Better*, NeurIPS (2020).
5. C. Domingo-Enrich, *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, arXiv:2206.00632 (2022); https://arxiv.org/abs/2206.00632.
6. J. Li, *Centered Permutation Prefixes for SGD with Random Reshuffling: Sharp Rates, Hölder Geometry, and Composite Proximal Extensions*, arXiv:2609.04578 (2026); https://arxiv.org/abs/2609.04578.
