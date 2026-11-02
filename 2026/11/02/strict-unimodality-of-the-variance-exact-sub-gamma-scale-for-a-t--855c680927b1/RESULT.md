# Strict unimodality of the variance-exact sub-gamma scale for a two-jump Poisson law

## Finding

Let \(N_\lambda\sim\operatorname{Poisson}(\lambda)\), where \(\lambda>0\), and let the independent positive jump sizes \(J_1,J_2,\ldots\) have
\[
\Pr(J_i=1)=\frac{39}{40},\qquad \Pr(J_i=5)=\frac1{40}.
\]
Center the compound Poisson variable:
\[
X=\sum_{i=1}^{N_\lambda}J_i-\lambda\mathbb EJ_1,\qquad
V=\operatorname{Var}(X)=\frac{8\lambda}{5}.
\]
For a right-sided sub-gamma inequality with the **true variance** fixed as quadratic proxy, call \(c>0\) feasible when
\[
\log\mathbb E e^{tX}\le\frac{Vt^2}{2(1-ct)}
\qquad\text{for every }0\le t<1/c.
\]
Let \(c_*\) be the infimum over feasible \(c\). Write
\[
F(t)=39(e^t-1-t)+(e^{5t}-1-5t),\quad
\Psi(t)=\frac1t-\frac{32t}{F(t)}\quad(t>0),
\]
and
\[
N(t)=32t^3F'(t)-32t^2F(t)-F(t)^2.
\]
**Theorem.** The function \(\Psi\) is strictly increasing up to a single point \(t_*\in(0,\infty)\) and strictly decreasing afterward. Equivalently, \(N\) has exactly one positive zero, and this zero is simple. Consequently the variational optimum of the variance-exact sub-gamma scale is achieved at one and only one positive argument:
\[
\boxed{c_*=\Psi(t_*)=\max_{t>0}\Psi(t),\qquad N(t_*)=0.}
\]
The maximizer has the **rigorously certified rational enclosure**
\[
\boxed{\frac{473723111}{10^9}<t_*<\frac{473723113}{10^9}.}
\]
Numerically, \(t_*\approx0.473723111601\) and \(c_*\approx0.895416095555\). The optimum is strictly larger than the third-cumulant lower bound \(41/48\) and is independent of the Poisson intensity \(\lambda>0\).

## Assumptions and scope

The jumps have exactly the two displayed values with the displayed probabilities, and the Poisson intensity is any strictly positive real number. There is no Gaussian component or additional jump component. The scale \(c_*\) is optimized with the true variance fixed, not with a freely varying variance proxy. The theorem covers the complete range \(t>0\) and establishes global shape and uniqueness, rather than only local maximality or existence. No statement is made for other two-point jump mixtures or all infinitely divisible distributions.

## Proof

**1. Reduce the problem to a scalar objective.** The centered compound Poisson cumulant generator is
\[
K_X(t)=\lambda\bigl(\mathbb E e^{tJ}-1-t\mathbb EJ\bigr)
=\frac{\lambda}{40}F(t).
\]
Since \(\mathbb EJ^2=8/5\), the normalized remainder moment-generating function in the variance-exact sub-gamma variational representation is
\[
M(t)=\frac{2K_X(t)}{Vt^2}=\frac{F(t)}{32t^2},\quad t>0.
\]
Here \(F(t)>32t^2>0\) for \(t>0\), because every exponential remainder contains strictly positive terms beyond second order. The established optimal-scale variational identity is
\[
c_*=\sup_{t>0}\frac{1-M(t)^{-1}}t
=\sup_{t>0}\Psi(t).
\]
Differentiation yields
\[
\Psi'(t)=\frac{N(t)}{t^2F(t)^2};
\]
thus it remains to prove that \(N\) changes sign exactly once on the positive half-line.

**2. Exact coefficient signs through degree eleven.** The entire function \(F\) has the series
\[
F(t)=\sum_{k=2}^{\infty}f_kt^k,\qquad
f_k=\frac{39+5^k}{k!}.
\]
Let \(T_n=n![t^n]N(t)\). Then, for every integer \(n\ge4\),
\[
T_n=32n(n-1)(n-3)(39+5^{n-2})
-\sum_{j=2}^{n-2}\binom nj(39+5^j)(39+5^{n-j}).
\]
Exact integer arithmetic gives
\[
\begin{array}{c|rrrrrrrr}
n&4&5&6&7&8&9&10&11\\\hline
T_n&0&0&99520&882112&-4769408&-240640896&-4342095552&-59940771264.
\end{array}
\]
In particular, the first nonzero coefficients have the sign pattern positive, positive, then negative.

