# Two logarithmic edge-leakage laws for maxima in a switching harmonic trap

## Finding

For the stationary one-dimensional switching-harmonic-trap gas defined below, let \(M_N\) be the rightmost position among \(N\) particles. Write \(L_N=\log N\) and set
\[
B_N=\sqrt{2L_N}-\frac{\log L_N+\log(4\pi)}{2\sqrt{2L_N}},\qquad A_N=\frac1{\sqrt{2L_N}}.
\]
The leading law of \(M_N/\sqrt{2\log N}\) is supported on \([\sqrt a,\sqrt b]\), where \(a=D/\mu_1<b=D/\mu_2\). Yet the finite-particle probabilities of falling below or exceeding the corresponding Gaussian edge thresholds have distinct, **exact logarithmic asymptotics**.

Define \(R_1=r_1/(2\mu_1)\), \(R_2=r_2/(2\mu_2)\), \(r_H=2r_1r_2/(r_1+r_2)\), and
\[
c=\frac{\Gamma(1+R_1+R_2)}{\Gamma(1+R_1)\Gamma(1+R_2)},\quad
H_- =\frac{cr_H}{4\mu_1},\quad H_+=\frac{cr_H}{4\mu_2},
\quad k_- =\frac ba-1,\quad k_+=1-\frac ab.
\]
For every fixed \(y\in\mathbb R\),
\[
\boxed{\lim_{N\to\infty}(\log N)^{R_1}\Pr\big\{M_N\le\sqrt a(B_N+A_Ny)\big\}=
H_-\int_0^\infty w^{R_1-1}\exp\{-\exp(-y+k_-w)\}\,dw,}
\tag{1}
\]
\[
\boxed{\lim_{N\to\infty}(\log N)^{R_2}\Pr\big\{M_N>\sqrt b(B_N+A_Ny)\big\}=
H_+\int_0^\infty w^{R_2-1}\left[1-\exp\{-\exp(-y-k_+w)\}\right]dw.}
\tag{2}
\]
Both limits are finite and strictly positive. In particular, the two leakage probabilities decay as generally different powers of \(\log N\), not as powers of \(N\).

There is also **endpoint localization of the shared trap environment**. Let \(U\in(0,1)\) be the stationary variance-mixing variable defined below. Conditional on the lower-edge event in (1), \((\log N)U\) converges in distribution to a variable with density
\[
\frac{w^{R_1-1}\exp\{-\exp(-y+k_-w)\}}
{\int_0^\infty s^{R_1-1}\exp\{-\exp(-y+k_-s)\}\,ds},\qquad w>0.
\tag{3}
\]
Conditional on the upper-edge event in (2), \((\log N)(1-U)\) converges to the density
\[
\frac{w^{R_2-1}[1-\exp\{-\exp(-y-k_+w)\}]}
{\int_0^\infty s^{R_2-1}[1-\exp\{-\exp(-y-k_+s)\}]\,ds},\qquad w>0.
\tag{4}
\]
These conditional limits pinpoint a \(1/\log N\)-wide range of effective trap variances underlying each rare edge event.


**Literal edges of the leading compact support.** The Gumbel-centered upper threshold above is slightly inside the unshifted endpoint \(\sqrt{2b\log N}\). For events defined at the **literal, unshifted support endpoints**, the theorem also yields the following sharper, qualitatively different laws:
\[
\boxed{\Pr\big\{M_N\le \sqrt{2a\log N}\big\}\sim
\frac{H_-}{R_1(2k_-)^{R_1}}
\left(\frac{\log\log N}{\log N}\right)^{R_1},}
\tag{LE}
\]
\[
\boxed{\Pr\big\{M_N>\sqrt{2b\log N}\big\}\sim
\frac{H_+\Gamma(R_2)}{\sqrt{4\pi}\,k_+^{R_2}}
(\log N)^{-R_2-1/2}.}
\tag{UE}
\]
Hence the lower endpoint has a \(\log\log N\) enhancement, while *genuine exceedance above the leading upper support* pays an additional factor \((\log N)^{-1/2}\). This difference originates in the logarithmic correction to a Gaussian maximum and is not detected by the first-order compact-support limit.


