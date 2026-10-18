# A uniform imbalance clock and two-sided logarithmic selection delay near Leslie–Gower neutrality

## Finding

For the symmetric two-species Leslie–Gower competition map, a squared-odds observable has a perturbatively constant logarithmic increment **uniformly for all positive initial populations and all time horizons**. This identity yields explicit two-sided weak-competition first-passage laws, including a nontrivial sigmoid transition when the initial population imbalance vanishes simultaneously with the competition perturbation.

Let \(a>1\) and, for \(|\varepsilon|\le 1/2\), consider
\[
 x_{n+1}=\frac{a x_n}{1+x_n+(1+\varepsilon)y_n},\qquad
 y_{n+1}=\frac{a y_n}{1+y_n+(1+\varepsilon)x_n},
 \qquad x_0,y_0>0.
\]
Put \(s_n=x_n+y_n\), \(w_n=(x_n-y_n)/s_n\) and, when \(x_0\ne y_0\), \(U_n=w_n^2/(1-w_n^2)=(x_n-y_n)^2/(4x_ny_n)\). Write \(c=(a-1)/a\). For all \(n\ge0\),
\[
\boxed{\left|\log\frac{U_n}{U_0}-c\varepsilon n\right|
\le \frac{a}{a-1}\left|\frac1{s_0}-\frac1{a-1}\right||\varepsilon|
+\left(4+\frac1{a-1}\right)n\varepsilon^2.}\tag{1}
\]
Moreover \(U_n\) strictly increases if \(\varepsilon>0\), strictly decreases if \(\varepsilon<0\), and remains constant if \(\varepsilon=0\). Formula (1) stays informative on the logarithmically enhanced critical timescale \(n=O(|\varepsilon|^{-1}\log(1/|\varepsilon|))\), with error \(o(1)\).

For \(\varepsilon>0\), fix \(s_0>0\), \(\gamma>0\), \(d>0\), and choose the initial positive imbalance \(w_0=d\varepsilon^\gamma<1\). For each fixed \(\tau\in\mathbb R\), define
\[
 n_\varepsilon(\tau)=\left\lfloor\frac{2\gamma\log(1/\varepsilon)/c+\tau}{\varepsilon}\right\rfloor.
\]
Then, locally uniformly for \(\tau\) in compact sets,
\[
\boxed{\displaystyle
 \lim_{\varepsilon\downarrow0}w_{n_\varepsilon(\tau)}=
 \frac{d e^{c\tau/2}}{\sqrt{1+d^2e^{c\tau}}},\qquad
 \lim_{\varepsilon\downarrow0}s_{n_\varepsilon(\tau)}=a-1.}\tag{2}
\]
For every fixed threshold \(0<\kappa<1\), the first crossing \(N_\varepsilon(\kappa)=\min\{n\ge0:w_n\ge\kappa\}\) exists for sufficiently small \(\varepsilon>0\) and obeys
\[
\boxed{\displaystyle
 \varepsilon N_\varepsilon(\kappa)=
 \frac{2\gamma}{c}\log\frac1\varepsilon
 +\frac1c\log\frac{\kappa^2}{(1-\kappa^2)d^2}+o(1).}\tag{3}
\]
On the opposite side, set \(\varepsilon=-h<0\), fix \(s_0>0\) and initial \(w_0=w\in(0,1)\), and define \(M_h(d,\gamma)=\min\{n\ge0:w_n\le d h^\gamma\}\). Then
\[
\boxed{\displaystyle
 h M_h(d,\gamma)=
 \frac{2\gamma}{c}\log\frac1h
 +\frac1c\log\frac{w^2}{(1-w^2)d^2}+o(1).}\tag{4}
\]
Also, at \(m_h(\tau)=\lfloor(2\gamma\log(1/h)/c+\tau)/h\rfloor\),
\[
 \lim_{h\downarrow0}\frac{w_{m_h(\tau)}}{h^\gamma}
 =\frac{w}{\sqrt{1-w^2}}e^{-c\tau/2},
\]
locally uniformly in \(\tau\). Thus the instability and stability sides of neutrality have the same leading logarithmic waiting time, but distinct normalized transition profiles.

## Assumptions and scope

The real parameter \(a>1\) is fixed; the two species share the same growth parameter and the same cross-competition coefficient. Every initial state considered has \(x_0,y_0>0\). For the drift bound \(0<|\varepsilon|\le1/2\) and \(x_0\ne y_0\); the case \(\varepsilon=0\) is interpreted directly. The asymptotic statements let \(\varepsilon\to0\) with \(a,s_0,\gamma,d,\kappa,w\) fixed as stated; \(d\varepsilon^\gamma<1\) or \(dh^\gamma<w\) is required to define the corresponding initial state or nontrivial threshold. The identity is symmetric under exchanging species. Logs are natural.

