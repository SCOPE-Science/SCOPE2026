# A critical-point discriminant controls the \(a\)-number of genus-four Artin–Schreier cubic covers in characteristic five

## Finding
Let \(k\) be algebraically closed of characteristic \(5\), and let
\[
f(x)=\alpha x^3+\beta x^2+\gamma x+\delta,\qquad\alpha\ne0.
\]
Write \(C_f\) for the smooth projective model of the affine Artin–Schreier curve \(y^5-y=f(x)\). Every such curve has genus \(4\) and Jacobian of \(5\)-rank zero. The complete \(a\)-number stratification of this cubic-pole family is
\[
a(J(C_f))=\begin{cases}4,&\beta^2+2\alpha\gamma=0,\\3,&\beta^2+2\alpha\gamma\ne0.\end{cases}
\]
Moreover, \(a=4\) (equivalently, superspeciality) occurs precisely when the quadratic derivative \(f'(x)\) has a double root. The superspecial parameter locus is a smooth divisor in the affine coefficient parameter space with \(\alpha\ne0\). All its geometric fibers are isomorphic to \(y^5-y=x^3\); the result does not claim distinct isomorphism classes for the complement.

## Assumptions and scope
The field \(k\) is algebraically closed and \(\operatorname{char}(k)=5\). The leading cubic coefficient \(\alpha\) is nonzero. The polynomial is allowed arbitrary quadratic, linear, and constant coefficients; the curve means its smooth projective model, rather than the affine chart alone. The \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_5,J(C_f)[5])\), equivalently \(\dim_k\ker\mathcal C\) on regular differentials, where \(\mathcal C\) denotes the \(5\)-semilinear Cartier operator. Superspecial means \(a=g\).

## Proof
1. The map \(x:C_f\to\mathbb P^1_k\) is a degree-\(5\) Artin–Schreier cover with a unique pole of order \(3\), at infinity. The ramification index there is \(5\) and the different exponent is \((5-1)(3+1)=16\). Riemann–Hurwitz gives \(2g-2=-10+16=6\), hence \(g=4\). The unique point \(P\) over infinity satisfies
\[
\operatorname{ord}_P(x)=-5,\quad\operatorname{ord}_P(y)=-3,\quad\operatorname{ord}_P(dx)=16-10=6.
\]
2. Four regular differentials form a basis:
\[
\{dx,\;x\,dx,\;y\,dx,\;y^2\,dx\}.
\]
Their orders at \(P\) are respectively \(6,1,3,0\). They are linearly independent (their pole semigroup weights, and thus their valuations, are distinct) and there are four of them, equal to the genus. They are regular at all finite points since \(\partial(y^5-y-f)/\partial y=-1\).
3. For the Cartier operator, \(\mathcal C(h^5\omega)=h\mathcal C(\omega)\), \(\mathcal C(dg)=0\), and on the rational coordinate \(x\), \(\mathcal C(x^jdx)=0\) whenever \(0\le j\le3\), whereas \(\mathcal C(x^4dx)=dx\). It follows that \(\mathcal C(dx)=\mathcal C(x\,dx)=0\). The identity \(y=y^5-f(x)\) gives
\[
\mathcal C(y\,dx)=y\mathcal C(dx)-\mathcal C(f(x)\,dx)=0.
\]
Squaring the same identity gives \(y^2=y^{10}-2y^5f+f^2\). The first two summands also have vanishing Cartier image after multiplication by \(dx\), because \(\mathcal C(f(x)\,dx)=0\). Thus
\[
\mathcal C(y^2\,dx)=\mathcal C(f(x)^2\,dx)
=(\beta^2+2\alpha\gamma)^{1/5}dx.
\]
Indeed, the sole exponent in \(f^2\), of degree at most \(6\), congruent to \(4\pmod 5\) is \(x^4\), with coefficient \(\beta^2+2\alpha\gamma\). Hence the Cartier matrix has rank \(0\) exactly when this coefficient vanishes, and rank \(1\) otherwise. The kernel dimension is consequently \(4\) or \(3\). Also \(\mathcal C^2=0\) on all four basis vectors, so its stable semilinear rank is zero; equivalently the Jacobian has \(5\)-rank zero.
4. Since \(f'(x)=3\alpha x^2+2\beta x+\gamma\), its quadratic discriminant in characteristic five is
\[
(2\beta)^2-4(3\alpha)\gamma
=4(\beta^2+2\alpha\gamma).
\]
The parameter divisor has equation \(H=\beta^2+2\alpha\gamma=0\), and is smooth on \(\alpha\ne0\) because \(\partial H/\partial\gamma=2\alpha\ne0\).
5. Translating \(x\) by \(-\beta/(3\alpha)\) removes the quadratic term; its resulting linear coefficient is \(\gamma-\beta^2/(3\alpha)\), which vanishes exactly when \(H=0\). An additive translation of \(y\) removes the remaining constant (as \(k\) is algebraically closed), and scaling \(x\) removes \(\alpha\). Consequently every superspecial member is geometrically isomorphic to \(y^5-y=x^3\). No claim about the Newton polygon, full Ekedahl–Oort type outside superspeciality, or the behavior of higher-degree poles is made.

## Verification
The self-contained Python script `check_cartier.py` enumerates all \(\alpha\in\mathbb F_5^\times\) and \(\beta,\gamma\in\mathbb F_5\), verifying the coefficient of \(x^4\) in \(f^2\), the derivative discriminant, and invariance of the vanishing locus under all translations \(x\mapsto x+u\). The finite test is diagnostic: the proof above establishes the universal statement for arbitrary coefficients over any algebraically closed characteristic-five field.

## Relationship to prior work
Farnell–Pries, *Families of Artin-Schreier curves with Cartier-Manin matrix of constant rank* (arXiv:1202.4183, first public version 2012-02-19), prove constant-rank results under a congruence hypothesis \(p\equiv1\pmod L\); here \(p=5\), the unique pole order is \(L=3\), and the hypothesis fails. Their work provides the methodological context, not the coefficient-dependent classification above. Farnell's dissertation (2010), section 2.6, examines a characteristic-five degree-four Artin–Schreier example, with different genus and pole order. Kudo–Harashita, *Superspecial curves of genus 4 in small characteristic* (arXiv:1607.01114), study global superspecial genus-four curves and establish earlier results covering uniqueness aspects of the superspecial fiber, but their results inspected do not provide the full discriminant-based \(a\)-number classification including the nonsuperspecial cubic members. The complete result here is the classification across all cubics; uniqueness of the superspecial isomorphism class in genus four is not asserted to be new.

## Limitations
This is a mathematical proof supported by finite diagnostics, not an independent audit. Specialized literature might overlap the explicit discriminant formula, and the original historical literature search is not an exhaustive novelty certification. The result does not give the non-superspecial Newton polygons or classify distinct curves with \(a=3\) up to isomorphism. A claim of a new complete genus-four superspecial-classification theorem is deliberately excluded.

## References
- S. Farnell and R. Pries, *Families of Artin-Schreier curves with Cartier-Manin matrix of constant rank*, arXiv:1202.4183 (2012), https://arxiv.org/abs/1202.4183.
- M. Kudo and S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114 (2016), https://arxiv.org/abs/1607.01114.
- S. Farnell, *Artin-Schreier Curves* (doctoral dissertation, 2010), https://mountainscholar.org/bitstreams/b29bf91f-4848-4aca-b33f-e67f23037554/download.
