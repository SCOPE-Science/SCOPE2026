# Exact geometric-shift q-Berezin radii and a square-root cutoff boundary law

## Finding
For \(0<q\le1\) and \(0\le\beta<1\), the complete \(q\)-Berezin range of the geometric unilateral shift on Hardy space is **the closed centered disk**
\[
\operatorname{Ber}_q(T_\beta)=\{z\in\mathbb C:|z|\le R(q,\beta)\},\qquad
R(q,\beta)=\frac{q r_*(1-r_*^2)}{1-\beta r_*^2-(1-\beta)h r_*},\quad h=\sqrt{1-q^2},
\]
where \(r_*\in(0,1)\) is the **unique** root of
\[
P_{q,\beta}(r)=1+(\beta-3)r^2+2(1-\beta)h r^3+\beta r^4=0.
\]
All maximizing normalized-kernel pairs have, for arbitrary \(\theta\in\mathbb R\),
\[
w_2=r_*e^{i\theta},\qquad w_1=\frac{r_*-h}{1-hr_*}e^{i\theta}.
\]
For each fixed \(q\in(0,1]\), the near-constant-weight regime has sharp square-root asymptotics
\[
1-r_*\sim\sqrt{\frac{1-h}{2}}\sqrt{1-\beta},\qquad
q-R(q,\beta)\sim q\sqrt{2(1-h)}\sqrt{1-\beta}
\quad(\beta\uparrow1).
\]
At the limiting constant weight \(\beta=1\), the actual range is the **open** disk \(\operatorname{Ber}_q(T_1)=q\mathbb D\), so its boundary-attainment status changes at the endpoint. In the separate fixed-\(\beta\) small-overlap regime,
\[
\lim_{q\downarrow0}\frac{R(q,\beta)}{q}=\frac2{1+\beta}.
\]

## Assumptions and scope
Let \(H^2(\mathbb D)=\{\sum_{n\ge0}a_nz^n:\sum|a_n|^2<\infty\}\), with normalized Szegő kernel \(e_w(z)=\sqrt{1-|w|^2}/(1-\overline w z)\). For \(0<q\le1\) define
\[
\operatorname{Ber}_q(T)=\{\langle Te_{w_1},e_{w_2}\rangle:\ w_1,w_2\in\mathbb D,\;\langle e_{w_1},e_{w_2}\rangle=q\}.
\]
The inner product is linear in its first entry. Set \(T_\beta z^n=\beta^n z^{n+1}\), for each \(n\ge0\), with real \(0\le\beta\le1\). The radius \(R(q,\beta)\) denotes the supremum of absolute values of that range. The theorem includes \(q=1\) and the rank-one shift at \(\beta=0\). The limit \(q\downarrow0\) is a limit of strictly positive overlap parameters, not a definition at zero.

## Proof
**Kernel geometry.** For any admissible kernel pair, 
\[
\langle e_{w_1},e_{w_2}\rangle=\frac{\sqrt{(1-|w_1|^2)(1-|w_2|^2)}}{1-\overline{w_1}w_2}=q>0.
\]
The denominator must be positive real, so \(w_1,w_2\) are collinear with the origin (apart from the trivial case that one parameter vanishes). Fix \(w_2=re^{i\theta}\) with \(0\le r<1\). Solving the squared overlap equation, while preserving the positive sign, gives the only possibilities
\[
w_1=e^{i\theta}\frac{r+h}{1+hr}\quad\text{or}\quad w_1=e^{i\theta}\frac{r-h}{1-hr},\qquad h=\sqrt{1-q^2}.
\]
Both lie in \(\mathbb D\). When \(q=1\), they coincide. This also covers \(r=0\), interpreted with the free orientation of \(w_1\).

**Exact shift transform and winning branch.** Summing the geometric series in the weighted-shift matrix coefficients yields
\[
\langle T_\beta e_{w_1},e_{w_2}\rangle=\frac{q(1-t)w_2}{1-\beta t},\qquad t=\overline{w_1}w_2\in(-1,1).
\]
For fixed \(w_2=re^{i\theta}\) and \(\beta<1\), the real function \((1-t)/(1-\beta t)\) is strictly decreasing in \(t\), since its derivative equals \(-(1-\beta)/(1-\beta t)^2\). Therefore the minus branch \(w_1=e^{i\theta}(r-h)/(1-hr)\) uniquely maximizes the magnitude when \(r>0\) and \(q<1\); at \(q=1\) the branches agree. On this branch \(t=r(r-h)/(1-hr)\), and cancellation reduces the modulus to
\[
F_{q,\beta}(r)=\frac{q r(1-r^2)}{1-\beta r^2-(1-\beta)h r},\qquad 0\le r<1.
\]
Its denominator is positive, since it equals \((1-hr)(1-\beta t)\). Moreover \(F(0)=0\), \(F(r)>0\) for \(r>0\), and \(\lim_{r\uparrow1}F(r)=0\) for \(\beta<1\).

**Unique global maximizer.** Direct differentiation gives
\[
F_{q,\beta}'(r)=\frac{qP_{q,\beta}(r)}{[1-\beta r^2-(1-\beta)hr]^2}.
\]
The derivative of the quartic is
\[
P'(r)=2r\big[(\beta-3)+3h(1-\beta)r+2\beta r^2\big].
\]
The bracket is increasing on \([0,1]\), but at \(r=1\) equals \(-3(1-\beta)(1-h)<0\). Thus \(P\) strictly decreases on \((0,1)\). As \(P(0)=1\) and \(P(1)=-2(1-\beta)(1-h)<0\), it has exactly one root \(r_*\in(0,1)\). It is the global maximizer. The strict branch comparison then identifies all maximizing pairs as claimed.

