# Exact turnover phase diagram for conditional signal noise in a quorum-sensing network

## Finding

Consider the four-channel cell–signal reaction model described below, at any positive, linearly stable deterministic equilibrium. Its stationary two-coordinate Gaussian linear-noise approximation has a conditional signal variance whose entire dependence on the signal-turnover multiplier \(r>0\) admits an exact classification. In particular, depending only on the local cell-division gain and demographic damping, this conditional variance is either strictly decreasing, identically equal to its Poisson reference level, strictly increasing, or has **exactly one interior maximum**.

More precisely, write the equilibrium as \((x_*,w_*)\), where \(x_*>0\), \(w_*=\alpha x_*/\kappa\), and set
\[
B=b(w_*)=d(x_*),\quad p=x_*d'(x_*),\quad q=x_*b'(w_*),\quad \Delta=p\kappa-\alpha q.
\]
Assume \(B,p,\alpha,\kappa>0\), \(q\geq0\), and \(\Delta>0\). For the stationary Gaussian fluctuation vector \((Z_x,Z_w)\), define the dimensionless conditional-noise ratio
\[
V(r)=\frac{\operatorname{Var}(Z_w\mid Z_x)}{w_*}.
\]
The denominator is the signal's conditional-Poisson variance at the reference equilibrium. The exact answer is
\[
\boxed{V(r)=1+\frac{\alpha(B-q)(B\kappa r+pq)}{(p+\kappa r)[B\Delta+B\kappa^2r+\alpha q^2]}.}
\]
Thus \(V(r)>1\) at every finite positive turnover rate exactly when \(q<B\), \(V(r)=1\) identically when \(q=B\), and \(V(r)<1\) at every such rate exactly when \(q>B\). All three cases have \(\lim_{r\to\infty}V(r)=1\).

To classify the dependence on rate, put
\[
\rho=\frac qB,\qquad \eta=\frac{\alpha q}{\kappa p}\in[0,1),\qquad z=\frac{\kappa r}{p}.
\]
If \(\rho>1\), \(V\) is strictly increasing. If \(\rho=1\), it is constant. If \(0\leq\rho<1\), then \(V\) has a unique interior global maximum if and only if
\[
\boxed{(1-\rho)\sqrt{1-\eta}>\rho.}
\]
In that case its unique maximizing rate and peak value are
\[
\boxed{r_*=\frac p\kappa\left[(1-\rho)\sqrt{1-\eta}-\rho\right],\qquad
V(r_*)=1+\frac{\alpha B}{\kappa p(1+\sqrt{1-\eta})^2}.}
\]
If \(0\leq\rho<1\) but the displayed strict inequality fails, \(V\) is strictly decreasing throughout \((0,\infty)\). The equality case corresponds to a boundary stationary derivative at \(r=0\), which is outside the specified domain, not to an interior maximum.

For the published parameter values \(b(w)=\frac12+2w^4/(1+w^4)\), \(d(x)=29/25+x\), \(\alpha=2\), and \(\kappa=1\), the stable positive equilibrium gives
\[
\boxed{r_*=1.122837273492056553\ldots,\qquad V(r_*)=2.014648952177141542\ldots.}
\]
The source's three numerical examples at \(r=0.5,1,256\) are reproduced; the theorem determines the unique peak between the displayed rates as well as the full parameter classification.

## Assumptions and scope

At population scale \(N\), the event rates of the four-channel continuous-time Markov jump model at densities \((x,w)\) are \(Nx b(w)\) for cell birth, \(Nx d(x)\) for cell death, \(Nr\alpha x\) for signal production, and \(Nr\kappa w\) for signal removal. Each event alters exactly one density coordinate by \(\pm1/N\). Here \(r>0\) scales both signal production and removal while their ratio and the biological production cost are fixed. The deterministic limit is
\[
\dot x=x[b(w)-d(x)],\qquad \dot w=r(\alpha x-\kappa w).
\]
Assume \(b\) and \(d\) are continuously differentiable near a selected positive equilibrium, with \(b'(w_*)\geq0\), \(d'(x_*)>0\), and \(\Delta>0\). Then the linearized deterministic Jacobian is Hurwitz for every \(r>0\), and the corresponding two-dimensional Ornstein–Uhlenbeck linear-noise approximation has a unique nonsingular stationary Gaussian distribution. There is no claim that the original finite-\(N\) jump process possesses a positive stationary distribution: the exact jump process also has an absorbing extinction state.

