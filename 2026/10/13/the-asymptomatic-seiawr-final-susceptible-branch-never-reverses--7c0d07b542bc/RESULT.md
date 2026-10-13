# The asymptomatic SEIAWR final susceptible branch never reverses with transmission

## Finding

For the short-term SEIAWR model, use the same final-size simplification as the source,
\[
I(0)=A(0)=W(0)=0.
\]
Define
\[
s_0=\frac{S(0)}N,
\qquad
x=\frac{S(\infty)}N.
\]
For a genuinely seeded outbreak, \(E(0)>0\), so \(0<s_0<1\). The source's exact final-size relation becomes
\[
\log\frac{s_0}{x}=\mathcal R_0(1-x).
\]

The physically admissible root is unique for every \(\mathcal R_0>0\), always obeys
\[
\mathcal R_0x<1,
\]
and consequently satisfies
\[
\frac{dx}{d\mathcal R_0}
=
\frac{1-x}{\mathcal R_0-1/x}<0.
\]
Thus the final susceptible population is strictly decreasing with the reproduction number throughout the seeded branch. It never reverses and becomes increasing at large \(\mathcal R_0\).

This corrects the source's subsequent parameter conclusions. Since
\[
\frac{\partial\mathcal R_0}{\partial k}
=
\frac{pN\beta}{\gamma'},
\]
for \(p>0\) the final susceptible population is strictly decreasing in the asymptomatic-transmission proportion \(k\). For fixed \(k\), the reproduction number is affine in \(p\), so the final susceptible size changes with the opposite sign to \(\partial\mathcal R_0/\partial p\). No extra reversal of the final-size branch creates three additional critical values of \(k\).

The paper's numerical value also selects the nontrivial implicit branch. If \(S(0)=N\) is imposed together with the zero initial values above, then \(E(0)=0\) as well, and the exact ODE remains disease free with \(S(\infty)=N\). At the source value
\[
\mathcal R_0=1.188808,
\]
the lower root of the implicit equation with \(s_0=1\) is
\[
x_-=0.700135812028657\ldots,
\]
matching the reported \(0.700135\). That lower root is the limit selected by arbitrarily small positive seeding, not the final state of an exactly unseeded deterministic trajectory.

## Assumptions and scope

The result concerns the source's short-term SEIAWR model without demographic turnover. All transmission, progression, recovery, shedding, and pathogen-decay parameters are positive, and the total human population \(N\) is constant.

The strict monotonicity theorem assumes a genuine exposed seed,
\[
E(0)>0,
\]
under the source simplification
\[
I(0)=A(0)=W(0)=0.
\]
Then
\[
S(0)=N-E(0)<N.
\]

The zero-seed branch statement is separate: if \(S(0)=N\) and all infected or exposed compartments are zero, the deterministic solution remains disease free.

The term “final size” here follows the source's usage for the final susceptible population \(S(\infty)\), not the attack size \(N-S(\infty)\).

## Proof

Put
\[
f(x)=\log\frac{s_0}{x}-\mathcal R_0(1-x),
\qquad
0<x\le s_0<1.
\]
Then
\[
\lim_{x\downarrow0}f(x)=+\infty,
\qquad
f(s_0)=-\mathcal R_0(1-s_0)<0.
\]
Also
\[
f'(x)=\mathcal R_0-\frac1x,
\qquad
f''(x)=\frac1{x^2}>0.
\]
Hence \(f\) is strictly convex. If \(1/\mathcal R_0\ge s_0\), it is strictly decreasing on the full admissible interval and has exactly one root. If \(1/\mathcal R_0<s_0\), it decreases until \(1/\mathcal R_0\) and then increases; because its value at \(s_0\) is still negative, the increasing segment contains no zero, while the decreasing segment contains exactly one. Thus the physical root is unique.

The root must satisfy
\[
x<\frac1{\mathcal R_0}.
\]
Indeed, suppose instead that \(x\ge1/\mathcal R_0\). Then \(f'\ge0\) on \([x,s_0]\), so
\[
f(s_0)\ge f(x)=0,
\]
contradicting
\[
f(s_0)<0.
\]
Therefore
\[
\mathcal R_0-\frac1x<0.
\]

Implicit differentiation of
\[
\log\frac{s_0}{x}=\mathcal R_0(1-x)
\]
gives
\[
\frac{dx}{d\mathcal R_0}
=
\frac{1-x}{\mathcal R_0-1/x}.
\]
The numerator is positive and the denominator is negative, proving strict decrease for every positive \(\mathcal R_0\).

The short-term reproduction number printed by the source is affine in \(p\) and \(k\), with
\[
\frac{\partial\mathcal R_0}{\partial k}
=
\frac{pN\beta}{\gamma'}.
\]
Thus, for \(p>0\), the chain rule gives
\[
\frac{dS(\infty)}{dk}<0.
\]
For fixed \(k\), \(\partial\mathcal R_0/\partial p\) is independent of \(p\), so there is at most one \(k\)-value at which the sign of the \(p\)-effect changes, and the sign for \(S(\infty)\) is the opposite of the sign for \(\mathcal R_0\).

Finally take \(s_0=1\). The implicit equation always has the root \(x=1\). When \(\mathcal R_0>1\), strict convexity gives one additional root in \((0,1/\mathcal R_0)\). The exact ODE with zero exposed, infected, asymptomatic, and reservoir seed selects \(x=1\), while the lower root is approached from positive seeds. At \(\mathcal R_0=1.188808\), direct root evaluation gives the numerical value stated in the finding.

## Verification

The bundled `verify.py` checks the implicit derivative algebra, verifies the source numerical lower root to high precision, verifies that its derivative is negative, and confirms that both \(x=1\) and the lower branch solve the zero-seed implicit equation when \(\mathcal R_0>1\).

The uniqueness and sign proof are analytic and do not rely on a numerical parameter scan.

## Relationship to prior work

Classical epidemic final-size theory already establishes logarithmic final-size relations and, in standard settings, monotone reduction of the remaining susceptible population as transmission strength increases. Arino, Brauer, van den Driessche, Watmough, and Wu derive final-size relations for a broad class of epidemic models. Hsu and Roeger explicitly prove decrease of final susceptible population with an acting reproduction number in a SARS model.

The contribution here is therefore not a new generic monotonicity principle. It is the source-specific diagnosis that the 2020 asymptomatic-transmission paper draws the opposite high-\(\mathcal R_0\) conclusion from its own implicit equation, propagates that reversal into its \(k\)- and \(p\)-sensitivity discussion, and numerically reports the nontrivial lower root under an exactly unseeded normalization that selects the trivial root dynamically.

Targeted searches by DOI, exact title, final-size reversal terminology, branch selection, and the source's reported numerical value did not locate a published correction of these statements.

## Limitations

The result concerns the source's short-term deterministic model and the final susceptible population. It does not revise the long-term model's equilibrium stability analysis.

When the initial exposed seed is extremely small and \(\mathcal R_0>1\), the seeded final state approaches the lower nontrivial root, so that root remains epidemiologically meaningful as a singular small-seed limit even though it is not the trajectory selected by exactly zero seeding.

The analysis does not address stochastic importation, for which an exactly disease-free initial condition can later become infected.

## References

1. J. Lv, S. Guo, J.-A. Cui, J. P. Tian, “Asymptomatic transmission shifts epidemic dynamics,” Mathematical Biosciences and Engineering 18 (2021), 92–111. DOI: 10.3934/mbe.2021005.
2. J. Arino, F. Brauer, P. van den Driessche, J. Watmough, J. Wu, “A final size relation for epidemic models,” Mathematical Biosciences and Engineering 4 (2007), 159–175. DOI: 10.3934/mbe.2007.4.159.
3. S.-B. Hsu, L.-I. W. Roeger, “The final size of a SARS epidemic model without quarantine,” Journal of Mathematical Analysis and Applications 333 (2007), 557–566. DOI: 10.1016/j.jmaa.2006.11.026.
