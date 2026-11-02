# Square-class Fourier support of unit quadratic shells over prime-square rings

## Finding

Let \(p\) be an odd prime, \(R=\mathbb Z/p^2\mathbb Z\), and \(t\in R^\times\). Define the smooth affine quadratic shell
\[
S_t=\{(a,b,c)\in R^3:a^2+bc=t\},\qquad
Q^\vee(u,v,w)=u^2+4vw.
\]
Use the **unnormalized, positive-sign** Fourier multiplier
\[
F_t(u,v,w)=\sum_{(a,b,c)\in S_t}
\exp(2\pi i(ua+vb+wc)/p^2).
\]
Write \(\chi_p\) for the Legendre symbol with \(\chi_p(0)=0\), \(\varepsilon=\chi_p(t)\in\{-1,1\}\), and \(e_m(s)=\exp(2\pi is/m)\). A complete multiplier formula is as follows:

* At the zero frequency, \(F_t(0,0,0)=p^4+\varepsilon p^3\).
* If \(M=(u,v,w)=pM'\) is nonzero, with \(M'\in\mathbb F_p^3\), then
  \[
  F_t(M)=\varepsilon p^3\sum_{r\in\mathbb F_p:\,r^2=tQ^\vee(M')}e_p(r).
  \]
* If \(M\notin pR^3\), then
  \[
  F_t(M)=p^2\sum_{r\in R:\,r^2=tQ^\vee(M)}e_{p^2}(r).
  \]

Consequently, with reductions and arithmetic in the appropriate residue rings,
\[
\boxed{F_t(M)\ne0\iff
\begin{cases}
\chi_p(tQ^\vee(M))=1,&M\notin pR^3,\\
\chi_p(tQ^\vee(M/p))\in\{0,1\},&0\ne M\in pR^3,\\
\text{always},&M=0.
\end{cases}}
\]
The Fourier characters with the complementary frequencies form an explicit basis for the nullspace of unnormalized convolution by \(\mathbf1_{S_t}\) on \(\ell^2(R^3)\). The exact convolution rank is
\[
\boxed{\operatorname{rank}T_t=p^2+\frac{p(p-1)(p+\varepsilon)(p^3+1)}2.}
\]
In particular, the ranks for quadratic-residue and quadratic-nonresidue unit levels differ by precisely
\[
\boxed{\operatorname{rank}T_{\mathrm{res}}-\operatorname{rank}T_{\mathrm{nonres}}=p(p-1)(p^3+1).}
\]
For \(p=3\), these ranks are respectively \(345\) and \(177\) in ambient dimension \(729\); for \(p=5\), they are \(7585\) and \(5065\) in ambient dimension \(15625\). Both support fractions tend to \(1/2\) as \(p\to\infty\), but their finite-prime difference is exact and substantial.

## Assumptions and scope

All variables and congruences are over \(R=\mathbb Z/p^2\mathbb Z\) unless explicitly reduced to \(\mathbb F_p\). The level \(t\) is required to be invertible and \(p\) odd. The value \(M/p\) appears only when all coordinates of \(M\) are divisible by \(p\); it means their residues after dividing by \(p\), defined in \(\mathbb F_p^3\). The sign of the Fourier exponential is positive. Multiplication by the shell indicator is *additive convolution*, not multiplication of functions.

Every shell is smooth: \(\nabla(a^2+bc)=(2a,c,b)\) is never zero modulo \(p\) on \(S_t\), because \(t\) is a unit. Its reduction contains \(p^2+\varepsilon p\) points, each with exactly \(p^2\) lifts satisfying the level equation.

## Proof

**1. Finite-field shell transform.** Write \(Q(a,b,c)=a^2+bc\), \(D=Q^\vee(U)=u^2+4vw\), and \(G=\sum_{x\in\mathbb F_p}e_p(x^2)\). For \(s\ne0\), completing the square in \(a\) and summing first over \(b,c\) gives
\[
\sum_{a,b,c\in\mathbb F_p}e_p(sQ(a,b,c)+ua+vb+wc)
=p\chi_p(s)G\,e_p(-D/(4s)).
\]
Orthogonality for the equation \(Q=t\) then gives its finite-field Fourier coefficient
\[
H_t(U)=p^2\mathbf1_{\{U=0\}}+
G\sum_{s\ne0}\chi_p(s)e_p(-ts-D/(4s)).
\]
The elementary Salié identity needed here is, for every \(t\ne0\),
\[
G\sum_{s\ne0}\chi_p(s)e_p(-ts-D/(4s))
=p\chi_p(t)\sum_{r^2=tD}e_p(r).
\]
For completeness, both sides have identical Fourier transforms as functions of \(D\): at frequency \(h=0\) both vanish; at \(h\ne0\), both equal \(pG\chi_p(-h)e_p(t/(4h))\). Indeed, the left transform imposes \(s=-1/(4h)\), while the right reduces to the quadratic Gauss sum in \(r\). Fourier inversion proves the identity without invoking a nonstandard black box. The usual identity \(G^2=\chi_p(-1)p\) is the sole Gauss-sum input. Thus
\[
H_t(0)=p^2+\varepsilon p,\quad
H_t(U)=\varepsilon p\sum_{r^2=tQ^\vee(U)}e_p(r)\quad(U\ne0).
\]
As \(p\) is odd, a sum of two roots \(e_p(r)+e_p(-r)\) cannot vanish; the singleton root \(r=0\) contributes \(1\). This proves the precise finite-field support criterion.

**2. Frequencies divisible by \(p\).** Every point on the reduced shell lifts to exactly \(p^2\) points on \(S_t\). For \(M=pM'\) their phase is constant along these lifts. Hence \(F_t(pM')=p^2H_t(M')\), giving the first two cases of the multiplier formula, including \(F_t(0)=p^2(p^2+\varepsilon p)\).

**3. Primitive frequencies.** Fix \(M\notin pR^3\). For each \(\bar x\) on the reduced smooth shell, choose a lift \(x\in S_t\). The lifts of \(\bar x\) in \(S_t\) are \(x+py\) with \(\nabla Q(\bar x)\cdot y=0\). Their Fourier contribution is zero unless
\[
\bar M=\lambda\nabla Q(\bar x),\quad\lambda\in\mathbb F_p^\times;
\]
when the condition holds, the contribution is exactly \(p^2e_{p^2}(M\cdot x)\). Such stationary residues exist precisely when \(tQ^\vee(\bar M)\) is a nonzero square. Each root \(r\in R\) of \(r^2=tQ^\vee(M)\) is automatically a unit, and the point
\[
 x_r=(tu/r,\,2tw/r,\,2tv/r)
\]
lies on \(S_t\), is a stationary lift, and satisfies \(M\cdot x_r=r\). By the uniqueness of lifting simple square roots, these points correspond bijectively to the stationary residues. Summing their contributions proves the primitive multiplier formula. The two terms \(e_{p^2}(r)+e_{p^2}(-r)\) cannot cancel: their quotient would otherwise be \(-1\), impossible for odd-order roots of unity.

**4. Rank and multiplicity counting.** For \(d\in\mathbb F_p\), the number of \(U=(u,v,w)\in\mathbb F_p^3\) with \(u^2+4vw=d\) is \(p^2\) when \(d=0\), and \(p^2+p\chi_p(d)\) when \(d\ne0\). This follows by counting \((v,w)\) for each \(u\). The number of reduced frequencies with \(\chi_p(tQ^\vee(U))=1\) is
\[
 B_\varepsilon=\frac{p-1}{2}(p^2+\varepsilon p).
\]
Each such reduction has \(p^3\) primitive lifts, all supported. Among frequencies in \(pR^3\), the supported number is \(p^2+B_\varepsilon\), including the origin. Therefore
\[
\operatorname{rank}T_t=p^3B_\varepsilon+p^2+B_\varepsilon
=p^2+\frac{p(p-1)(p+\varepsilon)(p^3+1)}2.
\]
Fourier characters form a basis of the ambient convolution operator, so counting supported multipliers gives its rank and identifying absent multipliers gives its entire nullspace. Subtracting the two rank formulas proves the square-class gap.

## Verification

The independent finite enumeration in `certificate.py` constructs each shell directly and calculates its Fourier coefficients in the integral polynomial basis of \(\mathbb Q(\zeta_{p^2})\). Two polynomial coefficient vectors represent the same cyclotomic number exactly when their difference is divisible by
\[
\Phi_{p^2}(z)=1+z^p+\cdots+z^{(p-1)p}.
\]
The checker tests the *full multiplier formula*, not merely zero/nonzero classification. It exhausts all \(p^6\) frequencies for one residue and one nonresidue unit level at each of \(p=3\) and \(p=5\), and tests fixed deterministic frequency subsets at \(p=7\). Full checked ranks are \(345,177\) at \(p=3\) and \(7585,5065\) at \(p=5\). The finite checks are illustrative and do not replace the universal proof above. Run `python certificate.py` with Python 3; no third-party packages are needed.

## Relationship to prior work

Iosevich and Koh (arXiv:0804.4505v1, 28 April 2008), especially their quadratic-surface Fourier calculation in Section 2, treat quadratic levels in vector spaces **over finite fields** and use Salié-type sums to obtain Fourier decay and extension bounds. Their calculation supplies the finite-field starting point, but not the two-conductor spectral-null classification or square-class convolution rank over \(\mathbb Z/p^2\mathbb Z\).

Hickman and Wright (arXiv:1801.03176v1, 9 January 2018) develop Fourier restriction and Kakeya theory over the residue rings, emphasizing parabolic graphs and scale effects. Their analyzed restriction estimates do not state an exact Fourier-null classification for the present smooth ternary shells. Watanabe (arXiv:2607.21913v1, 24 July 2026) determines eigenmatrices for **Smith-type** translation association schemes on matrix rings; a fixed-level quadratic shell is not a union of Smith-type classes, so its present multiplier is not an immediate implication of that theorem.

An equivalent classification might exist in a different language of local Bessel/Salié transforms, special-linear conjugacy classes, or finite-ring association schemes. This risk has not been completely eliminated.

## Limitations

No assertion is made for \(p=2\), for nonunit level \(t\), or for rings of length greater than two. The displayed formulas supply all Fourier multipliers and the complete kernel, but no separately enumerated list of coinciding nonzero complex eigenvalues is claimed. Literature searches cannot establish absolute priority; independent mathematical review has not been performed.

## References

1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1 (28 April 2008), https://arxiv.org/abs/0804.4505 .
2. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176v1 (9 January 2018), https://arxiv.org/abs/1801.03176 .
3. Y. Watanabe, *Bivariate Affine q-Krawtchouk Polynomials and Association Schemes over Galois Rings*, arXiv:2607.21913v1 (24 July 2026), https://arxiv.org/abs/2607.21913 .
4. L. J. Mordell, *On Salié's sum*, Glasgow Mathematical Journal (historical identity), https://www.cambridge.org/core/journals/glasgow-mathematical-journal/article/on-salies-sum/38879667B15CD585F5BC44A78A4FE404 .
