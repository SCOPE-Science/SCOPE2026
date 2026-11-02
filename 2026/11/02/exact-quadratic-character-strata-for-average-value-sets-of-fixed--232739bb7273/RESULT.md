# Exact quadratic-character strata for average value sets of fixed-coefficient quintics

## Finding

Let \(q\) be a power of a prime \(p>5\), let \(\chi\) denote the quadratic character of \(\mathbb F_q\), with \(\chi(0)=0\), and put
\[
\mathcal V_q(a,b)=\frac1{q^2}\sum_{c,d\in\mathbb F_q}\left|\{x^5+ax^4+bx^3+cx^2+dx:x\in\mathbb F_q\}\right|,\qquad B=b-\frac{2a^2}{5}.
\]
For every pair \((a,b)\in\mathbb F_q^2\), the exact mean value-set size is
\[
\boxed{\mathcal V_q(a,b)=
\begin{cases}
\displaystyle \frac{19q}{30}+\frac16-\frac{\chi(5)}{30}+
\frac{5+\chi(5)-5\chi(-15)}{30q}+
\frac{1+5\chi(-15)}{30q^2},&B=0,\\[8pt]
\displaystyle \frac{19q}{30}+\frac16+
\frac{5+\chi(5)+5\chi(5B)}{30q}+
\frac{-5+5\chi(-15)-5\chi(-15B)}{30q^2},&B\ne0.
\end{cases}}
\]
Thus it depends on the two leading fixed coefficients only through the vanishing and quadratic character of \(B\). If \(B_+\) is any nonzero square and \(B_-\) any nonsquare, then
\[
\boxed{\mathcal V_q(0,B_+)-\mathcal V_q(0,B_-)=
\frac{q\chi(5)-\chi(-15)}{3q^2}\ne0.}
\]
In particular, the two nonzero quadratic-character strata have distinct average image sizes for every allowed finite field, not only asymptotically.

## Assumptions and scope

Here \(p>5\) is the characteristic, so \(2,3,4,5\) and every integer partition block size up to \(5\) are units in \(\mathbb F_q\). The symbol \(\chi(t)\) refers to the character of the full field \(\mathbb F_q\), not necessarily the prime subfield. The value set is a **set**, not a multiset. The average ranges independently and uniformly over both coefficients \(c,d\); the constant coefficient is immaterial to image size.

Translation \(x\mapsto x-a/5\) is a bijection on the field. After the translation, the coefficient of the cubic term becomes \(B=b-2a^2/5\). The coefficients of the quadratic and linear terms undergo an invertible affine transformation as \(c,d\) vary. Hence it suffices to work with \(F_{u,v}(x)=x^5+Bx^3+ux^2+vx\) and its mean \(\mathcal V_q(B)\).

## Proof

**1. Inclusion–exclusion on fibers.** A polynomial of degree five has at most five distinct preimages of each output. Let \(C_r(u,v)\) be the number of \(r\)-element subsets \(S\subseteq\mathbb F_q\) on which \(F_{u,v}\) is constant. For each fixed \(u,v\),
\[
|F_{u,v}(\mathbb F_q)|=\sum_{r=1}^{5}(-1)^{r-1}C_r(u,v)
\]
because each nonempty fiber contributes \(\sum_{r\ge1}(-1)^{r-1}\binom{m}{r}=1\). For two distinct inputs, equality is one nontrivial linear condition in \(u,v\), with \(q\) solutions. For three distinct inputs, the resulting two linear equations have determinant proportional to the Vandermonde product, so exactly one pair \((u,v)\) works. Consequently
\[
\mathcal V_q(B)=q-\frac{\binom q2}{q}+
\frac{\binom q3-K_4(B)+K_5(B)}{q^2},\tag{1}
\]
where \(K_r(B)\) counts distinct unordered \(r\)-sets at which some member of the family is constant.

