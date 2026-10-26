# A gap-invariant quadratic composition formula for lunar divisors

## Finding

Let \(\odot\) denote binary lunar multiplication: for binary polynomials, each coefficient of the product is the logical OR of the products (logical AND) of pairs of coefficients. Let \(d_2(M)\) count distinct positive binary polynomials \(A\) admitting a binary polynomial \(B\) with \(A\odot B=M\).

For arbitrary integers \(h\ge3\) and \(n\ge1\), put
\[
W_{h,n}=3\sum_{j=0}^{n-1}2^{hj}=3\frac{2^{hn}-1}{2^h-1}.
\]
The support of its binary expansion is \(\{hj,hj+1:0\le j<n\}\), with no carries. For \(b\ge1\), let \(c_b(m)\) denote the number of ordered compositions of \(m\) into parts in \(\{1,\ldots,b\}\), with \(c_b(0)=1\) and \(c_b(m)=0\) for \(m<0\).

**Theorem.** For every \(h\ge3\) and \(n\ge1\),
\[
d_2(W_{h,n})=\sum_{b=1}^{n}\bigl(c_b(n-b)+c_b(n-b)^2\bigr).
\]
In particular, the count is independent of \(h\), despite the changing integer and spacing of its binary digits. The first seven values, for \(n=1,\ldots,7\), are \(2,4,6,12,24,62,160\). For \(n\ge4\) this count is strictly greater than twice the lunar divisor count of the length-\(n\) all-ones binary number. The threshold on the gap is exact: at \(h=2,n=2\) the count is \(5\), whereas the displayed sum equals \(4\).

## Assumptions and scope

All factors are nonzero finite binary polynomials, and a divisor means a *distinct factor*, not a factorization counted with multiplicity. The constant coefficient of a factor of \(W_{h,n}\) must be \(1\), because that of the target is \(1\). All integers \(h\ge3\) and \(n\ge1\) are included; no assertion about the usual integer divisor function is intended.

## Proof

Represent a binary number by its support of exponents. Lunar multiplication is Minkowski addition of finite supports. Put \(Q_n(X)=1+X+\cdots+X^{n-1}\) in the Boolean polynomial semiring and write the target as \((1+X)Q_n(X^h)\). Its support consists exactly of residues \(0\) and \(1\pmod h\) in a consecutive run of \(n\) blocks.

**Residue-exclusion lemma.** If \(A\odot B=(1+X)Q_n(X^h)\), the constant coefficients of both factors equal \(1\). Hence each support is contained in the target support. If both factors contained a term with exponent \(1\pmod h\), their product would contain an exponent \(2\pmod h\), impossible because \(h\ge3\). Thus at least one factor has all exponents divisible by \(h\). This argument also applies to \(h=3\): residue \(2\) is still excluded.

**Full-window lemma.** Let \(U,V\) be binary polynomials with constant coefficient \(1\), degree \(a\) and \(b-1\), respectively, and suppose \(a+b=n\). The equality \(U\odot V=Q_n\) holds for some \(V\) of degree \(b-1\) if and only if \(U\odot Q_b=Q_n\). Necessity follows by replacing every coefficient of \(V\) by \(1\): the support can only grow, its largest possible exponent is still \(n-1\), and it already contains every exponent through \(n-1\). Conversely take \(V=Q_b\). If the exponents in \(U\) are \(0=s_0<\cdots<s_r=a\), the intervals \([s_i,s_i+b-1]\) cover \([0,n-1]\) exactly when each gap \(s_{i+1}-s_i\) is at most \(b\). Thus the number of eligible \(U\) for fixed \(b\), and hence fixed \(a=n-b\), is \(c_b(n-b)\), by the bijection taking successive gaps as composition parts. When \(a=0\), the empty composition counts the constant polynomial \(1\).

**Counting pure factors.** A divisor supported only at exponents divisible by \(h\) is of the form \(A(X^h)\). Its cofactor necessarily has the form \(B_0(X^h)+XB_1(X^h)\). The two residue rows must each equal \(Q_n\): \(A\odot B_0=Q_n\) and \(A\odot B_1=Q_n\). Both cofactors have degree \(b-1\) in the compressed variable because each row has degree \(n-1\) and \(A\) has degree \(n-b\). By the full-window lemma, this is possible precisely for the \(c_b(n-b)\) allowed choices of \(A\), since choosing \(B_0=B_1=Q_b\) suffices. Summing over \(b\) gives \(\sum_b c_b(n-b)\) pure-residue divisors.

**Counting mixed factors.** Every other divisor has terms in both residue classes, so the residue-exclusion lemma forces its cofactor to have only exponents divisible by \(h\). Write the divisor as \(A_0(X^h)+XA_1(X^h)\) and cofactor as \(B(X^h)\). Since the target has both first and last exponents in each row and both rows have degree \(n-1\), the compressed polynomials \(A_0,A_1\) each have constant coefficient \(1\) and the same degree \(n-b\), while \(B\) has degree \(b-1\). Both rows must satisfy \(A_i\odot B=Q_n\). Necessity and sufficiency again follow from the full-window lemma, since a single common choice \(B=Q_b\) works for any pair of allowed \(A_0,A_1\). There are exactly \(c_b(n-b)^2\) such ordered pairs. Summing gives the second term. Pure and mixed factors are disjoint and exhaustive; the theorem follows.

For the final assertions, the classical all-ones composition bijection gives \(d_2(2^n-1)=\sum_{b=1}^n c_b(n-b)\). The difference between the theorem's count and twice this quantity is \(\sum_b c_b(n-b)(c_b(n-b)-1)\), nonnegative; it is positive as soon as \(n\ge4\) because \(b=n-2\) permits two compositions of \(2\) for \(n\ge4\). Finally \(W_{2,2}=15\), with five binary lunar divisors, while the formula gives four, demonstrating sharpness.

## Verification

The standalone `verify.py` computes the composition formula and independently enumerates all binary lunar divisors of small targets using their support subsets and the maximal admissible cofactor. It checks \(n\le6\) for several gaps \(h\ge3\), the seven initial predicted values, the \(h=2,n=2\) boundary, and the disjoint factor-count interpretation. Exact integer arithmetic is used. The verification is finite evidence; the full theorem is proved above.

## Relationship to prior work

Applegate, LeBrun and Sloane (2011), especially Theorem 12 and the discussion of bounded compositions in Section 6, establish \(d_2(2^n-1)=\sum_b c_b(n-b)\) and analyze distinct families of binary lunar numbers, including the one-hole runner-up \(2^n-3\). The present identity instead enumerates the two-residue periodic family \((1+X)Q_n(X^h)\) for every gap \(h\ge3\). The new ingredient is the residue-class obstruction forcing one pure-residue factor, and the consequent *square* of the bounded-composition counts. The classical repunit counting lemma alone does not assert this periodic-family enumeration. These comparisons do not establish absolute publication priority.

## Limitations

The statement concerns binary lunar arithmetic, not ordinary multiplication, and exactly two occupied residue classes within each block. The formula makes no claim of optimal divisor counts, or a uniform asymptotic expansion, for arbitrary binary strings. The proof is self-contained but not independently audited. Publication priority remains subject to fuller literature verification, especially potential specialized results on periodic Boolean-polynomial factorization.

## References

D. Applegate, M. LeBrun, and N. J. A. Sloane, *Dismal Arithmetic*, arXiv:1107.1130v1 (first submitted 2011-07-06), published in *Journal of Integer Sequences* 14 (2011), Article 11.9.8. Relevant material: Section 6, Theorems 12 and 14. https://arxiv.org/abs/1107.1130
