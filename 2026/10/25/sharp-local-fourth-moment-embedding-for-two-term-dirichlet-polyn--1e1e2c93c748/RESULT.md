# Sharp local fourth-moment embedding for two-term Dirichlet polynomials

## Finding
Consider all Dirichlet polynomials supported on at most two positive integers, \(P(s)=a m^{-s}+b n^{-s}\) with \(1\le m<n\), \(a,b\in\mathbb C\). Write
\[
\mathcal R(P)=\frac{\displaystyle\sup_{\theta\in\mathbb R}\int_\theta^{\theta+1}|P(\tfrac12+it)|^4\,dt}{\|P\|_{\mathscr H^4}^4}.
\]
The sharp two-term constant is
\[
\sup_{m<n}\ \sup_{(a,b)\ne(0,0)}\mathcal R(P)
 = C_{4,2}=\frac{1+A\xi+B\xi^2+(A/2)\xi^3+\xi^4/4}{1+4\xi^2+\xi^4}
 =1.60766932608856734\ldots,
\]
where \(A=2\sqrt2\,\operatorname{sinc}(\tfrac12\log2)\), \(B=2+\operatorname{sinc}(\log2)\), \(\operatorname{sinc}u=\sin(u)/u\), and \(\xi\) is the unique positive root of
\[
-\tfrac A2x^6+(2-2B)x^5-Ax^4-3x^3-\tfrac{5A}{2}x^2+(2B-8)x+A=0,
\quad \xi=0.44410406396943376\ldots.
\]
Equality for a nonzero polynomial occurs exactly when \(m=1\), \(n=2\), \(a b\ne0\), \(|b|/|a|=\xi\), and the maximizing interval is centered on an aligned relative phase:
\[
\arg(b/a)-(\theta+\tfrac12)\log2\equiv0\pmod{2\pi}.
\]
In particular this supplies the explicit lower bound \(C_4\ge C_{4,2}>3/2\) for the unrestricted local \(\mathscr H^4\)-embedding constant; it does not determine \(C_4\).

## Assumptions and scope
The normalized \(\mathscr H^4\) norm is the vertical Bohr mean
\[
\|P\|_{\mathscr H^4}^4=\lim_{T\to\infty}\frac1{2T}\int_{-T}^T|P(it)|^4\,dt.
\]
The local trace is an unweighted integral over an interval of length exactly one on \(\operatorname{Re}s=1/2\), optimized over all real starting points. The theorem quantifies over every pair of distinct positive integer frequencies and arbitrary complex coefficients, including one coefficient zero. No assertion is made for three or more frequencies or other interval lengths/exponents. The primary mathematical classification is MSC2020 30B50.

## Proof
**Norm identity.** For any distinct positive integers \(m,n\), expand the fourth power along the imaginary axis. The nonconstant exponentials \((n/m)^{ikt}\), \(k\in\{-2,-1,1,2\}\), have zero vertical mean. Hence, writing \(u=|a|\), \(v=|b|\),
\[
\|P\|_{\mathscr H^4}^4=u^4+4u^2v^2+v^4.
\]

**All frequencies except \((1,2)\).** Suppose first \(m\ge2\). The critical-line bound \(|P(\tfrac12+it)|\le(u+v)/\sqrt2\) gives, with \(x=v/u\) if \(u>0\),
\[
\mathcal R(P)\le\frac{(1+x)^4}{4(1+4x^2+x^4)}\le\frac23,
\]
since
\[
8(1+4x^2+x^4)-3(1+x)^4=(x-1)^2(5x^2-2x+5)\ge0.
\]
If \(m=1\) and \(n\ge3\), pointwise \(|P(\tfrac12+it)|\le u+v/\sqrt3\). With \(y=v/(\sqrt3u)\), the identity
\[
3(1+12y^2+9y^4)-2(1+y)^4
=(1-4y)^2+y^2(25y^2-8y+8)>0
\]
shows \(\mathcal R(P)<3/2\), since the quadratic \(25y^2-8y+8\) is strictly positive for real \(y\). The cases \(u=0\) or \(v=0\) have ratio at most one and are covered separately.

