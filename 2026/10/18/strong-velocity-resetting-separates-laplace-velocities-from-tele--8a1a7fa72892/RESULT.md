# Strong velocity resetting separates Laplace velocities from telegraph transport

## Finding

Consider a one-dimensional inertial active particle whose velocity is set to zero at independent Poisson events of rate \(r\), without resetting the underlying dichotomous propulsion force. At each nonresetting time its velocity obeys \(\dot V_r(t)=\Sigma S(t)-g(V_r(t))\), where \(S(t)\in\{-1,1\}\) flips at rate \(\lambda\). Define the unreset position increment \(X_r(t)=\int_0^t V_r(s)\,ds\). Let the joint velocity–orientation process be in stationarity.

**Theorem (two simultaneous fast-reset limits).** Under the assumptions below, as \(r\to\infty\):

1. For each fixed time, the rescaled stationary velocity \(Y_r(t)=rV_r(t)/\Sigma\) converges in second Wasserstein distance to the *symmetric unit-scale Laplace distribution*, having density \(e^{-|y|}/2\). If \(L\) is the Lipschitz constant specified below, the explicit bound is
   \[
   W_2\big(\mathcal L(Y_r(t)),\operatorname{Laplace}(0,1)\big)
   \le \sqrt{24\lambda/r}+\sqrt6\,L/r.
   \]
2. At any fixed distinct observation times \(t_1,\ldots,t_m\), the joint rescaled velocities converge in distribution to \((S(t_1)E_1,\ldots,S(t_m)E_m)\), where the \(E_j\) are independent mean-one exponential variables independent of the entire orientation process \(S\). In particular,
   \[
   \lim_{r\to\infty}\frac{r^2}{\Sigma^2}\operatorname{Var}V_r(t)=2,
   \quad
   \lim_{r\to\infty}\frac{r^2}{\Sigma^2}\operatorname{Cov}(V_r(0),V_r(t))=e^{-2\lambda t}\quad(t>0).
   \]
   Thus the limiting covariance at every strictly positive fixed lag is half its zero-lag limit after normalization by stationary variance.
3. **The spatial trajectories have a different limit from instantaneous velocities:** for every finite \(T>0\),
   \[
   \sup_{0\le t\le T}\left|\frac r\Sigma X_r(t)-\int_0^t S(s)\,ds\right|\longrightarrow0
   \quad\text{in }L^2.
   \]
   Consequently,
   \[
   \lim_{r\to\infty}\frac{r^2}{\Sigma^2}\operatorname{Var} X_r(T)
   =\frac{T}{\lambda}-\frac{1-e^{-2\lambda T}}{2\lambda^2}.
   \]

The limit is *not* convergence of \(Y_r\) as a continuous-path process. Its exponentially marked instantaneous fluctuations average out upon time integration, leaving the genuine persistent-telegraph trajectory. This distinction holds uniformly for both shear-thickening and shear-thinning drag families specified below.

## Assumptions and scope

