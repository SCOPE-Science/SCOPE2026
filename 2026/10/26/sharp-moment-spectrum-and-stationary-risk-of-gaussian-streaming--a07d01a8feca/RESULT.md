# Sharp moment spectrum and stationary risk of Gaussian streaming Kaczmarz

## Finding

**Theorem (sharp moment spectrum, stationary law, and risk).** Let \(m,d\ge1\) be integers, let \(\alpha\ge0\), and let \(\sigma,\tau>0\). At each iteration independently redraw \(m\) coefficient rows \(A_i\sim N(0,\sigma^2 I_d)\) and \(m\) scalar measurements \(B_i\sim N(0,\tau^2)\), with all rows and measurements mutually independent. Select \(I=i\) conditionally on the rows with probability proportional to \(\|A_i\|^\alpha\). Project the current iterate onto the selected, independently remeasured affine hyperplane:
\[
X_{k+1}=X_k+\frac{B_I-A_I^{\mathsf T}X_k}{\|A_I\|^2}A_I.
\]
For every deterministic initial \(X_0\in\mathbb R^d\), set
\[
p_*=\min\{d+\alpha,md\}.
\]
Then for **every real** \(p>0\) and **every integer** \(k\ge1\),
\[
\mathbb E\|X_k\|^p<\infty\quad\Longleftrightarrow\quad p<p_*.
\]
The Markov chain has exactly one invariant probability distribution \(\pi\), and its moments obey the identical sharp classification
\[
\int\|x\|^p\,\pi(dx)<\infty\quad\Longleftrightarrow\quad 0<p<p_*.
\]
In particular, for \(\alpha=2\) (squared-row-norm sampling) and \(0\le p<\min\{d+2,md\}\), the selected row radius has the exact inverse-moment formula
\[
\mathbb E\|A_I\|^{-p}=
\frac{2^{-p/2}}{\sigma^p}\frac{md}{md-p}
\frac{\Gamma((d+2-p)/2)}{\Gamma((d+2)/2)}.
\]
For \(\alpha=2\) and \(md>2\), the exact mean-square trajectory and stationary risk are
\[
\mathbb E\|X_k\|^2=\left(1-\frac1d\right)^k\|X_0\|^2+
\frac{dm\tau^2}{\sigma^2(md-2)}\left[1-\left(1-\frac1d\right)^k\right],
\qquad \int\|x\|^2\,\pi(dx)=\frac{dm\tau^2}{\sigma^2(md-2)}.
\]
When \(md\le2\), these mean squares are infinite for all \(k\ge1\), and the stationary second moment is infinite. More generally, finite mean-square risk occurs precisely when **both** \(d+\alpha>2\) and \(md>2\).

## Assumptions and scope

All random draws are renewed independently at **every** iteration; neither coefficient rows nor noisy right-hand sides are reused across iterations. The projected affine hyperplanes need not have a common solution. The coefficient-noise and measurement-noise distributions are isotropic and independent as specified. The selection probability uses the \(m\) newly observed **un-normalized coefficient-row norms**, not current residuals. For \(\alpha=0\), selection is uniform; for \(m=1\), it is deterministic. Zero Gaussian rows have probability zero. The law in the theorem holds without restricting the ratio \(\tau/\sigma\). No deterministic underlying matrix or static linear system is assumed.

## Proof

**1. Selection separates radius from direction.** Put \(R_i=\|A_i\|\) and \(U_i=A_i/R_i\). Gaussian rotational invariance makes the \(U_i\) independent uniform directions on \(S^{d-1}\), independent of every \(R_j\) and \(B_j\). Because the selection weights depend solely on radii, \(U_I\) remains uniform and independent of \(R_I\); also \(B_I\) is centered Gaussian of variance \(\tau^2\), independent of the selected radius and direction. The update is
\[
X_{k+1}=(I_d-U_IU_I^{\mathsf T})X_k+(B_I/R_I)U_I.
\]
The two terms are orthogonal. In particular,
\[
\|X_{k+1}\|^2=\|(I_d-U_IU_I^{\mathsf T})X_k\|^2+B_I^2/R_I^2.
\tag{1}
\]

