# Sharp variance-exact sub-gamma envelopes for symmetric bounded Lévy jumps

## Finding

Let \(X\) be a centered, nondegenerate, symmetric, infinitely divisible real random variable with Gaussian variance \(a\ge0\), symmetric Lévy measure \(\nu\) supported on \([-L,L]\setminus\{0\}\), and \(L>0\). Put \(V=a+\int x^2\nu(dx)>0\). The **variance-exact sub-gamma scale** \(c_*(X)\) is the smallest \(c\ge0\) such that
\[
\log\mathbb E e^{tX}\le \frac{Vt^2}{2(1-ct)}\quad\text{for every }0\le t<1/c,
\]
where \(1/0=+\infty\). Set
\[
r(z)=\begin{cases}2(\cosh z-1)/z^2,&z\ne0,\\1,&z=0,\end{cases}
\qquad
\gamma=\max_{z>0}\frac{1-r(z)^{-1}}z.
\]
Then \(c_*(X)\le L\gamma\). The constant is sharp, and equality holds **if and only if** \(a=0\) and \(\nu\) is concentrated on the two endpoints \(\{-L,L\}\), with equal masses. In particular, the unique maximizing argument \(z_0\) for \(\gamma\) lies in \((3.82237,3.82238)\), and \(\gamma\approx0.174217959651700457\). This is a strict improvement over the usual variance-exact Bernstein scale \(L/3\) for the symmetric infinitely divisible class.

There is an exact sharp refinement that quantifies the cost of smaller jumps or a Gaussian component. Define the variance-weighted probability measure on \([0,L]\) by
\[
\mu=\frac{a}{V}\delta_0+\frac1V\bigl(|x|\bigr)_\#\bigl(x^2\nu(dx)\bigr).
\]
For any \(0\le\alpha<1\) and \(0\le\eta<1\), if \(\mu([0,\alpha L])\ge\eta\), put
\[
R_{\alpha,\eta}(z)=(1-\eta)r(z)+\eta r(\alpha z),\qquad
\Gamma_{\alpha,\eta}=\max_{z>0}\frac{1-R_{\alpha,\eta}(z)^{-1}}z.
\]
Then \(c_*(X)\le L\Gamma_{\alpha,\eta}\), and equality holds if and only if
\[
\mu=(1-\eta)\delta_L+\eta\delta_{\alpha L}.
\]
The bound is attained by a symmetric compound-Poisson law with jump magnitudes \(L\) and \(\alpha L\) when \(\alpha>0\), and by a Gaussian-plus-symmetric-compound-Poisson law when \(\alpha=0\). If \(\eta>0\), then \(\Gamma_{\alpha,\eta}<\gamma\). In the pure Gaussian-variance dilution case,
\[
\Gamma_{0,\eta}\sim\frac1{\log(1/(1-\eta))}\quad(\eta\uparrow1).
\]

## Assumptions and scope

The Lévy measure is symmetric, has no mass at zero, is supported on \([-L,L]\), and satisfies \(\int(1\wedge x^2)\nu(dx)<\infty\). Infinite jump activity is allowed. The Gaussian part is independent in the Lévy–Khintchine representation. Symmetry and centering exclude a nonzero deterministic location shift. The variance \(V\) is strictly positive. The scale parameter is calibrated to the **actual variance**, not a larger proxy; optimality concerns the moment-generating-function inequality, not exact tail probabilities. The fraction \(\mu([0,\alpha L])\) measures variance contributed by Gaussian noise and by jumps of magnitude at most \(\alpha L\).

## Proof