As a concrete parameter illustration, let \(\mu_1=2\), \(\mu_2=1\), \(r_1=4\), \(r_2=2\), and \(D=1\). Then \(R_1=R_2=1\), \(a=1/2\), \(b=1\), and the literal-edge laws simplify to
\[
\Pr\{M_N\le\sqrt{\log N}\}\sim\frac{\log\log N}{3\log N},\qquad
\Pr\{M_N>\sqrt{2\log N}\}\sim\frac4{3\sqrt\pi}(\log N)^{-3/2}.
\]

## Assumptions and scope

Fix \(D>0\), \(\mu_1>\mu_2>0\) and \(r_1,r_2>0\), independently of \(N\). The \(N\) particle coordinates solve
\[
dX_i(t)=-\mu_{S(t)}X_i(t)\,dt+\sqrt{2D}\,dW_i(t),\quad i=1,\ldots,N,
\]
with independent standard Brownian motions \(W_i\). The shared two-state trap \(S\) switches from state 1 to state 2 at rate \(r_1\), and from 2 to 1 at rate \(r_2\), independently of the noises. All probabilities refer to a simultaneous stationary observation, and \(M_N=\max_i X_i\). There is no position resetting or interaction between particles.

The published exact stationary representation (Biroli–Kulkarni–Majumdar–Schehr, equations (12)–(13)) states that, conditionally on a common \(U=u\), the positions are independent centered Gaussians of variance \(v(u)=a+(b-a)u\), while \(U\) has the normalized density
\[
h(u)=\frac{cr_H}{4}u^{R_1-1}(1-u)^{R_2-1}\left(\frac{1-u}{\mu_1}+\frac{u}{\mu_2}\right),\qquad 0<u<1.
\tag{5}
\]
The definitions and claims above make sense for arbitrary positive, not necessarily integral, \(R_1,R_2\). For example, \(R_j<1\) produces an integrable singularity of \(h\) at the corresponding endpoint. The contrast \(b-a\) is assumed strictly positive.

## Proof

**1. Exact finite-\(N\) distribution.** Let \(\Phi\) and \(\bar\Phi=1-\Phi\) be the standard normal distribution function and survival function. Conditioning on \(U\) in (5) gives the *exact* identity
\[
Q_N(t):=\Pr(M_N\le t)=\int_0^1 h(u)\,\Phi\!\left(\frac{t}{\sqrt{v(u)}}\right)^Ndu.\tag{6}
\]
The coefficient \(h(u)\) behaves as \(H_-u^{R_1-1}\) at zero and as \(H_+(1-u)^{R_2-1}\) at one. To check its normalization directly, insert the two beta integrals in (5) and use \(R_1\mu_1=r_1/2\), \(R_2\mu_2=r_2/2\); the answer is one. Consequently (6) describes a probability law.

**2. Conditional Gaussian extreme limit.** Mills' ratio gives, for any fixed real \(z\),
\[
N\bar\Phi(B_N+A_Nz)\longrightarrow e^{-z},\qquad
\Phi(B_N+A_Nz)^N\longrightarrow G(z):=e^{-e^{-z}}.\tag{7}
\]
The second-order \(\log\log N\) correction in \(B_N\) is necessary: retaining only \(\sqrt{2\log N}\) would make the nontrivial functions in (1)–(2) disappear.

**3. Lower endpoint.** Substitute \(t=\sqrt a(B_N+A_Ny)\) and \(u=w/L_N\) into (6). Since \(v(u)=a(1+k_-u)\), uniformly on each bounded \(w\)-interval,
\[
\frac{t}{\sqrt{v(w/L_N)}}=B_N+A_N\big(y-k_-w+o(1)\big).
\]
Equations (5) and (7), together with \(du=dw/L_N\), yield the pointwise integrand in (1) after multiplication by \(L_N^{R_1}\).

