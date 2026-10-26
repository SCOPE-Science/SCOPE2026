# Cubic-root endemic spillover from a vanishing unvaccinated minority

## Finding

In the two-vaccination-status SIQS mean-field model of Frieswijk, Zino, and Cao [1], a very small unvaccinated minority can generate an endemic burden disproportionately larger than its population share when the vaccinated-only and minority within-group transmission channels are simultaneously critical.

Write \(\varepsilon\) for the **nonvaccinated** fraction, so the vaccinated fraction is \(1-\varepsilon\). Define
\[
 h_n=1-p_q,\quad h_v=1-p_q(1-\gamma_q),\quad s=1-\gamma_t,
 \quad a=h_n(1-\sigma_n),\quad b=s h_v(1-\sigma_v),\quad R=a/b.
\]
Assume \(a>b>0\), \(s>0\), \(0<\varepsilon<1\), and impose the two critical tuning conditions
\[
 \theta=\frac b a=\frac1R,\qquad \beta+\tau=2\lambda b.
\]
For **every** \(0<\varepsilon<1\), the mean-field equations have exactly two biologically admissible equilibria: the disease-free equilibrium and a unique endemic equilibrium with infection present in both groups. Let \(u_\varepsilon\) and \(w_\varepsilon\) denote, respectively, the endemic fractions of nonvaccinated and vaccinated individuals in either infectious or quarantined-infected states (conditional on group membership). Then, as \(\varepsilon\downarrow0\),
\[
 u_\varepsilon=\frac{R-1}{R^{2/3}s^{1/3}}\,\varepsilon^{1/3}+O(\varepsilon^{2/3}),
 \qquad
 w_\varepsilon=\frac{(R-1)s^{1/3}}{R^{1/3}}\,\varepsilon^{2/3}+O(\varepsilon).
\]
In particular, the **population-wide prevalence** (infectious plus quarantined-infected) is
\[
 P_\varepsilon=\varepsilon u_\varepsilon+(1-\varepsilon)w_\varepsilon
 =\frac{(R-1)s^{1/3}}{R^{1/3}}\,\varepsilon^{2/3}+O(\varepsilon).
\]
Thus \(P_\varepsilon/\varepsilon\to\infty\): prevalence tends to zero more slowly than the size of the minority. This is a deterministic equilibrium result in the large-population mean-field limit, not a finite-population persistence claim.

## Assumptions and scope

The two groups are nonvaccinated \(n\) and vaccinated \(v\). The population shares are \(\varepsilon\) and \(1-\varepsilon\). The health states are susceptible \(S\), mildly infectious \(I\), and isolated/quarantined infected \(Q\). The model [1] has positive infection rate \(\lambda\), positive recovery rate \(\beta\), testing rate \(\tau\ge0\), homophily parameter \(0\le\theta<1\), severe-symptom probability \(0<p_q<1\), responsibility parameters \(0\le\sigma_n,\sigma_v<1\), and vaccine factors \(0<\gamma_t<1\), \(0\le\gamma_q<1\). These ranges guarantee \(h_n,h_v,s,a,b>0\); additionally require \(a>b\) and the two critical equalities above. The equations are the deterministic infinite-population mean-field equations in [1], not the finite stochastic network process. All positivity and asymptotic assertions hold for fixed admissible values of the other parameters as \(\varepsilon\downarrow0\).

An individual in either \(I\) or \(Q\) is counted in the total infected burden; only individuals in \(I\) transmit infection. No global convergence or finite-population fixation assertion is made.

## Proof