**Step 1: normalized cumulant representation.** By symmetry and bounded Lévy support, for every real \(t\),
\[
K(t)=\log\mathbb E e^{tX}=\frac{at^2}{2}+\int(\cosh(tx)-1)\nu(dx)
=\frac{Vt^2}{2}\int_{[0,L]}r(tu)\mu(du).
\]
Write \(M(t)=\int r(tu)\mu(du)\). The even entire function \(r\) has power series \(r(z)=\sum_{n\ge0}2z^{2n}/(2n+2)!\), so \(M(t)\ge1\), with strict inequality for positive \(t\) unless \(X\) is Gaussian. Rearranging the definition of feasibility separately on \(t<1/c\) and \(t\ge1/c\) gives the exact formula
\[
c_*(X)=\sup_{t>0}\frac{1-M(t)^{-1}}t. \tag{1}
\]
Indeed, feasibility implies the indicated expression is at most \(c\); for \(t\ge1/c\) this holds automatically since the expression is at most \(1/t\). Conversely, if \(c\) is that supremum, then for each \(0<t<1/c\), \(M(t)^{-1}\ge1-ct>0\), giving feasibility. The supremum is attained for non-Gaussian \(X\), because the expression is positive for some \(t\) but tends to zero both at zero (symmetry removes the cubic cumulant) and at infinity (it is at most \(1/t\)).

**Step 2: extremal variance-profile comparison and equality.** The series shows \(r\) is strictly increasing on positive arguments. Write \(m=\mu([0,\alpha L])\ge\eta\). For every \(t>0\),
\[
M(t)\le m r(\alpha Lt)+(1-m)r(Lt)
\le \eta r(\alpha Lt)+(1-\eta)r(Lt).
\]
Both inequalities are strict unless \(m=\eta\), all the lower-group mass is at \(\alpha L\), and all other mass is at \(L\). Apply the strictly increasing map \(u\mapsto(1-u^{-1})/t\) and formula (1), with \(z=Lt\). The claimed bound follows. For a law not having the specified variance profile, strict inequality holds for every \(t>0\). Since its optimizing argument is finite and positive, its optimal scale is strictly less than the envelope. Conversely, the specified profile gives equality identically in the cumulant comparison. It is realized by independent symmetric compound-Poisson components with each sign rate \((1-\eta)V/(2L^2)\) at \(L\) and, if \(\alpha>0\), each sign rate \(\eta V/(2\alpha^2L^2)\) at \(\alpha L\); for \(\alpha=0\), use independent Gaussian variance \(\eta V\) in place of the second component. Setting \(\eta=0\) proves the universal sharp bound and its equality characterization. For \(\eta>0\) and \(\alpha<1\), \(R_{\alpha,\eta}(z)<r(z)\) at every \(z>0\), and compact attainment yields \(\Gamma_{\alpha,\eta}<\gamma\).

