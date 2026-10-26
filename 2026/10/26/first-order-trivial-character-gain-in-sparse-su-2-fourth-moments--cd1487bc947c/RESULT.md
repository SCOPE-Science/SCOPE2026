# First-order trivial-character gain in sparse \(SU(2)\) fourth moments

## Finding
For each integer \(n\ge1\), let \(\chi_j\) be the ordinary (unnormalized trace) character of the irreducible \((j+1)\)-dimensional representation of \(SU(2)\), and normalize Haar measure to have total mass one. Define the **two-mode** and **anchored three-mode** sharp fourth powers by
\[
B_n=\max_{|b|^2+|c|^2=1}\|b\chi_n+c\chi_{2n}\|_{L^4(SU(2))}^4,
\qquad
M_n=\max_{|a|^2+|b|^2+|c|^2=1}
\|a\chi_0+b\chi_n+c\chi_{2n}\|_{L^4(SU(2))}^4.
\]
The following strict improvement holds for **every** \(n\ge1\): \(M_n>B_n\). More precisely, as \(n\to\infty\) along either parity class,
\[
\boxed{M_n-B_n=\begin{cases}
\dfrac{100}{63n}+O(n^{-2}),&n\text{ odd},\\[3pt]
\dfrac{333+180\sqrt3}{169n}+O(n^{-2}),&n\text{ even}.
\end{cases}}
\]
For **every** normalized maximizing coefficient triple \((a_n,b_n,c_n)\), the moduli have the following limits:
\[
\begin{array}{c|c|c|c}
 &\lim n|a_n|&\lim |b_n|^2&\lim |c_n|^2\\ \hline
 n\text{ odd}&\dfrac{5\sqrt6}{21}&\dfrac13&\dfrac23\\[5pt]
 n\text{ even}&\sqrt{\dfrac{15+6\sqrt3}{52}}&\dfrac{8-2\sqrt3}{13}&\dfrac{5+2\sqrt3}{13}
\end{array}
\]
In fact \(|a_n|=\kappa_{\mathrm{parity}(n)}/n+O(n^{-2})\) and the displayed higher-mode squared moduli are each their stated limit plus \(O(n^{-1})\). The estimates are uniform within each of the two parity subsequences.

## Assumptions and scope
Characters are indexed by nonnegative **highest weights**, not by dimensions; \(\chi_0=1\). The orthonormality convention is \(\int\chi_j\overline{\chi_k}\,dg=\delta_{jk}\), and the coefficient-energy constraint therefore gives \(L^2\)-norm one. Coefficients may be arbitrary complex numbers, including zeros. The theorem concerns central Fourier polynomials on the fixed group \(SU(2)\) as their highest weight \(n\) increases. It does not assert an exact closed formula for \(M_n\) at each finite \(n\), nor complete phase classification of finite-weight extremizers.

## Proof
**1. Exact reduction from complex coefficients.** The Clebsch–Gordan character rule is
\[
\chi_r\chi_s=\sum_{j=|r-s|,\,j\equiv r+s\ (\mathrm{mod}\ 2)}^{r+s}\chi_j.
\]
This follows directly from \(\chi_j(\theta)=\sin((j+1)\theta)/\sin\theta\). On expanding the square of a character packet and using orthonormality, \(\|\sum_u\alpha_u\chi_u\|_4^4\) is the sum over \(j\) of the squared moduli of sums of products \(\alpha_u\alpha_v\) with **nonnegative integer** fusion coefficients. By the triangle inequality, replacing all coefficients by their absolute values can only increase the fourth moment; nonnegative real coefficients attain this upper bound. Hence the complex optimization is exactly the nonnegative-real optimization, without a phase assumption.

Set \(a,b,c\ge0\). Direct use of the character rule gives the **exact** homogeneous fourth-power polynomial
\[
\begin{split}
F_n(a,b,c)={}&a^4+6a^2(b^2+c^2)+12ab^2c+4ac^3\\
&+(n+1)b^4+6(n+1)b^2c^2+(2n+1)c^4\\
&+\mathbf{1}_{2\mid n}\left(4ab^3+12abc^2+(2n+4)b^3c+4(n+1)bc^3\right).
\end{split}
\]
For example, the terms \(b^3c\) and \(bc^3\) occur only for even \(n\): the two relevant tensor-product intervals then have the same parity. Their respective character-integral multiplicities are \(n/2+1\) and \(n+1\). Likewise \(\int\chi_n^2\chi_{2n}=1\) and \(\int\chi_{2n}^3=1\), yielding the \(12ab^2c\) and \(4ac^3\) terms. These checks, together with \(\int\chi_n^4=n+1\), \(\int\chi_n^2\chi_{2n}^2=n+1\), and \(\int\chi_{2n}^4=2n+1\), account for every monomial. No numerical experiment is used to infer this identity.

