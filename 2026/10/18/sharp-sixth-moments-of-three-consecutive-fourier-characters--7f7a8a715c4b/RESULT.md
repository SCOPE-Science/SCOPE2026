# Sharp sixth moments of three consecutive Fourier characters

## Finding

Let \(G\) be a compact Abelian group with Haar probability measure, and let \(\chi:G\to\mathbb T\) be a continuous character of order \(m\ge3\), allowing \(m=\infty\). For any \(a,b,c\in\mathbb C\), put \(T=a+b\chi+c\chi^2\). Then

\[
\|T\|_6^6\le K_m\bigl(|a|^2+|b|^2+|c|^2\bigr)^3.
\]

The **sharp** sixth-power constants \(K_m\), together with every equality case, are as follows. Define

\[
Q_3(t)=\frac{t^6+30t^4+40t^3+90t^2+60t+22}{(t^2+2)^3},\qquad
Q_4(t)=\frac{t^6+30t^4+120t^2+32}{(t^2+2)^3},
\]
\[
Q_5(t)=\frac{t^6+30t^4+90t^2+12t+20}{(t^2+2)^3},\qquad
Q_6(t)=\frac{t^6+30t^4+90t^2+22}{(t^2+2)^3},
\]
\[
Q_\infty(t)=\frac{t^6+30t^4+90t^2+20}{(t^2+2)^3}.
\]

For \(m=3\), \(K_3=9=Q_3(1)\); for \(m=4\), \(K_4=61/9=Q_4(1)\). For \(m=5\), let \(t_5\) be the unique positive root of \(4t^5+10t^3+5t^2-20t-2=0\), and put \(K_5=Q_5(t_5)\). For \(m=6\), put \(t_6=\sqrt{(\sqrt{101}-5)/4}\) and \(K_6=Q_6(t_6)\). For every finite \(m\ge7\), and for \(m=\infty\), put \(t_\infty=\sqrt{(\sqrt{105}-5)/4}\) and \(K_m=Q_\infty(t_\infty)\). Set \(t_3=t_4=1\). Numerically these constants are approximately \(9\), \(6.777778\), \(5.681107\), \(5.340548\), and \(5.284235\), respectively.

For nonzero \(T\), equality occurs **if and only if**

\[
(a,b,c)=\lambda(1,t_m\zeta,\zeta^2),\qquad \lambda\in\mathbb C\setminus\{0\},
\]

with \(|\zeta|=1\); in the finite cases \(m=3,4,5,6\), one also requires \(\zeta^m=1\). For \(m\ge7\) and \(m=\infty\), every unit-modulus \(\zeta\) is permitted. Equivalently, the sharp \(L^2\)-to-\(L^6\) norm of this three-character synthesis space is \(K_m^{1/6}\).

## Assumptions and scope

All norms are taken with normalized Haar measure. A character has finite order \(m\) if \(m\) is the least positive integer such that \(\chi^m=1\), and infinite order otherwise. Requiring \(m\ge3\) ensures that \(1,\chi,\chi^2\) are distinct; thus \(\|T\|_2^2=|a|^2+|b|^2+|c|^2\). No connectedness of \(G\) is assumed. The assertion holds for arbitrary complex coefficients, including vanishing coefficients; only the nonzero equality cases have all three coefficients nonzero.

## Proof

**Step 1: Exact moment decomposition and phase majorization.** Put \(P(z)=a+bz+cz^2\), and write

\[
P(z)^3=\sum_{k=0}^{6}d_k z^k.
\]

Haar orthogonality of the characters implies

\[
\|T\|_6^6=\sum_{r=0}^{m-1}\left|\sum_{\substack{0\le k\le6\\k\equiv r\ (\mathrm{mod}\ m)}}d_k\right|^2
\]

for finite \(m\); for infinite order the sum is simply \(\sum_{k=0}^6|d_k|^2\). Coefficientwise triangle inequalities show that this cannot exceed its value after replacing \((a,b,c)\) by \((\alpha,\beta,\gamma)=(|a|,|b|,|c|)\). In particular, all positive-coefficient formulas below are true upper bounds for complex coefficients.

**Step 2: A two-parameter symmetry reduction.** Set

\[
u=\alpha^2+\gamma^2,\qquad v=\beta^2,\qquad p=\alpha\gamma,\qquad s=\alpha+\gamma=\sqrt{u+2p}.
\]

Here \(0\le p\le u/2\) and \(u+v=\|T\|_2^2\). Direct convolution of \(P^3\) gives the infinite-order expression

\[
F_\infty=(u+v)^3+6uv(u+v)+(6u+18v)p^2+(18uv+12v^2)p.
\]

The finite-order alias corrections are exactly

\[
\begin{aligned}
F_6&=F_\infty+2p^3,\\
F_5&=F_\infty+6\beta p^2s,\\
F_4&=F_\infty+6up^2+6uvp+18vp^2,\\
F_3&=F_\infty+2p^3+2\beta s(6up+uv+3p^2+8pv).
\end{aligned}
\]

