# Two-step positivity and a three-state parity exception for cyclic Crank–Nicolson

## Finding
For an integer \(n\ge2\), let \(P\) be the cyclic permutation matrix \(Pe_j=e_{j-1}\), where indices are modulo \(n\), and put \(Q=P-I\). Thus \(Q\) is the generator of the continuous-time one-way, unit-rate \(n\)-cycle. For every time step \(h>0\), let
\[
 C_h=(I-hQ/2)^{-1}(I+hQ/2)
\]
be the unmodified Crank–Nicolson (implicit midpoint/trapezoidal) one-step matrix. Then, for **every** positive integer \(k\),
\[
 \boxed{C_h^k\ge0\text{ entrywise for every }h>0
 \quad\Longleftrightarrow\quad n=2\ \text{or}\ (n=3\text{ and }k\text{ is even}).}
\]
In particular, on a directed three-state cycle a single large step can send nonnegative data to a vector with a negative component, yet **every pair** of equal Crank–Nicolson steps is positivity preserving for every step size. No fixed positive power has this unconditional property on a directed cycle of length at least four.

There is also a complete sharp **two-step** threshold for every \(n\ge4\). Set \(r=h/(h+2)\in(0,1)\) and
\[
 F_n(r)=1-\sum_{j=2}^{n-1}(j-1)r^j.
\]
The function \(F_n\) has one zero \(\rho_n\) in \((1/2,1)\), and
\[
 \boxed{C_h^2\ge0\quad\Longleftrightarrow\quad
 h\le H_n:=\frac{2\rho_n}{1-\rho_n}.}
\]
The thresholds \(H_n\) strictly decrease with \(n\), and \(H_n\downarrow2\). The smallest nontrivial cutoff is \(H_4\approx3.835975919081\). For a concrete exact witness at \(h=4\),
\[
 C_h\big|_{n=3}=\frac1{19}\operatorname{circ}(-1,12,8),
 \qquad
 C_h^2\big|_{n=3}=\frac1{361}\operatorname{circ}(193,40,128),
\]
where \(\operatorname{circ}\) means that the first row is given by the displayed entries and all subsequent rows are its cyclic shifts. The first matrix is not nonnegative, while its square is strictly positive. At the same time step for \(n=4\),
\[
 C_h^2=\frac1{4225}\operatorname{circ}(1849,-24,1024,1376),
\]
so the two-step positivity recovery fails already in dimension four.

## Assumptions and scope
The cycle has precisely \(n\) distinct states, each with exactly one outgoing transition of rate one. The matrix \(P\) has \(P_{i,i+1}=1\), with indices modulo \(n\). Row vectors of state probabilities evolve by right multiplication; equivalently, nonnegative column data evolve by the displayed matrix or its transpose. Entrywise nonnegativity of the propagator is independent of this orientation choice. Time steps are equal and strictly positive, calculations use exact arithmetic, and \(k\) is fixed when \(h\) varies. The two-state case is the balanced two-state chain, not an arbitrary two-state generator. This result does not assert stage positivity, accuracy beyond the classical second order, or positivity on arbitrary graphs or nonlinear models.

## Proof
Put \(s=h/2\), \(r=s/(1+s)\), and \(S_n(r)=1+r+\cdots+r^{n-1}\). Because \(P^n=I\), direct geometric summation yields the exact backward-Euler resolvent
\[
 R_s=(I-sQ)^{-1}
 =\frac{I+rP+\cdots+r^{n-1}P^{n-1}}{S_n(r)}
 =\sum_{j=0}^{n-1}b_j(r)P^j,
 \quad b_j(r)=\frac{r^j}{S_n(r)}.
\]
The Cayley identity is \(C_h=2R_s-I\). In particular, \(C_h\mathbf1=\mathbf1\); every off-diagonal entry of \(C_h\) is positive, and its diagonal equals \(2/S_n(r)-1\). For \(n=2\), this diagonal is \((1-r)/(1+r)>0\), proving entrywise nonnegativity of every power.

