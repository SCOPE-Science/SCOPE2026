# Idempotent fluctuations of uniformly sampled perfect evolution algebras over finite fields

## Finding

For every prime power \(q\) and integer \(n\ge2\), let \(M\) be uniform in \(\mathrm{GL}_n(\mathbb F_q)\), and let \(X\) be the number of **nonzero** idempotents in the evolution algebra \(E_M\) defined below. Then

\[
\mathbb E X=1,
\qquad
\operatorname{Var}(X)=
\begin{cases}
1,&\operatorname{char}\mathbb F_q=2,\\[3pt]
\displaystyle 1-\frac{(q-1)((2q-1)^n-2q^n+1)}{2(q^n-1)(q^n-q)},&\operatorname{char}\mathbb F_q\ne2.
\end{cases}
\]

For every odd \(q\) and \(n\ge2\), the displayed correction is strictly positive, so the variance is strictly below one. It tends to zero as \(n\to\infty\) with odd \(q\) fixed, and as \(q\to\infty\) through odd prime powers with \(n\) fixed. For \(n=2\), the odd-characteristic variance simplifies to \(1-(q-1)/(q(q+1))\).

In characteristic two there is a stronger, **complete distribution law**. Write \(X=2^R-1\); then \(R\in\{0,\ldots,n\}\), and its distribution is independent of the extension degree of \(\mathbb F_q/\mathbb F_2\):

\[
\Pr(R=r)=\sum_{k=r}^{n}
(-1)^{k-r}2^{\binom{k-r}{2}}
\left[\begin{smallmatrix} k\\r\end{smallmatrix}\right]_{2}
\frac{1}{|\mathrm{GL}_k(\mathbb F_2)|},
\qquad 0\le r\le n.
\]

Here \(\left[\begin{smallmatrix}k\\r\end{smallmatrix}\right]_{2}\) is the binary Gaussian binomial coefficient, \(|\mathrm{GL}_k(\mathbb F_2)|=\prod_{i=0}^{k-1}(2^k-2^i)\), and the product for \(k=0\) is one. Equivalently, this is the distribution of the number of nonzero fixed vectors of a uniformly random element of \(\mathrm{GL}_n(\mathbb F_2)\).

## Assumptions and scope

An evolution algebra is a commutative, generally nonassociative algebra with a *natural basis* \(e_1,\dots,e_n\) satisfying \(e_i e_j=0\) for \(i\ne j\). Define

\[
e_i^2=\sum_{j=1}^n M_{ji}e_j,
\qquad M\in\mathrm{GL}_n(\mathbb F_q).
\]

Invertibility is equivalent to perfection \(E_M^2=E_M\). If \(x=(x_1,\ldots,x_n)^t\) and \(x^{[2]}=(x_1^2,\ldots,x_n^2)^t\), the idempotency equation is

\[
M x^{[2]}=x.
\]

Sampling is **uniform in invertible labelled natural-basis structure matrices**; it is not uniform on algebra isomorphism classes. The zero idempotent is excluded from \(X\) throughout, and the dimension assumption \(n\ge2\) is required for the variance denominator. No assumption of algebraic closure is made.

## Proof

**1. First moment.** Fix a nonzero \(x\in\mathbb F_q^n\). Its squared-coordinate vector \(x^{[2]}\) is nonzero. For uniformly random invertible \(M\), the vector \(Mx^{[2]}\) is uniform on the \(q^n-1\) nonzero vectors. Consequently

\[
\Pr(Mx^{[2]}=x)=\frac1{q^n-1}
\]

and summing over the \(q^n-1\) possible nonzero \(x\) gives \(\mathbb E X=1\).

**2. Two-point factorial moment.** If distinct nonzero \(x,y\) are both idempotents, they are linearly independent. Indeed, if \(y=tx\) with \(t\ne0\), then the quadratic equation gives \(t^2x=tx\), hence \(t=1\), contradicting distinctness. There are exactly

\[
D=(q^n-1)(q^n-q)
\]

ordered linearly independent pairs \((x,y)\). For such a pair, if \(x^{[2]}\) and \(y^{[2]}\) are independent, a uniform \(M\) sends them to \((x,y)\) with probability \(1/D\), since the invertible general linear group acts transitively on ordered independent pairs with equal-size fibres. If their squares are dependent, no invertible \(M\) can send them to independent vectors. Therefore

\[
\mathbb E[X(X-1)]=1-\frac{B}{D},
\]

where \(B\) counts independent pairs whose coordinatewise squares are dependent. Since \(\mathbb E X=1\), the left side equals \(\operatorname{Var}(X)\).

**3. Characteristic-sensitive collision count.** In characteristic two, coordinatewise squaring is a field automorphism, so it preserves linear independence of vector pairs; thus \(B=0\) and the variance equals one.

Suppose \(q\) is odd. Fix a nonzero \(x\) with exactly \(s\) nonzero coordinates. A vector \(y\ne0\) has \(y^{[2]}\) in the line through \(x^{[2]}\) precisely if its support equals that of \(x\) and, for some \(c\in(\mathbb F_q^\times)^2\), every nonzero coordinate of \(y\) is one of the two square roots of \(c x_i^2\). There are \((q-1)2^{s-1}\) such \(y\). Exactly \(q-1\) are scalar multiples of \(x\), so exactly \((q-1)(2^{s-1}-1)\) give the forbidden independent square-collision pairs. There are \(\binom ns(q-1)^s\) choices for \(x\) with support size \(s\). Summing, including the zero contribution at \(s=1\), gives

\[
B=(q-1)\sum_{s=1}^n \binom ns(q-1)^s(2^{s-1}-1)
=\frac{q-1}{2}\big((2q-1)^n-2q^n+1\big).
\]

