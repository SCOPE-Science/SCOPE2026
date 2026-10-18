# A two-term asymptotic for squarefree-product multiplicative energy over polynomial rings

## Finding

For a prime power \(q\ge2\), let \(\mathcal M_n\) be the set of monic degree-\(n\) polynomials over \(\mathbb F_q[T]\), and define
\[
E_q(n)=\#\{(A,B,C,D)\in\mathcal M_n^4:AB=CD,\ AB\text{ is squarefree}\}.
\]
Here the degree of the constant monic polynomial \(1\) is zero. For every fixed \(q\), as \(n\to\infty\),
\[
\boxed{E_q(n)=q^{2n}\left(c_q(n+1)+b_q+O_q\big((n+1)^4q^{-n/4}\big)\right),}
\]
where the leading coefficient is the strictly positive, absolutely convergent Euler product
\[
\boxed{c_q=\prod_{P\ \mathrm{monic\ irreducible}}
(1-q^{-\deg P})^4(1+4q^{-\deg P}).}
\]
The constant \(b_q\) is specified exactly below by an absolutely convergent derivative-like coefficient series. This determines a full secondary term with exponentially small normalized error, not only an order-of-magnitude estimate.

## Assumptions and scope

The field size \(q\) is any fixed prime power, including powers of the characteristic. The four inputs are monic and have **exactly** equal degree. The common product \(AB=CD\), rather than merely each of its four factors, is required to be squarefree. A degree-zero input is permitted. The implied constant in \(O_q\) can depend on \(q\); uniformity in \(q\) is not asserted.

Introduce the holomorphic four-variable Euler product
\[
H_q(z_1,z_2,z_3,z_4)=\prod_{P}
\left(1+\sum_{i=1}^4(z_i/q)^{\deg P}\right)
\prod_{i=1}^4\left(1-(z_i/q)^{\deg P}\right)
=\sum_{\mathbf j\in\mathbb Z_{\ge0}^4}h_q(\mathbf j)\,\mathbf z^{\mathbf j}.
\]
Put \(a(\mathbf j)=\max(j_1,j_2)\) and \(b(\mathbf j)=\max(j_3,j_4)\). Then
\[
\boxed{b_q=-\sum_{\mathbf j\in\mathbb Z_{\ge0}^4}
\big(a(\mathbf j)+b(\mathbf j)\big)h_q(\mathbf j).}
\]
Both \(\sum_{\mathbf j}|h_q(\mathbf j)|\) and \(\sum_{\mathbf j}|\mathbf j|\,|h_q(\mathbf j)|\) converge, making this a genuine and unambiguous explicit arithmetic constant. The product defining \(H_q\) converges normally on every closed polydisc strictly inside \(|z_i|<\sqrt q\); in particular it includes the polydisc \(|z_i|\le q^{1/4}\).

## Proof

**1. Factorization into four coprime components.** Given \(AB=CD\), take \(U=\gcd(A,C)\), \(X=A/U\) and \(Y=C/U\). Then \(\gcd(X,Y)=1\) and the equality forces unique monic \(V\) with
\[
A=UX,\qquad B=VY,\qquad C=UY,\qquad D=VX.
\]
Conversely these formulae give a collision when \(\gcd(X,Y)=1\). Under the additional hypothesis that \(AB=UVXY\) is squarefree, all four component polynomials \(U,V,X,Y\) must be squarefree **and pairwise coprime**. Conversely this condition makes the common product squarefree. Equal degrees for \(A,B,C,D\) force \(\deg U=\deg V=k\) and \(\deg X=\deg Y=n-k\), with \(0\le k\le n\). Thus the desired count is a sum of pairwise-coprime squarefree quadruple counts over precisely these degree patterns.

**2. An exact four-variable coefficient formula.** Each irreducible polynomial \(P\) may occur in none of the four components or in exactly one of them, always to exponent one. Therefore their generating function is
\[
F(\mathbf x)=\prod_P\left(1+x_1^{\deg P}+x_2^{\deg P}+x_3^{\deg P}+x_4^{\deg P}\right).
\]
Unique factorization of monic polynomials gives \(\prod_P(1-x^{\deg P})^{-1}=(1-qx)^{-1}\). Consequently
\[
F(\mathbf x)=\prod_{i=1}^4(1-qx_i)^{-1}\,H_q(qx_1,qx_2,qx_3,qx_4).
\]
As a formal power-series identity, coefficient extraction at degrees \((k,k,n-k,n-k)\) and summation over \(k\) give the **exact identity for every** \(n\ge0\):
\[
\boxed{q^{-2n}E_q(n)=\sum_{\mathbf j}h_q(\mathbf j)
\big(n+1-a(\mathbf j)-b(\mathbf j)\big)_+,}
\]
where \(t_+=\max(t,0)\). Indeed an index \(\mathbf j\) contributes precisely when \(a(\mathbf j)\le k\le n-b(\mathbf j)\), giving \(\big(n+1-a-b\big)_+\) admissible integers \(k\).

