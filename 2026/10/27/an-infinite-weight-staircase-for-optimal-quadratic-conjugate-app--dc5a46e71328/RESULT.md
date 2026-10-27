# An infinite weight staircase for optimal quadratic-conjugate approximation in Bergman spaces

## Finding
Let \(\alpha>-1\), let \(d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dx\,dy/\pi\) on the unit disk, and let \(A^2_\alpha\) denote its holomorphic \(L^2\) subspace. Consider the sharp best-holomorphic-approximation inequality
\[
\inf_{h\in A^2_\alpha}\|\overline z^{\,2}f-h\|_{L^2(\mu_\alpha)}^2
\le C_\alpha^2\|f\|_{A^2_\alpha}^2,
\qquad f\in A^2_\alpha.
\]
The exact sharp constant and **all** equality functions have an infinite staircase as the weight varies. Define
\[
\tau_j=\frac{j-1+\sqrt{9j^2+18j+1}}2\quad(j\ge1),\qquad\tau_0=-1,
\]
and, for integer \(n\ge1\),
\[
V_n(\alpha)=
\frac{2(\alpha+1)(2\alpha n+\alpha+2n^2+4n)}
{(\alpha+n)(\alpha+n+1)(\alpha+n+2)(\alpha+n+3)}.
\]
The \(\tau_j\) are strictly increasing to infinity, and \(2j<\tau_j<2j+1\). For each \(n\ge1\), if \(\tau_{n-1}<\alpha<\tau_n\), then
\[
C_\alpha^2=V_n(\alpha),
\]
and all nonzero equality functions are scalar multiples of \(z^n\). At \(\alpha=\tau_n\), both \(V_n\) and \(V_{n+1}\) give the sharp constant, and all nonzero equality functions are exactly the nonzero linear combinations of \(z^n\) and \(z^{n+1}\). There are no other equality functions.

The first transition is exactly \(\tau_1=\sqrt7\), and the large-weight law is
\[
\lim_{\alpha\to\infty}\alpha C_\alpha^2=\frac{16}{27},
\qquad \frac{n_\alpha}{\alpha}\longrightarrow\frac12
\]
for every selected maximizing monomial degree \(n_\alpha\), including the two possible degrees at a transition. Thus no fixed finite set of polynomial degrees contains an extremizer for all weights.

## Assumptions and scope
The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). The measure above has total mass one. Norms are defined using \(d\mu_\alpha\). The infimum is over the **entire** closed holomorphic Bergman subspace, not only over polynomials. All scalars and all holomorphic functions in \(A^2_\alpha\) are permitted. At a transition, the phrase "nonzero linear combination" permits either coefficient to vanish. Parameters are real with \(\alpha>-1\), and indexes \(j,n\) are positive integers unless otherwise stated.

The mathematical object is the optimal discrepancy after approximating the nonholomorphic product \(\overline z^{\,2}f\) by an arbitrary holomorphic function. It is equivalently the norm of the associated *big* Hankel map with the anti-analytic symbol \(\overline z^{\,2}\), but the theorem's sharp constant and extremizers are stated as a Bergman-space best-approximation problem.

## Proof
**Orthogonal projection and exact diagonalization.** Write
\[
m_n=\int_{\mathbb D}|z|^{2n}\,d\mu_\alpha(z)
=\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)}.
\]
Then \(e_n=z^n/\sqrt{m_n}\) is an orthonormal basis of \(A^2_\alpha\). Denote the orthogonal Bergman projection by \(P_\alpha\), and set \(T_\alpha f=(I-P_\alpha)(\overline z^{\,2}f)\). The nearest holomorphic approximant is \(P_\alpha(\overline z^{\,2}f)\). Angular Fourier orthogonality gives
\[
P_\alpha(\overline z^{\,2}e_n)=
\begin{cases}0,&n=0,1,\\
\sqrt{m_n/m_{n-2}}\,e_{n-2},&n\ge2.
\end{cases}
\]
The vectors \(T_\alpha e_n\) have distinct angular frequencies \(n-2\), and are therefore mutually orthogonal in the ambient \(L^2\) space. Pythagoras yields their squared norms
\[
v_0(\alpha)=\frac{2}{(\alpha+2)(\alpha+3)},\qquad
v_n(\alpha)=\frac{m_{n+2}}{m_n}-\mathbf1_{n\ge2}\frac{m_n}{m_{n-2}}\quad(n\ge1).
\]
Using the gamma recurrence, the formula for \(v_n\) agrees exactly with \(V_n\) in the Finding for every \(n\ge1\). Consequently, for any \(f=\sum_{n\ge0}c_ne_n\),
\[
\|T_\alpha f\|^2=\sum_{n\ge0}v_n(\alpha)|c_n|^2,
\qquad\|f\|^2=\sum_{n\ge0}|c_n|^2.
\]
The identity first holds for polynomials and extends by boundedness of multiplication by \(\overline z^{\,2}\) and projection. Since \(v_n\to0\), the sharp squared constant is the largest diagonal value, and the equality space is the span of the maximizing basis vectors.

