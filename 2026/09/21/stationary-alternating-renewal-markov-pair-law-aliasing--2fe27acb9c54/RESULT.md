# Stationary alternating-renewal processes can exactly mimic Markov two-time laws

## Result

Consider a stationary alternating renewal process \(X(t)\in\{0,1\}\). Successive state-1 sojourns are iid with strictly positive distribution \(F_1\), successive state-0 sojourns are iid with strictly positive distribution \(F_0\), and all sojourns are independent. Write
\[
\mu_i=\mathbb E T_i\in(0,\infty),\qquad M=\mu_0+\mu_1,
\qquad p=\Pr\{X(t)=1\}=\frac{\mu_1}{M},
\]
and let
\[
\phi_i(s)=\mathbb E e^{-sT_i},\qquad
r_i(s)=\frac{\phi_i(s)}{1-\phi_i(s)},\qquad s>0.
\]
Let \(C(t)=\operatorname{Cov}(X(0),X(t))\) and \(\widetilde C(s)=\int_0^\infty e^{-st}C(t)\,dt\).

Then the entire stationary second-order law identifies exactly the sum of the two renewal transforms:
\[
\boxed{
\widetilde C(s)=\frac{p(1-p)}{s}
-\frac{1}{M s^2}\frac{1}{1+r_0(s)+r_1(s)}
}
\tag{1}
\]
and, conversely, \(p\) and \(C\) determine \(M\) and \(r_0+r_1\). Indeed, because strictly positive sojourns satisfy \(\phi_i(s)\to0\) as \(s\to\infty\),
\[
\boxed{
\frac1M=\lim_{s\to\infty}s^2\left(\frac{p(1-p)}s-\widetilde C(s)\right)
}
\tag{2}
\]
and therefore
\[
\boxed{
r_0(s)+r_1(s)
=\left[M s^2\left(\frac{p(1-p)}s-\widetilde C(s)\right)\right]^{-1}-1.}
\tag{3}
\]
Thus second-order information generally cannot separate the two sojourn laws: it identifies their renewal-transform sum, not the two summands.

This non-identifiability persists even at the strongest-looking Markov benchmark. For every pair \(a,b>0\), the stationary two-state continuous-time Markov chain with state-1 holding time \(\operatorname{Exp}(a)\) and state-0 holding time \(\operatorname{Exp}(b)\) has a genuinely non-Markov alternating-renewal counterpart with exactly the same stationary two-time distribution at every lag.

The counterpart can be chosen as follows:

- state 1: \(T_1\sim\operatorname{Erlang}(2,2a)\), so \(\mathbb ET_1=1/a\);
- state 0: \(T_0\) is hyperexponential with Laplace transform
\[
\boxed{
\phi_0(s)=\frac{(a+b)s+4ab}{s^2+(5a+b)s+4ab}.}
\tag{4}
\]

The denominator in (4) has distinct positive roots \(\alpha<\beta\) of
\[
x^2-(5a+b)x+4ab=0.
\]
Since this polynomial is negative at \(x=a+b\), one has \(\alpha<a+b<\beta\), and hence (4) is the genuine two-exponential mixture
\[
\phi_0(s)=w\frac{\alpha}{s+\alpha}+(1-w)\frac{\beta}{s+\beta},
\qquad
w=\frac{\beta-(a+b)}{\beta-\alpha}\in(0,1).
\]
It has mean \(1/b\).

For the Markov pair,
\[
r_1(s)=\frac a s,\qquad r_0(s)=\frac b s.
\]
For the non-Markov pair,
\[
\frac{\phi_1(s)}{1-\phi_1(s)}
=\frac a s-\frac a{s+4a},
\qquad
\frac{\phi_0(s)}{1-\phi_0(s)}
=\frac b s+\frac a{s+4a}.
\]
Therefore both models have exactly
\[
\boxed{r_0(s)+r_1(s)=\frac{a+b}{s}.}
\tag{5}
\]
Equation (1) gives, in both cases,
\[
\boxed{
C(t)=\frac{ab}{(a+b)^2}e^{-(a+b)t}.}
\tag{6}
\]
They also have the same stationary probability \(p=b/(a+b)\). Because a stationary binary process's two-time joint law is determined by \(p\) and \(C(t)\), all four probabilities \(\Pr\{X(0)=i,X(t)=j\}\) agree with those of the Markov chain for every \(t\ge0\). Equivalently, all stationary lag-\(t\) two-state transition matrices agree with the Markov semigroup.

Nevertheless, the constructed process is not Markov: its state-1 holding time is Erlang-2 rather than exponential. Its exit hazard after age \(x\) in state 1 is
\[
\frac{4a^2x}{1+2ax},
\]
which depends on the elapsed sojourn age.

Hence an exactly exponential autocovariance, an exactly Lorentzian spectrum, or even the complete family of stationary two-time transition probabilities does **not** certify memorylessness within the alternating-renewal class.

## Proof of the transform identity