**2. Separate the vanishing low mode.** For \(a\in[0,1]\), set \(q=\sqrt{1-a^2}\) and write \(b=qx\), \(c=qy\), with \(x,y\ge0\) and \(x^2+y^2=1\). For \(p=\mathrm{odd}\), define
\[
f_p=x^4+6x^2y^2+2y^4,\quad
 g_p=x^4+6x^2y^2+y^4,\quad R_p=y(3x^2+y^2).
\]
For \(p=\mathrm{even}\), define
\[
f_p=x^4+2x^3y+6x^2y^2+4xy^3+2y^4,\quad
 g_p=(x+y)^4,\quad R_p=(x+y)^3.
\]
The exact polynomial becomes
\[
\Phi_n(a,x,y)=a^4+6a^2(1-a^2)
+4a(1-a^2)^{3/2}R_p(x,y)
+(1-a^2)^2\bigl(nf_p(x,y)+g_p(x,y)\bigr).
\]
Here \(B_n=\max_{x^2+y^2=1,\,x,y\ge0}(nf_p+g_p)\) and \(M_n=\max\Phi_n\).

**3. Unique interior maxima of the leading forms.** In odd parity, writing \(s=x^2\) gives \(f_{\rm odd}=2+2s-3s^2\), with its unique strict maximum \(f_{\rm odd,*}=7/3\) at \((x^2,y^2)=(1/3,2/3)\). Moreover the finite-weight two-mode maximum is achieved at \(s_n=(n+2)/(3n+4)\), with \(B_n=(n+1)(7n+8)/(3n+4)\).

In even parity set \(t=x/y\) for \(y>0\). Then
\[
f_{\rm even}(t)=\frac{t^4+2t^3+6t^2+4t+2}{(1+t^2)^2},\qquad
f_{\rm even}'(t)=-\frac{2(t+1)^2(t^2+2t-2)}{(1+t^2)^3}.
\]
The unique nonnegative maximizer is \(t_*=\sqrt3-1\), and its strict nondegenerate maximum equals \(f_{\rm even,*}=(30+12\sqrt3)/13\). At this point \(x_*^2=(8-2\sqrt3)/13\), \(y_*^2=(5+2\sqrt3)/13\). Consequently, for either parity, the leading form has one nondegenerate maximum in the open quarter circle.

