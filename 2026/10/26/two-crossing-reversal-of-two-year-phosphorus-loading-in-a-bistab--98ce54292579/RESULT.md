# Two-crossing reversal of two-year phosphorus loading in a bistable lake map

## Finding

The same two annual phosphorus loads can reverse their end-of-horizon water-quality ranking **twice** as initial lake phosphorus changes. This is a complete two-crossing criterion for the classical one-state nonlinear phosphorus-recycling lake map at recycling exponent \(q=2\), rather than a claim of a new lake model.

Write \(P_{HL}(P_0)\) for end-of-year-two phosphorus after a high load followed by a low load, and \(P_{LH}(P_0)\) for the reversed sequence. Define

\[
G(x)=(1-b)x+\frac{rx^2}{m^2+x^2},\qquad
\Delta=h-\ell>0,\qquad
K_\Delta(t)=\frac{m^2(2t+\Delta)}{(m^2+t^2)(m^2+(t+\Delta)^2)}.
\]

Then for every initial stock \(P_0\ge0\),

\[
P_{HL}(P_0)-P_{LH}(P_0)
=\Delta\left[rK_\Delta(G(P_0)+\ell)-b\right]. \tag{1}
\]

For every \(m,\Delta>0\), \(K_\Delta\) has precisely one maximizer \(t_{\rm pk}\) on \([0,\infty)\); it is strictly increasing before that point and strictly decreasing afterward. Consequently, the two sequences change ranking at **exactly two distinct strictly positive initial lake stocks** if and only if

\[
\boxed{\ell<t_{\rm pk}\quad\text{and}\quad
K_\Delta(\ell)<\frac br<K_\Delta(t_{\rm pk}).} \tag{2}
\]

When (2) holds, there are unique \(0<P_1<P_2<\infty\) such that \(P_{HL}<P_{LH}\) for \(0\le P_0<P_1\) and \(P_0>P_2\), while \(P_{HL}>P_{LH}\) for \(P_1<P_0<P_2\). Equality holds at the two thresholds. If (2) fails, there cannot be two distinct strictly positive changes of sign; tangent equalities are not counted as sign changes. The comparison concerns **terminal phosphorus only**, not cumulative pollution, time-to-recovery, or economic welfare.

A fully rational example is

\[
(b,r,m,\ell,h)=\left(\frac{12}{25},1,1,0,\frac3{10}\right).
\]

It has

\[
P_1=0.2005578231464619\ldots,
\qquad P_2=0.8769914992399731\ldots.
\]

At zero annual load, this very same model has attracting equilibria \(0\) and \(4/3\), separated by the repelling equilibrium \(3/4\): the double reversal is compatible with a genuinely bistable lake.

## Assumptions and scope

The normalized, annual-step phosphorus recurrence is

\[
P_{j+1}=(1-b)P_j+\frac{rP_j^2}{m^2+P_j^2}+L_j,
\quad P_0\ge0,
\]

with \(0<b<1\), \(r,m>0\), and fixed nonnegative annual loads \(0\le\ell<h\). For the first schedule \((L_0,L_1)=(h,\ell)\), and for the second \((L_0,L_1)=(\ell,h)\). Thus the total two-year external load and its two component magnitudes are identical. The lake's internal recycling is saturating and its annual retention \(1-b\) is between zero and one; these conditions ensure \(G\) is strictly increasing from zero onto \([0,\infty)\). No deterministic dynamics beyond the two displayed annual updates are assumed. A different recycling exponent, sediment-memory state, random forcing, or policy objective is not asserted to obey this theorem.

## Proof

**Step 1: Exact order identity.** Set \(f(x)=x^2/(m^2+x^2)\). The high-first schedule produces \(G(G(P_0)+h)+\ell\); the low-first schedule produces \(G(G(P_0)+\ell)+h\). With \(t=G(P_0)+\ell\) and \(\Delta=h-\ell\), subtraction gives

\[
G(t+\Delta)-G(t)-\Delta
=-b\Delta+r\bigl(f(t+\Delta)-f(t)\bigr).
\]

Elementary fraction subtraction yields

\[
\frac{f(t+\Delta)-f(t)}{\Delta}
=\frac{m^2(2t+\Delta)}{(m^2+t^2)(m^2+(t+\Delta)^2)}=K_\Delta(t),
\]

proving (1), including the endpoints \(P_0=0\) and \(\ell=0\).

**Step 2: Exactly one peak of the divided difference.** Differentiate \(f\):

\[
f'(x)=\frac{2m^2x}{(m^2+x^2)^2},\qquad
f''(x)=\frac{2m^2(m^2-3x^2)}{(m^2+x^2)^3}.
\]

