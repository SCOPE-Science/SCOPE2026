# A sharp correlated-noise threshold for spectral peaks in an overdamped feedforward Langevin pair

## Finding
Consider the stationary feedforward linear Langevin system in the next section. Although both deterministic eigenvalues are real and strictly negative, its downstream output can have a unique nonzero-frequency power-spectrum maximum. Put
\[
 t=k\sqrt{D_y/D_x},\quad c=b^2+t^2+2bt\rho,\quad h=\frac{a^2b^2}{a^2+b^2}.
\]
The *two-sided* downstream power spectral density is
\[
 S_x(\omega)=\frac{2D_x(\omega^2+c)}{(\omega^2+a^2)(\omega^2+b^2)}.
\]
It has precisely two strict global maxima at opposite nonzero frequencies if and only if \(c<h\), equivalently
\[
 \rho<\rho_c(t):=-\frac{t^2+b^4/(a^2+b^2)}{2bt}.
\]
In that case the unique positive maximizing frequency satisfies
\[
 \omega_*^2=-c+\sqrt{(a^2-c)(b^2-c)}.
\]
Otherwise the spectrum is strictly decreasing on \(\omega>0\) and is maximized uniquely at zero. At equality \(c=h\), zero is a quartically flat maximum, not an extra positive-frequency maximum.

There exists *some* positive feedforward coupling \(k\) that produces an off-zero spectral peak for prescribed \(a,b,D_x,D_y,\rho\) if and only if
\[
 \boxed{\rho<-\frac{b}{\sqrt{a^2+b^2}}}.
\]
This is a sharp anticorrelation boundary, attained in the coupling optimization at \(t=b^2/\sqrt{a^2+b^2}\). Independent input noises (\(\rho=0\)) cannot produce this kind of peak, regardless of feedforward gain.

Every peaked case also has exactly one positive-lag zero of its stationary downstream autocovariance, and the autocovariance is negative thereafter. This single sign reversal does not represent an oscillatory deterministic mode.

## Assumptions and scope
Let \(a,b,k,D_x,D_y\) be finite strictly positive real constants and \(-1<\rho<1\). Let \(W_x,W_y\) be Brownian motions with \(d\langle W_x,W_y\rangle_t=\rho\,dt\). The Itô system is
\[
 dX_t=(-aX_t+kY_t)\,dt+\sqrt{2D_x}\,dW_{x,t},\qquad
 dY_t=-bY_t\,dt+\sqrt{2D_y}\,dW_{y,t}.
\]
It is started in its unique centered stationary Gaussian law, which exists because both eigenvalues of the drift matrix are \(-a,-b\). We use \(C_x(\tau)=\mathbb E[X_{t+\tau}X_t]\) and the angular-frequency convention \(S_x(\omega)=\int_{\mathbb R}e^{-i\omega\tau}C_x(\tau)\,d\tau\). Peaks refer to the stationary spectrum of \(X\), not to a time-domain driven response, a nonlinear limit cycle, or the spectrum of \(Y\).

## Proof
The transfer matrix of the stable drift \(A=\bigl(\begin{smallmatrix}-a&k\\0&-b\end{smallmatrix}\bigr)\) is \(H(\omega)=(i\omega I-A)^{-1}\). The first row equals
\[
 \left(\frac1{a+i\omega},\ \frac{k}{(a+i\omega)(b+i\omega)}\right).
\]
The noise-intensity covariance is \(2D\), where
\[
 D=\begin{pmatrix}D_x&\rho\sqrt{D_xD_y}\\\rho\sqrt{D_xD_y}&D_y\end{pmatrix}.
\]
Thus the first diagonal entry of \(2H(\omega)DH(\omega)^*\) is the stated rational \(S_x\). Its denominator is positive for real \(\omega\); \(c=(b+t\rho)^2+t^2(1-\rho^2)>0\), so the numerator is nonnegative as required.