**3. All remaining coefficients are strictly negative.** For \(n\ge12\), retain just the strictly positive terms \(5^j5^{n-j}\) in the convolution sum, and note \(39\le5^{n-2}\). Then
\[
T_n\le 5^n\left[\frac{64}{25}n(n-1)(n-3)
-(2^n-2n-2)\right].
\]
Set
\[
Q_n=(2^n-2n-2)-\frac{64}{25}n(n-1)(n-3).
\]
Now \(Q_{12}=25718/25>0\), while direct algebra gives
\[
Q_{n+1}-2Q_n
=2n+\frac{64}{25}n(n^2-7n+8)>0\qquad(n\ge12).
\]
Induction proves \(Q_n>0\) for every \(n\ge12\), hence \(T_n<0\) in that entire range. Together with the preceding eight exact coefficients,
\[
N(t)=\frac{99520}{6!}t^6+\frac{882112}{7!}t^7
-\sum_{n=8}^{\infty}\frac{|T_n|}{n!}t^n.
\]
All series converge absolutely at every real \(t\).

**4. Strict unimodality and optimality.** Dividing by \(t^7\) on \(t>0\) yields
\[
\frac{N(t)}{t^7}=\frac{99520}{6!t}+\frac{882112}{7!}
-\sum_{n=8}^{\infty}\frac{|T_n|}{n!}t^{n-7}.
\]
This expression is continuous and strictly decreasing on \((0,\infty)\); the first term strictly decreases and every summand in the negative series is nonincreasing. Its limit is \(+\infty\) as \(t\downarrow0\) and \(-\infty\) as \(t\to\infty\), already because the first negative term is linear. Consequently it crosses zero once, from positive to negative. At that crossing its derivative is strictly negative, so the zero of \(N\) is simple. Since \(t^2F(t)^2>0\), the same sign change governs \(\Psi'\). Strict unimodality and global optimality follow. Moreover \(\lim_{t\downarrow0}\Psi(t)=\mathbb ER=41/48\), so its positive initial derivative proves \(c_*>41/48\). The ratio \(2K_X/(Vt^2)\), and hence the optimizer, does not depend on \(\lambda\).

**5. Rational isolation.** For every rational \(z\ge0\) and integer \(m>z-2\), let
\[
S_m(z)=\sum_{j=0}^m\frac{z^j}{j!}.
\]
The elementary geometric tail estimate gives
\[
S_m(z)<e^z<S_m(z)+
\frac{z^{m+1}}{(m+1)!\bigl(1-z/(m+2)\bigr)}
\quad(z>0).
\]
Substituting these two rational bounds, with \(m=80\), separately for \(e^t\) and \(e^{5t}\), yields exact rational lower and upper enclosures for \(N(t)\). At \(t=473723111/10^9\), the lower enclosure is positive; at \(t=473723113/10^9\), the upper enclosure is negative. Hence the unique zero lies strictly between the stated rational endpoints. The accompanying standalone verifier performs these calculations entirely with rational arithmetic.

## Verification

The file `verify.py` (Python standard library only) recomputes the Taylor coefficient formula with integer binomial coefficients, checks the finite sign exceptions, confirms the polynomial-exponential tail induction identity over diagnostic integer cases, and carries out both rational endpoint sign enclosures with 80-term exponential estimates. It also independently evaluates the optimal scale through two algebraically equivalent formulas and locates the unique root by numerical bisection. In the recorded run, **465 assertions passed**. The program's finite checks do not replace the all-index coefficient argument or the global monotonicity proof in the preceding section. The rational endpoint enclosures, unlike the printed decimal approximation, are mathematically rigorous certificates under exact arithmetic.

## Relationship to prior work

Chen (2026, arXiv:2610.00032v1), Theorem 3.1, establishes the exact variational formula for the optimal variance-exact right sub-gamma scale for spectrally positive infinitely divisible laws. Section 7.2 chooses **exactly the same two-point jump distribution** and establishes that at least one interior maximizer exists, with approximate location and scale. Its discussion after equation (59) explicitly does **not** establish uniqueness. The variational formula, transformation, original choice of probabilities, and existence/numerical estimates belong to that prior work. The additional result proved here is strict global unimodality, thereby closing this sharply specified uniqueness gap, together with a proof by an all-degree coefficient sign pattern and rational root enclosure.

The classical power-series and single-sign-change principles used in the proof are standard; they are not claimed as new general results. Targeted comparisons with accessible mathematical research records did not identify a prior theorem resolving the stated uniqueness gap for this distribution. A possible unlocated general unimodality theorem for exponential moment-generating-function ratios remains a qualification to historical priority.

## Limitations

The result concerns the displayed two-point jump mixture, without claiming uniqueness for other mixtures. It does not improve the universal characterization of sub-gamma admissibility, the underlying cumulant bound, or the concentration inequality beyond certifying the optimizer in this worked example. Although the root interval is exact, the displayed decimal value of \(c_*\) is a numerical approximation, not a rigorously rounded enclosure. No independent mathematical audit or comprehensive historical-priority certification has been performed.

## References

1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1, first posted 2026-09-02. In particular Theorem 3.1 and Section 7.2, equations (53)–(59). https://arxiv.org/html/2610.00032v1
2. Boucheron, Lugosi and Massart, *Concentration Inequalities: A Nonasymptotic Theory of Independence* (2013), general sub-gamma terminology, cited in Chen (2026).
3. Klar and Müller (2003), the \(\mathcal M\)-class of moment-generating-function inequalities, cited in Chen (2026); its original full text was not independently inspected.