Fix \(\lambda>0\) and propulsion acceleration \(\Sigma>0\). Suppose \(g\) is odd, nondecreasing, and continuously differentiable on a neighborhood of \([-b,b]\), with \(g(0)=0\), \(g(b)=\Sigma\) for some finite \(b>0\). Set \(L=\sup_{|v|\le b}|g'(v)|<\infty\). The motion begins from the stationary joint law of velocity and orientation. The Poisson reset process is independent of the stationary symmetric telegraph orientation; resets set \(V_r\) to zero but do *not* flip or redraw \(S\). The position itself is never reset. All limits hold at fixed \(\lambda,\Sigma,g,T\) as \(r\to\infty\).

Examples covered include \(g(v)=\tan v\) with arbitrary \(\Sigma>0\), \(b=\arctan\Sigma\), \(L=1+\Sigma^2\), and \(g(v)=\tanh v\) for \(0<\Sigma<1\), \(b=\operatorname{arctanh}\Sigma\), \(L\le1\). The confining interval is invariant under both deterministic force signs, and each reset regenerates the velocity from zero. The two-sided stationary Poisson construction therefore yields the unique stationary joint velocity–orientation law. Symmetry gives zero stationary velocity and position-increment means.

## Proof

**Step 1: A stationary age representation and an absolute velocity bound.** Let \(N_r\) be the independent two-sided Poisson reset process, and let \(A_r(t)\) be the elapsed time since its most recent point. In stationarity \(A_r(t)\sim\operatorname{Exp}(r)\), independent of the entire orientation trajectory. Writing \(a=A_r(t)\) and \(\tau=t-a\), the last velocity reset yields the exact pathwise representation
\[
V_r(t)=\int_{\tau}^{t}\{\Sigma S(u)-g(V_r(u))\}\,du.
\]
Since the drag is odd and nondecreasing, \(v g(v)\ge0\) and the scalar comparison principle gives \(|V_r(t)|\le\min\{b,\Sigma A_r(t)\}\). Indeed, starting at zero, the upper and lower derivatives of \(|V_r|\) are bounded by \(\Sigma\), and \(\pm b\) are barriers. Consequently \(|g(V_r(u))|\le L|V_r(u)|\le L\Sigma(u-\tau)\) between successive resets.

**Step 2: A quantitative coupling to signed exponential ages.** Let \(Z_r(t)=rA_r(t)\); its distribution is the mean-one exponential law for every \(r\). Compare \(Y_r(t)=rV_r(t)/\Sigma\) with \(S(t)Z_r(t)\):
\[
Y_r(t)-S(t)Z_r(t)=r\int_{t-A_r(t)}^t\{S(u)-S(t)\}\,du
-\frac r\Sigma\int_{t-A_r(t)}^t g(V_r(u))\,du.
\]
If the orientation does not flip in the most recent interval, the first integral vanishes; otherwise its absolute value is at most \(2rA_r(t)\). Conditional on the age \(a\), the probability of at least one flip is at most \(\lambda a\). Its squared expected contribution is at most \(4r^2\lambda\mathbb E[A_r^3]=24\lambda/r\). The drag contribution has absolute value at most \(Lr A_r^2/2\), and hence squared expectation at most \(L^2r^2\mathbb E[A_r^4]/4=6L^2/r^2\). Minkowski therefore gives
\[
\|Y_r(t)-S(t)Z_r(t)\|_2\le\sqrt{24\lambda/r}+\sqrt6 L/r.
\]
The sign \(S(t)\) is fair and independent of \(Z_r(t)\). Their product has density \(e^{-|y|}/2\). This proves the explicit Wasserstein estimate. The bound \(|Y_r|\le Z_r\) also ensures convergence of all fixed finite polynomial moments.

**Step 3: Independent fast-age marks at separated observation times.** Fix distinct deterministic times and let \(\delta>0\) be their minimum separation. Except on an event with probability at most \(m e^{-r\delta/2}\), each recent age is shorter than \(\delta/2\). The ages then depend only on disjoint Poisson increments, and can be coupled to independent exponential ages; their residual joint dependence vanishes as \(r\to\infty\). The orientation process is independent of those increments and its pathwise variation within every recent age vanishes in probability (probability at most \(m\lambda/r\)). Combining this with Step 2 gives the claimed joint convergence. Since \(|Y_r(t)|\le Z_r(t)\) and the exponential ages have uniformly bounded fourth moments, products are uniformly integrable. For \(t>0\), \(\mathbb E[S(0)S(t)]=e^{-2\lambda t}\), \(\mathbb E E_j=1\), and \(\mathbb E E_j^2=2\). These identities yield both covariance limits. No pointwise covariance convergence at \(t=0\) to the positive-lag expression is asserted.

**Step 4: A strong finite-horizon path limit.** The age process satisfies \(\mathbb E[Z_r(t)]=1\), \(\operatorname{Var}(Z_r(t))=1\), and, for \(t\ge s\),
\[
\operatorname{Cov}(Z_r(s),Z_r(t))=e^{-r(t-s)}.
\]
This follows directly from the Markov-age regression \(\mathbb E[Z_r(t)-1\mid Z_r(s)]=e^{-r(t-s)}(Z_r(s)-1)\). Define \(B_r(t)=S(t)(Z_r(t)-1)\). Independence of orientation and reset clocks and the telegraph correlation formula imply
\[
\mathbb E[B_r(s)B_r(t)]=e^{-(r+2\lambda)|t-s|}.
\]
Put \(H_r(t)=\int_0^t B_r(s)\,ds\). At every fixed \(t\in[0,T]\),
\[
\mathbb E H_r(t)^2
=2\int_0^t(t-u)e^{-(r+2\lambda)u}\,du
\le \frac{2T}{r+2\lambda}.
\]
For integer \(n\ge1\), take an evenly spaced time grid on \([0,T]\). Bound the maximum over grid points by the sum of their squared values; between adjacent points, use Cauchy–Schwarz and \(\mathbb E B_r(t)^2=1\). Thus
\[
\mathbb E\sup_{0\le t\le T}|H_r(t)|^2
\le \frac{4nT}{r+2\lambda}+\frac{2T^2}{n}.
\]
Choosing \(n=\max\{1,\lfloor\sqrt r\rfloor\}\) gives convergence to zero. The remaining integrated error is bounded by
\[
\mathbb E\sup_{0\le t\le T}
\left|\int_0^t\{Y_r(s)-S(s)Z_r(s)\}\,ds\right|^2
\le T^2\left(\sqrt{24\lambda/r}+\sqrt6 L/r\right)^2.
\]
Consequently \(\int_0^t Y_r(s)ds\to\int_0^t S(s)ds\) uniformly in \(L^2\) on every compact time interval, as claimed.

**Step 5: The finite-horizon transport variance.** The integral of the stationary symmetric orientation has zero mean. By the strong convergence in Step 4, its second moment is the limit of that of \(rX_r(T)/\Sigma\). Fubini and \(\mathbb E[S(s)S(t)]=e^{-2\lambda|t-s|}\) give
\[
\operatorname{Var}\left(\int_0^T S(s)ds\right)
=2\int_0^T (T-u)e^{-2\lambda u}\,du
=\frac T\lambda-\frac{1-e^{-2\lambda T}}{2\lambda^2}.
\]
The proof is complete.

## Verification

The standalone executable `verify.py` evaluates the stationary model with event-driven Poisson resets and orientation flips and fourth-order Runge–Kutta dynamics between events. Tests at \(r=20\) and \(r=80\) for both \(g(v)=\tan v\), \(\Sigma=1.2\), and \(g(v)=\tanh v\), \(\Sigma=0.6\), with \(\lambda=0.8\), compare scaled mean absolute velocity, scaled velocity variance, a separated-lag covariance at lag \(0.8\), and the integrated-displacement variance against their exact limits. They pass stated finite-sample tolerances. The script also checks exact stationary moments for the linear-drag specialization \(g(v)=\kappa v\):
\[
\mathbb E[V_rS]=\frac\Sigma{r+\kappa+2\lambda},\quad
\mathbb E[V_r^2]=\frac{2\Sigma^2}{(r+2\kappa)(r+\kappa+2\lambda)}.
\]
The linear-drag Green–Kubo integral is
\[
D_r=\frac{\mathbb E[V_r^2]+\Sigma\mathbb E[V_rS]/(2\lambda)}{r+\kappa},
\quad\text{so }\lim_{r\to\infty}r^2D_r/\Sigma^2=1/(2\lambda).
\]
This last long-time coefficient is established here **only for linear drag**, not as an interchange of the general nonlinear and infinite-observation-time limits.

Run the verification with `python verify.py` (requires Python and NumPy). The theorem is proved analytically above; finite numerical checks are supplementary and not used to infer convergence.

## Relationship to prior work

Howlader, Mondal and Das (arXiv:2606.00560, first posted 2026-05-30), §§2–4, introduce precisely this independent velocity-only resetting and retained dichotomous orientation and numerically observe a cusp-shaped steady velocity distribution and the exponent \(D_{\rm eff}\propto r^{-2}\). They do not explicitly establish the quantitative stationary Wasserstein limit, independent exponential velocity marks at separated times, or the pathwise telegraph limit for nonlinear drag. Their resetting protocol and qualitative numerical observations are prior work, not new claims.

Olsen and Löwen (arXiv:2401.12685; J. Stat. Mech. 033210, 2024) provide general propagator and diffusion methods for partial velocity resetting. Their general transport machinery is acknowledged; the full text was inaccessible in the present comparison, so implicit derivability of certain moment statements from that theory remains a novelty risk. The present finding emphasizes the distinct *joint* fast-reset stationary-velocity and finite-horizon functional limit for persistent dichotomous propulsion, with an explicit pathwise quantitative proof.

Other related works include Evans and Majumdar (2018), addressing position-reset run-and-tumble dynamics rather than a velocity-only reset that retains the propulsion force, and Santra, Olsen and Gupta (2024), addressing general switching processes. These concern different resetting/observable regimes and do not, on the inspected material, explicitly give the present two-scale law.

## Limitations

The theorem requires Poisson *velocity-only* resets, a persistent orientation independent of resetting, stationary joint initialization, fixed strictly positive orientation-flip rate, and smooth monotone bounded-trapping drag. No statement is made for resetting the orientation, weak confining drag outside the assumed class, nonsmooth dry friction, or simultaneous scaling of \(\lambda\) with \(r\). General nonlinear long-time diffusion coefficients require an additional uniform-in-time argument and are not claimed; the stated variance limit takes \(r\to\infty\) at each fixed finite observation horizon. Convergence of instantaneous scaled velocities is finite-dimensional rather than a continuous-path limit. A potentially relevant general partial-resetting paper could not be read in full, leaving an originality risk.

## References

1. S. Howlader, S. Mondal and P. Das, “Velocity Resetting of Inertial Run-and-Tumble Particles in Non-Newtonian Media: Velocity Distribution, Diffusion and First-Passage Time,” arXiv:2606.00560v1 (2026-05-30). https://arxiv.org/abs/2606.00560
2. K. S. Olsen and H. Löwen, “Dynamics of inertial particles under velocity resetting,” J. Stat. Mech. (2024) 033210, arXiv:2401.12685. https://arxiv.org/abs/2401.12685
3. M. R. Evans and S. N. Majumdar, “Run and tumble particle under resetting: a renewal approach,” J. Phys. A 51 (2018) 475003. https://doi.org/10.1088/1751-8121/aae74e
4. I. Santra, K. S. Olsen and D. Gupta, “Dynamics of switching processes: general results and applications in intermittent active motion,” Soft Matter 20 (2024), 9360–9372. https://doi.org/10.1039/d4sm01054j