To justify integration to infinity, choose a fixed small \(\varepsilon>0\). On \(0\le u\le\varepsilon\), the Gaussian hazard inequality \(\bar\Phi(z')/\bar\Phi(z)\ge\exp((z^2-z'^2)/2)\) for \(0<z'\le z\) yields, for all sufficiently large \(N\),
\[
N\bar\Phi\!\left(\frac{t}{\sqrt{v(u)}}\right)
\ge C_y\exp(c_\varepsilon L_Nu).
\]
Here \(C_y,c_\varepsilon>0\) are fixed; the bound follows from \(N\bar\Phi(t/\sqrt a)\to e^{-y}\) and \(t^2/[2a]=L_N+O(\log L_N)\). Thus the \(N\)-fold CDF is bounded by \(\exp\{-C_y\exp(c_\varepsilon w)\}\), an integrable majorant after multiplication by \(w^{R_1-1}\). On \(u\ge\varepsilon\), monotonicity supplies a superexponential bound \(\exp\{-C\exp(cL_N)\}\), whose product with \(L_N^{R_1}\) vanishes. Dominated convergence proves (1).

**4. Upper endpoint.** Put \(t=\sqrt b(B_N+A_Ny)\) and \(u=1-w/L_N\). Here \(v(u)=b(1-k_+(1-u))\) and, on bounded \(w\)-intervals,
\[
\frac{t}{\sqrt{v(1-w/L_N)}}=B_N+A_N\big(y+k_+w+o(1)\big).
\]
Using (7) in \(1-Q_N(t)\) gives the integrand in (2). For domination, the elementary union bound gives
\[
1-\Phi(z)^N\le\min(1,N\bar\Phi(z)).
\]
For \(z\ge z_0>0\), Gaussian hazard monotonicity implies \(\bar\Phi(z)/\bar\Phi(z_0)\le\exp(-(z^2-z_0^2)/2)\). For the present \(z=t/\sqrt{v(u)}\) and \(z_0=t/\sqrt b\), the difference is at least \(cL_N(1-u)\) for sufficiently large \(N\). Consequently the union bound is \(Ce^{-cw}\). Multiplication by \(w^{R_2-1}\) is integrable; the factor at \(u=0\) is handled by splitting off \(u\le1-\varepsilon\), where the probability is exponentially small in \(L_N\). Dominated convergence proves (2).

**5. Conditional trap localization and nondegeneracy.** Insert a bounded continuous test function of \(L_N U\), respectively \(L_N(1-U)\), in the corresponding numerator from (6). The same changes of variables and dominators give convergence to the integrals with the test function inserted. Division by the strictly positive limits (1)–(2) yields (3)–(4). The lower integral has a doubly exponentially damped tail, whereas the upper has an exponentially damped tail; both are integrable near zero since \(R_1,R_2>0\). All constants are therefore finite and positive.


**6. Unshifted support endpoints.** For \(t=\sqrt{2bL_N}\), the normal tail satisfies \(\sqrt{L_N}N\bar\Phi(\sqrt{2L_N})\to(4\pi)^{-1/2}\). In the upper endpoint window \(1-u=w/L_N\), a Mills-ratio calculation gives
\[
\sqrt{L_N}N\bar\Phi\!\left(\frac{t}{\sqrt{v(1-w/L_N)}}\right)
\longrightarrow (4\pi)^{-1/2}e^{-k_+w}.
\]
Moreover, \(N\bar\Phi(t/\sqrt{v(u)})=O(L_N^{-1/2})\) uniformly in \(u\), so \(1-(1-\bar\Phi)^N\sim N\bar\Phi\) uniformly wherever its nonzero contribution concentrates. The upper-endpoint Gaussian hazard bound in step 4 supplies an integrable exponential majorant after multiplying by \(\sqrt{L_N}\). Integration with the endpoint weight \(H_+w^{R_2-1}\) gives \(H_+\Gamma(R_2)/(\sqrt{4\pi}k_+^{R_2})\), proving (UE).

For \(t=\sqrt{2aL_N}\), introduce \(w=L_Nu\). Uniformly for \(w=O(\log L_N)\), Mills' ratio yields
\[
N\bar\Phi\!\left(\frac{t}{\sqrt{v(w/L_N)}}\right)
=(1+o(1))(4\pi L_N)^{-1/2}e^{k_-w}.
\]
For each fixed \(0<\epsilon<1\), the conditional maximum CDF converges uniformly to one on \(0\le w\le(1-\epsilon)\log L_N/(2k_-)\), while it is bounded by \(\exp\{-cL_N^{\epsilon/2}\}\) for \(w\ge(1+\epsilon)\log L_N/(2k_-)\). Endpoint mass satisfies \(\int_0^x h(u)du\sim H_-x^{R_1}/R_1\) as \(x\downarrow0\). The two cutoffs therefore sandwich \(\Pr\{M_N\le\sqrt{2aL_N}\}\) between endpoint masses with multiplicative factors \((1-\epsilon)^{R_1}\) and \((1+\epsilon)^{R_1}\), up to negligible remainders. Letting \(\epsilon\downarrow0\) proves (LE). No extension of the fixed-\(y\) limits (1)–(2) to growing \(y\) is assumed in this separate argument.

## Verification

The accompanying standalone `verify.py` evaluates the finite-particle Gaussian-mixture formula (6) numerically with an endpoint-adapted full-interval quadrature, compares it with both crossover integrals (1)–(2) and nominal-edge laws (LE)–(UE), and checks normalization of (5) for three independent parameter sets. It uses stable normal survival-function calculations and logarithmic sample sizes \(\log N=120,400,1200\). Execution produced **123 passing normalization, positivity, and large-sample edge checks**. These computations are numerical corroboration, not substitutes for the preceding uniform bounds. Execute with `python verify.py` using Python, NumPy, and SciPy.

## Relationship to prior work

Biroli, Kulkarni, Majumdar, and Schehr (arXiv:2312.02570, December 2023), including the supplement's section on order statistics, derive the exact Gaussian variance-mixture representation (5) and the *leading* compactly supported large-\(N\) distribution of \(M_N/\sqrt{2\log N}\). That leading result uses a delta approximation for the conditional maximum and does not retain its order-\(1/\sqrt{\log N}\) Gumbel fluctuations. Equations (1)–(4) and (LE)–(UE) address the nonuniform regime where this approximation cannot resolve either the Gaussian-centered crossover, the literal support leakage probability, or the conditional environment, and introduce a necessary second-order extreme-value centering. The earlier Biroli–Larralde–Majumdar–Schehr paper (arXiv:2307.15351) establishes leading conditional-independent-mixture extreme statistics in other correlated models. Huser, Opitz, and Thibaud (arXiv:1610.04536) study fixed-dimensional tail-dependence structure of Gaussian scale mixtures, not this simultaneous-growing-\(N\) compact-edge regime. Generic Gaussian-extreme and endpoint-regular-variation ingredients are standard and are not claimed to be independently new.

## Limitations

The result applies to fixed strictly positive switching rates and two fixed *distinct* positive trap stiffnesses. It is an asymptotic as the number of particles tends to infinity for fixed \(y\); no uniformity for \(y\) growing with \(N\) or across vanishing trap contrast is asserted. It concerns a stationary one-time spatial maximum, not the maximum over a temporal trajectory. The numerical program cannot certify the infinite-particle claims. The formulas derive from the published Gaussian mixture and could also be implied by an unlocated general random-environment extreme-value theorem; independent priority review has not been performed.

## References

1. M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570v1 (public 2023-12-05), especially Eqs. (12)–(16) and supplemental Eqs. (S74)–(S84). https://arxiv.org/abs/2312.02570
2. M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated systems*, arXiv:2307.15351v2 (2023), https://arxiv.org/abs/2307.15351
3. R. Huser, T. Opitz, E. Thibaud, *Bridging asymptotic independence and dependence in spatial extremes using Gaussian scale mixtures*, arXiv:1610.04536v2 (2016), https://arxiv.org/abs/1610.04536