**The two smallest frequencies.** Put \(m=1\), \(n=2\), and \(x=v/u>0\). Let \(w=\log2\) and \(\varphi=\arg(b/a)-(\theta+1/2)w\). Direct integration after centering \([\theta,\theta+1]\) gives
\[
\frac{\int_\theta^{\theta+1}|P(\tfrac12+it)|^4dt}{u^4}
=1+2x^2+\tfrac14x^4+2\sqrt2 x(1+\tfrac12x^2)\operatorname{sinc}(w/2)\cos\varphi+x^2\operatorname{sinc}(w)\cos(2\varphi).
\]
Both sinc factors are positive because \(0<w<\pi\). The unique maximizing phase modulo \(2\pi\) is \(\varphi=0\), where the numerator equals \(1+Ax+Bx^2+(A/2)x^3+x^4/4\), with \(A,B\) as above. Dividing by the norm identity produces \(F(x)\) in the finding.

Let \(D(x)=1+4x^2+x^4\) and \(N(x)=1+Ax+Bx^2+(A/2)x^3+x^4/4\). Direct differentiation gives \(N'D-ND'=Q(x)\), the degree-six polynomial displayed in the finding. Since \(A>0\) and \(2<B<3\), all nonconstant coefficients of \(Q\) are negative. Thus \(Q\) is strictly decreasing on \((0,\infty)\), with \(Q(0)=A>0\) and \(Q(x)\to-\infty\), so it has precisely one positive root \(\xi\). Consequently \(F\) increases up to \(\xi\) and decreases thereafter; its maximum is unique. The equality classification follows from strictness of the preceding frequency bounds and the strict phase alignment.

For completeness, \(\log2<7/10\), \(\sqrt2>7/5\), and \(\sin t/t\ge1-t^2/6\) for the relevant positive arguments imply \(A>27/10\) and \(B>29/10\). Substitution into \(F(1/2)\) gives \(F(1/2)>3/2\), separating the \((1,2)\) optimizer strictly from every other integer pair.

## Verification
The exact identities above are algebraic and cover every admissible integer pair. The companion `verify.py` evaluates the unique root by bisection, checks the polynomial identities using coefficient arithmetic and tests the integrated fourth power independently by deterministic quadrature on representative integer frequency pairs. Run `python3 verify.py` with the standard Python library. The numerical decimal values are illustrations, not replacements for the strict analytic inequalities or the all-integer argument.

## Relationship to prior work
Chen, Fang, Guo, Hou, Shao and Zhou (2026, arXiv:2609.11560) study the existence of a finite uniform local embedding bound for all Dirichlet polynomials and identify the allowed exponent regime. The available abstract does not state this sharp two-monomial fourth-moment calculation or its support rigidity. Their full manuscript could not be inspected, which leaves a specifically acknowledged comparison risk; absence from an abstract is not proof of absence from the complete paper.

Brevig (2016, arXiv:1606.03101) gives an optimal constant for a **weighted full-line** embedding of \(\mathscr H^2\), and separately discusses unweighted local \(\mathscr H^2\) estimates without determining their sharp local constant. Its setting and norm exponent differ from the present length-one unweighted fourth moment. General sharp Haar \(\Lambda(4)\) constants for character pairs control the Bohr mean used in the denominator but have no unweighted critical-line local trace numerator; their conclusions do not imply the present constant.

## Limitations
This is a complete sharp result **only** for polynomials with at most two nonzero Dirichlet coefficients; it is neither a global extremal theorem nor a determination of the unrestricted \(C_4\). Priority remains conditional on access to unavailable full relevant manuscripts and on other unindexed elementary computations. No independent mathematical audit has been performed. The local interval must have length one, the critical-line real part is fixed at one half, and the exponent is four.

## References
1. B. Chen, X. Fang, F. Guo, S. Hou, Y. Shao, Q. Zhou, *The Local Embedding Problem for Hardy Spaces of Dirichlet Series*, arXiv:2609.11560, first posted 2026-09-10, https://arxiv.org/abs/2609.11560.
2. O. F. Brevig, *An embedding constant for the Hardy space of Dirichlet series*, arXiv:1606.03101, first posted 2016-06-09, https://arxiv.org/abs/1606.03101.
