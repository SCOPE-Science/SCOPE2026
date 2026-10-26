# Exact coefficient heights and extremizers in a quadratic discriminant family

## Finding
For an imaginary quadratic field \(K\), define its *integral defining-polynomial height* \(H_{\mathrm{all}}(K)\) to be the minimum of \(\max(|A|,|B|,|C|)\) over irreducible polynomials \(AT^2+BT+C\in\mathbb Z[T]\) with \(A\ne0\) and a root generating \(K\). Define \(H_{\mathrm{monic}}(K)\) analogously with \(A=1\).

For every integer \(m\ge1\) such that \(d_m=4m(m+1)-1\) is squarefree, set \(K_m=\mathbb Q(\sqrt{-d_m})\). Then
\[
H_{\mathrm{all}}(K_m)=m+1,\qquad H_{\mathrm{monic}}(K_m)=m(m+1).
\]
The complete set of *positive-leading-coefficient* defining polynomials of height \(m+1\) is
\[
mT^2\pm T+(m+1),\qquad (m+1)T^2\pm T+m,
\]
with exactly two additional polynomials
\[
(m+1)T^2\pm kT+(m+1)
\]
if and only if \(4m+5=k^2\) for a positive integer \(k\le m+1\). All other minimizers are obtained by multiplying these polynomials by \(-1\).

There are infinitely many eligible \(m\), indeed a positive density, by the classical squarefree-value theorem for separable quadratic polynomials with no fixed square divisor. Thus the exact ratio \(H_{\mathrm{monic}}(K_m)/H_{\mathrm{all}}(K_m)=m\) is unbounded along an infinite family.

## Assumptions and scope
The integer \(m\) is positive and \(d_m\) is squarefree; without squarefreeness the stated field discriminant and height formulas need not hold. As \(d_m\equiv3\pmod4\), the fundamental discriminant of \(K_m\) is \(-d_m\) and its integers are \(\mathbb Z[(1+\sqrt{-d_m})/2]\). Heights refer to raw integer *coefficients*, not Mahler measure, Weil height, or the rescaled algebraic-generator height. The enumerated minimizers are literal polynomials, not equivalence classes under variable substitutions.

## Proof
**1. Universal lower bound.** Let \(f(T)=AT^2+BT+C\) be any integral quadratic defining an imaginary quadratic field of fundamental discriminant \(-d\), with \(d>0\). If \(\alpha\) is a root, then \(A\alpha\) is an algebraic integer satisfying the monic quadratic \(U^2+BU+AC\), so its discriminant is \(B^2-4AC=-dt^2\) for some nonzero integer \(t\). Thus \(4AC=B^2+dt^2\ge d\), and \(4H(f)^2\ge d\). In our family \(d_m>4m^2\), so every defining quadratic has height at least \(m+1\). The polynomial \(mT^2+T+(m+1)\) has discriminant \(1-4m(m+1)=-d_m\), is irreducible, and has height \(m+1\).

**2. Rigidity at minimum height.** Suppose \(A>0\) and \(H(f)=m+1\). The negative discriminant gives \(C>0\). If \(|t|\ge2\), then \(4AC\ge4d_m>4(m+1)^2\), a contradiction. Hence \(|t|=1\). Since \(B^2+d_m=4AC\), the parity is forced: \(B\) is odd and \(B^2\ge1\). Consequently \(AC\ge m(m+1)\). With \(1\le A,C\le m+1\), each of \(A,C\) must belong to \(\{m,m+1\}\); the pair \((m,m)\) is impossible. For \((A,C)=(m,m+1)\) or its reversal, the equation gives \(B^2=1\). For \((A,C)=(m+1,m+1)\), it gives \(B^2=4m+5\). The coefficient-height constraint supplies \(|B|\le m+1\). Conversely every displayed polynomial has discriminant \(-d_m\) and height \(m+1\), so it defines \(K_m\). For the symmetric exceptions, \(k^2=4(m+1)+1\) also implies \(\gcd(k,m+1)=1\).

**3. Monic minimum.** Write \(\omega=(1+\sqrt{-d_m})/2\). An integral generator has the form \(u+v\omega\) with \(u,v\in\mathbb Z\), \(v\ne0\). Its norm is
\[
N(u+v\omega)=\frac{(2u+v)^2+d_mv^2}{4}\ge\frac{d_m+1}{4}=m(m+1),
\]
because the integer \(2u+v\) has the same parity as \(v\), and the minimum is attained for \(|v|=1\), \(|2u+v|=1\). Every monic defining quadratic has this positive norm as its constant coefficient, so its height is at least \(m(m+1)\). The minimal polynomial of \(\omega\) is \(T^2-T+m(m+1)\), attaining the bound.

**4. Infinite family.** The polynomial \(4m^2+4m-1\) is an irreducible separable quadratic over \(\mathbb Q\), and its integer values have greatest common divisor \(1\) (already the values at \(m=0,1\) are \(-1,7\)). The classical quadratic squarefree-value theorem of Ricci therefore gives positive density of squarefree values for positive \(m\), completing the infinitude assertion.

## Verification
The accompanying self-contained `verify.py` exhaustively enumerates all positive-leading integer quadratics of coefficient height at most \(m+1\) for squarefree \(d_m\) with \(1\le m\le80\), compares their complete set with the formula above, and independently enumerates small integral generators to check the monic bound. It uses only Python's standard library and prints `CERTIFICATE_OK` when every assertion succeeds. Finite enumeration is corroboration, not proof of the universal or density statements.

## Relationship to prior work
Arango-Piñeros et al., *Counting number fields of fixed degree by their smallest defining polynomial* (arXiv:2602.06943v1, §2.3, Lemma 2.4), define precisely this nonmonic coefficient-height invariant and establish the universal imaginary-quadratic lower bound \(H(K)\ge\sqrt{|\mathrm{Disc}(K)|}/2\), together with an asymptotically matching upper bound for large discriminants. Bhargava and Vemulapalli, *The existence of small defining polynomials for number fields* (arXiv:2610.20600v1), prove a dimension-uniform \(O_n(\sqrt{|\mathrm{Disc}(K)|})\) existence theorem for all degree-\(n\) fields. The present statement is narrower: exact integer height, every minimizing polynomial, and exact monic comparison for the explicit discriminant sequence; the universal lower bound is credited, not newly claimed. The quadratic squarefree-value infinitude is classical and also not claimed as new.

## Limitations
The result is specific to a family of imaginary quadratic fields and is not a new universal height estimate. It does not resolve exact heights for general discriminants or other polynomial degrees. Some components are elementary consequences of standard discriminant and norm identities, so a disguised earlier formulation of the complete extremizer classification remains possible. The exceptional symmetric case \(4m+5=k^2\) does not imply there are infinitely many *squarefree* instances of that exception.

## References
1. M. Bhargava and S. Vemulapalli, *The existence of small defining polynomials for number fields*, arXiv:2610.20600v1 (publicly posted 2026-10-14), https://arxiv.org/pdf/2610.20600.
2. S. Arango-Piñeros, F. Gundlach, R. J. Lemke Oliver, K. J. McGown, W. Sawin, A. Serrano López, A. Shankar and I. Varma, *Counting number fields of fixed degree by their smallest defining polynomial*, arXiv:2602.06943v1 (2026-02-06), §2.3, https://arxiv.org/html/2602.06943v1.
3. Z. Rudnick, *Squarefree values of quadratic polynomials* (course notes, 2015), §1, including Ricci's 1933 theorem; https://www.math.tau.ac.il/~rudnick/courses/sieves2015/squarefrees.pdf.
