# Sharp all-iterate positivity threshold and delayed sign loss for an optimized two-step stiff solver

## Finding

For the published optimized two-step A-stable \(L(3/5)\)-stable linear multistep rule (Jensen, Lóczi and Ketcheson, Table 2), applied to \(y'=-\lambda y\), \(\lambda>0\), let \(s=h\lambda>0\). With exact positive startup \(y_0=1\), \(y_1=e^{-s}\), **every iterate is strictly positive if and only if**
\[
0<s\le \frac{16}{15}.
\]
For \(16/15<s<16/9\), the odd iterates are positive and an even iterate eventually becomes negative. For \(s\ge16/9\), the first computed iterate \(y_2\) is negative. In the intermediate range the first negative index is given exactly below, and is unbounded when \(s\) approaches \(16/15\) from above.

## Assumptions and scope

The published rule is
\[
y_{n+2}=\frac23y_{n+1}+\frac13y_n+h\left(\frac3{16}f(y_n)+\frac58f(y_{n+1})+\frac{25}{48}f(y_{n+2})\right).
\]
On scalar decay it becomes, for all integers \(n\ge0\),
\[
y_{n+2}=A(s)y_n+B(s)y_{n+1},\quad
A(s)=\frac{16-9s}{48+25s},\quad
B(s)=\frac{32-30s}{48+25s}.
\]
No claim is made for approximate startup, multidimensional positivity, variable steps, or other members of the optimized family.

## Proof

If \(0<s\le16/15\), then \(A(s)>0\) and \(B(s)\ge0\). Both initial values are positive, so induction proves all iterates positive.

For \(16/15<s<16/9\), \(A>0\), \(B<0\). The distinct roots of \(r^2-Br-A=0\) are
\[
r_+=\frac{B+\sqrt{B^2+4A}}2>0,\qquad
r_-=\frac{B-\sqrt{B^2+4A}}2<0.
\]
They satisfy \(\lvert r_-\rvert>r_+\). To exclude the only possible pure-positive-mode resonance, set \(q=(2-s)/(2+s)>0\). Direct rational substitution yields the exact identity
\[
q^2-Bq-A=\frac{4s^3}{(s+2)^2(25s+48)}>0.
\]
Because \(r_-<0<q\), this gives \(q>r_+\). Moreover, for \(0<s<2\), \(e^{-s}>(2-s)/(2+s)=q\), from \(2\operatorname{artanh}(s/2)>s\). Hence \(e^{-s}>r_+\), strictly throughout the intermediate range. Therefore
\[
y_n=c_+r_+^n+c_-r_-^n,
\quad c_+=\frac{e^{-s}-r_-}{r_+-r_-}>0,
\quad c_-=\frac{r_+-e^{-s}}{r_+-r_-}<0.
\]
Odd iterates are strictly positive; the even iterates have opposite-sign terms, and their negative contribution eventually dominates since \(\lvert r_-\rvert>r_+\). Define \(N_-(s)=\min\{n\ge0:y_n<0\}\), then
\[
N_-(s)=2\left(\left\lfloor
\frac{\log(c_+/(-c_-))}{2\log(\lvert r_-\rvert/r_+)}
\right\rfloor+1\right),\quad 16/15<s<16/9.
\]
The strict inequality defining the first negative even iterate handles equality at any preceding zero (a zero iterate is not counted as negative). If \(s\ge16/9\), then \(A\le0\), \(B<0\), and \(y_2=A+Be^{-s}<0\). This proves necessity and sufficiency.

At \(s_0=16/15\), the coefficients obey \(A(s_0)=3/35\), \(B(s_0)=0\), and
\[
B'(s_0)=-\frac{45}{112}.
\]
With \(r_0=\sqrt{3/35}\) and \(e_0=e^{-16/15}>r_0\), root continuity gives
\[
\log(\lvert r_-\rvert/r_+)\sim\frac{45}{112r_0}(s-s_0),\quad
\frac{c_+}{-c_-}\longrightarrow\frac{e_0+r_0}{e_0-r_0}.
\]
Substituting into the exact index formula and observing that the floor alters the index by less than two proves the sharp inverse-distance delay
\[
\lim_{s\downarrow16/15}(s-16/15)N_-(s)
=\frac{112r_0}{45}\log\frac{e_0+r_0}{e_0-r_0}
\approx1.83430639994433.
\]

## Verification

A reproducible program `check.py` checks the published coefficient reduction, the exact polynomial identity, the derivative \(B'(s_0)\), the root-based first-negative-index formula on test cases, and the delay constant. All infinite-quantifier claims are proved above, not inferred from numerical experiments. Run with `python check.py` (Python 3 standard library and SymPy are required).

## Relationship to prior work

Jensen, Lóczi and Ketcheson (arXiv:2610.22685v1, October 15, 2026), Table 2 and Corollary 4.2, give this optimized scheme, its second-order error constant and the A-stable \(L(3/5)\) damping property. They do not give its scalar all-iterate positivity frontier or first negative index. The classical SSP/monotonicity framework provides important general motivation, but the presence of a negative recurrence coefficient alone does not settle positivity for exact exponential startup. The earlier BDF2 delay study concerns another numerical formula, another start procedure, and another threshold; its statement does not imply the values here. The proof above establishes the complete sharp criterion for this specified rule.

## Limitations

This is a scalar constant-step result with **exact** initial values. The source's numerical tests employ TR-BDF2 initialization, which is not covered. A-stability and prescribed stiff-mode damping do not assert preservation of positivity. The inverse-distance first-sign-loss law is asymptotic and does not provide uniform finite-horizon positivity above the threshold. The result has not undergone independent audit; mathematical priority beyond inspected literature remains open.

## References

1. T. Jensen, L. Lóczi and D. I. Ketcheson, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1 (first public October 15, 2026), especially Corollary 4.2 and Table 2. https://arxiv.org/html/2610.22685v1
2. G. Li, Q. Lin, K. Zhang and Z. Zhou, *Optimized Two-Step Coarse Propagators in Parareal Algorithms*, arXiv:2605.11979 (2026), a distinct two-step numerical design and positivity comparison context. https://arxiv.org/abs/2605.11979
3. J. F. B. M. Kraaijevanger, *Contractivity of Runge–Kutta methods*, BIT 31 (1991), 482–528, classical monotonicity context (not relied upon for the proof).
