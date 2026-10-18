# The four-point nonordinary locus of a balanced cyclic-quintic genus-four family over characteristic eleven

## Finding

Let \(k=\overline{\mathbf F}_{11}\). For each \(t\in k\setminus\{0,1\}\), let \(C_t\) denote the smooth projective normalization of the Kummer cover
\[
 y^5=x(x-1)^2(x-t)^3.
\]
Its genus is four. Set
\[
 A(t)=t^2-5t-4,\qquad B(t)=t^2+4t-3\in\mathbf F_{11}[t].
\]
Then the Jacobian's \(11\)-rank \(f_{11}\) and \(a\)-number satisfy, for *every* admissible geometric parameter,
\[
 (f_{11}(\operatorname{Jac}(C_t)),a(\operatorname{Jac}(C_t)))=
 \begin{cases}(2,2),&A(t)B(t)=0,\\(4,0),&A(t)B(t)\ne0.\end{cases}
\]
Both quadratics are irreducible over \(\mathbf F_{11}\) and have no common root. Thus precisely four distinct geometric parameter points are nonordinary; all four lie in \(\mathbf F_{11^2}\setminus\mathbf F_{11}\). In particular no member has rank zero, one, or three; all other members are ordinary. These counts concern parameters of this marked cyclic-cover presentation, not unrestricted geometric isomorphism classes or twists.

## Assumptions and scope

We work in characteristic \(11\), with a fixed degree-five cyclic map \(C_t\to\mathbf P^1_k\) given by the rational function \(x\). For \(t\ne0,1\), the branch points are \(0,1,t,\infty\) and the local exponents, modulo five, are respectively \(1,2,3,4\). The cover is tame, connected, and smooth after normalization. Riemann–Hurwitz gives
\[
2g(C_t)-2=5(-2)+4(5-1)=6,
\]
so \(g=4\). The \(11\)-rank means the dimension of \(\operatorname{Jac}(C_t)[11](k)\) over \(\mathbf F_{11}\); the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_{11},\operatorname{Jac}(C_t))\).

## Proof

Write \(f(x)=x(x-1)^2(x-t)^3\). A basis of regular differentials is
\[
\begin{aligned}
\omega_1&=\frac{dx}{y},&
\omega_2&=\frac{(x-t)dx}{y^2},\\
\omega_3&=\frac{(x-1)(x-t)dx}{y^3},&
\omega_4&=\frac{(x-1)(x-t)^2dx}{y^4}.
\end{aligned}
\]
Indeed, at a branch point of local exponent \(e\in\{1,2,3\}\), the valuations are \(\operatorname{ord}(dx)=4\), \(\operatorname{ord}(y)=e\), and the corresponding vanishing factor has order five. The displayed numerators make each differential regular at the three finite branch points. At infinity \(\operatorname{ord}(x)=-5\), \(\operatorname{ord}(y)=-6\), \(\operatorname{ord}(dx)=-6\), and each numerator has degree \(j-1\) for \(\omega_j\), so its valuation there is \(1\). Each differential is therefore holomorphic. There are four, independently distinguished by the cyclic characters, hence they form a basis by the genus calculation.

Let \(h_1=1\), \(h_2=x-t\), \(h_3=(x-1)(x-t)\), \(h_4=(x-1)(x-t)^2\). Since \(11=2\cdot5+1\), the Cartier operator on \(\omega_j=h_jdx/y^j\) can be computed using
\[
\omega_j=\frac{h_j f^{2j}\,dx}{y^{11j}}.
\]
For a polynomial \(G(x)=\sum_m g_m x^m\), the Cartier extraction picks the coefficients \(g_{11r+10}^{1/11}x^r\,dx\). Exact expansion in \(\mathbf F_{11}[t,x]\) gives, with \(r=j-1\),
\[
\sum_{u=0}^{r}[x^{11u+10}](h_j f^{2j})\,x^{11u}
      =H_j(t)h_j(x)^{11},
\]
where
\[
 (H_1,H_2,H_3,H_4)
 =\bigl(4A(t),-5B(t),-5t^4B(t),4t^2A(t)\bigr).
\]
Therefore the Cartier operator is diagonal in this basis, with entries \(H_j(t)^{1/11}\). Its rank and stable semilinear rank equal the number of nonzero \(H_j(t)\): a nonzero diagonal entry stays nonzero under every Frobenius twist. This stable rank is the Jacobian's \(11\)-rank, and its rank deficiency is the \(a\)-number.

Because \(t\ne0\), the first and fourth diagonal entries vanish together exactly at roots of \(A\); the second and third vanish together exactly at roots of \(B\). The discriminants are \(8\) for \(A\) and \(6\) for \(B\), both nonsquares in \(\mathbf F_{11}\); the distinct monic irreducible quadratics are coprime. Each has two distinct roots in \(\mathbf F_{11^2}\setminus\mathbf F_{11}\), and none is an excluded parameter. At each root exactly two entries vanish, giving \((f_{11},a)=(2,2)\); elsewhere all four entries are nonzero, giving \((4,0)\). This proves the complete classification.

## Verification

The included standalone program `verify.py` requires Python 3 and no external libraries. Run `python3 verify.py` from the same directory. It constructs exact bivariate polynomials over \(\mathbf F_{11}\), checks every Cartier-extracted coefficient for each of the four basis differentials against the claimed \(H_j h_j^{11}\), verifies the two quadratic discriminants, checks that they are distinct and irreducible, and verifies the polynomial reciprocity identity \(A(t)=-\frac13 t^2 B(1/t)\). It prints `VERIFICATION_OK` on success. The polynomial identities are universal over \(\mathbf F_{11}\), not numerical samples of finitely many parameters. Valuations, the genus calculation, and the conceptual link between stable Cartier rank and \(p\)-rank are proved above, rather than inferred from program output.

## Relationship to prior work

Cavalieri and Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891, study general one-parameter families of cyclic covers branched at four points and give mass formulas for nonordinary curves. Their general mass theorem applies to this broad branch setting but does not specify these two quadratic equations or the exact \(11\)-rank and \(a\)-number at every parameter. Li, Mantovan, Pries, and Tang, *Newton Polygons Arising for Special Families of Cyclic Covers of the Projective Line*, arXiv:1805.06914, analyze the twenty special cyclic-cover families arising in Moonen's setting. The present balanced branch exponents \((1,2,3,4)\) are not among the listed degree-five special four-point families; their Newton-polygon classification does not imply this exact Cartier locus. General cyclic-cover Cartier and Hasse–Witt techniques are known; the assertion here is the explicit complete arithmetic stratum for the specified cover family and prime, not a new general Cartier formula.

## Limitations

This is an exact statement only for the given marked degree-five covers in characteristic \(11\). It does not classify abstract geometric isomorphism classes, arithmetic twists, or Newton polygons beyond the stated rank and \(a\)-number. It does not purport to establish uniqueness of this calculation in all unpublished databases; a separately documented prior-work comparison identifies residual bibliographic risk. Independent external audit has not been performed.

## References

1. Renzo Cavalieri and Rachel Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (first public version August 28, 2023), especially the discussion and formulas for four-branch cyclic covers.
2. Wanlin Li, Elena Mantovan, Rachel Pries, and Yunqing Tang, *Newton Polygons Arising for Special Families of Cyclic Covers of the Projective Line*, arXiv:1805.06914 (first public version May 17, 2018), for the special-family comparison and Newton-polygon background.