Writing \(z=\omega^2\ge0\), the positive scale factor \(2D_x\) can be dropped. For \(F(z)=(z+c)/((z+a^2)(z+b^2))\), the numerator of \(F'(z)\) is
\[
 -z^2-2cz+a^2b^2-c(a^2+b^2).
\]
This polynomial is strictly decreasing for \(z\ge0\). It is positive at zero exactly when \(c<h\). In that case it has exactly one positive zero \(z_*=-c+\sqrt{(a^2-c)(b^2-c)}\), producing two strict global maxima in \(\omega\). Otherwise \(F'(z)<0\) for all \(z>0\), including at \(c=h\). The equivalence with \(\rho<\rho_c(t)\) follows by substitution.

For fixed \(a,b\), optimizing the permitted correlation boundary over \(t>0\) uses the arithmetic-geometric mean inequality:
\[
 \rho_c(t)=-\frac{1}{2b}\left(t+\frac{b^4/(a^2+b^2)}{t}\right)
 \le-\frac b{\sqrt{a^2+b^2}},
\]
with equality exactly at \(t=b^2/\sqrt{a^2+b^2}\). Because this maximum lies strictly between \(-1\) and zero, a positive \(t\) satisfying \(\rho<\rho_c(t)\) exists exactly for the claimed anticorrelation condition. The physical \(k\) realizing \(t\) is \(k=t\sqrt{D_x/D_y}\).

For the covariance assertion, if \(a\ne b\), partial fractions give for \(\tau\ge0\)
\[
 C_x(\tau)=D_x\left[\frac{c-a^2}{a(b^2-a^2)}e^{-a\tau}
 +\frac{b^2-c}{b(b^2-a^2)}e^{-b\tau}\right].
\]
Since \(c<h<\min(a^2,b^2)\) in the peaked regime, the coefficient of the slower exponential is strictly negative and that of the faster exponential strictly positive. Their sum is strictly positive at \(\tau=0\), since it is the nonzero stationary variance. The ratio of the positive faster term to the magnitude of the negative slower term decreases strictly from above one to zero, proving exactly one positive-lag sign crossing. For \(a=b\), inversion gives
\[
 C_x(\tau)=\frac{D_xe^{-a\tau}}{2a^3}
 \bigl[(a^2+c)+(c-a^2)a\tau\bigr],
\]
whose bracket has precisely one positive zero because \(c<h=a^2/2\). The deterministic drift always has only negative real eigenvalues, including a possible Jordan block when \(a=b\), so no oscillatory deterministic eigenfrequency underlies these peaks.

For an exact example, \(a=b=k=D_x=D_y=1\) and \(\rho=-4/5\) give \(c=2/5\) and
\[
 S_x(\omega)=\frac{2(\omega^2+2/5)}{(1+\omega^2)^2},\quad
 \omega_*=\frac1{\sqrt5},\quad
 C_x(\tau)=\frac{7-3|\tau|}{10}e^{-|\tau|}.
\]
Here the nonzero spectral peaks coexist with a single sign change, at \(|\tau|=7/3\), rather than sustained oscillatory correlations.

## Verification
The accompanying `verify.py` checks the spectral formula against an independently inverted complex transfer matrix; checks the covariance inverse transform against an independently solved continuous Lyapunov equation and matrix exponential; tests the global peak-or-monotonicity alternatives at random positive parameters and correlations; and verifies the sharp optimized threshold algebraically. Run `python verify.py` with Python 3, NumPy and SciPy. Finite numerical comparisons support, but are not the proof of, the global parameter statement established above.

## Relationship to prior work
Wallace et al. (2011) derive noisy network spectral peaks near stable-focus feedback dynamics, and explicitly distinguish those quasicycles from stable-node feedforward regimes. The present exact feedforward construction instead has real deterministic eigenvalues and produces a nonzero spectral peak only through sufficiently anticorrelated inputs. MacKay (2021) gives a general Gaussian linear-mode covariance/inference framework that accommodates real modes and correlated excitation; that framework supplies background tools but does not state this specific necessary-and-sufficient correlation/coupling spectral boundary or the single autocovariance sign-crossing classification. Standard Ornstein--Uhlenbeck resolvent formulas are not claimed as new.

## Limitations
This is an exactly solvable linear Gaussian feedforward null model, not a claim that arbitrary neural or biochemical networks obey the same threshold. The theorem concerns Gaussian white forcing of two overdamped components, a fixed downstream coordinate, and stationary two-sided spectra. Finite-frequency peaks are not automatically evidence of a stable focus or deterministic oscillatory mode, but this result alone does not identify the mechanism of an observed empirical peak. The exact historical priority of the combined sharp boundary and sign-change result has not been independently certified.

## References
1. E. Wallace, M. Benayoun, W. van Drongelen, J. D. Cowan, "Emergent Oscillations in Networks of Stochastic Spiking Neurons," *PLoS ONE* **6** (2011), e14804, published 2011-05-06, https://doi.org/10.1371/journal.pone.0014804, freely accessible full article at https://pmc.ncbi.nlm.nih.gov/articles/PMC3089610/.
2. R. S. MacKay, "Inference of dominant modes for linear stochastic processes," *Royal Society Open Science* **8** (2021), 201442, https://doi.org/10.1098/rsos.201442, freely accessible article at https://pmc.ncbi.nlm.nih.gov/articles/PMC8059618/.
