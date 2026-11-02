# Strict finite-time work–leak anticorrelation and stall-point rate identification

## Finding

Consider a continuous-time three-state Markov heat-engine rate network, with states \(g,i,e\). The hot useful transition has rates \(g\to e:a\), \(e\to g:b\); the unbiased work transition has rates \(g\leftrightarrow i:w\); the cold transition has rates \(i\to e:c_c\), \(e\to i:d_c\); the distinct parasitic hot transition on the same state pair has rates \(i\to e:u\), \(e\to i:v\). All seven rates are strictly positive. Put \(c=c_c+u\), \(d=d_c+v\), and suppose the aggregate work-current stall identity \(ad=bc\) holds. Define \(r=a/b=c/d\).

The signed work count \(N_w(t)\) increases for \(i\to g\) and decreases for \(g\to i\); the separately labelled hot-leak count \(N_\ell(t)\) increases for parasitic \(i\to e\) and decreases for parasitic \(e\to i\). Initialize at the stationary distribution \(\pi=(1,1,r)/(2+r)\).

**Theorem.** Define
\[
T=(1+r)(b+d)+2w,\quad Z=(r+2)\bigl(rbd+w(b+d)\bigr),\quad K=(1+r)d+2w-b.
\]
Let \(f\) solve \(f''+Tf'+Zf=0\) with \(f(0)=1\) and \(f'(0)=-K\). For every real \(t>0\), define \(G(t)=\int_0^t(t-s)f(s)\,ds\). Then \(G(t)>0\), and
\[
\boxed{\operatorname{Cov}(N_w(t),N_\ell(t))=-\frac{w(u+rv)}{r+2}G(t)<0.}
\]
This holds at **every finite observation duration**, regardless of the sign of the mean leak current. Moreover,
\[
\mathbb E[N_w(t)]=0,\qquad \frac{\mathbb E[N_\ell(t)]}{t}=\frac{u-rv}{r+2}.
\]
Suppose the four aggregate parameters \(r,b,d,w\) are known. For any given \(t>0\), set
\[
U_t=-\frac{r+2}{wG(t)}\operatorname{Cov}(N_w(t),N_\ell(t)),\quad V_t=\frac{r+2}{t}\mathbb E[N_\ell(t)].
\]
Then the **two microscopic leak rates** are uniquely recovered from only the net labelled current mean and the mixed covariance:
\[
\boxed{u=\frac{U_t+V_t}{2},\qquad v=\frac{U_t-V_t}{2r}.}
\]
The long-time cumulant rates are also explicit:
\[
\lim_{t\to\infty}\frac{\operatorname{Cov}(N_w(t),N_\ell(t))}{t}=-\frac{wb(u+rv)}{Z},\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}(N_w(t))}{t}=\frac{2wrbd}{Z}>0.
\]

## Assumptions and scope

The model is the classical stationary population-rate network, **not** the larger explicit quantum-filter model or an energy-storing battery. Cold and parasitic transitions are distinguished in the counted trajectory, even though they connect the same pair of states. Physical decomposition imposes \(0<u<rd\) and \(0<v<d\). Counts are signed jumps, not unsigned traffic. Aggregate stall imposes reversibility after the bath labels are forgotten; it does not impose microscopic detailed balance on the individual cold and hot-leak channels. If \(u/v>r\), the mean parasitic heat transfer is positive while mean useful work transfer vanishes. No weak-coupling approximation is used beyond the assumption that the specified rate model applies.

## Proof

**Stationary generator.** By stall, \(a=rb\), \(c=rd\), and in column-vector convention the population generator is
\[
Q=\begin{pmatrix}-rb-w&w&b\\w&-rd-w&d\\rb&rd&-b-d\end{pmatrix}.
\]
It has \(Q\pi=0\). Moreover \(Q\operatorname{diag}(\pi)\) is symmetric, so the chain is irreducible, reversible at the aggregate level and has a simple zero eigenvalue with two strictly negative *real* eigenvalues. Direct determinant expansion yields
\[
\det(zI-Q)=z(z^2+Tz+Z).
\]

**Two marked currents.** Use the first derivatives of the two-field tilted generator,
\[
W=\begin{pmatrix}0&w&0\\-w&0&0\\0&0&0\end{pmatrix},\qquad
L=\begin{pmatrix}0&0&0\\0&0&-v\\0&u&0\end{pmatrix}.
\]
The negative entries record backward counted jumps and are not negative physical rates. Thus \(\boldsymbol1^\top W\pi=0\) and \(\boldsymbol1^\top L\pi=(u-rv)/(r+2)\), proving the means. As work and leak labels are mutually exclusive for each jump, the Markov property and the two chronological orders of a marked pair give exactly
\[
\operatorname{Cov}(N_w(t),N_\ell(t))=\int_0^t(t-s)S(s)\,ds,
\]
\[
S(s)=\boldsymbol1^\top L e^{Qs}W\pi+\boldsymbol1^\top W e^{Qs}L\pi.
\]
There is no simultaneous-jump delta term, and the mean-product subtraction is zero because the work current has zero mean. Matrix multiplication gives
\[
S(0)=-\frac{w(u+rv)}{r+2},\qquad S'(0)=-KS(0).
\]
The stationary spectral projection contributes nothing to \(S\) because \(\boldsymbol1^\top W\pi=0\). Cayley–Hamilton on the two-mode relaxation subspace proves \(S(s)=S(0)f(s)\) with precisely the scalar initial-value problem above.

