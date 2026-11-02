# A sharp scalar-positivity transition and three-state Markov obstruction for an L-stable fourth-order integrator

## Finding

Consider the L-stable branch of the sequential implicit two-stage, fourth-order, two-derivative integrator of Huo (2025) and Huo–Su (2026). For its parameter \(C\) and scalar stability function
\[
R_C(z)=-\frac{(183C-5)z^3+(972C-42)z^2+(1872C-168)z-288}{(z^2-12z+48)[9Cz^2-(39C+1)z+6]},
\]
write
\[
C_- = \frac{25-\sqrt{105}}{780},\qquad C_+ = \frac{25+\sqrt{105}}{780},\qquad C_q=\frac5{183}.
\]
For every \(C\in[C_-,C_+]\), every real \(x\ge0\), and every finite continuous-time Markov-chain (CTMC) row generator \(Q\) (off-diagonal entries nonnegative and \(Q\mathbf1=0\)), let \(R_C(hQ)\) denote the exact rational matrix functional calculus at step \(h\ge0\). The following sharp classification holds.

**(i) Scalar positivity.** \(R_C(-x)\ge0\) for every \(x\ge0\) **if and only if** \(C\ge C_q\). Within this parameter range, \(0\le R_C(-x)\le1\) for all \(x\ge0\).

**(ii) Minimal conservative-state dimension for loss of endpoint positivity.** If \(C<C_q\), there is a two-state CTMC generator and a step size with a negative entry in \(R_C(hQ)\), whereas every one-state CTMC is safe. If \(C\ge C_q\), **every** two-state CTMC generator is safe at **every** step size, but the **same three-state generator**
\[
Q_3=\begin{pmatrix}-1&1&0\\0&-1&1\\0&0&0\end{pmatrix}
\]
is unsafe at the fixed step \(h=12\) for **every** \(C\in[C_q,C_+]\). Precisely,
\[
[R_C(12Q_3)]_{12}=12R_C'(-12)
=-\frac{60(1204C^2+4C-1)}{49(98C+1)^2}<0.
\]
At the paper's quadratic-stiff-decay parameter \(C=C_q\), the negative transition entry is exactly
\[
[R_{C_q}(12Q_3)]_{12}=-\frac{16260}{22193521}.
\]
Thus the minimal number of **conservative Markov states** permitting a negative one-step transition entry is **two** below \(C_q\), and **three** at or above \(C_q\), throughout the full published A/L-stable interval. The exact CTMC semigroup \(e^{hQ}\) is nonnegative and row-stochastic at all nonnegative times, so these are discretization-induced sign violations.

## Assumptions and scope

