# SNGM's first source-initialized momentum resonances occur at period six
## Finding

Consider deterministic stochastic normalized gradient descent with momentum on the scalar strongly convex quadratic
\[
f(x)=\frac a2x^2,
\qquad
a>0.
\]
Use the source initialization
\[
u_0=0,
\]
constant step
\[
\eta>0,
\]
and momentum
\[
0<\beta<1.
\]
Away from the minimizer, the normalized gradient is just its sign, so the source recurrence becomes
\[
u_{t+1}
=
\beta u_t+\operatorname{sign}(x_t),
\qquad
x_{t+1}
=
x_t-\eta u_{t+1}.
\]

A nonzero source-initialized full-state return means
\[
(x_p,u_p)=(x_0,0)
\]
with no intermediate iterate equal to zero.

No such return exists for
\[
1\le p\le5.
\]
The first possible period is exactly six.

Write
\[
\varphi=\frac{1+\sqrt5}{2}.
\]
Up to changing every sign simultaneously, there are exactly two period-six momentum resonances.

The first is
\[
\boxed{
\beta=\varphi^{-1}.
}
\]
For every
\[
\boxed{
1<\frac{x_0}{\eta}<\varphi,
}
\]
the sign itinerary is
\[
+,+,-,-,-,+,
\]
and the momentum values over the six updates are
\[
1,\ \varphi,\ 0,\ -1,\ -\varphi,\ 0.
\]
The parameter values are
\[
x_0,
\quad
x_0-\eta,
\quad
x_0-\varphi^2\eta,
\quad
x_0-\varphi^2\eta,
\quad
x_0-\varphi\eta,
\quad
x_0,
\quad
x_0.
\]
Hence the full state returns exactly after six steps.

The second resonance is
\[
\boxed{
\beta=\varphi^{-1/2}.
}
\]
For every
\[
\boxed{
\beta<\frac{x_0}{\eta}<1,
}
\]
the sign itinerary is
\[
+,-,+,-,-,+.
\]
If
\[
r=\frac{x_0}{\eta},
\]
the six parameter positions, divided by \(\eta\), are
\[
r,
\quad
r-1,
\quad
r-\beta,
\quad
r-\varphi,
\quad
r-\beta^{-1},
\quad
r.
\]
Again
\[
(x_6,u_6)=(x_0,0).
\]

Both resonance families have an exact average stationarity floor that is independent of the initial point within the admissible interval. For the first family,
\[
\boxed{
\frac16\sum_{t=0}^{5}|f'(x_t)|
=
\frac{a\eta}{6}(1+3\varphi).
}
\]
For the second family,
\[
\boxed{
\frac16\sum_{t=0}^{5}|f'(x_t)|
=
\frac{a\eta}{6}
\left(
1-\beta+\varphi+\beta^{-1}
\right).
}
\]

Thus fixed-step SNGM need not approach the unique minimizer even on the simplest strongly convex quadratic. The residual scale is genuinely proportional to the learning rate.

## Assumptions and scope

The result uses Algorithm 1 of the defining SNGM paper with one deterministic gradient rather than a minibatch gradient.

The normalized gradient is defined only when the gradient is nonzero. The open initial intervals above ensure that no iterate in the periodic orbit hits the minimizer.

The learning rate is constant. The source experiments also use decaying schedules, and the finding does not assert periodicity under those schedules.

The theorem concerns exact return to the source-initialized full state
\[
(x_0,u_0)=(x_0,0).
\]
It does not classify every periodic orbit that can arise from an arbitrary nonzero momentum state.

The scalar curvature
\[
a
\]
cancels completely from the state dynamics because of gradient normalization. It appears only when the orbit is converted back to gradient norms or objective values.

## Proof

For a sign word
\[
s_0,\ldots,s_{p-1}\in\{-1,+1\},
\]
define
\[
U_0(\beta)=0
\]
and
\[
U_{j+1}(\beta)=\beta U_j(\beta)+s_j.
\]
Also define
\[
C_0(\beta)=0,
\qquad
C_j(\beta)=\sum_{i=1}^{j}U_i(\beta).
\]
Starting from
\[
u_0=0,
\]
the recurrence gives exactly
\[
u_j=U_j(\beta),
\qquad
x_j=x_0-\eta C_j(\beta).
\]

Therefore a full-state return after \(p\) steps requires the two polynomial identities
\[
U_p(\beta)=0,
\qquad
C_p(\beta)=0.
\]
The signs are feasible only if
\[
s_j
\left(
\frac{x_0}{\eta}-C_j(\beta)
\right)>0
\]
for every
\[
0\le j<p.
\]

There are only finitely many sign words for
\[
p\le6.
\]
Exact polynomial greatest-common-divisor reduction gives the following classification.

For
\[
p=1,2,3,5,
\]
the two return polynomials have no nonconstant common factor.

For
\[
p=4,
\]
the only nonconstant common factors that occur are, up to constants,
\[
(\beta+1)^2,
\qquad
\beta^2+1,
\qquad
(\beta-1)(\beta+1).
\]
None has a root in
\[
0<\beta<1.
\]

