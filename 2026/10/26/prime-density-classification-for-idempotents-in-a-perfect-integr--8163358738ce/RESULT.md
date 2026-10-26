# Prime-density classification for idempotents in a perfect integral evolution-algebra family

## Finding

For an integer \(b\notin\{0,2\}\), let \(E_b\) be the free rank-two \(\mathbb Z\)-algebra with natural basis \(e_1,e_2\) and multiplication

\[
e_1^2=-b e_1+e_2,\qquad e_2^2=e_1,\qquad e_1e_2=0.
\]

Its structure matrix is \(A_b=\begin{pmatrix}-b&1\\1&0\end{pmatrix}\), so \(\det A_b=-1\). Thus every reduction \(E_{b,p}=E_b\otimes_{\mathbb Z}\mathbb F_p\) is perfect. Put \(f_b(T)=T^3-bT-1\) and \(\Delta_b=4b^3-27\). The nonzero idempotents of \(E_{b,p}\) are in bijection with the roots of \(f_b\) in \(\mathbb F_p\).

Because \(b\ne0,2\), the rational-root test shows that \(f_b\) is irreducible over \(\mathbb Q\). Its Galois group is \(C_3\) if \(\Delta_b\) is a square and \(S_3\) otherwise. Consequently, among primes unramified in its splitting field:

- If \(\Delta_b\) is a square, the natural densities of primes giving 3 and 0 nonzero idempotents are \(1/3\) and \(2/3\), respectively.
- If \(\Delta_b\) is not a square, the natural densities of primes giving 3, 1, and 0 nonzero idempotents are \(1/6\), \(1/2\), and \(1/3\), respectively.

In particular, the density of primes for which \(E_{b,p}\) has at least one nonzero idempotent is \(1/3\) in the square-discriminant case and \(2/3\) in the nonsquare-discriminant case. The examples \(b=3\) and \(b=1\) realize the two cases: their discriminants are \(81\) and \(-23\).

## Assumptions and scope

The coefficient ring is \(\mathbb Z\); the algebra is commutative and need not be associative. A natural basis means that distinct basis elements multiply to zero. The parameter \(b\) is an integer other than 0 and 2. We use primes \(p\nmid\Delta_b\), which are unramified for the polynomial \(f_b\); the excluded primes form a finite set and do not affect natural densities.

## Proof

Let \(u=xe_1+ye_2\) over a field. The multiplication rules give

\[
u^2=(y^2-bx^2)e_1+x^2e_2.
\]

Thus \(u^2=u\) is equivalent to \(x=y^2-bx^2\) and \(y=x^2\). Substitution gives

\[
x(x^3-bx-1)=0,\qquad y=x^2.
\]

Every nonzero idempotent therefore has \(x\ne0\) and determines a root \(x\) of \(f_b\); conversely every root \(r\) of \(f_b\) is nonzero because \(f_b(0)=-1\), and yields the idempotent \(re_1+r^2e_2\). This is a bijection, including in characteristics where roots may repeat as polynomial roots: distinct field roots correspond to distinct idempotents.

The determinant calculation \(\det A_b=-1\) is valid over \(\mathbb Z\) and remains nonzero in every \(\mathbb F_p\), proving perfectness after every reduction. The only possible rational roots of the monic cubic \(f_b\) are \(1\) and \(-1\); their values are \(-b\) and \(b-2\). Hence \(f_b\) is irreducible for \(b\notin\{0,2\}\). Its discriminant is \(\Delta_b=4b^3-27\), which is nonzero for integral \(b\). An irreducible separable cubic has Galois group \(C_3\) when its discriminant is a square and \(S_3\) otherwise.

For an unramified prime, the factorization degrees of \(f_b\) modulo that prime are the cycle lengths of its Frobenius element. A root exists precisely when Frobenius has a fixed point. In \(C_3\), only the identity has a fixed point, with density \(1/3\); the other two elements are 3-cycles. In \(S_3\), the identity, transpositions, and 3-cycles have respective proportions \(1/6\), \(1/2\), and \(1/3\), and give respectively 3, 1, and 0 roots. The Chebotarev density theorem gives the stated distributions. Removing ramified primes does not change any natural density.

## Verification

The determinant, idempotent equations, rational-root test, discriminant, and conjugacy-class proportions are explicit in the proof. The two example parameters satisfy all hypotheses: \(f_1(T)=T^3-T-1\) is irreducible with discriminant \(-23\), and \(f_3(T)=T^3-3T-1\) is irreducible with discriminant \(81\). No finite-prime enumeration is used as evidence for the density statement.

## Relationship to prior work

The recent survey by Kaygorodov, Martín González, and Viruel gives a cubic-root criterion for idempotents in dimension two and lists reduction modulo primes as an open question. The present result does not claim the root criterion or Chebotarev's theorem as new; it gives an explicit complete prime-density distribution for the natural integral family \(E_b\), including the distinction between the cyclic and symmetric cubic Galois groups. A related research result constructs some idempotent-free perfect two-dimensional evolution algebra over every finite field, but that existence statement does not determine the prime distribution for one fixed integral model or this parameter family.

## Limitations

This is a family-level result, not a classification of reductions of arbitrary integral evolution algebras. At primes dividing \(\Delta_b\), the reduced cubic may have repeated roots and the unramified Frobenius classification is not asserted; these primes form a finite set. Perfectness nevertheless holds at every prime because the structure determinant is \(-1\). The support graph can change at primes dividing \(b\), also a finite set, which does not affect the density conclusions.

## References

1. I. Kaygorodov, C. Martín González, and A. Viruel, “Evolution algebras: a survey of results and a list of open problems,” arXiv:2610.22248 (first public version 15 October 2026), especially §2.1.5 and Question 45 in §2.2.7.
2. A. González Nevado, “Order structures around evolution algebras,” arXiv:2505.01444, cited by the survey for a related rational example; the full preprint was not directly inspected in this run.
3. Chebotarev density theorem; see, for example, J.-P. Serre, *Topics in Galois Theory*, 2nd ed., A K Peters/CRC Press, 2008.