**2. Exact selected-radius integrability threshold.** For \(m=1\), the selected radius is a \(d\)-dimensional chi radius and has finite inverse \(p\)-moment exactly for \(p<d\). Suppose \(m\ge2\). By exchangeability,
\[
\mathbb E R_I^{-p}=m\,\mathbb E\frac{R_1^{\alpha-p}}{\sum_{j=1}^m R_j^\alpha}.
\tag{2}
\]
Each radius has a continuous density bounded above and below by positive constants times \(r^{d-1}\) on \((0,1)\), and exponentially decreasing tails. Let \(T=\max_{2\le j\le m}R_j\). On \((0,1)\), its density is comparable to \(t^{d(m-1)-1}\). For all nonnegative \(\alpha\), the denominator of (2) is comparable, by positive constants depending only on \(m,\alpha\), to \(\max\{R_1,T\}^\alpha\). Restricting first to both variables below one, the contribution with \(r\le t\) is comparable to
\[
\int_0^1t^{d(m-1)-1-\alpha}
\left(\int_0^t r^{d+\alpha-p-1}\,dr\right)dt,
\tag{3}
\]
and the contribution with \(t\le r\) is comparable to
\[
\int_0^1r^{d-p-1}
\left(\int_0^r t^{d(m-1)-1}\,dt\right)dr.
\tag{4}
\]
The first is finite exactly when **both** \(p<d+\alpha\) and \(p<md\); the second exactly when \(p<md\). The remaining regions, where at least one variable exceeds one, have exponentially integrable upper tails and introduce no stricter conditions; in the case \(r\downarrow0\), \(t>1\), the same necessary condition \(p<d+\alpha\) applies. Divergence at either threshold follows from the positive lower-density bounds in these integrals, including logarithmic boundary divergence. Thus
\[
\mathbb E R_I^{-p}<\infty\quad\Longleftrightarrow\quad p<\min\{d+\alpha,md\}.
\tag{5}
\]
As \(B_I\) is a nondegenerate independent Gaussian, \(\mathbb E|B_I/R_I|^p\) has precisely the same threshold.

**3. Every positive finite iteration.** Orthogonality (1) implies \(\|X_{k+1}\|\ge |B_I|/R_I\). Hence all \(p\ge p_*\) moments are infinite, even if the previous iterate is deterministic and finite. Conversely, \(\|X_{k+1}\|\le\|X_k\|+|B_I|/R_I\). For \(0<p\le1\), apply \((a+b)^p\le a^p+b^p\); for \(p>1\), use \((a+b)^p\le2^{p-1}(a^p+b^p)\). Equation (5) then proves finiteness inductively for every finite \(k\) and every \(p<p_*\).

**4. Unique stationary law and its moments.** In dimension \(d=1\), each projection factor vanishes and \(X_{k+1}=B_IU_I/R_I\) is an independent fresh draw: its law is the unique invariant distribution and (5) proves its spectrum. In dimensions \(d\ge2\), write \(Q_k=I_d-U_kU_k^{\mathsf T}\) and \(Z_k=(B_k/R_k)U_k\). Every pair \((Q_k,Z_k)\) is independently redrawn. For every fixed \(v\), rotational invariance gives, for \(p>0\),
\[
\mathbb E\|Q_kv\|^p=q_p\|v\|^p,
\quad q_p=\mathbb E(1-U_{k,1}^2)^{p/2}<1;
\qquad q_2=1-\frac1d.
\tag{6}
\]
Since \(p_*\ge2\), the random translation has finite first moment. The backward affine series of independent past updates converges absolutely in mean norm by the bound \(\mathbb E\|Q_0\cdots Q_{-j+1}Z_{-j}\|\le q_1^j\mathbb E\|Z\|\). Its limit defines an invariant probability distribution. For any \(0<p<p_*\), the same estimate in \(L^p\) (Minkowski if \(p\ge1\), subadditivity if \(p\le1\)) proves that its \(p\)-moment is finite. Two trajectories driven by the same fresh noise contract: \(\mathbb E\|X_k-Y_k\|^2=q_2^k\|X_0-Y_0\|^2\) for deterministic starts. For arbitrary two invariant distributions, couple independently drawn initial states and apply bounded convergence to the almost-surely vanishing synchronized difference (the preceding conditional mean-square identity plus truncation of random initial differences suffices). This makes the invariant distribution unique. Finally, orthogonality (1) under invariance rules out finite \(p\)-moments for every \(p\ge p_*\).

