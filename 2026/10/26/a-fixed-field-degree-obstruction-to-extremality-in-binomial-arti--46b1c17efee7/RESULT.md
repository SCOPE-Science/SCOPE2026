# A fixed-field degree obstruction to extremality in binomial Artin–Schreier families

## Finding
Let \(p\) be an odd prime, \(h,n\ge1\), and \(K=\mathbb F_{p^{2n}}\). Fix \(a\in K^\times\) and \(b\in K\). Let \(C\) be the smooth projective model of
\[
y^p-y=a x^{p^h+1}+b x^2.
\]
Its genus is \(g=(p-1)p^h/2\). Whenever \(n\ge h\), writing \(d=\gcd(h,2n)\), one has the **coefficient-uniform point-count bound**
\[
\bigl|\#C(K)-(p^{2n}+1)\bigr|\le (p-1)p^{n+d}.
\]
In particular, for nonzero \(b\), Hasse–Weil maximality or minimality over \(K\) is possible only if
\[
n>h,\qquad h\mid 2n.
\]
Thus \(n\ge2h\) if \(h\) is odd, whereas \(n\ge3h/2\) if \(h\) is even. These are necessary conditions, **not** sufficiency or existence statements.

## Assumptions and scope
All varieties are defined over the indicated finite field, and \(p\) is odd. The coefficient \(a\) never vanishes, while \(b\) may vanish for the point-count inequality. The divisibility restriction is stated only for \(b\ne0\). The affine equation is smooth because its derivative in \(y\) equals \(-1\), and its unique pole at infinity has order \(p^h+1\), prime to \(p\), giving the genus formula by the standard Artin–Schreier genus calculation. Maximality (respectively minimality) means attaining \(p^{2n}+1+2gp^n\) (respectively \(p^{2n}+1-2gp^n\)).

## Proof
Put \(q=p^{2n}\) and define the quadratic map \(Q:K\to\mathbb F_p\) by
\[
Q(x)=\operatorname{Tr}_{K/\mathbb F_p}(a x^{p^h+1}+b x^2).
\]
For each \(x\in K\), the number of \(y\in K\) solving the displayed Artin–Schreier equation is \(p\) exactly when \(Q(x)=0\), and is zero otherwise. For a nontrivial additive character \(\psi\) of \(\mathbb F_p\), orthogonality yields
\[
\#C(K)=q+1+\sum_{t\in\mathbb F_p^\times}\sum_{x\in K}\psi(tQ(x)).\tag{1}
\]
The polar form is
\[
B_Q(x,z)=\operatorname{Tr}_{K/\mathbb F_p}
\bigl(a(x^{p^h}z+xz^{p^h})+2bxz\bigr).
\]
Nondegeneracy of the trace pairing identifies its radical with the kernel of
\[
L(x)=a x^{p^h}+a^{p^{2n-h}}x^{p^{2n-h}}+2bx.\tag{2}
\]
Here and below we use \(n\ge h\), so all exponents in (2) are nonnegative. Apply the \(p^h\)-Frobenius to (2) and use \(x^{p^{2n}}=x\). The radical consists precisely of solutions of
\[
a^{p^h}x^{p^{2h}}+2b^{p^h}x^{p^h}+ax=0.\tag{3}
\]
Let \(\sigma(x)=x^{p^h}\) and \(k=K^\sigma=\mathbb F_{p^d}\), where \(d=\gcd(h,2n)\). Since \(a\ne0\), (3) is a second-order \(\sigma\)-difference equation with nonzero trailing and leading coefficients. Writing \(v=(x,\sigma x)^T\), it is equivalent to
\[
\sigma(v)=Mv,\qquad
M=\begin{pmatrix}0&1\\-a/a^{p^h}&-2b^{p^h}/a^{p^h}\end{pmatrix}\in\operatorname{GL}_2(K).
\]
**Fixed-vector lemma.** For any field \(K\), automorphism \(\sigma\) with fixed field \(k\), and \(M\in\operatorname{GL}_s(K)\), the \(k\)-space of solutions to \(\sigma(v)=Mv\) has dimension at most \(s\). Indeed, if a minimally \(K\)-dependent family of \(k\)-independent solutions exists, normalize a dependence to have coefficient one on its final vector. Applying \(\sigma\) to the dependence and cancelling the invertible matrix \(M\) shows, by minimality, that each other coefficient is fixed by \(\sigma\), hence lies in \(k\), a contradiction. Thus any \(k\)-independent solutions are also \(K\)-independent. This proves the lemma.

