# A sharp storm-ordering window for saturation runoff in a periodic linear store

## Finding
Consider three equally spaced rainfall additions, repeated forever, with fixed total depths but freely permuted temporal order. In the finite-capacity linear-loss store defined below, put the three depths in ascending order \(a\), \(b\), \(c\), where \(0\le a\le b\le c\). Denote total runoff in the unique periodic state by \(W_{abc}\) for the cycle \((a,b,c)\), and \(W_{acb}\) for \((a,c,b)\). Then

\[
W_{abc}\ge W_{acb}
\]

for every capacity \(C>0\) and retention factor \(0<q<1\). If \(a<b<c\), the inequality is strict **if and only if**

\[
\boxed{\frac{b+qa}{1-q^2}<C<\frac{c+qb+q^2a}{1-q^3}}.
\]

If any two depths coincide, or the capacity lies outside the displayed open interval, the two cyclic orders give **exactly the same** total runoff. For three distinct depths this interval is nonempty, so time ordering can matter even though total rainfall and reservoir parameters do not change. Up to cyclic rotation, these are the only two different orderings of three depths; thus the result classifies every permutation.

The period length three is minimal for order sensitivity under equally spaced events: with one or two event positions, reversing the sequence is merely a cyclic rotation.

## Assumptions and scope
A nonnegative water store has a positive finite capacity \(C\). Between equally spaced instantaneous rain events, storage is multiplied by a fixed retention factor \(0<q<1\), representing first-order loss. Each event \(u_i\ge0\) first adds rainfall and then sheds all excess above capacity. Storage immediately after the event is \(x_i\); runoff from that event is \(w_i\):

\[
x_i=\min\{C,qx_{i-1}+u_i\},\qquad
w_i=(qx_{i-1}+u_i-C)_+.
\]

The rainfall depths \(a,b,c\) repeat in the chosen cyclic order. The three-step storage map contracts distances by at most \(q^3<1\), hence it has a unique globally attracting three-periodic state. The criterion concerns the sum of the three saturation-excess runoff volumes in that state, not peak discharge, risk under random rainfall, or transient runoff from a specified starting moisture.

## Proof
Write \(f_u(x)=\min\{C,qx+u\}\), \(U=a+b+c\), and \([z]_+=\max(0,z)\). In the periodic state, mass balance gives

\[
W=U-(1-q)(x_1+x_2+x_3).
\]

**Anchored-storage lemma.** For any periodic rainfall cycle, hypothetically set the post-event storage at one selected position to \(C\), then propagate the other storage values with the maps \(f_u\). Let \(S_j\) be the sum of these three hypothetical post-event storages for anchor \(j\). Because every map is nondecreasing and actual post-event storage is at most \(C\), each hypothetical state dominates the corresponding periodic state and \(S_j\) is at least the actual storage sum. If actual positive runoff occurs, some event has post-event storage \(C\), and anchoring at that event reproduces the entire periodic triple. If no positive runoff occurs, mass balance gives \(W=0\). Therefore, for all parameters,

\[
W=\max\{0,\max_j[U-(1-q)S_j]\}.
\]

For the increasing cycle \((a,b,c)\), if either of the first two positions is saturated, the last position is also saturated. Indeed, a saturated event with depth \(a\) or \(b\) requires that depth to be at least \((1-q)C\), and the later, no-smaller depths then preserve saturation. Consequently the last position is a valid anchor whenever any runoff occurs. Define

\[
A=f_a(C),\quad B=f_b(A),\quad D=f_c(A),\quad
E=f_b(C),\quad F=f_a(E).
\]

It follows from the anchored-storage lemma that

\[
W_{abc}=[U-(1-q)(C+A+B)]_+.
\]

For the reverse cycle \((a,c,b)\), saturation of the first event forces saturation of the second, so a runoff-producing periodic orbit must saturate at either the second or third event. The corresponding two candidate sums give

\[
W_{acb}=\max\{0,\;U-(1-q)(C+A+D),\;U-(1-q)(C+E+F)\}.
\]

Now \(D\ge B\), because \(c\ge b\). We also prove the **two-step inequality**

\[
E+F\ge A+B.
\]

If \(E=C\), then \(F=A\), whereas \(B\le C\), so this inequality reduces to \(C\ge B\). If \(E<C\), then neither \(f_a\) nor \(f_b\) clips in any of the four evaluations \(A,E,B,F\). Direct expansion yields