**1. Reduction of the actual stationary equations.** Let \(S_n,I_n,Q_n,S_v,I_v,Q_v\) denote population fractions. Define total infected fractions \(X_n=I_n+Q_n\), \(X_v=I_v+Q_v\), and conditional fractions \(u=X_n/\varepsilon\), \(w=X_v/(1-\varepsilon)\). The group totals are conserved and hence
\[
 S_n=\varepsilon(1-u),\qquad S_v=(1-\varepsilon)(1-w).
\]
The transmission hazards per susceptible, read directly from the source mean-field equations, are
\[
 H_n=2\lambda\left[(1-\sigma_n)\left(\frac\theta\varepsilon+1-\theta\right)I_n+(1-\sigma_v)(1-\theta)I_v\right],
\]
\[
 H_v=2\lambda s\left[(1-\sigma_n)(1-\theta)I_n+(1-\sigma_v)\left(\frac\theta{1-\varepsilon}+1-\theta\right)I_v\right].
\]
Because testing transfers \(I\) to \(Q\) without removing infection, the stationarity conditions for total infected and mildly infectious fractions are
\[
 H_n S_n=\beta X_n,\quad H_v S_v=\beta X_v,\qquad
 (\beta+\tau)I_n=h_n\beta X_n,\quad
 (\beta+\tau)I_v=h_v\beta X_v.
\]
These identities are necessary and sufficient for stationarity of the six mean-field equations, since \(Q_\alpha=X_\alpha-I_\alpha\). Substituting yields the **exact** fixed-point relations
\[
 \frac u{1-u}=(M_\varepsilon)_{11}u+(M_\varepsilon)_{12}w,
 \qquad \frac w{1-w}=(M_\varepsilon)_{21}u+(M_\varepsilon)_{22}w,
\]
where
\[
 M_\varepsilon=\frac{2\lambda}{\beta+\tau}
 \begin{pmatrix}
 a[\theta+(1-\theta)\varepsilon]&\frac b s(1-\theta)(1-\varepsilon)\\
 sa(1-\theta)\varepsilon&b[\theta+(1-\theta)(1-\varepsilon)]
 \end{pmatrix}.
\]
For a fixed point \((u,w)\in[0,1)^2\), all six stationary compartments are reconstructed as
\[
 I_n=\frac{h_n\beta}{\beta+\tau}\varepsilon u,\quad Q_n=\varepsilon u-I_n,\quad S_n=\varepsilon(1-u),
\]
\[
 I_v=\frac{h_v\beta}{\beta+\tau}(1-\varepsilon)w,\quad Q_v=(1-\varepsilon)w-I_v,\quad S_v=(1-\varepsilon)(1-w).
\]
These reconstructed fractions are nonnegative and satisfy the complete stationary system.

**2. Uniqueness and existence for every positive minority share.** Set
\[
 D=1-1/R,\qquad B=D/s,\qquad C=s(R-1).
\]
Under the critical equalities the matrix becomes
\[
 M_\varepsilon=
 \begin{pmatrix}
 1+(R-1)\varepsilon&B(1-\varepsilon)\\
 C\varepsilon&1-D\varepsilon
 \end{pmatrix}.
\]
It is strictly positive for every \(0<\varepsilon<1\), and direct expansion gives
\[
 \det M_\varepsilon=1,\qquad
 \operatorname{tr}M_\varepsilon=2+\frac{(R-1)^2}{R}\varepsilon>2.
\]
Hence its Perron eigenvalue exceeds one. Define the coordinatewise strictly increasing map
\[
 F_\varepsilon(z)_i=\frac{(M_\varepsilon z)_i}{1+(M_\varepsilon z)_i}
\]
on the nonnegative quadrant. For a positive Perron eigenvector \(r\), \(F_\varepsilon(tr)>tr\) for sufficiently small \(t>0\), while \(F_\varepsilon(1,1)<(1,1)\). Monotone iteration produces a positive fixed point strictly inside the unit square. Every nonzero fixed point must be strictly positive because the matrix is positive.

The positive fixed point is unique. Indeed, if \(x,y>0\) are different fixed points, after exchanging them if necessary set \(\alpha=\max_i x_i/y_i>1\). At a coordinate attaining this maximum, monotonicity and **strict subhomogeneity** give
\[
 x_i=F_\varepsilon(x)_i\le F_\varepsilon(\alpha y)_i
 <\alpha F_\varepsilon(y)_i=\alpha y_i=x_i,
\]
a contradiction. The origin is a second, disease-free fixed point. No additional boundary or interior equilibria exist.