Consequently the radical has dimension at most two over \(\mathbb F_{p^d}\), hence dimension \(r\le2d\) over \(\mathbb F_p\). Because \(p\) is odd, \(Q\) vanishes on its polar radical (since \(B_Q(x,x)=2Q(x)\)). A quadratic Gauss sum with radical dimension \(r\) in \(2n\) variables has absolute value \(p^{(2n+r)/2}\), even when the nondegenerate quotient has odd dimension. Applying this to each nonzero scalar multiple \(tQ\) in (1) gives
\[
\bigl|\#C(K)-(q+1)\bigr|\le(p-1)p^{n+r/2}\le(p-1)p^{n+d},
\]
as claimed.

If \(C\) were maximal or minimal, its point-count deviation would have absolute value \((p-1)p^{n+h}\). For \(n\ge h\), comparison forces \(d\ge h\); since \(d\le h\), necessarily \(d=h\), i.e. \(h\mid2n\).

For completeness, the excluded ranges \(n\le h\) are settled without appealing to a published Cartier-theoretic bound. If \(n<h\), the Hasse–Weil upper equality value exceeds the elementary point-count ceiling \(pq+1\), while the lower equality value is negative; neither can be attained. If \(n=h\) and \(b\ne0\), the radical equation reduces to
\[
(a+a^{p^h})x^{p^h}+2bx=0.
\]
It cannot vanish identically on \(K\): the identity and nontrivial involution \(x\mapsto x^{p^h}\) are \(K\)-linearly independent as maps \(K\to K\), and \(2b\ne0\). Hence \(r<2h\), so the Hasse–Weil extreme Gauss-sum magnitude is impossible. Therefore \(n>h\). Finally \(h\mid2n\) together with \(n>h\) gives the stated odd/even lower bounds.

## Verification
The standalone Python script `verify.py` performs finite-field arithmetic over explicitly specified irreducible polynomial bases. It independently computes the \(\mathbb F_p\)-rank of the polar map and, in three small cases, enumerates all curve points by trace. Its observed radical dimensions satisfy \(r\le2\gcd(h,2n)\), and point counts satisfy the stated inequality. The selected modulus polynomials were independently checked irreducible using exact computer algebra; the standalone script assumes these moduli and does not retest irreducibility. These finite experiments illustrate, but are not used to infer, the universal theorem; the argument above is symbolic and complete.

To replay, run `python verify.py` with Python 3. The script has no external dependencies.

## Relationship to prior work
Almeida Filho–Tafazolian–Vieira (2026) determine iterated Cartier ranks for general curves \(y^p-y=xR(x)\), and prove a coefficient-sensitive necessary field-degree bound for maximality/minimality. The present result is a different, arithmetic **support-sensitive** restriction for the two-term polynomial \(R(x)=a x^{p^h}+bx\): the fixed field of the exponent Frobenius yields \(h\mid2n\), a condition not implied by the cited bound \(n\ge h+1\). Earlier general treatments of quadratic forms and Weil sums, including Anbar–Meidl and Chen, provide classical ingredients and algorithms that might give alternative derivations, but the explicit coefficient-uniform divisibility obstruction was not identified in the inspected material. The source comparison is necessarily qualified by incomplete access to certain full texts.

## Limitations
The bound need not be sharp when \(d<h\), and no construction of extremal binomial curves is asserted. The coefficient \(b=0\) case is included only in the quantitative estimate, not the stricter \(n>h\) statement. Nothing is claimed for characteristic two, for polynomials with three or more Frobenius terms, or for arithmetic twists beyond the displayed model. Completeness of historical priority has not been independently established, especially against general finite-field quadratic-form classification results.

## References
1. G. B. Almeida Filho, S. Tafazolian, S. C. Vieira, *\(a\)-Numbers, higher Cartier ranks and maximality of van der Geer–van der Vlugt curves*, arXiv:2610.17476v1 (first posted October 12, 2026).
2. N. Anbar, W. Meidl, *Quadratic functions and maximal Artin–Schreier curves*, Finite Fields Appl. 30 (2014), 49–71, DOI:10.1016/j.ffa.2014.05.008.
3. T. Ito, R. Tatematsu, T. Tsushima, *Criteria of maximality and minimality of van der Geer–van der Vlugt curves*, arXiv:2412.00902.
4. R. Chen, *Classification of quadratic forms over finite fields with maximal and minimal Artin–Schreier curves*, arXiv:2411.11705.
5. D. Takeuchi, T. Tsushima, *Gauss sums and Van der Geer–Van der Vlugt curves*, arXiv:2305.06117.
