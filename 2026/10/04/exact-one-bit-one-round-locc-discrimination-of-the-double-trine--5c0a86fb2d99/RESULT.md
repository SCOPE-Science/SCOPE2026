# Exact one-bit one-round LOCC discrimination of the double trine
## Finding
For the equiprobable double-trine ensemble
\[
|s_i\rangle\otimes |s_i\rangle,\qquad i\in\{0,1,2\},
\]
with
\[
|s_0\rangle=|0\rangle,\quad
|s_1\rangle=-\frac12|0\rangle-\frac{\sqrt3}2|1\rangle,\quad
|s_2\rangle=-\frac12|0\rangle+\frac{\sqrt3}2|1\rangle,
\]
consider one-round Alice-to-Bob LOCC in which Alice has two outcomes, sends that one-bit outcome, and Bob then performs an arbitrary qubit POVM. The exact optimal minimum-error success probability is
\[
P_{\mathrm{1bit}}=
\frac{4+\sqrt3+\sqrt{15+6\sqrt3}}{12}
=0.897594048736878\ldots .
\]
An optimal protocol is: Alice measures \(\sigma_x\); after either outcome Bob ignores the least likely posterior trine state and performs the binary Helstrom measurement on the other two.

## Assumptions and scope
The source ensemble is exactly the double trine above, with equal prior \(1/3\). The communication direction is Alice to Bob, there is one measurement round, and Alice's message alphabet has size two. Bob's conditional POVM is unrestricted. Shared randomness is allowed but cannot improve the optimum because the objective is linear in protocol mixtures. No statement is made about two-way LOCC, more than two message symbols, non-adaptive protocols, unambiguous discrimination, or other ensembles.

Write the trine density matrices as
\[
\rho_i=\frac12(I+n_i\cdot\sigma),
\]
where the three unit Bloch vectors lie in the \(xz\)-plane, satisfy \(n_i\cdot n_j=-1/2\) for \(i\ne j\), and sum to zero. For a prior vector \(q=(q_0,q_1,q_2)\), let \(S(q)\) denote the optimal one-copy minimum-error success probability for the trine.

## Proof
For a binary Alice POVM \(\{E,I-E}\}\), the total success probability is the sum of two optimal Bob discrimination values. Each Bob value is a maximum of expressions linear in \(E\), so the total is convex in \(E\). The extreme points of the qubit effect interval \(0\le E\le I\) are orthogonal projections: if an eigenvalue of an effect lies strictly between zero and one, that eigenvalue can be perturbed in both directions. Therefore an optimum may be taken at a projection. The trivial projections \(0\) and \(I\) give only the uniform one-copy trine value \(2/3\), so it remains to consider a rank-one projector
\[
E=\frac12(I+m\cdot\sigma),\qquad |m|=1.
\]
Only the projection of \(m\) onto the trine plane affects the posterior priors. If that planar projection is \(r u\), with \(0\le r\le1\), the two branch values have the form
\[
\frac12\bigl(S(q_0+r d)+S(q_0-r d)\bigr)
\]
for a fixed direction \(d\). Since \(S\) is convex in its prior vector, this expression is even and convex in \(r\), hence nondecreasing for \(r\ge0\). Thus an optimum has \(r=1\): Alice's measurement axis lies in the trine plane.

By outcome exchange and the dihedral symmetry of the trine, write the planar angle as \(0\le\phi\le\pi/6\). The two normalized posterior prior vectors are
\[
q_i^\pm=\frac{1\pm m(\phi)\cdot n_i}{3}.
\]
The Helstrom dual for one-copy trine discrimination has a useful geometric form. Writing a dual operator as \(\Gamma=(R I+g\cdot\sigma)/2\), the constraints \(\Gamma\ge q_i\rho_i\) are exactly
\[
R\ge q_i+|g-q_i n_i|,
\]
so
\[
S(q)=\min_g\max_i\bigl(q_i+|g-q_i n_i|\bigr).
\]
This is the additively weighted smallest-enclosing-circle problem for the three points \(q_i n_i\).

If two constraints with weights \(a,b\) are active, their value is
\[
H(a,b)=\frac12\left(a+b+\sqrt{a^2+ab+b^2}\right),
\]
which is exactly the Helstrom success for those two weighted trine states. More explicitly, if \(d=\sqrt{a^2+ab+b^2}\), the tangent two-disc dual covers a third trine weight \(c\) exactly when
\[
c\le c_*(a,b):=\frac{ab(a+b+d)}{a^2+b^2+(a+b)d}.
\]
This follows by writing the dual center on the segment joining \(a n_i\) and \(b n_j\), with radii \(H(a,b)-a\) and \(H(a,b)-b\), and then squaring the remaining dual inequality.

For the plus branch on \(0\le\phi\le\pi/6\), the two larger weights \(a=q_0^+\) and \(b=q_1^+\) obey \(a,b\ge1/3\), whereas \(c=q_2^+\le(2-\sqrt3)/6<1/18\). Since \(d\le a+b\),
\[
c_*(a,b)\ge\frac{ab}{2(a+b)}\ge\frac1{18}>c,
\]
so the pair \((0,1)\) is dual-feasible throughout and therefore exactly optimal for that branch.

For the minus branch the ordering is \(q_2^-\ge q_0^-\ge q_1^-\), with \(q_2^->1/2\). A pair omitting state \(2\) cannot be feasible because its dual value is at most \(q_0^-+q_1^-=1-q_2^-<q_2^-\). A pair \((1,2)\) omitting state \(0\) also cannot be feasible: for \(a=q_1^-\le b=q_2^-\), the formula above gives \(c_*(a,b)<a\), because
\[
a^2+b^2+(a+b)d-b(a+b+d)=a(a-b+d)>0,
\]
while the omitted weight satisfies \(q_0^-\ge a\). Consequently the minus branch is supported either by the pair \((0,2)\), when that pair is feasible, or by all three constraints.

