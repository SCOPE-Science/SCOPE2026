# A parity bifurcation in sharp sixth moments of two \(\mathrm{SU}(2)\) characters

## Finding
Let \(\chi_j\) denote the ordinary (undivided) trace character of the \((j+1)\)-dimensional irreducible representation of \(\mathrm{SU}(2)\). For every integer \(n\ge2\), set
\[
K_n=\max_{|a|^2+|b|^2=1}\int_{\mathrm{SU}(2)}|a\chi_1(g)+b\chi_n(g)|^6\,dg,
\qquad S_n=\frac{n^3+3n^2+4n+2}{2}.
\]
Haar measure is probability-normalized, so \(\|\chi_j\|_2=1\) and the coefficient constraint is exactly the squared \(L^2\) norm.

There is a sharp parity bifurcation, with every complex equality case classified:

1. **Even \(n\ge6\):** \(K_n=S_n\), and the only nonzero equality pairs in the homogeneous inequality \(\int|a\chi_1+b\chi_n|^6\le K_n(|a|^2+|b|^2)^3\) are \((a,b)=(0,\lambda)\), \(\lambda\ne0\).
2. **Even \(n\in\{2,4\}\):** let \(q_n\) be the unique positive root of
   \[
   25+2(20n-25)q+(S_n-20n-5)q^2=0.
   \]
   Then
   \[
   K_n=\frac{5+90q_n+(60n+15)q_n^2+S_nq_n^3}{(1+q_n)^3}>S_n,
   \]
   and every nonzero equality pair is \((a,b)=\lambda(1,\pm\sqrt{q_n})\).
