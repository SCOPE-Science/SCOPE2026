# Strong behavioral inhibition leaves a herd-threshold final-size floor

## Finding

Consider
\[
\dot S=-\frac{\beta SI}{1+\epsilon I},
\qquad
\dot I=\frac{\beta SI}{1+\epsilon I}-\alpha I,
\]
with
\[
S(0)=S_0>0,\qquad I(0)=I_0>0,
\]
and
\[
\beta S_0>\alpha.
\]

Let \(S_\infty(\epsilon)\) be the susceptible population remaining as \(t\to\infty\). For every fixed
\[
q\in\left(\frac{\alpha}{\beta S_0},1\right),
\]
there are \(C>0\) and \(\epsilon_0>0\) such that for all \(\epsilon\ge\epsilon_0\),
\[
0<
\left(\frac{\alpha}{\beta}-\frac1\epsilon\right)-S_\infty(\epsilon)
\le
C\epsilon q^{\alpha\epsilon/\beta}.
\]
Hence
\[
S_\infty(\epsilon)
=
\frac{\alpha}{\beta}-\frac1\epsilon
+
O\!\left(\epsilon q^{\alpha\epsilon/\beta}\right),
\]
and
\[
\lim_{\epsilon\to\infty}S_\infty(\epsilon)=\frac{\alpha}{\beta}.
\]

The eventual susceptible depletion therefore satisfies
\[
\lim_{\epsilon\to\infty}
\left(S_0-S_\infty(\epsilon)\right)
=
S_0-\frac{\alpha}{\beta}.
\]
Strong behavioral inhibition does not drive cumulative susceptible infection to zero in the supercritical case.

For
\[
S_0=200,\qquad I_0=2,\qquad \alpha=2,\qquad \beta=0.2,
\]
the source parameter set gives
\[
S_\infty(\epsilon)\to10,
\qquad
S_0-S_\infty(\epsilon)\to190.
\]

## Assumptions and scope

All parameters are positive and
\[
\beta S_0>\alpha.
\]
The behavioral parameter \(\epsilon\) is fixed during each trajectory and then taken to infinity across the model family.

The final size is the number of initially susceptible individuals infected,
\[
S_0-S_\infty.
\]
It excludes the initially infected population.

The result concerns long-time cumulative depletion. Peak prevalence, peak time, and epidemic duration can still change substantially with \(\epsilon\).

## Proof

The source integrates the phase equation and obtains, with
\[
x=\frac{S}{S_0},
\qquad
\sigma=\frac{\alpha\epsilon}{\beta},
\]
the exact relation
\[
I
=
I_0x^\sigma
-\frac1\epsilon(1-x^\sigma)
+
S_0\frac{x-x^\sigma}{\sigma-1}.
\]
At the final state \(I=0\), the source's unique positive final-state root \(x_\infty\) therefore satisfies
\[
-\frac1\epsilon
+
\frac{S_0}{\sigma-1}x_\infty
+
A_\epsilon x_\infty^\sigma
=
0,
\]
where
\[
A_\epsilon
=
I_0+\frac1\epsilon-\frac{S_0}{\sigma-1}.
\]

Define
\[
a_\epsilon
=
\frac{\sigma-1}{\epsilon S_0}
=
\frac{\alpha}{\beta S_0}
-\frac1{\epsilon S_0}
\]
and
\[
C_\epsilon
=
\frac{\sigma-1}{S_0}A_\epsilon.
\]
The final-state equation is exactly
\[
x_\infty-a_\epsilon+C_\epsilon x_\infty^\sigma=0.
\]

Since
\[
A_\epsilon\to I_0>0,
\]
one has \(C_\epsilon>0\) for all sufficiently large \(\epsilon\), with
\[
C_\epsilon=O(\epsilon).
\]
Therefore
\[
0<x_\infty<a_\epsilon.
\]

Put
\[
r=\frac{\alpha}{\beta S_0}<1
\]
and fix any \(q\in(r,1)\). Since \(a_\epsilon\to r\), for sufficiently large \(\epsilon\),
\[
x_\infty<a_\epsilon<q.
\]
The exact root equation then gives
\[
0<a_\epsilon-x_\infty
=
C_\epsilon x_\infty^\sigma
\le
C_1\epsilon q^\sigma
=
C_1\epsilon q^{\alpha\epsilon/\beta}
\]
for some \(C_1>0\).

Multiplying by \(S_0\) and using
\[
S_0a_\epsilon
=
\frac{\alpha}{\beta}-\frac1\epsilon
\]
proves
\[
0<
\left(\frac{\alpha}{\beta}-\frac1\epsilon\right)-S_\infty(\epsilon)
\le
C\epsilon q^{\alpha\epsilon/\beta}.
\]
The right-hand side decays exponentially, proving the limit.

## Verification

The bundled `verify.py` reconstructs the source final-state equation and its transformed form using exact rational arithmetic at the source parameter values.

For the source's displayed large behavioral value
\[
\epsilon=9.8,
\]
one has
\[
\sigma=98
\]
exactly. The checker proves that the final-state root lies strictly below
\[
a_\epsilon
=
\frac{\alpha}{\beta S_0}
-\frac1{\epsilon S_0}
\]
by evaluating the exact final-state polynomial at \(0\) and \(a_\epsilon\).

The infinite-\(\epsilon\) conclusion is established analytically by the proof above; finite checks are only reproducibility tests.

## Relationship to prior work

The motivating article derives the exact phase relation, proves uniqueness of the final epidemic state, and studies how the behavioral parameter changes epidemic characteristics. It does not derive the strong-inhibition limit of \(S_\infty\).

A later primary study of final epidemic size under generalized contact and nonlinear incidence treats population-size-dependent contact rates and power-law incidence of the form
\[
\beta s^p i^q.
\]
That nonlinear family does not contain the prevalence-denominator incidence
\[
\frac{\beta SI}{1+\epsilon I}
\]
as analyzed there and does not imply the \(\epsilon\to\infty\) limit proved here.

The broader fact that behavior can reduce epidemic peaks or final size is established. The source-specific content is the exact strong-inhibition asymptotic and the nonzero limiting susceptible depletion.

## Limitations

The theorem assumes permanent fixed behavioral response and the deterministic model exactly as stated.

No claim is made for
\[
\beta S_0\le\alpha
\]
or for incidence laws with different low-prevalence behavior.

The result is a mathematical property of the model, not a claim about the effectiveness of real-world behavioral interventions.

## References

1. J. Li, X. Wang, X. Lin, “Impact of behavioral change on the epidemic characteristics of an epidemic model without vital dynamics,” Mathematical Biosciences and Engineering 15 (2018), 1425–1434. DOI: 10.3934/mbe.2018065.
2. W. Gao, Y. Wang, J. Cao, Y. Liu, “Final epidemic size and critical times for susceptible–infectious–recovered models with a generalized contact rate,” Chaos 34 (2024), 013152. DOI: 10.1063/5.0185707.
