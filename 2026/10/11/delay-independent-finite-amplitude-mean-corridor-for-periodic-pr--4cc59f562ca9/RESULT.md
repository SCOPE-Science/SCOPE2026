# Delay-independent finite-amplitude mean corridor for periodic predator–prey branches
## Finding
Consider the delayed predator–prey system
\[
\dot u(t)=u(t)(1-u(t))-\frac{s u(t)v(t)}{{m+\alpha\beta+u(t)}},
\]
\[
\dot v(t)=\delta v(t)\left(n+\frac{{\beta-v(t-\tau)}}{{\alpha\beta+u(t-\tau)}}\right),
\]
with
\[
s,m,\alpha,\beta,\delta,n>0,\qquad \tau\ge 0.
\]
Write
\[
p=\alpha\beta,\qquad q=m+\alpha\beta,
\]
and for a strictly positive \(T\)-periodic solution define
\[
\bar f=\frac1T\int_0^T f(t)\,dt,
\qquad
\operatorname{{Var}}_T(u)=\overline{{u^2}}-\bar u^2.
\]

Every strictly positive nonconstant periodic solution obeys the exact finite-amplitude law
\[
\boxed{{
\bar v=
\frac{{(q+\bar u)(1-\bar u)-\operatorname{{Var}}_T(u)}}s
}}.
\]
Because a nonconstant positive periodic solution has \(\operatorname{{Var}}_T(u)>0\),
\[
\bar v<\frac{{(q+\bar u)(1-\bar u)}}s.
\]
Thus temporal prey variation creates an exact predator-mean deficit below the prey nullcline evaluated at the mean prey density.

The predator equation supplies two additional, delay-independent constraints on the prey mean:
\[
\boxed{{
\bar u>1-s\left(n+\frac1\alpha\right)
}},
\]
and
\[
\boxed{{
1-\bar u>
\frac{{sp}}q\left(n+\frac{{\beta}}{{p+\bar u}}\right)
}}.
\]
They hold at arbitrary periodic-orbit amplitude and for every delay for which a strictly positive periodic orbit exists.

For the numerical Case 2 in the source,
\[
s=\frac15,\quad m=\frac1{{10}},\quad \alpha=1,\quad
\beta=\frac35,\quad \delta=\frac3{{10}},\quad n=\frac25,
\]
the bounds reduce to
\[
\boxed{{
\frac{{18}}{{25}}<\bar u<
\frac{{29+\sqrt{{14806}}}}{{175}}
=0.8610280454586158\ldots
}}.
\]
The exact mean law becomes
\[
\boxed{{
\bar v=5\left(\frac7{{10}}+\bar u\right)(1-\bar u)
-5\operatorname{{Var}}_T(u)
}}.
\]
The source's coexistence equilibrium has
\[
u_*=
\frac{{11+\sqrt{{5441}}}}{{100}}
=0.8476313442364011\ldots,
\]
so every positive finite-amplitude periodic branch in this benchmark has mean prey below \(0.861029\), only about \(0.013397\) above the equilibrium prey level.

## Assumptions and scope
The result applies to classical strictly positive periodic solutions of the displayed autonomous delay system. Strict positivity means \(u(t)>0\) and \(v(t)>0\) for all \(t\). No small-amplitude assumption is used. The period need not equal the delay. The result is conditional: it constrains any positive periodic solution that exists, but does not assert that a periodic solution exists for every parameter or delay.

The source proves local Hopf bifurcation and, under its hypotheses, global continuation/existence of periodic solutions. The present claim adds branch-wide finite-amplitude mean constraints that are independent of \(\tau\) and \(\delta\).

## Proof
Let \((u,v)\) be a strictly positive \(T\)-periodic solution. At a time when \(u\) attains its maximum, the prey equation and positivity give
\[
1-u=\frac{{sv}}{{q+u}}>0.
\]
Hence
\[
0<u(t)<1
\]
for every \(t\).

Divide the prey equation by \(u(t)\), integrate over one period, and use periodicity of \(\log u\):
\[
0=1-\bar u-s\overline{{\frac{v}{q+u}}}.
\]
With
\[
W(t)=\frac{{v(t)}}{{q+u(t)}},
\]
this is
\[
\bar W=\frac{{1-\bar u}}s.
\]
Averaging the prey equation itself gives
\[
0=\bar u-\overline{{u^2}}-s\overline{{uW}},
\]
so
\[
\overline{{uW}}
=\frac{{\bar u(1-\bar u)-\operatorname{{Var}}_T(u)}}s.
\]
Since \(v=(q+u)W\),
\[
\bar v=q\bar W+\overline{{uW}}
=\frac{{(q+\bar u)(1-\bar u)-\operatorname{{Var}}_T(u)}}s.
\]
If \(\operatorname{{Var}}_T(u)=0\), then \(u\) is constant; the prey equation then forces \(v\) to be constant, contradicting nonconstancy. Therefore the variance term is strictly positive for every nonconstant periodic orbit.