**Exact range and boundary.** The continuous function \(F\) maps \([0,r_*]\) onto \([0,R(q,\beta)]\). Every positive modulus in this interval occurs from the displayed admissible minus-branch kernel pair; simultaneous rotation by \(e^{i\theta}\) rotates its transform by the same phase. The origin occurs at \(w_2=0\). Thus the entire closed disk, including the boundary circle, is attained. For \(\beta=1\) the operator is the analytic multiplier \(M_z\), and \(\langle M_z e_{w_1},e_{w_2}\rangle=qw_2\). Every \(w_2\in\mathbb D\) admits an overlap-\(q\) companion \(w_1\), hence \(\operatorname{Ber}_q(T_1)=q\mathbb D\), with its boundary omitted.

**Sharp high-weight boundary layer.** Write \(\varepsilon=1-\beta\). The critical-point equation rearranges exactly as
\[
(1-r_*^2)^2=\varepsilon r_*^2(1-2hr_*+r_*^2).
\]
The unique root tends to one as \(\varepsilon\downarrow0\); dividing by \(\varepsilon\) and using \(h<1\) gives \((1-r_*)/\sqrt\varepsilon\to\sqrt{(1-h)/2}\). Writing \(\delta=1-r_*\), the quotient \(R/q\) has the asymptotic form
\[
\frac{R}{q}=\frac{r_*(1-r_*^2)}{(1-r_*^2)+\varepsilon(r_*^2-hr_*)}
=1-\delta-\frac{\varepsilon(1-h)}{2\delta}+O(\varepsilon).
\]
Substituting the critical-point scale proves \((q-R)/\sqrt\varepsilon\to q\sqrt{2(1-h)}\).

**Sharp small-overlap slope.** For \(h\le1\), the denominator of \(F/q\) satisfies
\[
1-\beta r^2-(1-\beta)hr\ge(1-r)(1+\beta r),
\]
whence \(F(r)/q\le r(1+r)/(1+\beta r)\le2/(1+\beta)\). For the reverse limiting inequality take \(r=1-\sqrt q\) and use \(1-h=O(q^2)\). Then \(F(r)/q\to2/(1+\beta)\), proving the asserted limit.

## Verification
The standalone Python file `verify_qberezin_radius.py` uses only Python standard-library modules. It checks direct normalized-kernel overlaps against the prescribed \(q\), compares the direct matrix-transform expression with the quartic-root radius, and samples competing second-kernel radii, together with the two sharp boundary laws. It performs 41,412 numerical/algebraic checks and passed. These finite tests provide reproducibility checks, not a substitute for the preceding proof.

An exact explicit witness distinguishes the sharp answer from the value \(\sqrt3/4\) quoted in an example in the motivating reference: at \(q=\beta=1/2\), choose \(w_2=5/6\) and \(w_1=(5/6-\sqrt3/2)/(1-5\sqrt3/12)\). Their normalized kernel overlap is exactly \(1/2\), and the transform modulus is
\[
\frac{55}{6(47-15\sqrt3)}>\frac{\sqrt3}{4}.
\]
The final strict inequality reduces to \(490^2>3\cdot282^2\). This is a concrete admissible lower witness; the quartic-root theorem independently proves global sharpness.

## Relationship to prior work
Bhattacharya and Patra, *q-Berezin Range of Operators in Hardy Space* (first publicly posted 5 January 2026, arXiv:2601.02334), Theorem 3.18 and Corollary 3.19, establish the circular geometry for real weighted shifts, including the geometric family. Their Remark 3.20 describes conditional critical-point equations but does not determine a globally sharp radius or all maximizing kernel pairs; it states the numerical example addressed above. The present result retains and credits that prior disk-geometry framework, and adds an explicit uniquely specified root, global extremal classification, exact disk closure, and singular boundary laws.

Mahapatra–Halder–Birbonshi–Patra–Paul (arXiv:2608.21723, August 2026), Section 3, studies the \(q\)-Berezin geometry of **Bergman-space** weighted shifts, based on a squared kernel and a different overlap constraint. Its Theorem 3.11 establishes disk geometry for that distinct space, not the present sharp Hardy geometric-shift radius. General \(q\)-numerical ranges and ordinary weighted-shift numerical radii optimize over different vector families and do not directly imply the formula here.

## Limitations
The claimed result concerns the exact geometric positive weight sequence \((\beta^n)_{n\ge0}\), not arbitrary complex weights, other reproducing-kernel Hilbert spaces, or the full unconstrained \(q\)-numerical radius. The square-root asymptotics hold at fixed \(q>0\); no uniform simultaneous \(q\to0\), \(\beta\to1\) statement is asserted. Publication priority over inaccessible or unindexed literature is not independently established. No independent scientific audit has been performed.

## References
1. D. Bhattacharya and A. Patra, *q-Berezin Range of Operators in Hardy Space*, arXiv:2601.02334, initially submitted 5 January 2026; see Theorem 3.18, Corollary 3.19, Remark 3.20. https://arxiv.org/html/2601.02334v2
2. S. Mahapatra, S. Halder, R. Birbonshi, A. Patra, and K. Paul, *q-Berezin sectorial operators with applications to q-Berezin number inequalities and q-Berezin ranges*, arXiv:2608.21723, 22 August 2026; see Section 3 and Theorem 3.11. https://arxiv.org/html/2608.21723v1
