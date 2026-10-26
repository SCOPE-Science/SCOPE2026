# Full-order sharp bound for the third symmetric Toeplitz determinant of starlike mappings

## Finding

For each \(0\le\alpha<1\), every normalized analytic starlike function of order \(\alpha\),
\[h(\zeta)=\zeta+a_2\zeta^2+a_3\zeta^3+a_4\zeta^4+\cdots,\qquad \Re\!\left(\frac{\zeta h'(\zeta)}{h(\zeta)}\right)>\alpha,\]
satisfies the **sharp** symmetric Toeplitz determinant bound
\[\left|T_3(2)(h)\right|=\left|(a_2-a_4)(a_2^2+a_2a_4-2a_3^2)\right|\le\frac49(1-\alpha)^3(9-7\alpha+2\alpha^2)(21-22\alpha+8\alpha^2).\tag{1}\]
Equality holds if and only if
\[h(\zeta)=\frac{\zeta}{(1-i\zeta)^{2(1-\alpha)}}\qquad\text{or}\qquad h(\zeta)=\frac{\zeta}{(1+i\zeta)^{2(1-\alpha)}}.\tag{2}\]
In particular, the sharp formula previously established for \(0\le\alpha\le2/3\) continues unchanged through the entire remaining range \(2/3<\alpha<1\).

For a complex Banach space \(X\) with unit ball \(\mathbb B\), the same sharp upper bound holds for the directional coefficients of every radial mapping \(F(z)=z\,\varphi(z)\) of starlikeness order \(\alpha\), where \(\varphi(0)=1\). Precisely, for every unit \(v\in X\) and norm-one functional \(\ell_v\in X^*\) with \(\ell_v(v)=1\), put
\[A_j(v)=\frac{\ell_v(D^jF(0)(v,\ldots,v))}{j!},\qquad j=2,3,4.\]
Then inequality (1) holds with \(a_j=A_j(v)\). Its constant is optimal in every nonzero complex Banach space. This includes the normalized directional expression of Theorem 2.3 of Panja–Majumder–Banerjee.

## Assumptions and scope

The unit disk is \(\mathbb D=\{\zeta:|\zeta|<1\}\), derivatives are complex derivatives, and the third symmetric Toeplitz determinant is the determinant of the matrix
\[\begin{pmatrix}a_2&a_3&a_4\\ a_3&a_2&a_3\\a_4&a_3&a_2\end{pmatrix}.\]
The exponent in (2) is the analytic branch normalized to equal one at the origin. All inequalities are uniform in \(\alpha\in[0,1)\), and the endpoint \(\alpha=1\) is excluded. The Banach-space statement concerns radial maps and individual complex directions; it does not assert a sharp estimate for arbitrary nonradial maps or for unrelated multilinear expressions.

## Proof

Write \(s=1-\alpha\in(0,1]\). The positive-real-part condition has the standard Schwarz-function form
\[\frac{\zeta h'(\zeta)}{h(\zeta)}=1+\frac{2s\omega(\zeta)}{1-\omega(\zeta)},\qquad \omega(\zeta)=x\zeta+y\zeta^2+c\zeta^3+O(\zeta^4),\quad|\omega(\zeta)|<1.\tag{3}\]
Comparing coefficients of the logarithmic derivative gives
\[\begin{aligned}
a_2&=2sx,\\
a_3&=s\bigl(y+(1+2s)x^2\bigr),\\
a_4&=s\left[\frac23c+\left(\frac43+2s\right)xy+\left(\frac23+2s+\frac43s^2\right)x^3\right].
\end{aligned}\tag{4}\]
Set \(U=(a_2-a_4)/s\) and \(V=(a_2^2+a_2a_4-2a_3^2)/s^2\). Direct substitution yields
\[U=2x-\frac23c-\left(\frac43+2s\right)xy-\left(\frac23+2s+\frac43s^2\right)x^3,\tag{5}\]
\[V=4x^2+\frac43xc-2y^2-\left(\frac43+4s\right)x^2y-\left(\frac23+4s+\frac{16}3s^2\right)x^4.\tag{6}\]

**Schur coefficient constraints.** Set \(r=|x|\in[0,1]\). The first two Schur steps for \(\omega(\zeta)/\zeta\) give parameters \(b,d\) such that
\[y=(1-r^2)b,\qquad c=(1-r^2)\bigl(d-\overline{x}b^2\bigr),\qquad |b|=t\in[0,1],\quad|d|\le1-t^2.\tag{7}\]
The formulas hold at \(r=1\) by continuity (and there \(y=c=0\)). Hence
\[|y|\le(1-r^2)t,\qquad |c|\le(1-r^2)\bigl[1-(1-r)t^2\bigr].\tag{8}\]

**First factor.** Triangle inequalities in (5), using the weaker \(|c|\le1-r^2\), give
\[\begin{aligned}|U|\le R_1(s,r):={}&2r+\frac23(1-r^2)+\left(\frac43+2s\right)r(1-r^2)\\&+\left(\frac23+2s+\frac43s^2\right)r^3.\end{aligned}\]
A direct factorization is
\[\frac23(4+3s+2s^2)-R_1(s,r)=\frac23(1-r)\bigl[(1-r)(r+3)+3s+2s^2(r^2+r+1)\bigr]\ge0.\tag{9}\]
The inequality is strict for \(r<1\) because \(s>0\). Thus
\[|U|\le M_1(s):=\frac23(4+3s+2s^2).\tag{10}\]

**Second factor.** Equations (6)–(8) give
\[\begin{aligned}|V|\le Q(s,r,t):={}&4r^2+\frac23(1+6s+8s^2)r^4+\frac43(1+3s)r^2(1-r^2)t\\&+2(1-r^2)^2t^2+\frac43r(1-r^2)\bigl[1-(1-r)t^2\bigr].\end{aligned}\tag{11}\]
At \(s=0\), the polynomial \(t\mapsto Q(0,r,t)\) is convex: its quadratic coefficient is \(\frac23(1-r)^2(r+1)(r+3)\ge0\). Its endpoint values obey
\[Q(0,r,1)=2+\frac83r^2\le\frac{14}3,\qquad Q(0,r,1)-Q(0,r,0)=\frac23(1-r^2)(r^2-2r+3)\ge0.\tag{12}\]
Therefore \(Q(0,r,t)\le14/3\) for every \(0\le r,t\le1\). The remaining terms have the exact decomposition
\[Q(s,r,t)-Q(0,r,t)=4s\bigl[r^4+r^2(1-r^2)t\bigr]+\frac{16}3s^2r^4.\tag{13}\]
Since \(r^4+r^2(1-r^2)t\le r^2\le1\), we conclude
\[|V|\le\frac{14}3+4s+\frac{16}3s^2=:M_2(s)=\frac23(7+6s+8s^2).\tag{14}\]
As \(T_3(2)(h)=s^3 UV\), (10) and (14) yield
\[|T_3(2)(h)|\le s^3M_1(s)M_2(s)=\frac49s^3(4+3s+2s^2)(7+6s+8s^2),\]
which is (1).

**Sharpness and equality.** For \(\omega(\zeta)=i\zeta\), coefficient comparison gives \(x=i\), \(y=c=0\), and (5)–(6) yield exactly \(U=iM_1(s)\), \(V=-M_2(s)\). The opposite sign \(\omega=-i\zeta\) gives conjugate equality. Conversely, equality in (1) implies equality in (10). The strict inequality in (9) forces \(r=1\), hence Schwarz's lemma forces \(\omega(\zeta)=x\zeta\) with \(|x|=1\). Equation (5) then gives \(|U|=|2x-(\frac23+2s+\frac43s^2)x^3|\le M_1(s)\), with equality only when \(x^2=-1\). Integrating (3) gives precisely the two functions in (2).

**Banach-ball transfer.** Let \(F(z)=z\varphi(z)\) satisfy the stated starlikeness definition. For each unit vector \(v\), the scalar slice \(h_v(\zeta)=\ell_v(F(\zeta v))=\zeta\varphi(\zeta v)\) has \(\Re(\zeta h_v'(\zeta)/h_v(\zeta))>\alpha\): the radial inverse-derivative identity is
\[[DF(z)]^{-1}F(z)=\frac{z\varphi(z)}{\varphi(z)+D\varphi(z)z},\]
so its positive-real-part condition reduces along each ray to that of \(h_v\). Its coefficients are precisely \(A_j(v)\). Apply (1) to \(h_v\). To see sharpness in every nonzero \(X\), choose unit \(v\) and norm-one \(\ell\) with \(\ell(v)=1\), and take \(F(z)=z(1-i\ell(z))^{-2s}\). Its radial logarithmic derivative equals \(1+2si\ell(z)/(1-i\ell(z))\), whose real part exceeds \(\alpha\), and its \(v\)-slice is the first function in (2). Therefore the bound is sharp.

## Verification

The accompanying `CHECKER.py` uses exact symbolic arithmetic to check the coefficient identities (4)–(6), the factorizations (9), (12), (13), the convexity coefficient in (11), and the extremal values. The remaining inferences are elementary positivity on the explicitly specified cube \(0\le r,t\le1\), \(0<s\le1\), together with Schwarz's lemma and the two Schur steps (7). The computation is a certificate for the identities, **not** a replacement for the analytic argument.

## Relationship to prior work

Panja, Majumder and Banerjee (arXiv:2610.15497v1, first public 2026-10-11) prove precisely bound (1), under the same directional determinant normalization, only for \(0\le\alpha\le2/3\) in their Theorems 2.3 and 2.4 (and state that range explicitly in the abstract and Remark 2.1). The present argument supplies the missing upper third of the order interval without modifying the sharp coefficient. Giri's arXiv:2606.17778 treats related third-order Toeplitz problems for subclasses of starlike mappings, including the order-zero constant. Earlier work by Ali, Thomas and Vasudevarao supplies the classical order-zero constant \(84\). The generalized paper arXiv:2601.03039 treats higher-vanishing subclasses and other determinants; those restrictions do not imply the full-order statement here.

## Limitations

This concerns radial starlike maps in Banach balls and the third **symmetric non-Hermitian** Toeplitz determinant. It does not prove a different sharp statement for general nonradial mappings, all Toeplitz orders, or Hermitian Toeplitz determinants. While the inspected relevant statements do not contain the range \(2/3<\alpha<1\), an unindexed independent proof or a more general theorem with this bound as a corollary remains a possible priority risk. No independent audit has been performed.

## References

1. S. Panja, S. Majumder and A. Banerjee, *Toeplitz determinants for starlike mappings of order α in several complex variables*, arXiv:2610.15497v1 (first submitted 2026-10-11), Theorems 2.3–2.4 and Remark 2.1. https://arxiv.org/html/2610.15497v1
2. S. Giri, *Third-Order Toeplitz Determinant for a Subclass of Starlike Mappings in Higher Dimensions*, arXiv:2606.17778v1 (2026-06-16). https://arxiv.org/abs/2606.17778
3. S. Giri and S. Sivaprasad Kumar, *Generalized Toeplitz determinants for Starlike Mappings in Several Complex Variables*, arXiv:2601.03039v1 (2026-01-06). https://arxiv.org/abs/2601.03039
4. M. F. Ali, D. K. Thomas and A. Vasudevarao, *Toeplitz determinants whose elements are the coefficients of analytic and univalent functions*, arXiv:1704.00657 (2017). https://arxiv.org/abs/1704.00657