**Step 3: global uniqueness of the universal optimizer.** Let \(A(z)=zr'(z)\) and \(B(z)=r(z)(r(z)-1)\). The sign of the derivative of \((1-r^{-1})/z\) is the sign of \(A-B\). With \(a_n=2/(2n+2)!\), the coefficient of \(z^{2n}\) in \(A\) is \(2n a_n\), while the coefficient in \(B\) is \(a_n C_n\), where
\[
C_n=\frac{4^{n+2}-4}{(2n+3)(2n+4)}-1>0\quad(n\ge1).
\]
The identity follows by expanding \(r^2=[2\cosh(2z)-8\cosh z+6]/z^4\). Put \(P_n=4^{n+2}-4\), \(D_n=(2n+5)(2n+6)\), \(E_n=(2n+3)(2n+4)\). Then
\[
nC_{n+1}-(n+1)C_n
=1+P_n\left(\frac{4n}{D_n}-\frac{n+1}{E_n}\right)+\frac{12n}{D_n}>0.
\]
The bracket is positive since its numerator after multiplying by \(D_nE_n\) is \(8+(n-1)(12n^2+42n+38)>0\). Therefore \(2n/C_n\) is strictly decreasing. A ratio-of-positive-power-series argument now shows \(A(z)/B(z)\) is strictly decreasing on \((0,\infty)\): writing the derivative of the quotient as a sum over pairs of coefficient indices, all off-diagonal terms are strictly negative because the coefficient ratios decrease. At zero \(A/B\to2\); at infinity \(A/B\to0\), since \(r(z)\sim e^z/z^2\). Thus \(A/B=1\) has a unique positive solution \(z_0\), and the envelope increases before \(z_0\) and decreases afterward. Equivalently \(z_0\) is the unique positive zero of
\[
z^3\sinh z-z^2(\cosh z-1)-2(\cosh z-1)^2=0.
\]
The fully rational Taylor remainder checker in `check.py` certifies opposite signs at \(3.82237\) and \(3.82238\). Numeric evaluation yields the stated \(\gamma\).

**Step 4: rare maximal-jump variance limit.** At \(\alpha=0\), write \(\varepsilon=1-\eta\) and \(H_{\varepsilon}(z)=\varepsilon(r(z)-1)/(z[1+\varepsilon(r(z)-1)])\). Set \(s=\log(1/\varepsilon)\). For any fixed \(\delta\in(0,1)\), on \(0<z\le(1-\delta)s\), Taylor's integral remainder gives \(r(z)-1\le z^2e^z/12\), so \(sH_\varepsilon(z)\le s^2\varepsilon^\delta/12\to0\). For \(z\ge(1-\delta)s\), \(H_\varepsilon(z)\le1/z\le1/((1-\delta)s)\). This proves \(\limsup s\Gamma_{0,\eta}\le1/(1-\delta)\). Taking \(z=(1+\delta)s\), the asymptotic \(r(z)\sim e^z/z^2\) gives \(\varepsilon[r(z)-1]\to\infty\), so \(sH_\varepsilon(z)\to1/(1+\delta)\). Letting \(\delta\downarrow0\) proves the asserted asymptotic.

## Verification

`check.py` is a standalone Python 3 script using standard-library rational arithmetic. It reproduces 1,625 exact rational assertions: factorial coefficient identities, strict coefficient-ratio positivity, monotonicity checks at integer indices, normalized hyperbolic bounds, two-point variance-profile comparisons, and rigorous Taylor enclosures of the derivative signs at the stated rational endpoints. Run `python3 check.py`. The saved `check_output.txt` contains the actual invocation result. Finite checks are not used as a proof of the infinite power-series or full class results; the preceding arguments establish those assertions analytically.

## Relationship to prior work

Chen (arXiv:2610.00032v1, first public 2026-09-02) gives a variance-fixed sub-gamma variational scale for **spectrally positive** infinitely divisible laws, including one-sided positive compound-Poisson jumps. The current result concerns **symmetric two-sided** Lévy measures and identifies the sharp universal extremizer, the variance-profile-constrained extremizers, an exact interior optimizer, and a logarithmic Gaussian-variance dilution law. Chen and Wang (arXiv:2609.02590v1, first public 2026-09-02) give directional scales for arbitrary infinitely divisible laws and discuss a Skellam phase transition; this supplies a closely related general variational framework and already covers optimization of the individual Skellam family. The present claim does **not** assert discovery of the Skellam variational formula. It instead proves the global class envelope and rigidity/stability. Classical Bennett/Bernstein inequalities give relevant bounded-increment concentration background but do not by themselves state this sharp class-wide scale and equality profile.

## Limitations

No statement is made about non-symmetric jumps, jumps of unbounded magnitude, non-infinitely-divisible variables, or optimal constants for a different variance proxy. The tail probability bound resulting from the sub-gamma inequality need not be sharp as a tail bound. The optimizer for general \(\Gamma_{\alpha,\eta}\) is defined variationally; uniqueness of its optimizing argument is not asserted. The numerical digits are diagnostic, with a rigorous rational enclosure only for \(z_0\). Historical priority remains provisional, especially because the full text of the closely related Chen–Wang preprint was not available for complete inspection.

## References

1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1, first public 2026-09-02, https://arxiv.org/html/2610.00032v1.
2. Y. Chen and X. Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1, first public 2026-09-02, https://arxiv.org/abs/2609.02590 (abstract accessible through https://papers.cool/arxiv/2609.02590).
3. G. Bennett, *Probability Inequalities for the Sum of Independent Random Variables*, Journal of the American Statistical Association 57 (1962), 33–45; classical Bennett envelope, https://en.wikipedia.org/wiki/Bennett%27s_inequality.
4. C. Houdré, P. Marchal, and P. Reynaud-Bouret, *Concentration for norms of infinitely divisible vectors with independent components*, arXiv:math/0607019 (2006), https://arxiv.org/abs/math/0607019.