\[
(E+F)-(A+B)=q(b-a)\ge0.
\]

Both candidate storage sums for the reverse cycle are consequently no smaller than the sum for the increasing cycle; hence \(W_{abc}\ge W_{acb}\).

For strictness, \(D>B\) holds exactly when \(c>b\) and \(B<C\). For \(q>0\), the two-step inequality is strict exactly when \(a<b\) and \(B<C\): in the case \(E=C\), its difference is \(C-B\); in the other case the difference is \(q(b-a)\). Thus strict runoff ordering holds exactly when \(a<b<c\), \(B<C\), and \(W_{abc}>0\). Under \(B<C\), one also has \(A<C\) (otherwise \(a\ge(1-q)C\), forcing \(B=C\)); therefore

\[
A=qC+a,\qquad B=q^2C+qa+b,
\]

and the sole potentially overflowing event is the one with depth \(c\). Hence

\[
W_{abc}>0\ \Longleftrightarrow\ qB+c>C.
\]

The pair of inequalities \(B<C<qB+c\) is exactly the claimed open capacity interval. Its width is

\[
\frac{(1+q)c-b-qa}{(1-q^2)(1+q+q^2)}>0
\]

whenever \(a<b<c\). All equality cases, including the two endpoints, follow because the argument uses strict inequalities throughout.

## Verification
As an exact example, use \(q=1/2\), \(C=2\), and \((a,b,c)=(1/4,1,3/2)\). The sharp capacity interval is \((3/2,33/14)\), which contains \(2\). Substituting into the periodic recurrence gives

\[
W_{abc}=5/16,\qquad W_{acb}=1/8,\qquad W_{abc}-W_{acb}=3/16.
\]

The standalone `verify.py` computes exact fixed points of the capped affine three-step composition independently of the preceding anchored formulas. It compares both expressions and both sides of the strictness criterion on 16,500 rational parameter combinations, including 1,632 cases of strict inequality. The script uses only Python's standard library and is invoked with `python verify.py`. These finite checks support the symbolic argument but are not a substitute for its universal proof.

## Relationship to prior work
Bartlett et al. (2015, Sections 2–3 and Appendix A) model storage threshold runoff under instantaneous rainfall additions and continuous losses, and derive distributional properties for stochastic rainfall. This supplies a physical setting, not the present deterministic three-event cyclic ordering theorem or its exact capacity interval. Gani and Pyke (1962) study first-emptiness probabilities for dams with ordered stochastic inputs and a steady-release rule; their abstract addresses a different stochastic event and release mechanism. The two-step anchored comparison and complete increasing-versus-reverse cyclic ordering theorem here are not asserted by either inspected source.

Classical cap-and-release storage dynamics and mass balance are acknowledged; the claimed distinction is the **universal three-position permutation comparison plus the necessary-and-sufficient strict capacity interval**, not the recurrence itself. A more abstract rearrangement or finite-buffer theorem might subsume this particular statement; historical coverage outside the inspected sources is not excluded.

## Limitations
The result is a theorem for a scalar store with homogeneous exponential retention, equally spaced impulses, no inflow during dry intervals, instantaneous full excess spill, and a periodically settled state. It need not remain true under rainfall-dependent losses, time-varying inter-event intervals, multiple spatial reservoirs, hysteretic runoff, or stochastic fluctuations. It makes no claim of empirical optimal storm forecasting and no claim that the increasing ordering maximizes runoff for cycles of four or more distinct depths. Independent historical-priority assessment has not been performed.

## References
1. Bartlett, M. S., Daly, E., McDonnell, J. J., Parolari, A. J., and Porporato, A. (2015). *Stochastic rainfall-runoff model with explicit soil moisture dynamics*. Proceedings of the Royal Society A 471, 20150389. DOI: 10.1098/rspa.2015.0389. Early online October 28, 2015. Public full text: https://water.usask.ca/hillslope/documents/pdfs/2015/Bartlett_Stochastic_20150389.full.pdf.
2. Gani, J., and Pyke, R. (1962). *Inequalities for First Emptiness Probabilities of a Dam with Ordered Inputs*. Journal of the Royal Statistical Society, Series B 24, 102–106. DOI: 10.1111/j.2517-6161.1962.tb00440.x. https://academic.oup.com/jrsssb/article/24/1/102/7035155.
