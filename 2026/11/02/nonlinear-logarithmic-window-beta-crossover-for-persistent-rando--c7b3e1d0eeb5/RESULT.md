# Nonlinear logarithmic-window Beta crossover for persistent random walks

## Finding

Fix \(c>0\) and a deterministic real sequence \(\beta_N\to\beta\in\mathbb R\). For each sufficiently large integer \(N\), take a fair initial sign and independent direction reversals with probability \(p_{N,k}=\min\{1,c k^{-\alpha_N}\}\), where \(\alpha_N=1+\beta_N/\log N\). If \(S_N\) is the resulting signed-step walk and \(X_N(t)\) its linearly interpolated trajectory divided by \(N\), then, for every \(T>0\),
\[
X_N\Longrightarrow Y_\lambda \quad\text{in } C([0,T]),\qquad \lambda=c e^{-\beta}.
\]
Here \(Y_\lambda(t)=\int_0^t E_\lambda(s)\,ds\), with \(E_\lambda\) a symmetric sign process whose reversals form a Poisson point process on \((0,\infty)\) with intensity \(\lambda\,ds/s\). Consequently, for each \(t>0\),
\[
\frac12\left(1+\frac{Y_\lambda(t)}t\right)\sim\operatorname{Beta}(\lambda,\lambda).
\]
In particular the normalized mean square displacement and Binder cumulant have the **nonlinear** crossover profiles
\[
\lim_{N\to\infty}\frac{\mathbb E[S_N(N)^2]}{N^2}=\frac1{1+2c e^{-\beta}},\qquad
\lim_{N\to\infty}\left(1-\frac{\mathbb E[S_N(N)^4]}{3(\mathbb E[S_N(N)^2])^2}\right)=\frac2{3+2c e^{-\beta}}.
\]
For \(0<s\le t\), the limiting two-time covariance is
\[
\operatorname{Cov}(Y_\lambda(s),Y_\lambda(t))=
\begin{cases}
\displaystyle\frac{s^2}{1+2\lambda}+\frac{s^{2\lambda+1}(t^{1-2\lambda}-s^{1-2\lambda})}{(1+2\lambda)(1-2\lambda)}, &\lambda\ne\tfrac12,\\
\displaystyle\frac{s^2}{2}\left(1+\log\frac ts\right),&\lambda=\tfrac12.
\end{cases}
\]
Thus \(\lambda=1/2\) is a logarithmic resonance in the covariance formula, while the one-time marginal law remains smoothly parametrized by \(\lambda\).

## Assumptions and scope

For each \(N\ge3\), define \(\alpha_N=1+\beta_N/\log N\). Only sufficiently large \(N\) are relevant, so \(\alpha_N>0\). Let \(V_{N,1}\) be equally likely to be \(1\) or \(-1\), independent of the complete family of independent Bernoulli random variables \(F_{N,k}\) with \(\mathbb P(F_{N,k}=1)=p_{N,k}\) for \(k\ge2\). Set \(V_{N,k}=V_{N,k-1}(-1)^{F_{N,k}}\) and \(S_N(m)=\sum_{k=1}^m V_{N,k}\), with \(S_N(0)=0\). Define the continuous process by linear interpolation of \(X_N(m/N)=S_N(m)/N\). The same infinite sequence of flips is defined separately for each row \(N\), so convergence is of laws and makes no coupling claim across rows.

The limiting Poisson process has infinitely many points accumulating at zero but finitely many points on every compact subinterval of \((0,\infty)\). Give the sign at time \(1\) the symmetric law, independently of the Poisson process, and extend the sign by reversal across its points. Its path is locally piecewise constant on \((0,\infty)\), and the Lebesgue integral defining \(Y_\lambda\) exists. The process \(Y_\lambda\) is continuous, starts at zero, and is \(1\)-Lipschitz. These claims concern fixed \(c>0\) and finite \(\beta\), not a uniform theorem when \(\beta_N\) diverges.

## Proof

