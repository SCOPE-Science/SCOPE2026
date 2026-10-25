# Exact reset-count and accumulated-distance law for one-sided Brownian smart resetting

## Finding

For the Brownian smart-reset search described below, the number \(N\) of *actual* negative-position returns before the target is reached has a geometric law. More strongly, the distances of successive actual returns, conditional on their occurrence, are independent exponentials whose rate is independent of the target distance. These two statements yield the complete joint law of the reset count and total return distance, including its atom at zero.

Fix \(D,r,L>0\) and set
\[
\kappa=\sqrt{r/D},\qquad p=\frac{1}{1+\kappa L},\qquad q=\frac{\kappa L}{1+\kappa L}=1-p.
\]
For every integer \(n\ge0\),
\[
\Pr(N=n)=p q^n.
\]
Conditional on \(N=n\), the total return distance \(C\) is Gamma distributed with shape \(n\) and rate \(\kappa\) when \(n\ge1\); for \(n=0\), \(C=0\). Equivalently, for \(0\le z\le1\) and \(s\ge0\),
\[
\mathbb E[z^N e^{-sC}]=\frac{p}{1-qz\kappa/(\kappa+s)}.
\]
This determines the mixed discrete-continuous law: \(\Pr(C=0)=p\), and on \(c>0\),
\[
 f_C(c)=pq\kappa\,e^{-p\kappa c},\qquad
 \Pr(C>c)=q e^{-p\kappa c}\quad(c\ge0).
\]
In particular, conditional on \(C>0\), \(C\) is exponential of rate \(p\kappa\); and conditional on \(C=c>0\), \(N-1\) is Poisson of mean \(q\kappa c\) (in the sense of a regular conditional law). The moments are
\[
\mathbb E C=L,\qquad \operatorname{Var}(C)=L^2+2L\sqrt{D/r},\qquad
\mathbb E C^m=\frac{q\,m!}{(p\kappa)^m}\quad(m\in\mathbb N,\ m\ge1).
\]
Thus a reset-rate-independent mean cost conceals a reset-rate-dependent fluctuation law. As \(r\downarrow0\), \(C\) tends to zero in probability although \(\mathbb EC=L\) at every positive rate; as \(r\to\infty\), \(C\) converges in distribution to an exponential variable of mean \(L\).

## Assumptions and scope

A particle begins at \(X_0=0\) on the real line, has motion \(dX_t=\sqrt{2D}\,dW_t\) between interventions, and is absorbed on first reaching the target \(L>0\). Independent Poisson monitoring times have intensity \(r>0\). At a monitoring time \(t\), the particle is instantaneously returned to zero *only* if \(X_{t-}<0\); at nonnegative positions the monitoring causes no change. There is no drift, delay during returns, additional thermal force, or cost of unsuccessful monitoring. The count \(N\) includes actual returns only, not all measurements. If an actual return occurs from \(-Y_j<0\), its distance cost is \(Y_j>0\), and \(C=\sum_{j=1}^N Y_j\), with \(C=0\) when \(N=0\). For constant force \(F_0>0\), the physical expenditure is \(F_0 C\), obtained by deterministic rescaling.

All formulas are exact for every \(D,r,L>0\), with no large-time or asymptotic approximation in the primary joint law. The boundary case \(r=0\) is excluded: it entails no resets and zero actual cost almost surely, despite the positive-rate mean limit being \(L\).

## Proof

**1. One-attempt stopping and the reset-depth transform.** Start at any \(x<L\). End one attempt at the earlier of hitting \(L\) and a negative-position Poisson observation (an actual reset). Let \(A\) denote the latter event; on \(A\) let \(Y=-X_{\tau-}>0\). For \(s\ge0\), set \(w_s(x)=\mathbb E_x[e^{-sY}\mathbf1_A]\). Standard killed-diffusion/Feynman–Kac reasoning, or conditioning on the first observation in a small interval, gives the bounded solution of
\[
D w_s''(x)=0\quad(0<x<L),\qquad
D w_s''(x)-r w_s(x)=-r e^{sx}\quad(x<0).
\]
The boundary condition is \(w_s(L)=0\), and \(w_s\) and its first derivative match continuously at zero. Boundedness for \(x\to-\infty\), together with these conditions, uniquely specifies the transform (the resonant value \(s=\kappa\) follows continuously).

