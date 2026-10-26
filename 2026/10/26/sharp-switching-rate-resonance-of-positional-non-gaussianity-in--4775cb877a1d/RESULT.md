# Sharp switching-rate resonance of positional non-Gaussianity in a two-stiffness harmonic trap

## Finding

Fix \(D>0\) and two positive harmonic relaxation coefficients \(a,b>0\). A particle evolves under equilibrium-strength white noise in a trap whose stiffness alternates at a common Poisson rate \(k>0\). Write \(M_j(k)=\mathbb E[X^j]\) for stationary positional moments. Define the *normalized Gaussian-excess parameter*
\[
Q(k)=\frac{M_4(k)}{3M_2(k)^2}-1.
\]
This convention is **one third** of conventional excess kurtosis \(M_4/M_2^2-3\), not that excess kurtosis itself.

The stationary law has the exact formula
\[
\boxed{Q(k)=\frac{(a-b)^2\,[4ab+3(a+b)k+2k^2]}{(a+b+2k)^2\,[4ab+(a+b)k]}.}
\]
If \(a\ne b\), both \(M_2\) and \(M_4\) are strictly decreasing functions of \(k\), yet the normalized observable has an interior maximum if and only if
\[
\boxed{\frac{\max(a,b)}{\min(a,b)}>3+2\sqrt2.}
\]
When this inequality holds, there is exactly one global maximizer \(k_*>0\), determined by the unique positive root of
\[
4ab[(a+b)^2-8ab]-16ab(a+b)k_*-5(a+b)^2k_*^2-2(a+b)k_*^3=0.
\]
When the ratio is at or below the threshold, \(Q(k)\) decreases strictly for every \(k>0\); at equality the derivative only vanishes in the excluded slow-switching limit. If \(a=b\), the positional law is Gaussian and \(Q(k)=0\) at every rate.

Thus sufficiently contrasting yet individually stable traps display enhanced *relative* non-Gaussianity at an intermediate switching rate while both unstandardized even moments fall monotonically.

## Assumptions and scope

Let \(S_t\in\{1,2\}\) be an irreducible stationary continuous-time Markov chain with generator \(\left(\begin{smallmatrix}-k&k\\k&-k\end{smallmatrix}\right)\). Let \(W_t\) be an independent two-sided standard Brownian motion. The scalar Itô equation is
\[
dX_t=-a_{S_t}X_t\,dt+\sqrt{2D}\,dW_t,\qquad a_1=a,\ a_2=b,
\]
with \(a,b,D,k>0\). All conclusions concern the unique long-time stationary law and exact population moments, not finite-time transients or estimators. The harmonic potential is \(V_i(x)=a_i x^2/2\) in units of unit mobility. The switching process does not reset position or directly impart impulses.

For any two initial positions coupled to the same noise and chain, their difference at time \(t\) is multiplied by \(\exp[-\int_0^t a_{S_u}\,du]\), whose magnitude is at most \(e^{-\min(a,b)t}\). A stationary solution exists via the convergent past integral
\[
X_t=\sqrt{2D}\int_{-\infty}^t \exp\!\left(-\int_s^t a_{S_u}\,du\right)\,dW_s.
\]
Conditional Gaussian variances are bounded by \(D/\min(a,b)\), ensuring finite moments of every order. This gives existence and uniqueness of the joint stationary process and justifies the generator moment identities below.

## Proof

Set \(u_i=\mathbb E[X^2\mathbf1_{\{S=i\}}]\) and \(v_i=\mathbb E[X^4\mathbf1_{\{S=i\}}]\). The stationary switching chain has probabilities \(1/2\) and \(1/2\). Applying Itô's formula and the two-state generator gives the exact systems
\[
\begin{pmatrix}2a+k&-k\\-k&2b+k\end{pmatrix}\binom{u_1}{u_2}=\binom D D,
\qquad
\begin{pmatrix}4a+k&-k\\-k&4b+k\end{pmatrix}\binom{v_1}{v_2}=12D\binom{u_1}{u_2}.
\]
Both matrices have strictly positive diagonal and positive determinants: \(4ab+2(a+b)k\) and \(16ab+4(a+b)k\), respectively. Direct inversion yields
\[
M_2(k)=\frac{D(a+b+2k)}{2ab+(a+b)k},\qquad
M_4(k)=\frac{6D^2[2a^2+2b^2+3(a+b)k+2k^2]}{[2ab+(a+b)k][4ab+(a+b)k]}.
\]
Substitution into \(M_4/(3M_2^2)-1\) and factorization give the displayed formula for \(Q\). Every denominator here is strictly positive for all stated parameters.