Next divide the predator equation by \(\delta v(t)\) and average. A period average is invariant under a time shift, hence
\[
\overline{{\frac{v}{p+u}}}
=n+\beta\overline{{\frac1{{p+u}}}}.
\]
Set
\[
Z(t)=\frac{{v(t)}}{{p+u(t)}}.
\]
Because \(q=p+m\) and \(m>0\), positivity of \(u\) implies
\[
\frac pq<\frac{{p+u}}{{q+u}}<1.
\]
Also
\[
W=\frac{{p+u}}{{q+u}}Z.
\]
Therefore
\[
\frac pq\,\bar Z<\bar W<\bar Z.
\]
Using \(u>0\),
\[
\bar Z=n+\beta\overline{{\frac1{{p+u}}}}
<n+\frac\beta p
=n+\frac1\alpha.
\]
Combining this with \(\bar W=(1-\bar u)/s\) yields
\[
\bar u>1-s\left(n+\frac1\alpha\right).
\]

For the opposite comparison, convexity of \(x\mapsto 1/(p+x)\) gives Jensen's inequality
\[
\overline{{\frac1{{p+u}}}}\ge \frac1{{p+\bar u}}.
\]
Hence
\[
\frac{{1-\bar u}}s=\bar W
>\frac pq\bar Z
\ge
\frac pq\left(n+\frac{{\beta}}{{p+\bar u}}\right),
\]
which proves the second mean constraint.

For Case 2, the latter inequality becomes
\[
875\bar u^2-290\bar u-399<0.
\]
Its positive root is
\[
\frac{{29+\sqrt{{14806}}}}{{175}},
\]
while the first inequality gives \(\bar u>18/25\). The source's equilibrium formula uses the positive root of \(u^2+Au+B=0\). With the Case 2 parameters,
\[
A=-\frac{{11}}{{50}},\qquad B=-\frac{{133}}{{250}},
\]
which gives
\[
u_*=(11+\sqrt{{5441}})/100.
\]

## Verification
The bundled checker replays the exact Case 2 algebra with rational arithmetic. It verifies the lower bound, the quadratic whose positive root gives the upper mean-prey bound, the coexistence-equilibrium quadratic, and the algebraic moment identity underlying the predator-mean defect. The stored checker output is `VERIFY_OK`.

The proof of the all-parameter theorem is analytic and does not depend on finite simulation or numerical continuation. The decimal values are evaluations of exact radicals.

## Relationship to prior work
Wu and Zheng introduced the delayed system above, studied equilibrium stability and local Hopf bifurcation, and proved global existence of periodic solutions after successive critical delays under their hypotheses. Their complete publisher text was inspected at the model, global-periodic-solution, and numerical-example sections. Searches within that text found no period-mean or average-population statement; its global result concerns existence and continuation, not the finite-amplitude mean geometry proved here.

The nondelayed motivating predecessor of Basheer, Quansah, and Parshad uses a related additional-food Holling–Tanner model but a different prey functional-response denominator. It motivated the delayed source but does not imply the present delay-independent mean corridor from the material inspected. A later paper by Yu, Wang, and Zhai cites Wu–Zheng while studying a different ratio-dependent bioeconomic model with harvesting; its stated Hopf and control results do not imply the current mean identities.

Targeted literature searches used the same object name together with time average, mean prey, mean predator, periodic orbit, variance, additional food, and delay-independent bound formulations. The closest returned results concerned other dynamical systems or generic recurrence balances, not this model or these inequalities.

## Limitations
The theorem does not determine the period, phase, extrema, Floquet multipliers, Hopf direction, uniqueness, or stability of a periodic orbit. It does not extend automatically to nonperiodic recurrent states because the delayed state lives in an infinite-dimensional phase space and the present proof uses period-shift invariance directly. The lower general bound can be noninformative when \(s(n+1/\alpha)\ge1\); the Case 2 specialization is informative on both sides.

A short averaging identity can be rediscovered under different terminology, so unindexed literature remains a residual originality risk. The 2019 motivating predecessor was not available here as complete lawful full text; only its bibliographic record and the delayed source's explicit presentation of the predecessor model were used. No novelty is claimed for the equations, coexistence equilibrium, Hopf thresholds, or existence of periodic solutions.

## References
1. L. Wu and H. Zheng, “Hopf bifurcation in a delayed predator-prey system with asymmetric functional response and additional food,” *AIMS Mathematics* 6 (2021), 12225–12244. DOI 10.3934/math.2021708.
2. A. Basheer, E. Quansah, and R. D. Parshad, “The effect of additional food in Holling Tanner type models,” *International Journal of Dynamics and Control* 7 (2019), 1195–1212. DOI 10.1007/s40435-019-00580-3.
3. T. Yu, Q. Wang, and S. Zhai, “Exploration on dynamics in a ratio-dependent predator-prey bioeconomic model with time delay and additional food supply,” *Mathematical Biosciences and Engineering* 20 (2023), 15094–15119. DOI 10.3934/mbe.2023676.
