# A unique intermediate-dispersal variance minimum in heterogeneous two-patch populations

## Finding

For a linearized two-patch population whose local return rates are unequal and whose independent environmental forcing intensities differ, regional stationary fluctuation variance has **at most one finite interior extremum**, and any such extremum is a strict global **minimum**. There is an exact necessary-and-sufficient noise-ratio interval for the minimum to exist.

Label the slower-returning patch first, with return rates \(0<a<b\), and let its forcing variance rate be \(A>0\); let the faster-returning patch have forcing variance rate \(B>0\). Let \(d\geq0\) be symmetric dispersal. Define
\[
\rho_- = \frac{a^2}{b^2},\qquad
\rho_+ = \frac{3a+b}{a+3b},\qquad r=\frac AB.
\]
Then \(\rho_-<\rho_+\), and the stationary variance \(V(d)\) of total abundance *deviations* satisfies:

1. If \(r\leq\rho_-\), then \(V(d)\) increases strictly on \([0,\infty)\).
2. If \(\rho_-<r<\rho_+\), then \(V(d)\) decreases strictly until one positive dispersal rate \(d_*\) and increases strictly thereafter. This is its unique finite global minimum.
3. If \(r\geq\rho_+\), then \(V(d)\) decreases strictly on \([0,\infty)\).

Here \(d_*\) is the unique positive solution of
\[
\frac AB=\frac{a^2(a+b)+4a(a+b)d+2(3a+b)d^2}
{b^2(a+b)+4b(a+b)d+2(a+3b)d^2}.
\]
If \(a=b\), regional variance is constant in \(d\), irrespective of the independent forcing intensities. Exchanging patch labels covers \(a>b\).

## Assumptions and scope

Let \(W_1,W_2\) be independent standard Brownian motions. The population deviations \(X_1,X_2\) from a stable reference state follow the continuous-time linear stochastic system
\[
\begin{aligned}
\mathrm dX_1 &= [-(a+d)X_1+dX_2] \,\mathrm dt +\sqrt A\,\mathrm dW_1,\\
\mathrm dX_2 &= [dX_1-(b+d)X_2] \,\mathrm dt +\sqrt B\,\mathrm dW_2.
\end{aligned}
\]
Parameters satisfy \(a,b,A,B>0\) and \(d\geq0\). The observable is the **sum of deviations**, \(S=X_1+X_2\), and \(V(d)=\lim_{t\to\infty}\operatorname{Var}(S(t))\), independent of the finite initial covariance. The drift matrix is positive definite in magnitude for every admissible parameter set, so a unique stationary centered Gaussian law exists. Equal additive environmental noise amplitudes are not required; noise sources are independent. No population extinction or nonnegative stochastic population process is claimed.

## Proof

**Stationary covariance.** Write \(Q=\begin{pmatrix}a+d&-d\\-d&b+d\end{pmatrix}\). Since \(a,b>0\) and \(d\geq0\), \(Q\) is symmetric positive definite. For the stationary covariance \(C=\begin{pmatrix}u&w\\w&v\end{pmatrix}\), the Lyapunov identity \(QC+CQ=\operatorname{diag}(A,B)\) is equivalent to
\[
2(a+d)u-2dw=A,\quad 2(b+d)v-2dw=B,\quad
(a+b+2d)w-d(u+v)=0.
\]
Eliminating \(u,v,w\) gives the exact regional variance
\[
\boxed{V(d)=\frac{(a+b+4d)\{A(b+d)+B(a+d)\}}
{2(a+b+2d)\{ab+(a+b)d\}}.}
\]
In particular, \(V(0)=A/(2a)+B/(2b)\) and \(\lim_{d\to\infty}V(d)=(A+B)/(a+b)\).

