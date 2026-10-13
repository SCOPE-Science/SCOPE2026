# Exact diagonal-square defect of Choudhry's one-parameter \(6\times 6\) pseudo-bimagic family
## Finding
For Choudhry's one-parameter order-\(6\) matrix \(M(t)\) from arXiv:2610.00915v1, let \(\Delta(t)\) be the sum of the squares on either main diagonal of \(M(t)\) minus the common squared-row sum. Then \(\Delta(t)=-2(t^2+3)Q(t)\), where \(Q(t)=t^{14}-75t^{12}-384t^{11}+285t^{10}+18432t^9+6129t^8-103680t^7+18387t^6+165888t^5+7695t^4-31104t^3-18225t^2+2187\). The polynomial \(Q\) has no rational root, so \(\Delta(t)\ne0\) for every \(t\in\mathbb Q\). Consequently no rational specialization of this family is bimagic. Moreover, for every rational \(a\ne0\) and \(b\), the affine normalization \(aM(t)+bJ\) has diagonal-square defect \(a^2\Delta(t)\), so no nonzero affine scaling/translation of a rational specialization becomes bimagic.

The two squared diagonal sums are equal for this block family, so \(\Delta(t)\) is the complete obstruction to upgrading the squared semi-magic condition to the bimagic condition.

## Assumptions and scope
The parameter \(t\) is rational, matching the rational-parameter setting used for the source construction. The matrix \(M(t)\) is exactly the one-parameter family displayed around equation (3.17) of Choudhry's preprint, with squared row/column sum
\[
2\bigl((t^4+30t^2+9)(t^2+3)^2\bigr)^2.
\]
The claim is family-specific. It does not assert that general bimagic squares of order \(6\) do not exist; numerical general examples are known, and the existence of a parametrized general order-\(6\) family remains a separate question.

## Proof
Write
\[
F(t)=(t^4+30t^2+9)(t^2+3)^2.
\]
The source block form is
\[
M(t)=\begin{bmatrix}X(t)&-X(t)J_3\\-J_3Y(t)&J_3Y(t)J_3\end{bmatrix}.
\]
Squaring entries removes all signs. The squared sum on either main diagonal is therefore
\[
\operatorname{tr}(X(t)^{*2})+\operatorname{tr}(Y(t)^{*2}),
\]
while every squared row and column has sum \(2F(t)^2\). Substituting the six diagonal polynomials printed for \(X(t)\) and \(Y(t)\) and collecting exactly gives
\[
\Delta(t)=\operatorname{tr}(X(t)^{*2})+\operatorname{tr}(Y(t)^{*2})-2F(t)^2
        =-2(t^2+3)Q(t),
\]
with \(Q(t)\) as stated above.

It remains to show that \(Q\) has no rational root. Since \(Q\) is monic with integer coefficients, the rational-root theorem implies that any rational root is an integer \(r\). Reducing modulo \(3\) gives
\[
Q(r)\equiv r^{14}\pmod 3,
\]
so an integer root must satisfy \(3\mid r\). Write \(r=3u\). The constant term of \(Q(3u)\) is \(2187=3^7\), while every nonconstant term is divisible by \(3^8\): the lowest cases are
\[
v_3(18225(3u)^2)\ge8,\qquad
v_3(31104(3u)^3)\ge8,\qquad
v_3(7695(3u)^4)\ge8,
\]
and all higher-degree terms have at least the same \(3\)-adic valuation. Hence
\[
Q(3u)\equiv3^7\not\equiv0\pmod{3^8},
\]
a contradiction. Thus \(Q(t)\ne0\) for all \(t\in\mathbb Q\); also \(t^2+3\ne0\) over \(\mathbb Q\), proving \(\Delta(t)\ne0\).

Finally let \(N=aM(t)+bJ\) with \(a\ne0\). Because \(M(t)\) is magic, the ordinary sum of a main diagonal equals the ordinary row sum. Expanding squares therefore cancels the cross term and the constant term in the diagonal-minus-row comparison:
\[
\Delta_N=a^2\Delta(t).
\]
Thus affine normalization cannot remove the obstruction.

## Verification
The bundled `verify.py` reconstructs the six diagonal polynomials directly from the coefficient vectors printed in the source, computes the defect with exact integer polynomial arithmetic, and verifies the factorization \(\Delta(t)=-2(t^2+3)Q(t)\). It checks the \(3\)-adic rational-root certificate coefficient by coefficient.

As a numerical anchor, the source's \(t=2\) matrix has common squared-row sum \(100962050\), both squared diagonal sums \(55622784\), and therefore
\[
\Delta(2)=-45339266,
\]
exactly matching the polynomial formula. The verifier also checks affine-defect scaling on three nontrivial integer affine transforms.

## Relationship to prior work
Choudhry constructs the one-parameter order-\(6\) pseudo-bimagic family and states the block criterion that would upgrade the construction to bimagic when the squared diagonal sum matches the squared row sum. The paper does not evaluate that upgrade condition on the displayed one-parameter family, and it explicitly leaves the search for parametrized general bimagic squares of order \(6\) for future work. The exact defect factorization above closes the specialization question for this particular displayed family: no rational choice of its parameter, and no subsequent nonzero affine normalization, reaches the bimagic locus.

The 2021 even-order existence theorem of Pan, Li, Chen, and Xin concerns normal bimagic squares and shows that normal order \(6\) squares do not exist. It does not imply the present statement, which concerns a general, non-normal rational family and an exact internal obstruction.

## Limitations
This is not a nonexistence theorem for general order-\(6\) bimagic squares, nor for all parametrized constructions of order \(6\). It excludes only the rational points of Choudhry's explicit one-parameter family and their nonzero affine normalizations. Over algebraic extensions, zeros of \(Q\) may exist and are outside the claim.

The originality search found no published statement of this exact defect polynomial or its rational nonvanishing. Because the motivating preprint is very recent, unindexed informal calculations remain a residual literature risk.

## References
1. A. Choudhry, "Construction of parametrized families of general pseudo-bimagic and bimagic squares," arXiv:2610.00915v1, first public 2026-10-01.
2. F. Pan, W. Li, G. Chen, and B. Xin, "A complete solution to the existence of normal bimagic squares of even order," Discrete Mathematics 344 (2021), Article 112292.