For \(a\ne b\), direct differentiation yields
\[
\frac{dM_2}{dk}=-\frac{D(a-b)^2}{[2ab+(a+b)k]^2}<0,
\]
and
\[
\frac{dM_4}{dk}=-\frac{6D^2(a-b)^2\{12ab(a+b)+4(a^2+4ab+b^2)k+3(a+b)k^2\}}{[2ab+(a+b)k]^2[4ab+(a+b)k]^2}<0.
\]
Write \(s=a+b>0\) and \(p=ab>0\), and define
\[
P(k)=4p(s^2-8p)-16psk-5s^2k^2-2sk^3.
\]
An exact derivative identity is
\[
\frac{dQ}{dk}=\frac{2(a-b)^2P(k)}{(s+2k)^3(4p+sk)^2}.
\]
The sign of the derivative is precisely the sign of \(P\). Crucially,
\[
P'(k)=-16ps-10s^2k-6sk^2<0\qquad(k\ge0).
\]
Furthermore \(P(k)\to-\infty\) as \(k\to\infty\), and \(P(0)=4p(s^2-8p)\). If \(s^2\le8p\), then \(P(k)<0\) for all \(k>0\). If \(s^2>8p\), the intermediate value theorem and strict monotonicity produce exactly one positive root; \(Q\) increases before it and decreases thereafter, giving a unique global maximizer. Finally \(s^2>8p\) is equivalent to \(a/b+b/a>6\), or \(\max(a,b)/\min(a,b)>3+2\sqrt2\). This proves sharpness including the equality case.

The exact limits are
\[
\lim_{k\downarrow0}Q(k)=\frac{(a-b)^2}{(a+b)^2},\qquad
Q(k)=\frac{(a-b)^2}{2(a+b)k}+O(k^{-2})\quad(k\to\infty).
\]
These follow by direct expansion of the rational expression. At \(a=b\) the drift is independent of the chain and the stationary law is the standard Gaussian Ornstein–Uhlenbeck equilibrium.

## Verification

The included standalone `check.py` recomputes the two moment systems symbolically, reconstructs \(Q\), checks both moment derivatives and the exact cubic derivative factorization, and verifies the threshold with contrasting exact-rational examples. In particular, for \(a=1,b=9,D=1\), the cubic is \(1008-1440k-500k^2-20k^3\), with its unique positive zero at approximately \(0.580341977711327\); \(Q(0)=16/25\) (the one-sided limit) and \(Q(1/4)=22336/33957>16/25\). These calculations corroborate, but do not substitute for, the analytic sign proof. Reproduce using `python check.py` with SymPy installed.

## Relationship to prior work

Kwon, Noh, and Park [1] give a rigorous physical framework for Brownian motion in a time-dependent harmonic force constant and study work fluctuations under prescribed protocols. This provides an archived physical starting point, but not symmetric Markov switching or a stationary spatial kurtosis switching-rate optimum.

Alston, Cocconi, and Bertrand [2] analyze general two-state switching harmonic traps and derive stationary second-moment and entropy-production identities (notably their Section 4, equations (31)–(39)); those results include the forward variance mechanism here. They do not state the normalized fourth-moment threshold or its unique critical switching rate.

Biroli, Kulkarni, Majumdar, and Schehr [3] obtain the full stationary joint distribution for two-state switched harmonic confinement, including arbitrary positive switching rates and a Gaussian-mixture representation, Equations (10)–(13). This is **stronger forward distributional coverage**, and contains the present model. Moreover, its main-text Equation (14) and supplementary Equations (S69), (S72), (S73) explicitly provide the second moment, the mixed fourth moment, and a cross-particle squared-moment covariance. Because the particles are conditionally independent Gaussian given the switching environment, the reported mixed fourth moment is exactly one third of the single-particle fourth moment; consequently the forward formula for \(Q\) is already implied by those published expressions. The distinct assertion investigated here is the global sharp sign classification for the *switching-rate derivative of a normalized fourth moment*, its universal stiffness ratio threshold and monotone-raw-moment contrast. That result requires the explicit fourth-moment elimination and derivative polynomial sign analysis; neither the threshold nor the peak classification is stated in the relevant main or supplementary discussions examined. The result is therefore offered as a specific sharp implication not identified in those distributional studies, not as a new forward stationary distribution. An undiscovered equivalent prior classification remains a priority risk.

## Limitations

This theorem requires two **strictly positive** stiffnesses, symmetric environment transition rates, common positive Gaussian noise strength, and one spatial dimension. An off state with zero or negative stiffness, unequal switching rates, non-Markov driving, measurement noise, finite-time sampling, or active propulsion need separate analysis. The phase classification is for the dimensionless normalized fourth-moment excess, not for conventional absolute kurtosis or entropy production. The slow-rate endpoint has a mixture limit; at exactly zero switching there are multiple environment-conditioned stationary laws, so no uniqueness claim is made there. The archived 2013 paper motivates the physical system; the sharper full-model studies [2] and [3] are later publications explicitly compared for novelty and priority. Independent external validation and empirical resolvability are not claimed.

## References

[1] C. Kwon, J. D. Noh, H. Park, *Work fluctuations in a time-dependent harmonic potential: rigorous results and beyond the overdamped limit*, arXiv:1303.6742v1, first public 2013-03-27. https://arxiv.org/abs/1303.6742

[2] H. Alston, L. Cocconi, T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630v1, first public 2022-02-05. https://arxiv.org/abs/2202.02630

[3] M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570v1, first public 2023-12-05. https://arxiv.org/abs/2312.02570