3. **Odd \(n\ge3\):** put \(c_3=24\), \(c_5=6\), and \(c_n=0\) for odd \(n\ge7\). Define
   \[
   Q_n(t)=5t^6+c_nt^5+90t^4+160t^3+(60n+15)t^2
   +\frac{15}{2}(n+1)^2t+S_n.
   \]
   The polynomial \((1+t^2)Q_n'(t)-6tQ_n(t)\) has exactly one positive zero \(t_n\). Then
   \[
   K_n=\frac{Q_n(t_n)}{(1+t_n^2)^3}>S_n,
   \]
   and all nonzero equality pairs are precisely \((a,b)=\lambda(t_n,1)\), \(\lambda\ne0\). In particular the lower representation has nonzero optimal weight for every odd \(n\), however large. As \(n\) tends to infinity through odd values,
   \[
   t_n=\frac{5}{2n}+O(n^{-2}),\qquad K_n-S_n=\frac{75}{8}n+O(1).
   \]

Thus the high-weight representation entirely excludes the defining representation at the sixth moment for every even \(n\ge6\), but never does so for odd \(n\). The exceptional even cases, strict positive odd mixture, sharp constants, phase rigidity, and asymptotic residual gain belong to one all-weight statement.

## Assumptions and scope
The group is the compact simply connected \(\mathrm{SU}(2)\), not its finite subgroups. Irreducible characters are real-valued and orthonormal for Haar probability, indexed by highest weight \(j=0,1,2,\ldots\), with \(\chi_1\) the two-dimensional fundamental character. For a diagonal element with eigenvalues \(e^{\pm i\theta}\), \(\chi_j=\sin((j+1)\theta)/\sin\theta\), with endpoint values taken by continuity. Coefficients \(a,b\) are arbitrary complex numbers; the equality descriptions include all nonzero common complex multiples. Only sixth moments are claimed, for exactly two modes \(\chi_1,\chi_n\) and \(n\ge2\).

## Proof
**1. Exact mixed sixth moments.** The Clebsch–Gordan product identity reads
\[
\chi_u\chi_v=\sum_{k=|u-v|,\,|u-v|+2,\ldots,u+v}\chi_k.
\]
The integral of a character product is the multiplicity of the trivial representation. Iterating gives
\[
\chi_n^2=\sum_{j=0}^{n}\chi_{2j},
\qquad
\chi_1^3=2\chi_1+\chi_3,
\qquad
\chi_1^4=2\chi_0+3\chi_2+\chi_4,
\qquad
\chi_1^5=5\chi_1+4\chi_3+\chi_5.
\]
More explicitly, the multiplicity of \(\chi_k\) in \(\chi_n^3\) is zero unless \(0\le k\le3n\) and \(k\equiv n\pmod2\), and otherwise equals
\[
m_{n,k}=\begin{cases}k+1,&k\le n,\\ (3n-k)/2+1,&n<k\le3n.\end{cases}
\]
This follows by counting those \(j\in\{0,\ldots,n\}\) for which \(\chi_k\) occurs in \(\chi_{2j}\chi_n\). Squaring the decomposition gives
\[
\int\chi_n^6\,dg=\sum_{k}m_{n,k}^2=S_n.
\]
In detail, the sum is \(\sum_{j=0}^{n/2}(2j+1)^2+\sum_{j=1}^{n}j^2\) if \(n\) is even, and \(\sum_{j=1}^{(n+1)/2}(2j)^2+\sum_{j=1}^{n}j^2\) if \(n\) is odd; both equal the stated cubic.

The remaining mixed integrals follow from the same products:
\[
\begin{array}{c|rrrrrrr}
j&0&1&2&3&4&5&6\\\hline
\displaystyle {6\choose j}\int\chi_1^{6-j}\chi_n^j\,dg
&5&c_n&90&160\mathbf1_{n\text{ odd}}&60n+15&\frac{15}{2}(n+1)^2\mathbf1_{n\text{ odd}}&S_n
\end{array}
\]
where \(c_3=24\), \(c_5=6\), and \(c_n=0\) otherwise. For example, \(\int\chi_1^4\chi_n^2=2+3+1=6\); \(\int\chi_1^2\chi_n^4=(n+1)+3n=4n+1\). For odd \(n\), the multiplicities of \(\chi_1,\chi_3\) in \(\chi_n^3\) are respectively \(2,4\), hence \(\int\chi_1^3\chi_n^3=8\). Also \(\chi_1\chi_n^2=2\sum_{j=0}^{n-1}\chi_{2j+1}+\chi_{2n+1}\). Pairing this with the explicit \(m_{n,k}\) yields \(\int\chi_1\chi_n^5=\frac54(n+1)^2\) for odd \(n\); it vanishes for even \(n\) by parity. These identities establish the entire table, including the \(n=3,5\) exceptions.

**2. Complex phase alignment.** Expanding \((a\chi_1+b\chi_n)^3(\bar a\chi_1+\bar b\chi_n)^3\) shows that each scalar product multiplying a monomial in \(a,b,\bar a,\bar b\) is a nonnegative invariant-tensor multiplicity. Taking absolute values term by term therefore gives
\[
\int|a\chi_1+b\chi_n|^6\,dg
\le \int\bigl(|a|\chi_1+|b|\chi_n\bigr)^6\,dg,
\]
where the right side denotes the *algebraic sixth power*, not the sixth power of a positive function. Equality holds for aligned coefficients. If both magnitudes are nonzero, a positive \(\int\chi_1^4\chi_n^2=6\) term forces the relative complex phase to be \(0\) or \(\pi\) for even \(n\); for odd \(n\), the positive \(\int\chi_1^3\chi_n^3=8\) terms also force relative phase \(0\). (Termwise triangle equality implies these restrictions.) Thus the magnitude optimization is exact, not merely an upper estimate.

**3. Even weights.** Put \(p=|b|^2/(|a|^2+|b|^2)\). The phase-aligned normalized sixth moment is
\[
R_n(p)=5(1-p)^3+90p(1-p)^2+(60n+15)p^2(1-p)+S_np^3.
\]
Its derivative has the strictly useful Bernstein form
\[
\frac{R'_n(p)}3=25(1-p)^2+2(20n-25)p(1-p)+(S_n-20n-5)p^2.
\]
For even \(n\ge6\), all three coefficients are positive; hence \(R_n\) is strictly increasing on \([0,1]\) and only \(p=1\) is optimal. For \(n=2,4\), the last coefficient is negative, the first two positive; after \(q=p/(1-p)\), the derivative changes sign exactly once at the unique positive zero specified in the finding. The maximum is therefore strict, interior, and unique in \(p\). Phase rigidity yields exactly the two indicated signs.

**4. Odd weights.** Put \(t=|a|/|b|\) whenever \(b\ne0\). The phase-aligned quotient equals \(Q_n(t)/(1+t^2)^3\). Its derivative has numerator
\[
\begin{aligned}
H_n(t)={}&-c_nt^6-150t^5+(5c_n-480)t^4+(300-240n)t^3\\
&-\tfrac{15}{2}(5n^2+10n-59)t^2\\
&-3(n^3+3n^2-36n-8)t+\tfrac{15}{2}(n+1)^2.
\end{aligned}
\]
For all odd \(n\ge3\), the coefficients of powers at least \(t^2\) are strictly negative, the constant term is positive, and the linear coefficient is positive only at \(n=3\). The ordered list of nonzero coefficients therefore changes sign exactly once. Since \(H_n(0)>0\) and \(H_n(t)<0\) for all sufficiently large positive \(t\), Descartes' rule and continuity give one and only one positive root. The quotient first increases and then decreases, so this root is the unique global maximum on \([0,\infty]\). Its value exceeds both endpoints, and relative phase alignment is compulsory.

For the odd-weight asymptotic, substitute \(t=c/n\) into the explicit \(H_n(t)\). Uniformly for \(c\) in compact sets,
\[
n^{-2}H_n(c/n)=\tfrac{15}{2}-3c+O(n^{-1}).
\]
Uniqueness and the sign change give \(nt_n=\frac52+O(n^{-1})\). Expanding the quotient at this root gives \(K_n-S_n=\frac{75}{8}n+O(1)\). This completes all claimed cases and equality classifications.

## Verification
The complete standalone reproducibility program is `checker.py` and its recorded execution is `checker_output.txt`. It independently computes invariant multiplicities by repeated Clebsch–Gordan convolution (not by calling the formulas under test), compares all seven exact mixed-moment coefficients for \(2\le n\le66\), independently integrates the equivalent Chebyshev polynomials against semicircle moments for \(2\le n\le19\), expands complex sixth moments, tests phase dominance and the derived inequalities, and checks the symbolic derivative-sign structure and asymptotic scale. Its recorded execution passes 4,724 assertions. These finite calculations are diagnostic; the universal all-weight assertions are proved above by exact tensor-product multiplicities and polynomial signs.

## Relationship to prior work
Clebsch–Gordan decomposition and central-character orthogonality are classical; Crampé, Poulain d'Andecy and Vinet (2019) analyze centralizers and tensor couplings, including the decomposition underlying the present calculation. Grow and Myers (2020) give the standard normalized Haar and character formulas in their study of Fourier-series convergence on \(\mathrm{SU}(2)\). Neither work states the sharp sixth-power norm of the two-character packet or its all-weight optimizer bifurcation. Fourth-moment character-packet classifications and general finite-abelian-character inequalities do not determine these sixth-moment optimization parameters. The claimed addition is the combined exact mixed sixth moments, global coefficient optimization for every weight, full complex phase rigidity, and asymptotic odd-weight residual gain, not the Clebsch–Gordan rule itself.

## Limitations
Only the two-dimensional central Fourier subspace spanned by \(\chi_1\) and \(\chi_n\) is treated; no assertion is made for arbitrary multi-character packets, noncentral matrix coefficients, or even moments other than six. The constants are defined algebraically by unique positive roots rather than uniform radical expressions. The proof is self-contained subject to standard compact-group representation theory. Search and source comparison do not establish exhaustive bibliographic priority; an equivalent result in unindexed or inaccessible specialized literature remains possible. Independent validation has not been performed.

## References
1. N. Crampé, L. Poulain d'Andecy, and L. Vinet, *Temperley–Lieb, Brauer and Racah algebras and other centralizers of su(2)*, arXiv:1905.06346 (first public version 2019-05-15). https://arxiv.org/abs/1905.06346
2. D. Grow and D. Myers, *Almost everywhere convergence of Fourier series on SU(2): the case of Hölder continuous functions*, arXiv:2005.11245 (first public version 2020-05-22). https://arxiv.org/abs/2005.11245
