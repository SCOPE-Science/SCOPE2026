# Two reentrant kurtosis regimes under Gaussian-distributed Ornstein–Uhlenbeck resets

## Finding

Consider a harmonically confined Brownian particle whose location is replaced at Poisson times by an independent Gaussian draw. For a fixed rate, varying the square of the mean reset displacement can change the sign of its stationary **fourth cumulant** twice: positive, then negative, then positive. There are exactly two disjoint reset-rate/width regimes in which this happens, and their boundaries are algebraic.

Write \(K_4=\mathbb E[(X-\mathbb EX)^4]-3\operatorname{Var}(X)^2\). Set \(q=r/\kappa>0\), \(v=D/\kappa>0\), and \(d=\sigma^2-v\). The complete formula is

\[
K_4=A(q)m^4+6B(q)m^2d+3C(q)d^2,
\]

where

\[
\begin{aligned}
A(q)&=\frac{6q(q^3-q^2-6q+2)}{(q+1)^4(q+2)^2(q+3)(q+4)},\\
B(q)&=-\frac{4q(q^2+q-3)}{(q+1)^2(q+2)^2(q+3)(q+4)},\\
C(q)&=\frac{4q}{(q+2)^2(q+4)}>0.
\end{aligned}
\]

Let \(a=0.321637174263296\ldots\) and \(b=2.85577250663599\ldots\) denote the positive roots of \(q^3-q^2-6q+2=0\). For \(d\ne0\), put \(t=m^2/|d|\ge0\). **Exactly two distinct positive roots**, and the \(+,-,+\) sign sequence as \(t\) increases, occur if and only if

\[
\big(0<q<a\ \text{and}\ d<0\big)\quad\text{or}\quad\big(q>b\ \text{and}\ d>0\big).
\]

If \(a<q<b\), precisely one positive root occurs (positive to negative), for either sign of \(d\). Every other open regime has no positive root and a strictly positive fourth cumulant. At \(q=a\) the unique positive root occurs only if \(d<0\), and at \(q=b\) only if \(d>0\). If \(d=0\), \(K_4=A(q)m^4\); thus it can vanish even for \(m\ne0\) at either special rate.

Because the stationary variance is positive, the same sign classification applies to the excess kurtosis \(K_4/\operatorname{Var}(X)^2\). Zero fourth cumulant is **not** a claim of a Gaussian stationary law.

## Assumptions and scope

Between independent, instantaneous resets, \(X_t\) solves \(dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t\), with \(\kappa>0,D>0\). Reset times form an independent Poisson process of rate \(r>0\); each reset assigns an independent real Gaussian \(N(m,\sigma^2)\), with \(m\in\mathbb R\), \(\sigma^2>0\). The thermal variance is \(v=D/\kappa\), and \(d=\sigma^2-v\) may have either sign, subject to \(v+d>0\). The claim concerns the unique invariant **one-time position distribution**; it does not concern dynamical entropy production, higher cumulants, or behavior under non-Poisson resetting.

## Proof

**Stationary renewal representation.** At a stationary observation time, the elapsed time \(T\) since the most recent reset is exponential with rate \(r\), independently of the fresh reset sample and subsequent Brownian noise. Define \(U=e^{-\kappa T}\). Directly,

\[
\mathbb P(U\le u)=u^q\quad(0<u<1),\qquad \mu_j:=\mathbb E[U^j]=\frac{q}{q+j}\quad(j\ge0).
\]

Solving the OU stochastic differential equation over this age gives

\[
X\mid(U=u)\sim N\big(mu,\ v+d u^2\big).
\]

This conditional variance is positive: it interpolates between \(v>0\) and \(\sigma^2>0\).

**Fourth cumulant.** Apply the law of total cumulance for a conditional Gaussian with conditional mean \(M=mU\) and conditional variance \(V=v+dU^2\):

\[
\kappa_4(X)=\kappa_4(M)+6\operatorname{Cov}\big((M-\mathbb EM)^2,V\big)+3\operatorname{Var}(V).
\]

Substituting \(\mu_j=q/(q+j)\) yields

\[
\begin{aligned}
A&=\mu_4-4\mu_1\mu_3+12\mu_1^2\mu_2-6\mu_1^4-3\mu_2^2,\\
B&=\mu_4-2\mu_1\mu_3+2\mu_1^2\mu_2-\mu_2^2,\\
C&=\mu_4-\mu_2^2.
\end{aligned}
\]

Elementary fraction reduction produces the stated rational \(A,B,C\). The \(v\)-only terms cancel, so the fourth cumulant depends only on \(q,m,d\). The stationary variance is \(m^2(\mu_2-\mu_1^2)+v+d\mu_2>0\).

