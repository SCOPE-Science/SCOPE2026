# Sharp cached-versus-refreshed stability thresholds for spectral-step SketchySGD

## Finding
Consider two interpolating least-squares components \(f_1(w)=\tfrac12 w_1^2\) and \(f_2(w)=\tfrac12 w_2^2\), with average \(f(w)=\tfrac14\|w\|_2^2\). Use independent one-example Hessian, learning-rate, and stochastic-gradient minibatches in the ideal exact-arithmetic version of the spectral-learning-rate rule (3) of Frangella–Rathore–Zhao–Udell. Form a rank-one Nyström estimate of the sampled Hessian, regularize it by \(\rho I\), and choose spectral step \(\eta=\alpha/L_{P,T}\) from an independently sampled Hessian. The full Hessian is \(I_2/2\) and has condition number \(1\).

For every \(\rho>0\), \(0<\alpha<2\), integer \(k\geq0\), and deterministic \(w_0\in\mathbb R^2\), put \(t=\rho/(1+\rho)\) and \(Q(g)=1-g+g^2/2\). If the sampled preconditioner and spectral learning rate are **cached** for all iterations, while gradient minibatches are resampled independently, then
\[
\mathbb E\|w_k^{\mathrm{cache}}\|_2^2=\left[\tfrac12 Q(\alpha)^k+\tfrac14 Q(\alpha t)^k+\tfrac14 Q(\alpha/t)^k\right]\|w_0\|_2^2.
\]
If the preconditioner and learning-rate minibatches are **refreshed independently every step**, then
\[
\mathbb E\|w_k^{\mathrm{fresh}}\|_2^2=\left[\tfrac12 Q(\alpha)+\tfrac14 Q(\alpha t)+\tfrac14 Q(\alpha/t)\right]^k\|w_0\|_2^2.
\]
For \(w_0\ne0\), the cached process converges in mean square precisely when \(\rho>\alpha/(2-\alpha)\). At equality its squared-error expectation tends to \(\|w_0\|_2^2/4\); below this threshold it diverges to infinity. At the source's ideal spectral scaling \(\alpha=1/2\), the cached stability threshold is \(\rho>1/3\); the refreshed stability threshold is strictly lower:
\[
\rho>\rho_\star:=\frac{1+\sqrt3-\sqrt{3+2\sqrt3}}{\sqrt{3+2\sqrt3}-\sqrt3}\approx0.233944912506935.
\]
At the refreshed equality its expected squared norm stays constant; below it the expectation diverges. Thus a nonempty interval of positive regularizations stabilizes refreshed sampling while cached sampling fails.

For instance, at \(\rho=1/4\) and \(\alpha=1/2\),
\[
\mathbb E\|w_k^{\mathrm{cache}}\|_2^2=\left[\tfrac12(5/8)^k+\tfrac14(181/200)^k+\tfrac14(13/8)^k\right]\|w_0\|_2^2,
\qquad \mathbb E\|w_k^{\mathrm{fresh}}\|_2^2=(189/200)^k\|w_0\|_2^2.
\]
The cached mean-square error diverges although every fixed sampled environment has a decaying conditional **mean iterate**; the refreshed mean-square error converges geometrically.

## Assumptions and scope
The domain is \(\mathbb R^2\). The stochastic-gradient minibatch \(B\), curvature minibatch \(S\), and step-estimation minibatch \(T\) are individually uniform on \(\{1,2\}\) and mutually independent. Each consists of a single example. The per-example Hessian is \(H_j=e_je_j^\top\) and \(\nabla f_j(w)=w_je_j\). The ideal Gaussian rank-one Nyström operation is in exact arithmetic and uses a test direction with nonzero component along \(e_S\) (probability one). Its approximation is exactly \(H_S\), and the preconditioner is \(P_S=H_S+\rho I\). The step is defined exactly by
\[
\eta(S,T)=\frac{\alpha}{\lambda_{\max}(P_S^{-1/2}H_TP_S^{-1/2})},\qquad w^+=w-\eta(S,T)P_S^{-1}\nabla f_B(w).
\]
All random choices within an iteration are independent, and all fresh environments across iterations are independent. For cached sampling, the initial \((S,T)\) pair is held fixed but the \(B\) values remain independent. Mean-square convergence means \(\mathbb E\|w_k\|_2^2\to0\) for each nonzero deterministic starting point. No claim is made about averaging algorithms, adaptive damping, finite-precision Nyström shifts, or finite-iteration eigenvalue estimators.

## Proof
Because \(H_S=e_Se_S^\top\), a Gaussian test direction \(v\) gives sketch \(Y=H_Sv=v_Se_S\). Whenever \(v_S\ne0\), the exact Nyström formula \(Y(v^\top Y)^{-1}Y^\top\) equals \(e_Se_S^\top=H_S\). Therefore \(P_S\) is diagonal, and \(\lambda_{\max}(P_S^{-1/2}H_TP_S^{-1/2})=1/P_{S,TT}\), so \(\eta(S,T)=\alpha P_{S,TT}\).