Indeed on \([0,L]\), \(w_s(x)=w_s(0)(1-x/L)\). For \(x<0\) and \(s\ne\kappa\),
\[
 w_s(x)=A_s e^{\kappa x}+\frac{\kappa^2}{\kappa^2-s^2}e^{sx}.
\]
Using continuity at zero to eliminate \(A_s\) gives
\[
 w_s'(0-)=\kappa w_s(0)-\frac{\kappa^2}{\kappa+s}.
\]
Matching this to \(w_s'(0+)=-w_s(0)/L\) proves
\[
\boxed{w_s(0)=\frac{\kappa^2L}{(1+\kappa L)(\kappa+s)}=q\frac{\kappa}{\kappa+s}.}
\]
In particular, one attempt ends in a reset with probability \(q=w_0(0)\) and reaches the target first with probability \(p=1-q\). Conditional on a reset, its depth has Laplace transform \(\kappa/(\kappa+s)\), hence \(Y\sim\operatorname{Exp}(\kappa)\). The identity is independent of \(L\) after conditioning on the reset event. An attempt ends almost surely: absent a negative observation, one-dimensional Brownian motion hits \(L\) in finite time almost surely.

**2. Renewal and complete joint law.** Every actual reset returns the process to \(0\), and the Brownian and Poisson processes have the strong Markov and memoryless properties. Thus attempts are independent and identically distributed. The probability of exactly \(n\) failures followed by a success is \(q^n p\), proving the geometric law. Because each failed attempt has exponential depth as above, the conditional joint distribution of its depths factors. Equivalently, one may couple the system to an independent geometric \(N\) and independent exponential variables \((Y_j)_{j\ge1}\) of rate \(\kappa\), with \(C\overset{d}=\sum_{j=1}^N Y_j\). This establishes the displayed joint generating/Laplace function and the conditional Gamma laws.

**3. Mixed marginal and posterior count.** Summing the Gamma densities for \(n\ge1\) gives
\[
\begin{aligned}
 f_C(c)&=\sum_{n\ge1} p q^n\frac{\kappa^n c^{n-1}}{(n-1)!}e^{-\kappa c}\\
 &=p q\kappa e^{-(1-q)\kappa c}=p q\kappa e^{-p\kappa c},\quad c>0.
\end{aligned}
\]
The missing mass is \(\Pr(N=0)=p\) at zero. Dividing the joint density at fixed \(n\ge1\) by \(f_C(c)\) gives \(\Pr(N=n\mid C=c)=e^{-q\kappa c}(q\kappa c)^{n-1}/(n-1)!\) for \(c>0\). The factorial moments of the exponential component yield all stated moments, including \(\mathbb EC=q/(p\kappa)=L\) and \(\operatorname{Var}(C)=2q/(p\kappa)^2-L^2=L^2+2L/\kappa\).

**4. Singular rate limits.** If \(r\downarrow0\) then \(\kappa\downarrow0\) and \(\Pr(C>0)=q\to0\), so \(C\to0\) in probability. Nevertheless, \(\mathbb EC=L\) for each \(r>0\); the family is not uniformly integrable. For \(r\to\infty\), \(p\to0\), \(q\to1\), and \(p\kappa\to1/L\), so the positive exponential component converges to \(\operatorname{Exp}(1/L)\) and the atom vanishes. This proves the two limit laws.

## Verification

The accompanying `verify.py` independently generates Brownian trajectories between Poisson monitoring times using Gaussian increments; it uses the exact Brownian-bridge barrier crossing probability \(\exp[-(L-x)(L-y)/(D\Delta t)]\) to recognize target hits before a monitoring time. Thus first passage is not approximated by endpoint sampling. The program compares Monte Carlo reset frequencies, counts, mean depths, costs, variance, Laplace values and upper tails against the claimed laws at three well-separated rates. It also checks the matching derivatives and residuals of the boundary-value calculation and normalizations of the conditional law. Execute using `python verify.py` with NumPy installed. Finite simulation supports the proof, not a universal certification; the analytic boundary-value and renewal calculations establish all-parameter results.

## Relationship to prior work

Tal-Friedman, Keidar, Reuveni, and Roichman formulate precisely this one-sided Brownian smart-reset protocol. Their 2024 preprint and 2025 article compute its mean total linear distance cost \(\mathbb EC=L\) and the mean number of actual resets \(\mathbb EN=\kappa L\); Appendix C derives the integrated negative-side occupation kernel. Those results are adopted here, not claimed as new. The additional conclusion is the *joint* reset-count/cumulative-distance law, its exponential reset-depth structure, exact cost quantiles and fluctuations, conditional reset count, and singular weak-rate limit. The one-attempt killed-diffusion calculation supplies the missing path-level relation.

Sunil, Blythe, Evans, and Majumdar derive general renewal transforms for the number and cost of *unconditional* Poisson resetting; their displayed Brownian geometric count pertains to that distinct protocol. Their general renewal structure is methodologically relevant, but using it here requires the distinct one-sided killed Green function and an explicit reset-depth calculation. Plata, Gupta, and Azaele analyze asymmetric state-dependent resetting and mean first passage; their published analysis does not supply the displayed cumulative-distance joint law. Related stochastic-return work treats other return mechanisms and work observables. This comparison does not establish absolute priority: unlocated equivalent results remain a risk.

## Limitations

The joint law is not asserted for position-dependent observation intensity other than the specified half-line rate, asymmetric diffusion coefficients, drift, non-Poisson monitoring, finite-duration active returns during which other dynamics continue, multiple targets, or nonlinear cost functions. In particular, the exponential mixture applies to the *linear sum of return distances*, not generally to sums of nonlinear functions of those distances. No distributional assertion is made about full elapsed passage time or its correlation with \(C\). The no-reset limit does not commute with taking expectations; extrapolating the positive-rate mean law to \(r=0\) is invalid.

## References

1. O. Tal-Friedman, T. D. Keidar, S. Reuveni, Y. Roichman, *Smart Resetting: An Energy-Efficient Strategy for Stochastic Search Processes*, arXiv:2409.10108 (first publicly posted 2024-09-16); *Physical Review Research* **7**, 013033 (2025), DOI: 10.1103/PhysRevResearch.7.013033. Relevant text: main article Sec. II and Appendix C.
2. J. C. Sunil, R. A. Blythe, M. R. Evans, S. N. Majumdar, *The cost of stochastic resetting*, arXiv:2304.09348 (2023); *Journal of Physics A* **56**, 395001 (2023), DOI: 10.1088/1751-8121/acf3bb. Relevant text: Secs. 2-3 and renewal formulas.
3. C. A. Plata, S. Gupta, S. Azaele, *Asymmetric Stochastic Resetting: Modeling Catastrophic Events*, arXiv:2007.12417 (2020), model, MFPT and appendices.
4. S. Gupta, C. A. Plata, *Work fluctuations for diffusion dynamics submitted to stochastic return*, arXiv:2206.07618 (2022). Related work fluctuations with noninstantaneous return.
5. P. Singh, A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715 (2022). Related integral first-passage functionals under unconditional resetting.
