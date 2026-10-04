# Exact standardized concentration profile for symmetric geometric laws
## Finding
For every real \(c>0\), consider the symmetric geometric distribution
\[
\Pr\{X_q=k\}=\frac{1-q}{1+q}q^{|k|},\qquad k\in\mathbb Z,\quad 0<q<1.
\]
Its mean is \(0\) and its variance is
\[
\sigma_q^2=\frac{2q}{(1-q)^2}.
\]
The complete standardized central-mass profile is
\[
\inf_{0<q<1}\Pr\{|X_q|\le c\sigma_q\}
=
\min_{0<q<1}\Pr\{|X_q|<c\sigma_q\}
=
\frac{c}{\sqrt{c^2+2}}.
\]
The closed-event infimum is never attained. The open-event minimum is attained uniquely at
\[
q_1(c)=\exp\!\left(-2\operatorname{arsinh}\frac{c}{\sqrt2}\right)
=1+c^2-c\sqrt{c^2+2}.
\]
Equivalently, in the parameterization \(p=1-q\) used for a difference of two independent geometric variables, the unique open-event minimizer is
\[
p_1(c)=c\left(\sqrt{c^2+2}-c\right).
\]
At \(c=1\), the formula gives \(1/\sqrt3\), recovering the previously known one-standard-deviation value.

## Assumptions and scope
The parameter \(c\) is any positive real number and \(q\) ranges over \((0,1)\). The distribution is supported on all integers and is symmetric and log-concave. The claim concerns intervals centered at the mean whose radius is a fixed multiple of the distribution's own standard deviation. It does not assert an extremal result over all infinitely divisible or all discrete log-concave distributions.

## Proof
Put
\[
r(q)=c\sigma_q=\frac{c\sqrt{2q}}{1-q}.
\]
This is strictly increasing from \(0\) to \(+\infty\). If \(m\le r(q)<m+1\), where \(m\) is a nonnegative integer, then summing the two geometric tails gives
\[
\Pr\{|X_q|\le c\sigma_q\}=1-\frac{2q^{m+1}}{1+q}.
\]
For \(s=m+1\ge1\), let \(q_s\) be the unique solution of \(r(q_s)=s\). Writing
\[
t_s=\operatorname{arsinh}\!\left(\frac{c}{\sqrt2\,s}\right),
\]
we have \(q_s=e^{-2t_s}\). On the band \(s-1\le r(q)<s\), the displayed central mass is strictly decreasing in \(q\), so its band infimum is
\[
b_s(c)=1-\frac{2q_s^s}{1+q_s}.
\]
It remains to compare these infinitely many band infima. Define their complementary masses
\[
T_s(c)=1-b_s(c)=\frac{2q_s^s}{1+q_s}
=\frac{e^{-(2s-1)t_s}}{\cosh t_s}.
\]
Treat \(s\ge1\) as a real variable. Since
\[
t_s'=-\frac{\tanh t_s}{s},
\]
differentiation gives
\[
\frac{d}{ds}\log T_s
=-2t_s+\frac{2s-1+\tanh t_s}{s}\tanh t_s.
\]
Because \(0<\tanh t_s<1\),
\[
\frac{2s-1+\tanh t_s}{s}<2,
\]
and because \(t_s>\tanh t_s\) for \(t_s>0\), the derivative is strictly negative. Hence \(T_s(c)\) strictly decreases and \(b_s(c)\) strictly increases with \(s\). The global closed-event infimum therefore comes from the first band. At \(s=1\),
\[
b_1(c)=\frac{1-q_1(c)}{1+q_1(c)}=\tanh t_1=\frac{c}{\sqrt{c^2+2}}.
\]
The first closed band approaches this value only as \(q\uparrow q_1(c)\). At the boundary \(r(q_1)=1\), the closed event acquires the atoms at \(\pm1\), so its probability jumps upward; all later band infima are strictly larger. Thus the closed infimum is not attained.

For the open event, on the band \(s-1<r(q)\le s\) one has
\[
\Pr\{|X_q|<c\sigma_q\}=1-\frac{2q^s}{1+q},
\]
which is strictly decreasing in \(q\). Its minimum on that band is attained at \(q_s\) and equals \(b_s(c)\). Since \(b_s(c)\) is strictly increasing in \(s\), the unique global minimum occurs at \(q_1(c)\), and it equals \(c/\sqrt{c^2+2}\).

## Verification
The proof uses exact summation of geometric tails, an explicit solution of the threshold equation, and a sign computation for a one-variable derivative. The critical inequalities are strict: \(t>\tanh t\) for \(t>0\), and \((2s-1+\tanh t)/s<2\) for \(s\ge1\). Direct numerical stress tests over multipliers ranging from \(0.05\) to \(100\) and the first one hundred lattice bands agree with the analytic ordering; these tests are not used as proof.

## Relationship to prior work
Zhang, Hu, and Sun determine the symmetric-geometric infimum at exactly one standard deviation and obtain \(1/\sqrt3\). Their proof analyzes the same lattice staircase only at that single radius. The result here gives the exact profile for every positive standardized radius, identifies the unique open-event optimizer, and proves that the first lattice threshold controls every radius.

Bobkov, Marsiglietti, and Melbourne study concentration functions of discrete log-concave laws. They prove sharp variance control of the largest atom, with equality for two-sided geometric laws, and give fixed-integer-window bounds for concentration functions. Those statements do not optimize a centered window whose radius itself scales with the varying standard deviation, and their Section 8 bounds do not imply the profile above.

## Limitations
The result is specific to the symmetric geometric family. It does not determine the all-radius extremal profile for general infinitely divisible distributions, for all symmetric log-concave integer laws, or for other one-parameter families. Literature searches did not locate a prior statement of the all-radius formula, but an equivalent result under different terminology may exist.

## References
1. J. Zhang, Z.-C. Hu, and W. Sun, *On the measure concentration of infinitely divisible distributions*, arXiv:2310.03471. First public version: 2023-10-05. Published in *Acta Mathematica Scientia* 45 (2025), 473–492, DOI 10.1007/s10473-025-0211-x.
2. S. G. Bobkov, A. Marsiglietti, and J. Melbourne, *Concentration functions and entropy bounds for discrete log-concave distributions*, arXiv:2007.11030. First public version: 2020-07-21.