For every fixed \(u>0\), \(v\ge0\), these expressions are strictly increasing as \(p\) increases from \(0\) to \(u/2\): each displayed contribution is nondecreasing and \(F_\infty\) contains a positive coefficient of \(p^2\). Consequently equality in the global maximum forces \(p=u/2\), or \(\alpha=\gamma>0\). The degenerate case \(u=0\) gives the quotient \(1\), which is below all claimed maxima. Writing \(\alpha=\gamma=r>0\), \(\beta=rt\), gives

\[
\frac{F_m}{(u+v)^3}=Q_m(t),\qquad t\ge0,
\]

with the five rational functions stated above. The limit as \(t\to\infty\) is \(1\), so no maximum is lost in this normalization.

**Step 3: One-variable global maxima.** Straight differentiation gives

\[
Q'_3(t)=-\frac{12(t-1)(t+2)(2t+1)(2t^2+2t+5)}{(t^2+2)^4},
\]
\[
Q'_4(t)=-\frac{48t(t-1)(t+1)(t^2+6)}{(t^2+2)^4},
\]
\[
Q'_5(t)=-\frac{12(4t^5+10t^3+5t^2-20t-2)}{(t^2+2)^4},
\]
\[
Q'_6(t)=-\frac{12t(4t^4+10t^2-19)}{(t^2+2)^4},
\]
\[
Q'_\infty(t)=-\frac{24t(2t^4+5t^2-10)}{(t^2+2)^4}.
\]

These show a single strict maximum at \(t=1\) for \(m=3,4\). For \(m=5\), Descartes' sign rule gives at most one positive root of the quintic in its derivative, and the polynomial changes sign from negative at zero to positive at infinity; hence there is exactly one and it is the maximum. The equations for \(m=6\) and \(m\ge7\) have unique positive roots after the substitution \(y=t^2\), giving the displayed radical values. All five maximizers are strictly positive. This proves the sharp constants.

**Step 4: All complex equality cases.** Every maximizer has \(|a|=|c|>0\) and \(|b|=t_m|a|>0\). Equality in the coefficient \(d_2=3a(ac+b^2)\) under coefficientwise majorization forces \(ac/b^2\) to be positive real. Hence there are \(\lambda\ne0\) and \(|\zeta|=1\) with \((a,b,c)=\lambda(1,t_m\zeta,\zeta^2)\). Each coefficient \(d_k\) of the cube then has phase \(\lambda^3\zeta^k\) and strictly positive magnitude. When \(m=3,4,5,6\), at least one residue class contains two indices differing by exactly \(m\), so equality in the grouped triangle inequality requires \(\zeta^m=1\). Conversely, that condition makes all contributing terms in every residue class have the same phase. For \(m\ge7\) or infinite order there is no aliasing among degrees \(0,\ldots,6\), and every \(\zeta\) works. Thus the stated equality list is exhaustive. \(\square\)

## Verification

The included standard-library-only `verify.py` reconstructs the seven coefficients of the cube, verifies the five moment identities as exact multivariate polynomial identities, and verifies each critical derivative numerator exactly. It also checks the finite-order sharpness witnesses using finite character sums. The proof of global maximality uses the monotonicity and root-count arguments above, not numerical experiments. Run `python3 verify.py` after extracting the embedded files.

## Relationship to prior work

D. V. Gorbachev's September 25, 2026 survey of sharp Bernstein–Nikolskii inequalities motivates the search for exact constants and equality geometry on constrained polynomial spaces, but its general inequalities and reproducing-kernel bounds do not determine the present finite-character, exact \(L^2\)-to-\(L^6\) constants. Y. Ling, J. Geng, J. Li, and H. Wang study Gaussian **average** Nikolskii factors rather than the deterministic worst-case extremal constant. J. M. Ash and M. Ganzburg solve a different extremal quantity involving the largest individual Fourier coefficient compared with an \(L^p\) norm; their result cannot be applied to obtain these sixth-moment maxima. Publicly indexed results on the three-frequency Fourier projection norm or the Sidon constant likewise concern different pairs of norms and do not imply this assertion.

The fifth- and sixth-order torsion cases are genuine additional alias regimes: the general no-alias constant applies only from character order seven onward. The optimizer changes between orders five, six, and seven; these values cannot be recovered from a fourth-moment estimate by interpolation, since the corresponding maximizing coefficient proportions differ.

## Limitations

The theorem treats exactly three **consecutive** distinct powers of a single character and the sixth moment, not arbitrary triples of frequencies or higher moments. The absence of an equivalent earlier specialized calculation cannot be established solely by database searches; older unindexed finite-dimensional norm calculations remain a literature risk. The embedded checker verifies finite algebraic identities but does not independently certify originality or the analytic reasoning. Independent review has not been performed.

## References

1. D. V. Gorbachev, *Sharp Bernstein–Nikolskii inequalities for polynomials and entire functions of exponential type*, arXiv:2609.32072v1, first posted 2026-09-25; https://arxiv.org/html/2609.32072v1.
2. Y. Ling, J. Geng, J. Li, and H. Wang, *Average Nikolskii factors for random trigonometric polynomials*, Journal of Inequalities and Applications 2026, article 78 (2026), https://doi.org/10.1186/s13660-026-03484-x.
3. J. M. Ash and M. Ganzburg, *An extremal problem for trigonometric polynomials*, Proc. Amer. Math. Soc. 127 (1999), 211–216, https://doi.org/10.1090/S0002-9939-99-04481-0.
