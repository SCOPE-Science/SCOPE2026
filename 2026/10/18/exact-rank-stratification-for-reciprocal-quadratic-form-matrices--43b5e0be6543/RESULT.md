# Exact rank stratification for reciprocal quadratic-form matrices over prime fields

## Finding

Let \(p\ge 5\) be a prime and \(c,d\in\mathbb Z\). Suppose the discriminant \(\Delta=c^2-4d\) is a quadratic nonresidue modulo \(p\). Write \(\alpha,\beta\in\mathbb F_{p^2}\) for the two roots of \(T^2+cT+d\), and put \(z=\alpha/\beta\) and \(t=\operatorname{ord}_{\mathbb F_{p^2}^{\times}}(z)\). The choice of root interchanges \(z\) and \(z^{-1}\), so \(t\) is well defined. It divides \(p+1\), and \(t>1\).

For the \(p\)-by-\(p\) matrix
\[
M_p(c,d)=\bigl[(i^2+cij+dj^2)^{p-2}\bigr]_{0\le i,j<p}\pmod p,
\]
its **exact** rank is
\[
\operatorname{rank}_{\mathbb F_p}M_p(c,d)=p-1-\delta_p(t),\qquad
\delta_p(t)=\begin{cases}
0 &t\text{ odd},\\
(p-1)/2 &t=2,\\
(p+1)/4-2 &t=4,\\
(p+1)/t &t\ge 6\text{ even}.
\end{cases}
\]
Here the case \(t=4\) is possible only when \(4\mid p+1\), and the displayed integer is nonnegative. In particular, for the corresponding *integer* determinant
\[
D_p(c,d)=\det\bigl[(i^2+cij+dj^2)^{p-2}\bigr]_{0\le i,j<p},
\]
one has the uniform, not necessarily optimal, divisibility
\[
p^{1+\delta_p(t)}\mid D_p(c,d).
\]
The statement concerns the rank of the **full** matrix with both indices including zero, and not the smaller nonzero-index determinants occurring elsewhere in the literature.

## Assumptions and scope

All ranks and orders are over the indicated finite fields; \(c\) and \(d\) are reduced modulo \(p\) for this purpose. The nonsquare condition implies \(d\ne0\pmod p\), since a monic quadratic with a zero constant term splits. It also implies \(\alpha\ne\beta\), \(\beta=\alpha^p\), and \(\alpha\beta=d\). Thus \(z^p=z^{-1}\) and \(z^{p+1}=1\). The determinant is formed from integer entries before reduction. No assertion of an **exact integer determinant valuation** is made.

## Proof

**1. Reduction to an explicit coefficient matrix.** Work in \(\mathbb F_p\), and write
\[
f(T)^{p-2}=\sum_{a=0}^{2p-4}u_a T^a,\qquad f(T)=T^2+cT+d.
\]
In particular \(u_0=d^{p-2}\ne0\) and \(u_{2p-4}=1\). Let \(C\) be the coefficient matrix of the unique polynomial of degree at most \(p-1\) in each variable representing the same function on \(\mathbb F_p^2\) as \((X^2+cXY+dY^2)^{p-2}\). A positive exponent \(e\) reduces to \(1+((e-1)\bmod(p-1))\) and exponent zero remains zero. Since the total degree is \(2p-4\), the reduced polynomial equals
\[
\begin{aligned}
R(X,Y)={}&u_0Y^{p-3}+X^{p-3}+u_{p-3}X^{p-3}Y^{p-1}\\
&+u_{p-1}X^{p-1}Y^{p-3}+u_{p-2}X^{p-2}Y^{p-2}\\
&+\sum_{r=1}^{p-4}(u_r+u_{r+p-1})X^rY^{p-3-r}.
\end{aligned}
\]
Let \(V=(i^r)_{0\le i,r<p}\) be the evaluation Vandermonde matrix. It is invertible over \(\mathbb F_p\), and \(M_p(c,d)=VCV^{\mathsf T}\). Hence \(M_p(c,d)\) and \(C\) have the same rank. The displayed nonzero positions occupy disjoint rows and columns except that the rows indexed \(0\) and \(p-1\) share column \(p-3\). The row \(p-3\) has the nonzero entry \(1\) in column \(0\), and the row \(0\) has a nonzero entry \(u_0\) in column \(p-3\). All remaining potentially nonzero positions are isolated in distinct rows and columns. It follows **exactly**, not merely as a bound, that
\[
\operatorname{rank}(M_p(c,d))=2+\mathbf1_{u_{p-2}\ne0}+\sum_{r=1}^{p-4}\mathbf1_{u_r+u_{r+p-1}\ne0}.
\]

**2. Interpolation identifies every possible zero.** The polynomial \(f\) has no root in \(\mathbb F_p\), so Fermat's theorem gives \(f(x)^{p-2}=1/f(x)\) for \(x\in\mathbb F_p^\times\). Let \(H(T)=\sum_{r=0}^{p-2}h_rT^r\) interpolate \(1/f(x)\) on \(\mathbb F_p^\times\). The coefficients satisfy \(h_r=u_r+u_{r+p-1}\) for \(1\le r\le p-4\), and \(h_{p-2}=u_{p-2}\): they are exactly the corresponding residues of powers modulo \(T^{p-1}-1\).