Differentiating the resolvent identity gives
\[
 \frac{dR_s}{ds}=R_s Q R_s=\frac{R_s^2-R_s}{s},
 \qquad C_h^2=I+4s\frac{dR_s}{ds}.
\]
Since \(s\,dr/ds=r(1-r)\), the coefficient of \(P^j\) in \(C_h^2\), for \(1\le j<n\), is exactly
\[
 d_j(r)=\frac{4r^j(1-r)}{S_n(r)^2}
 \left(jS_n(r)-rS_n'(r)\right).
\]
Its sign is the sign of \(jS_n-rS_n'\). For \(j\ge1\),
\[
 jS_n-rS_n'=\bigl(S_n-rS_n'\bigr)+(j-1)S_n,
\]
so all off-diagonal coefficients are nonnegative **exactly when** the \(j=1\) coefficient is nonnegative. The latter has the sign of
\[
 S_n-rS_n'=1-\sum_{j=2}^{n-1}(j-1)r^j=F_n(r).
\]
Every diagonal of \(C_h^2\) is strictly positive, because it is a sum of squares of the diagonal of \(C_h\) and products of its strictly positive off-diagonal entries (cyclic circulant transposition gives matching positive off-diagonal factors). Therefore \(C_h^2\ge0\) is equivalent to \(F_n(r)\ge0\).

For \(n=3\), \(F_3(r)=1-r^2>0\) throughout \((0,1)\). Hence \(C_h^2\) is strictly positive for every \(h>0\), and \(C_h^{2m}=(C_h^2)^m\) is strictly positive for every integer \(m\ge1\).

For every \(n\ge4\), \(F_n\) is strictly decreasing on \((0,1)\), and
\[
 F_n(1/2)=\frac{n}{2^{n-1}}>0,
 \qquad F_n(1)=1-\frac{(n-2)(n-1)}2<0.
\]
Thus there is a unique zero \(\rho_n\in(1/2,1)\), establishing the sharp stated threshold. Adding one further negative summand makes \(F_{n+1}(r)<F_n(r)\) on \((0,1)\), hence \(\rho_{n+1}<\rho_n\). The pointwise infinite limit is
\[
 F_\infty(r)=1-\frac{r^2}{(1-r)^2},
\]
whose unique root on \((0,1)\) is \(1/2\). Monotonicity therefore gives \(\rho_n\downarrow1/2\), and consequently \(H_n\downarrow2\).

It remains to establish the claimed **all-power** dichotomy. The resolvent limit is \(R_s\to J_n/n\), where \(J_n\) is the all-ones matrix. Therefore
\[
 C_h\to H:=2J_n/n-I,
 \qquad H^2=I\quad(s\to\infty).
\]
For every odd \(k\) and \(n\ge3\), the diagonal of \(C_h^k\) tends to \(2/n-1<0\), excluding unconditional positivity.

For \(n\ge4\) and every fixed \(m\ge1\), differentiate \(b_1(r)=r/S_n(r)\) at \(r=1\):
\[
 b_1'(1)=\frac{3-n}{2n}.
\]
Using \(r=1-s^{-1}+O(s^{-2})\) and the exact formula for \(d_1\) gives
\[
 (C_h^2)_{0,1}= -\frac{2(n-3)}{ns}+O(s^{-2}).
\]
Since \(C_h^2=I+O(s^{-1})\) entrywise,
\[
 \boxed{(C_h^{2m})_{0,1}
 =-\frac{2m(n-3)}{ns}+O(s^{-2})<0}
\]
for all sufficiently large \(s\). Thus no fixed even power is unconditionally nonnegative if \(n\ge4\). Together with the \(n=2\) and \(n=3\) cases, this completes the all-power classification.

## Verification
The standalone `verify.py` uses only Python's `fractions.Fraction` and direct rational Gaussian elimination. For each \(2\le n\le10\) and eight rational choices of \(r\), it reconstructs \(R_s\) and \(C_h\) independently of the circulant formula; checks exact row sums, the resolvent coefficients, the two-step derivative identity, and equivalence of matrix nonnegativity with \(F_n(r)\ge0\). For \(n=2,\ldots,9\), it computes the first six powers at a large rational step, testing the two parity exceptions and their counterexamples. The exact arithmetic verifier completed successfully with **4,496 assertions**. Finite calculations confirm instances and formulas; they are not used to infer the all-dimensional or all-step statements, which follow from the displayed analytical proof.

## Relationship to prior work
Higueras and Roldán (2023, arXiv:2301.01066) provide sharp **one-step** Crank–Nicolson positivity and maximum-norm contractivity thresholds for symmetric Dirichlet second-difference heat matrices. Their full paper analyzes a different generator and does not determine positivity of two or more steps on a *directed* cycle.

Fallat and Tsatsomeros (2002) establish Cayley transform identities and study positivity classes, including \(M\)-matrices; their Lemma 2.2 contains the basic resolvent algebra. These known identities are used here, but their theorems do not classify powers of the Cayley transform of an oriented cyclic Markov generator.

The published result *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* determines one-step positivity from the backward-Euler diagonal return entries, including a general irreducible-chain obstruction to unconditional **one-step** positivity beyond two states. It neither settles nor precludes unconditional positivity of \(C_h^2\) in three states; indeed the exact \(h=4\) witness has negative one-step diagonal and strictly positive square.

The published result *Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson* proves positivity of composites \(C_s^kR_s^m\) with \(m\ge k\) on the symmetric nearest-neighbor heat lattice. Its built-in backward-Euler smoothing and two-direction graph are different from unfiltered powers \(C_h^k\) on one-way directed cycles; it does not imply the parity classification or the sharp \(H_n\) above.

Classical Runge–Kutta absolute-monotonicity bounds yield sufficient step restrictions for broad problem classes. They cannot supply the special three-state unconditional two-step behavior or the exact cycle-dependent two-step boundary beyond the universal sufficient range.

## Limitations
The result treats only identical rates on a single directed cycle and the unmodified equal-step Crank–Nicolson map in exact arithmetic. Different transition rates, multiple outgoing edges, boundary conditions, unequal steps, and mixed integrators are not classified. A fixed finite step has eventual positivity by standard spectral mixing in this irreducible finite-state setting; the stronger question addressed here concerns *one fixed power uniformly over arbitrarily large time steps*. Bibliographic priority remains uncertain: related positivity results could appear under eventual-nonnegativity, Cayley-power, or nonreversible Markov-transition terminology outside the inspected works. Neither independence nor exhaustive literature coverage is asserted.

## References
1. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank-Nicolson scheme for the heat equation*, first publicly posted 2023-01-03, arXiv:2301.01066, https://arxiv.org/abs/2301.01066.
2. S. M. Fallat and M. J. Tsatsomeros, *On the Cayley transform of positivity classes of matrices*, Electronic Journal of Linear Algebra 9 (2002), 190–196, DOI: 10.13001/1081-3810.1086, https://journals.uwyo.edu/index.php/ela/article/view/173.
3. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
4. *Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac.
5. Z. Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics 28 (1998), 309–326, DOI: 10.1016/S0168-9274(98)00050-6.