**2. The two high-order interpolation conditions.** Write \(s=\sum_i x_i\) and \(Q=\sum_i x_i^2\). If four distinct inputs are zeros of \(F_{u,v}(x)-y\), the fifth root, counted with multiplicity, is \(-s\). The coefficient of \(x^3\) then forces \(B=e_2(x_1,\ldots,x_4)-s^2=-(Q+s^2)/2\). Conversely this relation determines the remaining coefficients uniquely. Thus
\[
24K_4(B)=\#\{(x_1,\ldots,x_4)\text{ pairwise distinct}:Q+s^2=-2B\}.\tag{2}
\]
Five distinct roots force their sum to vanish and their second elementary symmetric function to be \(B\), equivalent to
\[
120K_5(B)=\#\{(x_1,\ldots,x_5)\text{ pairwise distinct}:s=0,\ Q=-2B\}.\tag{3}
\]
Both converses hold because the specified symmetric coefficients determine a monic quintic of the required form.

**3. Exact quadratic-form counts.** For a nondegenerate quadratic form in \(r\ge1\) variables with determinant square class \(\Delta\), write \(Z_r(t;\Delta)\) for its number of representations of \(t\). Standard quadratic Gauss-sum evaluation gives
\[
Z_{2j}(t;\Delta)=q^{2j-1}+
\begin{cases}(q-1)q^{j-1}\chi((-1)^j\Delta),&t=0,\\-q^{j-1}\chi((-1)^j\Delta),&t\ne0,\end{cases}
\]
\[
Z_{2j+1}(t;\Delta)=q^{2j}+
\begin{cases}0,&t=0,\\q^j\chi((-1)^j\Delta t),&t\ne0.\end{cases}
\]
For dimension zero put \(Z_0(t)=1\) if \(t=0\) and \(0\) otherwise. These formulas also follow from additive-character orthogonality and the identity \(G(\chi)^2=\chi(-1)q\).

To remove the pairwise-distinct conditions in (2) and (3), apply the partition-lattice Möbius formula. A partition with block sizes \(m_1,\ldots,m_r\) carries weight \((-1)^{n-r}\prod_i(m_i-1)!\); summing over partitions of the same type gives the weights in the table below. For (2), the identified-coordinate quadratic form has matrix \(\operatorname{diag}(m_i)+mm^{\mathsf T}\) and determinant \(5\prod_i m_i\). For (3), the quadratic form \(\sum_i m_i y_i^2\) restricted to \(\sum_i m_i y_i=0\) has dimension \(r-1\) and determinant square class \(5\prod_i m_i\) (eliminate the last coordinate and apply the determinant lemma). All forms are nondegenerate because \(p>5\).

| Count | Block sizes | Combined Möbius weight | Form dimension | Determinant square class |
|---|---|---:|---:|---:|
| \(24K_4\) | \((4),(3,1),(2,2),(2,1,1),(1,1,1,1)\) | \(-6,8,3,-6,1\) | \(1,2,2,3,4\) | \(20,15,20,10,5\) |
| \(120K_5\) | \((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1)\) | \(24,-30,-20,20,15,-10,1\) | \(0,1,1,2,2,3,4\) | n/a, \(20,30,15,20,10,5\) |

In each row, multiply the listed weight by the applicable \(Z_r(-2B;\Delta)\) and add. For \(B=0\), put \(A=\chi(5)\), \(C=\chi(-15)\), and \(D=\chi(-20)\). This yields
\[
24K_4=q^3-6q^2+11q-6+(q-1)(qA+8C+3D),
\]
\[
120K_5=q^3-10q^2+35q-26+(q-1)(qA+20C+15D).
\]
For \(B\ne0\), the corresponding evaluations are
\[
24K_4=q^3-6q^2+11q-6-qA-8C-3D-6\chi(-10B)-6q\chi(5B),
\]
\[
120K_5=q^3-10q^2+35q-50-qA-20C-15D-30\chi(-10B)-10q\chi(5B)-20\chi(-15B).
\]
Substitute into (1), cancel the \(\chi(-20)\) and \(\chi(-10B)\) terms, and simplify to obtain the boxed formula.

