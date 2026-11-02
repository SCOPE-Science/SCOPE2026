# Exact affine-shift squarefree quartic correlations and a cubic-character variance law

## Finding
Let \(q\) be any odd prime power and \(h(T)=uT+v\) with \(u\ne0\). The number \(C_q(u,v)\) of monic quartics \(f\in\mathbb F_q[T]\) for which both \(f\) and \(f+h\) are squarefree is
\[
C_q(u,v)=q^4-2q^3+q(q-1)-2\sum_{s\in\mathbb F_q^\times}\chi_q(u^2-16s^3).
\]
Set \(C_0=q^4-2q^3+q(q-1)+2\). For uniformly selected \(u\in\mathbb F_q^\times\) and any fixed \(v\),
\[
\mathbb E_u C_q(u,v)=C_0,\qquad
\operatorname{Var}_u(C_q(u,v))=
\begin{cases}8q,&q\equiv1\pmod3,\\0,&q\not\equiv1\pmod3.\end{cases}
\]
The count is independent of the intercept \(v\). In the first case it depends only on the cubic-residue class of \(u\), through the Frobenius character sums of the curves \(Y^2=u^2-16X^3\). The second case includes every odd power of three.

## Assumptions and scope
The field is \(\mathbb F_q\) for an arbitrary odd prime power \(q\), without excluding characteristic three. Here \(\chi_q\) is the quadratic multiplicative character, extended by \(\chi_q(0)=0\). Squarefree means no nonconstant square factor in \(\mathbb F_q[T]\); equivalently, \(\gcd(f,f')=1\). The variance is the population variance over all \(q-1\) nonzero slopes; the intercept is held fixed. Only nonconstant affine shifts are treated.

## Proof
Translation \(T\mapsto T-v/u\) bijects monic quartics and changes \(uT+v\) into \(uT\), so assume \(v=0\). There are \(q^4-q^3\) squarefree monic quartics. If \(B\) is the number of monic quartics for which both \(f\) and \(f+uT\) are nonsquarefree, inclusion-exclusion gives \(C_q=q^4-2q^3+B\).

Count ordered pairs \((\alpha,\beta)\in\mathbb F_q^2\) satisfying \(f(\alpha)=f'(\alpha)=0\) and \((f+uT)(\beta)=(f+uT)'(\beta)=0\). The roots must differ: if \(\alpha=\beta\), subtraction of derivative conditions gives \(u=0\). At distinct roots, four Hermite conditions uniquely determine the four lower coefficients of a monic quartic. Hence the incidence count is precisely \(I=q(q-1)\).

Every nonsquarefree monic quartic has either a rational repeated root or is the square \(H^2\) of a monic irreducible quadratic. A quartic has more than one distinct rational repeated root precisely when it is the square of a split squarefree monic quadratic. For fixed \(f=H^2\), with \(H\) monic quadratic, suppose \(g=H^2+uT\) is nonsquarefree. The polynomial \(g\) cannot be another monic quadratic square: if \(H^2-K^2=uT\), then the quadratic factor \(H+K\) divides a nonzero linear polynomial, impossible in odd characteristic. Thus \(g\) has exactly one rational repeated root \(\beta\).

Put \(s=H(\beta)\). The equations \(g(\beta)=g'(\beta)=0\) imply \(s\ne0\), \(\beta=-s^2/u\), and \(H'(\beta)=-u/(2s)\). Conversely, each \(s\in\mathbb F_q^\times\) produces exactly one such \(H\), given by
\[
H(T)=(T-\beta)^2-\frac{u}{2s}(T-\beta)+s,
\qquad \beta=-\frac{s^2}{u}.
\]
Its discriminant is \((u^2-16s^3)/(4s^2)\). When this value is a nonzero square, \(H\) has two rational repeated roots and incidence counting overcounts by one; when it is a nonsquare, \(H\) has no rational repeated root and incidence counting undercounts by one. A zero discriminant has one repeated root and requires no correction. The correction is therefore \(-\sum_{s\ne0}\chi_q(u^2-16s^3)\). Interchanging \(f\) and \(g\) gives the same correction for those \(g\) that are quadratic squares. Since both cannot simultaneously be quadratic squares, the corrections do not overlap. Consequently
\[
B=q(q-1)-2\sum_{s\ne0}\chi_q(u^2-16s^3),
\]
which proves the first assertion.

Define \(S_q(u)=\sum_{s\in\mathbb F_q}\chi_q(u^2-16s^3)\). Its zero summand is \(\chi_q(u^2)=1\), so \(C_q=C_0-2S_q(u)\). If \(3\nmid q-1\), cubing permutes \(\mathbb F_q\) and \(S_q(u)=\sum_{y\in\mathbb F_q}\chi_q(u^2-16y)=0\). Thus \(C_q=C_0\) for every slope.

If \(3\mid q-1\), choose a nontrivial cubic character \(\psi\), extended by zero. Each nonzero cube \(y\) has \(1+\psi(y)+\overline\psi(y)\) cube roots. Changing variables \(y=(u^2/16)z\) gives
\[
S_q(u)=A\psi(u^2/16)+\overline A\,\overline\psi(u^2/16),
\quad A=\sum_{z\in\mathbb F_q}\psi(z)\chi_q(1-z).
\]
Here the unweighted quadratic-character sum vanishes. The standard Gauss-sum product formula \(A=G(\psi)G(\chi_q)/G(\psi\chi_q)\), together with \(\lvert G(\eta)\rvert^2=q\) for nontrivial multiplicative \(\eta\), proves \(\lvert A\rvert^2=q\). All three relevant characters are nontrivial because \(\psi\) has order three and \(\chi_q\) order two. As \(u\) traverses the nonzero field elements, \(\psi(u^2/16)\) is uniformly distributed among the three cube roots of unity. Orthogonality gives \(\mathbb E S_q=0\), \(\mathbb E S_q^2=2\lvert A\rvert^2=2q\), hence \(\mathbb E C_q=C_0\) and \(\operatorname{Var}C_q=4(2q)=8q\). This completes the proof for all odd prime powers.

## Verification
Execute `python verify.py` in a standard Python 3 environment. The standalone checker implements finite fields, Euclidean polynomial gcds and direct squarefreeness tests, independent of the Hermite-incidence proof. It exhausts \(628254\) monic quartic/shift checks for \(62\) shifts over fields of orders \(3,5,7,11,13,9\); additionally, it tests all slopes and their exact first and second moments for orders \(25\) and \(27\), giving \(92\) total slope-moment terms across eight fields. All comparisons passed. Finite checks are illustrations, not a proof for unrestricted field sizes.

## Relationship to prior work
Carmon and Rudnick (2012, arXiv:1205.1599) prove large-field bounds for polynomial Möbius correlations in which at least one exponent is odd. The two-squarefree-indicator count here has both exponents even and is not evaluated by that theorem. Keating and Rudnick (2015, arXiv:1504.03444, Appendix A, Theorem A.2) give a general asymptotic pair-squarefree count as the polynomial degree grows, with a nonzero error term; their result does not specify the exact fixed-degree-four correction nor its \(u\)-variance. Related fixed-degree calculations for cubic affine shifts and quartic constant shifts do not cover the nonconstant affine quartic stratum. Standard character-sum identities are used to evaluate the new finite-degree correlation.

## Limitations
The result does not include constant shifts \(u=0\), characteristic two, higher polynomial degrees, simultaneous squarefreeness of three or more translates, or a full distribution of the cubic Jacobi sums. The mathematical proof is complete under the stated hypotheses. Exhaustive historical priority cannot be guaranteed; equivalent unlocated exact formulas remain a literature risk.

## References
1. D. Carmon and Z. Rudnick, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field*, arXiv:1205.1599, first posted 8 May 2012, https://arxiv.org/abs/1205.1599 .
2. J. P. Keating and Z. Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions*, arXiv:1504.03444, first posted 14 April 2015, Appendix A, https://arxiv.org/abs/1504.03444 .
3. Standard finite-field Gauss and Jacobi character-sum identities, as used in the proof above.