**3. Analytic convergence.** Write \(d=\deg P\). The local factor of \(H_q\) is \((1+\sum_i w_i)\prod_i(1-w_i)\), where \(w_i=(z_i/q)^d\). Its linear terms cancel, hence the local factor is \(1+O(\max_i|w_i|^2)\) on a fixed bounded polydisc. Since the number of monic irreducibles of degree \(d\) is at most \(q^d\), the sum of local deviations is bounded by a geometric series when \(\max_i|z_i|<\sqrt q\). Thus \(H_q\) is holomorphic and bounded on \(|z_i|\le q^{1/4}\). Multivariable Cauchy estimates imply that some finite \(M_q\) satisfies
\[
|h_q(\mathbf j)|\le M_q q^{-|\mathbf j|/4},\qquad
|\mathbf j|=j_1+j_2+j_3+j_4.
\]
In particular the weighted coefficient sums in the assumptions converge absolutely.

**4. Main and secondary terms.** We may replace the positive part in the exact identity by \(n+1-a-b\), incurring only indices with \(a+b>n\). Since \(a+b\le|\mathbf j|\) and the number of four-component nonnegative vectors of total weight \(m\) is \(\binom{m+3}{3}\), the absolute error is at most
\[
M_q\sum_{m>n}\binom{m+3}{3}(m+n+1)q^{-m/4}
=O_q((n+1)^4q^{-n/4}).
\]
The unrestricted linear sum is
\[
(n+1)\sum_{\mathbf j}h_q(\mathbf j)
-\sum_{\mathbf j}(a+b)h_q(\mathbf j)
=(n+1)H_q(1,1,1,1)+b_q.
\]
Evaluating \(H_q\) at the all-one vector yields the stated product \(c_q\). Every factor is positive; moreover \((1-u)^4(1+4u)=1+O(u^2)\) as \(u\to0\), and \(\sum_Pq^{-2\deg P}<\infty\). Hence \(0<c_q<\infty\) and the proof is complete.

## Verification

An independent finite-field enumerator and a coefficient-based prime-allocation dynamic program agree for every \(0\le n\le7\) over \(\mathbb F_2\), every \(0\le n\le3\) over \(\mathbb F_3\), and every \(0\le n\le2\) over \(\mathbb F_5\). The verifier is provided as `verify.py`. The direct enumerator classifies a product as squarefree by polynomial gcd with its formal derivative and then sums the squares of product multiplicities. The second computation enumerates the assignments of irreducibles to the four coprime component slots. The check reports `VERIFY_OK` if all 15 test cases agree. The analytic estimate and convergence are proved in the preceding section, not inferred from finite tests.

## Relationship to prior work

Afifurrahman, *Statistics of divisor functions over function fields* (arXiv:2610.11240v1), Theorems 2.1–2.3 and Proposition 3.1, establishes unrestricted polynomial collision counts and supplies the unique four-component factorization used here. The manuscript's relevant complete mathematical text addresses unrestricted products rather than the condition that the **common product** be squarefree. The present secondary constant and exponential fixed-field error do not follow from those unrestricted formulas alone.

Lieb, *Uniform Probability and Natural Density of Mutually Left Coprime Polynomial Matrices over Finite Fields* (arXiv:1702.08312), Section 3, develops exact inclusion-exclusion counting for pairwise-coprime polynomial tuples and large-field expansions. Coprimality **without individual squarefreeness**, however, gives a different local generating series. Combining the two restrictions and summing correlated degree profiles is needed here to recover the fixed-field two-term energy asymptotic.

An earlier arithmetic claim concerns tuples for which each of \(A,B,C,D\) is squarefree, with \(q\to\infty\) at fixed degree; that weaker product restriction and different limit do not determine the present fixed-\(q\), \(n\to\infty\) theorem. Thus the restriction that the **product** is squarefree and the exponential secondary-term control are essential parts of the present statement.

## Limitations

The secondary term is expressed as an absolutely convergent four-variable Euler-product coefficient sum, not simplified to an elementary expression. No uniformity in the field size is proved. The analytic result concerns monic polynomials of equal degrees only. The result does not claim that the proof mechanism itself, unique factorization, or pairwise-coprime counting is new. An older implicit specialisation of general multivariate Euler-product theory could still overlap with the stated formula; independent validation is outstanding.

## References

1. Muhammad Afifurrahman, *Statistics of divisor functions over function fields*, arXiv:2610.11240v1 (publicly submitted 2026-10-08), https://arxiv.org/html/2610.11240v1 .
2. Julia Lieb, *Uniform Probability and Natural Density of Mutually Left Coprime Polynomial Matrices over Finite Fields*, arXiv:1702.08312 (2017), https://arxiv.org/abs/1702.08312 .