At exact neutrality, the total density satisfies the scalar Beverton–Holt recurrence \(s_{n+1}=a s_n/(1+s_n)\); the composition \(w_n\) is conserved and every positive split of total mass \(a-1\) is a fixed point. For nonzero perturbation, this formerly neutral composition coordinate changes slowly.

## Proof

**1. Exact multiplicative imbalance identity.** Abbreviate \(A=1+x+y\) and write the next state as \(x'=ax/(A+\varepsilon y)\), \(y'=ay/(A+\varepsilon x)\). Subtraction gives
\[
 x'-y'=\frac{a(x-y)(A+\varepsilon(x+y))}{(A+\varepsilon x)(A+\varepsilon y)}.
\]
Since \(4x'y'=4a^2xy/[(A+\varepsilon x)(A+\varepsilon y)]\), it follows **exactly** that
\[
\frac{U'}U=\frac{(1+\varepsilon r)^2}
 {(1+\varepsilon r_x)(1+\varepsilon r_y)},\qquad
 r=\frac{x+y}{1+x+y},\quad r_x=\frac{x}{1+x+y},\quad r_y=\frac{y}{1+x+y},\quad r_x+r_y=r.
\tag{5}
\]
The numerator minus denominator in the normalized expression (5) equals
\[
\varepsilon r+\varepsilon^2(r^2-r_xr_y)
=\varepsilon\{r+\varepsilon(r^2-r_xr_y)\}.
\]
Here \(0<r<1\), \(0<r_x,r_y<r\) and \(0<r^2-r_xr_y\le r^2<r\). Thus the bracket is positive for \(|\varepsilon|\le1/2\), proving all claimed strict monotonicity statements. The signs of \(w_n\) and \(x_n-y_n\) never change.

**2. Uniform log-drift estimate.** The elementary inequality
\[
 |\log(1+z)-z|\le z^2\qquad(|z|\le1/2)
\]
combined with (5) gives
\[
 \left|\log\frac{U_{n+1}}{U_n}-\varepsilon r_n\right|
 \le (2r_n^2+r_{x,n}^2+r_{y,n}^2)\varepsilon^2
 \le 4\varepsilon^2.\tag{6}
\]
The total density has the two-sided scalar bound
\[
 \frac{a s_n}{1+(1+|\varepsilon|)s_n}
 \le s_{n+1}\le
 \frac{a s_n}{1+(1-|\varepsilon|)s_n}.
\]
For \(t_n=1/s_n\), this becomes
\[
 \left|t_{n+1}-\frac{t_n+1}{a}\right|\le\frac{|\varepsilon|}{a}.
\]
The neutral inverse-density fixed point is \(t_*=1/(a-1)\). Iteration yields
\[
 |t_n-t_*|\le a^{-n}|t_0-t_*|+\frac{|\varepsilon|}{a-1}.
\tag{7}
\]
Since \(r_n=1/(1+t_n)\), \(c=1/(1+t_*)\), and the function \(t\mapsto(1+t)^{-1}\) is 1-Lipschitz on nonnegative reals,
\[
 \sum_{j=0}^{n-1}|r_j-c|
 \le\frac{a}{a-1}|t_0-t_*|+\frac{n|\varepsilon|}{a-1}.
\]
Summing (6) and using this bound proves (1) for all integers \(n\ge0\), with no asymptotic hypothesis or lower bound on \(U_0\).

**3. Positive-perturbation sigmoid.** With \(w_0=d\varepsilon^\gamma\),
\[
 U_0=\frac{d^2\varepsilon^{2\gamma}}{1-d^2\varepsilon^{2\gamma}}
 =d^2\varepsilon^{2\gamma}(1+o(1)).
\]
Uniformly on compact \(\tau\)-sets, the right side of (1) at time \(n_\varepsilon(\tau)\) is \(O(\varepsilon\log(1/\varepsilon))\), because the initial total density is fixed. The integer part contributes only \(O(\varepsilon)\). Therefore
\[
 \log U_{n_\varepsilon(\tau)}=\log d^2+c\tau+o(1),
\]
uniformly on compact \(\tau\)-sets. Inversion of \(U=w^2/(1-w^2)\), with positive \(w\), gives the first limit (2). Formula (7) ensures \(s_{n_\varepsilon(\tau)}\to a-1\) uniformly as well. The sigmoid limit, or directly (1), shows that every \(0<\kappa<1\) is crossed for sufficiently small \(\varepsilon\); strict monotonicity makes the first crossing well-defined. Since the one-step variation of \(\log U\) is \(O(\varepsilon)\) uniformly, the discrete overshoot is \(o(1)\), and substituting \(U=\kappa^2/(1-\kappa^2)\) into (1) proves (3).

**4. Negative-perturbation selection.** Let \(h=-\varepsilon>0\) and \(w_0=w\in(0,1)\). At times \(m_h(\tau)\), (1) similarly implies
\[
 \log U_{m_h(\tau)}=\log\frac{w^2}{1-w^2}
 -2\gamma\log(1/h)-c\tau+o(1).
\]
Hence \(U_{m_h(\tau)}/h^{2\gamma}\to [w^2/(1-w^2)]e^{-c\tau}\); because \(U_{m_h(\tau)}\to0\), the asserted rescaled composition follows. Strict decrease and the uniform one-step logarithmic estimate give the first passage (4), again with an \(o(1)\) overshoot. These arguments also show that the specified first-passage times are finite for all sufficiently small \(h\).

## Verification

The standalone `verify.py` implements the map separately from the symbolic derivation. It checks (5) and the strict sign of its multiplier using **60 exact rational cases** (three growth parameters, five signed perturbations, four positive states); the log-drift bound (1) at **14,448 finite states** covering positive and negative perturbations; and **16 numerical first-passage trajectories** at four shrinking perturbation magnitudes on both sides of neutrality. Its successful execution returns:

`VERIFY_OK: 60 exact rational multiplier/sign identities; 14448 finite drift-bound checks; 16 crossover first-passage trajectories`

These are exact finite identity checks and finite numerical corroborations only. The estimates (5)–(7) and limiting arguments above, rather than the experiments, establish the all-time and asymptotic claims. To reproduce, run `python verify.py` with Python 3 using only its standard library.

## Relationship to prior work

Cushing, Levarge, Chitnis and Henson (2004) analyze the underlying two-species Leslie–Gower competition map (their equations (1)–(2)) and classify globally attracting coexistence and exclusion scenarios. Their full manuscript gives equilibrium and basin results, rather than a uniform logarithmic imbalance clock or the near-neutral logarithmic first-passage constants derived here. The neutral continuum and classical stability exchange are therefore not presented as new. The 2012 Chow–Hsieh general Beverton–Holt competition paper is potentially relevant to broad stability theory, but its full text was not accessible during this examination; no assertion that its body excludes these quantitative laws is made. The present result is a parameter-dependent **time-resolved** theorem in a symmetric specialization of the classical competition map. A general prior perturbation theorem could potentially subsume it, so historical priority remains a qualified claim rather than a certification.

## Limitations

Only the symmetric two-species rational map and fixed \(a>1\) are treated. The all-time bound is proved for \(|\varepsilon|\le1/2\); the asymptotic critical-window laws require \(\varepsilon\to0\) with the stated fixed initial-density data. The result does not provide stochastic demographic-noise selection times, unequal intrinsic growth rates, arbitrary multispecies competition, or a universal normal-form theorem. In particular, no conclusion about historical novelty follows solely from unsuccessful searches or from the availability of only an abstract for a possibly related paper. The asymptotic limits have no separately proved universal optimal convergence rate beyond the estimates displayed.

## References

1. J. M. Cushing, S. Levarge, N. Chitnis and S. M. Henson, *Some Discrete Competition Models and the Competitive Exclusion Principle*, Journal of Difference Equations and Applications 10 (2004), 1139–1151. DOI: `10.1080/10236190410001652739`. Author-hosted complete manuscript: https://www.andrews.edu/~henson/DiscreteCompetitionModels.pdf . Institutional record (2004-11-01): https://digitalcommons.andrews.edu/pubs/2086/ .
2. Y. Chow and J. Hsieh, *On multidimensional discrete-time Beverton–Holt competition models*, Journal of Difference Equations and Applications (first published online 2012-02-10). DOI: `10.1080/10236198.2012.656618`. Full text not available in this examination; any comparison is limited to accessible bibliographic/abstract material.
3. S. Kalabušić, M. R. S. Kulenović, E. Pilav and E. Silić, *Dynamics of a two-dimensional system of rational difference equations of Leslie–Gower type*, Advances in Difference Equations (2011), article 29. DOI: `10.1186/1687-1847-2011-29`. Its different competition map supplies context rather than implying the specific near-neutral estimates above.