**1. Exact triangular-array reversal limit.** Fix \(0<\delta<T\). Uniformly over integers \(k\) satisfying \(\delta N\le k\le TN\), the power law and \(\beta_N\to\beta\) give
\[
N p_{N,k}=c\,e^{-\beta_N}(k/N)^{-\alpha_N}\longrightarrow\frac\lambda{k/N}
\]
in the sense that the difference between the two sides, maximized over this interval, tends to zero. The truncation by \(1\) is inactive here for large \(N\). In particular \(\max p_{N,k}=O(N^{-1})\), and \(\sum_{\delta N\le k\le TN}p_{N,k}^2=O(N^{-1})\). For a continuous nonnegative compactly supported test function \(f\) on \((\delta,T)\), the independence identity
\[
\mathbb E\exp\!\left(-\sum_k f(k/N)F_{N,k}\right)
=\prod_k\left[1+p_{N,k}(e^{-f(k/N)}-1)\right]
\]
therefore tends, after taking logarithms and a Riemann sum, to
\[
\exp\!\left(\int_\delta^T\frac\lambda t(e^{-f(t)}-1)\,dt\right).
\]
This is the Laplace functional of a Poisson point process of intensity \(\lambda\,dt/t\) on \((\delta,T)\), and proves convergence of the independent-turn point process on every compact interval away from zero.

**2. Fair sign and functional convergence.** For any deterministic index \(j\), the variable \(V_{N,j}\) is a product of the fair initial sign and a function of the reversals up to \(j\). Consequently it is exactly fair and independent of the later reversals. On \([\delta,T]\), the reversal-point convergence and this independent fair sign give \(J_1\)-convergence of the sign trajectories to \(E_\lambda\) restricted to \([\delta,T]\). The Poisson limit has no endpoint points almost surely and only finitely many jumps on this interval. Hence the integral of the sign path is a continuous functional into \(C([\delta,T])\) at the limiting paths. For every \(t\le\delta\), both the normalized walk and the limiting integral have absolute value at most \(\delta+N^{-1}\); their initial contributions to the values at later times are likewise bounded by \(\delta+N^{-1}\). The uniform \(1\)-Lipschitz bound and the converging-together argument, first \(N\to\infty\) and then \(\delta\downarrow0\), establish the claimed convergence in \(C([0,T])\). They also establish consistency for every finite \(T\).

**3. The exact Beta marginal.** Write \(u=\log t\), \(H(u)=E_\lambda(e^u)\), and \(U(u)=e^{-u}Y_\lambda(e^u)\). The transformed Poisson process has constant intensity \(\lambda\,du\); hence \(H\) is a two-sided stationary fair-sign Markov chain, flipping at rate \(\lambda\). Scaling invariance makes \(U\) stationary. It solves the pathwise equation \(\dot U=-U+H\) between flips and takes values in \([-1,1]\). The joint Markov generator is
\[
\mathcal L f(x,h)=(-x+h)\partial_x f(x,h)+\lambda[f(x,-h)-f(x,h)].
\]
Let \(a_m=\mathbb E[U^m]\), \(b_m=\mathbb E[U^mH]\). Applying stationarity to \(x^m\) and \(x^m h\) yields, for \(m\ge1\),
\[
a_m=b_{m-1},\qquad b_m=\frac{m}{m+2\lambda}a_{m-1}.
\]
Since \(a_0=1\) and \(a_1=b_0=0\), the odd moments vanish and
\[
a_{2j}=\prod_{r=0}^{j-1}\frac{2r+1}{2r+1+2\lambda}.
\]
These are exactly the moments of \(2B-1\) for \(B\sim\operatorname{Beta}(\lambda,\lambda)\). Uniqueness of the moment problem on the compact interval \([-1,1]\) establishes the law. Self-similarity gives the same law for \(Y_\lambda(t)/t\) at every \(t>0\). The second and fourth moments are therefore
\[
\mathbb E[Y_\lambda(t)^2]=\frac{t^2}{1+2\lambda},\qquad
\mathbb E[Y_\lambda(t)^4]=\frac{3t^4}{(1+2\lambda)(3+2\lambda)}.
\]
Every \(X_N(t)\) is bounded in absolute value by \(t+N^{-1}\); uniform integrability transfers these moments through weak convergence. Substitution gives the Binder formula.

**4. The two-time covariance.** The number of reversals between positive times \(u<v\) is Poisson with mean \(\lambda\log(v/u)\), independent of the preceding sign. Thus
\[
\mathbb E[E_\lambda(u)E_\lambda(v)]
=\exp(-2\lambda\log(v/u))=(u/v)^{2\lambda}.
\]
The sign is centered; boundedness permits Fubini. For \(0<s\le t\),
\[
\frac{\partial}{\partial t}\mathbb E[Y_\lambda(s)Y_\lambda(t)]
=\int_0^s (u/t)^{2\lambda}\,du
=\frac{s^{2\lambda+1}}{(1+2\lambda)t^{2\lambda}}.
\]
Integrating from \(s\) to \(t\), with the already established diagonal value \(s^2/(1+2\lambda)\), gives the displayed power formula and its logarithmic value when \(\lambda=1/2\).

