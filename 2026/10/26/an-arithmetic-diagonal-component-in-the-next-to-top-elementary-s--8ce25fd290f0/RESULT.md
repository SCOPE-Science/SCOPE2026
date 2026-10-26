# An arithmetic diagonal component in the next-to-top elementary-symmetric derivative locus

## Finding
Let \(K\) be algebraically closed of characteristic \(p>0\). For integers \(n\ge d\ge4\), write \(e_d=e_d(x_1,\ldots,x_n)\) for the degree-\(d\) elementary symmetric polynomial, and let \(C_{d-2}(e_d)\) be the closed scheme defined by all its order-\(d-2\) squarefree derivatives. Put
\[
 k=n-d+2,\qquad Q=p^{v_p(k-1)}.
\]
Set \(A_i=K e_i\), \(D=K(1,\ldots,1)\) and \(P_i=D+K e_i\) in \(K^n\). The irreducible components of the **underlying reduced variety** are exactly
\[
 (C_{d-2}(e_d))_{\mathrm{red}}=
 \begin{cases}
 \displaystyle\bigcup_{i=1}^n P_i,&Q>2,\\[3pt]
 \displaystyle\bigcup_{i=1}^n A_i\;\cup\;\begin{cases}D,&p\mid\binom{k}{2},\\\varnothing,&p\nmid\binom{k}{2},\end{cases}&Q\le2.
 \end{cases}
\]
For \(Q\le2\), the extra diagonal line occurs if and only if \(p\) is odd with \(p\mid k\), or \(p=2\) with \(4\mid k\). Thus the projectivization has \(n+1\), rather than \(n\), isolated points in these cases, despite the same dimension. When \(Q>2\), its projectivization is an arrangement of \(n\) lines through the diagonal point.

## Assumptions and scope
All derivative ideals are over an algebraically closed field of prime characteristic, with \(n\ge d\ge4\). The assertion concerns the reduced underlying variety and its complete irreducible-component list, not the defining ideal's primary decomposition, multiplicities or embedded components. Every order-\(d-2\) squarefree derivative is the elementary symmetric quadratic \(e_2\) on a complementary \(k\)-subset of indices. Differentiating a variable twice vanishes by multilinearity.

## Proof
**At most two coordinate values.** Put \(q=d-2\ge2\). Suppose a common zero has three coordinates with distinct values. Since \(n\ge d=q+2\), choose \(q-1\) indices avoiding those three. Differentiating \(e_d\) at these indices gives an elementary symmetric cubic in the remaining variables. All its first derivatives vanish, by the assumed order-\(q\) equations. If \(E_1,E_2\) are the elementary symmetric forms of degrees one and two in those remaining variables, then the first derivative obtained by deleting a variable with value \(z\) equals \(E_2-zE_1+z^2\). Thus three distinct coordinate values are roots of the same monic quadratic, an impossibility over any field.

**No two large value-blocks.** Suppose two distinct values \(a,b\) appear with multiplicities \(s,t\ge2\), where \(s+t=n\). For any allowed integer \(j\), the \(e_2\)-equation on a \(k\)-subset with exactly \(j\) occurrences of \(a\) reads
\[
 F(j)=\binom{k}{2}b^2+j(k-1)b(a-b)+\binom{j}{2}(a-b)^2=0.
\]
The feasible \(j\)'s comprise every integer between \(\max(0,k-t)\) and \(\min(k,s)\). Because \(s,t,k,n-k\ge2\), this interval contains three consecutive integers. Its second finite difference is exactly \((a-b)^2\), which is nonzero. This contradiction is characteristic-independent.

**One exceptional coordinate.** Every nonconstant common zero therefore has a single coordinate \(a\) and \(n-1\) equal coordinates \(b\), with \(a\ne b\). Both types of \(k\)-subset exist because \(2\le k\le n-2\). Their two equations are
\[
 \binom{k}{2}b^2=0,\qquad
 \binom{k}{2}b^2+(k-1)b(a-b)=0.
\]
If \(b=0\), the point lies on the coordinate axis \(A_i\), and conversely every such axis satisfies every quadratic equation. If \(b\ne0\), these equations, with \(a\ne b\), are equivalent to \(p\mid(k-1)\) and \(p\mid\binom{k}{2}\). For odd \(p\) that is equivalent to \(p\mid(k-1)\), while for \(p=2\) it is equivalent to \(4\mid(k-1)\). In either characteristic it is equivalent to \(Q>2\). Hence exactly in this regime, \(a\) and \(b\) may vary independently, yielding the whole plane \(P_i\).

**Equal coordinates and exhaustiveness.** A point with every coordinate equal to \(b\) satisfies every equation exactly when \(\binom{k}{2}b^2=0\). A nonzero such point exists precisely when \(p\mid\binom{k}{2}\), giving the diagonal \(D\). If \(Q>2\), \(D\) is contained in every \(P_i\). Otherwise it is an extra component, not contained in any \(A_i\). For \(Q\le2\), the binomial divisibility is equivalent to \(p\mid k\) for odd \(p\) and to \(4\mid k\) for \(p=2\). The preceding alternatives exhaust all points, and the displayed distinct linear spaces have equal dimension within each case and contain one another only as explicitly indicated. They are therefore exactly the irreducible components.

## Verification
The standalone `VERIFY.py` uses exact arithmetic over prime finite fields. It compares the full system of \(\binom nk\) quadratic equations with the predicted union on every point of \(\mathbb F_p^n\), for \(p=2\) and \(4\le n\le8\), \(p=3\) and \(4\le n\le6\), and \(p=5\) and \(4\le n\le5\), always for \(4\le d\le n\). It returns `VERIFY_OK`. Finite checks supplement but do not replace the general proof above.

## Relationship to prior work
Ying Xie's *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1 (first public 2026-09-24), establishes general derivative-locus dimensions and the maximal-dimensional (extremal) components. Its Theorem 1.3 already identifies the planes \(P_i\) when \(Q>2\) (the higher-dimensional regime); that case is included here only to state a complete classification. Its Theorem 1.4 describes local rings at coordinate components, but it does not list all components in the lower-dimensional regime, and Section 7 explicitly leaves the smaller-dimensional component classification open. The additional diagonal line and the proof that there are no other lower-dimensional components are the contribution here. Ian Orzel's arXiv:2509.05009v3 studies the order-two zero space defined by the polynomial and first derivatives, rather than this next-to-top derivative locus. No priority claim about general dimension formulas, generic multiplicities, or the known extremal planes is made.

## Limitations
This result is set-theoretic: neither reducedness of the derivative ideal nor absence of embedded primes is asserted. The argument requires \(d\ge4\) and algebraic closure, and it does not settle component classifications for other derivative orders. No independent assessment of novelty or verification has been performed; an unindexed earlier calculation of the quadratic deletion ideal remains possible.

## References
1. Y. Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1, 2026-09-24, https://arxiv.org/html/2610.00259v1.
2. I. Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009v3, https://arxiv.org/html/2509.05009v3.
3. A. Cafure, G. Matera and M. Privitelli, *Singularities of symmetric hypersurfaces and Reed--Solomon codes*, Adv. Math. Commun. 6 (2012), 69--94, arXiv:1109.2265.
