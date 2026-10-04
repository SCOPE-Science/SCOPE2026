# A corrected delay-independent predator-extinction threshold in a fear-stage model

## Finding

Consider the delayed predator-prey system
\[
P_1'
=
\frac{rP_1}{1+k f P_3(t-\tau_1)}
-d_1P_1-c_1P_1^2
-\frac{b_2P_1P_3}{(1+b_1P_1)(1+kb_3P_3)},
\]
\[
P_2'
=
\frac{\eta b_2P_1P_3}{(1+b_1P_1)(1+kb_3P_3)}
-(d_2+c_2)P_2,
\]
\[
P_3'
=
c_2P_2(t-\tau_2)-d_3P_3-c_3P_3^2.
\]

Assume all parameters are positive,
\[
\tau_1,\tau_2\ge0,
\]
the initial histories are positive and continuous, and
\[
r>d_1.
\]
Define the predator-free prey level
\[
K=\frac{r-d_1}{c_1}
\]
and the stage-reproduction quantity
\[
\mathcal R_P
=
\frac{\eta b_2c_2K}
{(1+b_1K)(d_2+c_2)d_3}.
\]

If
\[
\mathcal R_P<1,
\]
then for every choice of the two delays,
\[
P_2(t)\to0,
\qquad
P_3(t)\to0,
\qquad
P_1(t)\to K.
\]

This supplies a rigorous delay-independent sufficient condition for predator extinction in the printed model.

The source's preliminary extinction calculation contains a separate error. It states
\[
P_3'
\le
\left(\frac{\eta b_2}{b_1}-d_3\right)P_3-c_3P_3^2
\]
and then concludes
\[
\lim_{t\to\infty}P_3(t)
=
\frac{\eta b_2/b_1-d_3}{c_3}.
\]
The first inequality does not follow from the model because the exact adult-predator equation contains the positive delayed maturation input
\[
c_2P_2(t-\tau_2).
\]

For the parameter values used in the source's Figure 3,
\[
\eta=\frac12,\quad
b_2=\frac35,\quad
b_1=\frac12,\quad
c_2=\frac45,\quad
d_3=\frac1{10},\quad
c_3=\frac1{50},
\]
and at a state with
\[
P_2(t-\tau_2)=P_3(t)=1,
\]
the exact adult derivative is
\[
P_3'
=
\frac45-\frac1{10}-\frac1{50}
=
\frac{17}{25}
=
0.68,
\]
whereas the asserted upper right-hand side is
\[
\left(
\frac{(1/2)(3/5)}{1/2}-\frac1{10}
\right)
-\frac1{50}
=
\frac{12}{25}
=
0.48.
\]
Thus the displayed differential inequality is false.

The published limit formula is also incompatible with the same paper's stable coexistence example. Solving the printed nondelayed equilibrium equations at all of its Figure 3 parameters gives
\[
P_3^*
=
4.28272994079448\ldots,
\]
while the displayed Section-2 expression equals
\[
\frac{(1/2)(3/5)/(1/2)-1/10}{1/50}=25.
\]

The corrected theorem also explains why the paper's qualitative sufficient condition
\[
\frac{\eta b_2}{b_1}<d_3
\]
can still be true even though its proof is invalid: that condition is stronger than
\[
\mathcal R_P<1.
\]

## Assumptions and scope

The theorem applies to the exact delayed system written above, with positive parameters and positive continuous histories.

The strict condition
\[
\mathcal R_P<1
\]
is sufficient. No necessity claim is made at
\[
\mathcal R_P=1
\]
or above it.

The result is uniform in both delays. The first delay affects only the fear term in prey reproduction, while the second enters the maturation flux.

The theorem concerns predator extinction and convergence to the predator-free prey state. It does not reclassify the source's Hopf, saddle-node, transcritical, homoclinic, or bistability computations.

## Proof

The prey equation immediately gives
\[
P_1'
\le
(r-d_1)P_1-c_1P_1^2.
\]
Therefore
\[
\limsup_{t\to\infty}P_1(t)\le K.
\]

Fix
\[
\varepsilon>0
\]
small enough that
\[
A_\varepsilon c_2
<
(d_2+c_2)d_3,
\]
where
\[
A_\varepsilon
=
\frac{\eta b_2(K+\varepsilon)}
{1+b_1(K+\varepsilon)}.
\]
Such an \(\varepsilon\) exists because
\[
\mathcal R_P<1.
\]

For all sufficiently large \(t\),
\[
P_1(t)\le K+\varepsilon.
\]
The juvenile-predator recruitment term then satisfies
\[
\frac{\eta b_2P_1P_3}
{(1+b_1P_1)(1+kb_3P_3)}
\le
A_\varepsilon P_3.
\]
Hence, writing
\[
q=d_2+c_2,
\]
one has
\[
P_2'\le A_\varepsilon P_3-qP_2.
\]

Choose \(\alpha\) such that
\[
\frac{A_\varepsilon}{d_3}
<
\alpha
<
\frac{q}{c_2}.
\]
The interval is nonempty exactly because
\[
A_\varepsilon c_2<qd_3.
\]

Define
\[
L(t)
=
P_2(t)+\alpha P_3(t)
+\alpha c_2\int_{t-\tau_2}^{t}P_2(s)\,ds.
\]
Differentiation and use of the exact adult-predator equation give
\[
\begin{aligned}
L'
&\le
A_\varepsilon P_3-qP_2
+\alpha\bigl(c_2P_2(t-\tau_2)-d_3P_3-c_3P_3^2\bigr)\\
&\quad
+\alpha c_2\bigl(P_2(t)-P_2(t-\tau_2)\bigr)\\
&=
-\bigl(q-\alpha c_2\bigr)P_2
-\bigl(\alpha d_3-A_\varepsilon\bigr)P_3
-\alpha c_3P_3^2.
\end{aligned}
\]
Both linear coefficients are strictly positive. Thus \(L\) is eventually nonincreasing and
\[
\int^\infty P_2(t)\,dt<\infty,
\qquad
\int^\infty P_3(t)\,dt<\infty.
\]