**One-crossing derivative.** Define positive quadratic polynomials for \(d\geq0\):
\[
\begin{aligned}
U(d)&=a^2(a+b)+4a(a+b)d+2(3a+b)d^2,\\
W(d)&=b^2(a+b)+4b(a+b)d+2(a+3b)d^2.
\end{aligned}
\]
Direct differentiation of the displayed rational formula yields
\[
V'(d)=\frac{(b-a)\{BU(d)-AW(d)\}}
{2(a+b+2d)^2\{ab+(a+b)d\}^2}.
\]
For \(a<b\), the sign is therefore that of \(R(d)-A/B\), where \(R(d)=U(d)/W(d)\). A polynomial differentiation and cancellation gives
\[
\boxed{R'(d)=\frac{4(b-a)(a+b)(a+b+2d)\{ab+(a+b)d\}}{W(d)^2}>0.}
\]
The boundary values are \(R(0)=a^2/b^2\) and \(\lim_{d\to\infty}R(d)=(3a+b)/(a+3b)\). Their difference equals \((b-a)(a^2+4ab+b^2)/(b^2(a+3b))>0\). Consequently, \(R\) rises strictly through every value between these two endpoints exactly once. If the noise ratio lies below, inside, or above this interval, the derivative of \(V\) is respectively always positive, negative-then-positive, or always negative for finite positive \(d\). This proves all three cases, including the nonattainment of the limiting infimum when \(r\geq\rho_+\).

When \(a=b\), summing the stochastic equations cancels dispersal and gives \(\mathrm dS=-aS\,\mathrm dt+\sqrt A\,\mathrm dW_1+\sqrt B\,\mathrm dW_2\). Its stationary variance \((A+B)/(2a)\) is independent of \(d\). Relabeling proves the remaining asymmetric cases.

**Exact witness.** For \((a,b,A,B)=(1,2,1/2,1)\), the noise ratio \(1/2\) lies strictly between the two boundaries \(1/4\) and \(5/7\), and \(R(1)=1/2\). Hence the unique optimum is exactly \(d_*=1\), where
\[
\boxed{V(0)=\frac12,\qquad V(1)=\frac{49}{100},\qquad \lim_{d\to\infty}V(d)=\frac12.}
\]
Thus an intermediate dispersal rate reduces regional variance even in a single-species linear stochastic setting, provided both intrinsic return rates and local forcing differ suitably.

## Verification

Run `python3 check.py` with Python 3. No nonstandard packages or external data are required. The program solves the stationary Lyapunov equations independently, in exact rational arithmetic, for 480 positive-parameter configurations and compares against the closed-form variance. It also checks the strict ratio ordering on a finite grid and independently confirms the rational witness, both limiting variances, and derivative signs. Successful output reports 480 cases and the exact \(49/100\) minimum. These finite checks are safeguards against algebraic and transcription errors, **not** the proof of the quantified all-parameter assertion, which is the differentiation and monotonic-ratio identity above.

## Relationship to prior work

Kendall et al. (2000) derive exact population synchrony formulas in a discrete-time two-patch model with identical local regulation. Their total-population equation decouples from migration because the two regulation coefficients coincide. In the continuous-time setting here this corresponds to the flat \(a=b\) boundary, not to the heterogeneous rate and noise phase diagram.

Keeling (2000; precise first-online date listed by the publisher as 25 December 2001) develops stochastic metapopulation moment closures and distinguishes single-species from natural-enemy persistence effects. Its objective is persistence/extinction and its dynamical equations differ from the exact stationary additive-noise covariance problem here. Loreau, Mouquet and Gonzalez (2003) establish spatial insurance with nonmonotone productivity variability in a nonlinear, multispecies consumer-resource model; the present statement identifies an explicit *linear, single-species* mechanism and the sharp ratio conditions for a unique **regional-variance** minimum.

A later study on noise, coupling, and early-warning indicators (2017) derives homogeneous two-patch spectra and numerically examines heterogeneous patches. Its accessible section descriptions do not state the present exact heterogeneity/noise-ratio condition. The general Lyapunov covariance method is standard prior mathematics; neither solving a Lyapunov equation nor observing that intermediate dispersal sometimes helps is asserted to be new. The assessed contribution is the complete necessary-and-sufficient one-valley classification, its thresholds, and its restriction to a natural two-patch ecological fluctuation model.

## Limitations

The OU model is a linear fluctuation approximation. Gaussian trajectories can be negative and do not describe individual counts, absorption, genuine extinctions, nonlinear density dependence, multiplicative environmental noise, temporally correlated forcing, or dispersal costs. The result concerns variance of the **regional sum** and does not automatically hold for local variances, coefficients of variation with changing means, or arbitrary networks of three or more patches. The exact phase diagram assumes independent additive noises and symmetric dispersal; correlated noises can change it. Published equivalence under alternative stochastic-control or spatial-insurance terminology remains a bibliographic risk, and independent scholarly assessment has not been performed.

## References

1. Kendall, B. E., Bjørnstad, O. N., Bascompte, J., Keitt, T. H., and Fagan, W. F. (2000). *Dispersal, Environmental Correlation, and Spatial Synchrony in Population Dynamics*. The American Naturalist 155, 628–636. DOI: 10.1086/303350. Full text examined via a lawful university-hosted author copy.
2. Keeling, M. J. (2000). *Metapopulation moments: coupling, stochasticity and persistence*. Journal of Animal Ecology 69, 725–736. DOI: 10.1046/j.1365-2656.2000.00430.x. Publisher full text and PDF examined.
3. Loreau, M., Mouquet, N., and Gonzalez, A. (2003). *Biodiversity as spatial insurance in heterogeneous landscapes*. PNAS 100, 12765–12770. DOI: 10.1073/pnas.2235465100. Full text examined via an author's institutional website.
4. *How noise and coupling influence leading indicators of population extinction in a spatially extended ecological system* (2017). DOI: 10.1080/17513758.2017.1339834. Indexed model, analytic homogeneous-case and heterogeneous-case descriptions consulted; complete article was not retrieved.