Fix coordinate \(j\in\{1,2\}\). Its multiplicative factor is \(1-g_j\) when \(B=j\), and \(1\) otherwise, where \(g_j=\eta(S,T)/P_{S,jj}\). The four equiprobable choices \((S,T)\), ordered as \((j,j),(j,3-j),(3-j,j),(3-j,3-j)\), yield gains \(\alpha,\alpha t,\alpha,\alpha/t\). The one-step conditional squared multiplier averaged over \(B\) is therefore \(\tfrac12[1+(1-g_j)^2]=Q(g_j)\).

In the cached scheme, conditioning on \((S,T)\) and iterating independent gradient samples gives \(\mathbb E[w_{j,k}^2\mid S,T]=Q(g_j)^k w_{j,0}^2\). Averaging the four equiprobable environments, then summing \(j=1,2\), gives the cached formula. In the refreshed scheme, fresh independence at every iteration gives \(\mathbb E[w_{j,k+1}^2\mid w_{j,k}]=M w_{j,k}^2\), where \(M=[2Q(\alpha)+Q(\alpha t)+Q(\alpha/t)]/4\). Iteration and summation yield the refreshed formula for all \(k\ge0\). Both statements include zero coordinates, arbitrary deterministic starts, and \(k=0\).

For \(0<\alpha<2\) and \(0<t<1\), the gains \(\alpha\) and \(\alpha t\) lie strictly between \(0\) and \(2\), hence their \(Q\)-values are less than \(1\). The remaining value obeys \(Q(\alpha/t)<1\) exactly when \(\alpha/t<2\), or \(t>\alpha/2\), equivalently \(\rho>\alpha/(2-\alpha)\). At equality \(Q(\alpha/t)=1\), with mixture weight \(1/4\); below, its value exceeds \(1\) and its nonzero weight forces divergence.

At \(\alpha=1/2\), set \(s=t+t^{-1}\ge2\). Algebra gives
\[
M=\frac{s^2-4s+24}{32},\qquad M<1\iff s<2+2\sqrt3.
\]
Since \(t\in(0,1)\), the function \(t+t^{-1}\) is strictly decreasing. Its unique threshold is \(t_\star=1+\sqrt3-\sqrt{3+2\sqrt3}\), yielding \(\rho_\star=t_\star/(1-t_\star)\) as stated. The equality and divergent cases follow from the exact geometric expression. At \(\rho=1/4\), \(t=1/5\) and \(Q(1/2)=5/8\), \(Q(1/10)=181/200\), \(Q(5/2)=13/8\), giving \(M=189/200\). For each fixed environment the conditional mean factor of the selected coordinate is \(1-g_j/2\); all three possible gains \(1/2,1/10,5/2\) lie in \((0,4)\), so the conditional mean iterate converges even for the cached process at this witness.

## Verification
The standalone standard-library-only file `VERIFY.py` independently enumerates all \(2^3\) choices of curvature sample, spectral-step sample, and stochastic-gradient sample. It computes per-step squared multipliers without substituting the theorem's mixture formulas, then compares exact rational powers for seven positive regularizations, five positive scales, two coordinates, and eleven horizons. It reports `PASS` for 1575 exact equalities/inequalities plus exact rational witness and polynomial checks. The algebraic argument above, not the finite enumeration, proves the claim for all eligible real parameters and all horizons.

## Relationship to prior work
Frangella, Rathore, Zhao, and Udell introduce the independent fresh Hessian minibatch in their spectral step (3), the practical update in Algorithm 1, and the recommendation to reuse a curvature preconditioner for constant-Hessian objectives. Their Section 4 convergence theorems analyze a different fixed-step stage-averaging version, not the present small-minibatch ideal spectral-step iteration. The results here do not contradict those theorems or assert instability for the full finite-precision default implementation. Vaswani and collaborators analyze regularized subsampled Newton under interpolation with a different conservatively parameterized stepsize. Lacotte and Pilanci analyze fixed and refreshed data-oblivious sketches in full-gradient iterative Hessian sketch; their inverse-moment identity assumes a step independent of the current embedding and does not include separately sampled curvature-based steps or stochastic gradient minibatches. None of these inspected statements implies the stated four-environment law or both sharp cutoffs.

## Limitations
The exact result concerns two features and two examples, batch size one, ideal rank-one reconstruction, and an exact spectral eigenvalue. It is a precise boundary for this natural scheme, not a guarantee or failure theorem for larger datasets, finite randomized-power estimates, finite-precision spectral regularization, or the source's default larger rank. Generic finite-variance preconditioned SGD results may give broad sufficient bounds without determining these exact cutoffs. Originality comparisons have residual risk from unindexed equivalent derivations, and independent audit has not been performed.

## References
1. Z. Frangella, P. Rathore, S. Zhao, and M. Udell, *SketchySGD: Reliable Stochastic Optimization via Randomized Curvature Estimates*, arXiv:2211.08597 (first public 2022-11-16), especially Algorithms 1–4, equation (3), Section 4, and Appendix A. https://arxiv.org/html/2211.08597v5
2. S. Y. Meng, S. Vaswani, I. Laradji, M. Schmidt, and S. Lacoste-Julien, *Fast and Furious Convergence: Stochastic Second Order Methods under Interpolation*, arXiv:1910.04920, Section 3. https://arxiv.org/html/1910.04920v2
3. J. Lacotte and M. Pilanci, *Faster Least Squares Optimization*, arXiv:1911.02675 (first public 2019-11-06), Sections 1, 3, 4, and Theorem 4.1. https://arxiv.org/pdf/1911.02675