The same estimate bounds \(P_2\) and \(P_3\); the logistic comparison bounds \(P_1\). Consequently the right-hand sides of the delay system are bounded, so \(P_2\) and \(P_3\) are uniformly continuous. Barbalat's lemma yields
\[
P_2(t)\to0,
\qquad
P_3(t)\to0.
\]

Finally, the prey equation can be written
\[
P_1'
=
P_1\bigl(g(t)-c_1P_1\bigr),
\]
where
\[
g(t)
=
\frac{r}{1+k f P_3(t-\tau_1)}
-d_1
-\frac{b_2P_3(t)}
{(1+b_1P_1(t))(1+kb_3P_3(t))}.
\]
Since
\[
P_3(t)\to0,
\]
also
\[
P_3(t-\tau_1)\to0,
\]
and therefore
\[
g(t)\to r-d_1>0.
\]
Standard scalar comparison with logistic equations having coefficients
\[
r-d_1\pm\delta
\]
then gives
\[
P_1(t)\to\frac{r-d_1}{c_1}=K.
\]

To compare with the source's simpler condition, observe
\[
\frac{K}{1+b_1K}<\frac1{b_1}
\]
and
\[
\frac{c_2}{d_2+c_2}<1.
\]
Hence
\[
\frac{\eta b_2}{b_1}<d_3
\]
implies
\[
\mathcal R_P<1.
\]
So the source's qualitative extinction condition survives as a stricter sufficient condition, although the displayed proof and limiting value do not.

## Verification

The bundled `verify.py` checks three independent pieces.

First, with the Figure 3 parameters it evaluates the exact adult-predator derivative at
\[
P_2(t-\tau_2)=P_3(t)=1
\]
and obtains
\[
0.68,
\]
while the source's asserted upper bound is
\[
0.48.
\]

Second, it solves the source's printed nondelayed equilibrium equations at the Figure 3 parameter set and obtains
\[
(P_1^*,P_2^*,P_3^*)
\approx
(3.653998959363385,\,
0.993885636243748,\,
4.282729940794482).
\]
The residual norm is below the numerical tolerance, whereas the source's displayed limit formula evaluates to \(25\).

Third, an exact rational parameter witness
\[
r=\frac{11}{10},\quad
d_1=1,\quad
c_1=1,\quad
b_1=1,\quad
b_2=\frac15,\quad
\eta=1,\quad
c_2=1,\quad
d_2=1,\quad
d_3=\frac1{10}
\]
has
\[
K=\frac1{10},
\qquad
\mathcal R_P=\frac1{11}<1,
\]
even though
\[
\frac{\eta b_2}{b_1}=\frac15>d_3.
\]
Thus the corrected criterion rigorously covers parameter regimes not covered by the source's simpler sufficient condition.

## Relationship to prior work

Kong and Shao introduce the exact three-variable delayed fear-stage model studied here. Their preparation section prints the adult-predator inequality and the limiting expression corrected above, and their Figure 3 gives a stable coexistence parameter set whose equilibrium is incompatible with that expression.

Li, Sun, and Liu study a different stage-structured Crowley-Martin predator-prey model and prove a sharp reproduction-number threshold between predator extinction and permanence. Their maturation mechanism is not the same: mature predator recruitment is represented through a delayed birth flux with an explicit juvenile survival factor, while the present model keeps an explicit juvenile state and feeds delayed juvenile density into the adult equation. Their work establishes that reproduction-number threshold analysis is prior art, but it does not state the present model's Lyapunov-Krasovskii criterion or correct the Kong-Shao calculation.

Liu and Beretta similarly develop threshold dynamics for a Beddington-DeAngelis stage-structured predator-prey model. This is broader methodological precedent for stage-reproduction thresholds, not statement-level coverage of the source-specific correction.

The new content is therefore restricted to the exact Kong-Shao equations: the false pointwise inequality and false adult-limit formula are identified, a stronger valid delay-independent extinction condition is proved for that model, and both a source-parameter contradiction and an exact parameter witness are supplied.

## Limitations

The theorem proves only the strict sufficient regime
\[
\mathcal R_P<1.
\]
It does not establish a necessary-and-sufficient global threshold for the full fear-delay model.

The source's Figure 3 equilibrium is used only to refute the claimed universal adult-predator limiting formula; no claim is made here about the correctness of all of the paper's numerical bifurcation diagrams.

The adult competition term
\[
-c_3P_3^2
\]
is retained in the proof but is not needed to make the strict threshold work. A sharper critical-case result may therefore be possible.

The older stage-structured literature contains related threshold methods in different model formulations. The result does not claim novelty for Lyapunov-Krasovskii extinction arguments in general.

## References

1. W. Kong, Y. Shao, “The effects of fear and delay on a predator-prey model with Crowley-Martin functional response and stage structure for predator,” AIMS Mathematics 8 (2023), 29260–29289. DOI: 10.3934/math.20231498.
2. N. Li, W. Sun, S. Liu, “A stage-structured predator-prey model with Crowley-Martin functional response,” Discrete and Continuous Dynamical Systems - B 28 (2023), 2463–2489. DOI: 10.3934/dcdsb.2022177.
3. S. Liu, E. Beretta, “A stage-structured predator-prey model of Beddington-DeAngelis type,” SIAM Journal on Applied Mathematics 66 (2006), 1101–1129. DOI: 10.1137/050630003.