For
\[
p=6,
\]
the only common factors with a root in
\[
(0,1)
\]
are
\[
\beta^2+\beta-1
\]
and
\[
\beta^4+\beta^2-1.
\]
The first has the unique admissible root
\[
\beta=\varphi^{-1},
\]
and occurs only for the sign word
\[
+,+,-,-,-,+
\]
and its global sign reversal.

For this root,
\[
\beta^2+\beta=1.
\]
The momentum and cumulative-displacement sequences simplify to
\[
U_1,\ldots,U_6
=
1,\ \varphi,\ 0,\ -1,\ -\varphi,\ 0
\]
and
\[
C_0,\ldots,C_6
=
0,\ 1,\ \varphi^2,\ \varphi^2,\ \varphi,\ 0,\ 0.
\]
The sign inequalities reduce exactly to
\[
1<\frac{x_0}{\eta}<\varphi.
\]

The second polynomial has the unique admissible root
\[
\beta=\varphi^{-1/2},
\]
because
\[
\beta^2=\varphi^{-1}.
\]
It occurs only for
\[
+,-,+,-,-,+
\]
and its global sign reversal. Its cumulative displacements are
\[
C_0,\ldots,C_6
=
0,\ 1,\ \beta,\ \varphi,\ \beta^{-1},\ 0,\ 0,
\]
so the sign inequalities reduce exactly to
\[
\beta<\frac{x_0}{\eta}<1.
\]

Since no shorter positive-momentum return is possible, every feasible return just constructed has exact period six.

Finally, on the first family the sum of the six absolute normalized positions is
\[
1+3\varphi,
\]
independent of
\[
x_0/\eta.
\]
On the second family it is
\[
1-\beta+\varphi+\beta^{-1}.
\]
Multiplying by
\[
a\eta/6
\]
gives the stated mean gradient norms.

## Verification

The accompanying `verify.py` reconstructs the exact return polynomials for every sign word of lengths one through six using rational polynomial arithmetic.

It verifies that periods below six have no admissible root in
\[
0<\beta<1,
\]
that the two period-six candidate factors and sign words are exactly those stated above, and that the sign-feasibility intervals are nonempty.

It then replays both resonance families for multiple initial points and checks the exact six-step state return and mean-gradient formulas numerically at high precision.

The finite enumeration is exhaustive for periods up to six. It is not used to make any statement about longer periods.

## Relationship to prior work

Zhao, Shi, Xie, and Li introduce SNGM by placing the normalized stochastic gradient inside a Polyak-style momentum accumulator. Their Algorithm 1 uses
\[
u_{t+1}
=
\beta u_t+\frac{g_t}{\|g_t\|}
\]
followed by
\[
w_{t+1}=w_t-\eta u_{t+1}.
\]
Their smooth-objective theorem gives, for a constant learning rate, an average stationarity upper bound containing a term proportional to
\[
L\eta.
\]
The inspected source does not classify exact periodic states or identify algebraic momentum resonances.

Wang, Jia, and Wen study search-direction correction methods that also combine inertia with normalized-gradient information. Their methods use a different velocity rule, additional gradient terms, and a restart condition; their convex convergence theory therefore does not imply the SNGM return-polynomial classification.

Bernstein, Wang, Azizzadenesheli, and Anandkumar study signSGD and Signum. Signum first averages the raw gradient and then takes the sign of that momentum before updating the parameter. SNGM instead inserts the normalized gradient into the momentum and applies the full momentum vector as the update. The scalar recurrences are consequently different.

Focused searches for SNGM, normalized-gradient momentum, scalar quadratic periodic orbits, momentum resonances, and limit cycles did not identify an implication-equivalent published classification.

## Limitations

The classification is only for source-initialized returns of period at most six. Longer resonances are not classified.

The exact resonance momenta
\[
\varphi^{-1}
\]
and
\[
\varphi^{-1/2}
\]
are mathematical boundary cases rather than the momentum values most commonly used in deep-learning experiments.

The result is deterministic and one-dimensional. It does not claim that stochastic minibatch SNGM exhibits the same exact cycles.

The practical relevance is diagnostic: it shows that the constant-step stationarity floor in the source theory corresponds to real recurrent dynamics, even under strong convexity.

## References

1. Shen-Yi Zhao, Chang-Wei Shi, Yin-Peng Xie, and Wu-Jun Li, “Stochastic Normalized Gradient Descent with Momentum for Large-Batch Training,” arXiv:2007.13985v1, first submitted 2020-07-28; later published in Science China Information Sciences.
2. Yifei Wang, Zeyu Jia, and Zaiwen Wen, “The Search direction Correction makes first-order methods faster,” arXiv:1905.06507v1, first submitted 2019-05-16; later published in SIAM Journal on Scientific Computing.
3. Jeremy Bernstein, Yu-Xiang Wang, Kamyar Azizzadenesheli, and Anima Anandkumar, “signSGD: Compressed Optimisation for Non-Convex Problems,” arXiv:1802.04434v1, first submitted 2018-02-13; ICML 2018.