**4. Squareclass gap.** For \(B\ne0\), multiplicativity gives \(\chi(5B)=\chi(5)\chi(B)\) and \(\chi(-15B)=\chi(-15)\chi(B)\). Subtracting the cases \(\chi(B)=1\) and \(-1\) gives exactly \((q\chi(5)-\chi(-15))/(3q^2)\). Its numerator cannot vanish because \(q\ge7\) while each displayed character has absolute value one. This proves the inequality.

## Verification

The standalone standard-library verifier `verify.py` evaluates both sides using exhaustive field arithmetic for all parameter values \(B\) over prime fields of orders \(7,11,13,17,19,23,29,31\) and over \(\mathbb F_{49}\). It also checks zero, square and nonsquare parameters over \(\mathbb F_{121}\), and exhausts the original unnormalized leading-coefficient pairs \((a,b)\) over \(\mathbb F_7\) and \(\mathbb F_{11}\). An independent combinatorial replay counts the eligible four- and five-element subsets directly at field orders \(7,11,13,17\) and compares formula (1).

Execution completed with `VERIFY_OK`, for \(372\) tested configurations, \(13,427,430\) direct input evaluations and \(11,418\) distinct-subset tests. These checks are finite corroboration only; the unrestricted conclusion follows from the algebraic proof.

## Relationship to prior work

Cesaratto, Matera, Pérez and Privitelli (arXiv:1306.1744, initial public posting 2013-06-07) give a general **exact inclusion–exclusion identity** in terms of as-yet-unevaluated interpolation-set counts, and bounds in a restricted range of fixed coefficients. Matera, Pérez and Privitelli (arXiv:1310.3293, initial posting 2013-10-11) prove estimates and second-moment results. Their 2015 follow-up (arXiv:1511.07942, initially posted 2015-11-25) treats wider, including nonlinear, coefficient families, but still derives estimates from unevaluated interpolation-point counts (its Lemma 3.1 and Section 6.3). Their explicit main first-moment estimate assumes \(s\le d-4\), and the preceding sharper estimate assumes \(s\le d/2-1\); neither includes the fixed-two-coefficient quintic case \((d,s)=(5,2)\). Those general identities, the leading coefficient \(19q/30\), and the underlying Gauss formulas are not claimed as new. The present statement evaluates both remaining interpolation terms, including their quadratic-character split, to give a coefficient-resolved **exact** mean in this natural boundary family.

Cohen's 1972 analysis of uniform distribution of finite-field polynomials supplies general factorization-pattern estimates and an asymptotic value-set corollary, but its inspected introductory theorems do not state the present exact quintic character law. The possibility of equivalent formulas elsewhere in the literature remains a priority risk.

## Limitations

Characteristic \(2,3,5\) is excluded: the quadratic-form determinants and coefficient normalization used above need not be units there. The result concerns an average over the two lower coefficients, not the full distribution of individual value-set sizes, and it does not assert a formula for degrees other than five. Publication priority has not been independently established.

## References

1. E. Cesaratto, G. Matera, M. Pérez, and M. Privitelli, *On the value set of small families of polynomials over a finite field, I*, arXiv:1306.1744 (first posted 2013-06-07), https://arxiv.org/abs/1306.1744.
2. G. Matera, M. Pérez, and M. Privitelli, *On the value set of small families of polynomials over a finite field, II*, arXiv:1310.3293 (first posted 2013-10-11), https://arxiv.org/abs/1310.3293.
3. G. Matera, M. Pérez, and M. Privitelli, *On the value set of small families of polynomials over a finite field, III*, arXiv:1511.07942 (first posted 2015-11-25), https://arxiv.org/abs/1511.07942.
4. S. D. Cohen, *Uniform Distribution of Polynomials Over Finite Fields*, J. London Math. Soc. (2) 6 (1972), 93–102, https://doi.org/10.1112/jlms/s2-6.1.93.
