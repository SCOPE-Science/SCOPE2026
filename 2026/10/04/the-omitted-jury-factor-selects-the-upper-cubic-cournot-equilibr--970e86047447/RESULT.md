# The omitted Jury factor selects the upper cubic-Cournot equilibrium branch
## Finding
For the cubic-cost Cournot map of Papadopoulos, Sarafopoulos and Ioannidis, define
\[
s=d(\mu-1),\qquad B=4(1+c_2)-s^2,
\]
and let the second equilibrium coordinate be a positive root of
\[
P(q)=6c_1q^2+Bq-\bigl(2(\alpha-c_3)+s(\alpha-c)\bigr)=0.
\]
At any positive equilibrium \((q_1^*,q_2^*)\) and any adjustment speed \(k>0\), the Jury quantity omitted from Proposition 2 factors exactly as
\[
1-\operatorname{tr}J+\det J
 =k^2q_1^*q_2^*P'(q_2^*).
\]
Under the delayed-feedback map of Proposition 3, the same quantity is
\[
1-\operatorname{tr}J_m+\det J_m
 =\frac{k^2}{(1+m)^2}q_1^*q_2^*P'(q_2^*).
\]
Therefore, when \(P\) has two distinct positive roots \(q_-<q_+\), the lower branch satisfies \(P'(q_-)<0\) and is unstable for every \(k>0\) and every admissible \(m\ge 0\). The upper branch satisfies \(P'(q_+)>0\). Thus the statement in the source that the second Jury inequality is always satisfied is false under its stated cubic-cost restrictions, and Propositions 2 and 3 require the additional branch condition \(P'(q_2^*)>0\).

An exact admissible counterexample also shows that the two displayed inequalities retained in each proposition can both hold while the omitted Jury inequality fails. Take
\[
\alpha=\frac75,\quad c=\frac25,\quad d=\frac12,\quad \mu=1,\quad
c_1=1,\quad c_2=-2,\quad c_3=\frac32,\quad c_4=0,
\]
so that
\[
q_1^*=\frac12,\qquad
q_- =\frac{10-\sqrt{70}}{30}.
\]
For \(k=1/100\), the source's two displayed conditions (40) and (41) are respectively
\[
\frac{731-33\sqrt{70}}{500}>0,
\qquad
\frac{595607+199\sqrt{70}}{150000}>0,
\]
but the omitted condition is
\[
1-\operatorname{tr}J+\det J
=\frac{7-\sqrt{70}}{150000}<0.
\]
Indeed the second diagonal eigenvalue in this witness is
\[
\lambda_2=\frac{1493+\sqrt{70}}{1500}>1.
\]
With delayed feedback \(m=1\), the retained conditions (48) and (49) are also positive,
\[
\frac{4393-199\sqrt{70}}{1500}>0,
\qquad
\frac{797069+133\sqrt{70}}{50000}>0,
\]
while
\[
1-\operatorname{tr}J_m+\det J_m
=\frac{7-\sqrt{70}}{600000}<0,
\qquad
\lambda_{2,m}=\frac{2993+\sqrt{70}}{3000}>1.
\]
Hence the lower positive equilibrium cannot be stabilized by this feedback law.

## Assumptions and scope
The claim concerns the modified two-firm discrete Cournot game in Sections 4 and 5 of the cited 2025 article. The source assumes a cubic second-player cost and states
\[
c_1>0,\qquad c_2\le 0,\qquad c_4\ge0,\qquad c_2^2\le3c_1c_3.
\]
The witness satisfies all four restrictions. Its marginal cost is
\[
3q^2-4q+\frac32,
\]
whose discriminant is \(-2\), so it is positive for every real \(q\). Both equilibrium coordinates are positive. No assertion is made about parameter restrictions not stated in the inspected model, global dynamics away from the equilibrium, or welfare interpretation.

## Proof
The source equilibrium equations give
\[
q_1^*=\frac{\alpha-c+s q_2^*}{2}
\]
and the quadratic equation \(P(q_2^*)=0\) above. Its derivative is
\[
P'(q)=12c_1q+B.
\]
The Jacobian printed by the source yields its second Jury condition
\[
1-\operatorname{tr}J+\det J
=k^2q_1^*q_2^*\bigl(B+12c_1q_2^*\bigr),
\]
which is exactly \(k^2q_1^*q_2^*P'(q_2^*)\). In the controlled map every Jacobian increment is scaled by \(1/(1+m)\), and the corresponding source expression is exactly the same factor multiplied by \(1/(1+m)^2\).

Because \(c_1>0\), if the quadratic has distinct real roots \(q_-<q_+\), then
\[
P'(q_-)<0<P'(q_+).
\]
If both roots are positive, all factors outside \(P'(q_-)\) in the Jury expression are positive. Hence the lower branch violates the necessary Jury condition for every positive \(k\), with or without admissible feedback. Equivalently, its characteristic polynomial \(\chi(\lambda)=\lambda^2-(\operatorname{tr}J)\lambda+\det J\) satisfies \(\chi(1)<0\) and tends to \(+\infty\) as \(\lambda\to+\infty\), so a real multiplier exceeds one.

For the displayed witness, \(s=0\), \(B=-4\), and
\[
P(q)=6q^2-4q+\frac15.
\]
Its two roots are \((10\pm\sqrt{70})/30\), both positive. Substitution into the source formulas gives the exact expressions in the Finding section. Their signs follow from \(8<\sqrt{70}<9\). The bundled verifier repeats these calculations with exact rational quadratic-surd arithmetic.

## Verification
`verifier.py` implements arithmetic in \(\mathbb{Q}(\sqrt{70})\) using Python's standard-library `fractions.Fraction`. It verifies the source cubic-cost restrictions, the exact equilibrium equation, positivity of both roots and both coordinates, positivity of the retained inequalities (40), (41), (48), and (49), negativity of the omitted Jury expression, and a multiplier strictly larger than one in both the uncontrolled and controlled witnesses. It prints `VERIFY_OK` only if every exact check passes.

The general branch theorem is symbolic: it follows from the identity between the missing Jury factor and \(P'(q_2^*)\). The finite witness is used only to disprove the sufficiency of the two displayed conditions as stated.

## Relationship to prior work
Papadopoulos, Sarafopoulos and Ioannidis derive the cubic equilibrium quadratic and explicitly write the three Jury inequalities, but they state that the second one is always satisfied and omit it from Propositions 2 and 3. Their numerical example uses parameters for which a unique positive equilibrium is reported, so it does not expose the two-positive-root branch issue.

The 2019 asymmetric-cost relative-profit model is a quadratic-cost predecessor, and the 2023 relative-profit chaos-control paper studies bifurcation and control in a different Cournot map. Neither inspected source contains the cubic-equilibrium derivative criterion above. Exact-title, DOI, proposition, Jury, lower-branch, and equivalent-factor searches located no source-specific published correction.

## Limitations
This result corrects the local linear stability criterion for the cubic-cost equilibrium branches. It does not classify all global invariant sets, establish the existence or absence of chaos for the counterexample, or invalidate the source's numerical conclusions for its separate parameter choice. The literature search cannot prove absolute novelty; the residual risk is an unindexed or differently phrased correction deriving the same branch condition.

## References
1. K. Papadopoulos, G. Sarafopoulos, and E. Ioannidis, “Delayed Feedback Chaos Control on a Cournot Game with Relative Profit Maximization,” *Mathematics* 13 (2025), 2328. DOI: 10.3390/math13152328.
2. G. Sarafopoulos and K. Papadopoulos, “Dynamics of a Cournot Game with Differentiated Goods and Asymmetric Cost Functions based on Relative Profit Maximization,” *European Journal of Interdisciplinary Studies* 11 (2019), 41–56. DOI: 10.24818/ejis.2019.08.
3. Z. Wei, W. Tan, A. A. Elsadany, and I. Moroz, “Complexity and chaos control in a Cournot duopoly model based on bounded rationality and relative profit maximization,” *Nonlinear Dynamics* 111 (2023), 17561–17589. DOI: 10.1007/s11071-023-08782-3.