**3. Fractional-power asymptotics.** The two equilibrium equations are exactly
\[
 \frac{u^2}{1-u}=(R-1)\varepsilon u+B(1-\varepsilon)w,
\]
\[
 \frac{w^2}{1-w}+D\varepsilon w=C\varepsilon u.
\]
Put \(t=\varepsilon^{1/3}\), \(u=tU\), \(w=t^2W\). After dividing the first equation by \(t^2\) and the second by \(t^4\), we obtain
\[
 \frac{U^2}{1-tU}=(R-1)t^2U+B(1-t^3)W,
\]
\[
 \frac{W^2}{1-t^2W}+DtW=CU.
\]
At \(t=0\), the positive solution is uniquely
\[
 U_0=(B^2C)^{1/3}=\frac{R-1}{R^{2/3}s^{1/3}},
 \qquad W_0=(BC^2)^{1/3}=\frac{(R-1)s^{1/3}}{R^{1/3}}.
\]
The Jacobian of these two equations with respect to \((U,W)\) at \((0,U_0,W_0)\) is
\[
 \begin{pmatrix}2U_0&-B\\-C&2W_0\end{pmatrix},
 \qquad \det=4U_0W_0-BC=3BC>0.
\]
The ordinary implicit-function theorem therefore supplies smooth positive functions \(U(t)=U_0+O(t)\), \(W(t)=W_0+O(t)\) for all sufficiently small positive \(t\). They reconstruct a positive stationary solution, which by Step 2 is the **unique** endemic solution. Substitution gives both asserted expansions and that for \(P_\varepsilon\).

## Verification

The supplied `verify.py` independently constructs the critical two-by-two matrix and checks its exact symbolic trace and determinant. It also solves the two rational equilibrium equations with high precision for decreasing positive minority fractions, checks both original residuals, and records convergence of \(u_\varepsilon/\varepsilon^{1/3}\) and \(w_\varepsilon/\varepsilon^{2/3}\) to their analytical constants. The finite numerical cases are checks; the all-parameter result follows from the proof above.

For example, admissible parameters are
\[
 p_q=1/4,\quad \gamma_q=0,\quad \gamma_t=2/3,\quad
 \sigma_n=\sigma_v=0,\quad \lambda=1,\quad\beta=\tau=1/4,\quad\theta=1/3.
\]
They give \(R=3\), \(s=1/3\) and
\[
 u_\varepsilon\sim \frac{2}{3^{1/3}}\varepsilon^{1/3},\qquad
 w_\varepsilon\sim\frac{2}{3^{2/3}}\varepsilon^{2/3}.
\]

## Relationship to prior work

Frieswijk, Zino, and Cao [1] introduced the polarized activity-driven SIQS system, derived the large-population equations and an exact infection-invasion threshold. The 2023 version analyzes endemic equilibria under the additional assumption that vaccinated infectious people are fully responsible (\(\sigma_v=1\)); this suppresses the vaccinated-to-others infectious contact pathway and is outside the present strictly positive coupling assumption. The theorem here analyzes the fully coupled nonlinear equilibrium at a jointly critical, diminishing-minority limit, rather than rederiving their threshold.

Hiraoka and coauthors [2] derived a next-generation-matrix herd-immunity threshold under vaccination homophily, including the qualitative possibility of epidemic spread in a very small unvaccinated group. Their model and results concern a static-network SIR/percolation final-size question, not the specified SIQS endemic equilibrium or its cubic-root and two-thirds-power prevalence laws. Wang and coauthors [3] analyzed existence and stability of endemic states in a different controlled SIS model; their general methods motivate the uniqueness comparison, not these fractional-power constants. Existing epidemic-threshold results alone do not imply the nonlinear stationary asymptotics here.

## Limitations

The mean-field limit is taken before letting the minority fraction vanish; for fixed finite population size the number of nonvaccinated people cannot be arbitrarily small while remaining positive, and the stochastic epidemic can go extinct. The two critical tuning equations are essential: perturbing the recovery/testing combination or homophily can change the powers. The result does not cover permanently immune SIR outbreaks, adaptive vaccination choice, heterogeneous individual contact activity, or claim global stability or a particular basin of the endemic equilibrium. Bibliographic comparisons are nonexhaustive, and no independent scientific validation is claimed.

## References

[1] K. Frieswijk, L. Zino, and M. Cao, *A Polarized Temporal Network Model to Study the Spread of Recurrent Epidemic Diseases in a Partially Vaccinated Population*, arXiv:2209.08045 (first public 2022-09-16), especially mean-field equations and epidemic threshold; IEEE Transactions on Network Science and Engineering (2023), DOI: 10.1109/TNSE.2023.3272472.

[2] T. Hiraoka, A. K. Rizi, M. Kivelä, and J. Saramäki, *Herd Immunity and Epidemic Size in Networks with Vaccination Homophily*, arXiv:2112.07538 (2021); Physical Review E 105, L052301 (2022).

[3] Y. Wang, S. Gracy, H. Ishii, and K. H. Johansson, *Suppressing the endemic equilibrium in SIS epidemics: A state dependent approach*, arXiv:2106.00122 (2021).