## Verification

The supplementary standalone script `checks/moment_checker.py` compares an exact Markov-moment recurrence against independently enumerated finite walk distributions at exponent \(1\) and tests the stationary Beta moment recurrence with exact rational arithmetic. It also computes the exact finite-discrete moment recurrences numerically for three fixed values of \(\beta\) and increasing horizons. The script reports 131 passing finite assertions. Its recorded stdout is in `checks/moment_checker_output.txt`. The finite computations test identities and qualitative finite-size approach, not the point-process or functional weak limit. The latter is established by the analytical arguments above.

The fourth-moment recurrence used by the script, with \(m_r=\mathbb E[S^r]\), \(u_r=\mathbb E[S^rV]\), and \(g_k=1-2p_{N,k}\), is
\[
\begin{aligned}
m'_2&=m_2+2g_k u_1+1,& u'_1&=g_k u_1+1,\\
m'_4&=m_4+4g_k u_3+6m_2+4g_k u_1+1,&
u'_3&=g_k u_3+3m_2+3g_k u_1+1.
\end{aligned}
\]
Here primed quantities are evaluated after step \(k\). These equations follow by expanding \((S+V')^r\) and using \(\mathbb E[V'\mid S,V]=g_kV\), \((V')^2=1\).

## Relationship to prior work

Pradhan, Roy and Ray (2026) study this power-law reversal model, identify the dynamical transition at exponent \(1\), and establish the relevance of the logarithmic scaling combination \((\alpha-1)\log N\). Their fluctuation analysis (equations (28)–(32) and supplementary section SVI) uses an expansion first-order in \(\alpha-1\). That expansion does not by itself give a controlled full limiting law when \((\alpha-1)\log N\to\beta\) at finite nonzero \(\beta\). This result retains the full exponential dependence on \(\beta\), gives the complete functional limit, and deduces an exact nonlinear Binder crossover.

Engländer and Volkov (2016/2018) already identified the fixed-critical \(c/k\) Beta law; Engländer, Volkov and Wang (2019/2020), Theorem 4(3), developed its Poisson zigzag **functional** limit and Remark 15 included more general single fixed sequences with \(k p_k\to c\). These known results are indispensable ingredients, not claimed as novel here. They do not state the observation-horizon-dependent triangular-array critical window \(\alpha_N=1+\beta_N/\log N\). The present proof explicitly handles its local intensity and provides the nonlinear physical scaling curves. A 2026 study of reinforced processes under critical Markov switching also derives Beta stationary laws for exponential telegraph relaxation, but in a different model with a fixed critical switching parameter, not the varying-exponent window studied here.

The additional two-time covariance is an explicit consequence of the established Poisson zigzag correlation, not an independent new universality claim. The asserted contribution is the **joined triangular-window limit and its nonlinear distributional/observable profile**. Classical Poisson and Beta facts alone, without proving the triangular scaling, do not determine the observational finite-size crossover.

## Limitations

The result assumes independent flips, a fair initial direction, fixed \(c>0\), and a convergent *finite* parameter \(\beta_N\). It does not give a convergence rate, uniform estimates for unbounded \(\beta_N\), or multidimensional or interacting-walk analogues. The Beta distribution and its critical zigzag origin are established in prior literature. The exponent-window result could be subsumed by a broader triangular-array point-process invariance principle not located in the inspected sources; independent historical-priority assessment remains necessary. Finite checking is not a substitute for the analytic weak-convergence proof.

## References

1. A. Pradhan, R. Roy and P. Ray, *Diffusive-to-Ballistic transition in a Persistent Random Walk*, arXiv:2605.20116v1 (first public 2026-05-19), especially equations (28)–(32) and supplementary SVI. https://arxiv.org/html/2605.20116
2. J. Engländer, S. Volkov and Z. Wang, *The coin-turning walk and its scaling limit*, arXiv:1904.10953v1 (first public 2019-04-24), especially Theorem 4, Remark 11, Remark 15 and §6.10. https://arxiv.org/abs/1904.10953
3. J. Engländer and S. Volkov, *Turning a Coin over Instead of Tossing It*, arXiv:1606.03281v1 (2016); *Journal of Theoretical Probability* 31 (2018), 1097–1118. https://arxiv.org/abs/1606.03281
4. *Exact random centering and hybrid fluctuation limits for interacting reinforced processes under critical Markov switching*, arXiv:2610.02609v1 (2026), especially Proposition 3.5 and Remark 3.7. https://arxiv.org/html/2610.02609v1