**Sharp mode transitions.** Direct calculation gives
\[
v_1-v_0=\frac{4(\alpha+1)}{(\alpha+2)(\alpha+3)(\alpha+4)}>0,
\]
and, for every integer \(n\ge1\),
\[
v_{n+1}-v_n=
\frac{4(\alpha+1)[\alpha^2+(1-n)\alpha-2n^2-5n]}
{\prod_{r=0}^{4}(\alpha+n+r)}.
\]
All denominator factors are positive in the stated domain. The bracket is a quadratic in \(\alpha\), negative at \(\alpha=-1\), with exactly one root in \((-1,\infty)\); that positive root is precisely \(\tau_n\). Moreover, for fixed \(\alpha>-1\), consecutive bracket values decrease by \(\alpha+4n+7>0\) as \(n\) increases. Hence the sequence \(v_n\) rises strictly from \(n=0\) to a unique maximizing degree and then falls, except when one bracket vanishes and two adjacent degrees tie. The \(\tau_n\) increase strictly because the positive root of each successive bracket moves right; alternatively this follows immediately from their radical formula. The radical inequality \(2n<\tau_n<2n+1\) follows by squaring positive quantities. This proves the sharp constant, every transition, and every equality case.

**Large-weight scale.** The transition formula implies \(\tau_n=2n+1+O(n^{-1})\). Thus any maximizing degree satisfies \(n_\alpha/\alpha\to1/2\). Substituting \(n/\alpha\to t>0\) into the exact expression gives
\[
\alpha V_n(\alpha)\longrightarrow\frac{4t}{(1+t)^3},
\]
whose unique maximum for \(t>0\) occurs at \(t=1/2\), with value \(16/27\). This proves both asymptotic assertions.

## Verification
The self-contained script `verify.py` checks the gamma-recurrence rational identity, the one-step difference identity, first-mode dominance, the algebraic threshold roots, and direct orthogonal-projection calculations for complex polynomial coefficients with four integral weights. It also tests parameter regimes against sufficiently long exact mode prefixes and checks the large-weight coefficient. Running `python verify.py` with SymPy produced `PASS` and 1650 counted assertion groups; the exact terminal output is in `verify_output.txt`. The unbounded integer-mode and real-parameter conclusions are proved above, **not inferred from finite experiments**.

## Relationship to prior work
Bourass, El-Fallah, Marrhich and Naqos (first public arXiv version February 2, 2021) analyze singular-value rearrangements and their asymptotics for anti-analytic Hankel operators on Bergman spaces. Their Section 8 treats asymptotics for the linear conjugate symbol. The present finding instead determines the exact finite-index maximizing mode and all weight-driven transitions for the quadratic conjugate product. General asymptotic singular-value statements do not imply the discrete sharp constants or equality spaces.

Peláez, Perälä and Rättyä (first public version November 7, 2019) establish boundedness criteria for large classes of radial weighted Bergman Hankel operators. Pau's 2015 preprint characterizes Schatten ideal membership. Neither inspected theorem determines the parameter-specific exact norming polynomial degrees in this quadratic best-approximation question. These works motivate the family but are not represented as proving the present exact staircase. The classical 1988 paper of Arazy, Fisher and Peetre is a material bibliographic risk: its full text was not available for definitive comparison in this review. A hidden equivalent formulation in classical weighted-shift or Bergman literature remains possible.

## Limitations
This is an exact best-approximation statement for \(\overline z^{\,2}f\) and the standard power-weight family \(\alpha>-1\). No assertion is made for a general conjugate symbol, nonradial weights, or higher powers. The proof establishes no originality relative to inaccessible literature, and priority is not independently established. The weight parameter labels a function-space family; the result is not an assertion about the first date of publication of the basic projection formulas.

## References
1. M. Bourass, O. El-Fallah, I. Marrhich, H. Naqos, *On singular values of Hankel operators on Bergman spaces*, arXiv:2102.01743v1 (February 2, 2021), https://arxiv.org/abs/2102.01743 .
2. J. Á. Peláez, A. Perälä, J. Rättyä, *Hankel operators induced by radial Bekollé–Bonami weights on Bergman spaces*, Mathematische Zeitschrift 296 (2020), 211–238; available online November 7, 2019, https://doi.org/10.1007/s00209-019-02412-8 .
3. J. Pau, *Characterization of Schatten class Hankel operators on weighted Bergman spaces*, arXiv:1502.04721v1 (February 16, 2015), https://arxiv.org/abs/1502.04721 .
4. J. Arazy, S. D. Fisher, J. Peetre, *Hankel operators on weighted Bergman spaces*, American Journal of Mathematics 110 (1988), 989–1053, https://doi.org/10.2307/2374685 (full-text comparison unavailable).