Over \(\mathbb F_{p^2}\), partial fractions and the finite-geometric identity
\[
\frac1{x-\alpha}=\frac{\sum_{r=0}^{p-2}\alpha^{p-2-r}x^r}{1-\alpha^{p-1}},\qquad x\in\mathbb F_p^\times,
\]
give, using \(\alpha^{p-1}=\beta/\alpha\) and \(\beta^{p-1}=\alpha/\beta\),
\[
h_r=\frac{\alpha^{p-1-r}+\beta^{p-1-r}}{(\alpha-\beta)^2},\qquad 0\le r\le p-2.
\]
Consequently \(h_r=0\) precisely when \(z^{p-1-r}=-1\). Inserting these coefficients in the exact rank count yields
\[
\operatorname{rank}(M_p(c,d))=p-1-\#\{k\in\{1,3,4,\ldots,p-2\}:z^k=-1\}.
\]
The exponent \(2\) is excluded because the boundary monomials occupying rows \(0,p-1,p-3\) already contribute two independent columns; no corresponding isolated row exists.

**3. Count the roots of minus one.** Since \(z\) has order \(t\), the equation \(z^k=-1\) has no solution if \(t\) is odd, and otherwise is equivalent to \(k\equiv t/2\pmod t\). As \(t\mid p+1\), among \(1\le k\le p-2\) there are \((p-1)/2\) solutions for \(t=2\); for \(t=4\) there are \((p+1)/4-1\) solutions and removing the forbidden \(k=2\) gives \((p+1)/4-2\); and for even \(t\ge6\) there are exactly \((p+1)/t\). This is the claimed formula.

**4. Integer consequence.** The reduction of the integer matrix has rank \(p-1-\delta_p(t)\), hence nullity \(1+\delta_p(t)\). By integral Smith normal form, at least that many invariant factors are divisible by \(p\). Thus \(p^{1+\delta_p(t)}\) divides its integer determinant. This implication remains valid when the determinant itself vanishes.

## Verification

A standalone standard-library Python verifier (`verify.py`) computes the multiplicative order of \(z\) in the explicitly represented quadratic extension \(\mathbb F_{p^2}\), independently performs modular Gaussian elimination on the full \(p\)-by-\(p\) matrix, and checks the formula for **all** irreducible parameter pairs \((c,d)\) at primes \(p=5,7,11,13,17,19,23\): **724 comparisons**, all successful. The proof establishes the universal quantifiers; these finite tests do not establish the infinite result.

For instance, at \(p=19\), \((c,d)=(1,10)\) has a nonsquare discriminant and \(t=4\); the exact rank is \(15\), implying \(19^4\mid D_{19}(1,10)\). This is stronger than the generic square-divisibility statement when the latter applies. At \(p=19\), \((c,d)=(1,2)\) has \(t=20\), giving rank \(17\) and a cubic divisibility bound.

## Relationship to prior work

Zhang and Yang (2026), *A Determinant Congruence Conjectured by Sun*, Theorem 1.1 and Lemmas 3.1–3.3, prove \(p^2\mid D_p(c,d)\) under the different hypothesis that \(d\) is a nonsquare, using a rank upper bound \(p-2\) and a particular coefficient cancellation. Their proof already contains the polynomial coefficient decomposition used in Step 1 above; it is credited here. The current theorem supplies an **exact rank** for the irreducible-discriminant locus, including cases where \(d\) is a square, by counting *all* zero interpolation coefficients via the Frobenius root ratio. It gives explicit higher congruence exponents when the nullity exceeds two. Neither result implies the other in its full hypothesis range.

She and Sun (2025), *Some Determinants Involving Binary Forms*, treat related quadratic-form determinant congruences and product formulas for smaller nonzero-index matrices. Their Theorems 1.2–1.3 concern determinant evaluations rather than this full-matrix rank stratification. Zhu and Ren (2024), *On Some Determinant Conjectures*, likewise analyze related proper subdeterminants and specific Lucas-sequence coefficient obstructions. Their cases and objects do not state the order-indexed rank formula for the full matrix. These are comparisons of the actual mathematical conclusions, not title-based exclusions.

## Limitations

The theorem assumes an irreducible quadratic modulo \(p\); it does not classify split or repeated-root forms. The divisibility conclusion is only a **lower bound** on the integer determinant's \(p\)-adic valuation and may be strict, including possible zero determinants. Relevant general identities about cyclic-group interpolation or Cauchy-type matrices could conceivably contain an implicit equivalent formulation; no exhaustive uniqueness assertion is made. Independent mathematical validation has not been performed.

## References

- Y. Zhang and Y. Yang, *A Determinant Congruence Conjectured by Sun*, arXiv:2605.19486 (first posted 19 May 2026), https://arxiv.org/abs/2605.19486 ; full text https://arxiv.org/pdf/2605.19486 .
- Y.-F. She and Z.-W. Sun, *Some Determinants Involving Binary Forms*, arXiv:2407.04642 (2024 preprint; 2025 publication), https://arxiv.org/pdf/2407.04642 .
- H.-L. Zhu and M.-Z. Ren, *On Some Determinant Conjectures*, arXiv:2409.07008 (2024), https://arxiv.org/abs/2409.07008 .
- Z.-W. Sun, *On Some Determinants and Permanents*, arXiv:2207.13039 (2022), https://arxiv.org/abs/2207.13039 .