The method is applied to an autonomous linear system \(u'=Qu\) in exact arithmetic, with the exact trajectory derivative \(u''=Q^2u\). The matrix functional calculus is the completed one-step map of the cited sequential integrator; it is not a claim about stages, nonlinear solves, finite precision, or its separate approximate ADER spatial-derivative closure. A CTMC row generator is any real square matrix whose off-diagonal entries are nonnegative and whose row sums are zero. The zero generator in dimension one has one-step map \([1]\). No symmetry, reversibility, diagonalizability, or irreducibility is assumed.

The interval \([C_-,C_+]\) is exactly the published scalar A/L-stable parameter interval. In particular, its parameters are strictly positive, and the denominator of \(R_C(z)\) has no root in the closed left half-plane. Since CTMC generators have spectrum there, \(R_C(hQ)\) is defined for all \(h\ge0\). All classification quantifiers above range over the entire interval, all step sizes, and all CTMC generators of the stated sizes.

## Proof

**1. Scalar factorization.** Inserting \(z=-x\) into the published function gives
\[
R_C(-x)=\frac{N_C(x)}{D_C(x)},\quad
\begin{aligned}
N_C(x)&=(183C-5)x^3+(42-972C)x^2+(1872C-168)x+288,\\
D_C(x)&=(x^2+12x+48)[9Cx^2+(39C+1)x+6].
\end{aligned}
\]
As \(C>0\), \(D_C(x)>0\) for every \(x\ge0\). If \(C<C_q\), then \(183C-5<0\). The cubic numerator tends to negative infinity and therefore \(R_C(-x)<0\) for every sufficiently large \(x\).

At \(C=C_q\), exact cancellation gives
\[
R_{C_q}(-x)=\frac{2(157x^2-1188x+2928)}{(x^2+12x+48)(5x^2+42x+122)}.
\]
The numerator quadratic has positive leading coefficient and discriminant \(-427440<0\), so it is strictly positive at every real \(x\). Moreover,
\[
N_C(x)-N_{C_q}(x)=(C-C_q)\,3x(61x^2-324x+624).
\]
The quadratic inside the parenthesis has discriminant \(-47280<0\) and positive leading coefficient. Hence \(N_C(x)\ge N_{C_q}(x)>0\) for all \(x\ge0\) whenever \(C\ge C_q\). The cited A-stability theorem gives \(|R_C(-x)|\le1\) for every \(C\in[C_-,C_+]\), establishing \(0<R_C(-x)\le1\) for all finite \(x\ge0\) on that subinterval. Conversely, \(C<C_q\) gives negative scalar response somewhere. This proves (i).

**2. All two-state generators.** Every two-state CTMC row generator is
\[
Q_2=\begin{pmatrix}-a&a\\b&-b\end{pmatrix},\qquad a,b\ge0.
\]
If \(s=a+b=0\), its step is the identity. Otherwise \(Q_2^2=-sQ_2\), and with \(x=hs\) the rational functional calculus yields
\[
R_C(hQ_2)=I+\frac{1-R_C(-x)}s Q_2.
\]
The two off-diagonal entries are nonnegative when \(R_C(-x)\le1\); each diagonal entry is a convex combination of \(1\) and \(R_C(-x)\). Hence \(0\le R_C(-x)\le1\) implies \(R_C(hQ_2)\) is entrywise nonnegative for **all** such \(Q_2\) and \(h\). If \(C<C_q\), choose \(Q_2=\left(\begin{smallmatrix}-1&1\\0&0\end{smallmatrix}\right)\) and \(h\) with \(R_C(-h)<0\), which exists by part 1; its \((1,1)\) step entry is negative. Dimension one is always safe because its only CTMC generator is zero.

**3. Universal three-state witness.** The leading \(2\times2\) block of \(12Q_3\) is the Jordan block \(\left(\begin{smallmatrix}-12&12\\0&-12\end{smallmatrix}\right)\). Evaluating a rational analytic function on this block gives its off-diagonal entry as \(12R_C'(-12)\); the third state does not change the leading block. Differentiating the factored rational stability function gives the exact identity
\[
R_C'(-12)=-\frac{5(1204C^2+4C-1)}{49(98C+1)^2}.
\]
The polynomial \(1204C^2+4C-1\) is strictly increasing for \(C>0\), and at \(C_q=5/183\) it equals \(271/33489>0\). Hence \(R_C'(-12)<0\) for all \(C\in[C_q,C_+]\). Substitution of \(C_q\) gives \(12R_{C_q}'(-12)=-16260/22193521\). Thus the three-state step has a strictly negative entry at \(h=12\) for every parameter at or above \(C_q\). Combining this with Step 2 proves the minimal-dimension classification.

**4. Conservation and exact-flow comparison.** The method has \(R_C(0)=1\). For every row generator \(Q\), the rational functional calculus therefore gives \(R_C(hQ)\mathbf1=\mathbf1\) wherever defined: total probability is conserved, despite the sign failure. Because each \(Q\) is Metzler, \(e^{hQ}\) is entrywise nonnegative and row-stochastic for \(h\ge0\). This completes the proof.

## Verification

The supplied standard-library Python file `verify.py` reconstructs the stability rational function directly from the two sequential stage factors, checks the resulting bivariate polynomial identity exactly, verifies the scalar numerator and denominator, checks both discriminants, proves the derivative identity by exact polynomial coefficient comparison, and evaluates the three-state step as an exact rational \(3\times3\) matrix with an explicitly inverted denominator. The code has no stochastic tests and requires no third-party dependencies. Run `python3 verify.py` in the folder containing the file; a successful run prints `VERIFY_OK` and an exact-check count.

In particular, the independent matrix evaluation gives \([R_{C_q}(12Q_3)]_{12}=-16260/22193521\) without evaluating a numerical derivative. Exact arithmetic checks support, but do not replace, the sign and quantifier arguments in the proof.

## Relationship to prior work

Huo's original implicit TSFO paper (first public version December 1, 2025; latest accessible version June 22, 2026) constructs the method and derives the A/L-stable interval; Huo and Su (August 4, 2026) give its conservative transport–relaxation implementation and the explicit rational stability function, including the special value \(C_q=5/183\) for quadratic stiff decay. Those contributions concern order, stability, damping, and differential-operator closure. In the inspected full texts, neither establishes the scalar nonnegativity threshold nor the minimum conservative Markov-state dimension for an endpoint sign failure.

Absolute monotonicity and positivity of rational integrators form an established framework; notably, the 2013 work of Lóczi and Ketcheson analyzes rational stability functions and finite positivity thresholds. Its general theory explains why A/L-stability need not confer unrestricted positivity, but the explicitly stated parameter transition \(C_q\), exact derivative witness, and dimension-two/dimension-three dichotomy for this particular newly used two-derivative method do not follow from a numerical value tabulated there. Related published results for the [2/2] Padé and SSP-SDIRK2(2) methods have different stability rational functions and different state-dimension thresholds; they supply conceptual precedents, not an implication of the specific classification here.

## Limitations

This result establishes **endpoint** positivity failure for linear CTMC generators, not positivity failure of every initial condition or of every discretized PDE. The chosen three-state chain is reducible; irreducible-chain minimality is not addressed. The scalar criterion is only nonnegativity of the completed scalar stability factor, not positivity of all internal stages or a nonlinear strong-stability-preserving property. The exact coefficient threshold pertains to the cited one-parameter L-stable branch, not every two-derivative integrator. The proof does not quantify error, accuracy, or stability under finite-precision nonlinear stage solves, flux limiters, or the approximate ADER closure. Historical priority cannot be ruled out absolutely; closely related general positivity ideas predate the cited method.

## References

1. Z. Huo, *An L-Stable Implicit Two-Stage Fourth-Order Time Discretization for Stiff Evolution Problems*, arXiv:2512.01628v4. First publicly submitted December 1, 2025; version dated June 22, 2026. https://arxiv.org/abs/2512.01628
2. Z. Huo and Y. Su, *An L-Stable Sequential Two-Stage Fourth-Order Method with ADER Trajectory Derivatives for Stiff Transport–Relaxation Systems*, arXiv:2608.03256v1. First submitted August 4, 2026. https://arxiv.org/abs/2608.03256
3. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651 (2013). https://arxiv.org/abs/1303.6651
4. M. N. Spijker, *Stepsize Conditions for General Monotonicity in Numerical Initial Value Problems*, SIAM Journal on Numerical Analysis 45 (2007), DOI:10.1137/060661739.
