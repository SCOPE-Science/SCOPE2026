# Polyp self-renewal makes mean persistence independent of medusa noise

## Finding

Consider the stochastic jellyfish model
\[
\begin{aligned}
dP&=\left[(a-d)P+bM-b_1P^2\right]dt+\sigma_1P\,dB_1(t),\\
dM&=\left[cP-d^*M-b_2M^2\right]dt+\sigma_2M\,dB_2(t),
\end{aligned}
\]
where \(P\) is the polyp population and \(M\) is the medusa population.

Set
\[
r_P=a-d-\frac{\sigma_1^2}{2}.
\]
If
\[
r_P>0,
\]
then every positive solution obeys
\[
\liminf_{t\to\infty}
\frac1t\int_0^tP(s)\,ds
\ge
\frac{r_P}{b_1}
\quad\text{almost surely}.
\]
This conclusion is independent of the medusa-noise intensity \(\sigma_2\).

The result also yields persistence in mean for the weighted total used in the source,
\[
W=
\frac{d^*}{b}P+M.
\]
Writing
\[
q=\frac{d^*}{b},
\]
one has
\[
q\frac{r_P}{b_1}
\le
\liminf_{t\to\infty}
\frac1t\int_0^tW(s)\,ds
\]
and
\[
\limsup_{t\to\infty}
\frac1t\int_0^tW(s)\,ds
\le
\frac{
2\left(a-d+\frac{bc}{d^*}\right)
}{
\min\left\{\frac{bb_1}{d^*},b_2\right\}
}
\quad\text{almost surely}.
\]

Thus the second small-noise condition imposed in the source's persistence-in-mean theorem,
\[
c-d^*-\frac{\sigma_2^2}{2}>0,
\]
is not needed for persistence in mean of this model.

At the source's displayed biological parameters, choose
\[
\sigma_1=0.1,
\qquad
\sigma_2=1.
\]
Then
\[
a-d-\frac{\sigma_1^2}{2}=0.1448>0,
\]
but
\[
c-d^*-\frac{\sigma_2^2}{2}=-0.4065<0.
\]
The source's theorem is therefore silent, while the present result gives
\[
\liminf_{t\to\infty}
\frac1t\int_0^tP(s)\,ds
\ge14480
\]
and
\[
\liminf_{t\to\infty}
\frac1t\int_0^tW(s)\,ds
\ge
\frac{14842}{425}
\approx34.9223529412
\]
almost surely.

## Assumptions and scope

The parameters
\[
b,d^*,b_1,b_2
\]
are positive, \(c\ge0\), and the initial populations are positive. The Brownian motions are independent as in the printed stochastic model.

The theorem concerns persistence in mean in the source's sense: a positive almost-sure lower bound and a finite almost-sure upper bound for the long-time average of the weighted total \(W\).

The result does not assert stochastic permanence of both stages in probability. It also does not assert that the medusa population itself has a positive time average when \(\sigma_2\) is arbitrarily large.

The lower polyp bound is sharp for the decoupled limiting case \(b=0\), where the polyp equation is exactly stochastic logistic. For the biological two-stage model with \(b>0\), recruitment from medusae can only increase \(P\) relative to that baseline.

## Proof

Let \(X\) solve
\[
dX=
X\left[(a-d)-b_1X\right]dt
+
\sigma_1X\,dB_1(t),
\qquad
X(0)=P(0).
\]

Define the positive stochastic factor
\[
R(t)
=
\exp\!\left(
-\sigma_1B_1(t)
+
\frac{\sigma_1^2}{2}t
\right).
\]
Itô's product rule gives
\[
\frac{d}{dt}\bigl(RP\bigr)
=
(a-d)RP
-
b_1R P^2
+
bRM,
\]
whereas
\[
\frac{d}{dt}\bigl(RX\bigr)
=
(a-d)RX
-
b_1R X^2.
\]

