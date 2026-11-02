# A three-objective conflict for Bernoulli-erased heavy-ball optimization

## Finding

Consider raw Polyak heavy-ball optimization of \(f(x)=x^2/2\), with an independently missing gradient at each iteration. Write \(B_n\sim\operatorname{Bernoulli}(p)\), independently, with \(0<p<1\). The unbiased gradient observation is \(B_nX_n/p\). For constant step \(\gamma>0\), momentum \(0\le\beta<1\), and deterministic initial state \((X_{-1},X_0)\), the recursion is
\[
 X_{n+1}=(1+\beta-\gamma B_n/p)X_n-\beta X_{n-1}.
\]
Set \(q=1-p\) and
\[
 D=2\gamma(1-\beta)-\gamma^2\left(\frac{1-\beta}{1+\beta}+\frac qp\right),
 \qquad \Gamma_p(\beta)=\frac{2p(1-\beta^2)}{1+\beta-2p\beta}.
\]
The following **joint, exact three-objective classification** holds.

**(i) Stability capacity.** The homogeneous recursion converges geometrically to zero in mean square for every deterministic initial state if and only if \(D>0\), equivalently \(0<\gamma<\Gamma_p(\beta)\). The largest admissible step threshold optimized over momentum is
\[
 \sup_{0\le\beta<1}\Gamma_p(\beta)=
 \begin{cases}2p,&0<p\le1/2,\\
 \displaystyle\frac{4p}{1+2\sqrt{p(1-p)}},&1/2<p<1.
 \end{cases}
\]
The maximizing momentum is uniquely \(\beta=0\) in the first regime and uniquely
\[
 \beta_{\mathrm{capacity}}=\frac{\sqrt p-\sqrt q}{\sqrt p+\sqrt q}
\]
in the second. In particular, momentum strictly increases the maximum stable step if and only if \(p>1/2\).

**(ii) Persistent-noise floor.** Add to each update an independent, centered scalar \(\eta_n\), independent of all erasures and past states, with \(\mathbb E\eta_n^2=\sigma^2>0\). For every stable pair \((\beta,\gamma)\), the limiting stationary squared error is exactly \(\sigma^2/D\). For each fixed \(0<\gamma<\sup_\beta\Gamma_p(\beta)\), the unique momentum minimizing this error over stable choices is
\[
 \beta_{\mathrm{noise}}(\gamma)=\begin{cases}
 0,&0<\gamma\le1,\\
 \sqrt\gamma-1,&1<\gamma<\sup_\beta\Gamma_p(\beta).
 \end{cases}
\]
The second regime is possible only when \(p>1/2\). The additive-noise variance is measured in the **update**, not in the raw gradient oracle.

**(iii) Every finite horizon.** For the standard zero-velocity initialization \(X_{-1}=X_0\ne0\), and with \(\eta_n\equiv0\), every constant-step heavy-ball choice satisfies, for all integers \(n\ge1\),
\[
 \mathbb E X_n^2\ge q^nX_0^2.
\]
Equality holds simultaneously at every horizon for \(\beta=0,\gamma=p\). At each fixed horizon \(n\ge2\), this pair is the **unique** achieving choice among \(0\le\beta<1,\gamma>0\). Thus, even where nonzero momentum enlarges the stability-capacity interval or reduces the persistent-noise floor at a fixed step, it cannot improve the optimal mean-square error at **any** finite horizon from zero initial velocity.

For example, at \(p=4/5\), the maximum step threshold increases from \(8/5\) to \(16/9\) with \(\beta_{\mathrm{capacity}}=1/3\). At the larger fixed step \(\gamma=17/10\), zero momentum has \(D=-17/80\) and is unstable, while \(\beta=1/3\) gives \(D=119/1200>0\) and is mean-square stable. At fixed \(\gamma=25/16\), stationary error is minimized at \(\beta=1/4\), with \(D=275/1024\); zero momentum instead gives \(D=75/1024\). Yet the unique optimal finite-horizon scheme is \((\beta,\gamma)=(0,4/5)\), with squared error \(5^{-n}X_0^2\).

## Assumptions and scope

All random variables \(B_n\) are iid; each \(B_n\) is independent of \((X_{n-1},X_n)\) formed before that update. The method uses unnormalized/raw Polyak momentum \(\beta(X_n-X_{n-1})\), not exponentially weighted-average momentum. The Bernoulli oracle returns the **unbiased, rescaled** gradient \(B_nX_n/p\); this normalization matters. The stability condition is convergence of \(\mathbb E(X_n^2+X_{n-1}^2)\) for every deterministic initial state. In part (ii), \(\eta_n\) is also iid with finite positive variance and independent of the erasures. All statements use exact real arithmetic, scalar quadratic curvature one, and constant parameters, with the listed strict parameter boundaries. The supremum of admissible steps is a stability **ceiling** and is not itself stable.