**Strict positivity of the integrated kernel.** The two nonzero eigenvalues of \(Q\) are real negative, so \(f\) is a linear combination of two decaying real exponentials, or, for a repeated decay eigenvalue, a linear polynomial times a decaying exponential. Each form has at most one zero on \((0,\infty)\). The Laplace transform is
\[
\widehat f(z)=\frac{z+T-K}{z^2+Tz+Z}=\frac{z+(r+2)b}{z^2+Tz+Z},
\]
whence \(\int_0^\infty f(s)\,ds=(r+2)b/Z>0\). Because \(f(0)=1\), either \(f\) remains positive, or its only sign change is from positive to negative. In the second case, its cumulative integral initially grows and later decreases towards the **strictly positive** total integral. Thus \(H(t)=\int_0^t f(s)\,ds>0\) for every \(t>0\), even if \(f(t)\) itself changes sign. Finally \(G(t)=\int_0^t H(s)\,ds>0\). Since \(u+rv>0\), the finite-time covariance is strictly negative.

**Inversion and asymptotics.** The covariance determines \(u+rv=U_t\), while the mean parasitic current determines \(u-rv=V_t\); solving gives the displayed unique reconstruction. The positive total kernel integral yields \(G(t)/t\to(r+2)b/Z\). The zero-frequency work variance follows independently by placing \(e^{\xi}\), \(e^{-\xi}\) on the two work jumps, differentiating the dominant tilted eigenvalue twice at zero, and obtaining \(2wrbd/Z\). Both asymptotic cumulants are exact consequences of the finite irreducible Markov chain, not finite numerical extrapolations.

## Verification

Run the embedded `verify.py` using Python 3 with SymPy, NumPy and SciPy. It verifies the stationary generator, characteristic polynomial, marked-jump kernel derivatives and zero-frequency cumulant identities symbolically, and independently compares direct finite-time matrix-exponential quadrature with the scalar-ODE formula on 125 deterministic physically admissible parameter sets. The proof of universal positivity is analytic and does **not** rely on the finite tests.

## Relationship to prior work

Prataviera and de Oliveira (2026) derive the **same three-state rate model**, its stationary probabilities, hot-leak mean, useful current, engine reversal threshold and filtering-dependent mean power. Those are credited. Their results do not state a two-channel finite-time signed-count covariance, its strict all-duration sign, or the two-direction leak-rate inverse. Sánchez, Sothmann, Jordan and Büttiker (2013) analyze electric–heat noise and current stall in a distinct four-state, capacitively coupled quantum-dot system; their tight-coupling noise proportionality does not imply the three-state parallel-leak covariance/inverse. General current full-counting-statistics and stalling fluctuation–dissipation theory are background methods, not claimed as new. Broader implicit mathematical coverage is a remaining originality risk.

## Limitations

The theorem assumes exact aggregate stall, stationary initialization, channel-resolved signed net currents and known aggregate rate parameters. It does not establish a sign away from stall, a result for the explicit filter GKSL or Redfield dynamics, or battery-energy fluctuations. The algebraic reconstruction gives ensemble quantities and no finite-sample statistical error bars; at short durations it can be ill-conditioned because \(G(t)=t^2/2+O(t^3)\). Thermodynamic ordering of separate reservoirs is not needed for the sign proof. General mathematical results not located in the literature could cover a portion of this specialization.

## References

1. G. A. Prataviera and M. C. de Oliveira, *Finite-Bandwidth Protection of a Three-Level Quantum Heat Engine Against Parasitic Heat Leaks*, arXiv:2609.40038v1 (first posted 2026-09-30), https://arxiv.org/abs/2609.40038.
2. R. Sánchez, B. Sothmann, A. N. Jordan and M. Büttiker, *Correlations of heat and charge currents in quantum-dot thermoelectric engines*, New Journal of Physics 15 (2013) 125001, arXiv:1307.0598, https://arxiv.org/abs/1307.0598.
3. T. R. Gingrich, J. M. Horowitz, N. Perunov and J. L. England, *Dissipation Bounds All Steady-State Current Fluctuations*, Physical Review Letters 116 (2016) 120601, https://doi.org/10.1103/PhysRevLett.116.120601.
4. *Effective Equilibrium in Out-of-Equilibrium Interacting Coupled Nanoconductors*, https://pmc.ncbi.nlm.nih.gov/articles/PMC7516514/.
