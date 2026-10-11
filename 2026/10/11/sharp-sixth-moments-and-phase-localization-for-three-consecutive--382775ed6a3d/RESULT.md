# Sharp sixth moments and phase localization for three consecutive Fourier cosets

## Finding
Let \(G\) be a finite abelian group with normalized counting measure, \(H\le\widehat G\) a subgroup of order \(h\ge1\), and \(\chi\in\widehat G\) such that the coset \(\chi H\) has order \(r\ge3\) in \(\widehat G/H\). Put
\[
\Lambda=H\cup\chi H\cup\chi^2H,\qquad
\mathcal C_{G,\Lambda}=
\sup_{\substack{0\ne f\in L^2(G)\\\operatorname{supp}\widehat f\subseteq\Lambda}}
\frac{\|f\|_6^6}{\|f\|_2^6}.
\]
Set \(K=H^\perp\), and define the following positive numbers:
\[
\begin{aligned}
&t_3=t_4=1,\\
&t_5=\text{the unique positive root of }4t^5+10t^3+5t^2-20t-2=0,\\
&t_6=\tfrac12\sqrt{\sqrt{101}-5},\\
&t_r=\tfrac12\sqrt{\sqrt{105}-5}\quad(r\ge7).
\end{aligned}
\]
Define \(E_r(t)\) by
\[
\begin{array}{c|l}
r&E_r(t)\\\hline
3&t^6+30t^4+40t^3+90t^2+60t+22\\
4&t^6+30t^4+120t^2+32\\
5&t^6+30t^4+90t^2+12t+20\\
6&t^6+30t^4+90t^2+22\\
r\ge7&t^6+30t^4+90t^2+20.
\end{array}
\]
Then the exact sharp sixth-power constant is
\[
\boxed{\mathcal C_{G,\Lambda}=h^2\,\frac{E_r(t_r)}{(2+t_r^2)^3}.}
\]
In particular the five values of \(\mathcal C_{G,\Lambda}/h^2\) are
\[
9,\quad \frac{61}{9},\quad
\frac{E_5(t_5)}{(2+t_5^2)^3},\quad
\frac{404\sqrt{101}-1235}{529},\quad
\frac{35(\sqrt{105}-3)}{48},
\]
corresponding respectively to \(r=3,4,5,6,\ge7\). Their numerical values are approximately \(9,6.777778,5.681107,5.340548,5.284235\).

Every nonzero extremizer, and only those extremizers, is of the form
\[
\boxed{f(x_0+k)=\lambda\big(1+t_r\omega\chi(k)+\omega^2\chi(k)^2\big)
\ (k\in K),\qquad f(x)=0\ (x\notin x_0+K),}
\]
where \(x_0+K\) is any coset, \(\lambda\in\mathbb C\setminus\{0\}\), and \(|\omega|=1\). For \(3\le r\le6\), necessarily \(\omega^r=1\); for \(r\ge7\), every unimodular \(\omega\) is allowed. Thus, modulo complex scaling, the extremizers on each of the \(h\) cosets are \(r\) isolated points for \(r\le6\), and one circle for \(r\ge7\). Choosing a different representative of a coset merely relabels the phase parameter.

## Assumptions and scope
Fourier characters are complex unit-modulus homomorphisms; \(\chi^jH\) denotes multiplication of characters. Fourier and physical \(L^2\) norms use the probability Haar measure on \(G\), so \(\|f\|_2^2=\sum_{\gamma\in\widehat G}|\widehat f(\gamma)|^2\). The hypothesis \(r\ge3\) makes the three cosets distinct. All assertions hold for arbitrary finite abelian \(G\), not only cyclic groups, and no assumptions about prime factors are required.

## Proof
**1. Exact cyclic moment reduction.** Let \(\zeta\) be a primitive \(r\)-th root of unity. For \(P(z)=a+bz+cz^2\), orthogonality yields
\[
\frac1r\sum_{j=0}^{r-1}|P(\zeta^j)|^6
=\sum_{u=0}^{r-1}\left|\sum_{i+j+k\equiv u\ (\mathrm{mod}\ r)}a_i a_j a_k\right|^2,
\qquad(a_0,a_1,a_2)=(a,b,c).
\]
The triangle inequality shows that replacing \(a,b,c\) by their magnitudes does not decrease this moment. The coefficient vectors can therefore be assumed nonnegative for determining the maximum.

**2. A rigorous symmetric-magnitude reduction.** On \(\mathbb Z_r\), extend \(v=(|a|,|b|,|c|)\) by zero and reflect indices by \(J(i)=2-i\). Set \(w_i=\sqrt{(v_i^2+v_{Ji}^2)/2}\). For every cyclic shift \(s\), Cauchy--Schwarz gives
\[
\begin{aligned}
R_s(w)&=\tfrac12\sum_i\|(v_i,v_{Ji})\|_2\|(v_{i+s},v_{J(i+s)})\|_2\\
&\ge\tfrac12\sum_i(v_iv_{i+s}+v_{Ji}v_{J(i+s)})=R_s(v),
\end{aligned}
\]
where \(R_s(v)=\sum_i v_iv_{i+s}\). The zero shift is unchanged. Since
\[
\frac1r\sum_{j=0}^{r-1}|\sum_i v_i\zeta^{ij}|^6
=\sum_{s+t+u=0}R_s(v)R_t(v)R_u(v),
\]
and all \(R_s\) are nonnegative, symmetrization cannot decrease the moment. When \(|b|>0\) and \(|a|\ne|c|\), the term at shift \(1\) increases strictly, hence so does the sixth moment (the summand with shifts \(0,1,-1\) detects it). Thus an interior maximizer must have \(|a|=|c|>0\).