Thus \(f'\) strictly rises on \([0,c]\) and strictly falls on \([c,\infty)\), where \(c=m/\sqrt3\). Since

\[
K_\Delta'(t)=\frac{f'(t+\Delta)-f'(t)}{\Delta},
\]

this derivative is positive whenever \(t+\Delta\le c\), and negative whenever \(t\ge c\). On the remaining interval \(\max\{0,c-\Delta\}<t<c\), the function \(f'(t+\Delta)\) is strictly decreasing while \(f'(t)\) is strictly increasing, so their difference is strictly decreasing. At the left end it is positive, and at the right end negative. In the case \(\Delta\ge c\), the difference at the left endpoint \(t=0\) is \(f'(\Delta)-f'(0)=f'(\Delta)>0\). Hence in every case there is a unique zero \(t_{\rm pk}\in(\max\{0,c-\Delta\},c)\), and the derivative is positive before it and negative after it. Also \(K_\Delta(t)>0\), and \(K_\Delta(t)\to0\) as \(t\to\infty\).

**Step 3: Complete sign-change classification.** Because

\[
G'(x)=1-b+\frac{2rm^2x}{(m^2+x^2)^2}>0
\]

for all \(x\ge0\), \(P_0\mapsto t=G(P_0)+\ell\) maps \([0,\infty)\) bijectively and strictly increasingly onto \([\ell,\infty)\). The sign of (1) is the sign of \(K_\Delta(t)-b/r\). A horizontal level intersects a positive strictly unimodal function on \((\ell,\infty)\) **twice with both crossings transversal** if and only if its starting value lies strictly below that level and its unique interior peak lies strictly above: precisely (2). In this regime, the sign is negative, then positive, then negative. If the left endpoint already lies on or beyond the peak, or if the level does not lie strictly between its starting and peak values, there can be at most one positive sign change. Tangential contacts at the peak or the left endpoint do not create two positive ranking reversals.

**Step 4: Rational bistable witness.** For the stated parameters, \(\Delta=3/10\), \(b/r=12/25\), and

\[
K_{3/10}(0)=\frac{30}{109}<\frac{12}{25},\qquad
K_{3/10}(1/2)=\frac{26}{41}>\frac{12}{25}.
\]

Since \(K_{3/10}\) rises from zero to its unique maximum, these inequalities imply condition (2) and two distinct strictly positive crossings. Inverting \(G(P)=\frac{13}{25}P+P^2/(1+P^2)\) at the two positive roots of \(K_{3/10}(t)=12/25\) gives the printed initial-stock thresholds; the inversion is unique because \(G'>0\). At zero load, nonzero fixed points solve \(12P^2-25P+12=0\), namely \(P=3/4\) and \(P=4/3\). Their respective derivatives are \(709/625>1\) and \(541/625<1\); \(G'(0)=13/25<1\). The lower and upper fixed points are attracting, with the intermediate fixed point repelling. This confirms the example's bistable ecological interpretation without extrapolating the ordering theorem to any other ecological regime.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It (i) evaluates the two schedules independently with exact rational arithmetic at \(P_0=0,1/2,1\), confirming signs negative/positive/negative; (ii) checks the exact algebraic difference formula; (iii) solves the two positive crossover equations with 85-digit decimal arithmetic and 260 bisection iterations; (iv) verifies the unforced fixed points and their local multipliers by the rational formulas above; and (v) runs 3,000 seeded floating-point comparisons of the two independently evaluated schedules against identity (1) over broad positive parameter ranges. Numerical checks confirm reproducibility, but uniqueness and global assertions are supplied by the proof, not by finite enumeration.

For reproducibility, run `python verify.py`; the script has no network or external-package dependencies.

## Relationship to prior work

Carpenter, Ludwig, and Brock (1999) introduced the alternate-state and phosphorus-management setting, while Carpenter, Brock, and Hanson (1999) and Janssen and Carpenter (1999) provide accessible accounts of the nonlinear phosphorus-recycling recurrence and adaptive lake management. In particular, the 1999 open-access papers explicitly exhibit the saturating term and annual recurrence. Their inspected full-text portions address policy, resilience, sediment feedback and social–ecological simulations, rather than the stated sharp *two annual loads, two initial-stock crossings* classification. This result starts from their established recurrence; it neither claims to introduce it nor to solve their multiyear optimal-control problems. An analogous ordering argument from general nonlinear difference-equation theory might subsume the calculation; no such explicit dominating theorem was established from inspected material.

## Limitations

The double-reversal theorem is restricted to the deterministic one-state map with recycling exponent exactly \(q=2\), two annual updates, fixed nonnegative loading pair, and terminal phosphorus as objective. It says nothing about actual lake-management optimality with storage, slow sediment pools, observations, risk, costs, or continuous-time responses. The accessible abstract, but not the complete text, of the closely related Carpenter–Ludwig–Brock 1999 management paper was inspected; that gap, together with possible general scalar-map ordering theorems, leaves a residual originality risk. A bibliographic 1998 working-paper antecedent lacks a verified exact public day; the day-precise source date records a verified 1999 journal appearance, not a claim that the underlying model first existed then. No independent audit has been performed.

## References

1. S. R. Carpenter, D. Ludwig, and W. A. Brock (1999), “Management of eutrophication for lakes subject to potentially irreversible change,” *Ecological Applications* **9**:751–771, first published 1999-08-01. https://doi.org/10.1890/1051-0761(1999)009[0751:MOEFLS]2.0.CO;2
2. S. R. Carpenter, W. A. Brock, and P. J. Hanson (1999), “Ecological and social dynamics in simple models of ecosystem management,” *Conservation Ecology* **3**(2):4, published 1999-08-06. https://www.ecologyandsociety.org/vol3/iss2/art4/
3. M. A. Janssen and S. R. Carpenter (1999), “Managing the resilience of lakes: A multi-agent modeling approach,” *Conservation Ecology* **3**(2):15, published 1999-11-24. https://www.ecologyandsociety.org/vol3/iss2/art15/
