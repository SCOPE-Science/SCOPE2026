# Peak timing after a finite pumping pulse in the Glover–Balmer stream-depletion model

## Finding

In the ideal Glover–Balmer stream-depletion model, a constant-rate pumping pulse of duration \(\tau>0\) has a unique global maximum normalized stream-depletion rate at time \(t_*\) after pumping begins, with

\[
 t_* > \max\{\tau,2a/3\},\qquad t_* < \tau+2a/3,
\]

where \(a=d^2S/(4T)\). The peak time is characterized by

\[
 q(t_*)=q(t_* - \tau),\qquad q(t)=\frac{\sqrt a}{\sqrt\pi\,t^{3/2}}e^{-a/t},
\]

or equivalently

\[
 \frac32\log\!\left(\frac{t_*}{t_* - \tau}\right)
 = \frac{a\tau}{t_*(t_* - \tau)}.
\]

In addition, \(t_*\) is strictly increasing in \(\tau\), but \(0<dt_*/d\tau<1\). Thus increasing the pumping duration shifts the maximum later by less than the added duration; the delay after cessation, \(t_* - \tau\), strictly decreases.

## Assumptions and scope

Assume a homogeneous, isotropic, laterally unbounded confined aquifer with constant transmissivity \(T>0\) and storage coefficient \(S>0\), a straight fully penetrating stream held at fixed stage, and a well at perpendicular distance \(d>0\). Pumping is at constant rate \(Q>0\) on \([0,\tau]\) and zero thereafter. The standard linear Glover–Balmer model and superposition are assumed. The time \(t\) is measured from pump start, and \(t_*\) is the time of the peak stream-depletion rate, not the peak aquifer drawdown.

## Proof

Put \(a=d^2S/(4T)>0\). The step-pumping stream-depletion fraction is

\[
 D(t)=\operatorname{erfc}\!\left(\sqrt{a/t}\right),\quad t>0,
\]

with \(D(0)=0\). Differentiation gives

\[
 q(t)=D'(t)=\frac{\sqrt a}{\sqrt\pi\,t^{3/2}}e^{-a/t}.
\]

The normalized depletion rate for a finite pulse is \(P_\tau(t)=D(t)\) for \(0<t\le\tau\), and \(P_\tau(t)=D(t)-D(t-\tau)\) for \(t>\tau\). During pumping, \(D\) is strictly increasing. After cessation,

\[
 P_\tau'(t)=q(t)-q(t-\tau).
\]

The logarithm of the ratio in this difference is

\[
 G(t)=\log\frac{q(t)}{q(t-\tau)}
 =-\frac32\log\frac{t}{t-\tau}+\frac{a\tau}{t(t-\tau)}.
\]

Its derivative is

\[
 G'(t)=\frac{\tau}{t^2(t-\tau)^2}
 \left[\frac32t(t-\tau)-a(2t-\tau)\right].
\]

The bracket is an upward-opening quadratic, positive at \(t=0\), negative at \(t=\tau\), and positive for sufficiently large \(t\). It therefore has exactly one zero above \(\tau\). Expansion of the displayed formula gives \(G(t)=-3\tau/(2t)+O(t^{-2})\) as \(t\to\infty\), so \(G(t)\to0\) from below. Consequently \(G\) first strictly decreases from \(+\infty\), then strictly increases to \(0\) from below. It has exactly one zero on \((\tau,\infty)\). Hence \(P_\tau'\) changes sign exactly once, from positive to negative, proving that the pulse response has one global maximum at the unique root \(t_*\) of \(q(t_*)=q(t_* - \tau)\).

The function \(q\) increases strictly up to \(m=2a/3\) and decreases strictly thereafter, since

\[
 \frac{q'(t)}{q(t)}=-\frac{3}{2t}+\frac{a}{t^2}.
\]

At the equality \(q(t_*)=q(t_* - \tau)\), the two arguments must lie on opposite sides of the mode: \(t_* - \tau<m<t_*\). This yields \(t_* > \max\{\tau,m\}\) and \(t_*<\tau+m\), giving the stated bounds.

Finally, implicit differentiation of \(q(t_*)=q(t_* - \tau)\) gives

\[
 \frac{dt_*}{d\tau}=-\frac{q'(t_* - \tau)}{q'(t_*)-q'(t_* - \tau)}.
\]

Because \(q'(t_* - \tau)>0\) and \(q'(t_*)<0\), the derivative lies strictly between zero and one. Thus the peak time increases with pulse duration, while \(t_* - \tau\) decreases. The bounds also give \(t_*\to 2a/3\) as \(\tau\downarrow0\). As \(\tau\to\infty\), \(0<t_* - \tau<2a/3\) and \(q(t_*)=q(t_* - \tau)\to0\), so \(t_* - \tau\to0\).

## Verification

The result is an analytic consequence of the classical step response and linear superposition. The uniqueness argument uses the explicit derivative of the complementary error function and the sign pattern of one quadratic; it does not infer uniqueness from sampled times or numerical plots. The theorem concerns the ideal fully penetrating, fixed-stage Glover–Balmer model and a single rectangular pumping pulse only.

## Relationship to prior work

Glover and Balmer introduced the step-pumping stream-depletion response. Jenkins documented rate and volume calculations during pumping and after shutdown, including intermittent pumping schedules, and emphasized the operational importance of residual effects. Zlotnik analyzed maximum stream-depletion rates for continuously pumped wells in leaky aquifers. The present statement concerns the exact unique time of the maximum for one finite constant-rate pulse in the classical fully penetrating model, including a strict duration-dependent bracket and a derivative bound for the peak time. The reviewed material did not establish that exact combination; an uninspected full text on intermittent pumping remains a bibliographic risk.

## Limitations

The result is not a theorem for leaky aquifers, partially penetrating streams, finite stream width, variable stream stage, heterogeneous aquifers, nonlinear flow, or arbitrary multi-pulse schedules. Superposition requires the stated linear model. The proof determines the unique peak time implicitly; it does not give an elementary closed form for \(t_*\). Independent audit and independent validation have not been performed.

## References

1. R. E. Glover and G. G. Balmer, “River depletion resulting from pumping a well near a river,” *Eos, Transactions American Geophysical Union* 35(3) (June 1954), 468–470. DOI: 10.1029/TR035i003p00468.
2. C. T. Jenkins, *Computation of Rate and Volume of Stream Depletion by Wells*, U.S. Geological Survey Techniques of Water-Resources Investigations, Book 4, Chapter D1 (1968). https://pubs.usgs.gov/twri/twri4d1/
3. V. A. Zlotnik, “A concept of maximum stream depletion rate for leaky aquifers in alluvial valleys,” *Water Resources Research* 40 (2004), W06507. DOI: 10.1029/2003WR002932.
4. B. Hunt, “Review of Stream Depletion Solutions, Behavior, and Calculations,” *Journal of Hydrologic Engineering* 19(1) (2014), 167–178. DOI: 10.1061/(ASCE)HE.1943-5584.0000768.
