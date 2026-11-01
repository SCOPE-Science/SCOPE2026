# Parity-sharp sixth-moment synthesis for the trivial and a high-weight \(SU(2)\) character

## Finding

Write \(dg\) for probability Haar measure on \(SU(2)\). For every integer \(n\ge 2\), let \(\chi_n\) be the ordinary trace of the irreducible representation of highest weight \(n\), so \(\chi_0=1\) and \(\int\chi_n^2\,dg=1\). Define the sharp sixth-moment synthesis constant
\[
K_n=\sup_{(a,b)\ne(0,0)}\frac{\int_{SU(2)}|a+b\chi_n(g)|^6\,dg}{(|a|^2+|b|^2)^3},\qquad
S_n=\frac{(n+1)(n^2+2n+2)}2.
\]

**Odd highest weights.** For every odd \(n\ge3\), \(K_n=S_n\). All nonzero equality cases are exactly \((a,b)=(0,\lambda)\) with \(\lambda\in\mathbb C\setminus\{0\}\).

**Even highest weights.** For every even \(n\ge2\), put
\[
T_n=\frac{5n^2+10n+8}{8},\qquad
P_n(x)=x^6+15x^4+20x^3+15(n+1)x^2+6T_nx+S_n,
\]
and
\[
H_n(x)=T_n+[5(n+1)-S_n]x+(10-5T_n)x^2-10nx^3-10x^4-4x^5.
\]
There is precisely one positive real root \(x_n\) of \(H_n\), and
\[
\boxed{K_n=\frac{P_n(x_n)}{(1+x_n^2)^3}>S_n.}
\]
All nonzero equality cases are exactly \((a,b)=\lambda(x_n,1)\) for \(\lambda\in\mathbb C\setminus\{0\}\). Along even integers tending to infinity,
\[
\boxed{x_n=\frac5{4n}+O(n^{-2}),\qquad K_n-S_n=\frac{75}{32}n+O(1).}
\]
Thus mixing in the trivial character strictly improves the sharp sixth moment at every even highest weight but at no odd highest weight at least three. The parity effect is exact at finite weights and has an explicitly quantified large-weight scale.

## Assumptions and scope

All characters are unnormalized traces, not dimension-normalized traces. In particular, \(\chi_n(e)=n+1\) and \(\|\chi_n\|_{L^2(dg)}=1\). Coefficients \(a,b\) are arbitrary complex scalars; the stated optimizer families include their global complex phases. The parameter \(n\) is any integer at least two, not a fixed-size numerical census. The norm exponent is exactly six. The result does not assert a bound for larger multi-character spans, other exponents, or deformed quantum groups.

## Proof

**1. Exact character moments.** Put \(\mu_j(n)=\int\chi_n^j\,dg\). The Weyl character and class-integration formulas give
\[
\chi_n(e^{i\theta})=\sum_{h=0}^{n}e^{i(n-2h)\theta},\qquad
\int F(g)\,dg=\frac2\pi\int_0^\pi F(e^{i\theta})\sin^2\theta\,d\theta
\]
for central \(F\). Equivalently, for Laurent polynomials symmetric under inversion and \(z=e^{i\theta}\), the Haar integral is \(\operatorname{CT}[(1-z^2)F(z)]\). If \(jn\) is even and \(j\ge2\), substitution \(u=z^2\) gives the exact finite coefficient identity
\[
\mu_j(n)=[u^{jn/2}]\frac{(1-u^{n+1})^j}{(1-u)^{j-1}};
\]
if \(jn\) is odd, \(\mu_j(n)=0\). Expanding the numerator by the binomial formula yields, for every \(n\ge2\),
\[
\mu_0=1,\quad \mu_1=0,\quad \mu_2=1,\quad
\mu_3=\begin{cases}1&n\text{ even},\\0&n\text{ odd},\end{cases}
\quad\mu_4=n+1,
\]
\[
\mu_5=\begin{cases}(5n^2+10n+8)/8&n\text{ even},\\0&n\text{ odd},\end{cases}
\qquad \mu_6=S_n.
\]
To check the two nontrivial polynomial identities without unspecified enumeration, for \(n=2k\) the coefficient formula is
\[
\mu_5=\binom{5k+3}{3}-5\binom{3k+2}{3}+10\binom{k+1}{3},\quad
\mu_6=\binom{6k+4}{4}-6\binom{4k+3}{4}+15\binom{2k+2}{4};
\]
for \(n=2k+1\), it gives
\[
\mu_6=\binom{6k+7}{4}-6\binom{4k+5}{4}+15\binom{2k+3}{4}.
\]
Each displayed finite binomial expression expands to the asserted formula, including the smallest eligible indices under the convention \(\binom ab=0\) for integers \(0\le a<b\). Alternatively, repeated Clebsch–Gordan products \(\chi_j\chi_n=\sum_{h=|j-n|,\,h\equiv j+n\ (2)}^{j+n}\chi_h\) independently give the same moments.

**2. Reduction from complex coefficients.** Every \(\mu_j(n)\) is nonnegative: it is the multiplicity of the trivial representation in the tensor power corresponding to \(\chi_n^j\). Expanding
\[
\int|a+b\chi_n|^6\,dg=\sum_{k,l=0}^3\binom3k\binom3l
 a^{3-k}\overline a^{3-l}b^k\overline b^l\mu_{k+l}(n)
\]
and applying the triangle inequality termwise shows the maximum at fixed \((|a|,|b|)\) occurs for aligned real nonnegative coefficients. For even \(n\), \(\mu_3=1\) supplies a strictly phase-sensitive term whenever \(ab\ne0\); alignment is then the only maximizing relative phase. For odd \(n\), the phase reduction still gives an upper bound, sufficient because the optimum found below uses \(a=0\).