**4. Quantitative perturbation lemma and proof of the limits.** Let \(v\) be an angular coordinate on the compact quarter circle and suppose smooth \(f,g,R\) have a unique nondegenerate interior maximizer \(v_*\) of \(f\), with \(f(v_*)>0\) and \(R(v_*)>0\). The functions above satisfy these hypotheses. Compactness and comparison with \((a,v)=(0,v_*)\) first imply that every maximizer of \(\Phi_n\) has \(a=o(1)\), \(v\to v_*\): after division by \(n\), the leading term is \((1-a^2)^2f(v)\), whose unique maximum occurs at \((0,v_*)\). The derivative in \(a\) at \(0\) equals \(4R(v)>0\) near \(v_*\), so for all sufficiently large \(n\) every maximum has \(a>0\), and it is interior in both variables. The stationarity equation in \(a\) reads
\[
4R(v)-4nf(v)a+O\bigl(a+na^3\bigr)=0
\]
uniformly near \(v_*\). Since \(a=o(1)\) and \(f(v_*)>0\), it first gives \(a=O(n^{-1})\). The angular stationarity equation is \(nf'(v)+O(1)=0\); nondegeneracy then gives \(v-v_*=O(n^{-1})\). Substitution yields
\[
a=\frac{R(v_*)}{n f(v_*)}+O(n^{-2}).
\]
For \(v\) near \(v_*\), maximizing in \(a\) uniformly gives the scalar expansion
\[
\max_{a\ge0}\Phi_n(a,v)=nf(v)+g(v)+\frac{2R(v)^2}{nf(v)}+O(n^{-2}).
\]
The unperturbed maximizer of \(nf+g\) and the maximizer of the perturbed expression both satisfy \(v=v_*+O(n^{-1})\). Sandwiching the difference of their two maximal values between evaluations at these maximizing points proves
\[
M_n-B_n=\frac{2R(v_*)^2}{nf(v_*)}+O(n^{-2}).
\]
This argument is uniform over **all** maximizing triples; it makes no uniqueness assertion about their phases.

**5. Exact constants, and the strict finite-weight gain.** In odd parity,
\[
R_{\rm odd,*}=\frac{5\sqrt6}{9},\qquad
\frac{R_{\rm odd,*}}{f_{\rm odd,*}}=\frac{5\sqrt6}{21},\qquad
\frac{2R_{\rm odd,*}^2}{f_{\rm odd,*}}=\frac{100}{63}.
\]
In even parity, the identity \(f_{\rm even,*}=2(x_*+y_*)^2\) gives
\[
\frac{R_{\rm even,*}}{f_{\rm even,*}}=\frac{x_*+y_*}{2}
=\sqrt{\frac{15+6\sqrt3}{52}},\qquad
\frac{2R_{\rm even,*}^2}{f_{\rm even,*}}=(x_*+y_*)^4
=\frac{333+180\sqrt3}{169}.
\]
The stated limits and errors follow. To show strict gain for every finite \(n\ge1\), the maximizing pair \((b,c)\) can be chosen with \(b,c>0\). In odd parity this follows from the displayed exact \(s_n\); in even parity the sample \(b=c=1/\sqrt2\) already has fourth power \((15/4)n+4\), strictly larger than either boundary value \(n+1\) or \(2n+1\). At any such two-mode maximizer the right derivative of \(\Phi_n(a,x,y)\) at \(a=0\) is \(4R_p(x,y)>0\), so admitting a sufficiently small positive trivial-character coefficient strictly improves the sharp norm.

## Verification
The included standalone checker independently builds every fourth-moment coefficient from the fusion rule for \(1\le n\le60\) in exact symbolic arithmetic, verifies both algebraic limiting constants, and compares a separate numerical optimization at 14 representative odd/even indices from 9 through 800. Twelve class-angle Haar quadratures independently check genuinely complex-coefficient fourth moments. The finite experiments corroborate the polynomial and limit computations; only the displayed analytical argument establishes the all-weight and asymptotic statements. Run \(\texttt{python3 verify\_sparse\_anchor.py}\) with Python, SymPy, and SciPy available.

## Relationship to prior work
Character fusion, orthonormality, and general nonabelian Fourier norm inequalities are classical. Akylzhanov–Liflyand–Ruzhansky (2019) examine Fourier re-expansion and summability on compact Lie groups, including \(SU(2)\); Ellis–Kindler–Lifshitz–Minzer (2024) study hypercontractivity and product mixing for compact Lie groups. Those regimes do not state the sharp sensitivity of the finite central packet \(\{\chi_0,\chi_n,\chi_{2n}\}\) to the added trivial mode. Sharp two-character results concern \(B_n\) rather than \(M_n-B_n\); general high-weight fixed-offset asymptotics do not directly cover one pinned low representation with the other two weights diverging. The new result is the exact first nonzero gain and the concomitant optimal low-mode scaling, not the elementary Clebsch–Gordan rule itself.

## Limitations
The theorem gives a strict inequality for every \(n\) but only asymptotic coefficients for the three-mode sharp constant. It does not claim a complete finite-\(n\) optimizer phase classification or an exact finite-\(n\) formula for \(M_n\). The source comparison is best-knowledge, not a mathematical proof of priority; equivalent specialized computations may exist outside the inspected literature.

## References
1. R. Akylzhanov, E. Liflyand, M. Ruzhansky, *Re-expansions on compact Lie groups*, arXiv:1902.06077 (first public version 2019-02-16).
2. D. Ellis, G. Kindler, N. Lifshitz, D. Minzer, *Product Mixing in Compact Lie Groups*, arXiv:2401.15456 (first public version 2024-01-27).