## Proof

Write \(a=1+\beta-\gamma\), \(v=\gamma^2q/p\), and \(a_n=1+\beta-\gamma B_n/p\). Then \(\mathbb E a_n=a\) and \(\operatorname{Var}(a_n)=v\). The exact transfer on the three moments \((\mathbb E X_n^2,\mathbb E X_nX_{n-1},\mathbb E X_{n-1}^2)\) is
\[
 M=\begin{pmatrix}a^2+v&-2a\beta&\beta^2\\a&-\beta&0\\1&0&0\end{pmatrix}.
\]
For \(0<\beta<1\), define \(A_n=\left(\begin{smallmatrix}a_n&-\beta\\1&0\end{smallmatrix}\right)\) and
\[
 P=\begin{pmatrix}
 1&-\beta a/(1+\beta)\\
 -\beta a/(1+\beta)&\beta^2
 \end{pmatrix}.
\]
Direct multiplication gives the **exact conditional energy identity**
\[
 \mathbb E(A_n^{\mathsf T}PA_n)-P=-D\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]
where \(\det P=\beta^2\gamma[2(1+\beta)-\gamma]/(1+\beta)^2\). If \(D\ge0\), then \(\gamma\le\Gamma_p(\beta)<2(1+\beta)\), so \(P\) is positive definite. If \(D>0\), expected \(P\)-energy strictly dissipates by \(D\mathbb E X_n^2\). Moreover the two-step observability form
\[
 (x,y)\mapsto x^2+\mathbb E[(a_nx-\beta y)^2]
\]
is positive definite for \(\beta>0\). Hence in every block of two steps the energy decreases by a fixed strictly positive proportion, proving geometric mean-square stability. At \(D=0\), the positive-definite expected \(P\)-energy is conserved and geometric mean-square decay is impossible. For \(\beta=0\), the exact scalar amplification is \(\mathbb E a_n^2=1-D\), giving stability if and only if \(D>0\).

To exclude \(D<0\), suppose contrary to the claim that every deterministic homogeneous initial state were mean-square stable. This would force \(\rho(M)<1\): the positive-semidefinite rank-one covariance matrices generated by deterministic initial vectors span the three-dimensional real symmetric covariance space, and all their iterates would decay. With independent additive variance-one innovations, the resulting forced covariance recursion would therefore have a finite stationary positive-semidefinite solution. At stationarity, let \(m=\mathbb E X_n^2=\mathbb E X_{n-1}^2\), \(r=\mathbb E X_nX_{n-1}\). The cross-moment equation gives \(r=am/(1+\beta)\), and the variance equation gives \(Dm=1\), impossible for \(D<0\). The same argument covers any \(D\le0\) once nondecay at zero is included. Thus \(D>0\) is necessary and sufficient. The same stationarity equations with innovation variance \(\sigma^2\) prove part (ii)'s value \(m=\sigma^2/D\).

Solving \(D>0\) for \(\gamma\) gives \(\Gamma_p(\beta)\). Its derivative has the sign of \((2p-1)(1+\beta^2)-2\beta\), divided by a strictly positive factor. For \(p\le1/2\), the sign is negative for all \(\beta>0\); for \(p>1/2\) there is exactly one root in \((0,1)\), namely \(\beta_{\mathrm{capacity}}\) above. Substitution yields the displayed sharp ceiling. At fixed \(\gamma\), differentiating \(D\) gives
\[
 \frac{\partial D}{\partial\beta}=-2\gamma+\frac{2\gamma^2}{(1+\beta)^2},\qquad
 \frac{\partial^2D}{\partial\beta^2}=-\frac{4\gamma^2}{(1+\beta)^3}<0.
\]
Thus its unique maximizer on \([0,1)\) is \(0\) for \(\gamma\le1\), or \(\sqrt\gamma-1\) for \(\gamma>1\). Its maximum is positive whenever \(\gamma\) is below the global stability ceiling; consequently this maximizer is itself stable and uniquely minimizes \(\sigma^2/D\).