**3. Odd-weight rigidity.** Set \(t=|b|^2/(|a|^2+|b|^2)\). For odd \(n\), the preceding reduction gives
\[
\frac{\int|a+b\chi_n|^6\,dg}{(|a|^2+|b|^2)^3}
\le (1-t)^3+15t(1-t)^2+15(n+1)t^2(1-t)+S_nt^3.
\]
The right side is a cubic Bernstein polynomial with control values \(1,5,5(n+1),S_n\). Since \(S_n>5(n+1)\) for every odd \(n\ge3\), each control value is strictly below \(S_n\), except the last. Thus the bound is strictly smaller than \(S_n\) unless \(t=1\). Equality at \(t=1\) gives only the pure \(\chi_n\) line.

**4. Even-weight sharp optimizer.** For even \(n\) let \(x=|a|/|b|\) when \(b\ne0\). The phase reduction and moment table show that the best value at ratio \(x\) is exactly \(Q_n(x)=P_n(x)/(1+x^2)^3\). Direct differentiation gives
\[
Q_n'(x)=\frac{6H_n(x)}{(1+x^2)^4}.
\]
Here \(H_n(0)=T_n>0\). For \(n=2\), the linear coefficient of \(H_n\) vanishes; for even \(n\ge4\), it is negative because \(S_n>5(n+1)\). All remaining nonconstant coefficients are strictly negative for every even \(n\ge2\): \(T_n\ge6\) and \(n>0\). Hence \(H_n\) is strictly decreasing on \((0,\infty)\) and tends to \(-\infty\). It has one positive root \(x_n\); \(Q_n\) rises to that root and then falls. The omitted case \(b=0\) has value \(1\), while \(Q_n(0)=S_n\ge15\). Consequently the root gives the unique global optimum, with \(K_n>S_n\). Strict phase alignment proves the full equality classification.

**5. Large-even-weight correction.** The exact moment formulas give \(T_n=(5/8)n^2+O(n)\) and \(S_n=n^3/2+O(n^2)\). For fixed \(c>0\),
\[
\frac{H_n(c/n)}{n^2}=\frac58-\frac c2+O(n^{-1}).
\]
Uniqueness of the positive root implies \(nx_n\to5/4\). Substitution into the polynomial and a mean-value estimate using \(H_n'(c/n)=-n^3/2+O(n^2)\) uniformly near \(c=5/4\) sharpens this to \(x_n=5/(4n)+O(n^{-2})\). Finally,
\[
K_n-S_n=\frac{6T_nx_n+[15(n+1)-3S_n]x_n^2+20x_n^3+(15-3S_n)x_n^4+(1-S_n)x_n^6}{(1+x_n^2)^3}
=\frac{75}{32}n+O(1),
\]
as claimed.

## Verification

The standalone file `check_su2.py` requires only standard Python 3 and runs with `python3 check_su2.py`. Its independent tests compare: (i) Clebsch–Gordan decompositions against the explicit polynomial moments; (ii) those values against Weyl constant-term extraction; (iii) discrete Weyl quadrature on sufficiently fine nonaliasing grids; and (iv) stationary-root bisection and moment maximization for finite weights, together with large-even-weight checks. The completed run passed 983 deterministic assertions. The proof above, not these finite tests, establishes the infinite family and uniqueness.

## Relationship to prior work

Sang-Gyun Youn, *A Khintchine inequality for central Fourier series on non-Kac compact quantum groups* (arXiv:2408.13519, initial public version 2024-08-24), contrasts classical compact connected semisimple groups with non-Kac quantum groups and proves general Khintchine-type estimates in the latter setting. The inspected primary sections do not state the finite classical \(SU(2)\) two-character sharp sixth-moment extremal law above. Koornwinder's *Representations of SU(2) and Jacobi polynomials* (arXiv:1606.08189) supplies standard representation-theoretic background rather than this norm optimization.

Earlier work on character \(L^p\) growth, notably Giulini, Soardi and Travaglini's 1982 *Norms of characters and Fourier series on compact Lie groups*, addresses individual-character estimates and general Fourier-series phenomena. Full text of that earlier paper could not be examined in this review; an implicit specialization remains a priority risk. Other publicly indexed neighboring results treat fourth moments of high-weight packets, sixth moments of different character pairs, or abelian character spectra, and do not provide an identified stronger statement implying the present all-\(n\) parity classification. The first-weight plane \(\operatorname{span}\{\chi_0,\chi_1\}\), analyzed elsewhere, is deliberately outside the asserted new range.

## Limitations

The result is local to the two-dimensional central Fourier space \(\operatorname{span}\{1,\chi_n\}\) with \(n\ge2\); it does not solve sharp synthesis in arbitrary character spans. The asymptotic is along even integers only. Independently verifying historical priority, especially in specialized older character-norm literature, remains necessary. No independent mathematical audit has been performed.

## References

1. Sang-Gyun Youn, *A Khintchine inequality for central Fourier series on non-Kac compact quantum groups*, arXiv:2408.13519v1, 2024-08-24, https://arxiv.org/abs/2408.13519.
2. Tom H. Koornwinder, *Representations of SU(2) and Jacobi polynomials*, arXiv:1606.08189v1, 2016-06-27, https://arxiv.org/abs/1606.08189.
3. S. Giulini, P. M. Soardi and G. Travaglini, *Norms of characters and Fourier series on compact Lie groups*, Journal of Functional Analysis 46 (1982), 88–101, https://doi.org/10.1016/0022-1236(82)90045-3.