The assertion is **conditional** Gaussian variance \(\operatorname{Var}(Z_w\mid Z_x)\), equal to the Schur complement of the cell variance in the stationary covariance matrix, not the unconditional signal variance and not the finite-\(N\) conditional variance of the full nonlinear jump process.

## Proof

**1. Stable Gaussian covariance.** At equilibrium, where \(b(w_*)=d(x_*)=B\), the Ornstein–Uhlenbeck drift and diffusion covariances are
\[
J_r=\begin{pmatrix}-p&q\\r\alpha&-r\kappa\end{pmatrix},\qquad
D_r=\begin{pmatrix}2x_*B&0\\0&2r\alpha x_*\end{pmatrix}.
\]
Its trace is \(-p-r\kappa<0\) and determinant is \(r\Delta>0\). Write the unique stationary covariance as \(\Sigma=\begin{pmatrix}s&t\\t&u\end{pmatrix}\), satisfying \(J_r\Sigma+\Sigma J_r^{\mathsf T}+D_r=0\). The three scalar equations are
\[
ps-qt=x_*B,\qquad r\alpha s+qu-(p+r\kappa)t=0,\qquad u=w_*+\frac\alpha\kappa t.
\]
Solving them gives
\[
\boxed{t=\frac{\alpha x_*(B\kappa r+pq)}{\Delta(p+\kappa r)},\quad
s=\frac{x_*[B\Delta+B\kappa^2r+\alpha q^2]}{\Delta(p+\kappa r)},\quad
u=w_*+\frac\alpha\kappa t.}
\]
Every displayed denominator is positive: in particular \(\Delta>0\), \(p+\kappa r>0\), and \(B\Delta+B\kappa^2r+\alpha q^2>0\). Therefore \(s>0\) and the usual Gaussian conditioning identity applies.

**2. Exact conditional variance.** Taking the Gaussian Schur complement and dividing by \(w_*=\alpha x_*/\kappa\) yields
\[
V(r)=\frac{u-t^2/s}{w_*}
=1+\frac{\alpha(B-q)(B\kappa r+pq)}{(p+\kappa r)[B\Delta+B\kappa^2r+\alpha q^2]}.
\]
Since \(q\geq0\), the factor \(B\kappa r+pq\) is strictly positive for every \(r>0\). The sign of \(V(r)-1\) is therefore precisely the sign of \(B-q\), and the large-rate limit is \(1\).