**Complete root classification.** When \(d\ne0\), write \(\varepsilon=\operatorname{sgn}(d)\). Then

\[
\frac{K_4}{d^2}=P_{q,\varepsilon}(t)=A(q)t^2+6\varepsilon B(q)t+3C(q),\qquad t=\frac{m^2}{|d|}\ge0.
\]

Its discriminant is the strictly positive quantity

\[
\Delta(q)=36B(q)^2-12A(q)C(q)=\frac{288q^2(q^2-2q+3)}{(q+1)^4(q+2)^2(q+3)^2(q+4)^2}>0.
\]

The cubic \(h(q)=q^3-q^2-6q+2\) has exactly two positive zeros: its derivative \(3q^2-2q-6\) has one positive zero, so \(h\) decreases then increases on the positive half-line; also \(h(0)>0\), \(h(1)<0\), \(h(3)>0\). Call the zeros \(a<b\). Thus \(A>0\) outside \([a,b]\), \(A<0\) inside, and \(A=0\) at endpoints. In addition, \(B>0\) when \(q<c=(\sqrt{13}-1)/2\), and \(B<0\) when \(q>c\), with \(a<c<b\) (for instance using \(h(0)>0\), \(h(1)<0\), \(h(2)<0\), \(h(3)>0\) and \(1<c<2\)).

If \(A<0\), positive constant term and negative leading coefficient force exactly one positive simple root (the roots are real and have opposite signs). If \(A>0\), both roots have the same sign because their product \(3C/A>0\); their sum is \(-6\varepsilon B/A\). Therefore both are positive exactly when \(\varepsilon B<0\), which occurs precisely in the two regimes stated. Otherwise both are negative, so \(P>0\) on \(t\ge0\). At the endpoint \(A=0\), the polynomial is linear and has a positive root precisely when \(\varepsilon B<0\). For \(d=0\), the formula immediately reduces to \(A m^4\). This exhausts all rates and reset parameters.

## Verification

An independent raw-moment route starts from the conditional normal moments, integrates them against the beta age density, and obtains

\[
\begin{aligned}
M_1&=m\mu_1,\\
M_2&=m^2\mu_2+v+d\mu_2,\\
M_3&=m^3\mu_3+3m(v\mu_1+d\mu_3),\\
M_4&=m^4\mu_4+6m^2(v\mu_2+d\mu_4)+3(v^2+2vd\mu_2+d^2\mu_4).
\end{aligned}
\]

The independent identity \(K_4=M_4-4M_1M_3-3M_2^2+12M_1^2M_2-6M_1^4\) reduces to the same \(A,B,C\). A standalone Python verifier checks these rational identities, the positive discriminant, and direct numerical beta-mixture integrations.

For a concrete nondegenerate example, take \(q=4\), \(v=2\), \(\sigma^2=3\) (so \(d=1\)). Then

\[
K_4=\frac{13t^2-850t+4375}{26250},\qquad t=m^2,
\]

with exact positive roots \(t_{\pm}=(425\pm75\sqrt{22})/13\). The sign is positive at \(m=0\), negative at \(m=3\), and positive at \(m=8\), as checked by direct conditional-Gaussian quadrature.

## Relationship to prior work

Olsen (2023), *Steady-state moments under resetting to a distribution*, gives a general stationary moment hierarchy and explicit mean, variance, and third-cumulant analyses for a harmonic trap with Gaussian resetting (Sec. III, Eqs. 21–27). That hierarchy supplies a route to the present fourth cumulant, but the source does not state the complete fourth-cumulant sign classification or its two reentrant regimes. The present result is a **new parameter-space consequence** of the established moment framework, not a new invariant-density formula or a replacement for that framework. Related studies of ordinary OU resetting and centered-reset fourth moments do not provide the noncentered two-root classification.

## Limitations

The signs classify the fourth cumulant, not the full distribution; Gaussianity does not follow from zero excess kurtosis. The classification is one-dimensional and assumes Poisson clocks, Gaussian reset positions, and constant harmonic confinement. It does not apply without adjustment to age-dependent resets, non-Gaussian reset laws, active run-and-tumble driving, or time-dependent traps. The result is not claimed to be independent of Olsen's general moment hierarchy.

## References

1. Kristian Stølevik Olsen, *Steady-state moments under resetting to a distribution*, Physical Review E **108**, 044120 (2023), doi:10.1103/PhysRevE.108.044120; arXiv:2310.04840 (first posted 2023-10-07).
2. *Ornstein-Uhlenbeck process and generalizations: Particle dynamics under comb constraints and stochastic resetting*, Physical Review E **107**, 054129 (2023), doi:10.1103/PhysRevE.107.054129 (related OU resetting, not Gaussian reset-to-distribution classification).