**3. A one-variable sharp maximization.** For \(a=c=x>0\), \(b=tx\), the cubic coefficients of \(P(z)^3\), ordered by degrees \(0,\ldots,6\), are
\[
(x^3,\ 3x^2b,\ 3x^3+3xb^2,\ 6x^2b+b^3,\ 3x^3+3xb^2,\ 3x^2b,\ x^3).
\]
Grouping these seven coefficients modulo \(r\) and squaring gives exactly \(x^6E_r(t)\). The squared coefficient norm is \(x^2(2+t^2)\), hence the ratio is \(E_r(t)/(2+t^2)^3\). Differentiating this ratio produces the numerator (with common positive denominator \((2+t^2)^4\))
\[
\begin{array}{c|l}
3&-12(t-1)(t+2)(2t+1)(2t^2+2t+5)\\
4&-48t(t-1)(t+1)(t^2+6)\\
5&-12(4t^5+10t^3+5t^2-20t-2)\\
6&-12t(4t^4+10t^2-19)\\
r\ge7&-24t(2t^4+5t^2-10).
\end{array}
\]
Each numerator is positive before, and negative after, its unique positive interior maximum. In the quintic case, the polynomial starts negative and has exactly one positive zero by Descartes' sign rule. The remaining roots follow from a quadratic equation in \(t^2\). Each maximum is strictly above the boundary values at \(t=0\) and \(t\to\infty\). This proves the stated constants and forces \(x>0\), \(t=t_r\).

**4. All phases.** With positive magnitudes, equality in the cubic-coefficient triangle inequality requires alignment of every contributing monomial in each residue class. The two monomials of degree \(2\) with distinct exponent multisets, \(a^2c\) and \(ab^2\), force
\[
2\arg b\equiv\arg a+\arg c\pmod{2\pi}.
\]
Thus, after scaling, the three coefficients have phases \(1,e^{i\theta},e^{2i\theta}\). For \(r\le6\), the degree \(0\) and degree \(r\) coefficients of \(P^3\) both occur and must align, forcing \(e^{ir\theta}=1\). For \(r\ge7\) no two degrees between \(0\) and \(6\) wrap modulo \(r\), so \(\theta\) is arbitrary. Conversely each listed phase choice attains all triangle bounds.

**5. Lifting to arbitrary groups and exact localization.** By duality \(\chi|_K\) has order exactly \(r\). Any function with Fourier support in \(\Lambda\) restricts on each coset \(C=x_0+K\) to a polynomial
\[
f(x_0+k)=A_C+B_C\chi(k)+C_C\chi(k)^2.
\]
There are \(h=|H|\) such cosets, and every choice of the triples is realized by the stated Fourier support. If \(s_C=|A_C|^2+|B_C|^2+|C_C|^2\), orthogonality gives
\[
\|f\|_2^2=\frac1h\sum_Cs_C,
\qquad
\|f\|_6^6\le\frac{K_r}{h}\sum_Cs_C^3
\le h^2K_r\|f\|_2^6,
\]
where \(K_r=E_r(t_r)/(2+t_r^2)^3\). The final inequality is equality only when at most one \(s_C\) is positive; the cyclic equality conditions on that coset give precisely the displayed family. Its Fourier support lies in \(\Lambda\) because \(\mathbf1_C\) has Fourier support in \(H\). This proves sharpness and exhaustiveness.

## Verification
The standalone program `artifacts/verify.py` checks the exact degree-six residue-class polynomials for orders \(3\) through \(15\), the five symbolic derivatives, a rational root isolation of the exceptional quintic, direct complex Fourier samples, concrete subgroup-coset lifts, and reflection autocorrelation inequalities. Run with `python artifacts/verify.py` from the package root; it requires Python 3 and SymPy. The general theorem is established by the analytic argument above, not by these finite samples.

## Relationship to prior work
Junge--Palazuelos--Parcet--Perrin study finite-cyclic even-moment hypercontractivity for length-weighted semigroups. Their finite-cyclic theorems concern the optimal **semigroup time**, not the sharp unweighted sixth moment of the three-coset frequency subspace. Nursultanov--Ruzhansky--Tikhonov give general Nikolskii inequalities on compact groups, which yield coarse support-based estimates without the torsion-dependent sharp constants or equality phases. The continuous-circle sharp sixth-moment value for the analytic quadratic is precisely the \(r\ge7\) branch, and is not presented as a new continuous result. The contribution here is the complete finite-torsion phase diagram for \(r=3,4,5,6\), plus its exact lifting and extremizer localization for three cosets in arbitrary finite abelian dual groups. No universal historical-priority claim is made.

## Limitations
Only a sixth moment and exactly three consecutive quotient-frequency cosets are treated. Orders \(r=1,2\) are excluded because the cosets are not distinct. The result does not provide sharp constants for four or more cosets, non-even norms, or general coefficient weights. An equivalent formula in older finite-grid sharp Nikolskii tables cannot be ruled out without an exhaustive historical bibliography.

## References
1. M. Junge, C. Palazuelos, J. Parcet and M. Perrin, *Hypercontractivity in group von Neumann algebras*, arXiv:1304.5789v1, publicly submitted 2013-04-21. Section 2.3 and Theorem A3 treat finite cyclic groups.
2. E. D. Nursultanov, M. V. Ruzhansky and S. Yu. Tikhonov, *Nikolskii inequality and functional classes on compact Lie groups*, arXiv:1507.07111v1, publicly submitted 2015-07-25. Section 2 discusses general support-based Nikolskii bounds.