If all three constraints are active and \(e_2=q_0q_1+q_1q_2+q_2q_0\), \(e_3=q_0q_1q_2\), solving the three equalities gives
\[
S(q)=\frac{2e_2e_3}{4e_3-e_2^2}.
\]
When both branches are two-active, the total value reduces to
\[
F_2(\phi)=\frac{4+\sqrt3\cos\phi}{12}+
\frac{\sqrt{5+4\cos(\phi-\pi/6)}+\sqrt{5+4\cos(\phi+\pi/6)}}{8\sqrt3}.
\]
This is nonincreasing on \([0,\pi/6]\). Indeed, for
\[
h(x)=\frac{\sin x}{\sqrt{5+4\cos x}},
\]
one has
\[
h'(x)=\frac{2+5\cos x+2\cos^2x}{(5+4\cos x)^{3/2}}>0
\]
for \(0\le x\le\pi/3\). The derivative of the sum of square roots in \(F_2\) is \(2h(\pi/6-\phi)-2h(\pi/6+\phi)\le0\), and the remaining cosine term also decreases.

In the three-active minus-branch regime, the induced priors satisfy
\[
e_2=\frac14,\qquad e_3=\frac{1+\sin(3\phi)}{108},
\]
so that branch has value
\[
S_-(\phi)=\frac{2(1+\sin(3\phi))}{16\sin(3\phi)-11}.
\]
Its derivative is
\[
S_-'(\phi)=-\frac{162\cos(3\phi)}{(16\sin(3\phi)-11)^2}.
\]
Whenever the three-active expression is feasible its denominator is positive. Put \(\delta=\pi/6-\phi\). The increasing plus-branch contribution has derivative smaller than \(\delta/3\), whereas
\[
|S_-'(\phi)|\ge \frac{162}{25}\sin(3\delta)
\ge \frac{972}{25\pi}\delta>\frac\delta3.
\]
Thus the total value also decreases in this regime. Continuity at the active-set transition proves that the global maximum occurs at \(\phi=0\) (and its symmetry images).

At \(\phi=0\), Alice measures \(\sigma_x\). One branch has posterior priors
\[
\left(\frac13,\frac{2+\sqrt3}6,\frac{2-\sqrt3}6\right),
\]
and the other is its permutation. The least likely state is inactive in Bob's dual. Since distinct trine states have squared overlap \(1/4\), binary Helstrom discrimination gives
\[
P_{\mathrm{1bit}}
=\frac12\left(\frac{4+\sqrt3}6+
\frac{\sqrt{15+6\sqrt3}}6\right)
=\frac{4+\sqrt3+\sqrt{15+6\sqrt3}}{12}.
\]
This proves both the converse and achievability.

## Verification
The standalone script `artifacts/verify.py` uses only the Python standard library. It checks the radical value, reconstructs all two-active and three-active Helstrom-dual candidates, verifies dual feasibility on a dense grid of planar Alice projectors, checks that no grid value exceeds the claimed optimum, and confirms the reported posterior priors at the maximizing \(\sigma_x\) measurement. The finite grid is a corroborating computation only; the universal optimum follows from the analytic convexity, dual reduction, and monotonicity proof above.

## Relationship to prior work
Dutra, Ohst, Nguyen and Gühne introduced a convergent SDP hierarchy for one-round LOCC with a bounded message alphabet. For the double trine, their Table 1 reports, for a two-symbol message, a see-saw lower bound \(0.8976\) and an SDP-hierarchy upper bound \(0.905\); the paper uses the gap to compare two- and three-symbol protocols rather than closing the two-symbol optimum. The formula above closes that numerical interval exactly.

Chitambar and Hsieh previously solved the unrestricted one-way LOCC problem for the double trine. Their optimal Alice measurement has three outcomes and achieves success \(1/2+\sqrt3/4\), so it does not imply the optimum under a one-bit/two-symbol communication cap. Their branch analysis and the later communication-bounded SDP result are consistent with the present value.

Achenbach, Leppäjärvi, Lee and Heinosaari subsequently quoted the same numerical one-bit interval in their multi-copy state-discrimination comparison. No inspected source gives the exact radical above or an analytic optimality proof for the two-symbol message class.

## Limitations
The theorem is specific to the equiprobable double trine, one round, the Alice-to-Bob direction, and a two-symbol message. It does not determine the best protocol with three or four Alice outcomes, the full two-way LOCC optimum, or communication-constrained discrimination for arbitrary ensembles. The originality search cannot exclude an equivalent calculation under terminology not captured by the inspected literature; this remains the principal residual literature risk.

## References
1. A. C. R. Dutra, T.-A. Ohst, H.-C. Nguyen, and O. Gühne, “Structure of quantum measurements implementable with one round of classical communication,” arXiv:2510.09381 (first public 2025-10-10); Rep. Prog. Phys. 89, 037601 (2026), DOI: 10.1088/1361-6633/ae4fef.
2. E. Chitambar and M.-H. Hsieh, “Revisiting the optimal detection of quantum information,” arXiv:1304.1555; Phys. Rev. A 88, 020302(R) (2013), DOI: 10.1103/PhysRevA.88.020302.
3. T. Achenbach, L. Leppäjärvi, H. Lee, and T. Heinosaari, “Nonclassical traits in multi-copy state discrimination,” arXiv:2604.26647 (2026).