For the finite-horizon result, the event \(B_0=\cdots=B_{n-1}=0\) has probability \(q^n\), and on that event the zero-velocity initialization makes every iterate equal to \(X_0\), regardless of \((\beta,\gamma)\). Nonnegativity of squared errors on all other sample paths yields the lower bound. For \((\beta,\gamma)=(0,p)\), the first observed gradient sends \(X\) to zero permanently, so equality holds. If \(n\ge2\) and another parameter pair attained equality, every positive-probability sample path with at least one observed gradient would have to end at zero. The path of \(n-1\) erasures followed by one observation forces \(\gamma=p\). The path of \(n-2\) erasures followed by one observation and one erasure then ends at \(-\beta X_0\), forcing \(\beta=0\). This proves uniqueness, including all boundaries.

## Verification

Run `python verify.py` in the directory containing the embedded standalone verifier; `requirements.txt` specifies the symbolic dependency. The verifier checks the two-by-two Lyapunov matrix identity, the three-moment recurrence, rational stability and noise examples, the derivative-based formulas, and direct enumeration of Bernoulli histories against exact rational moments and the finite-horizon bound. These finite tests supplement, and do not replace, the quantified analytic proof above. The example \(p=4/5\), \(\gamma=25/16\), \(\beta=1/4\) gives exact \(D=275/1024\); with \(\beta=0\), \(D=75/1024\).

## Relationship to prior work

Bollapragada, Chen and Ward (arXiv:2206.07553, first publicly posted 2022-06-15) analyze stochastic heavy-ball convergence for quadratic problems with minibatch sampling. The question here isolates **unbiased Bernoulli gradient erasure** and compares three different notions of optimality on one model. Stamatiou (arXiv:1704.08515) gives general necessary-and-sufficient mean-square conditions for stochastic linear two-step recurrences; therefore the isolated mean-square criterion here is **not claimed to be generally new**. Loizou and Richtárik (arXiv:1710.10737) give stochastic heavy-ball convergence results for quadratic loss with random sketches, including momentum-free rate bounds and bounds that do not improve with momentum. Their analysis includes a Bernoulli projector as a limiting elementary sampling specialization; it does not give the exact mean-square-stability threshold optimized over momentum and update-noise-floor design conflict established here. Gitman, Lang, Zhang and Xiao (arXiv:1910.13962) develop parameter and stationary-noise tradeoffs for momentum with additive state-independent gradient noise, rather than this coupled random-curvature/erasure process. Kidambi and collaborators (arXiv:1803.05591) explain momentum's possible nonacceleration in stochastic optimization with different examples. The distinctive conclusion established here is the exact **simultaneous design conflict**: momentum can increase the maximal permitted step and reduce an additive stationary noise floor at fixed step, but cannot beat momentum-free, one-success exact annihilation at any finite horizon from zero initial velocity. This classification is specialized and does not claim general stochastic-heavy-ball acceleration or new generic two-step-stability theory.

## Limitations

The analysis is one-dimensional and the random gradient is zero with a positive probability; this makes the universal finite-horizon lower bound unusually strong. The first- and second-moment statements are about fixed parameters and independent observation erasures. The stationary noise floor assumes independent additive update errors of constant variance, and its optimizer may differ for other noise injection conventions. The proof does not address adaptive parameter schedules, nonquadratic objectives, higher-dimensional noncommuting Hessians, finite-precision effects, or wall-clock cost. Generic stochastic two-step theory already covers parts of the stability calculation; specialized historical overlap with the joint three-objective formulation cannot be completely excluded.

## References

1. R. Bollapragada, T. Chen and R. Ward, *On the fast convergence of minibatch heavy ball momentum*, arXiv:2206.07553, first public version 2022-06-15, https://arxiv.org/abs/2206.07553.
2. I. S. Stamatiou, *A note on Asymptotic mean-square stability of stochastic linear two-step methods for SDEs*, arXiv:1704.08515, first public 2017-04-27, https://arxiv.org/abs/1704.08515.
3. I. Gitman, H. Lang, P. Zhang and L. Xiao, *Understanding the Role of Momentum in Stochastic Gradient Methods*, arXiv:1910.13962, first public 2019-10-30, https://arxiv.org/abs/1910.13962.
4. R. Kidambi, P. Netrapalli, P. Jain and S. M. Kakade, *On the insufficiency of existing momentum schemes for Stochastic Optimization*, arXiv:1803.05591, first public 2018-03-15, https://arxiv.org/abs/1803.05591.
5. N. Loizou and P. Richtárik, *Linearly Convergent Stochastic Heavy Ball Method for Minimizing Generalization Error*, arXiv:1710.10737, first public 2017-10-30, https://arxiv.org/abs/1710.10737.
6. M. Pan et al., *Accelerated Convergence of Stochastic Heavy Ball Method under Anisotropic Gradient Noise*, arXiv:2312.14567, first public 2023-12-22, https://arxiv.org/abs/2312.14567.