**3. Global turnover classification.** The stability condition \(\Delta>0\) means \(0\leq\eta<1\). Let \(h=1-\eta(1-\rho)>0\). The preceding identity becomes
\[
V(r)=1+\frac{\alpha(B-q)}{\kappa p}\,f(z),\qquad
f(z)=\frac{z+\rho}{(z+1)(z+h)},\quad z>0.
\]
A direct derivative factorization gives
\[
f'(z)=\frac{(1-\rho)^2(1-\eta)-(z+\rho)^2}{(z+1)^2(z+h)^2}.
\]
If \(\rho>1\), the numerator is strictly negative for \(z\geq0\), and the coefficient of \(f\) in \(V-1\) is negative, hence \(V'(r)>0\). If \(\rho=1\), the coefficient vanishes. If \(\rho<1\), the numerator changes sign at most once on \(z>0\), from positive to negative, and its only possible positive root is \(z_*=(1-\rho)\sqrt{1-\eta}-\rho\). When this root is positive, it is the unique global maximizer. Otherwise \(V\) strictly decreases for positive \(r\). At the positive root, substituting \(h=\rho+(1-\rho)(1-\eta)\) into \(f\) gives
\[
f(z_*)=\frac{1}{(1-\rho)(1+\sqrt{1-\eta})^2}.
\]
The claimed formulas for \(r_*\) and \(V(r_*)\) follow. This proves the complete classification for every permissible parameter choice and all \(r>0\).

**4. Reference equilibrium.** With the displayed Hill and death rates, positive equilibria solve
\[
P(x)=-\frac{33}{50}-x+\frac{536}{25}x^4-16x^5=0.
\]
Descartes' rule gives at most two positive roots, while \(P(0)<0\), \(P(1)>0\), and \(P(2)<0\) ensure exactly two; the larger is the stable coexistence root \(x_*=1.296749526950432837\ldots\). Exact rational evaluation yields \(P(1.296749526)>0\) and \(P(1.296749527)<0\). At this root, \(w_*=2x_*\), \(p=x_*\), \(B=29/25+x_*\), and \(q=8x_*w_*^3/(1+w_*^4)^2\). Substitution gives \(\rho=0.0344480956449\ldots\), \(\eta=0.1305268919266\ldots\), and thus the strict interior-maximizer criterion and numerical values in the finding. All numerical values are supplementary to the exact algebraic formulas.

## Verification

The included `verify.py` evaluates the stationary \(2\times2\) Lyapunov identity symbolically, proves the Gaussian Schur-complement reduction and derivative factorization by exact symbolic simplification, tests parameter regimes with rational arithmetic, isolates the larger equilibrium with rational endpoint signs, and independently checks the reference numerical covariance matrix to high precision. It reproduces \(V(0.5)=1.88052501256\ldots\), \(V(1)=2.01152426461\ldots\), and \(V(256)=1.01836071485\ldots\). Run `python verify.py` with the dependencies in `requirements.txt`. The analytic proof, not numerical sampling, establishes the all-parameter and all-rate assertions.

## Relationship to prior work

Ayala and Zimmer (2026) introduce the exact four-channel reaction network, derive its deterministic and linear-noise limits, state the matrix Lyapunov characterization of stationary covariance, and report three conditional-variance values. Those foundations are not new here. The additional result is the **closed-form Schur-complement reduction**, the exact amplification/suppression test \(q\lessgtr B\), the necessary-and-sufficient criterion for a unique finite-turnover peak, and the explicit maximizing rate and peak height for all stable positive equilibria in the model class.

Thomas, Straube and Grima (2012) develop the general slow-scale linear-noise approximation for biochemical networks. Oyarzún, Lugagne and Stan (2014/2015) study feedback-dependent noise amplification and attenuation in a different metabolic gene circuit. These works motivate careful treatment of timescale-dependent stochastic fluctuations, but no inspected statement gives the present four-channel conditional signal-noise turnover classification. The mathematical use of Lyapunov equations and Gaussian conditioning is standard; no novelty is claimed for those general tools.

## Limitations

The conclusion is exact for the stationary Gaussian linear-noise approximation at a linearly stable positive deterministic equilibrium, not for the full finite-population Markov jump process, which can eventually reach extinction. The rate multiplier holds birth/death kinetics, production cost, and the signal production-to-removal ratio fixed. Conditional and unconditional noise behave differently: the latter is not classified by this theorem. The optimizing turnover rate is not an optimizer of the rare-event extinction barrier, the mean extinction time, or experimental signal-detection fidelity. The theorem assumes nonnegative local signal-to-division gain \(q\) and positive crowding damping \(p\); negative feedback and unstable equilibria are outside scope. The paper's reported parameters are illustrative rather than organism-calibrated.

## References

1. M. Ayala and J. Zimmer, *Computing Extinction Barriers in a Quorum-Sensing Reaction Network*, arXiv:2609.39946v1, first posted 2026-09-30. https://arxiv.org/abs/2609.39946 ; accessible HTML https://arxiv.t3mt.com/html/2609.39946v1 .
2. P. Thomas, A. V. Straube and R. Grima, *The slow-scale linear noise approximation: an accurate, reduced stochastic description of biochemical networks under timescale separation conditions*, BMC Systems Biology 6:39 (2012). https://doi.org/10.1186/1752-0509-6-39 .
3. D. A. Oyarzún, J.-B. Lugagne and G.-B. V. Stan, *Noise Propagation in Synthetic Gene Circuits for Metabolic Control*, ACS Synthetic Biology 4:116–125 (2015), first online 2014. https://doi.org/10.1021/sb400126a .