A standard equilibrium alternating-renewal calculation gives
\[
\widetilde C(s)=\frac{p(1-p)}s
-\frac1{M s^2}
\frac{(1-\phi_0(s))(1-\phi_1(s))}{1-\phi_0(s)\phi_1(s)}.
\tag{7}
\]
This is the \(\{0,1\}\)-valued specialization of the equilibrium correlation formula in Akimoto (2023), Eq. (151).

Now
\[
1+r_0+r_1
=1+\frac{\phi_0}{1-\phi_0}+\frac{\phi_1}{1-\phi_1}
=\frac{1-\phi_0\phi_1}{(1-\phi_0)(1-\phi_1)},
\]
so (7) is exactly (1). The large-\(s\) limit of the final factor in (7) is one, proving (2); rearrangement then gives (3).

The explicit phase-type construction follows from direct algebra. For \(T_1\sim\operatorname{Erlang}(2,2a)\),
\[
\phi_1(s)=\frac{4a^2}{(s+2a)^2},
\qquad
r_1(s)=\frac{a}{s}-\frac{a}{s+4a}.
\]
Defining \(r_0(s)=b/s+a/(s+4a)\) and using \(\phi_0=r_0/(1+r_0)\) yields (4). The root argument above proves that (4) is a proper hyperexponential law. Adding the two renewal transforms gives (5), after which (6) follows from (1) by Laplace inversion.

## What second-order data can identify

The obstruction is exact rather than merely a counterexample. Equations (2)-(3) show that the second-order observational equivalence class consists precisely of all admissible decompositions of the identified function \(r_0+r_1\) into two renewal transforms having the already identified means \(\mu_0=(1-p)M\) and \(\mu_1=pM\).

There are useful identifiable submodels. If one of the two sojourn laws is known, the other is recovered by subtraction in (3) and \(\phi=r/(1+r)\). If the two sojourn laws are known a priori to be identical, then \(r_0=r_1=(r_0+r_1)/2\), so the common law is also identified. The unrestricted two-law model does not enjoy this property.

## Scientific significance

Two-state Markov models are often assessed through occupancy fractions, empirical autocorrelations, spectra, or lagged transition probabilities. The construction above shows that even perfect population knowledge of all such two-time quantities cannot distinguish a Markov telegraph process from a smooth non-Markov semi-Markov process. Higher-order or duration-sensitive information is indispensable.

The example is not a heavy-tail pathology: both alternative holding-time laws are finite-dimensional phase-type distributions with moments of every order.

## Prior literature and originality boundary

The forward equilibrium correlation transform is classical renewal theory; a recent explicit formula is Eq. (151) of Akimoto (2023). Lowen and Teich (1993) and later work study autocorrelation and spectra of alternating-renewal signals for specified waiting-time laws. Duffy, King and Malone (2007) show that much coarser long-range-dependence summaries can fail to distinguish substantially different on/off models. Statistical work such as Dewanji and Kalbfleisch (1987) estimates sojourn laws from substantially richer windowed path data.

To the best of our knowledge, the checked literature does not state the exact second-order equivalence-class reduction (3), nor the all-parameter phase-type construction (4)-(6) showing that a genuinely non-Markov stationary alternating-renewal process can have exactly the same two-time law at every lag as a two-state continuous-time Markov chain. The novelty claim is limited to those inverse/aliasing statements and the explicit construction, not to the forward correlation formula itself.

Residual originality risk remains because older reliability, random-telegraph, ion-channel, or semi-Markov literature may contain an equivalent inverse observation under different terminology.

## Limitations

The result concerns stationary alternating renewal processes with independent successive positive sojourns and finite state-specific means. It does not say that full sample paths are non-identifying: observed switching times immediately reveal non-exponential durations in the counterexample. It also does not address hidden-state observation error, dependence between successive sojourns, more than two states, or nonstationary initialization.

## Reproducibility

`artifacts/verify_symbolic.py` checks the renewal-transform cancellation, covariance transform, hyperexponential representation, and several positive parameter cases using symbolic and high-precision arithmetic. `artifacts/VERIFICATION.txt` records the verified output.

## References

1. T. Akimoto, “Statistics of the number of renewals, occupation times, and correlation in ordinary, equilibrium, and aging alternating renewal processes,” *Physical Review E* 108, 054113 (2023). DOI: https://doi.org/10.1103/PhysRevE.108.054113 ; arXiv: https://arxiv.org/abs/2306.00359
2. S. B. Lowen and M. C. Teich, “Fractal renewal processes generate 1/f noise,” *Physical Review E* 47, 992–1001 (1993). DOI: https://doi.org/10.1103/PhysRevE.47.992
3. K. Duffy, C. King, and D. Malone, “Ambiguities in estimates of critical exponents for long-range dependent processes,” *Physica A* 377, 43–52 (2007). DOI: https://doi.org/10.1016/j.physa.2006.11.015
4. A. Dewanji and J. D. Kalbfleisch, “Estimation of sojourn time distributions for cyclic semi-Markov processes in equilibrium,” *Biometrika* 74, 281–288 (1987). DOI: https://doi.org/10.1093/biomet/74.2.281
5. N. T. Argon, “Alternating Renewal Processes,” in *Wiley Encyclopedia of Operations Research and Management Science* (2011). DOI: https://doi.org/10.1002/9780470400531.eorms0025