Set
\[
Y_P=RP,
\qquad
Y_X=RX.
\]
Because
\[
P=\frac{Y_P}{R},
\qquad
X=\frac{Y_X}{R},
\]
their difference satisfies the ordinary random differential equation
\[
\frac{d}{dt}(Y_P-Y_X)
=
\left[
a-d-
\frac{b_1}{R}(Y_P+Y_X)
\right](Y_P-Y_X)
+
bRM.
\]
The initial difference is zero and the forcing term is nonnegative. Variation of constants therefore gives
\[
Y_P(t)-Y_X(t)\ge0.
\]
Since \(R(t)>0\),
\[
P(t)\ge X(t)
\]
pathwise.

Put
\[
r_P=a-d-\frac{\sigma_1^2}{2}.
\]
The scalar logistic equation has the explicit solution
\[
X(t)
=
\frac{
X(0)\exp\!\left(r_Pt+\sigma_1B_1(t)\right)
}{
1+b_1X(0)
\int_0^t
\exp\!\left(r_Ps+\sigma_1B_1(s)\right)ds
}.
\]
Let
\[
D(t)
=
1+b_1X(0)
\int_0^t
\exp\!\left(r_Ps+\sigma_1B_1(s)\right)ds.
\]
Then
\[
\frac{d}{dt}\log D(t)=b_1X(t),
\]
so
\[
\frac1t\int_0^tX(s)\,ds
=
\frac{\log D(t)}{b_1t}.
\]

If \(r_P>0\), the Brownian strong law
\[
B_1(t)/t\to0
\]
implies
\[
\frac{\log D(t)}{t}\to r_P.
\]
Hence
\[
\frac1t\int_0^tX(s)\,ds
\to
\frac{r_P}{b_1}
\]
and, from the explicit formula,
\[
\frac{\log X(t)}{t}\to0
\]
almost surely. Since \(P\ge X\), this proves
\[
\liminf_{t\to\infty}
\frac1t\int_0^tP(s)\,ds
\ge
\frac{r_P}{b_1}.
\]

It remains to prove a finite upper mean bound for \(W\). Let
\[
q=\frac{d^*}{b},
\qquad
x=qP,
\qquad
y=M,
\qquad
W=x+y.
\]
The linear medusa terms cancel:
\[
dW
=
\left[
\left(a-d+\frac{bc}{d^*}\right)x
-
\frac{bb_1}{d^*}x^2
-
b_2y^2
\right]dt
+
\sigma_1x\,dB_1
+
\sigma_2y\,dB_2.
\]
Define
\[
A=a-d+\frac{bc}{d^*}
\]
and
\[
k=
\frac12
\min\left\{
\frac{bb_1}{d^*},
b_2
\right\}.
\]
Since \(r_P>0\), one has \(A>0\). Also,
\[
x^2+y^2\ge\frac12(x+y)^2.
\]
Therefore the drift of \(W\) is bounded above by
\[
AW-kW^2.
\]

Applying Itô's formula to \(\log W\) and discarding its nonpositive quadratic-variation correction gives
\[
d\log W
\le
(A-kW)dt+dN_t,
\]
where
\[
dN_t
=
\sigma_1\frac{x}{W}\,dB_1
+
\sigma_2\frac{y}{W}\,dB_2.
\]
Because \(x/W\) and \(y/W\) lie in \([0,1]\),
\[
\langle N\rangle_t
\le
\max\{\sigma_1^2,\sigma_2^2\}t.
\]
Thus
\[
N_t/t\to0
\]
almost surely.

Moreover,
\[
W(t)\ge qP(t)\ge qX(t),
\]
so
\[
\liminf_{t\to\infty}\frac{\log W(t)}{t}\ge0.
\]
Integrating the logarithmic inequality and dividing by \(t\) now gives
\[
\limsup_{t\to\infty}
\frac1t\int_0^tW(s)\,ds
\le
\frac{A}{k},
\]
which is the stated upper bound. The lower bound follows from
\[
W\ge qP.
\]
Together these are exactly the two inequalities required for persistence in mean.