Inserting this into the factorial moment completes the stated variance formula. Positivity holds because for \(n\ge2\) there are vectors of support two, giving \(B>0\). The two asymptotic conclusions follow from \((2q-1)/q^2<1\) for each odd \(q\ge3\) and from the leading fixed-dimension expansion \(B/D\sim(2^{n-1}-1)q^{1-n}\).

**4. Complete characteristic-two law.** Let \(q=2^f\) and define \(T(v)=M v^{[2]}\). Then \(T\) is a bijective Frobenius-semilinear map, and its fixed set is a vector space over \(\mathbb F_2\), of dimension \(R\). Any \(\mathbb F_2\)-independent fixed vectors are \(\mathbb F_q\)-independent: induct on their number; if the last fixed vector were a linear combination of the earlier ones over \(\mathbb F_q\), applying \(T\) and comparing the unique coefficients would force all coefficients to satisfy \(a^2=a\), hence to lie in \(\mathbb F_2\), a contradiction. In particular \(R\le n\).

For each \(0\le k\le n\), every ordered \(\mathbb F_q\)-independent \(k\)-tuple has independent squared-coordinate vectors. It is fixed by \(T\) with probability \(\prod_{i=0}^{k-1}(q^n-q^i)^{-1}\). As there are exactly that many ordered independent \(k\)-tuples, the expected number of ordered \(\mathbb F_2\)-independent fixed \(k\)-tuples is one. If \(R=r\), their number is \(|\mathrm{GL}_k(\mathbb F_2)|\left[\begin{smallmatrix}r\\k\end{smallmatrix}\right]_2\). Thus

\[
\mathbb E\left[\begin{smallmatrix} R\\k\end{smallmatrix}\right]_2
=\frac1{|\mathrm{GL}_k(\mathbb F_2)|}
\quad(0\le k\le n).
\]

Binary Gaussian-binomial inversion of this finite upper-triangular system yields the displayed probability formula. No limit or semilinear conjugacy-class classification is required.

## Verification

The standard-library script `verify_random_evolution.py` constructs explicit polynomial-basis models of the indicated extension fields, exhaustively scans every invertible matrix, independently counts the solutions of \(Mx^{[2]}=x\), and checks the exact first moment, second factorial moment, and characteristic-two distribution. The checked field/dimension pairs are \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2),(7,2),(8,2),(9,2)\). All ten completed exact scans returned `VERIFY_OK`.

For example, in dimension two the exact variance is \(5/6\) over \(\mathbb F_3\), \(13/15\) over \(\mathbb F_5\), \(25/28\) over \(\mathbb F_7\), and exactly one over each of \(\mathbb F_2,\mathbb F_4,\mathbb F_8\). The finite verifications check the formulas but are not used as proof for arbitrary field orders or dimensions.

Run using `python verify_random_evolution.py` from the directory containing the script; no nonstandard libraries or external files are required.

## Relationship to prior work

García-Martínez and Pérez-Rodríguez [1, Section 3.3] provide the structural idempotent equation for evolution algebras and establish existence over the complex numbers for perfect algebras. Hu and Wen [2] construct and classify idempotents in a particular three-dimensional family that is not perfect at its exceptional member. Neither contains a distribution over uniformly random invertible finite-field structure matrices.

Wei and Zou [3] give a finite-field enumeration of **isomorphism classes of algebras with \(E^2=E\)**. Their word *idempotent* describes the algebra, not the number of pointwise idempotents \(x^2=x\), and their orbit counts do not supply the factorial moment here. General Shintani descent for semilinear matrix actions [4] provides broader context for the characteristic-two field-extension invariance; no novelty of that abstract correspondence is asserted.

A subsequently available survey [5, Remark 23 and Conjecture 2] explicitly records the first moment and proposes a Galois-theoretic large-field description. Thus the first moment is included as normalization, **not claimed as a new discovery**. Its conjectural limit and the general semilinear literature do not give the exact odd-characteristic finite-field variance defect. Survey [5] first appeared after the temporal anchor of the present motivating literature and is used only for scientific comparison.

## Limitations

The exact variance and characteristic-two distribution concern uniform structure matrices, not an isomorphism-class-uniform ensemble. The complete law in odd characteristic and higher odd-characteristic factorial moments are not determined. No Poisson or full symmetric-group limiting distribution is proved. The characteristic-two law may also be recovered by broader established semilinear tools; the distinguishing contribution is the uniform exact odd-characteristic second-moment correction and its comparison with the even-characteristic behaviour. Search and source comparisons cannot rule out an unindexed equivalent formula; independent mathematical review has not been performed.

## References

1. X. García-Martínez and A. Pérez-Rodríguez, *A note on complete evolution algebras*, arXiv:2512.12418v1 (first posted 2025-12-13), especially Section 3.3. https://arxiv.org/abs/2512.12418
2. X.-Y. Hu and R. Wen, *Idempotent-free non-solvable evolution algebras over the complex numbers*, arXiv:2609.25023 (first posted 2026-08-12), Theorem 2.1. https://arxiv.org/abs/2609.25023
3. Y. Wei and Y. M. Zou, *Isomorphism classes of idempotent evolution algebras*, arXiv:2310.12368v1 (2023), Introduction and Sections 2–6. https://arxiv.org/abs/2310.12368
4. S. Harper, *Totally deranged elements of almost simple groups and invariable generating sets*, arXiv:2304.10213 (2023), Section 2.2 (Shintani descent). https://arxiv.org/abs/2304.10213
5. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first posted 2026-10-15), Remark 23, Question 22 and Conjecture 2. https://arxiv.org/abs/2610.22248