**5. Exact squared-norm sampling moments and risk.** Under \(\alpha=2\), write \(V_i=R_i^2/\sigma^2\), with iid chi-square laws of \(d\) degrees of freedom. Their sum \(S\) is chi-square of \(md\) degrees of freedom. The proportions \(V_i/S\) are independent of \(S\) and have Dirichlet parameters \((d/2,\dots,d/2)\). Selecting index \(i\) with probability \(V_i/S\) size-biases its proportion; therefore \(W=V_I/S\) has beta law with parameters \(d/2+1\) and \((m-1)d/2\), independent of \(S\) (for \(m=1\), \(W=1\)). Gamma negative-moment formulas for \(R_I=\sigma\sqrt{SW}\) yield the displayed Mellin expression. At \(p=2\), this reduces to \(\mathbb E R_I^{-2}=m/[\sigma^2(md-2)]\). Taking expectation in (1), invoking (6) and \(\mathbb E B_I^2=\tau^2\), gives the scalar linear recursion
\[
\mathbb E\|X_{k+1}\|^2=(1-1/d)\mathbb E\|X_k\|^2+
\frac{m\tau^2}{\sigma^2(md-2)},
\]
whose solution is the stated exact finite-time and stationary risk. When \(md\le2\), (1) and (5) force infinite risk already after the first step. For arbitrary \(\alpha\), (5) at \(p=2\) gives the final if-and-only-if variance criterion.

## Verification

The companion standalone `verify.py` uses exact rational arithmetic for conditional squared-norm sampling identities, evaluates the closed-form negative Mellin moment against independent beta/gamma calculations, and compares independent Monte Carlo samples and repeated random row-projection iterations against the analytic mean-square trajectory. It completes 70 deterministic diagnostic assertions with a fixed random seed. The finite tests are cross-checks only; all general-dimension and all-real-moment statements are proved above using integral comparisons, projection orthogonality, and contractive affine recursions. Run `python verify.py` with NumPy and SciPy installed.

## Relationship to prior work

Gan and Wu (2026, arXiv:2608.22259, first submitted 2026-08-23) investigate randomized Kaczmarz-type methods for **fixed, doubly noisy** coefficient matrices and measurements, with stochasticity in the solver selection. Their theorems do not address completely fresh independent Gaussian matrix and right-hand-side draws at each step, the size-bias parameter \(\alpha\), sharp all-order moment existence, or the stationary law of the remeasured affine projection chain. Gower and Richtárik (2015) develop general randomized sketch-and-project convergence for fixed consistent data, and Zhang et al. (2023) study sparse Kaczmarz with residual-dependent selection and a fixed matrix. Zhang, Zeng and Zhang (2026) study repeated observations with signal averaging but a fixed underlying linear system and residual-dependent row selection, without an all-order stationary integrability law for independently remeasured affine hyperplanes. Needell (2010) studies fixed noisy measurements. De Sa et al. (2026) study power-law spectra with randomized homogeneous projection-gradient updates, not additive Gaussian offsets divided by fresh row radii. These distinct hypotheses prevent direct implication of the present statement. Related mathematical literature may still contain a specialized equivalent formulation; no claim of absolute historical priority is made.

## Limitations

The Gaussian isotropy, fresh independent redraws, independent nondegenerate measurement noise, and norm-power selection are essential to this particular exact formula. No analogous exact frontier is asserted for cached noisy rows, correlated measurements, non-Gaussian coefficient distributions, nonisotropic covariances, or selection by residual magnitude. The Gaussian scale assumptions exclude noiseless right-hand sides. The closed-form Mellin and mean-square constants apply to \(\alpha=2\), whereas the moment existence threshold applies to all \(\alpha\ge0\). The assertion of an invariant law is mathematical and does not imply finite mean-square risk beyond the stated frontier. Historical priority is subject to independent literature examination.

## References

1. Gan and Wu, *On Convergence Behavior of Randomized Kaczmarz-type Methods for Solving Doubly Noisy Linear Systems*, arXiv:2608.22259 (first public 2026-08-23), https://arxiv.org/abs/2608.22259.
2. Gower and Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (2015), https://arxiv.org/abs/1506.03296.
3. L. Zhang, Z. Yuan, H. Wang and H. Zhang, *A Weighted Randomized Sparse Kaczmarz Method for Solving Linear Systems*, arXiv:2306.06813 (2023), https://arxiv.org/abs/2306.06813.
4. Needell, *Randomized Kaczmarz Solver for Noisy Linear Systems*, arXiv:0902.0958 (2009), https://arxiv.org/abs/0902.0958.
5. De Sa, Ahle, Bulatov and Ré, *Stochastic Optimization Under Power-Law Spectra: Tight Bounds and Shuffling Analysis*, arXiv:2609.36271 (2026), https://arxiv.org/abs/2609.36271.
6. L. Zhang, J. Zeng and H. Zhang, *Relaxed Greedy Randomized Kaczmarz with Signal Averaging for Solving Doubly-Noisy Linear Systems*, arXiv:2603.29372 (2026), https://arxiv.org/abs/2603.29372.