## Verification

The bundled `verify.py` checks the algebra of the weighted cancellation and the source-parameter witness with exact rational arithmetic.

For the source values,
\[
a=\frac3{20},
\quad
d=\frac1{5000},
\quad
b=\frac{17}{10},
\quad
c=\frac{61}{625},
\quad
d^*=\frac{41}{10000},
\quad
b_1=\frac1{100000},
\quad
b_2=\frac1{10000},
\]
and
\[
\sigma_1=\frac1{10},
\qquad
\sigma_2=1,
\]
it verifies
\[
r_P=\frac{181}{1250}=0.1448,
\]
\[
\frac{r_P}{b_1}=14480,
\]
\[
c-d^*-\frac{\sigma_2^2}{2}
=
-\frac{813}{2000},
\]
and
\[
\frac{d^*}{b}\frac{r_P}{b_1}
=
\frac{14842}{425}.
\]

The stochastic comparison and time-average limits are proved analytically and do not rely on finite simulation.

## Relationship to prior work

Win and Tian study this exact stochastic polyp-medusa system. Their Theorem 3.9 assumes both
\[
a-d-\frac{\sigma_1^2}{2}>0
\]
and
\[
c-d^*-\frac{\sigma_2^2}{2}>0
\]
to obtain persistence in mean for the weighted population \(W=d^*P/b+M\).

Stochastic logistic persistence theory is much older. The scalar comparison process used here is a standard stochastic logistic equation, and prior logistic literature establishes persistence and extinction thresholds based on the noise-corrected growth rate.

General stochastic cooperative-system literature also shows that componentwise noise and positive coupling can interact nontrivially in persistence questions. The common Lotka-Volterra cooperative framework, however, uses multiplicative interspecific interaction and does not directly contain the additive medusa-to-polyp recruitment term \(bM\) of the jellyfish model.

The deterministic predecessor for this jellyfish model already highlights the biological asymmetry of the stages: it identifies regimes in which polyps persist while medusae do not. The present result is the stochastic analogue needed for the exact two-stage SDE, and it supplies a quantitative pathwise lower bound plus a full mean-persistence conclusion independent of medusa noise.

Searches by the motivating DOI and title, stage-specific persistence, stochastic-logistic comparison, medusa-noise independence, and weighted-population time averages did not locate a published statement of this one-condition theorem for the 2022 jellyfish SDE.

## Limitations

The result removes the medusa-noise condition only from persistence in mean. It does not prove the source's stronger stochastic-permanence conclusion under arbitrary medusa noise.

The lower bound controls the polyp time average and therefore the weighted total. It does not imply a positive medusa time average.

The proof uses the positive recruitment sign \(bM\). Reversing that coupling or adding a direct negative medusa-dependent term to the polyp equation would invalidate the comparison.

The upper bound is deliberately coarse because it is used only to establish finite mean abundance; no claim of sharpness is made for that constant.

## References

1. Z. T. Win, B. Tian, “Population dynamical behaviors of jellyfish model with random perturbation,” Discrete and Continuous Dynamical Systems - B 28 (2023), 2994–3013. DOI: 10.3934/dcdsb.2022201. Early access 25 October 2022.
2. M. Liu, K. Wang, “Population dynamical behavior of Lotka-Volterra cooperative systems with random perturbations,” Discrete and Continuous Dynamical Systems 33 (2013), 2495–2522. DOI: 10.3934/dcds.2013.33.2495.
3. C. Lu, X. Ding, “Survival Analysis of a Nonautonomous Logistic Model with Stochastic Perturbation,” Journal of Applied Mathematics 2012 (2012), 692742. DOI: 10.1155/2012/692742.
4. Z. T. Win, B. Tian, S. Liu, “Asymptotic behaviors of jellyfish model with stage structure,” Mathematical Biosciences and Engineering 18 (2021), 2508–2526. DOI: 10.3934/mbe.2021128.
